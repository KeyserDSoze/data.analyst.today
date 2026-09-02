## 19.11 Personal Career Operating Plan

Una checklist può essere utile per ricordare ciò che conta.

Ma alla fine di questo libro possiamo fare qualcosa di più operativo.

Costruire un **Personal Career Operating Plan**.

Non è un curriculum.

Non è una lista di corsi da completare.

Non è neppure un piano quinquennale rigido.

È una fotografia periodica di:

- quali responsabilità vogliamo saper possedere;
- quali capacità sostengono quelle responsabilità;
- cosa possiamo delegare;
- che cosa dobbiamo ancora saper verificare;
- dove stiamo accumulando domain leverage;
- quale optionality stiamo costruendo;
- quale evidence dimostra che stiamo davvero crescendo.

## Stato, non voto

Evitiamo un punteggio numerico arbitrario.

Per ogni area possiamo usare quattro stati.

### STRONG

Posso applicare la capacità in autonomia, spiegare i principali failure mode e revisionare output altrui o AI.

### DEVELOPING

Posso lavorare sul problema con supporto, ma alcune assunzioni o failure mode richiedono review.

### DEPENDENT

Riesco a produrre un risultato soprattutto grazie a tool, AI o altre persone, ma non possiedo ancora sufficiente verification reserve.

### UNKNOWN

Non ho abbastanza esposizione reale per sapere quanto sono forte.

`UNKNOWN` è spesso più sano di un falso `STRONG`.

## 1. Target Responsibility

La prima domanda non è:

> “Quale posizione voglio?”

È:

> **“Quale responsabilità voglio essere capace di possedere meglio fra 12–24 mesi?”**

Esempi:

- possedere una retention investigation end-to-end;
- progettare e governare experiment di prodotto;
- essere semantic owner di un dominio;
- tradurre forecast in capacity decision;
- gestire analytics per pricing;
- costruire eval e operating contract per agenti analitici;
- guidare executive decision analysis;
- trasformare workflow ricorrenti in data product affidabili.

Scrivere una responsabilità è più utile di scrivere:

> “diventare senior”.

Perché possiamo capire quali capacità mancano.

## 2. Decision Portfolio

Quali decisioni sappiamo già migliorare?

Costruiamo una tabella personale.

| Decisione / problema | Ruolo attuale | Stato | Evidence |
|---|---|---|---|
| onboarding / activation | analysis contributor | STRONG | 2 casi end-to-end |
| pricing | analysis contributor | DEVELOPING | progetto osservazionale, nessun experiment |
| forecast → staffing | nessuna esperienza | UNKNOWN | — |
| agent eval | reviewer | DEPENDENT | uso framework esistente |

L'obiettivo non è riempire cento righe.

È rendere visibile il proprio **decision span reale**.

## 3. Capability Portfolio

Rivediamo le quattro dimensioni del paragrafo 19.4.

### Breadth

Quali discipline riesco a comprendere abbastanza da scegliere il metodo e collaborare?

Possibili aree:

- EDA/statistica;
- experimentation;
- causalità;
- forecasting;
- prediction;
- SQL/data modeling;
- architecture;
- visualization;
- decision analysis;
- AI/agent workflow;
- reliability/governance.

### Depth

Dove so andare oltre la superficie?

Scegliere poche aree in cui possiamo spiegare:

- assunzioni;
- failure mode;
- alternative;
- trade-off;
- verification strategy.

### Domain

Dove stiamo accumulando conoscenza che non deriva soltanto da un corso?

Esempi:

- payments;
- marketplace;
- SaaS;
- retail;
- supply chain;
- finance;
- healthcare.

### Operating responsibility

Che cosa abbiamo già posseduto?

- singola analisi;
- metrica;
- experiment;
- predictive policy;
- dashboard/prodotto;
- data product;
- agent workflow;
- recurring decision process.

Per ogni area segnare:

