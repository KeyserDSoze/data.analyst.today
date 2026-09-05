## 4.19 Caso end-to-end — Una crescita vera, ma molto meno semplice di quanto sembra

> **Caso simulato/composito.** Azienda, numeri e circostanze sono costruiti a fini didattici.

Il management di **MercatoHub**, marketplace europeo di elettronica ricondizionata, riceve il report del secondo trimestre. I quattro numeri in apertura sono tutti positivi: **GMV +18,7% YoY**, **ordini +12,1%**, **average order value +5,9%**, **clienti attivi +9,4%**.

La prima slide preparata per il management titola:

> **La crescita sta accelerando.**

La headline non contiene un errore aritmetico. Contiene però un'interpretazione molto più ricca dei quattro KPI: suggerisce una crescita ampia, strutturale e sufficientemente sana da poter giustificare nuovi investimenti. È esattamente il tipo di salto che l'EDA deve stressare.

La domanda diventa quindi:

> **La crescita è diffusa, robusta e accompagnata da segnali operativi coerenti, oppure è concentrata in pochi driver?**

Il dataset arriva dal Capitolo 3 con una Data Readiness Review completata: grain, chiavi, duplicati, resi e copertura temporale sono già stati verificati. Rimane un caveat noto: `active_customer` ha cambiato significato con il lancio della nuova app. Questo confine è importante perché non stiamo rifacendo la data-quality review; stiamo usando una conoscenza già acquisita per evitare di interpretare male una metrica.

## La distribuzione indebolisce la prima generalizzazione

L'AOV passa da **€286 a €303**. La media conferma che il valore economico per ordine è salito, ma la distribuzione mostra che il movimento non è uniforme: `P50` passa soltanto da **€231 a €234**, mentre `P90` cresce da **€612 a €735**.

Il cliente al centro della distribuzione spende quasi quanto l'anno precedente. L'aumento medio è quindi sostenuto soprattutto dagli ordini di fascia alta. La frase “gli ordini valgono di più” diventa una descrizione più precisa: **è aumentato soprattutto il peso degli ordini ad alto valore**.

La decomposizione per categoria localizza immediatamente questa coda:

| Categoria | GMV YoY |
|---|---:|
| Smartphone | +6% |
| Laptop | +11% |
| Tablet | +4% |
| Fotografia | +9% |
| Gaming GPU | +71% |

Gaming GPU genera il **46% dell'incremento assoluto di GMV** pur rappresentando meno del 15% del business nel periodo precedente. La crescita complessiva è reale, ma una parte molto grande dell'accelerazione vive in una sola categoria.

## Anche la crescita clienti dipende da una definizione

Il +9,4% di `active_customer` sembra confermare che la crescita sia sostenuta da una base clienti più ampia. Ma con la nuova app è diventato necessario autenticarsi anche per salvare un prodotto nei preferiti. La metrica storica, che definisce attivo chi ha almeno una visita autenticata negli ultimi 90 giorni, incorpora quindi un cambiamento dell'interfaccia.

Quando l'analista usa `unique_buyers`, definito in modo coerente su entrambi gli anni, la crescita è **+4,1%**. Entrambi i numeri sono veri: utenti autenticati attivi +9,4%, persone o account che hanno acquistato +4,1%. Solo il secondo, però, risponde direttamente alla domanda su quanto si sia ampliata la base degli acquirenti.

Questo cambia il rapporto tra le componenti della crescita. Il GMV sale molto più rapidamente degli acquirenti unici: una parte rilevante dell'espansione viene quindi da valore e mix degli ordini, non semplicemente da più clienti.

## Categoria e seller raccontano la stessa concentrazione da due lati

MercatoHub ha 1.840 seller attivi. La mediana del GMV per seller è quasi invariata, mentre il top 5% cresce del **38%**. I seller maggiori sono proprio quelli più esposti a GPU e hardware premium.

A questo punto due strutture si sovrappongono: la crescita è concentrata per categoria e per seller. Non significa che la concentrazione sia necessariamente negativa; significa che la headline “la crescita sta accelerando” nasconde **da dove** quell'accelerazione provenga e quanto potrebbe dipendere dalla tenuta di un gruppo relativamente ristretto di prodotti e operatori.

## Un denominatore incoerente trasformava anche il post-vendita in una buona notizia

