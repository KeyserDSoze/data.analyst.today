## 3.14 Data contract: quando un controllo deve diventare un'aspettativa condivisa

Finora abbiamo lavorato soprattutto dal punto di vista del consumatore del dato: riceviamo un dataset, ne comprendiamo grain, chiavi, tempo e qualità, poi decidiamo se è utilizzabile.

Ma alcuni problemi non dovrebbero essere riscoperti a ogni analisi.

Se un campo critico cambia significato, se una chiave deve essere unica o se un evento non può essere rinominato senza conseguenze, queste aspettative devono progressivamente diventare **esplicite a monte**.

Qui entra il concetto di **data contract**.

### Che cosa interessa all'analista

Un data contract può assumere forme tecniche diverse. Per il Data Analyst il punto centrale è più semplice:

> **chi produce un dato e chi lo usa condividono una definizione verificabile delle proprietà che non possono cambiare silenziosamente.**

Tra queste proprietà possono esserci:

- significato del dataset o dell'evento;
- grain;
- chiavi;
- campi obbligatori;
- tipi e unità;
- valori ammessi;
- nullability;
- frequenza e latenza attese;
- owner;
- regole per modifiche incompatibili.

La progettazione e governance dei contract verranno riprese nei Capitoli 12 e 18. Qui ci interessa capire **quando l'analista dovrebbe chiedere che una conoscenza scoperta durante l'indagine diventi un vincolo permanente**.

### Caso simulato/composito — Il conversion rate che crolla senza che le vendite cambino

Un marketplace monitora quotidianamente il checkout conversion rate.

Lunedì il valore passa dal **3,8% al 2,9%**.

Le vendite assolute sono quasi stabili.

L'analista controlla il denominatore: il numero di `checkout_started` è aumentato del 31%.

La causa emerge dopo il confronto con il team frontend.

Prima della release, l'evento veniva emesso quando l'utente entrava esplicitamente nel primo step di checkout. Dopo la release viene emesso già all'apertura automatica del drawer del carrello.

Il nome dell'evento non è cambiato.

La pipeline non è fallita.

Il campo è ancora valido.

È cambiato il **fenomeno misurato**.

### Dal problema al contratto

La conoscenza emersa dall'incidente potrebbe essere formalizzata così:

```text
Event: checkout_started
Definition: emitted once when the user explicitly enters checkout step 1
Grain: one event per checkout attempt
Required fields: session_id, timestamp, cart_value
Owner: Checkout Product Team
Semantic changes: analytics review required before production
```

Il valore del contratto non sta nel formato del documento. Sta nel rendere il cambiamento **visibile prima** che diventi una falsa storia nei KPI.

### Non tutto merita lo stesso livello di formalizzazione

Un campo esplorativo usato da un solo analista una volta all'anno non richiede necessariamente lo stesso processo di una metrica che alimenta:

- board reporting;
- pricing;
- campagne automatizzate;
- decisioni operative quotidiane;
- modelli predittivi in produzione.

La formalizzazione dovrebbe essere proporzionata alla criticità.

### Dalla scoperta locale alla prevenzione sistemica

Durante una Data Readiness Review, chiediamoci:

- questo problema può ripetersi?
- la proprietà che abbiamo verificato dovrebbe essere sempre vera?
- chi può modificarla a monte?
- come può sapere che esistono consumatori dipendenti da quella proprietà?
- possiamo trasformare il controllo manuale in una regola condivisa?

Se la risposta è sì, abbiamo superato il confine tra "fix dell'analisi" e **miglioramento del sistema dati**.

> **La maturità non consiste nel diventare bravissimi a scoprire ogni volta lo stesso problema. Consiste nel trasformare le scoperte importanti in aspettative che il sistema non possa violare silenziosamente.**