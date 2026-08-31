## 0.3 Verificare senza rifare tutto a mano

Se per usare l'AI dobbiamo replicare manualmente ogni passaggio, perdiamo gran parte del vantaggio.

Se invece non verifichiamo nulla, perdiamo il controllo.

La domanda utile non è:

> “Devo ricontrollare tutto?”

È:

> **“Quale sistema di controlli mi dà fiducia sufficiente per questa decisione senza duplicare l'intero lavoro?”**

Questa è la differenza tra review artigianale e **verification by design**.

### Verificare non significa duplicare

Un buon controllo cerca i punti in cui il risultato potrebbe rompersi.

Se un agente calcola la revenue mensile, non è sempre necessario riscrivere la stessa query da zero. Possiamo controllare, per esempio:

- il totale contro Finance;
- il numero di ordini contro una sorgente operativa;
- la cardinalità dei join;
- alcuni record campione;
- la somma dei segmenti rispetto al totale;
- la coerenza con periodi precedenti;
- valori impossibili o salti inattesi.

Se un agente costruisce un modello predittivo, i controlli cambiano:

- split corretto;
- assenza di leakage;
- confronto con una baseline semplice;
- metriche su holdout;
- calibrazione;
- stabilità sui segmenti;
- monitoraggio dopo il deployment.

Se propone una spiegazione causale, cambiano ancora:

- ordine temporale;
- confondenti plausibili;
- gruppi comparabili;
- design sperimentale o quasi-sperimentale;
- spiegazioni alternative compatibili con i dati.

La verifica non replica l'analisi. **La mette sotto pressione nei punti in cui un errore sarebbe più probabile o più costoso.**

### Il principio dei controlli ortogonali

Un controllo è particolarmente informativo quando usa una strada diversa da quella che ha prodotto il risultato.

Supponiamo che una query calcoli fatturato per €12,4 milioni. Chiedere a un secondo agente di riscrivere la stessa query, con la stessa metrica e le stesse tabelle, può essere utile per trovare errori di implementazione.

Ma non ci protegge necessariamente da un'assunzione semantica condivisa.

Se entrambe le query usano la tabella sbagliata, possono concordare perfettamente.

Per aumentare l'indipendenza possiamo confrontare il risultato con:

- ledger Finance;
- incassi;
- ordini spediti;
- reconciliation esistenti;
- trend storici;
- una sorgente con grain diverso.

> **Più il controllo è indipendente dall'errore che stiamo cercando, più è informativo.**

### Caso simulato/composito: la query giusta sulla tabella sbagliata

Un agente riceve il compito:

> “Calcola il churn mensile degli abbonati.”

Genera una query formalmente corretta usando `subscriptions_current` e restituisce un churn del 4,1%.

Il numero è plausibile. La query passa la review sintattica. Un secondo agente, leggendo la stessa tabella, conferma il risultato.

Il problema è nella sorgente: `subscriptions_current` contiene soltanto lo stato corrente degli abbonamenti e rimuove le sottoscrizioni cancellate dopo 90 giorni.

La query è corretta. Il modello mentale del dato è sbagliato.

Un controllo ortogonale ricostruisce la metrica usando eventi di cancellazione, snapshot mensili, fatturazione e confronto con il reporting Finance.

Il churn risulta 6,8%.

Questo è il tipo di errore che l'AI non elimina, perché nasce **prima del codice**: nella scelta della rappresentazione del fenomeno.

### Una verification stack a quattro livelli

Per analisi importanti è utile distinguere quattro famiglie di controllo.

#### 1. Controlli deterministici

Verificano proprietà che dovrebbero essere vere senza interpretazione:

- `unique`;
- `not null`;
- range ammessi;
- referential integrity;
- row count;
- reconciliation;
- freshness.

Sono candidati naturali all'automazione.

#### 2. Controlli statistici

Verificano se il comportamento del dato è compatibile con ciò che ci aspettiamo:

- distribuzioni;
- drift;
- anomalie;
- intervalli attesi;
- benchmark storico;
- stabilità per segmento.

#### 3. Controlli semantici

Verificano che stiamo misurando davvero il fenomeno che crediamo di misurare:

- grain;
- definizione della metrica;
- denominatore;
- popolazione;
- finestra temporale;
- inclusioni ed esclusioni;
- significato delle date e degli stati.

#### 4. Controlli decisionali

Verificano se l'evidenza è sufficiente per l'azione proposta:

- l'effetto è materialmente rilevante?
- l'incertezza è compatibile con la decisione?
- stiamo descrivendo o sostenendo una relazione causale?
- esiste una spiegazione alternativa credibile?
- la decisione è reversibile se l'ipotesi si rivela sbagliata?

I primi livelli possono essere automatizzati molto. Gli ultimi richiedono più contesto e giudizio.

### Quando gli output diventano troppi: campionare il rischio

Con sistemi agentici non è realistico leggere tutto con la stessa profondità.

La review può concentrarsi su:

- output ad alto impatto;
- risultati molto diversi dalla baseline;
- casi rari o fuori distribuzione;
- analisi con molti join o trasformazioni;
- output che modificano dati o sistemi;
- casi in cui gli agenti sono in disaccordo;
- un campione casuale, utile per intercettare failure mode non previsti.

La logica è simile al quality control: non serve ispezionare ogni vite con lo stesso metodo, ma il processo deve rendere probabile l'individuazione dei difetti importanti.

### Usare un agente come critico

Un pattern utile è separare chi produce la risposta da chi ha il mandato di contestarla.

Invece di chiedere:

> “Verifica questa analisi.”

possiamo chiedere:

> “Assumi che questa conclusione sia sbagliata. Trova tre modi plausibili in cui potremmo esserci ingannati e proponi test che distinguano le alternative.”

Il fatto che un critic agent non trovi errori non rende automaticamente vera la conclusione. Ma costringe il processo a cercare evidenza contraria invece di accumulare soltanto conferme.

### La profondità della review deve seguire il rischio

La review umana approfondita diventa particolarmente importante quando:

- l'azione è difficile da invertire;
- l'impatto finanziario è elevato;
- sono coinvolte persone;
- esistono implicazioni normative;
- il sistema opera fuori distribuzione;
- gli agenti sono in disaccordo;
- il risultato è nuovo o sorprendente;
- la conclusione dipende da molte assunzioni.

Le linee guida Microsoft sugli agenti insistono su human oversight, escalation e governance proporzionata al rischio.

Fonti:
- https://learn.microsoft.com/en-us/agents/center-of-excellence/responsible-ai
- https://learn.microsoft.com/en-us/agents/center-of-excellence/govern-agents-risk

> **Non verificare tutto allo stesso modo. Verifica in proporzione a rischio, novità, impatto e incertezza.**

Il professionista AI-native non sostituisce il lavoro manuale con la fiducia cieca. Sostituisce il controllo riga-per-riga con un sistema di evidenze, test, campionamento, audit ed escalation.
