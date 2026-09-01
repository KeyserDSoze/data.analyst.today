## 9.13 Sequential testing: progettare una decisione che può arrivare prima

La sezione 9.6 ha fissato il problema del peeking in un fixed-horizon test.

Qui affrontiamo il caso diverso:

> **vogliamo intenzionalmente poter prendere una decisione a più checkpoint intermedi.**

In questo caso non dobbiamo fingere di avere una singola analisi finale.

Dobbiamo progettare un **sequential experiment**.

### Il principio

Una procedura sequenziale definisce prima:

- quando possiamo valutare i dati;
- quali soglie valgono a ogni look;
- come viene controllato il rischio di falso positivo;
- quali regole consentono successo, futility o stop per danno.

Non esiste una sola metodologia sequenziale.

Possiamo incontrare, tra le altre:

- group sequential designs;
- alpha-spending approaches;
- sempre-validi confidence sequences / evidence processes;
- metodi bayesiani con decision threshold espliciti.

Per il Data Analyst il punto non è scegliere un metodo per moda.

È garantire coerenza tra **frequenza delle decisioni e inferenza**.

### Caso simulato/composito — Pricing page ad alto traffico

StreamNow testa una nuova pricing page.

Il business vorrebbe una decisione il prima possibile perché ogni settimana di test ha costo opportunità elevato.

Piano fixed-horizon precedente:

```text
14 giorni
1 final read
```

Nuovo piano sequenziale:

```text
checkpoint: D4, D7, D10, D14
success boundary: definita dal metodo scelto
futility: possibile solo dai checkpoint previsti
safety: continuo e separato
max duration: 14 giorni
```

Il team non dice più:

> “Abbiamo guardato al D4 e per fortuna era significativo.”

Dice:

> “D4 era un decision point previsto e la soglia usata è quella compatibile con il sequential design.”

### Sequential non significa decisione continua su ogni evento

Più frequente non significa necessariamente migliore.

Controllare ogni minuto può:

- aumentare complessità;
- rendere governance poco trasparente;
- incoraggiare decisioni troppo reattive;
- avere scarso valore se l'outcome matura lentamente.

Se una metrica richiede sette giorni di maturity, un checkpoint ogni ora è semanticamente inutile.

### Efficacy, futility e safety

È utile distinguere tre ragioni di stop.

**Efficacy**

L'evidenza ha superato la soglia prevista per una decisione positiva.

**Futility**

Il design conclude che continuare difficilmente produrrà l'informazione decisionale desiderata secondo la regola stabilita.

**Safety / harm**

Un guardrail grave richiede intervento operativo.

Safety può avere logica diversa e molto più rapida rispetto all'inferenza sulla primary.

### Optional stopping deve essere parte del design

La flessibilità è utile solo se documentata.

Un team non dovrebbe scegliere dopo il fatto se interpretare il test come:

- fixed horizon;
- sequential;
- “abbiamo aspettato finché l'effetto si è stabilizzato”.

L'Experiment Contract deve fissare il regime prima del lancio.

### Durata massima resta importante

Anche un sequential design deve avere una domanda su:

- maximum sample;
- maximum duration;
- practical stopping point.

Se non raggiungiamo nessuna boundary entro la fine, il risultato può essere **inconclusive**.

“Inconclusivo” è un esito legittimo.

### Sequential e novelty

Raggiungere una success boundary molto presto non risolve automaticamente i problemi di:

- novelty;
- learning;
- weekend mix;
- long-term outcome.

Possiamo avere una regola statistica che autorizza una conclusione sul **short-term effect**, ma una decisione di ship può richiedere comunque una minimum exposure age o guardrail maturi.

Il piano statistico e il piano decisionale devono essere compatibili.

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

> **Sequential testing non è guardare più spesso. È progettare in anticipo una procedura in cui guardare più volte è parte della matematica e della governance.**
