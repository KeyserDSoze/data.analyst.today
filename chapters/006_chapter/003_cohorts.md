## 6.2 Coorti: confrontare clienti allo stesso punto del lifecycle

Segmentare risponde soprattutto a **chi** si comporta in modo diverso. Una coorte aggiunge un'altra dimensione: **quando è entrato nel processo e da quanto tempo ha avuto la possibilità di vivere il prodotto**.

Una coorte è un gruppo di utenti, account o clienti che condivide un'origine analiticamente rilevante. Può essere il mese del primo acquisto, la settimana di registrazione, l'inizio dell'abbonamento, la prima attivazione oppure l'ingresso attraverso una determinata campagna.

Il punto non è costruire una heatmap elegante. È evitare confronti ingiusti tra popolazioni con età diversa.

Microsoft Learn descrive i cohort chart proprio come uno strumento per raggruppare utenti in base a una caratteristica condivisa, per esempio la data di iscrizione, e seguirne retention e comportamento nei periodi successivi.[^ms-cohort]

### Caso simulato/composito: FlowDesk e la retention che sembrava peggiorare lentamente

**FlowDesk** è un SaaS B2B per la gestione dei processi operativi. La retention a sei mesi, osservata a livello aggregato, è scesa dall'82% al 79% nell'ultimo anno.

Tre punti percentuali sembrano un deterioramento moderato.

L'analista costruisce invece le coorti mensili di acquisizione e confronta ogni gruppo alla stessa età:

| Coorte | M1 | M3 | M6 |
| --- | ---: | ---: | ---: |
| Gennaio | 94% | 88% | 84% |
| Febbraio | 93% | 87% | 83% |
| Marzo | 92% | 86% | 82% |
| Aprile | 91% | 84% | 79% |
| Maggio | 89% | 81% | 75% |
| Giugno | 88% | 79% | 72% |

L'aggregato nascondeva un deterioramento progressivo delle nuove generazioni di clienti. La base storica, più fedele, teneva ancora alto il KPI complessivo.

La domanda cambia da:

> Perché la retention totale è scesa di tre punti?

A:

> Che cosa è cambiato per i clienti entrati da aprile in poi?

Questa seconda domanda è molto più investigabile.

### La coorte deve rappresentare un vero punto di partenza

Non sempre il signup è il miglior momento zero.

In un prodotto self-service può esserlo. In un SaaS enterprise, invece, il contratto può essere firmato settimane prima del go-live. In un marketplace, la registrazione può precedere di mesi il primo acquisto. In una banca, l'apertura del conto e il primo utilizzo significativo possono essere eventi molto diversi.

La scelta del `t0` deve essere coerente con il fenomeno che vogliamo osservare.

Per FlowDesk il team prova tre definizioni:

- mese di firma del contratto;
- mese di completamento del setup;
- mese della prima automazione realmente eseguita.

La terza produce coorti più comparabili per studiare l'adozione, perché allinea i clienti al momento in cui il prodotto ha iniziato davvero a entrare nel processo operativo.

### Coorti temporali e coorti comportamentali

Una coorte può anche essere definita da un comportamento:

- utenti che completano l'onboarding entro tre giorni;
- clienti che invitano almeno un collega nella prima settimana;
- account che attivano un'integrazione;
- acquirenti che effettuano un secondo ordine entro trenta giorni.

Queste viste sono utili, ma introducono un rischio interpretativo importante.

FlowDesk osserva che gli account che creano almeno tre workflow nella prima settimana hanno retention M6 dell'88%, contro il 63% di quelli che ne creano uno solo.

È una **associazione** forte. Non dimostra che costringere ogni cliente a creare tre workflow porterebbe automaticamente la retention all'88%.

I clienti più motivati, più maturi o meglio supportati potrebbero sia creare più workflow sia rimanere più a lungo.

La coorte comportamentale genera quindi una buona ipotesi di activation. Non fornisce ancora la prova causale dell'intervento.

### Il problema della maturità

Una delle tabelle più ingannevoli è quella in cui le coorti recenti mostrano celle vuote o percentuali parziali e vengono comunque confrontate con coorti completamente mature.

Una coorte acquisita due mesi fa non può ancora avere una retention M6 osservata.

Per questo ogni vista di coorte dovrebbe rendere visibili almeno:

- definizione del momento zero;
- numerosità iniziale;
- età raggiunta dalla coorte;
- evento che definisce l'attività;
- eventuali cambi di tracking o prodotto avvenuti nel periodo.

### Dalla heatmap alla timeline del business

Il vero valore della cohort analysis emerge quando la tabella viene sovrapposta alla storia operativa.

In FlowDesk il deterioramento comincia nelle coorti entrate dopo aprile. Nella stessa finestra sono successi tre eventi:

1. è stato modificato l'onboarding self-service;
2. è cresciuto un nuovo canale partner;
3. il mix si è spostato verso aziende più piccole.

La coorte non ci dice quale dei tre abbia causato il problema. Ci dice **dove nel tempo cercare il cambiamento**.

Questa è la sua funzione nel lifecycle:

**rendere confrontabili clienti entrati in momenti diversi e collegare il loro comportamento alla timeline del prodotto e del business.**

[^ms-cohort]: Microsoft Learn, “AI/BI dashboard visualization types — Cohort chart”, https://learn.microsoft.com/en-us/azure/databricks/dashboards/manage/visualizations/types