`STRONG / DEVELOPING / DEPENDENT / UNKNOWN`.

## 4. Task Exposure Map

Prendiamo le attività che occupano una parte significativa del nostro tempo.

Per ognuna chiediamo:

- il costo di automazione sta scendendo?
- il task è ripetitivo?
- il risultato è facilmente verificabile?
- quale failure cost contiene?
- quale parte della responsabilità resta umana?

Esempio:

| Task | Exposure | Decisione personale |
|---|---|---|
| boilerplate SQL | alta | DELEGATE MORE |
| metric definition | media | KEEP / SPECIALIZE |
| chart formatting | alta | DELEGATE MORE |
| causal design review | media | REBUILD / SPECIALIZE |
| weekly manual export | alta | RETIRE/AUTOMATE |
| executive challenge handling | bassa-media | KEEP |

Il punto non è automatizzare tutto.

È smettere di spendere capitale professionale dove non costruisce più vantaggio.

## 5. Delegation Boundary

Per i workflow principali, quale livello di delega è appropriato?

Richiamiamo i livelli:

- **A — Human execution**;
- **B — AI draft**;
- **C — AI execution + targeted verification**;
- **D — Agent workflow + sampling/audit**;
- **E — Bounded autonomous service**.

Per ogni workflow chiediamo:

1. a quale livello sono oggi?
2. quale livello sarebbe economicamente utile?
3. che cosa devo saper verificare per salire di un livello?
4. quali failure mode devono essere coperti prima?

Questo trasforma “devo usare più AI” in un piano concreto.

## 6. Verification Reserve

Quali competenze devono restare vive anche se le usiamo meno manualmente?

Una scheda personale può includere:

| Verification skill | Stato | Come la mantengo |
|---|---|---|
| grain/cardinality | STRONG | query review + incident |
| uncertainty/power | DEVELOPING | experiment review mensile |
| causal identification | DEVELOPING | case critique |
| temporal leakage | STRONG | forecast/model review |
| semantic modeling | DEPENDENT | progetto dedicato |

Se una skill è `DEPENDENT` ma protegge un failure mode importante del nostro lavoro, diventa una priorità di apprendimento.

## 7. Learning Portfolio

Un piano equilibrato dovrebbe includere più di corsi e tutorial.

### Learn

Un concetto o metodo nuovo.

### Apply

Un progetto reale o simulato end-to-end.

### Review

Criticare lavoro proprio, altrui o AI.

### Teach

Spiegare il concetto a qualcuno o scriverne una nota.

### Operate

Vedere cosa succede quando il metodo entra in un processo reale e incontra dati sporchi, stakeholder e failure.

Una competenza che esiste soltanto in `Learn` è ancora fragile.

## 8. Domain Accumulation Plan

La conoscenza di dominio cresce lentamente.

Per renderla deliberata possiamo mantenere un **domain notebook** con:

- economics;
- driver principali;
- definizioni;
- processi;
- stakeholder;
- failure mode ricorrenti;
- regolazione rilevante;
- stagionalità;
- metriche che vengono spesso confuse;
- domande che il business continua a ripetere.

L'obiettivo non è diventare enciclopedia del settore.

È costruire un modello del sistema abbastanza ricco da formulare ipotesi migliori.

## 9. Evidence Portfolio

Come dimostriamo le nostre capacità?

Per ogni progetto importante conserviamo, nei limiti consentiti da privacy e confidenzialità:

- problema;
- decisione;
- Analytical Brief;
- failure mode trovato;
- metodo scelto e alternative scartate;
- verification;
- uncertainty;
- recommendation;
- outcome/learning;
- cosa abbiamo delegato all'AI;
- cosa abbiamo verificato personalmente.

Il portfolio professionale del futuro potrebbe assomigliare sempre meno a una galleria di dashboard e sempre più a una raccolta di **decision case**.

## 10. Escalation Network

