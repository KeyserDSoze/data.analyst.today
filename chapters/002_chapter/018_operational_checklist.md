## 2.17 Checklist operativa: prima di iniziare un'analisi

Prima di aprire uno strumento, eseguire una query o chiedere aiuto a un sistema AI, è utile passare attraverso una checklist minima.

### Problema e decisione

- Qual è il problema di business?
- Quale decisione deve essere presa?
- Chi prende la decisione?
- Qual è il costo di una decisione sbagliata?
- Entro quando serve una risposta?

### Domanda analitica

- La domanda è descrittiva, diagnostica, predittiva, prescrittiva o causale?
- Qual è la popolazione di interesse?
- Qual è l'unità di analisi?
- Qual è il periodo temporale corretto?
- Quale baseline useremo?

### Metriche

- Qual è la metrica primaria?
- Qual è il denominatore?
- Esistono metriche di guardrail?
- Le definizioni sono condivise con gli stakeholder?
- Le metriche possono essere manipolate o interpretate in modi diversi?

### Ipotesi

- Quali spiegazioni sono plausibili prima di guardare i risultati?
- Quali spiegazioni alternative dobbiamo escludere?
- Quali variabili potrebbero confondere il confronto?

### Dati

- Quali fonti servono?
- Qual è la granularità?
- Il dato copre tutta la popolazione rilevante?
- Esistono missing value, duplicati, ritardi o cambiamenti di tracking?
- La metrica può essere ricostruita in modo ripetibile?

### Metodo

- Qual è il metodo più semplice capace di rispondere alla domanda?
- Serve davvero un modello complesso?
- Serve statistica inferenziale?
- Serve un esperimento?
- Quale livello di precisione è sufficiente?

### Output

- Quale decisione potrebbe cambiare?
- Come comunicheremo l'incertezza?
- Quali limiti devono essere esplicitati?
- Quale azione suggeriremmo se l'ipotesi fosse confermata?
- Cosa faremmo se fosse smentita?

### AI

Se usiamo l'AI:

- stiamo fornendo definizioni e contesto sufficienti?
- possiamo verificare query, formule e codice generati?
- l'AI sta distinguendo fatti, inferenze e ipotesi?
- abbiamo controllato che non stia inventando colonne, metriche o regole di business?
- stiamo delegando l'esecuzione o anche il giudizio?

Questa checklist non deve trasformarsi in burocrazia. Deve diventare un'abitudine mentale.

Con esperienza molte domande verranno poste quasi automaticamente. Ma saltarle completamente è uno dei modi più semplici per costruire un'analisi tecnicamente corretta e decisionalmente inutile.
