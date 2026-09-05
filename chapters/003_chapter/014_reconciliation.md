## 3.13 Riconciliazione: spiegare la differenza prima di scegliere il numero

Nel lavoro reale capita spesso che due sistemi mostrino valori diversi per una metrica che porta lo stesso nome. La reazione più pericolosa è scegliere subito quale dashboard “ha ragione”, perché la divergenza può nascere prima del codice: definizione, popolazione, tempo, grain, stati e unità possono essere diversi pur lasciando invariato il nome della metrica.

La **riconciliazione** serve a trasformare quella differenza in una spiegazione verificabile.

### Caso simulato/composito — Il fatturato che non coincide

Una società retail riceve due report mensili:

```text
ERP / Finance:        €1.842.310
Dashboard Sales:      €1.917.480
Differenza:              €75.170
```

Il delta è circa il **4,1%**. Invece di partire dalle query, l'analista confronta le definizioni.

Finance riconosce il ricavo alla data di spedizione, mentre Sales lo attribuisce alla data dell'ordine. Finance esclude gli ordini annullati prima della spedizione; Sales li rimuove quando riceve l'aggiornamento di stato. Sales include un contributo di spedizione che Finance classifica separatamente, e alcune note di credito del mese precedente vengono registrate contabilmente nel mese corrente.

A questo punto il problema cambia natura. I due numeri non sono semplicemente due implementazioni concorrenti della stessa metrica: rappresentano **due viste differenti del fenomeno**.

## La reconciliation bridge rende il delta intelligibile

Un modo efficace di lavorare consiste nel partire da un totale e spiegare, voce per voce, come arrivare all'altro:

| Voce | Impatto |
|---|---:|
| Totale Sales | €1.917.480 |
| Ordini non ancora spediti | -€31.800 |
| Contributi di spedizione | -€19.420 |
| Cancellazioni non ancora recepite | -€8.650 |
| Note di credito / resi | -€15.300 |
| Totale Finance | €1.842.310 |

La tabella non elimina la differenza: la **spiega**. In casi reali le componenti possono interagire e il ponte può richiedere una ricostruzione record per record, ma il principio resta lo stesso.

Quando due metriche non coincidono, l'ordine di investigazione dovrebbe seguire la semantica prima dell'implementazione. Prima verifichiamo se significano la stessa cosa; poi se includono la stessa popolazione, usano lo stesso timestamp, aggregano allo stesso grain, trattano allo stesso modo cancellazioni e rettifiche, condividono unità e valuta, fotografano lo stesso momento e applicano trasformazioni comparabili.

Questo ordine evita di passare ore su una query quando la divergenza è già spiegata da una regola di riconoscimento diversa.

## Riconciliare non significa imporre un solo numero

La riconciliazione può concludere che le metriche debbano restare diverse. `ordered_revenue` può essere corretta per il monitoraggio commerciale mentre `recognized_revenue` è quella appropriata per la contabilità. Forzare entrambe dentro un'unica definizione renderebbe meno utile ciascun processo.

L'obiettivo è impedire che due numeri con significati diversi vengano presentati come se misurassero la stessa cosa.

Anche la materialità conta. Una discrepanza dello 0,02% dovuta ad arrotondamenti può essere irrilevante per una decisione strategica e inaccettabile in un processo regolato. Per questo la riconciliazione dovrebbe dichiarare quale fonte è autorevole per quale uso, quale tolleranza è accettabile, quali differenze sono attese e quali richiedono escalation.

Un buon output finale non dice soltanto “i dati tornano”. Dice, per esempio:

> La dashboard Sales supera Finance di €75.170. La differenza è interamente spiegata da timing di riconoscimento, shipping fees, cancellazioni e note di credito; non emerge una perdita di record non spiegata.

oppure:

> Rimangono €18.400 non riconciliati, concentrati sugli ordini marketplace. Finché il delta non viene spiegato, il dato non è pronto per il consuntivo.

La riconciliazione chiude così il circuito fra semantica, lineage e readiness.

> **Se due sistemi mostrano numeri diversi, la prima responsabilità dell'analista non è scegliere un vincitore. È rendere la differenza intelligibile e stabilire quale numero è autorevole per quale decisione.**
