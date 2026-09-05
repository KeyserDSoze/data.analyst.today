# Glossario

Questo glossario raccoglie i termini che nel libro hanno un significato operativo ricorrente. Non sostituisce le definizioni complete nei capitoli: serve a ritrovare rapidamente il concetto e il confine che lo rende utile.

## A

**A/B test** — Esperimento controllato in cui unità eleggibili vengono assegnate a varianti differenti per stimare l'effetto di un cambiamento sotto un disegno dichiarato.

**Activation** — Comportamento o insieme di comportamenti iniziali usati come proxy del raggiungimento di un primo valore significativo. Deve essere validato rispetto al lifecycle reale, non scelto soltanto perché facile da misurare.

**Agent / agente AI** — Sistema che usa un modello per perseguire un obiettivo attraverso più passaggi e, in alcuni casi, strumenti o azioni. Più aumenta l'autonomia, più diventano importanti scope, permessi, logging, stop condition e ownership.

**Analytical Data Contract** — Specifica del significato di un dataset analitico: grain, chiavi, popolazione, formule, semantica temporale, regole di inclusione/esclusione e assunzioni rilevanti.

**Analytics Operating Contract** — Contratto operativo di una capacità analitica ricorrente: purpose, criticality, ownership, SLO, serving states, test, incident response, change policy, cost-to-serve, adoption e retirement. Non è un contratto legale.

**Associazione** — Relazione osservata tra variabili o gruppi. Non implica automaticamente causalità.

## B

**Backfill** — Ricostruzione o ricalcolo di dati storici dopo una correzione, una nuova logica o un recupero da incidente.

**Baseline** — Punto di confronto semplice o sistema corrente contro cui valutare un metodo, un modello o una decisione nuova.

**Bias** — Errore sistematico che sposta una misura, una stima o una conclusione in una direzione. Più dati non eliminano automaticamente un bias di selezione, misurazione o design.

## C

**Calibration** — Coerenza tra probabilità previste e frequenze osservate. Un modello può ordinare bene i casi ma essere mal calibrato.

**Capstone Routing Canvas** — Artefatto del Capitolo 17 che parte da decisione, failure cost e claim necessario per scegliere il percorso minimo sufficiente di evidenze e metodi.

**Causal identification** — Argomento che collega un confronto osservabile a un effetto causale sotto assunzioni esplicite.

**Claim level** — Forza dell'affermazione autorizzata dall'evidenza: descrittiva, diagnostica, predittiva, causale o decisionale.

**Cohort** — Gruppo di unità accomunate da un evento o una caratteristica in un momento definito, seguito nel tempo per confrontare comportamento o outcome.

**Confondente / confounder** — Variabile che influenza sia esposizione/trattamento sia outcome e può distorcere un confronto causale se non gestita correttamente.

**Counterfactual / controfattuale** — Outcome che un'unità avrebbe avuto sotto un'alternativa al trattamento o alla condizione osservata. È l'oggetto mancante che una strategia causale cerca di rappresentare credibilmente.

**Criticality tier** — Livello operativo assegnato a un prodotto o workflow in base al costo del fallimento e all'importanza della decisione supportata. Determina quanto controllo è proporzionato, non quanto il prodotto è tecnicamente sofisticato.

**CUPED** — Tecnica di variance reduction che usa informazione pre-esperimento correlata con l'outcome per aumentare la precisione di una stima sperimentale.

## D

**Data contract** — Nel Capitolo 12, promessa tra producer e consumer su schema, semantica, qualità, freshness, ownership e modalità di evoluzione di un asset dati.

**Data leakage** — Uso, durante training o feature construction, di informazione che non sarebbe disponibile al prediction time o che contamina il confine tra training e valutazione.

**Data lineage** — Mappa delle dipendenze che collega sorgenti, trasformazioni, asset e consumer. È utile per root-cause analysis, impact analysis e recovery.

**Decision owner** — Persona o ruolo con autorità e responsabilità sulla scelta che l'analisi deve supportare.

**Decision quality** — Qualità del processo decisionale ex ante: alternative considerate, evidenza proporzionata, assunzioni, rischi, incertezza e switching condition. È distinta dall'outcome osservato ex post.

**Decision span** — Ampiezza con cui una persona sa accompagnare il lavoro da output ed evidenza verso alternative, decision design e, quando serve, decision system, senza oltrepassare claim o authority.

**Degraded mode** — Stato in cui un prodotto analitico continua a servire un sottoinsieme di usi con limiti espliciti, anziché fingere piena affidabilità o bloccarsi senza alternativa.

**Delegation Boundary** — Livello di esecuzione che può essere affidato a AI o agenti mantenendo una verification depth coerente con failure cost, reversibilità e maturità del workflow.

**Drift** — Cambiamento nel tempo della distribuzione dei dati, della relazione tra feature e outcome, della popolazione o del processo che può degradare comparabilità e performance.

## E

**EDA — Exploratory Data Analysis** — Esplorazione strutturata della distribuzione, delle relazioni e delle anomalie dei dati prima di irrigidire una spiegazione o un modello.

**Error budget** — Quota di mancato rispetto implicitamente compatibile con uno SLO. Serve a rendere esplicito il trade-off tra reliability e velocità di cambiamento.

**Estimand** — Quantità causale o statistica che vogliamo stimare, definita rispetto a popolazione, trattamento, confronto e outcome.

**Expected value** — Media ponderata degli esiti possibili secondo le loro probabilità. È una dimensione della decisione, non un sostituto di downside, vincoli e irreversibilità.

## F

**Freshness** — Quanto il dato disponibile è aggiornato rispetto al periodo o all'evento che dovrebbe rappresentare.

**Funnel** — Sequenza di step attraverso cui passa una popolazione. Localizza dove avviene una perdita, ma non identifica automaticamente perché avvenga.

