## 12.11 SLA e SLO del dato: quando "aggiornato" deve diventare una garanzia

Dire che un dataset è "aggiornato ogni mattina" è troppo vago per un sistema critico.

Un'organizzazione matura trasforma aspettative implicite in **obiettivi misurabili**.

In ambito dati, uno SLO può definire per esempio:

- freshness;
- completeness;
- availability;
- accuratezza rispetto a controlli noti;
- tempo massimo di recovery.

### Caso realistico: Solaria Energy

Solaria gestisce 2,6 milioni di contatori intelligenti.

Il management riceve ogni mattina un report sui consumi del giorno precedente.

Per mesi il requisito informale è:

> il report deve essere pronto entro le 08:00.

Ma cosa significa esattamente?

Alle 07:55 il dashboard è disponibile, ma il 7% dei contatori non ha ancora inviato i dati.

Il sistema è "disponibile", ma non è completo.

Il team definisce allora tre SLO distinti:

```text
freshness:    dati fino alle 23:59 del giorno precedente entro le 07:30
completeness: almeno 99,2% dei meter attesi entro le 08:00
availability: semantic model interrogabile nel 99,9% delle finestre previste
```

Ora la qualità operativa è osservabile.

### Freshness non è completeness

Un dataset può essere recente ma incompleto.

Può anche essere completo ma vecchio.

Esempio:

```text
Dataset A
ultimo timestamp: 07:58
completezza: 83%

Dataset B
ultimo timestamp: 06:40
completezza: 99,9%
```

Quale è migliore?

Dipende dalla decisione.

Per un alert operativo potrebbe essere preferibile A. Per un report finanziario potrebbe essere preferibile B.

### SLA, SLO e aspettative

In modo pratico:

- **SLO**: obiettivo interno misurabile;
- **SLA**: impegno formale verso un consumer, spesso con conseguenze organizzative o contrattuali.

Non serve trasformare ogni tabella in un contratto legale. Serve però rendere esplicite le aspettative sui dataset critici.

### Caso: dashboard executive "verde"

Un dashboard mostra un indicatore verde perché il refresh BI è terminato alle 06:30.

Ma la tabella ordini upstream ha ricevuto solo l'82% dei file giornalieri.

Il refresh tecnico è riuscito.

Il prodotto dati, invece, non ha rispettato la garanzia di completezza.

Questo è uno degli errori più comuni nelle organizzazioni immature:

**monitorare il job invece del significato del dato.**

### Metriche utili

Per un dataset importante si possono misurare:

| Dimensione | Esempio |
|---|---|
| Freshness | `now - max(event_timestamp)` |
| Completeness | righe ricevute / righe attese |
| Validity | % record che rispettano regole di dominio |
| Uniqueness | duplicati su chiavi critiche |
| Availability | % finestre in cui il dataset è interrogabile |
| Recovery | tempo medio per tornare a uno stato affidabile |

### Error budget

Il concetto di error budget può essere utile anche nei sistemi dati.

Se l'obiettivo è 99,9% di disponibilita', una certa quota di failure è implicitamente tollerata.

Questo aiuta a evitare due estremi:

- pretendere affidabilita' infinita a costo infinito;
- accettare incidenti continui senza una soglia esplicita.

### Cosa deve fare il Data Analyst

Quando usa un dataset critico dovrebbe sapere almeno:

1. quando dovrebbe essere pronto;
2. quanto può essere incompleto;
3. quale ritardo è accettabile;
4. chi possiede il problema se lo SLO fallisce;
5. se il dashboard segnala davvero la qualità del dato o solo il completamento del refresh.

### Metodo operativo

Per ogni prodotto dati importante definire:

```text
owner
consumer principali
freshness target
completeness target
availability target
quality checks
alerting
recovery procedure
```

**Un dataset affidabile non è quello che di solito funziona. È quello per cui sappiamo cosa significa funzionare.**
