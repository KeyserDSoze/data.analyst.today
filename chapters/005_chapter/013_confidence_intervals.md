## 5.12 Intervalli di confidenza: mostrare la precisione insieme alla stima

Una stima puntuale è facile da comunicare perché sembra completa. “CSAT 84%”, “conversion 6,1%”, “tempo medio 31,4 minuti” occupano poco spazio e invitano il lettore a trattare il numero come se il parametro fosse noto esattamente.

Lo standard error ci ha mostrato che non è così. Un campione diverso avrebbe prodotto una stima diversa. L'**intervallo di confidenza** porta quella variabilità accanto al punto centrale invece di nasconderla.

In un caso classico la struttura è:

`stima ± valore critico × standard error`.

La larghezza dell'intervallo dipende quindi dalla variabilità campionaria, dalla numerosità informativa, dal livello di confidenza e dal metodo utilizzato. NIST descrive il confidence interval proprio come uno strumento per rappresentare quanto bene una statistica campionaria approssima il parametro della popolazione.[^nist-ci]

## Tre filiali, tre quantità di informazione

Una banca misura il CSAT dopo un nuovo processo di onboarding:

| Filiale | CSAT stimato | Intervallo 95% | Risposte |
|---|---:|---:|---:|
| Torino Centro | 84% | 82%–86% | 1.240 |
| Novara | 87% | 79%–93% | 74 |
| Biella | 83% | 81%–85% | 1.110 |

Se ordinassimo soltanto la stima puntuale, Novara sarebbe la migliore. L'intervallo racconta però che quella posizione è sostenuta da molta meno informazione: il 87% è compatibile, secondo il modello utilizzato, con un ventaglio di valori molto più ampio.

La conclusione corretta non è “Novara è sicuramente la filiale migliore”, ma:

> **Novara ha la stima puntuale più alta, ma la sua performance è conosciuta con molta meno precisione.**

Il ranking smette così di confondere livello osservato e certezza della stima.

## Che cosa significa davvero “95%”

Nell'interpretazione frequentista classica, dopo aver calcolato un intervallo specifico non diciamo che “c'è il 95% di probabilità che il parametro vero sia dentro”. Il parametro viene trattato come fisso. È il **procedimento** a possedere una proprietà di copertura: se ripetessimo molte volte lo stesso disegno di campionamento e costruissimo ogni volta l'intervallo con lo stesso metodo, circa il 95% degli intervalli conterrebbe il parametro reale.

NIST esplicita questa distinzione nelle sue pagine sui confidence limits.[^nist-ci-mean]

Davanti a un pubblico manageriale non serve trasformare il risultato in una lezione filosofica. Serve però non attribuire all'intervallo una probabilità che il metodo frequentista non sta calcolando.

## Un intervallo quantifica soltanto l'incertezza che il metodo sa vedere

Questa limitazione è più importante della distinzione terminologica. Un confidence interval classico può quantificare bene la variabilità campionaria sotto un certo disegno e un insieme di assunzioni. Non incorpora automaticamente selection bias, nonresponse bias, measurement error, definizioni sbagliate, missing non ignorabili, drift della popolazione o confondimento causale.

Una survey selezionata male può produrre un intervallo strettissimo attorno a una stima distorta. Per questo:

> **intervallo stretto significa precisione rispetto al modello; non garanzia universale di accuratezza.**

È il motivo per cui il Capitolo 5 continua a dipendere dai Capitoli 2 e 3. Prima dobbiamo aver definito correttamente il fenomeno e capito come i dati lo rappresentano; solo allora ha senso quantificare con precisione la variabilità della stima.

## Precisione e materialità non sono la stessa domanda

Una piattaforma con milioni di sessioni può stimare che una modifica aumenti la conversione da 4,000% a 4,015% con un intervallo molto stretto. Possiamo conoscere quell'effetto con grande precisione e scoprire comunque che è economicamente irrilevante dopo costi, complessità e guardrail.

Al contrario, un nuovo prodotto B2B con 42 clienti può mostrare churn del 12% e un intervallo molto ampio. La conclusione professionale può essere che, con i dati attuali, non riusciamo ancora a distinguere bene uno scenario sano da uno problematico. L'intervallo largo non è un fallimento dell'analisi: è **la misura corretta della poca informazione disponibile**.

A quel punto la decisione può essere aspettare, raccogliere nuovi dati, agire in modo reversibile oppure intervenire comunque perché il costo dell'attesa è maggiore. L'inferenza non elimina la scelta; rende visibile quanto stiamo scegliendo sotto incertezza.

Per un pubblico tecnico possiamo riportare:

> `CSAT 84%, CI 95% 82%–86%, secondo metodo e assunzioni dichiarate.`

Per un pubblico manageriale possiamo tradurre senza perdere il caveat:

> `La migliore stima è 84%; l'incertezza di campionamento la colloca circa tra 82% e 86%. L'intervallo non include eventuali bias di raccolta.`

La seconda frase è più lunga di un singolo KPI, ma impedisce al lettore di attribuire al numero una precisione che non possiede.

> **Una stima puntuale dice dove guardare. Un intervallo dice quanto precisamente riusciamo a vedere quel punto sotto il metodo che abbiamo scelto.**

---

### Fonti

[^nist-ci]: NIST/SEMATECH, *What are confidence intervals?*. https://www.itl.nist.gov/div898/handbook/prc/section1/prc14.htm
[^nist-ci-mean]: NIST/SEMATECH, *Confidence Limits for the Mean*. https://www.itl.nist.gov/div898/handbook/eda/section3/eda352.htm
