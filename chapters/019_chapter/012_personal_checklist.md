## 19.11 Personal Career Operating Plan

Il capitolo può ora trasformarsi in un artefatto operativo. Il **Personal Career Operating Plan** non è un curriculum, una lista di corsi o un piano quinquennale rigido. È una fotografia periodica di quali responsabilità vogliamo saper possedere, quali capacità le sostengono, che cosa possiamo delegare e quale verification reserve dobbiamo continuare a mantenere.

### Stati

Per evitare punteggi arbitrari usiamo quattro stati:

| Stato | Significato |
|---|---|
| `STRONG` | applico la capacità in autonomia, conosco i failure mode principali e so revisionare output altrui o AI |
| `DEVELOPING` | lavoro sul problema con supporto; alcune assunzioni o failure mode richiedono review |
| `DEPENDENT` | produco soprattutto grazie a tool, AI o altre persone, senza verification reserve sufficiente |
| `UNKNOWN` | non ho abbastanza esposizione reale per valutare la capacità |

`UNKNOWN` è più utile di un falso `STRONG`.

## 1. Target Responsibility

La prima domanda è: **quale responsabilità voglio essere capace di possedere meglio fra 12–24 mesi?** Può essere una retention investigation end-to-end, experiment governance, semantic ownership di un dominio, forecast-to-capacity decision, pricing analytics, agent eval, executive decision analysis o la trasformazione di un workflow ricorrente in data product affidabile.

Scrivere “diventare senior” non indica che cosa dobbiamo imparare. Scrivere una responsabilità sì.

## 2. Decision Portfolio

Registriamo poche decisioni o classi di problema su cui abbiamo esperienza reale.

| Decisione / problema | Ruolo attuale | Stato | Evidence |
|---|---|---|---|
| onboarding / activation | analysis contributor | STRONG | 2 casi end-to-end |
| pricing | analysis contributor | DEVELOPING | progetto osservazionale, nessun experiment |
| forecast → staffing | nessuna esperienza | UNKNOWN | — |
| agent eval | reviewer | DEPENDENT | uso framework esistente |

La tabella rende visibile il decision span reale, non quello suggerito dal titolo.

## 3. Capability Portfolio

Valutiamo le quattro dimensioni già incontrate: **Breadth, Depth, Domain, Operating responsibility**. Per ciascuna non basta elencare temi; dobbiamo sapere se riusciamo a spiegare assunzioni, failure mode, trade-off e verification strategy.

Nella breadth possono rientrare statistica/EDA, experimentation, causalità, forecasting, prediction, SQL/data modeling, architecture, visualization, decision analysis, AI workflow e reliability. Nella depth scegliamo poche aree in cui sappiamo andare oltre l'uso superficiale. Nel domain registriamo contesti realmente accumulati. Nell'operating responsibility indichiamo che cosa abbiamo già posseduto nel lifecycle: analisi, metrica, experiment, policy, data product, agent workflow o recurring decision process.

## 4. Task Exposure Map

Osserviamo le attività che consumano tempo e chiediamo quanto il costo di esecuzione stia scendendo, quanto siano verificabili e quale responsibility moat resti.

| Task | Exposure | Decisione personale |
|---|---|---|
| boilerplate SQL | alta | DELEGATE MORE |
| metric definition | media | KEEP / SPECIALIZE |
| chart formatting | alta | DELEGATE MORE |
| causal design review | media | REBUILD / SPECIALIZE |
| weekly manual export | alta | RETIRE / AUTOMATE |
| executive challenge handling | bassa-media | KEEP |

Il punto non è automatizzare tutto. È smettere di spendere capitale professionale dove non costruisce più vantaggio o verification capability.

## 5. Delegation Boundary e Verification Reserve

Per i workflow principali indichiamo il livello di delega attuale e quello desiderabile:

`A Human execution → B AI draft → C AI execution + targeted verification → D Agent workflow + sampling/audit → E Bounded autonomous service`

