## 17.3 “Possiamo aumentare i prezzi senza distruggere valore?”

### Caso simulato/composito: Vectora

Un e-commerce di elettronica, **Vectora**, considera un aumento medio dei prezzi del 6% per recuperare margine.

Il CFO chiede:

> “Quanto volume perderemmo?”

La domanda sembra chiedere un numero: elasticità della domanda.

Ma la decisione reale è più ampia:

> **In quali categorie un aumento di prezzo crea contribution profit incrementale senza distruggere troppo volume, acquisizione, retention o posizionamento competitivo?**

## Routing iniziale

| Elemento | Scelta |
|---|---|
| Decisione | aumento uniforme, aumento selettivo o nessun aumento |
| Failure cost | perdita di volume, erosione del margine totale, danno alla relazione con il cliente |
| Claim necessario | causale o quasi-causale sulla risposta al prezzo nei segmenti importanti |
| Reversibilità | alta per test limitati; più bassa per repricing generalizzato |
| Incertezza critica | elasticità eterogenea e reazione dei competitor |
| Stop rule | nessun +6% generalizzato basato soltanto su correlazioni storiche |

Questa classificazione rende subito evidente che una regressione sui dati storici può essere un input, non necessariamente la prova finale.

## 1. Il prezzo non è assegnato casualmente

Nei dati storici, i prodotti con prezzo più alto vendono spesso di più.

Non significa che alzare il prezzo aumenti la domanda.

I bestseller possono avere contemporaneamente:

- domanda strutturalmente più alta;
- brand più forte;
- minore comparabilità;
- disponibilità migliore;
- prezzi maggiori.

Inoltre il prezzo cambia in risposta a:

- stock;
- promozioni;
- competitor;
- stagionalità;
- domanda attesa;
- lifecycle del prodotto.

La correlazione `prezzo ↔ unità` è quindi contaminata da molte decisioni operative precedenti.

## 2. Analytical Brief: definire la funzione obiettivo

L'obiettivo non è massimizzare revenue né unità vendute.

Vectora decide di usare come outcome principale:

**contribution profit per visitatore**, con guardrail su:

- conversione;
- nuovi clienti;
- repeat purchase;
- stock turnover;
- cancellazioni;
- customer complaints;
- price index rispetto ai competitor comparabili.

Questo evita una trappola: dichiarare vincente una strategia perché aumenta il margine percentuale mentre riduce troppo il profitto totale.

## 3. Evidence Map: che cosa può spiegare la risposta osservata?

Il team separa:

- differenze cross-sectional tra SKU;
- variazioni di prezzo nel tempo sullo stesso SKU;
- promozioni;
- stock availability;
- competitor price index;
- stagionalità;
- traffico e channel mix;
- cambi di assortimento.

La prima analisi mostra che una singola elasticità media sarebbe inutile.

I segmenti si comportano in modo molto diverso:

- accessori commodity: molto elastici;
- prodotti premium esclusivi: meno elastici;
- categorie con molti competitor comparabili: più sensibili;
- articoli con stock scarso: risposta diversa;
- prodotti prossimi a una nuova generazione: elasticità instabile.

## 4. Scenario analysis prima dell'esperimento

Per ogni categoria il team costruisce scenari:

- prudente;
- centrale;
- severo.

Per ogni scenario calcola:

`prezzo × volume atteso − costo prodotto − costi variabili − costo promozionale − effetti operativi rilevanti`.

Un aumento uniforme del 6% appare fragile:

- alcune categorie migliorano il contribution profit;
- altre perdono abbastanza volume da distruggere valore;
- in alcune, l'incertezza attraversa la soglia che separa “aumentare” da “non aumentare”.

È proprio qui che entra il concetto di **switching value** del Capitolo 15.

## 5. Quale evidenza merita un test?

Non ogni categoria richiede un esperimento.

Il team classifica le categorie:

### Evidenza già sufficiente

Categorie con risposta storica stabile, rischio basso e ampia distanza dallo switching threshold.

### Decision-critical uncertainty

Categorie in cui piccoli cambi nell'elasticità cambiano la decisione.

### Non testabili facilmente

Categorie con forti interferenze, cambi assortimento o competitor response molto rapida.

L'**Experiment Contract** viene attivato soltanto sul secondo gruppo.

Dove possibile, Vectora usa test geografici o subset di SKU con guardrail definiti prima del lancio.

L'esperimento non serve a dimostrare genericamente che “il prezzo conta”. Serve a stimare la risposta utile a una decisione specifica.

## 6. Un errore sottile: il test di prezzo può cambiare il contesto

Anche un esperimento ben randomizzato può essere difficile da interpretare se:

- i competitor reagiscono al nuovo prezzo;
- i clienti confrontano SKU trattati e non trattati;
- esistono effetti di sostituzione tra prodotti;
- il test dura troppo poco per osservare repeat purchase;
- il prezzo influenza il mix di clienti acquisiti.

Per questo il claim deve essere proporzionato al design.

Un test può identificare bene l'effetto locale di un repricing in una finestra limitata senza dimostrare cosa accadrà dopo sei mesi su tutto il catalogo.

## 7. Decision Record

Le alternative sono:

### A — +6% generalizzato

Semplice da implementare, ma ignora eterogeneità e rischio competitivo.

### B — Nessun aumento

Protegge volume ma lascia margine sul tavolo nei segmenti meno elastici.

### C — Repricing selettivo con test nelle zone incerte

- `+4–7%` sui segmenti meno elastici e lontani dallo switching threshold;
- nessun aumento sulle commodity ad alta comparabilità;
- test sulle categorie intermedie;
- guardrail su conversione e nuovi clienti;
- revisione settimanale durante il rollout;
- rollback se contribution profit o guardrail superano le soglie definite.

La scelta è C.

## 8. Decision Communication Pack

La headline non è:

> “L'elasticità media è -1,2.”

È:

> **“Un +6% uniforme non è robusto: l'economia cambia molto per categoria. Abbiamo segmenti con spazio di prezzo, commodity dove il volume perso supera il beneficio e un gruppo intermedio in cui l'incertezza giustifica test limitati.”**

L'evidenza principale mostra:

1. contribution profit per scenario;
2. elasticità/range per cluster;
3. switching threshold;
4. guardrail;
5. piano di rollout e rollback.

## 9. Outcome review

Il post-decision review misura:

- contribution profit per visitor;
- unità e conversione;
- nuovi clienti;
- repeat purchase;
- competitor price index;
- stock turnover;
- effetti di sostituzione tra SKU.

L'obiettivo non è dimostrare che la previsione iniziale era perfetta.

È capire se la policy di repricing ha creato valore e se i parametri della decisione devono essere aggiornati.

## Cosa abbiamo scelto di non fare

Non serve costruire un modello strutturale perfetto di domanda per tutto il catalogo prima di decidere.

Non serve nemmeno testare ogni SKU.

La catena è proporzionata al rischio:

**Analytical Brief → EDA Evidence Map → Uncertainty Brief → Causal Identification Brief dove necessario → Experiment Contract sui segmenti decision-critical → Decision Record → Decision Communication Pack**

> **Il pricing non è trovare il prezzo più alto che il cliente sopporta. È scegliere dove il valore incrementale del prezzo supera il valore del volume perso, con un livello di evidenza proporzionato al rischio della decisione.**
