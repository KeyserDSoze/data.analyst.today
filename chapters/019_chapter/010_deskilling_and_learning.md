## 19.9 Verification reserve: che cosa dobbiamo continuare a sapere anche quando deleghiamo

Uno dei rischi professionali più interessanti dell'AI non è la sostituzione immediata, ma il **deskilling graduale**. Quando un sistema esegue bene una parte crescente del lavoro possiamo perdere lentamente la capacità di svolgerlo, valutarlo, diagnosticare quando cambia e intervenire quando l'automazione esce dai confini attesi.

Non ogni perdita di manualità è negativa. Non serve ricordare a memoria ogni funzione di un database o ogni flag di una CLI. Il rischio nasce quando esternalizziamo **la competenza che ci serviva per controllare il processo che stiamo delegando**.

Per distinguere le due cose è utile una semplice classificazione.

| Categoria | Che cosa contiene | Regola |
|---|---|---|
| Must internalize | grain, cardinality, denominator, population, time semantics, uncertainty, causal vs predictive claim, leakage, randomization, baseline, cost asymmetry, unit economics, decision threshold | il modello mentale deve restare abbastanza forte da riconoscere una violazione |
| Can delegate, must inspect | SQL complesso, feature pipeline, visualization code, experiment analysis, forecast code, documentazione, test generation | l'esecuzione può essere delegata, la struttura e i failure mode devono restare leggibili |
| Safe to externalize | sintassi rara, nome esatto di una funzione, boilerplate, conversioni meccaniche, flag occasionali | recupero on demand è spesso sufficiente |

Questa distinzione porta a un concetto centrale del capitolo: la **verification reserve**, cioè la capacità residua di controllare un processo anche quando l'AI esegue quasi tutto il lavoro. Se un agente SQL è affidabile da un anno, la reserve non consiste nel riscrivere ogni query. Consiste nel sapere ancora chiedere se una join moltiplica il grain, se il filtro è applicato prima o dopo l'aggregazione, se il denominator è coerente, se la data è davvero `as-of` e se una tabella rappresenta uno snapshot o una event history.

Quando questa reserve scende a zero, la delega diventa dipendenza.

Un caso lo mostra bene. Un team usa da diciotto mesi un agente SQL con qualità media elevata. Gradualmente gli analyst smettono di leggere la query e controllano soltanto il risultato. Poi `customer_status` cambia rappresentazione: da snapshot giornaliero diventa event history. L'agente continua a produrre SQL sintatticamente corretto ma interpreta ogni riga come stato corrente. I customer count si duplicano e l'errore rimane invisibile per tre settimane.

Il modello non è necessariamente peggiorato. È cambiato il sistema attorno a lui e il team aveva perso proprio il controllo che avrebbe riconosciuto il nuovo grain temporale.

La ricerca disponibile offre un segnale coerente con questo rischio, ma va calibrata correttamente. Uno studio Microsoft Research presentato a CHI 2025 ha raccolto **936 esempi** di utilizzo della GenAI da **319 knowledge worker**. Nel campione auto-riferito, maggiore fiducia nella GenAI è associata a minore enactment/effort di critical thinking; gli autori osservano inoltre che parte del lavoro critico si sposta verso information verification, response integration e task stewardship.

Fonte: https://www.microsoft.com/en-us/research/publication/the-impact-of-generative-ai-on-critical-thinking-self-reported-reductions-in-cognitive-effort-and-confidence-effects-from-a-survey-of-knowledge-workers/

Lo studio è survey/self-report: non dimostra causalmente che l'AI provochi deskilling. È però sufficiente a ricordare un failure mode plausibile: **quando cresce la fiducia nell'automazione, il critical engagement non può essere lasciato al caso**.

La risposta non è conservare artificialmente frizione in produzione. È progettare deliberate practice sui modelli mentali che proteggono il lavoro. Una “palestra analitica” può includere bug hunt su query generate, semantic reconstruction a partire da una definizione business, causal critique, review di experiment con SRM o contamination, forecast stress test, AI red-team e spiegazioni senza tool del fenomeno, dell'assunzione critica e del risultato che cambierebbe la decisione.

In training può essere utile anche introdurre **deliberate friction**: formulare l'ipotesi prima di chiedere alternative all'AI, stimare l'ordine di grandezza prima di vedere il risultato, definire il test plan prima del codice o elencare i failure mode prima di chiedere una review. La frizione è utile quando costruisce un modello mentale; è inutile quando diventa rituale o rallenta un processo produttivo senza ridurre rischio.

La stessa AI può essere usata come coach: generare casi con bug, criticare una causal claim, simulare uno stakeholder ostile, proporre edge case o nascondere la soluzione finché non abbiamo espresso una previsione. Il learning design conta più della presenza o assenza dello strumento.

Anche la manutenzione delle competenze dovrebbe seguire il rischio, non una cadenza rituale. Conviene mantenere una pratica profonda sugli output AI che incontriamo davvero, tornare periodicamente su una competenza fondamentale senza scorciatoie e usare incidenti e postmortem per aggiornare la propria failure-mode library. Ogni tanto vale anche la pena affrontare un caso fuori dalla comfort zone per capire quali parti del nostro modello mentale sono diventate dipendenti dal contesto abituale.

L'obiettivo dell'apprendimento cambia quindi da semplice capacità di produrre a capacità di **specificare, verificare, falsificare, intervenire e spiegare**.

> **Usare meno una competenza non significa poter smettere di possederla. Se quella competenza protegge il confine tra output plausibile ed evidenza affidabile, deve restare viva.**