Poi rendiamo esplicita la verification reserve che permette di salire di livello.

| Verification skill | Stato | Come la mantengo |
|---|---|---|
| grain/cardinality | STRONG | query review + incident |
| uncertainty/power | DEVELOPING | experiment review |
| causal identification | DEVELOPING | case critique |
| temporal leakage | STRONG | forecast/model review |
| semantic modeling | DEPENDENT | progetto dedicato |

Se una skill è `DEPENDENT` e protegge un failure mode importante del nostro lavoro, diventa una priorità.

## 6. Learning Portfolio

L'apprendimento deve attraversare più modalità:

**Learn → Apply → Review → Teach → Operate**

`Learn` introduce il concetto; `Apply` lo porta in un caso end-to-end; `Review` ci obbliga a criticare lavoro proprio, altrui o AI; `Teach` verifica se sappiamo spiegare il modello; `Operate` mostra cosa accade quando il metodo incontra dati sporchi, stakeholder e failure. Una competenza che esiste soltanto in `Learn` è ancora fragile.

## 7. Domain ed Evidence Portfolio

Per il dominio possiamo mantenere un notebook con economics, driver, definizioni, processi, stakeholder, failure mode ricorrenti, regolazione, stagionalità e metriche spesso confuse. L'obiettivo è costruire un modello del sistema, non un'enciclopedia.

Per l'evidence portfolio conserviamo invece, nei limiti di privacy e confidenzialità, decision case che mostrino problema, decisione, failure mode, metodo e alternative scartate, verification, uncertainty, recommendation, outcome/learning e ruolo dell'AI. Un portfolio così dimostra judgment meglio di una galleria di output.

## 8. Escalation Network

Il Capability Portfolio non deve diventare autosufficienza. Registriamo le persone o funzioni a cui possiamo passare rapidamente un rischio quando serve profondità diversa: Finance, Legal/Privacy, Security, Data Engineering, ML Engineering, statistica/causal specialist, domain expert, Product, Operations. La seniority comprende anche la qualità di questa rete.

## 9. Optionality Stress Test e Career Experiments

Periodicamente stressiamo il piano contro più futuri: tool che cambia, organizzazione diversa, nuovo dominio, AI che accelera più del previsto, AI che delude, requisiti di audit più forti. Lo scopo non è eliminare ogni dipendenza, ma individuare quella che potrebbe azzerare troppo capitale professionale.

Le lacune possono essere esplorate con **career experiments** reversibili: guidare un experiment review per qualche mese, diventare owner di una metrica certificata, fare shadowing di data incident, costruire un progetto causale con specialist review, trasformare un report in Analytics Operating Contract, creare una agent eval suite o lavorare su un nuovo dominio. Ogni esperimento dovrebbe avere una capacità da testare, evidence attesa, reviewer e criterio per decidere se approfondire.

## Personal Review Gate

A ogni review assegniamo alle attività e capacità una delle seguenti azioni:

| Azione | Quando usarla |
|---|---|
| `KEEP` | resta importante e il livello è adeguato |
| `DELEGATE MORE` | il task è maturo e verificabile; il tempo può spostarsi verso responsabilità maggiori |
| `REBUILD SKILL` | la verification reserve sta scendendo troppo |
| `SPECIALIZE` | l'area ha valore, profondità e feedback sufficienti per un investimento maggiore |
| `ESCALATE / BUILD NETWORK` | il lavoro incontra rischi che richiedono specialisti non ancora raggiungibili bene |
| `RETIRE` | skill, tool o attività hanno ritorno troppo basso rispetto alle alternative |

Una carriera cresce anche attraverso ciò che scegliamo di non mantenere più.

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

La domanda finale del piano non è soltanto “che cosa devo imparare?”. È:

> **Quale responsabilità voglio essere capace di possedere, quale lavoro posso delegare per arrivarci e quali competenze devo mantenere vive per meritare quella delega?**

Questo è il career operating model del libro.