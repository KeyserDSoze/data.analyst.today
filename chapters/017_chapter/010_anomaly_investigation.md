## 17.9 Atlas Streaming — “L'alert è rosso: cosa è cambiato davvero?”

> **Caso simulato/composito.** Organizzazione, numeri e sequenza sono costruiti per la didattica.

Alle **09:12** Atlas Streaming riceve un alert high severity: **trial-to-paid conversion -17%** rispetto al baseline atteso. La metrica è collegata a ricavi futuri, quindi la reazione naturale è cercare subito un bug e valutare rollback.

Un anomaly detector, però, ha dimostrato soltanto che la serie si comporta diversamente dall'attesa. Non ha identificato se il cambiamento sia nei dati, nella definizione, nel mix, nel comportamento, nel sistema o nel contesto esterno.

Il failure cost è doppio: ignorare un outage reale oppure rollbackare una feature sana. Per questo la stop rule operativa è: **nessuna azione irreversibile finché il segnale non viene riconciliato con una fonte indipendente e la popolazione resta comparabile**.

### Il primo gate dice che il fenomeno non è solo telemetry

Il team controlla freshness, completeness, duplicate, pipeline error, schema change e volume eventi. `subscription_started` è effettivamente diminuito; anche il sistema di billing mostra un calo coerente. Il segnale non è quindi un semplice event-loss.

Questa evidenza non ci autorizza ancora a parlare di checkout failure. Ci autorizza soltanto a spostare il caso da **data anomaly** a un insieme più ristretto di ipotesi business/system/semantic.

Payment authorization, provider error, latency e decline code sono normali. L'ipotesi payment perde priorità. Non esiste inoltre un breakpoint coerente con una release e il calo compare anche su client non esposti. L'ipotesi release non è matematicamente impossibile, ma l'Evidence Ledger accumula **evidence against** sufficiente per non partire dal rollback.

### La scoperta decisiva non è un bug: è una popolazione non matura

Il calo è concentrato in tre paesi interessati da una nuova partnership. Quegli utenti ricevono un trial di **30 giorni**, mentre il prodotto standard usa un trial di 7 giorni. La metrica aziendale continua però a essere:

> `trial-to-paid entro 14 giorni`

Gli utenti della partnership vengono quindi classificati come “non convertiti” quando, per design, non hanno ancora raggiunto il momento in cui ci aspettiamo che convertano.

La query è invariata. La formula è invariata. È cambiato il processo business. Questo è **semantic drift**: il KPI conserva la sintassi e perde la comparabilità decisionale.

L'anomaly detector ha fatto correttamente il proprio lavoro dicendo “questa serie non si comporta più come prima”. Sarebbe invece scorretto trasformare il -17% in “la capacità del prodotto di convertire trial in clienti è peggiorata del 17%”.

### La decisione si chiude qui — e il business outcome deve aspettare

In un incidente non serve un audit di tre settimane. Una Data Readiness Review compatta ha già risposto alle domande che potevano cambiare l'azione immediata: il dato è fresco; billing conferma che la tempistica delle conversioni osservate è diversa; payment e release non mostrano failure coerenti; la popolazione e il timing di eligibility sono cambiati.

Le alternative diventano quindi semplici. **Rollback prodotto** non è supportato. **Bloccare la partnership** sarebbe prematuro, perché sappiamo che la metrica è immatura ma non se la nuova offerta ha economics peggiori. La scelta corretta è **correggere il KPI e aprire un monitor separato**: cohort per trial type, conversione dopo eligibility, expected revenue per trial cohort e alert distinti per trial standard e 30-day.

Lo stato decisionale è:

```text
INCIDENT: metric semantics
PRODUCT ROLLBACK: NO
PARTNERSHIP ECONOMICS: WAIT FOR COHORT MATURITY
```

Il caso finisce volutamente prima di sapere se la partnership è buona o cattiva. Quella conclusione richiede che le coorti maturino per **30–45 giorni** e che possiamo osservare conversione dopo eligibility, revenue per trial cohort, churn iniziale e CAC/payback.

Questa è una stop rule matura: **non ancora**, con oggetto, orizzonte e next evidence definiti.

### Evidence Ledger

| Observed | Inferred | Still unknown |
|---|---|---|
| trial-to-paid alert -17% | KPI non è più comparabile tra trial type | economics della partnership |
| billing conferma timing diverso, non solo telemetry | non c'è evidenza per rollback prodotto | conversion after eligibility delle coorti nuove |
| payment normale, nessun release breakpoint | semantic drift spiega il falso severity signal | CAC/payback, early churn, long-run value |
| partnership usa trial 30d vs standard 7d | | |

La severity dell'incidente passa quindi da `high-severity product incident` a **metric semantics incident con monitor economico aperto**. Non significa che non sia successo niente: il sistema di osservabilità era diventato non allineato al processo commerciale, e proprio per questo avrebbe potuto innescare un rollback sbagliato.

La headline operativa può dire:

> **L'alert non indica al momento un deterioramento del checkout: il nuovo trial da 30 giorni rende non comparabile la metrica `paid entro 14 giorni`. Correggiamo il KPI e aspettiamo la maturazione delle coorti partnership prima di giudicarne il valore economico.**

**Percorso effettivo:** alert → Data Readiness Review compatta → EDA Evidence Map → Decision Record operativo → Decision Communication Pack → **WAIT FOR COHORT MATURITY** → outcome review.

Non addestriamo un nuovo anomaly model e non facciamo causal inference. Nessuno dei due metodi chiude il rischio decisionale ancora aperto meglio della semplice correzione semantica e dell'attesa necessaria.

> **Anomaly detection riduce il tempo per accorgerci che qualcosa è cambiato. La maturità analitica include riconoscere quando il prossimo passo corretto è cambiare la metrica e aspettare che il fenomeno diventi osservabile.**
