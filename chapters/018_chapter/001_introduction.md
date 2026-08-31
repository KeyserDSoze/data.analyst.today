# Capitolo 18 — Costruire un sistema analitico che scala

Una buona analisi risolve una domanda.

Un buon sistema analitico evita che la stessa domanda debba essere risolta da zero ogni settimana.

Questa distinzione sembra banale, ma segna il passaggio tra un team che produce insight e un'organizzazione che riesce a utilizzare dati in modo affidabile nel tempo.

Un analista può costruire una query impeccabile, una dashboard utile o un modello che migliora una decisione. Ma se il risultato dipende da passaggi manuali, definizioni non documentate, file locali, controlli informali e conoscenza custodita nella testa di una sola persona, il valore creato resta fragile.

Scalare non significa semplicemente aggiungere tecnologia.

Significa rendere un processo:

- ripetibile;
- osservabile;
- verificabile;
- comprensibile;
- governabile;
- modificabile senza rompere tutto;
- utilizzabile da persone diverse da chi lo ha costruito.

Il problema quindi non è solo:

> “Come automatizziamo questa analisi?”

È:

> **“Quale parte di questa analisi merita di diventare infrastruttura decisionale?”**

## Dal progetto al prodotto analitico

Immaginiamo un'azienda SaaS che ogni lunedì misura:

- pipeline commerciale;
- ARR;
- churn;
- NRR;
- activation;
- support backlog;
- forecast trimestrale.

All'inizio un analyst scarica tre file, esegue una query, aggiorna un workbook e prepara una slide.

Funziona.

Poi l'azienda cresce.

Il CFO vuole il dato alle 8:00.

Il VP Sales vuole drill-down per regione.

Customer Success usa una definizione diversa di churn.

Il team Product vuole distinguere logo retention e revenue retention.

Una modifica CRM rompe la logica del forecast.

L'analista che costruiva il report va in ferie.

Quello che sembrava un report diventa improvvisamente un sistema critico.

La domanda cambia.

Non basta più chiedere se il calcolo è corretto oggi.

Dobbiamo chiedere:

- chi possiede la metrica?
- chi possiede la pipeline?
- quali dati sono fonte autorevole?
- quali test devono passare?
- quanto può essere vecchio il dato?
- come scopriamo che qualcosa si è rotto?
- chi viene avvisato?
- come gestiamo una modifica semantica?
- come ricostruiamo il passato?
- cosa succede se una sorgente non arriva?

Queste non sono domande accessorie.

Sono parte della qualità analitica.

## Il sistema operativo dell'analytics

Un sistema analitico maturo può essere pensato come una catena:

**Sorgenti → Contratti → Trasformazioni → Test → Metriche → Prodotti analitici → Decisioni → Feedback**

con una seconda catena trasversale:

**Ownership → Osservabilità → Governance → Versionamento → Incident management**

Se manca la seconda catena, la prima può funzionare per mesi e fallire proprio quando diventa importante.

## Scalare non significa automatizzare tutto

Un errore frequente è trasformare ogni analisi in pipeline.

Non tutto lo merita.

Un'analisi una tantum su un'acquisizione, una nuova categoria o una crisi operativa può restare esplorativa.

Un processo invece tende a meritare industrializzazione quando è:

- ricorrente;
- business-critical;
- utilizzato da più team;
- soggetto a errori manuali;
- abbastanza stabile semanticamente;
- abbastanza costoso da ricostruire ogni volta.

Una buona domanda è:

> **“Se questa analisi smettesse di funzionare domani, chi se ne accorgerebbe e quale decisione verrebbe compromessa?”**

Più seria è la risposta, più serve pensare in termini di sistema.

## Caso realistico: il weekly report che diventa infrastruttura

Una società B2B da 180 milioni di euro di ARR produce ogni lunedì un executive revenue report.

Per due anni il processo è manuale.

Un senior analyst:

1. esporta opportunità dal CRM;
2. legge dati di billing;
3. ricostruisce ARR e pipeline;
4. applica correzioni note;
5. aggiorna il file del CFO.

Tempo medio: quattro ore.

Errori significativi: rari.

Sembra efficiente.

Poi il senior analyst lascia l'azienda.

Il nuovo team scopre che:

- la definizione di expansion ARR non è documentata;
- alcune eccezioni enterprise sono codificate in formule Excel;
- una tabella di mapping territori vive su un drive personale;
- il report non ha test automatici;
- nessuno sa quale timestamp determina il cut-off settimanale;
- Sales e Finance usano versioni diverse dello stesso numero.

Il problema non era la competenza del vecchio analyst.

Era che il sistema dipendeva dalla sua memoria.

La soluzione non è semplicemente “rifare tutto in SQL”.

Il redesign richiede:

- definizione condivisa delle metriche;
- ownership business;
- trasformazioni versionate;
- controlli di riconciliazione;
- freshness target;
- alerting;
- documentazione delle eccezioni;
- semantic layer comune;
- runbook per incidenti.

Il report smette di essere un file.

Diventa un prodotto analitico.

## Una definizione operativa

In questo capitolo chiameremo **sistema analitico** un insieme di dati, trasformazioni, metriche, controlli, ownership e interfacce progettato per supportare decisioni ricorrenti con un livello di affidabilità esplicito.

La tecnologia può cambiare.

Il principio no.

> **Una singola analisi crea conoscenza. Un sistema analitico rende quella conoscenza riutilizzabile senza perdere controllo sul significato.**