Nessun Capability Portfolio deve essere autosufficiente.

Chi possiamo coinvolgere quando serve profondità diversa?

Costruiamo una rete reale:

- Finance;
- Legal/privacy;
- Security;
- Data Engineering;
- ML Engineering;
- statistica/causal specialist;
- domain expert;
- Product;
- Operations.

Conoscere il nome del tipo di esperto non basta.

Una carriera senior include anche relazioni attraverso cui possiamo **escalare rapidamente un rischio**.

## 11. Career Optionality Stress Test

Una volta l'anno chiediamo:

### Tool change

Se il mio stack sparisse, quanto velocemente potrei ricostruire produttività?

### Organization change

Le mie skill funzionano soltanto nell'azienda attuale perché conosco eccezioni non documentate?

### Domain change

Quale parte del mio sapere è trasferibile e quale deve essere ricostruita?

### AI acceleration

Se il mio task principale diventasse 10 volte più economico, quale responsabilità superiore potrei assumere?

### AI disappointment

Se l'automazione procedesse più lentamente, possiedo ancora abbastanza capacità esecutiva?

### Regulation/risk

Se aumentassero requisiti di audit e human approval, saprei lavorare in modo più rigoroso?

L'obiettivo non è essere perfettamente robusti.

È evitare una singola dipendenza nascosta.

## 12. Twelve-month career experiments

Una carriera non deve essere pianificata soltanto con grandi decisioni irreversibili.

Possiamo usare **career experiments**.

Esempi:

- guidare un experiment review per tre mesi;
- diventare owner di una metrica certificata;
- fare shadowing a un data incident rotation;
- costruire un progetto di causal inference con specialist review;
- trasformare un report ricorrente in Analytics Operating Contract;
- costruire un agent eval suite;
- lavorare su un problema in un dominio nuovo;
- presentare una Decision Communication Pack a leadership.

Ogni esperimento deve avere:

- competenza da testare;
- evidence attesa;
- durata;
- mentor/reviewer;
- criterio per decidere se approfondire.

Questo costruisce optionality con rischio limitato.

## Il Personal Review Gate

Ogni trimestre o semestre, per le principali skill e attività scegliamo una delle azioni seguenti.

### KEEP

È ancora importante e il livello è adeguato.

### DELEGATE MORE

Il task è maturo, verificabile e occupa tempo che può essere spostato verso responsabilità più alte.

### REBUILD SKILL

La verification reserve sta diventando troppo bassa.

### SPECIALIZE

L'area ha abbastanza valore, interesse e profondità da meritare maggiore investimento.

### ESCALATE / BUILD NETWORK

Il lavoro incontra rischi che richiedono specialisti con cui non abbiamo ancora una relazione efficace.

### RETIRE

La skill/tool/activity ha ritorno troppo basso rispetto alle alternative.

Una carriera cresce anche attraverso ciò che scegliamo **di smettere di mantenere**.

## Template sintetico

```text
PERSONAL CAREER OPERATING PLAN

Target responsibility:
Decision portfolio:

Capability Portfolio
- Breadth:
- Depth:
- Domain:
- Operating responsibility:

Task exposure
- Delegate more:
- Keep human-led:
- Retire/automate:

Delegation boundary:
Verification reserve:

Learning portfolio
- Learn:
- Apply:
- Review:
- Teach:
- Operate:

Domain accumulation:
Evidence portfolio:
Escalation network:

Career optionality risks:
12-month career experiments:

Next review date:
Actions: KEEP / DELEGATE MORE / REBUILD / SPECIALIZE / ESCALATE / RETIRE
```

## La domanda finale del piano

Non chiedere soltanto:

> “Che cosa devo imparare?”

Chiedi:

> **“Quale responsabilità voglio essere capace di possedere, quale lavoro posso delegare per arrivarci e quali competenze devo mantenere vive per meritare quella delega?”**

Questo è il career operating model del libro.
