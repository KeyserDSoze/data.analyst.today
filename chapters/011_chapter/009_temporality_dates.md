## 11.8 Date e temporalità: il tempo non è una colonna qualsiasi

Una delle fonti più comuni di errore analitico è usare una data corretta per rispondere alla domanda sbagliata. Un ordine può avere `created_at`, `paid_at`, `shipped_at`, `delivered_at`, `returned_at` e `recognized_revenue_date`: tutte date valide, ma ognuna racconta un evento diverso.

Per questo la time semantics dell’Analytical Data Contract deve separare almeno **event time**, quando il fatto accade; **system time**, quando il sistema lo registra; **warehouse availability time**, quando diventa interrogabile; **reporting/competence time**, a quale periodo viene attribuito; **validity time**, quando un attributo è considerato valido. Late-arriving data, backfill e analisi point-in-time diventano gestibili soltanto quando questi tempi non vengono compressi in una singola colonna “date”.

### ForgeMarket: tre crescite corrette con tre significati diversi

ForgeMarket presenta tre numeri di crescita Q4. Commerciale raggruppa per `created_at` e ottiene **+14% bookings**; Finance usa la data di fatturazione e ottiene **+6% billed revenue**; Operations usa `delivered_at` e ottiene **+2% delivered value**.

Nessun numero è necessariamente sbagliato. Diventano incompatibili quando vengono chiamati tutti `revenue_growth`. La responsabilità del modello semantico è associare nome e definizione all’evento temporale che rappresentano.

Anche la timezone appartiene alla domanda. Se una campagna italiana parte alle 00:00 locali ma gli eventi sono in UTC, `DATE(event_timestamp_utc)` può spostare le prime ore nel giorno precedente. La giornata business può essere definita dalla timezone del mercato, del merchant, dell’utente, da UTC per processi infrastrutturali o da una timezone contabile centrale. Non esiste un default universale: esiste una policy.

I confini temporali devono essere altrettanto espliciti. Per periodi consecutivi una convenzione semiaperta riduce ambiguità:

```sql
WHERE event_at >= TIMESTAMP '2026-08-01 00:00:00'
  AND event_at <  TIMESTAMP '2026-09-01 00:00:00'
```

È più robusta di un `<= 23:59:59` che dipende dalla precisione del timestamp.

### Late data: il passato può restare aperto

Una vendita può avvenire il 31 agosto alle 23:50 e arrivare nel warehouse il 1° settembre alle 02:15. Per “quanto abbiamo venduto ad agosto?” useremo event/competence time; per “quanti record ha processato la pipeline il 1° settembre?” ingestion time. Se il modello conserva soltanto una delle due date, alcune domande diventano impossibili o vengono ricostruite per approssimazione.

Un KPI pubblicato oggi può inoltre cambiare domani quando arrivano eventi tardivi. Il contract dovrebbe quindi dichiarare lateness attesa, finestra di backfill, momento di stabilizzazione e policy di restatement. Un service level come:

```text
freshness SLA: 95% degli eventi entro 30 minuti
stabilizzazione D+1: 99,8%
backfill consentito: 7 giorni
```

racconta molto più di “dashboard aggiornata ogni giorno”.

### Point-in-time correctness: quale attributo conoscevamo allora?

Un cliente era `SMB` nel 2024 e diventa `Enterprise` nel 2026. Collegare le vendite 2024 alla dimensione corrente significa riscrivere il passato. Possiamo volerlo fare intenzionalmente, ma dobbiamo distinguere la **current-state view** dalla **historical as-of view**.

Questo è lo stesso confine informativo del Capitolo 10. Se produciamo uno score il 1° agosto alle 08:00, una feature è valida soltanto se possiamo ricostruirla usando informazioni conoscibili entro quel momento. Per questo, quando serve, il modello analitico dovrebbe distinguere:

```text
event_at
recorded_at
available_at
```

Un warehouse che conserva soltanto lo stato finale può rendere impossibile una vera validazione `as-of`.

### Temporal contract

| Campo | Domanda |
|---|---|
| business event | quale evento stiamo datando? |
| event timestamp | quando è accaduto? |
| reporting date | a quale periodo appartiene? |
| timezone | quale giorno/orario usa il business? |
| availability | quando il dato era conoscibile? |
| history mode | current-state o as-of? |
| lateness policy | quanto ritardo accettiamo? |
| restatement | il passato può cambiare? |

> **La data corretta non è la colonna più comoda. È quella che rappresenta il tempo della domanda e il livello di conoscenza disponibile in quel momento.**
