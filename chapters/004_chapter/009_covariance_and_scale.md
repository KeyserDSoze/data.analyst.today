## 4.8 Covarianza, scala e perché il contesto conta

La covarianza misura se due variabili tendono a muoversi insieme. Se cresce una e tende a crescere anche l'altra, la covarianza è positiva. Se una cresce mentre l'altra tende a diminuire, è negativa.

Il problema è che il valore dipende dalla scala delle variabili. Una covarianza tra ricavi espressi in euro e ordini giornalieri non è direttamente confrontabile con una covarianza tra conversion rate e tempo medio di sessione.

È uno dei motivi per cui, nella pratica, gli analisti usano spesso la correlazione: standardizza la relazione e la riporta su una scala interpretabile tra -1 e 1.

### Caso: due mercati che sembravano uguali

Una società di delivery confronta due città, Torino e Bologna. In entrambe, ordini giornalieri e numero di rider attivi si muovono insieme.

La covarianza è molto più alta a Torino. Il team conclude che il mercato torinese sia "più sensibile" alla disponibilità di rider.

Ma Torino genera quasi il doppio degli ordini medi giornalieri. La scala più grande amplifica automaticamente la covarianza.

Quando l'analista calcola la correlazione, i risultati sono:

- Torino: 0,63
- Bologna: 0,79

La lettura cambia completamente. In termini relativi, Bologna mostra una relazione più stretta tra domanda e disponibilità della flotta.

La morale non è che la covarianza sia inutile. È che **una misura statistica non va interpretata separatamente dalla sua scala e dalla domanda a cui deve rispondere**.