## G

**Grain / granularità** — Che cosa rappresenta esattamente una riga o un'unità del dataset. Un grain ambiguo rende fragili join, metriche e aggregazioni.

**Guardrail** — Metrica o condizione che limita una decisione anche quando la metrica primaria migliora, perché protegge un'altra dimensione materialmente importante.

## H

**Holdout** — Porzione di dati o popolazione esclusa dal ciclo di ottimizzazione e mantenuta per una valutazione più indipendente.

## I

**Interference** — Situazione in cui il trattamento di un'unità può influenzare l'outcome di un'altra, violando l'idea che le unità siano isolate.

**Intervallo di confidenza** — Intervallo prodotto da una procedura inferenziale con una proprietà di copertura sotto assunzioni dichiarate. Non incorpora automaticamente ogni forma di bias o errore di misurazione.

## L

**Lifecycle** — Percorso temporale di un'entità attraverso stati ed eventi rilevanti, per esempio acquisizione, activation, retention, churn e riattivazione.

## M

**Materialità** — Importanza di un effetto, rischio o differenza rispetto alla decisione. Una differenza statisticamente precisa può essere economicamente o operativamente irrilevante.

**MDE — Minimum Detectable Effect** — Effetto di una certa dimensione che un disegno sperimentale è progettato per rilevare con livelli di errore/power dichiarati.

**Method Budget** — Vincolo del capstone che obbliga ogni tecnica o artefatto a giustificare quale rischio decisionale chiude. Serve a rendere visibile anche il costo della sovra-analisi.

**Metric semantic drift** — Cambiamento del significato decisionale di una metrica anche quando formula o query restano apparentemente identiche.

## O

**Observability** — Capacità di capire lo stato di un sistema attraverso segnali utili per rilevare, diagnosticare e gestire failure materialmente rilevanti.

**Outcome review** — Valutazione ex post di ciò che è accaduto dopo una decisione, separata dalla qualità del processo con cui la decisione era stata presa.

## P

**Personal Career Operating Plan** — Artefatto del Capitolo 19 che collega target responsibility, Capability Portfolio, task exposure, Delegation Boundary, verification reserve, domain/evidence portfolio, optionality e career experiments.

**Prediction time** — Momento esatto in cui una previsione viene prodotta. Determina quali informazioni sono legittimamente disponibili alle feature.

**Prediction interval** — Intervallo che rappresenta l'incertezza su un futuro valore osservabile, distinto dall'incertezza sulla sola stima di un parametro medio.

**Producer data contract** — Contratto che specifica ciò che una sorgente promette di pubblicare e come può evolvere senza sorprendere i consumer.

## R

**Randomization unit** — Unità alla quale viene assegnato il trattamento in un esperimento: utente, account, tenant, store, regione o altro cluster coerente con il rischio di interferenza.

**Reconciliation** — Confronto tra un output analitico e una fonte o relazione indipendente sufficientemente autorevole per verificare correttezza end-to-end.

**Responsibility moat** — Parte del valore professionale che resta legata a contesto, semantica, rischio, trade-off, verifica e accountability anche quando il task materiale diventa più economico da eseguire. Non implica immunità permanente dall'automazione.

**Rollback** — Ripristino di una versione precedente di codice, configurazione o servizio. Nei sistemi dati può richiedere anche backfill, cache invalidation e comunicazione ai consumer.

## S

**Semantic layer** — Livello che formalizza entità, relazioni e metriche condivise tra dati grezzi e consumo analitico.

**Sensitivity analysis** — Analisi di quanto una conclusione o scelta cambia al variare di assunzioni, parametri o scenari.

**Serving state** — Stato esplicito con cui un prodotto analitico comunica se il dato è pienamente utilizzabile, utilizzabile con caveat, stale, partial/degraded o `BLOCKED` per la decisione prevista.

**SLI — Service Level Indicator** — Misura osservata di una proprietà del servizio che conta per il consumer, per esempio freshness o completeness.

**SLO — Service Level Objective** — Target dichiarato per uno SLI.

**SLA — Service Level Agreement** — Accordo formale su un livello di servizio, eventualmente associato a conseguenze o responsabilità specifiche.

**SRM — Sample Ratio Mismatch** — Scostamento inatteso tra allocazione prevista e osservata delle unità in un esperimento. È un segnale di possibile problema nel processo sperimentale.

**Stop condition** — Condizione definita prima o durante il lavoro che impone di fermare, degradare, rivedere o non promuovere un'analisi, un esperimento, un modello o un agente.

**Switching value** — Valore di un'assunzione o parametro al quale cambia l'alternativa preferita.

## T

**Task exposure** — Quanto il costo di esecuzione di un'attività può essere compresso da AI o software. È distinto dalla responsabilità necessaria per sapere se l'attività era appropriata e corretta.

**Time-to-value** — Tempo necessario perché un utente, processo o investimento raggiunga un primo valore operativo rilevante.

## U

**Unit economics** — Relazione tra ricavi, costi variabili e valore economico a una unità decisionale coerente: cliente, ordine, workload, prodotto o altra unità.

## V

**Variance reduction** — Tecniche che riducono la variabilità di una stima senza richiedere necessariamente più traffico o osservazioni.

**Verification reserve** — Capacità residua di controllare e diagnosticare un processo anche quando una parte consistente dell'esecuzione è delegata ad AI o automazione.

## W

**Window / finestra temporale** — Intervallo di osservazione o aggregazione. La scelta della finestra modifica popolazione, maturità degli outcome e comparabilità.

> **Un termine tecnico è utile quando riduce l'ambiguità. Se la parola diventa più precisa della decisione che dovrebbe descrivere, abbiamo soltanto spostato il problema nel vocabolario.**