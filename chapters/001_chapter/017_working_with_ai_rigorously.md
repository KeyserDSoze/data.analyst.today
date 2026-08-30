## 1.16 Lavorare con l'AI senza perdere rigore

L'AI generativa può ridurre drasticamente il tempo necessario per molte attività dell'analista. Il rischio è confondere velocità con affidabilità.

Un metodo utile consiste nel trattare l'AI come un collaboratore molto veloce che richiede supervisione.

### 1.16.1 Usare l'AI per generare, non per decretare

L'AI è particolarmente utile per:

- proporre ipotesi;
- generare una prima query SQL;
- scrivere boilerplate Python;
- suggerire controlli di qualità;
- spiegare codice esistente;
- creare una prima bozza di documentazione;
- proporre visualizzazioni;
- elencare possibili interpretazioni alternative.

È molto meno sicuro usarla come autorità finale sulla correttezza di una metrica, di una causalità o di una decisione di business.

### 1.16.2 Separare generazione e verifica

Un workflow robusto distingue due momenti:

1. **Generazione**: produrre rapidamente candidate query, ipotesi, trasformazioni o spiegazioni.
2. **Verifica**: controllare dati, logica, assunzioni, output e coerenza con il dominio.

La stessa AI può aiutare nella verifica, ma non dovrebbe essere l'unico livello di controllo.

### 1.16.3 Chiedere sempre cosa è stato assunto

Dopo aver ottenuto una risposta, è utile chiedere:

- quali assunzioni sono state fatte;
- quali colonne o filtri sono stati usati;
- quali alternative sono state scartate;
- quali condizioni renderebbero la conclusione falsa;
- quali verifiche indipendenti effettuare.

Questo trasforma il dialogo con l'AI da semplice produzione di output a processo di controllo.

### 1.16.4 Validare con risultati noti

Se l'AI genera SQL o una misura, bisogna confrontare l'output con casi semplici di cui conosciamo il risultato.

Esempio: prima di fidarsi del “fatturato mensile”, verificare manualmente pochi ordini, un singolo giorno o una singola regione.

### 1.16.5 Rendere la semantica esplicita

La qualità dell'AI migliora quando il contesto è chiaro: nomi coerenti, descrizioni, relazioni, definizioni delle metriche e istruzioni di business riducono l'ambiguità.

Microsoft raccomanda esplicitamente di preparare dati, modelli semantici e utenti prima di usare Copilot in Power BI. La documentazione segnala che modelli poco curati e prompt vaghi possono produrre output di bassa qualità, inaccurati o fuorvianti, e che i modelli sottostanti non sono garantiti deterministici né sempre corretti.

### 1.16.6 Mantenere una traccia riproducibile

Un'analisi AI-assisted dovrebbe lasciare traccia di:

- domanda iniziale;
- definizioni usate;
- query finali;
- trasformazioni;
- dataset e versioni;
- assunzioni;
- controlli effettuati;
- decisioni prese.

L'obiettivo è fare in modo che il risultato possa essere riesaminato anche senza la conversazione originale con l'assistente.

### 1.16.7 Applicare proporzionalità al rischio

Non tutte le analisi richiedono lo stesso livello di controllo. Una query esplorativa interna può tollerare maggiore approssimazione di una decisione che influenza prezzi, credito, personale o investimenti rilevanti.

Il NIST AI Risk Management Framework e il relativo profilo per l'AI generativa propongono un approccio basato sul rischio: governance, misurazione, gestione e monitoraggio dovrebbero essere proporzionati al contesto d'uso e alle conseguenze potenziali.

### Regola operativa

> Usa l'AI per ampliare la capacità di esplorare. Usa metodo, dati e verifica per restringere ciò che sei disposto a credere.

### Riferimenti

- Microsoft Learn, *Use Copilot with semantic models in Power BI*: https://learn.microsoft.com/en-us/power-bi/create-reports/copilot-semantic-models
- Microsoft Learn, *Copilot in Power BI: Integration Overview and Benefits*: https://learn.microsoft.com/en-us/power-bi/create-reports/copilot-integration
- NIST, *Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile*: https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence
