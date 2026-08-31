## 14.10 Privacy e dati sensibili: non tutto ciò che l'AI può vedere deve essere mostrato all'AI
L'AI-assisted analytics rende molto semplice copiare una tabella, un estratto di log o un dataset dentro un sistema generativo e chiedere: “trova qualcosa di interessante”. Questa facilità crea un nuovo rischio operativo: il dato può essere condiviso prima ancora che qualcuno si chieda se sia appropriato farlo.

La prima domanda non è quindi:

> “L'AI sa analizzare questo dataset?”

ma:

> “L'AI è autorizzata a ricevere questo dataset, in questa forma, per questo scopo?”

## Minimizzazione prima della potenza

Un analista dovrebbe chiedersi:

- servono davvero nomi e indirizzi email?
- basta un identificativo pseudonimo?
- è necessario includere testo libero dei ticket?
- possiamo aggregare prima di inviare?
- quali colonne contengono dati personali o commercialmente sensibili?
- il sistema AI utilizzato è approvato dall'organizzazione?
- dove vengono elaborati e conservati i dati?
- quali log e audit trail rimangono?

## Caso realistico: i ticket del customer care

Un team vuole usare un LLM per classificare automaticamente 180.000 ticket e capire le principali cause di insoddisfazione.

Il primo prototipo esporta:

- nome cliente;
- email;
- numero d'ordine;
- testo completo del ticket;
- note interne dell'operatore;
- categoria prodotto.

Per l'analisi tematica, nome ed email non servono. In molti casi non serve neppure il numero d'ordine. Le note interne possono contenere informazioni che non dovrebbero essere inviate al sistema scelto.

Una progettazione più matura costruisce una vista dedicata:

- `ticket_id` pseudonimizzato;
- testo ripulito da pattern sensibili dove possibile;
- macro-categoria prodotto;
- paese;
- data;
- outcome del ticket.

Lo stesso problema analitico viene risolto con una superficie di rischio molto più piccola.

## Least privilege anche per gli agenti

Un agente che può interrogare il warehouse non dovrebbe necessariamente poter vedere tutto il warehouse.

L'accesso ideale segue il principio del minimo privilegio:

- dataset strettamente necessari;
- permessi read-only quando bastano;
- separazione tra ambienti di sviluppo e produzione;
- approvazione umana per azioni irreversibili;
- logging delle interrogazioni e delle azioni;
- blocchi espliciti su dati particolarmente sensibili.

Questo diventa ancora più importante quando gli agenti possono usare tool, inviare messaggi, modificare file o eseguire query.

## La privacy non è una casella finale

Se il workflow viene progettato senza considerare privacy e sicurezza, aggiungere un controllo alla fine è spesso troppo tardi. Microsoft, nella propria guida per agenti responsabili, tratta privacy, sicurezza, trasparenza e accountability come decisioni da incorporare fin dall'architettura e raccomanda human approval per azioni difficili da invertire o che coinvolgono persone, denaro o compliance.

**L'AI non cambia il principio fondamentale: utilizzare un dato perché è disponibile non significa avere una ragione legittima per utilizzarlo.**

### Fonti

- Microsoft Learn, Responsible AI for agents: https://learn.microsoft.com/en-us/agents/center-of-excellence/responsible-ai
- NIST AI RMF Generative AI Profile: https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence
