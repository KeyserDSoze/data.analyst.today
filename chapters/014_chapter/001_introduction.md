# Capitolo 14 — AI-assisted analytics: accelerare senza perdere rigore

L'intelligenza artificiale generativa sta cambiando rapidamente il lavoro analitico. Oggi un analista può chiedere a un assistente AI di scrivere SQL, generare Python, spiegare una query, proporre visualizzazioni, riassumere una tabella, suggerire ipotesi, documentare un modello e persino orchestrare una sequenza di attività.

Questo non elimina il lavoro dell'analista. Sposta il punto in cui si concentra il valore.

Quando il costo della sintassi diminuisce, aumentano di importanza:

- la qualità della domanda;
- la semantica delle metriche;
- la qualità dei dati;
- la verifica dell'output;
- la scelta del metodo;
- il controllo delle assunzioni;
- il giudizio sul fatto che una conclusione sia sufficientemente affidabile per una decisione.

Un modello generativo può produrre una query elegante che risponde alla domanda sbagliata. Può creare una regressione perfettamente eseguibile su un target contaminato. Può riassumere con sicurezza un pattern che dipende da un join duplicante. Può inventare colonne plausibili che non esistono. Può scegliere la data sbagliata in un modello semantico e restituire un risultato formalmente coerente ma business-wise errato.

Per questo il principio del capitolo è:

> **AI-assisted analytics non significa delegare il giudizio. Significa comprimere il costo dell'esecuzione e reinvestire il tempo risparmiato in verifica, interpretazione e decisione.**

## Un caso realistico: il query assistant che "salva" tre ore e quasi costa €400.000

Una marketplace company vuole sapere perché il Gross Merchandise Value del Sud Europa è sceso del 7,2% nell'ultima settimana.

Un analyst chiede a un assistente AI:

> "Scrivi una query SQL che confronti GMV per paese e categoria rispetto alla settimana precedente e identifichi i driver principali."

L'assistente genera in pochi secondi una query complessa con CTE, window functions e ranking dei contributi.

La query gira senza errori. Il risultato mostra che la categoria Electronics in Spagna è responsabile di quasi metà del calo.

Il team commerciale prepara una campagna promozionale da €400.000.

Prima del lancio, però, un secondo analyst nota che la query usa `order_created_at` mentre il KPI ufficiale GMV del finance team usa `payment_captured_at`. Durante quella settimana un problema di PSP aveva spostato molti pagamenti al giorno successivo.

Usando la data corretta, il calo reale è soltanto dell'1,4% e il driver principale non è Electronics ma un ritardo operativo in Portogallo.

L'AI aveva scritto SQL corretto. Il problema era semantico.

Questa distinzione accompagnerà tutto il capitolo:

**correttezza sintattica ≠ correttezza analitica ≠ correttezza decisionale**

## Dalla copilota all'agente

Possiamo pensare a tre livelli di uso dell'AI nel lavoro analitico.

### Livello 1 — Assistente

L'AI aiuta in attività locali:

- spiega una formula;
- suggerisce SQL;
- corregge un errore Python;
- propone un grafico;
- riscrive una documentazione.

### Livello 2 — Copilota analitico

L'AI partecipa a una sequenza di ragionamento:

- interpreta la richiesta;
- propone un piano;
- genera codice;
- confronta risultati;
- suggerisce verifiche;
- prepara un summary.

### Livello 3 — Workflow agentico

L'AI può usare strumenti e compiere più passi:

1. interrogare un semantic model;
2. eseguire query;
3. controllare anomalie;
4. produrre un report;
5. confrontare il risultato con una baseline;
6. richiedere approvazione umana prima di un'azione.

Più aumenta l'autonomia, più devono aumentare controlli, logging, limiti, test e governance.

## Perché il semantic layer diventa ancora più importante

La generazione naturale di query non riduce il bisogno di semantica condivisa. Lo aumenta.

Microsoft documenta che Copilot in Power BI dipende fortemente dalla preparazione del semantic model: nomi, descrizioni, relazioni, misure, organizzazione e linguistic modeling influenzano direttamente la qualità delle risposte. La documentazione avverte anche che output inaccurate o misleading restano possibili e che gli utenti devono valutare criticamente i risultati.

In altre parole, l'AI non elimina il problema della semantica. Lo rende più visibile.

Se un'organizzazione ha cinque definizioni diverse di "cliente attivo", un assistente AI non può inventare quale sia quella corretta per il board.

## La nuova unità di lavoro dell'analista

Nel lavoro tradizionale la sequenza era spesso:

**domanda → query → risultato → slide**

Con l'AI diventa più utile pensare a:

**domanda → contesto → specifica → generazione → verifica → stress test → interpretazione → decisione**

La qualità della specifica e della verifica diventa centrale.

## Obiettivo del capitolo

Alla fine del capitolo dovresti essere in grado di:

- formulare prompt analitici robusti;
- usare AI per SQL, Python e documentazione senza delegare la semantica;
- riconoscere hallucination e semantic errors;
- verificare numeri e codice generati;
- usare AI per EDA e debugging;
- costruire workflow human-in-the-loop;
- capire quando un agentic workflow è utile e quando è eccessivo;
- distinguere velocità di produzione da affidabilità della conclusione.

### Fonti

- NIST, *Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile*, https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence
- Microsoft Learn, *Use Copilot with semantic models in Power BI*, https://learn.microsoft.com/en-us/power-bi/create-reports/copilot-semantic-models
