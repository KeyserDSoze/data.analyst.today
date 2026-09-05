## 12.5 Batch, micro-batch e streaming: progettare per time-to-decision

Dopo aver deciso dove il dato viene catturato, preservato e curato, resta una domanda che spesso viene trasformata troppo presto in una scelta tecnologica:

> **Quanto ritardo possiamo tollerare prima che una decisione perda valore?**

“Real time” non è un obiettivo in sé. È una risposta possibile a un requisito di time-to-decision. Tra un report mensile e uno stream sub-second esiste un continuum di frequenze, e ogni riduzione di latenza può aumentare costo, stato da gestire, observability e complessità di recovery.

### Caso simulato/composito — CasaNova e il real time senza un utente real time

CasaNova chiede una dashboard vendite “real time”. Il discovery mostra però che i regional manager intervengono sullo staffing una volta al giorno, il pricing cambia settimanalmente, il replenishment gira alle 22:00 e il board guarda i dati ogni settimana.

Un refresh ogni 15 minuti è già più fresco di qualsiasi processo decisionale downstream. Portarlo a due secondi non cambia alcuna azione: compra soltanto complessità.

In fraud detection può valere il contrario. Se una carta compromessa continua a effettuare transazioni, trenta minuti di latenza possono generare altre perdite. In quel caso il percorso:

```text
evento
→ scoring
→ decisione
→ blocco/review
```

può dover chiudersi in pochi secondi.

### Event time, processing time e late data

La bassa latenza introduce una difficoltà ulteriore: l'ordine in cui gli eventi arrivano non coincide necessariamente con l'ordine in cui sono accaduti. Dobbiamo distinguere **event time**, quando il fenomeno è avvenuto, da **processing time**, quando la pipeline lo elabora.

Google Dataflow usa il watermark per rappresentare una soglia oltre la quale il sistema si aspetta che i dati di una finestra siano arrivati; un evento che arriva dopo che il watermark ha superato la finestra è late data. La documentazione corrente ricorda anche che gli eventi non sono garantiti in ordine e che trigger e watermark determinano quando emettere risultati.

Fonti:
- https://docs.cloud.google.com/dataflow/docs/concepts/streaming-pipelines
- https://docs.cloud.google.com/dataflow/docs/guides/develop-and-test-pipelines

Questo trasforma “quando pubblichiamo?” in un trade-off esplicito. Aspettare di più può aumentare completezza ma ritarda l'azione; pubblicare prima può richiedere correzioni successive.

Per questo un sistema può servire più stati della stessa evidenza:

```text
10:05 → risultato provisional
10:20 → aggiornamento con late events
T+1   → risultato finale riconciliato
```

Streaming e batch possono quindi convivere senza essere ridondanti: uno può alimentare alert operativi, l'altro la riconciliazione certificata. Il rischio nasce quando due percorsi producono due “verità” senza una regola su quale stato sia preliminare e quale definitivo.

Nella Data Flow Architecture Map annotiamo:

```text
decision deadline:
processing mode:
event-time field:
processing/ingestion time:
expected lateness:
watermark/window policy:
late-data behavior:
provisional or final output:
reconciliation path:
```

> **Una buona architettura non minimizza la latenza in assoluto. Minimizza il tempo tra un cambiamento rilevante e una decisione affidabile che può ancora fare la differenza.**
