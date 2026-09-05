## 0.3 Verificare senza rifare tutto a mano

Se per usare l'AI dobbiamo replicare manualmente ogni passaggio, perdiamo gran parte del vantaggio. Se invece non verifichiamo nulla, perdiamo il controllo. La domanda utile, quindi, non è «devo ricontrollare tutto?», ma **quale sistema di controlli mi dà fiducia sufficiente per questa decisione senza duplicare l'intero lavoro?**

È la differenza tra una review artigianale, costruita ogni volta dopo che l'output esiste, e una **verification by design**, nella quale i controlli vengono scelti in base ai modi plausibili in cui il risultato potrebbe rompersi.

### Verificare significa cercare failure mode, non duplicare il lavoro

Supponiamo che un agente calcoli la revenue mensile. Riscrivere da zero la stessa query può trovare un errore di implementazione, ma non è sempre il modo più informativo di usare il tempo di review. Un controllo migliore può confrontare il totale con Finance, il numero di ordini con una sorgente operativa, la cardinalità dei join con il grain atteso e la somma dei segmenti con il totale. Un piccolo campione di record può mettere in evidenza inclusioni o esclusioni inattese; la serie storica può mostrare salti incompatibili con ciò che sappiamo del business.

Con un modello predittivo cambiano i punti di rottura e quindi cambiano i controlli. Diventano centrali la correttezza dello split, l'assenza di leakage, il confronto con una baseline semplice, le metriche su holdout, la calibrazione, la stabilità sui segmenti e il monitoraggio dopo il deployment. Con una spiegazione causale cambiano ancora: dobbiamo verificare l'ordine temporale, cercare confondenti plausibili, valutare la comparabilità dei gruppi, esaminare il disegno sperimentale o quasi-sperimentale e chiedere quali spiegazioni alternative restino compatibili con i dati.

La verifica non replica l'analisi. **La mette sotto pressione nei punti in cui un errore sarebbe più probabile o più costoso.**

### Il principio dei controlli ortogonali

Un controllo diventa particolarmente informativo quando segue una strada diversa da quella che ha prodotto il risultato. Se una query calcola fatturato per €12,4 milioni, chiedere a un secondo agente di riscrivere la stessa query usando la stessa metrica e le stesse tabelle può essere utile per intercettare un errore sintattico o logico. Ma se entrambi condividono la stessa assunzione semantica, possono concordare perfettamente e avere comunque torto.

Per aumentare l'indipendenza possiamo confrontare il fatturato con il ledger Finance, con gli incassi, con gli ordini spediti, con reconciliation già esistenti, con il trend storico o con una sorgente che abbia un grain diverso. Il valore del controllo non dipende soltanto dalla sua accuratezza; dipende anche dalla probabilità che fallisca **per un motivo diverso** rispetto al percorso che stiamo controllando.

> **Più il controllo è indipendente dall'errore che stiamo cercando, più è informativo.**

### Caso simulato/composito: la query giusta sulla tabella sbagliata

Un agente riceve il compito di calcolare il churn mensile degli abbonati. Genera una query formalmente corretta usando `subscriptions_current` e restituisce un churn del 4,1%. Il numero è plausibile, la query passa la review sintattica e un secondo agente, leggendo la stessa tabella, conferma il risultato.

Il problema è nella rappresentazione del fenomeno. `subscriptions_current` contiene soltanto lo stato corrente degli abbonamenti e rimuove le sottoscrizioni cancellate dopo 90 giorni. Il codice, quindi, non è il punto in cui nasce l'errore: la query è coerente con la tabella, ma la tabella non conserva la storia necessaria per ricostruire correttamente il churn.

Un controllo ortogonale cambia strada. Ricostruisce la metrica usando eventi di cancellazione e snapshot mensili, la confronta con la fatturazione e con il reporting Finance e ottiene un churn del 6,8%. La differenza non deriva da una formula più sofisticata, ma dall'aver messo in discussione il modello mentale del dato.

Questo è il tipo di errore che l'AI non elimina, perché nasce **prima del codice**, nella scelta di come rappresentare il fenomeno che vogliamo misurare.

