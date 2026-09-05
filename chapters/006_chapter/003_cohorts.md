## 6.2 Coorti: confrontare clienti allo stesso punto del lifecycle

La segmentazione risponde soprattutto a **chi** si comporta in modo diverso. La coorte aggiunge il tempo: **quando è entrato quel cliente e da quanto tempo ha avuto la possibilità di vivere il prodotto?**

È una distinzione essenziale perché un portafoglio aggregato mescola continuamente clienti giovani e maturi. Se non allineiamo l'età del lifecycle, possiamo scambiare una diversa esposizione al tempo per una diversa qualità della relazione.

Microsoft Learn descrive le cohort chart proprio come viste che raggruppano utenti secondo una caratteristica condivisa, per esempio la data di iscrizione, e ne seguono retention e comportamento nei periodi successivi.[^ms-cohort] Il valore analitico non è la heatmap in sé. È la possibilità di confrontare gruppi **alla stessa maturità**.

### FlowDesk: una piccola variazione aggregata nasconde coorti sempre peggiori

**FlowDesk**, SaaS B2B per processi operativi, vede la retention a sei mesi scendere dall'82% al 79% nell'ultimo anno. Tre punti percentuali sembrano un deterioramento moderato. Quando l'analista ricostruisce le coorti mensili di acquisizione, il quadro cambia:

| Coorte | M1 | M3 | M6 |
| --- | ---: | ---: | ---: |
| Gennaio | 94% | 88% | 84% |
| Febbraio | 93% | 87% | 83% |
| Marzo | 92% | 86% | 82% |
| Aprile | 91% | 84% | 79% |
| Maggio | 89% | 81% | 75% |
| Giugno | 88% | 79% | 72% |

La base storica, più fedele, tiene ancora alto il KPI complessivo mentre le nuove generazioni di clienti stanno peggiorando progressivamente. La domanda non è più “perché la retention totale è scesa di tre punti?”, ma **“che cosa è cambiato per i clienti entrati da aprile in poi?”**.

Questa domanda è più utile perché collega il comportamento alla timeline del business. Ma prima ancora di cercare una spiegazione dobbiamo scegliere bene il momento zero.

Per FlowDesk il contratto firmato non coincide necessariamente con l'inizio dell'esperienza reale. Il team confronta tre possibili `t0`: firma del contratto, completamento del setup e prima automazione realmente eseguita. Per studiare l'adozione, la terza definizione rende le coorti più confrontabili, perché allinea i clienti al momento in cui il prodotto entra davvero nel processo operativo.

La scelta del `t0` dipende quindi dalla domanda. In un prodotto self-service il signup può essere sufficiente; in un SaaS enterprise il go-live può arrivare settimane dopo la firma; in un marketplace la registrazione può precedere di mesi il primo acquisto. La coorte deve iniziare nel punto che rende confrontabile **l'esposizione al fenomeno che vogliamo studiare**.

### Una coorte comportamentale genera ipotesi, non automaticamente cause

Le coorti possono essere definite anche da un comportamento: completare l'onboarding entro tre giorni, invitare un collega nella prima settimana, attivare un'integrazione o effettuare un secondo ordine entro trenta giorni. Queste viste possono essere molto informative, ma richiedono lo stesso linguaggio calibrato usato nella segmentazione.

FlowDesk osserva, per esempio, che gli account che creano almeno tre workflow nella prima settimana hanno retention M6 dell'**88%**, contro il **63%** di quelli che ne creano uno solo. È un'associazione forte e un ottimo candidato per ragionare sull'activation. Non dimostra però che obbligare ogni cliente a creare tre workflow porterebbe automaticamente la retention all'88%: clienti più motivati, meglio supportati o più maturi possono sia creare più workflow sia restare più a lungo.

La coorte ci dice **dove esiste una differenza che merita spiegazione**. Non identifica da sola l'intervento che la produrrebbe.

### Maturità e timeline: il tempo deve essere trattato correttamente due volte

Una coorte acquisita due mesi fa non può ancora avere una retention M6 osservata. Le celle vuote o parzialmente mature non sono zero e non sono risultati confrontabili con coorti che hanno già attraversato sei mesi. Ogni vista dovrebbe quindi conservare almeno il momento zero, la numerosità iniziale, l'età raggiunta dalla coorte, l'evento che definisce l'attività e gli eventuali cambi di tracking o prodotto avvenuti nel periodo.

Una volta costruita correttamente la vista, la coorte diventa una timeline del business. In FlowDesk il deterioramento comincia ad aprile. Nella stessa finestra cambiano tre cose: onboarding self-service, crescita di un nuovo canale partner e mix più orientato verso aziende piccole. La cohort analysis non decide quale dei tre eventi abbia causato la perdita di retention. Fa qualcosa di precedente e fondamentale: **localizza nel tempo la rottura e restringe lo spazio delle ipotesi**.

Questo è il ponte verso il funnel. Ora sappiamo *chi* sta peggiorando e *da quando*. Il passo successivo è capire **dove**, dentro il percorso verso il valore, le nuove coorti iniziano a divergere.

[^ms-cohort]: Microsoft Learn, *AI/BI dashboard visualization types — Cohort chart*: https://learn.microsoft.com/en-us/azure/databricks/dashboards/manage/visualizations/types
