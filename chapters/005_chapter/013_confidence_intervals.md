## 5.12 Intervalli di confidenza: una stima dovrebbe mostrare anche la propria precisione

Una stima puntuale comprime due informazioni in una sola:

- ciò che abbiamo osservato;
- quanto è incerto ciò che stiamo stimando.

Se una survey produce `62%`, il lettore tende naturalmente a trattare quel numero come se il parametro fosse noto con precisione.

L'**intervallo di confidenza** rende visibile la seconda parte.

Per una media, in un caso classico, la struttura generale è:

\[
\text{stima} \pm \text{valore critico} \times \text{standard error}
\]

L'intervallo dipende quindi da:

- stima osservata;
- variabilità campionaria;
- numerosità effettiva;
- livello di confidenza;
- assunzioni del metodo utilizzato.

NIST descrive il confidence interval come un intervallo costruito per esprimere quanto bene una statistica campionaria approssima il parametro di popolazione.[^nist-ci]

### Caso simulato/composito — Tre filiali, tre livelli di precisione

Una banca misura il CSAT dopo un nuovo processo di onboarding.

| Filiale | CSAT stimato | Intervallo 95% | Risposte |
|---|---:|---:|---:|
| Torino Centro | 84% | 82%–86% | 1.240 |
| Novara | 87% | 79%–93% | 74 |
| Biella | 83% | 81%–85% | 1.110 |

Se guardassimo soltanto il punto centrale, Novara sarebbe prima.

Ma il suo intervallo è molto più ampio. Il campione è piccolo e il dato è compatibile con un ventaglio di valori molto più largo.

Il management non dovrebbe leggere:

> “Novara è sicuramente la filiale migliore.”

Dovrebbe leggere:

> **“Novara ha la stima puntuale più alta, ma al momento la sua performance è conosciuta con molta meno precisione.”**

È un'informazione più completa.

### Che cosa significa davvero un intervallo al 95%

Nell'interpretazione frequentista classica, dopo che l'intervallo è stato calcolato non diciamo:

> “c'è il 95% di probabilità che il parametro vero sia dentro questo specifico intervallo”.

Il parametro è trattato come fisso. È il **procedimento** ad avere una proprietà di copertura: se ripetessimo il campionamento e costruissimo ogni volta l'intervallo con lo stesso metodo, circa il 95% degli intervalli così ottenuti conterrebbe il parametro reale.

NIST sottolinea esplicitamente questa distinzione.[^nist-ci-mean]

Non serve trasformarla in una disputa filosofica davanti a un executive. Serve evitare una spiegazione statisticamente sbagliata.

### L'intervallo non contiene tutti gli errori possibili

Questo punto è ancora più importante.

Un intervallo di confidenza classico può quantificare l'incertezza dovuta al modello di campionamento e alla variabilità statistica **sotto le assunzioni adottate**.

Non incorpora automaticamente:

- selection bias;
- nonresponse bias;
- measurement error;
- definizioni sbagliate;
- dati mancanti non ignorabili;
- drift della popolazione;
- confondimento causale.

Un survey campionato male può produrre un intervallo strettissimo attorno a una stima distorta.

Quindi:

> **intervallo stretto = precisione rispetto al modello; non garanzia universale di accuratezza.**

### Precisione statistica e materialità sono due domande diverse

Una piattaforma con milioni di sessioni stima che una modifica aumenti la conversione da 4,000% a 4,015%.

Con un campione enorme l'intervallo può essere strettissimo.

La stima può quindi essere molto precisa e, contemporaneamente, economicamente irrilevante dopo costi, complessità e guardrail.

Questo ci porta a una distinzione centrale:

- **precisione:** quanto conosciamo bene l'effetto o il parametro;
- **materialità:** quanto quel valore cambia una decisione.

La sezione 5.17 tornerà esplicitamente su significatività statistica vs rilevanza business.

### Un intervallo largo può essere la risposta corretta

Un nuovo prodotto B2B ha 42 clienti. Il churn osservato è 12%, ma l'intervallo è ampio.

La conclusione professionale può essere:

> “Con i dati disponibili non possiamo ancora distinguere bene uno scenario di churn strutturalmente basso da uno potenzialmente problematico.”

Questa non è assenza di analisi.

È un'informazione decisionale: **l'evidenza disponibile non è ancora abbastanza precisa**.

A quel punto possiamo decidere se:

- aspettare altri dati;
- raccogliere informazione aggiuntiva;
- prendere una decisione reversibile;
- agire comunque perché il costo dell'attesa è maggiore.

Questa logica collegherà l'inferenza al Capitolo 15 sulla decisione.

### Come comunicare un intervallo

Per un pubblico tecnico:

> “CSAT stimato 84%, CI 95% 82%–86%, secondo il metodo e le assunzioni dichiarate.”

Per un pubblico manageriale:

> “La nostra migliore stima è 84%; la precisione del campione colloca la stima in un intervallo circa 82%–86%. Questo intervallo non include eventuali bias di raccolta.”

La seconda frase è meno elegante di un singolo `84%`, ma è molto più difficile da usare oltre ciò che i dati consentono.

> **Una stima puntuale dice dove guardare. Un intervallo dice quanto vicino possiamo vedere.**

[^nist-ci]: NIST/SEMATECH, *What are confidence intervals?*: https://www.itl.nist.gov/div898/handbook/prc/section1/prc14.htm
[^nist-ci-mean]: NIST/SEMATECH, *Confidence Limits for the Mean*: https://www.itl.nist.gov/div898/handbook/eda/section3/eda352.htm
