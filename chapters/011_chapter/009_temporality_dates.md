## 11.8 Date e temporalità: il tempo non è una colonna qualsiasi

Una delle fonti più comuni di errore analitico è usare una data corretta per rispondere alla domanda sbagliata.

Un ordine può avere:

- `created_at`;
- `paid_at`;
- `shipped_at`;
- `delivered_at`;
- `returned_at`;
- `recognized_revenue_date`.

Tutte possono essere valide. Ma ciascuna definisce una storia diversa.

### Time semantics nell’Analytical Data Contract

Per ogni dataset importante dovremmo distinguere almeno:

- **event time** — quando il fatto è accaduto nel mondo reale;
- **system time** — quando il sistema lo ha registrato o aggiornato;
- **warehouse availability time** — quando l’informazione è diventata interrogabile;
- **reporting/competence time** — a quale periodo il business attribuisce il fatto;
- **validity time** — da quando a quando un attributo o stato è valido.

Questa separazione diventa essenziale con late-arriving data, rettifiche, backfill e modelli point-in-time.

### Caso simulato/composito — ForgeMarket e il trimestre che cresceva del 14%, 6% o 2%

ForgeMarket, piattaforma B2B, presenta tre numeri di crescita Q4.

Commerciale usa:

```sql
DATE_TRUNC('quarter', created_at)
```

e ottiene **+14% bookings**.

Finance usa la data di fatturazione e ottiene **+6% billed revenue**.

Operations usa `delivered_at` e ottiene **+2% delivered value**.

Nessuno dei tre numeri è necessariamente sbagliato.

Il problema nasce se tutti vengono chiamati semplicemente `revenue_growth`.

La prima responsabilità del modello semantico è quindi associare il nome della metrica all’evento temporale che rappresenta.

### Timezone: il giorno del business non coincide sempre con UTC

Un marketplace globale registra gli eventi in UTC.

Una campagna italiana parte alle 00:00 ora locale. Se raggruppiamo direttamente con:

```sql
DATE(event_timestamp_utc)
```

una parte delle prime ore può finire nel giorno UTC precedente.

La domanda corretta è:

> quale timezone definisce la giornata per questa decisione?

La regola può essere:

- timezone del mercato;
- timezone del merchant;
- timezone dell’utente;
- UTC per processi infrastrutturali;
- timezone contabile centrale.

Non esiste una scelta universale. Deve essere dichiarata.

### Intervalli temporali: evitare doppi conteggi ai confini

Per periodi consecutivi è spesso robusto usare convenzioni semiaperte:

```sql
WHERE event_at >= TIMESTAMP '2026-08-01 00:00:00'
  AND event_at <  TIMESTAMP '2026-09-01 00:00:00'
```

Questo riduce ambiguità rispetto a condizioni come `<= 23:59:59`, che possono fallire quando aumenta la precisione dei timestamp.

La regola editoriale è più importante della sintassi specifica:

> **i confini temporali devono essere coerenti, non approssimati.**

### Event time vs ingestion time

Immaginiamo una vendita avvenuta il 31 agosto alle 23:50, caricata nel warehouse il 1° settembre alle 02:15.

Per la domanda “quanto abbiamo venduto ad agosto?” useremo probabilmente event/competence time.

Per la domanda “quanti record ha processato la pipeline il 1° settembre?” useremo ingestion time.

Se il dataset conserva soltanto una delle due date, alcune analisi diventano impossibili o vengono ricostruite in modo ambiguo.

### Late-arriving data e backfill

Un KPI giornaliero può cambiare dopo la pubblicazione perché arrivano eventi tardivi.

Il contratto dovrebbe quindi specificare:

- lateness attesa;
- finestra di backfill;
- quando una giornata viene considerata “stabile”;
- se i report storici vengono restated;
- come comunicare revisioni importanti.

Esempio:

```text
freshness SLA: 95% degli eventi entro 30 minuti
stabilizzazione D+1: 99,8%
backfill consentito: 7 giorni
```

Questo è molto più utile di un generico “dashboard aggiornato ogni giorno”.

### Point-in-time correctness

Un altro errore frequente è analizzare eventi storici usando attributi noti soltanto oggi.

Un cliente era `SMB` nel 2024 e diventa `Enterprise` nel 2026.

Se colleghiamo le vendite 2024 alla dimensione corrente, stiamo riscrivendo il passato.

Lo stesso problema appare con:

- pricing tier;
- territorio commerciale;
- account manager;
- rischio cliente;
- categoria prodotto;
- stato contrattuale.

La domanda da fare è:

> voglio il valore **corrente** dell’attributo oppure il valore **as-of event time**?

Le Slowly Changing Dimensions formalizzano una delle strategie per conservare questa distinzione.

### As-of time e modelli predittivi

Il Capitolo 10 ha introdotto la frontiera informativa della previsione.

Nel data modeling quella frontiera deve diventare eseguibile.

Se produciamo uno score il 1° agosto alle 08:00, ogni feature dovrebbe poter essere ricostruita usando soltanto dati disponibili entro quel momento.

Quindi il modello analitico dovrebbe distinguere, quando necessario:

```text
event_at
recorded_at
available_at
```

Un warehouse che conserva solo lo stato finale può rendere impossibile una vera validazione `as-of`.

### Temporal contract

Per ogni metrica o dataset temporale importante documentiamo:

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

> **La data corretta non è la colonna più comoda. È quella che rappresenta il tempo della domanda analitica.**