Il vecchio report mostra `return rate = 7,8%`; la nuova dashboard `7,1%`. Sembrerebbe un ulteriore segnale di crescita sana. Le due serie, però, usano denominatori differenti: lo storico misura **ordini con almeno un reso / ordini consegnati**, il nuovo **unità restituite / unità spedite**.

Sono metriche legittime ma non comparabili. Ricostruendo entrambi i periodi con la stessa definizione a livello ordine, il risultato diventa:

```text
anno precedente: 7,8%
anno corrente:    8,3%
Gaming GPU:       11,2% → 12,8%
```

La storia cambia ancora. La categoria che traina gran parte dell'accelerazione mostra anche un'esperienza post-vendita più problematica. L'EDA non ha dimostrato che la categoria “causi” il peggioramento complessivo né che i resi rendano la crescita non profittevole; ha identificato un guardrail che la headline iniziale non conteneva.

## La crescita sopravvive anche quando stressiamo i giorni eccezionali

Tre giornate hanno GMV eccezionalmente alto e coincidono con il lancio di una GPU molto richiesta. Sono eventi commerciali reali, non outlier da cancellare. La domanda è quanto influenzino la conclusione.

La sensitivity analysis produce:

```text
GMV YoY con tutti i giorni:             +18,7%
GMV YoY senza i tre principali launch: +12,6%
```

La crescita resta forte. Quindi la headline non dipende interamente da tre giornate. Allo stesso tempo, circa un terzo dell'accelerazione rispetto alla crescita “core” è associato a un evento molto concentrato. La robustezza non elimina la concentrazione; la quantifica.

## L'EDA Evidence Map ricompone il caso

A questo punto l'analista può separare ciò che è osservato dalle interpretazioni che restano aperte:

| Livello | Evidenza |
|---|---|
| **Osservato** | GMV +18,7%; ordini +12,1%; unique buyers +4,1%. |
| **Struttura** | Crescita fortemente concentrata su GPU, ordini high-value e top seller. |
| **Robustezza** | Senza tre launch days il GMV resta +12,6% YoY. |
| **Segnale operativo** | Return rate coerentemente definito peggiora 7,8% → 8,3%; GPU 11,2% → 12,8%. |
| **Ipotesi** | Nuova domanda GPU, mix premium e concentrazione seller possono spiegare gran parte dell'accelerazione. |
| **Non dimostrato** | Che il marketing abbia causato la crescita; che il boom GPU sia persistente; che la maggiore concentrazione sia economicamente negativa. |
| **Prossimo passo** | Analizzare contribution margin, repeat buyers, acquisizione per canale e persistenza delle coorti GPU. |

La headline iniziale può quindi essere sostituita da una conclusione più lunga ma molto più difendibile:

> **Il GMV cresce del 18,7% YoY e la crescita resta solida (+12,6%) anche escludendo i tre principali giorni di lancio. L'accelerazione è però concentrata nella categoria Gaming GPU, negli ordini di fascia alta e nei seller maggiori. Gli acquirenti unici crescono del 4,1%, molto meno della precedente metrica di “active customer”. Inoltre, usando una definizione comparabile, il return rate peggiora dal 7,8% all'8,3%. La crescita è quindi reale, ma meno diffusa e accompagnata da rischi di concentrazione e post-vendita che richiedono analisi ulteriori prima di aumentare indiscriminatamente gli investimenti.**

Il management non approva automaticamente un aumento generalizzato del budget marketing del 25%. Decide invece di separare nei report la crescita core dal contributo delle categorie ad alta volatilità, monitorare concentrazione seller, contribution margin e return rate della GPU, usare `unique_buyers` come metrica stabile della base acquirenti e verificare nei mesi successivi persistenza, repeat purchase e margine. Eventuali attribuzioni a specifici canali marketing verranno testate con disegni più forti.

Il valore dell'EDA non è stato trovare una versione più pessimista della storia. È stato trasformare **un aggregato corretto** in una descrizione della struttura abbastanza precisa da capire quali rischi monitorare e quali spiegazioni meritino il prossimo investimento analitico.

> **Una buona EDA non distrugge la headline iniziale per principio. La sottopone a abbastanza attrito da scoprire quale parte meriti davvero di sopravvivere.**
