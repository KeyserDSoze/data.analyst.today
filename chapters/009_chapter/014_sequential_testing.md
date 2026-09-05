## 9.13 Sequential testing: quando più decision point fanno parte del design

La sezione 9.6 ha separato monitoring operativo e decisione di efficacia in un fixed-horizon test. Qui affrontiamo il caso diverso: **vogliamo intenzionalmente poter concludere a più checkpoint intermedi**.

In questo scenario non dobbiamo fingere di avere una sola analisi finale. Dobbiamo scegliere una procedura in cui il modo di guardare i dati appartenga alla matematica e alla governance dell'esperimento.

Il principio è semplice: prima del lancio definiamo quando possiamo valutare l'evidenza, quali soglie valgono ai diversi look, come controlliamo il rischio di falso positivo e quali regole consentono successo, futility o stop per danno.

Esistono famiglie diverse — group sequential designs, alpha-spending, confidence sequences/evidence processes, approcci bayesiani con decision threshold espliciti. Johari, Pekelis e Walsh hanno mostrato come p-value e intervalli “always valid” possano rendere l'inferenza coerente con optional stopping e continuous monitoring.[^johari] Il punto per il Data Analyst non è scegliere il metodo più sofisticato, ma far corrispondere **frequenza delle decisioni e procedura inferenziale**.

### Caso simulato/composito — StreamNow

StreamNow testa una nuova pricing page. Ogni settimana di test ha un costo opportunità elevato, quindi il business vuole la possibilità di concludere prima dei 14 giorni.

Il vecchio piano era:

```text
14 giorni
1 final read
```

Il nuovo piano è:

```text
checkpoint: D4, D7, D10, D14
success boundary: definita dal metodo scelto
futility: possibile solo ai checkpoint previsti
safety: continuo e separato
max duration: 14 giorni
```

Ora un risultato al D4 non è una sbirciata fortunata: è un decision point previsto, interpretato con la boundary prevista.

### Più frequente non significa più utile

Controllare ogni minuto aumenta complessità e incentiva reazioni premature senza necessariamente comprare informazione. Se l'outcome richiede sette giorni di maturity, un checkpoint orario è semanticamente vuoto anche se statisticamente implementabile.

Efficacy, futility e safety restano inoltre ragioni di stop diverse. **Efficacy** significa che l'evidenza ha superato la soglia positiva prevista. **Futility** significa che, secondo la regola progettata, continuare difficilmente produrrà l'informazione decisionale cercata. **Safety/harm** protegge il sistema e può operare con soglie più rapide e conservative.

La flessibilità è utile soltanto se è dichiarata. Non possiamo decidere dopo il fatto se il run era fixed horizon, sequential o “abbiamo aspettato finché sembrava stabile”.

### Anche un sequential design ha un orizzonte massimo

Servono maximum sample, maximum duration e una regola per il caso in cui nessuna boundary venga attraversata. **Inconclusive** è un esito legittimo.

Inoltre una boundary raggiunta presto non elimina novelty, learning, weekend mix o outcome a lungo termine. Possiamo avere abbastanza evidenza per una conclusione sul short-term effect e non ancora abbastanza osservazione per una decisione di ship. Il piano inferenziale e quello decisionale devono essere compatibili.

Microsoft, discutendo event-based A/B test, sottolinea proprio che continuous monitoring con statistiche fixed-horizon inflaziona il rischio di false positive e che, quando la decisione richiede monitoraggio ripetuto, servono procedure sequential adatte.[^ms-event]

### Sequential contract

```text
Why sequential instead of fixed horizon?
Maximum duration/sample:
Checkpoint schedule:
Method / boundary framework:
Efficacy rule:
Futility rule:
Safety rule:
Outcome maturity at each checkpoint:
Minimum calendar/exposure duration:
What happens if no boundary is crossed?
Who authorizes the decision?
```

> **Sequential testing non significa guardare più spesso. Significa progettare un esperimento in cui più momenti di decisione sono parte esplicita del metodo, invece di emergere dalla curiosità della dashboard.**

[^johari]: Johari, R., Pekelis, L. & Walsh, D.J., *Always Valid Inference: Bringing Sequential Analysis to A/B Testing*: https://arxiv.org/abs/1512.04922
[^ms-event]: Microsoft Research, *For Event-based A/B tests: why they are special*: https://www.microsoft.com/en-us/research/articles/for-event-based-a-b-tests-why-they-are-special/
