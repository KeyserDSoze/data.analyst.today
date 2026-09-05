## 3.12 Caso end-to-end — Il ritardo che esisteva, ma non quanto sembrava

> **Caso simulato/composito.** Azienda, persone e numeri sono costruiti a fini didattici, combinando problemi realistici di sistemi transazionali ed event data.

ProntoVeloce gestisce consegne last-mile per ristoranti e piccoli retailer in quattro Paesi europei. Il lunedì mattina il COO apre la dashboard operativa e vede un peggioramento netto:

```text
Late delivery rate
mese precedente: 11,8%
mese corrente:   17,6%
```

La definizione dichiarata sembra semplice: percentuale di consegne completate oltre 45 minuti dalla conferma dell'ordine. Un aumento di quasi sei punti percentuali potrebbe giustificare interventi su courier capacity, incentivi, routing e SLA con i partner.

Il team potrebbe partire subito alla ricerca di una causa operativa. L'analista fa invece una scelta meno spettacolare e più importante: prima di spiegare il **17,6%**, deve capire se quel numero rappresenta davvero il fenomeno.

## La prima crepa: il dataset non ha un solo grain

La dashboard usa `orders`, `restaurants` e `delivery_events`. `orders` sembra contenere una riga per ordine; `delivery_events`, invece, registra una riga per evento di stato:

```text
order_id | event_type         | event_time
A4102    | order_confirmed    | 19:02
A4102    | courier_assigned   | 19:07
A4102    | picked_up          | 19:31
A4102    | delivered          | 19:48
```

Una query ad hoc aveva collegato ordini ed eventi senza prima ridurre gli eventi al livello ordine, moltiplicando le righe. Il late delivery rate della dashboard ufficiale non è ancora dimostrato sbagliato, ma il controllo cambia l'atteggiamento dell'analista: le sorgenti non possono essere trattate come tabelle intercambiabili. Prima va dichiarato il grain di ciascuna.

Mentre verifica le cardinalità emerge una seconda anomalia. `order_id`, descritto internamente come identificatore dell'ordine, compare con due ristoranti e due valute diverse. Il team applicativo spiega che ogni Paese genera la propria sequenza di ID. La vera chiave è:

```text
(country_code, order_id)
```

Tre settimane prima una pipeline aveva iniziato a collegare alcuni eventi soltanto su `order_id`. Il join era tecnicamente valido; l'identità dell'ordine era sbagliata. Una piccola quota di consegne aveva ricevuto eventi appartenenti a ordini di un altro Paese.

La prima ipotesi di business — “abbiamo un problema di courier capacity” — è già prematura. Il sistema di misura sta introducendo rumore prima ancora che il processo operativo venga analizzato.

## Il timestamp non misura più la stessa cosa

La ricostruzione del tempo introduce una terza svolta. Fino a metà mese `delivered_at` veniva derivato dall'evento emesso dall'app del courier al momento della consegna. Dopo una release, per alcuni ordini il campo viene valorizzato dal back office quando lo stato finale viene sincronizzato.

Il nome della colonna è rimasto invariato. La semantica no.

Per courier con connettività debole possono passare diversi minuti tra consegna reale e sincronizzazione. Confrontando `event_time` e `ingested_at`, l'analista vede che il ritardo cresce proprio nelle settimane in cui il KPI peggiora. Il dataset non sta soltanto osservando consegne più lente; in parte sta misurando una latenza diversa.

Il problema si complica perché l'**8,7%** degli ordini completati non possiede un evento `delivered` utilizzabile entro la finestra di elaborazione. Il missing raggiunge il **21,4%** sulla versione precedente dell'app courier e resta sotto il 2% sulla versione nuova. Una procedura di fallback utilizza `closed_at` del back office come timestamp di consegna, producendo durate più elevate proprio nel gruppo con più missing.

Il valore assente non è quindi casuale. Il meccanismo che produce il missing è collegato alla misura che stiamo cercando di calcolare.

## Anche il denominatore è cambiato

Il late delivery rate dovrebbe riguardare le consegne effettivamente completate. Una modifica al modello semantico ha però incluso nel denominatore anche ordini cancellati dopo l'assegnazione del courier. Alcuni di questi record ricevono una durata artificiale fino alla chiusura amministrativa e finiscono tra i “late”.

