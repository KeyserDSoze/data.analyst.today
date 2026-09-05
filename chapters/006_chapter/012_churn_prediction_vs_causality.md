## 6.11 Churn prediction: rischio, diagnosi e persuadibilità sono problemi diversi

Dopo aver descritto segmenti, coorti, activation, retention e valore, la richiesta naturale è: **possiamo prevedere chi se ne andrà?**

Spesso sì. Ma prima dell'algoritmo dobbiamo separare tre problemi che vengono facilmente confusi: **prediction**, cioè chi ha maggiore probabilità di churn; **diagnosis**, cioè quali condizioni accompagnano il churn; **intervention**, cioè su quali clienti una certa azione riduce davvero la probabilità di uscita.

Un modello predittivo risponde soprattutto alla prima domanda.

### Northstar CRM: un buon ranking non è ancora una strategia di retention

**Northstar CRM** serve circa **18.000 aziende**. Il team Data Science assegna settimanalmente un risk score a ogni account. Fra i segnali più predittivi emergono riduzione dei login, meno utenti attivi nel workspace, mancato uso delle automazioni, aumento dei ticket di supporto e assenza dell'integrazione contabile. Gli account nel decile di rischio più alto churnano molto più spesso della media.

Il modello è quindi utile per il ranking. Il salto problematico arriva quando il Customer Success conclude: “pochi login predicono churn, quindi dobbiamo far aumentare i login”.

Pochi login possono essere sintomo di un prodotto diventato meno utile, di un champion che ha lasciato l'azienda, di una migrazione già decisa, di un ridimensionamento o perfino di un workflow diventato più efficiente. Il segnale predittivo localizza il rischio; non identifica automaticamente la leva.

Il caso dei ticket di supporto rende il punto ancora più evidente. Se molti ticket sono associati a churn elevato, non ne segue che bisogna impedire ai clienti di contattare il supporto. È più plausibile una struttura del tipo:

`problema del cliente → più ticket`

`problema del cliente → maggiore rischio di churn`

Il ticket può essere un proxy del problema sottostante. **Predittore e causa non sono sinonimi.**

### Il cliente più facile da prevedere può essere il più difficile da salvare

Northstar può intervenire su **300 account al mese**. Se prende semplicemente i 300 risk score più alti, può finire per contattare clienti che hanno già comunicato la disdetta, stanno cessando l'attività o hanno completato la migrazione verso un concorrente. Sono casi facili da prevedere e poco influenzabili.

Per una lista operativa conviene quindi tenere separate almeno tre dimensioni:

| Dimensione | Domanda |
| --- | --- |
| Risk | Quanto è probabile l'uscita? |
| Value | Quanto valore è a rischio? |
| Actionability | Abbiamo ancora una leva plausibile e il tempo per usarla? |

A queste si aggiunge spesso il tempo al rinnovo. Un account ad alto rischio e alto valore può comunque non essere prioritario se la decisione di uscire è irreversibile; un account con rischio leggermente più basso può avere più valore atteso se esiste ancora un problema concreto e risolvibile.

### Persuadibilità: chi cambia comportamento proprio grazie all'intervento?

C'è infine una domanda ancora più esigente: **quale cliente cambierebbe comportamento proprio grazie alla nostra azione?**

Un cliente ad alto rischio può churnare comunque. Uno a basso rischio sarebbe rimasto anche senza intervento. Il gruppo più interessante può essere quello per cui il trattamento produce un effetto incrementale. È il territorio dell'uplift modeling, degli heterogeneous treatment effects e della sperimentazione mirata.

Questo capitolo non deve anticipare un tutorial di machine learning. Deve chiarire dove la prediction entra nel lifecycle e dove smette di bastare. Il Capitolo 8 affronterà causalità e treatment effect; il Capitolo 9 la sperimentazione; il Capitolo 10 i modelli predittivi, compresi leakage, calibration, threshold e monitoring.

La regola da portare avanti è semplice:

> **Un modello che predice bene chi churnerà non dimostra perché churnerà e non identifica automaticamente chi possiamo salvare.**

Prima di costruire un churn model dobbiamo quindi sapere quale decisione userà il ranking, quanta capacità operativa esiste e quale evidenza guiderà l'intervento. Senza queste risposte rischiamo di produrre un modello tecnicamente corretto per una decisione ancora indefinita.