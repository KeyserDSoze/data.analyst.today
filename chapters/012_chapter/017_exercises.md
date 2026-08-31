## 12.16 Esercizi: progettare e diagnosticare sistemi dati

Gli esercizi di questo capitolo non chiedono di memorizzare definizioni. Chiedono di ragionare come un analista che deve lavorare dentro un sistema reale.

### Esercizio 1 — Full reload o CDC?

Un e-commerce ha una tabella ordini da 600 milioni di righe. Ogni giorno vengono create o modificate circa 4 milioni di righe.

Il full reload notturno dura 5 ore e spesso termina dopo l'orario previsto per il dashboard executive.

Domande:

1. quali vantaggi potrebbe offrire il CDC?
2. quali nuovi rischi introduce?
3. come gestiresti update multipli dello stesso ordine?
4. come verificheresti che una ripartenza non abbia duplicato dati?

### Esercizio 2 — Pipeline verde, dato sbagliato

Un dashboard mostra vendite giornaliere inferiori del 14% rispetto alla settimana precedente.

Tutti i job risultano `SUCCESS`.

Scopri che 3 dei 28 file regionali non sono mai arrivati.

Domande:

- quale controllo mancava?
- quale SLO proporresti?
- il dashboard dovrebbe essere pubblicato comunque?
- come comunicheresti l'incidente agli stakeholder?

### Esercizio 3 — Breaking change silenzioso

Un campo `delivery_time` mantiene lo stesso nome ma cambia unità da minuti a secondi.

Le pipeline non falliscono.

Il P95 dei tempi di consegna cresce di circa 60 volte.

Domande:

1. perché uno schema test non basta?
2. quale data contract avrebbe potuto prevenire il problema?
3. quale controllo di plausibilita' aggiungeresti?

### Esercizio 4 — Real time o no?

Una società B2B produce circa 25.000 eventi al giorno.

Il CFO legge il report una volta al giorno alle 09:00.

Il team propone una piattaforma streaming con latenza inferiore al secondo.

Valuta:

- valore reale della latenza;
- costi operativi;
- soluzione alternativa;
- casi in cui invece lo streaming sarebbe giustificato.

### Esercizio 5 — Orchestrazione

Hai questi task:

```text
A: ingest orders
B: ingest refunds
C: ingest customers
D: calculate net revenue
E: calculate customer segments
F: refresh semantic model
```

Definisci un DAG ragionevole.

Poi descrivi cosa dovrebbe succedere se `B` fallisce.

### Esercizio 6 — Recovery

Una pipeline incrementale ha caricato 730.000 righe prima di fallire.

Il retry riparte dall'inizio e usa `INSERT` puro.

Qual è il rischio?

Proponi almeno due strategie per rendere il processo idempotente.

### Esercizio 7 — Data product SLO

Progetta SLO per un dataset usato dal team antifrode.

Considera almeno:

- freshness;
- completeness;
- availability;
- recovery.

Poi confrontali con gli SLO di un report finanziario mensile.

### Esercizio 8 — Caso da architecture review

Una società omnicanale ha:

- POS;
- e-commerce;
- loyalty;
- ERP;
- app mobile;
- advertising data.

Il CEO vuole sapere il Customer Lifetime Value omnicanale.

Progetta ad alto livello:

1. sorgenti;
2. ingestion;
3. raw layer;
4. curated layer;
5. identity resolution;
6. business layer;
7. semantic layer;
8. freshness appropriata;
9. quality checks;
10. ownership.

### Esercizio 9 — Cloud cost investigation

Una dashboard cloud costa circa €24.000 al mese.

La usano 32 persone.

Scopri che:

- legge 18 TB a refresh;
- si aggiorna ogni 5 minuti;
- il 70% degli utenti la apre una sola volta al giorno;
- la maggior parte delle metriche cambia lentamente.

Elenca le prime cinque azioni che valuteresti.

### Esercizio 10 — La domanda più importante

Per un dataset che usi regolarmente, prova a rispondere senza consultare documentazione:

> Da dove arriva, quali trasformazioni subisce, quando è considerato completo, chi ne è responsabile e cosa succede se il processo fallisce?

Se non sai rispondere, hai appena identificato un rischio analitico reale.

## Sintesi finale del capitolo

Un Data Analyst moderno non deve progettare ogni pipeline, ma deve saper leggere l'architettura abbastanza bene da distinguere:

- dato operativo e dato analitico;
- batch e streaming;
- raw e curated;
- lake, warehouse e lakehouse;
- trasformazione e semantica;
- refresh riuscito e dato affidabile;
- schema valido e significato valido;
- disponibilita' tecnica e utilita' decisionale.

L'architettura non è lo sfondo dell'analisi.

**È la catena di assunzioni attraverso cui la realtà diventa un numero.**