### Una verification stack a quattro livelli

Per le analisi importanti conviene pensare alla verifica come a una stack. I livelli non sostituiscono uno l'altro: proteggono da famiglie di errore diverse.

| Livello | Domanda principale | Esempi di controllo |
|---|---|---|
| Deterministico | Le proprietà che devono essere vere lo sono? | `unique`, `not null`, range ammessi, referential integrity, row count, reconciliation, freshness |
| Statistico | Il comportamento del dato è compatibile con ciò che ci aspettiamo? | distribuzioni, drift, anomalie, intervalli attesi, benchmark storico, stabilità per segmento |
| Semantico | Stiamo misurando davvero il fenomeno che crediamo di misurare? | grain, definizione della metrica, denominatore, popolazione, finestra temporale, inclusioni/esclusioni, significato di date e stati |
| Decisionale | L'evidenza è sufficiente per l'azione proposta? | materialità dell'effetto, incertezza, distinzione descrizione/causalità, spiegazioni alternative, reversibilità della decisione |

I controlli deterministici sono spesso candidati naturali all'automazione, perché verificano proprietà che dovrebbero valere senza interpretazione. I controlli statistici richiedono già una baseline o un'aspettativa su ciò che il dato dovrebbe fare. I controlli semantici spostano l'attenzione dal calcolo al significato, mentre quelli decisionali chiedono se una conclusione tecnicamente corretta sia anche abbastanza forte per giustificare un'azione. Salendo nella stack aumenta il bisogno di contesto e giudizio, non perché i test automatici diventino inutili, ma perché non possono decidere da soli che cosa il business intenda per «cliente», «revenue» o «evidenza sufficiente».

### Quando gli output diventano troppi

Con sistemi agentici non è realistico leggere tutto con la stessa profondità. La review deve quindi campionare **il rischio**, non distribuire attenzione in modo uniforme. Un output ad alto impatto merita più attenzione di una bozza esplorativa; un risultato molto lontano dalla baseline è più informativo da ispezionare di uno perfettamente ordinario; casi rari, trasformazioni con molti join, modifiche a dati o sistemi e disaccordi fra agenti sono segnali che aumentano la priorità della review.

Accanto a questa selezione guidata dal rischio resta utile anche un campione casuale. Serve a intercettare failure mode che non avevamo previsto e che, proprio per questo, non avrebbero attivato nessuna regola di escalation. La logica è simile al quality control: non è necessario ispezionare ogni vite con lo stesso metodo, ma il processo deve rendere probabile l'individuazione dei difetti importanti.

Un altro modo per rendere la verifica più informativa è separare chi produce una risposta da chi ha il mandato di contestarla. Invece di chiedere a un critic agent «verifica questa analisi», possiamo chiedergli di assumere che la conclusione sia sbagliata, individuare modi plausibili in cui potremmo esserci ingannati e proporre test capaci di distinguere le alternative. Se il critic non trova errori, la conclusione non diventa automaticamente vera; il processo ha però cercato evidenza contraria invece di accumulare soltanto conferme.

La profondità della review umana deve infine seguire rischio, novità, impatto e incertezza. Diventa particolarmente importante quando un'azione è difficile da invertire, l'impatto finanziario è elevato, sono coinvolte persone o implicazioni normative, il sistema opera fuori distribuzione, gli agenti sono in disaccordo, il risultato è sorprendente o la conclusione dipende da molte assunzioni. Le linee guida Microsoft sugli agenti insistono proprio su human oversight, escalation e governance proporzionata al rischio.

Fonti:
- https://learn.microsoft.com/en-us/agents/center-of-excellence/responsible-ai
- https://learn.microsoft.com/en-us/agents/center-of-excellence/govern-agents-risk

> **Non verificare tutto allo stesso modo. Verifica in proporzione a rischio, novità, impatto e incertezza.**

Il professionista AI-native non sostituisce il lavoro manuale con la fiducia cieca. Sostituisce il controllo riga-per-riga con un sistema di evidenze, test, campionamento, audit ed escalation progettato per trovare gli errori che contano davvero.
