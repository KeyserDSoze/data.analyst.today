# 18.2 SLA, osservabilità e incident management

Un dataset può essere tecnicamente corretto e comunque inutilizzabile.

Se arriva alle 14:00 ma il pricing meeting è alle 9:00, è troppo tardi.

Se contiene il 92% delle transazioni ma nessuno sa quali mancano, può essere pericoloso.

Se aggiorna in tempo ma non segnala una rottura di schema, può generare decisioni sbagliate più velocemente.

Per questo la qualità di un sistema analitico non può essere ridotta alla correttezza della query.

## Qualità come insieme di dimensioni

Per un prodotto analitico ricorrente è utile esplicitare almeno:

- **freshness** — quanto è aggiornato il dato;
- **completeness** — quanto è completo;
- **accuracy** — quanto riflette correttamente la realtà;
- **consistency** — se resta coerente tra sistemi e periodi;
- **availability** — se è accessibile quando serve;
- **latency** — quanto tempo passa dall'evento alla disponibilità analitica.

Non tutte le dimensioni hanno la stessa importanza per ogni use case.

Un report mensile di board può tollerare ore di latency ma non errori di riconciliazione.

Un sistema antifrode può richiedere secondi di latency e accettare un livello diverso di completezza iniziale.

## SLA, SLO e aspettative

Nel mondo SRE, gli SLO sono usati per descrivere e misurare il livello desiderato di affidabilità di un servizio.

La stessa logica è molto utile per i dati.

Esempio:

> La tabella `daily_orders` deve essere completa per almeno il 99,5% degli ordini del giorno precedente entro le 07:30 CET nel 99% dei giorni lavorativi del trimestre.

Questa frase è molto più utile di:

> “La pipeline deve essere affidabile.”

Perché rende il concetto misurabile.

## Caso realistico: dashboard verde, dati rotti

Una catena retail utilizza una dashboard giornaliera per allocare stock.

Alle 8:00 tutti i KPI sono verdi.

Le vendite del giorno precedente sembrano in linea.

Alle 10:30 il team operations scopre che 63 negozi non avevano inviato i dati POS.

La pipeline non era fallita.

Aveva elaborato correttamente ciò che aveva ricevuto.

L'errore era di osservabilità.

Il sistema controllava:

- job success;
- durata;
- presenza della tabella.

Non controllava:

- numero atteso di store;
- volume transazioni per store;
- confronto con baseline storica;
- percentuale di sorgenti complete.

Questo caso mostra una distinzione fondamentale:

**pipeline health ≠ data health**.

## Le tre domande dell'osservabilità

Per ogni prodotto critico dovremmo poter rispondere rapidamente a tre domande:

1. **È arrivato?**
2. **È completo e plausibile?**
3. **Se qualcosa è sbagliato, sappiamo dove guardare?**

La terza richiede lineage, logging e ownership.

## Incident management per i dati

Quando un prodotto analitico diventa infrastruttura, serve un modo esplicito per gestire gli incidenti.

Un runbook minimo può indicare:

- sintomo;
- owner;
- sorgenti coinvolte;
- controlli da eseguire;
- workaround;
- criteri di rollback;
- consumer da avvisare;
- modalità di ricostruzione dati;
- post-mortem.

## Non tutti gli incidenti sono uguali

Una metrica cosmetica mancante su una dashboard interna non ha lo stesso impatto di una revenue metric sbagliata durante il closing.

Possiamo classificare gli incidenti in base a:

- impatto finanziario;
- numero di consumer;
- reversibilità;
- visibilità esterna;
- rischio regolatorio;
- durata.

Questo permette escalation proporzionate.

## Error budget analitico

Un concetto SRE utile anche nell'analytics è l'error budget.

Se promettiamo il 99,5% di affidabilità, stiamo implicitamente accettando una quantità limitata di fallimento.

Questo evita due estremi:

- pretendere perfezione a costi sproporzionati;
- accettare inaffidabilità senza misura.

Per una dashboard non critica, il 98% può essere sufficiente.

Per un feed che guida pagamenti o reporting regolatorio, no.

Il livello di affidabilità deve dipendere dalla decisione supportata.

## Il costo dell'affidabilità

Più affidabilità richiede:

- ridondanza;
- test;
- monitoring;
- processi di recovery;
- ownership;
- capacità operativa.

Quindi la domanda non è “possiamo arrivare al 100%?”

È:

> **“Quale livello di affidabilità è economicamente e operativamente coerente con l'impatto della decisione?”**

## Segnali utili da monitorare

Un prodotto analitico può avere monitor su:

- freshness;
- row count;
- null rate;
- cardinalità delle chiavi;
- distribuzioni;
- volumi per sorgente;
- duplicati;
- schema changes;
- riconciliazioni con sistemi finanziari;
- drift delle metriche;
- runtime e costo.

Non tutto deve generare una notifica.

Un alert utile deve indicare che qualcuno può o deve agire.

Troppi alert non aumentano il controllo.

Creano assuefazione.

## Una regola operativa

> **Un sistema è osservabile quando non dobbiamo aspettare che sia un utente a dirci che il dato è sbagliato.**

La maturità analitica include quindi una capacità apparentemente poco glamour: sapere quando il proprio numero non merita ancora di essere usato.

## Fonti

- Google Cloud, *Site Reliability Engineering*: https://cloud.google.com/sre
- Databricks, *Guiding principles*: https://docs.databricks.com/gcp/en/lakehouse-architecture/guiding-principles
