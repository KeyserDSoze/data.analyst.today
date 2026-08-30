## 7.8 Il forecast non è un numero: gli intervalli di previsione

Molte dashboard mostrano il futuro con una singola linea. È elegante, leggibile e spesso fuorviante.

Un forecast puntuale come "la domanda prevista per ottobre è 12.400 unità" dà l'impressione che il futuro sia stato stimato con precisione. In realtà un modello serio dovrebbe comunicare anche quanta incertezza esiste intorno a quella previsione.

### Caso realistico: 12.400 unità non significa 12.400 unità

Un produttore di elettrodomestici deve decidere quante unità di un nuovo forno ordinare per il mercato italiano nel mese di ottobre.

Il modello produce:

- forecast puntuale: 12.400 unità;
- intervallo di previsione 80%: 11.300-13.600;
- intervallo di previsione 95%: 10.400-14.700.

Se il responsabile acquisti riceve solo 12.400, potrebbe interpretarlo come una stima quasi certa. Gli intervalli raccontano invece una storia diversa: lo scenario plausibile è ampio.

Questo cambia la decisione.

Se lo stock-out costa molto, può avere senso ordinare più vicino alla parte alta dell'intervallo. Se l'obsolescenza è costosa, può essere preferibile un ordine più prudente con possibilità di riapprovvigionamento.

Il forecast, quindi, non decide da solo. Offre una distribuzione di scenari che deve essere collegata ai costi delle decisioni.

### Intervallo di confidenza e intervallo di previsione non sono la stessa cosa

È utile separare due idee:

- un **intervallo di confidenza** riguarda l'incertezza sulla stima di un parametro;
- un **intervallo di previsione** riguarda l'incertezza su una futura osservazione.

Il secondo è normalmente più largo perché deve incorporare non solo l'incertezza del modello, ma anche la variabilità futura del fenomeno.

### L'incertezza cresce con l'orizzonte

Prevedere domani è generalmente più facile che prevedere tra dodici mesi.

Per questo un forecast corretto dovrebbe mostrare intervalli che tendono ad allargarsi con l'orizzonte.

Un modello che presenta la stessa precisione apparente a 7, 30 e 365 giorni merita attenzione: potrebbe non rappresentare adeguatamente l'incertezza.

### Caso realistico: il budget costruito sulla linea centrale

Una società SaaS prepara il piano annuale usando un forecast del new ARR:

| Trimestre | Forecast ARR nuovo |
|---|---:|
| Q1 | 4,8 M€ |
| Q2 | 5,2 M€ |
| Q3 | 5,7 M€ |
| Q4 | 6,1 M€ |

Il CFO costruisce costi, assunzioni e investimenti sulla linea centrale. A metà anno, il risultato è del 9% sotto il forecast e parte un piano di riduzione dei costi.

Il problema non era necessariamente che il modello fosse "sbagliato". L'analisi ex post mostra che il risultato reale era ancora dentro l'intervallo di previsione 80%.

Il vero errore era organizzativo: il piano aziendale aveva trasformato una previsione probabilistica in una promessa.

Da quel momento l'azienda costruisce tre scenari:

- downside;
- base;
- upside.

Le assunzioni di spesa vengono associate a soglie e trigger espliciti.

### Forecast probabilistico e decisione

Quando l'incertezza ha valore economico, possiamo spingerci oltre il singolo intervallo e ragionare in termini di probabilità:

- probabilità di superare la capacità produttiva;
- probabilità di scendere sotto una soglia di cassa;
- probabilità di mancare l'SLA;
- probabilità di esaurire lo stock;
- probabilità di raggiungere il target.

A quel punto il forecast diventa un vero strumento di decisione.

> **Una previsione senza incertezza è spesso una narrazione troppo precisa di un futuro che preciso non è.**

### Riferimenti

- NIST, materiali sugli intervalli statistici e prediction intervals: https://www.nist.gov/publications/fiducial-prediction-intervals
- Hyndman, R.J. & Athanasopoulos, G., *Forecasting: Principles and Practice*, 3rd edition: https://otexts.com/fpp3/
