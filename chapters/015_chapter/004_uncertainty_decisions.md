## 15.3 Decidere sotto incertezza: agire, aspettare o comprare informazione

Le decisioni reali arrivano quasi sempre prima della certezza. Questo non ci obbliga a scegliere tra agire alla cieca e aspettare finché sapremo tutto. Esiste un insieme più utile di mosse:

```text
ACT
PILOT
WAIT
BUY INFORMATION
ABANDON
```

La qualità della decisione dipende anche dal saper scegliere **quale mossa è appropriata al tipo di incertezza e al costo del commitment**.

Una prima distinzione è tra incertezza realisticamente riducibile prima della deadline, incertezza che non possiamo ridurre nel tempo utile e scenario uncertainty, cioè futuri qualitativamente diversi per i quali una singola distribuzione puntuale sarebbe artificiale. Possiamo misurare il CAC di un nuovo mercato con un pilot; non possiamo conoscere con precisione la risposta di un competitor tra tre anni; possiamo invece costruire scenari credibili nei quali domanda, pricing power e costi cambiano insieme.

Questa distinzione evita una scorciatoia frequente: “servono più dati”. Prima di chiedere un'altra query o un altro modello chiediamo invece:

> **Quale informazione aggiuntiva potrebbe realmente cambiare la preferenza tra le alternative?**

Se non sappiamo nominarla, rischiamo analysis for analysis's sake. Se la risposta è precisa, il lavoro analitico diventa progettare il modo più economico e credibile per ottenerla.

### Comprare informazione con una decisione più piccola

Una società SaaS europea valuta un investimento di €2M per aprire un team locale in Portogallo. Ha già 420 clienti acquisiti organicamente, retention a 12 mesi superiore alla media europea, ARPA leggermente inferiore e forte inbound in tre verticali. Quasi non possiede, però, evidenza sul CAC di un sales motion locale.

Il management chiede se il mercato giustifica €2M. Un business case con parametri puntuali darebbe l'impressione di una previsione che i dati non possono sostenere. Il Decision Record rende invece esplicite quattro alternative:

```text
A — business as usual: continuare inbound senza team locale
B — investimento completo da €2M
C — pilot commerciale da €250k
D — partnership con reseller locale
```

La variabile che più discrimina B da C e D è il CAC ottenibile dal sales motion locale. Gli scenari iniziali sono:

| Scenario | CAC | Sales conversion | Retention 24m | Lettura |
|---|---:|---:|---:|---|
| Downside | €2.400 | 14% | 62% | investimento completo fragile |
| Centrale | €1.800 | 18% | 70% | caso interessante |
| Upside | €1.450 | 22% | 75% | forte economics |

Il team non deve conoscere oggi il futuro a 24 mesi. Deve capire se può **comprare informazione sul CAC e sulla conversion senza impegnare tutto il capitale**. La recommendation diventa quindi un pilot da €250k con criteri di go/no-go predefiniti. L'investimento completo resta un'opzione, non un impegno.

Questa non è indecisione. È una decisione progettata per apprendere.

### Value of Information: la domanda pratica prima della formula

Il Capitolo 5 ha già introdotto il Value of Information. Qui ci interessa il suo uso decisionale. Per ogni informazione candidata chiediamo:

```text
potrebbe cambiare la decisione?
quanto è plausibile che la cambi?
quanto costa ottenerla?
quanto tempo richiede?
quanto costa aspettare?
arriverà prima che la decisione perda valore?
```

Una ricerca da €100k può essere molto conveniente se evita realisticamente un commitment irreversibile da €10M. La stessa ricerca può essere inutile se richiede sei mesi e la finestra commerciale chiude tra quattro settimane.

Per questo il Decision Record deve rendere confrontabili tre costi:

```text
cost of acting wrong
cost of waiting
cost of learning
```

“Raccogliamo più dati” non è automaticamente prudenza. Aspettare può significare revenue persa, rischio non mitigato, clienti ancora esposti, capacità immobilizzata o una finestra competitiva che si chiude.

### Reversibilità cambia l'evidence threshold

Una nuova email testata sul 5% della base e la chiusura di un magazzino non richiedono lo stesso livello di evidenza. La prima decisione è economica, reversibile e con blast radius limitato; la seconda introduce transizione, perdita di capacità e costi difficili da recuperare.

Una scelta reversibile può quindi essere usata come **strumento di apprendimento**. Il *Green Book 2026* tratta esplicitamente flessibilità e real options quando incertezza e irreversibilità sono rilevanti, pur avvertendo che assegnare probabilità troppo precise a scenari fragili può introdurre spurious accuracy.[^green-book-real-options]

Nel lavoro analitico questo si traduce in pilot, rollout per regione, investimento a tranche, contratti più brevi, capacità modulare o stop/go gate. Il valore di un'opzione non è soltanto ciò che produce oggi, ma anche il diritto che conserva di scegliere diversamente domani.

### WAIT e ABANDON devono essere decisioni finite

`WAIT` è legittimo soltanto se dichiara quale informazione attendiamo e quando rivaluteremo. “Aspettiamo più dati” è procrastinazione; “non approviamo il rollout completo finché non abbiamo almeno 8 settimane di retention sul pilot e CAC sotto €1.900 su 100 lead qualificati; review il 15 novembre” è una decisione con soglia, owner e scadenza.

Anche `ABANDON` è un esito analiticamente valido. Diventa razionale quando l'upside massimo plausibile è piccolo, il downside è inaccettabile, l'informazione critica costa più del valore che potrebbe sbloccare, il costo dell'attesa domina oppure un'alternativa è chiaramente superiore. Continuare a studiare una decisione morta è un opportunity cost.

Il blocco uncertainty del Decision Record resta quindi operativo:

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

> **Una buona decisione sotto incertezza non richiede conoscere tutto. Richiede sapere quale incertezza vale la pena ridurre, quale dobbiamo accettare e quale scelta preserva il maggior valore mentre impariamo.**

[^green-book-real-options]: HM Treasury, *The Green Book 2026*, https://www.gov.uk/government/publications/the-green-book-appraisal-and-evaluation-in-central-government/the-green-book-2026
