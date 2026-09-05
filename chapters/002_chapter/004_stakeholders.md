## 2.3 Stakeholder: chi chiede non è sempre chi decide

Una richiesta analitica raramente appartiene a una sola persona. Chi apre il ticket può non usare mai il risultato; chi usa il report ogni giorno può non avere autorità sulla decisione; chi decide può dipendere da una metrica definita da Finance; e la persona che conosce davvero le eccezioni del processo può non essere stata coinvolta nella richiesta iniziale.

Questa distribuzione del contesto è uno dei motivi per cui un'analisi può essere tecnicamente corretta e organizzativamente sbagliata. Il problema non è soltanto raccogliere “i requisiti”. È capire **dove vive il significato necessario a rendere quei requisiti coerenti**.

Nel brief conviene quindi distinguere almeno cinque funzioni: il **requester**, che formula la richiesta; il **decision owner**, che possiede l'autorità di agire; il **domain expert**, che conosce processi ed eccezioni; il **data o metric owner**, che conosce fonti e definizioni autorevoli; e l'**end user**, che utilizzerà concretamente l'output. Nelle analisi semplici possono coincidere nella stessa persona. Nei processi importanti, assumere che coincidano è rischioso.

### Caso simulato/composito: un CAC, quattro interpretazioni

Marketing chiede un report sul Customer Acquisition Cost. Il marketing manager ha aperto la richiesta, ma il CMO userà il numero per allocare budget. Finance stabilisce quali costi devono entrare nel calcolo, il CRM owner conosce i limiti dell'attribuzione e i campaign manager utilizzeranno il report ogni giorno.

Se l'analista parla soltanto con il requester, può costruire un CAC perfettamente coerente con le tabelle marketing e tuttavia incompatibile con la definizione su cui Finance costruisce il budget. A quel punto non abbiamo una formula sbagliata: abbiamo **ownership semantica non mappata**.

Lo stesso problema appare con colonne apparentemente inequivocabili. `status = closed`, per esempio, può indicare un problema risolto, una richiesta duplicata, un cliente non raggiungibile, una pratica annullata oppure una chiusura automatica dopo un certo numero di giorni. Il domain expert può cambiare l'interpretazione di settimane di dati spiegando in pochi minuti quale evento operativo produce realmente quello stato.

Per questo il dominio non è un'aggiunta “soft” alla parte tecnica. È una componente del modello dei dati.

## Il disaccordo va reso visibile

Quando stakeholder diversi definiscono in modo incompatibile “cliente acquisito”, “revenue” o “lead qualificato”, la soluzione non è scegliere silenziosamente la versione che rende più semplice la query. Il disaccordo stesso è un requisito: forse serve una definizione condivisa, forse due metriche sono legittime perché supportano decisioni diverse, forse un owner deve stabilire la source of truth, oppure la divergenza va documentata come limite dell'analisi.

Una stakeholder interview serve quindi anche a trovare incompatibilità **prima che entrino nel codice**. Dovrebbe far emergere il problema, la decisione, le alternative, il timing, le metriche già utilizzate, le eccezioni operative, gli owner delle fonti critiche e i vincoli economici o normativi. Non occorre trasformarla in un questionario meccanico: l'obiettivo è ricostruire la mappa di responsabilità che determina il significato del brief.

L'analista, inoltre, non è un raccoglitore passivo. Se lo stakeholder chiede venti grafici, il requisito reale non diventa automaticamente “produrre venti grafici”. Il business porta contesto e possibilità d'azione; domain e data owner portano conoscenza operativa e semantica; l'analista deve usare questi elementi per proporre il prodotto minimo capace di ridurre l'incertezza che conta.

La stakeholder map rimane quindi un artefatto utile da compilare:

| Ruolo | Persona/Team | Conoscenza/ownership | Decisione o uso | Coinvolgimento necessario |
|---|---|---|---|---|
| Requester |  |  |  |  |
| Decision owner |  |  |  |  |
| Domain expert |  |  |  |  |
| Data/metric owner |  |  |  |  |
| End user |  |  |  |  |

> **Mappare gli stakeholder significa sapere chi possiede la decisione, chi possiede il significato e chi subirà le conseguenze di una definizione sbagliata.**
