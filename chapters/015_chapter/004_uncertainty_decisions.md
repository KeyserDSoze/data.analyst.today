## 15.3 Decidere sotto incertezza: agire, aspettare o comprare informazione

Le decisioni reali arrivano quasi sempre prima della certezza.

Questo non significa che dobbiamo scegliere tra due estremi:

```text
agire subito senza capire
vs
aspettare finché sapremo tutto
```

Esiste uno spazio molto più utile di mosse intermedie.

```text
ACT
PILOT
WAIT
BUY INFORMATION
ABANDON
```

La qualità della decisione dipende anche dal saper scegliere **quale di queste mosse è appropriata al tipo di incertezza che abbiamo davanti**.

### Non tutta l'incertezza è uguale

Per una decisione operativa distinguiamo almeno tre categorie.

**Incertezza riducibile**

Possiamo realisticamente ottenere più informazione.

Esempi:

- non conosciamo il CAC di un nuovo mercato ma possiamo fare un pilot;
- non sappiamo il tasso di errore di un processo ma possiamo campionare manualmente;
- non conosciamo l'effetto di una feature ma possiamo sperimentare.

**Incertezza difficilmente riducibile nel tempo utile**

Potremmo saperne di più in futuro, ma non prima della decisione.

Esempi:

- risposta di un competitor;
- shock macroeconomico;
- evoluzione normativa ancora non definita;
- domanda di mercato tra tre anni.

**Incertezza strutturale / scenario uncertainty**

Non abbiamo una singola distribuzione affidabile degli esiti. Esistono futuri qualitativamente differenti.

Esempio:

- nuovo mercato cresce molto oppure resta di nicchia;
- una tecnologia diventa standard oppure viene sostituita;
- un cambio di piattaforma modifica radicalmente i costi unitari.

Questa distinzione serve perché non ogni incertezza merita altra analisi.

### La domanda chiave: cosa potrebbe davvero cambiare la scelta?

Prima di chiedere un'altra query, un altro modello o un altro workshop, chiediamo:

> **Quale informazione aggiuntiva potrebbe ribaltare la preferenza tra le alternative?**

Se non sappiamo nominare quell'informazione, rischiamo di fare analysis for analysis' sake.

Se invece la risposta è precisa, abbiamo una guida per il prossimo investimento informativo.

Esempio:

```text
Decisione:
aprire un team commerciale locale?

Uncertainty che domina:
CAC locale sostenibile

Informazione che potrebbe cambiare la decisione:
CAC osservato dopo 100 lead qualificati
```

A quel punto il lavoro analitico diventa progettare il modo più economico e credibile per ottenere quell'informazione.

### Caso simulato/composito — espansione SaaS in Portogallo

Una società SaaS europea valuta un investimento di €2M per aprire un team locale in Portogallo.

Dati disponibili:

- 420 clienti acquisiti organicamente;
- retention a 12 mesi superiore alla media europea;
- ARPA leggermente inferiore;
- forte inbound in tre verticali;
- quasi nessuna evidenza sul CAC di un motion commerciale locale.

Il management chiede:

> “Il mercato giustifica €2M?”

Una risposta falsa sarebbe produrre un unico business case con parametri puntuali e trattarlo come previsione.

Il Decision Record elenca invece:

```text
A — business as usual: continuare inbound senza team locale
B — investimento completo da €2M
C — pilot commerciale da €250k
D — partnership con reseller locale
```

La variabile che più separa B da C/D è il CAC ottenibile dal sales motion locale.

Scenari iniziali:

| Scenario | CAC | Sales conversion | Retention 24m | Lettura |
|---|---:|---:|---:|---|
| Downside | €2.400 | 14% | 62% | investimento completo fragile |
| Centrale | €1.800 | 18% | 70% | caso interessante |
| Upside | €1.450 | 22% | 75% | forte economics |

Il team non ha bisogno di conoscere subito il futuro a 24 mesi con precisione.

Ha bisogno di capire **se può comprare informazione sul CAC e sulla conversion senza impegnare tutto il capitale**.

La raccomandazione diventa:

> “Finanziare un pilot da €250k con criteri di go/no-go predefiniti. Il pilot serve a misurare CAC e funnel locale; l'investimento completo resta un'opzione, non un impegno.”

Questa non è indecisione.

È una decisione progettata per apprendere.

### Il valore dell'informazione, senza falsa precisione

