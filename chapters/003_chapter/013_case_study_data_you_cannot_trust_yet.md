## 3.12 Caso end-to-end — Il ritardo che esisteva, ma non quanto sembrava

> **Caso simulato/composito.** Azienda, persone e numeri sono costruiti a fini didattici, combinando problemi realistici di sistemi transazionali ed event data.

**ProntoVeloce** gestisce consegne last-mile per ristoranti e piccoli retailer in quattro Paesi europei.

Il lunedì mattina il COO apre la dashboard operativa e vede un peggioramento netto:

```text
Late delivery rate
mese precedente: 11,8%
mese corrente:   17,6%
```

La definizione dichiarata è semplice:

> percentuale di consegne completate oltre 45 minuti dalla conferma dell'ordine.

Un aumento di quasi sei punti percentuali potrebbe giustificare interventi su courier capacity, incentivi, routing e SLA con i partner.

Prima di cercare la causa, però, l'analista deve stabilire se il **17,6%** rappresenta davvero il fenomeno.

### 1. Qual è il grain?

La dashboard usa tre dataset principali:

```text
orders
restaurants
delivery_events
```

`orders` contiene apparentemente una riga per ordine.

`delivery_events` contiene invece una riga per **evento di stato**:

```text
order_id | event_type         | event_time
A4102    | order_confirmed    | 19:02
A4102    | courier_assigned   | 19:07
A4102    | picked_up          | 19:31
A4102    | delivered          | 19:48
```

La prima query usata da un report ad hoc aveva collegato `orders` e `delivery_events` senza ridurre gli eventi a livello ordine.

La conseguenza era una moltiplicazione delle righe.

Il problema non rende automaticamente sbagliato il late delivery rate della dashboard ufficiale, ma è il primo segnale: **le sorgenti non possono essere usate senza dichiarare il grain**.

### 2. `order_id` non è globale

La documentazione interna dice che `order_id` identifica un ordine.

Il profiling mostra però collisioni apparentemente impossibili: lo stesso identificatore compare con due ristoranti e due valute differenti.

La spiegazione arriva dal team applicativo: ogni Paese genera la propria sequenza di ID.

La vera chiave è:

```text
(country_code, order_id)
```

Una pipeline introdotta tre settimane prima aveva collegato alcuni eventi soltanto su `order_id`.

Una piccola quota di consegne aveva quindi ricevuto eventi provenienti da ordini di un altro Paese.

Il join era tecnicamente valido.

L'identità dell'ordine era sbagliata.

### 3. Il timestamp di consegna ha cambiato significato

Fino a metà mese `delivered_at` veniva derivato dall'evento emesso dall'app del courier al momento della consegna.

Dopo una release, per alcuni ordini il campo viene valorizzato dal back office quando il sistema sincronizza lo stato finale.

Per courier con connettività debole possono trascorrere diversi minuti tra consegna reale e sincronizzazione.

Il nome della colonna è rimasto lo stesso.

La semantica è cambiata.

Quando l'analista confronta `event_time` e `ingested_at`, nota che il divario è concentrato proprio nelle settimane in cui il KPI peggiora.

### 4. Il missing non è casuale

L'**8,7%** degli ordini completati non ha un evento `delivered` utilizzabile entro la finestra di elaborazione della dashboard.

Non sono distribuiti uniformemente.

Il missing raggiunge il **21,4%** per una versione precedente dell'app courier e meno del 2% per la versione nuova.

Una procedura di fallback usa `closed_at` del back office come timestamp di consegna.

Questo tende a produrre durate maggiori proprio per il gruppo con più missing.

Quindi il problema non è semplicemente "ci mancano alcune date".

Il meccanismo di missingness è collegato alla misura che stiamo cercando di calcolare.

### 5. Il denominatore è cambiato

Il late delivery rate dovrebbe essere calcolato sulle **consegne effettivamente completate**.

Dopo una modifica al modello semantico, però, il denominatore include anche ordini cancellati dopo l'assegnazione del courier.