Il KPI sta così mescolando due fenomeni diversi: ritardo di consegna e cancellazione del processo. Separarli non è una correzione cosmetica di SQL; è una decisione sulla popolazione che la metrica pretende di rappresentare.

Anche gli outlier confermano che la pulizia automatica sarebbe pericolosa. `delivery_minutes` contiene valori come:

```text
-12
38
51
94
861
```

`-12` è impossibile e deriva da un problema di timezone. `861`, oltre quattordici ore, sembra altrettanto assurdo finché il team non scopre che alcuni ordini corporate vengono programmati molte ore prima della finestra di consegna. Il record è reale; è la definizione del KPI a essere inadatta a quel tipo di ordine. La soluzione corretta è escludere le consegne programmate secondo una regola di business documentata, non tagliare tutti i valori estremi.

## La riconciliazione ricostruisce il KPI

A questo punto l'analista confronta quattro prospettive indipendenti: eventi dell'app courier, stato finale dell'ordine, sistema di billing — che paga il courier solo per consegne completate — e log del partner di routing.

Il confronto rende visibili quattro correzioni principali:

| Correzione | Effetto sul late delivery rate apparente |
|---|---:|
| join con chiave incompleta | -1,1 pp |
| cancellazioni nel denominatore | -1,3 pp |
| fallback `closed_at` | -1,0 pp |
| ordini programmati fuori perimetro | -0,8 pp |

Questi contributi non possono essere sommati ingenuamente perché alcune righe ricadono in più categorie. Ricostruendo il KPI ordine per ordine, il risultato diventa:

```text
mese precedente: 11,9%
mese corrente:   13,4%
```

Il peggioramento **esiste ancora**, ma non è più +5,8 punti percentuali: è circa **+1,5 punti**.

Questa nuova informazione cambia la decisione. Un deterioramento reale rimane, quindi non possiamo archiviare il problema come semplice errore di pipeline. Ma la scala del fenomeno non giustifica più, da sola, un intervento urgente e generalizzato sulla capacità dei courier.

## Solo adesso inizia la diagnosi del business

Con un dataset ricostruito e un perimetro coerente, l'analista scompone la durata:

```text
conferma → assegnazione courier
assegnazione → pickup
pickup → consegna
```

Il deterioramento principale non emerge nell'ultimo tratto di routing, come ipotizzato inizialmente. Si concentra nel tempo **conferma → pickup** per un gruppo di ristoranti entrati recentemente nella piattaforma. Il tempo mediano di preparazione stimato passa da circa **18 a 24 minuti**.

Questa osservazione non dimostra che l'onboarding dei ristoranti abbia causato il peggioramento. Ma restringe il problema e cambia il prossimo investimento investigativo: prima di aggiungere budget ai courier, conviene capire che cosa sta succedendo nella preparazione degli ordini dei nuovi partner.

## Il verdetto non è “dataset pulito”

La Data Readiness Review produce un risultato più utile di un giudizio binario.

Il dato è **pronto** per il confronto mensile del late delivery rate, per segmentazioni per Paese, ristorante e tipologia ordine e per l'analisi delle componenti della durata. È **pronto con caveat** sulle ultime 24 ore, perché una quota di eventi arriva tardi; sui confronti precedenti alla migrazione, che richiedono una regola temporale coerente; e sui courier con vecchia app, dove la completezza del timestamp è inferiore. È invece **non pronto** per SLA in tempo reale sul singolo courier finché il problema di sincronizzazione non viene corretto.

La richiesta iniziale era “perché le consegne in ritardo sono esplose?”. Il lavoro effettivo è stato diverso: capire quale riga rappresentasse l'ordine, quale chiave lo identificasse davvero, quale timestamp misurasse la consegna, perché alcuni eventi mancassero, chi entrasse nel denominatore, quali outlier fossero errori e quali casi reali, e infine se il KPI si riconciliasse con fonti indipendenti.

Solo dopo questa catena l'analisi ha guadagnato il diritto di parlare del business.

> **Capire i dati non è una fase preliminare da superare in fretta. È il lavoro con cui costruiamo il confine tra ciò che il dataset mostra e ciò che siamo autorizzati a concludere.**
