## 15.11 Decision Quality Gate: siamo pronti a scegliere?

Il Decision Record contiene il ragionamento completo.

Prima della scelta finale serve però un gate più rapido:

> **abbiamo abbastanza struttura per prendere questa decisione senza nascondere un buco essenziale dietro un numero preciso?**

Il **Decision Quality Gate** non certifica che l'esito sarà buono.

Certifica che il processo ha affrontato le domande necessarie per il livello di rischio della scelta.

### 1. Decisione e ownership

- La scelta richiesta è formulata come confronto tra alternative?
- Esiste un decision owner nominato?
- La deadline è chiara?
- Abbiamo distinto recommendation dell'analista da decisione del business owner?

Se non sappiamo **chi sceglie cosa entro quando**, il lavoro non è ancora un problema decisionale ben formato.

### 2. Obiettivo e vincoli

- Qual è l'obiettivo primario?
- Quali obiettivi secondari contano?
- Quali vincoli sono non negoziabili?
- Abbiamo definito guardrail che non vogliamo sacrificare per migliorare il KPI principale?

Un'opzione che viola un vincolo fondamentale non deve sopravvivere grazie a un expected value elevato.

### 3. Alternative reali

- `Business as usual / do nothing` è esplicito?
- Esistono almeno due opzioni realmente differenti?
- Abbiamo considerato una soluzione più piccola o reversibile?
- Le opzioni escluse hanno una motivazione documentata?
- Esistono alternative dominate che possiamo eliminare?

Se abbiamo analizzato soltanto la soluzione preferita, non abbiamo ancora fatto option appraisal.

### 4. Evidenza

- Quali finding sono materialmente rilevanti?
- Qual è il claim level di ciascuna evidenza critica?
- Le metriche e popolazioni sono affidabili?
- Quale deliverable precedente supporta il claim: Uncertainty Brief, Causal Identification Brief, Predictive Decision Card, ecc.?
- Abbiamo cercato evidenza contraria o spiegazioni alternative?

### 5. Incertezza

- Quale incertezza domina il ranking?
- È riducibile entro la deadline?
- Quale informazione potrebbe cambiare scelta?
- Quanto costa ottenerla?
- Quanto costa aspettare?
- Stiamo usando una probabilità difendibile o un decimale decorativo?

### 6. Value e downside

- Benefici e costi sono realmente incrementali rispetto al baseline?
- Abbiamo incluso costi operativi e opportunity cost?
- Qual è il downside plausibile?
- Esistono impatti non monetizzabili materialmente importanti?
- L'organizzazione può assorbire il downside?
- La capacità operativa è coerente con l'opzione?

### 7. Reversibilità e optionality

- Quanto è difficile tornare indietro?
- Possiamo fare pilot, tranche o rollout graduale?
- Una alternativa preserva più opzioni future?
- Abbiamo un rollback realistico?
- Qual è il blast radius della scelta sbagliata?

### 8. Sensitivity e switching

- Quali 3–5 assunzioni governano la scelta?
- Conosciamo i principali switching values?
- Quanto siamo lontani dal punto di indifferenza?
- Gli scenari sono coerenti o soltanto “±20%”?
- Rischi correlati potrebbero muoversi insieme?
- Il ranking resta robusto in futuri plausibili?

### 9. Pre-mortem

- Se tra sei mesi la decisione fosse un fallimento, quali sarebbero le cause plausibili?
- Quali sono rilevabili presto?
- Quali guardrail o leading indicator aggiungiamo?
- Chi ha costruito il miglior caso contro l'opzione preferita?

### 10. Recommendation

La recommendation deve poter completare questa frase:

> **“Preferiamo X a Y, Z e business as usual perché…”**

E anche questa:

> **“Cambieremmo idea se…”**

Se la seconda frase manca, spesso le assunzioni critiche sono ancora implicite.

### 11. Execution

- Qual è il primo passo concreto?
- Quali condizioni di stop/escalation esistono?
- Chi può modificare il piano?
- Come sapremo se l'esecuzione diverge dalla decisione approvata?

### 12. Learning contract

- Quale outcome misuriamo?
- Qual è la baseline?
- Quale range/scenario avevamo previsto?
- Quando avviene la review?
- Quali informazioni dobbiamo registrare per distinguere decision, execution e outcome quality?

### Quattro stati del gate

Possiamo usare una classificazione semplice.

**DECIDE**

Le alternative sono abbastanza caratterizzate e l'incertezza residua è compatibile con il rischio.

**PILOT / STAGE**

L'opzione sembra promettente ma il valore dell'informazione e la reversibilità rendono preferibile un impegno parziale.

**WAIT FOR X**

Una informazione specifica, ottenibile entro il tempo utile, potrebbe cambiare materialmente il ranking.

Il record deve indicare `X`, soglia e review date.

**NO ACTION / ABANDON**

Business as usual domina oppure nessuna opzione supera costi, rischi e opportunity cost.

Questi quattro esiti impediscono alla checklist di diventare una macchina che produce sempre “go”.

### Il gate deve essere proporzionato

Una modifica reversibile da €2.000 non richiede lo stesso livello di formalità di:

- acquisizione aziendale;
- pricing globale;
- chiusura di un mercato;
- policy su persone;
- capex pluriennale.

Ma le domande fondamentali restano le stesse.

Cambia la profondità con cui le documentiamo.

### La domanda finale

Prima di premere “send” chiediamoci:

> **Se il decision owner seguisse esattamente questa raccomandazione e l'esito fosse negativo, potremmo comunque difendere il processo usando l'evidenza, le alternative e i trade-off disponibili oggi?**

Se la risposta è no, manca ancora qualcosa nel Decision Record.

> **Il gate non serve a eliminare il rischio. Serve a impedire che assumiamo rischio senza aver chiarito quale rischio stiamo scegliendo e perché.**