Alcuni di questi record ricevono una durata artificiale fino alla chiusura amministrativa e finiscono tra i "late".

Il KPI sta quindi mescolando due fenomeni:

- ritardo della consegna;
- cancellazione del processo.

Separarli è una decisione semantica, non un dettaglio di SQL.

### 6. Gli outlier raccontano due storie diverse

La distribuzione di `delivery_minutes` contiene valori come:

```text
-12
38
51
94
861
```

`-12` è impossibile: deriva da un problema di timezone tra due eventi.

`861` — oltre 14 ore — sembra anch'esso un errore, ma l'indagine mostra che alcuni ordini corporate vengono davvero programmati molte ore prima della finestra di consegna.

Il record è reale. È la **definizione di durata** a non essere appropriata per quel tipo di ordine.

La soluzione non è tagliare tutti gli outlier. È escludere dal KPI operativo le consegne programmate secondo una regola business documentata.

### 7. Riconciliare con una fonte indipendente

L'analista costruisce una riconciliazione tra:

- eventi dell'app courier;
- stato finale dell'ordine;
- sistema di billing, che paga il courier solo per consegne completate;
- log del partner di routing.

Il confronto rende visibili quattro correzioni principali:

| Correzione | Effetto sul late delivery rate apparente |
|---|---:|
| join con chiave incompleta | -1,1 pp |
| cancellazioni nel denominatore | -1,3 pp |
| fallback `closed_at` | -1,0 pp |
| ordini programmati fuori perimetro | -0,8 pp |

Le componenti non devono essere sommate ingenuamente come se fossero indipendenti; alcune righe ricadono in più categorie. Dopo la ricostruzione ordine per ordine, il KPI diventa:

```text
mese precedente: 11,9%
mese corrente:   13,4%
```

Il peggioramento **esiste ancora**.

Ma non è +5,8 punti percentuali. È circa +1,5 punti.

Questa differenza cambia la decisione.

### 8. Solo adesso inizia la diagnosi del business

Una volta stabilito un dataset sufficientemente coerente, l'analista segmenta la durata nelle sue componenti:

```text
conferma → assegnazione courier
assegnazione → pickup
pickup → consegna
```

Il principale deterioramento non emerge nell'ultimo tratto di routing, come ipotizzato inizialmente.

È concentrato nel tempo **conferma → pickup** per un gruppo di ristoranti entrati recentemente nella piattaforma.

Il tempo mediano di preparazione stimato passa da circa 18 a 24 minuti.

Questa osservazione non dimostra ancora che l'onboarding dei ristoranti abbia causato il peggioramento. Ma restringe la prossima indagine e impedisce di spendere subito budget aggiuntivo sui courier.

### 9. Il verdetto di data readiness

L'analista non dichiara il dataset "pulito".

Documenta invece:

**Pronto per:**

- confronto mensile del late delivery rate;
- segmentazione per Paese, ristorante e tipologia ordine;
- analisi delle componenti della durata.

**Con caveat:**

- ultime 24 ore, perché una quota di eventi arriva in ritardo;
- confronti precedenti alla migrazione, che richiedono una regola temporale coerente;
- courier su vecchia app, per cui la completezza del timestamp è inferiore.

**Non pronto per:**

- SLA in tempo reale per singolo courier, finché il problema di sincronizzazione non viene corretto.

Questa è una conclusione molto più utile di "data quality buona/cattiva".

### La lezione

La richiesta iniziale era:

> "Perché le consegne in ritardo sono esplose?"

Prima di rispondere sono servite domande meno spettacolari:

- una riga rappresenta un ordine o un evento?
- qual è la vera chiave?
- quale timestamp misura la consegna?
- perché mancano alcuni eventi?
- chi entra nel denominatore?
- quali outlier sono errori e quali casi reali?
- il dato si riconcilia con una fonte indipendente?

Solo dopo possiamo discutere il business.

> **Capire i dati non è una fase preliminare da superare il più velocemente possibile. È il lavoro con cui costruiamo il confine tra ciò che il dataset mostra e ciò che siamo autorizzati a concludere.**