In teoria possiamo formalizzare il **Value of Information**.

Nel lavoro quotidiano spesso basta una versione qualitativa molto potente.

Per ogni informazione candidata chiediamo:

```text
1. potrebbe cambiare la decisione?
2. quanto è plausibile che la cambi?
3. quanto costa ottenerla?
4. quanto tempo richiede?
5. quanto costa aspettare?
6. l'informazione arriverà prima che la decisione perda valore?
```

Se una ricerca costa €100k e può realisticamente evitare un investimento irreversibile da €10M, il suo valore può essere alto.

Se richiede sei mesi e la finestra commerciale chiude tra quattro settimane, può arrivare troppo tardi.

### Delay cost: anche aspettare è una scelta con un costo

“Raccogliamo più dati” suona prudente.

Ma aspettare può costare:

- revenue persa;
- rischio non mitigato;
- clienti esposti a un problema;
- finestra competitiva;
- capacità immobilizzata;
- apprendimento rinviato.

Il Decision Record dovrebbe quindi contenere:

```text
cost of acting wrong:
cost of waiting:
cost of learning:
```

Solo così possiamo confrontare davvero `ACT`, `WAIT` e `BUY INFORMATION`.

### Reversibilità: quando possiamo agire con meno certezza

Il livello di evidenza richiesto dovrebbe dipendere dalla reversibilità della scelta.

Confrontiamo:

**A — Testare una nuova email sul 5% della base**

- costo basso;
- rollback immediato;
- blast radius limitato.

**B — Chiudere un magazzino**

- costi di transizione elevati;
- perdita di capacità;
- difficile rollback;
- impatto su persone e servizio.

La stessa incertezza non giustifica la stessa azione.

Una scelta reversibile può essere usata come **strumento di apprendimento**.

### Real options: preservare il diritto di scegliere più avanti

Il Green Book 2026 tratta esplicitamente la flessibilità e le **real options** quando l'incertezza e l'irreversibilità sono rilevanti.

Fonte: https://www.gov.uk/government/publications/the-green-book-appraisal-and-evaluation-in-central-government/the-green-book-2026

Nel lavoro analitico la traduzione pratica è:

- pilot prima del rollout;
- contratto annuale prima di uno pluriennale;
- rollout per regione;
- investimento a tranche;
- capacità modulare;
- stop/go gate dopo nuova evidenza.

Il valore di una soluzione non è soltanto ciò che produce oggi.

Può includere **la flessibilità che preserva domani**.

### Una decisione può essere “non ancora”

`WAIT` è legittimo soltanto se contiene una condizione esplicita.

Debole:

> “Aspettiamo più dati.”

Forte:

> “Non approviamo il rollout completo finché non abbiamo almeno 8 settimane di retention sul pilot e CAC sotto €1.900 su 100 lead qualificati. Review il 15 novembre.”

Ora l'attesa ha:

- informazione richiesta;
- soglia;
- owner;
- data di revisione.

Non è procrastinazione indefinita.

### Quando abbandonare

Anche `ABANDON` è una decisione analitica.

Può diventare razionale quando:

- l'upside massimo plausibile è piccolo;
- il downside è inaccettabile;
- le informazioni critiche sono troppo costose da ottenere;
- il costo dell'attesa supera il valore potenziale;
- un'alternativa domina chiaramente;
- il problema non è più strategicamente rilevante.

Continuare a studiare una decisione morta consuma capacità che potrebbe essere usata altrove.

### Decision Record — blocco uncertainty

```text
key uncertainty:
why it matters:
reducible before deadline?: yes/no/partly
information that could flip choice:
cost to learn:
time to learn:
cost of waiting:
reversibility of current options:
pilot / staged option available?:
next information gate:
review date:
```

### Regola operativa

Quando manca certezza non chiediamo automaticamente “servono più dati?”.

Chiediamo:

1. quale incertezza domina la scelta?
2. è realmente riducibile?
3. quale informazione potrebbe cambiare decisione?
4. quanto costa ottenerla?
5. quanto costa aspettarla?
6. possiamo comprare informazione con una scelta più piccola e reversibile?
7. qual è il punto in cui smettiamo di analizzare e scegliamo?

> **Una buona decisione sotto incertezza non richiede conoscere tutto. Richiede sapere quale incertezza vale la pena ridurre, quale dobbiamo accettare e quale scelta preserva il maggior valore mentre impariamo.**
