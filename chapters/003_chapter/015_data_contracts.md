## 3.14 Data contract: quando una scoperta deve diventare un'aspettativa condivisa

Finora abbiamo guardato il dato soprattutto dal punto di vista di chi lo consuma: riceviamo una fonte, ne ricostruiamo grain, identità, tempo e qualità e decidiamo se può sostenere l'analisi. Ma alcuni problemi, una volta scoperti, non dovrebbero essere investigati di nuovo da zero ogni volta.

Se una chiave deve essere unica, se un evento ha una definizione precisa, se un campo critico non può cambiare unità o se una semantica richiede un review prima di essere modificata, quella conoscenza può diventare un **data contract**.

Il valore del contract non dipende dal formato tecnico. Dal punto di vista dell'analista, il principio è questo:

> **Chi produce un dato e chi lo usa condividono una definizione verificabile delle proprietà che non possono cambiare silenziosamente.**

Queste proprietà possono riguardare significato del dataset, grain, chiavi, campi obbligatori, tipi, unità, domini, nullability, frequenza, latenza, owner e gestione delle modifiche incompatibili. La progettazione e la governance più ampia arriveranno nei Capitoli 12 e 18; qui ci interessa il momento in cui una conoscenza emersa dall'indagine merita di smettere di essere locale.

### Caso simulato/composito — Il conversion rate che crolla senza che le vendite cambino

Un marketplace monitora il checkout conversion rate. Un lunedì il KPI passa dal **3,8% al 2,9%**, mentre le vendite assolute restano quasi stabili.

Il primo controllo cade sul denominatore: gli eventi `checkout_started` sono aumentati del **31%**. Il team frontend spiega che una release ha cambiato il punto in cui l'evento viene emesso. Prima scattava quando l'utente entrava esplicitamente nel primo step del checkout; dopo la release viene emesso già all'apertura automatica del drawer del carrello.

Il nome dell'evento non è cambiato. La pipeline non è fallita. Il campo è valido. È cambiato il **fenomeno misurato**.

Il problema non dovrebbe essere risolto soltanto correggendo la dashboard. La nuova conoscenza deve diventare una protezione per il futuro:

```text
Event: checkout_started
Definition: emitted once when the user explicitly enters checkout step 1
Grain: one event per checkout attempt
Required fields: session_id, timestamp, cart_value
Owner: Checkout Product Team
Semantic changes: analytics review required before production
```

Il contratto rende visibile la dipendenza prima che una modifica di prodotto diventi una falsa storia nei KPI.

## Formalizzare in proporzione al rischio

Non tutto richiede lo stesso livello di governance. Un campo esplorativo usato una volta da un singolo analista non merita necessariamente il processo di una metrica che alimenta board reporting, pricing, campagne automatiche o modelli in produzione.

La formalizzazione dovrebbe crescere con la criticità e con il numero di consumatori. Il criterio utile è chiedersi se la proprietà verificata dovrebbe rimanere vera nel tempo, chi può modificarla a monte e quale impatto avrebbe un cambiamento silenzioso sui processi che dipendono da essa.

Quando la risposta è rilevante, abbiamo superato il confine tra **fix dell'analisi** e **miglioramento del sistema dati**.

La Data Readiness Review diventa così una sorgente di requisiti a monte: i controlli che oggi richiedono investigazione manuale possono trasformarsi in contratti, validazioni o alert. L'organizzazione impara dal problema invece di diventare soltanto più brava a scoprirlo.

> **La maturità non consiste nel riconoscere ogni volta lo stesso difetto. Consiste nel trasformare le scoperte importanti in aspettative condivise che il sistema non possa violare silenziosamente.**
