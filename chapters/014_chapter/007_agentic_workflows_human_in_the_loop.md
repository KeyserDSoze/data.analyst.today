# 14.6 Agentic workflows e human-in-the-loop: automatizzare il processo senza automatizzare l'errore

Quando un assistente AI passa dalla singola risposta a una sequenza di azioni, entriamo nel territorio dei workflow agentici.

Un agente può, in linea di principio:

1. ricevere una richiesta;
2. scegliere quali dati interrogare;
3. eseguire SQL;
4. interpretare il risultato;
5. produrre grafici;
6. confrontare KPI con soglie;
7. generare una raccomandazione;
8. inviare una notifica o avviare un'azione.

La capacità è potente. Il rischio è altrettanto semplice da capire: **un errore nei primi passi può propagarsi automaticamente nei successivi**.

## Caso realistico: l'agente che voleva spegnere una campagna profittevole

Un e-commerce costruisce un workflow che ogni mattina:

- legge ROAS per campagna;
- identifica quelle sotto 1,5;
- prepara una raccomandazione di pausa;
- chiede approvazione al marketing manager.

Un lunedì l'agente segnala una campagna con ROAS 1,18.

La query è corretta, ma il feed revenue è D+1 mentre la spesa advertising è quasi real-time. Gran parte delle conversioni della domenica non è ancora arrivata.

Il giorno successivo il ROAS reconciliato è 2,34.

Se il workflow avesse avuto autonomia completa, avrebbe spento una campagna sana sulla base di fonti con latenze diverse.

Il controllo giusto non era "il numero è sotto 1,5?", ma:

- i dataset sono completi?
- le latenze sono compatibili?
- il KPI è finalizzato?
- il costo di una falsa azione è accettabile?

## Dove inserire l'essere umano

Non esiste un unico modello human-in-the-loop.

### Approval before action

L'AI prepara un'azione, ma una persona approva.

Adatto a:

- variazioni budget;
- comunicazioni executive;
- modifiche a metriche;
- decisioni su clienti di alto valore.

### Approval on exception

Il workflow procede automaticamente per casi normali e chiede intervento quando rileva anomalie.

Esempio:

- refresh standard automatico;
- escalation se row count cambia >10%;
- escalation se reconciliation differisce >1%.

### Audit after action

L'azione è automatica ma completamente loggata e campionata per review successiva.

Adatto soprattutto a task reversibili e a basso rischio.

## Il principio della reversibilità

Più un'azione è difficile da annullare, più deve essere alto il livello di controllo.

| Azione | Reversibilità | Autonomia AI ragionevole |
|---|---|---|
| proporre una query | alta | alta |
| creare una bozza di report | alta | alta |
| pubblicare KPI ufficiale | media | limitata |
| modificare budget advertising | media | approval |
| rifiutare credito / cambiare prezzo | bassa | controllo forte |

## Un agente deve sapere quando non sa

Un workflow maturo deve poter produrre output come:

> "Non posso determinare il driver con sufficiente affidabilità perché la tabella payments è incompleta dalle 03:00 alle 06:20."

Questo è un comportamento migliore di una raccomandazione forzata.

Per ottenerlo, il sistema deve avere accesso a segnali di qualità:

- freshness;
- completeness;
- schema status;
- reconciliation;
- confidence del metodo;
- limiti di utilizzo.

## Controlli minimi per workflow agentici analitici

Un workflow che usa dati aziendali dovrebbe avere almeno:

- identità e permessi minimi necessari;
- scope degli strumenti consentiti;
- logging delle query e delle azioni;
- limiti di costo;
- test sui dati prima dell'interpretazione;
- soglie di escalation;
- possibilità di stop;
- versioning di prompt, metriche e logica;
- review periodica degli errori.

## Caso realistico: anomaly agent per supply chain

Un distributore industriale monitora 6.400 SKU.

L'agente identifica ogni giorno anomalie su:

- domanda;
- stockout risk;
- lead time;
- purchase orders.

All'inizio genera oltre 300 alert al giorno. Gli operatori smettono di leggerli.

La soluzione non è un modello più grande. Il team introduce:

- classificazione per impatto economico;
- deduplication degli alert correlati;
- cooldown di 48 ore;
- soglia più alta per SKU a basso valore;
- escalation umana solo oltre €25k di rischio stimato.

Gli alert scendono a 18–25 al giorno e diventano operativi.

Questo mostra che l'automazione deve essere progettata intorno alla **capacità decisionale umana**, non solo alla capacità computazionale.

> **Un agente utile non è quello che fa più cose da solo. È quello che automatizza le parti reversibili e verificabili e rende esplicite le parti che richiedono giudizio.**

### Fonti

- NIST, *Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile*, https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence
