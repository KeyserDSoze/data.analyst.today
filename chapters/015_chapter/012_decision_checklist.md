## 15.11 Decision Quality Gate: siamo pronti a scegliere?

Il Decision Record conserva il ragionamento completo. Prima della scelta finale serve però un artefatto più rapido che risponda a una domanda semplice:

> **Abbiamo abbastanza struttura per decidere senza nascondere un buco essenziale dietro un numero preciso?**

Il **Decision Quality Gate** non certifica che l'esito sarà buono. Verifica che il processo abbia affrontato, con profondità proporzionata al rischio, le condizioni necessarie per assumere consapevolmente il trade-off.

### 1. Decisione e ownership

- La scelta è formulata come confronto tra alternative?
- Esiste un decision owner nominato?
- La deadline è chiara?
- Recommendation dell'analista e decisione del business owner sono distinte?

Se non sappiamo **chi sceglie cosa entro quando**, il problema non è ancora decisionale.

### 2. Obiettivo, vincoli e guardrail

- Qual è l'obiettivo primario?
- Quali obiettivi secondari contano?
- Quali vincoli sono non negoziabili?
- Quali guardrail non vogliamo sacrificare per migliorare il KPI principale?

Un'opzione che viola un vincolo fondamentale non deve sopravvivere grazie a un expected value elevato.

### 3. Alternative reali

- `Business as usual / do nothing` è esplicito?
- Esistono almeno due opzioni realmente differenti?
- Abbiamo considerato una soluzione più piccola o reversibile?
- Le opzioni escluse hanno una motivazione?
- Esistono opzioni dominate che possiamo eliminare?

Se abbiamo analizzato soltanto la soluzione preferita, non abbiamo ancora fatto option appraisal.

### 4. Evidenza

- Quali finding sono materialmente rilevanti?
- Qual è il claim level dell'evidenza critica?
- Metriche, popolazioni e timestamp sono affidabili?
- Quale deliverable precedente qualifica il claim: Uncertainty Brief, Causal Identification Brief, Predictive Decision Card, AI Analysis Control Sheet, ecc.?
- Abbiamo cercato evidenza contraria o spiegazioni alternative?

### 5. Incertezza e informazione

- Quale incertezza domina il ranking?
- È riducibile entro la deadline?
- Quale informazione potrebbe cambiare scelta?
- Quanto costa ottenerla?
- Quanto costa aspettare?
- Le probabilità hanno una base difendibile o sono decimali decorativi?

### 6. Value e downside

- Benefici e costi sono realmente incrementali rispetto al baseline?
- Abbiamo incluso costi operativi e opportunity cost?
- Qual è il downside plausibile?
- Esistono impatti non monetizzabili materialmente importanti?
- L'organizzazione può assorbire il downside?
- La capacità operativa è coerente con l'opzione?

### 7. Reversibilità e optionality

- Quanto è difficile tornare indietro?
- Possiamo usare pilot, tranche o rollout graduale?
- Una alternativa preserva più opzioni future?
- Esiste un rollback realistico?
- Qual è il blast radius della scelta sbagliata?

### 8. Sensitivity e switching

- Quali 3–5 assunzioni governano la scelta?
- Conosciamo i principali switching values?
- Quanto siamo lontani dal punto di indifferenza?
- Gli scenari rappresentano mondi coerenti o soltanto “±20%”?
- Rischi correlati potrebbero muoversi insieme?
- Il ranking resta robusto in futuri plausibili?

### 9. Pre-mortem

- Se tra sei mesi la decisione fosse un fallimento, quali sarebbero le cause plausibili?
- Quali possiamo rilevare presto?
- Quali leading indicator o guardrail aggiungiamo?
- Chi ha costruito il miglior caso contro l'opzione preferita?

### 10. Recommendation

La recommendation deve completare entrambe le frasi:

> **Preferiamo X a Y, Z e business as usual perché...**

> **Cambieremmo idea se...**

Se la seconda manca, le assunzioni decisive sono probabilmente ancora implicite.

### 11. Execution

- Qual è il primo passo concreto?
- Quali condizioni di stop, rollback o escalation esistono?
- Chi può modificare il piano?
- Come sapremo se l'esecuzione diverge dalla decisione approvata?

### 12. Learning contract

- Quale outcome misuriamo?
- Qual è la baseline?
- Quale range o scenario avevamo previsto?
- Quando avviene la review?
- Quali informazioni dobbiamo registrare per distinguere decision, execution e outcome quality?

## I quattro esiti del gate

Il gate deve poter produrre esiti diversi da “go”.

**DECIDE** — le alternative sono abbastanza caratterizzate e l'incertezza residua è compatibile con rischio e reversibilità.

**PILOT / STAGE** — l'opzione è promettente, ma il valore dell'informazione e la possibilità di limitare il commitment rendono preferibile un impegno parziale.

**WAIT FOR X** — una informazione specifica, ottenibile entro il tempo utile, potrebbe cambiare materialmente il ranking. Il record deve indicare `X`, soglia e review date.

**NO ACTION / ABANDON** — business as usual domina oppure nessuna opzione supera costi, rischi e opportunity cost.

La formalità deve essere proporzionata. Una modifica reversibile da €2.000 non richiede la stessa profondità di pricing globale, acquisizione aziendale, capex pluriennale o policy con impatto su persone. Le domande fondamentali, però, restano le stesse.

Prima della decisione chiediamo infine:

> **Se il decision owner seguisse esattamente questa recommendation e l'esito fosse negativo, potremmo comunque difendere il processo usando l'evidenza, le alternative e i trade-off disponibili oggi?**

Se la risposta è no, manca ancora qualcosa nel Decision Record.

> **Il gate non serve a eliminare il rischio. Serve a impedire che assumiamo rischio senza aver chiarito quale rischio stiamo scegliendo e perché.**
