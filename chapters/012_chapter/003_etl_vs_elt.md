## 12.2 ETL vs ELT: dove trasformiamo il dato e perché

ETL significa **Extract, Transform, Load**.

ELT significa **Extract, Load, Transform**.

La differenza sembra piccola, ma cambia il modo in cui costruiamo e governiamo la pipeline.

### ETL

Nel modello ETL classico:

1. estraiamo i dati dalle sorgenti;
2. li trasformiamo prima di caricarli nella destinazione analitica;
3. carichiamo il risultato già curato.

Questo approccio è stato molto comune quando storage e capacità di calcolo erano costosi e il data warehouse doveva ricevere dati già conformati.

### ELT

Con ELT:

1. estraiamo i dati;
2. li carichiamo rapidamente in una piattaforma analitica;
3. eseguiamo le trasformazioni usando la capacità di calcolo della piattaforma stessa.

La crescita del cloud, dello storage economico e dei motori analitici scalabili ha reso ELT molto comune.

## Non è una guerra di acronimi

ETL ed ELT non sono ideologie. Sono pattern.

La scelta dipende da:

- volume;
- latenza;
- sicurezza;
- costi;
- capacità del motore di destinazione;
- necessità di conservare il raw;
- requisiti normativi;
- competenze del team.

### Caso realistico: il campo che nessuno aveva previsto

**MareaPay**, fintech europea, estrae dati da un provider di pagamenti. La prima pipeline ETL conserva soltanto i campi necessari ai report del momento:

- transaction_id;
- amount;
- currency;
- status.

Sei mesi dopo il team antifrode scopre che il provider trasmetteva anche:

- device fingerprint;
- authentication method;
- risk signals;
- timestamp intermedi.

Quei campi erano stati eliminati prima del caricamento.

Per ricostruire la storia bisogna richiedere un costoso backfill al provider, che conserva solo 90 giorni di dettaglio.

Il problema non è che ETL sia sbagliato. Il problema è che l'architettura aveva eliminato troppo presto informazione potenzialmente utile.

Una soluzione moderna potrebbe conservare una copia raw e costruire sopra versioni curate.

## Conservare raw non significa usare raw

Questo punto è cruciale.

Conservare il dato grezzo può aiutare per:

- audit;
- reprocessing;
- debugging;
- nuove esigenze;
- cambiamenti nella logica di business.

Ma il raw non dovrebbe automaticamente diventare il layer da cui ogni analista costruisce dashboard.

Se ognuno interpreta direttamente eventi grezzi, ritorniamo al problema delle definizioni locali.

### Pipeline mentale

Una pipeline robusta spesso separa:

**acquisizione → conservazione → validazione → conformazione → business logic → serving**.

Non importa se i prodotti utilizzati si chiamano ETL, ELT, dataflow, notebook, pipeline o transformation framework. Quello che conta è che ogni passaggio abbia una responsabilità chiara.

## Quando una trasformazione dovrebbe avvenire presto?

Alcune trasformazioni possono essere necessarie prima dello storage analitico:

- rimozione o tokenizzazione di dati sensibili;
- decryption controllata;
- filtri imposti da compliance;
- validazione tecnica minima;
- conversione di formati non supportati.

Altre trasformazioni possono essere più appropriate dopo il caricamento:

- join tra sorgenti;
- deduplication;
- business logic;
- metriche;
- dimensional modeling;
- aggregazioni.

### Domanda operativa per l'analista

Quando utilizzi una tabella trasformata chiediti:

> Posso risalire al dato precedente alla trasformazione, capire la logica applicata e ricostruire il risultato?

Se la risposta è no, la pipeline è più difficile da verificare.
