## 8.1 Il controfattuale: la domanda che non possiamo osservare direttamente

Per misurare un effetto causale vorremmo osservare due risultati per la stessa unità:

- che cosa accade se riceve il trattamento;
- che cosa accade se non lo riceve.

Nel linguaggio dei *potential outcomes* possiamo indicare questi due risultati come:

- `Y(1)` = risultato con trattamento;
- `Y(0)` = risultato senza trattamento.

L'effetto causale individuale sarebbe:

`Y(1) - Y(0)`

Il problema fondamentale è che per la stessa unità osserviamo soltanto uno dei due risultati.

### Caso - Il coupon da 20 euro

Un retailer invia un coupon da 20 € a 50.000 clienti. Entro trenta giorni:

- il 24% dei clienti con coupon effettua un acquisto;
- tra i clienti senza coupon il tasso medio di acquisto è il 15%.

Una lettura superficiale attribuirebbe al coupon un incremento di 9 punti percentuali.

Ma il marketing team ha selezionato per la campagna i clienti che avevano visitato il sito almeno tre volte nelle ultime due settimane.

Questi clienti avevano già una propensione all'acquisto maggiore.

La domanda giusta non è:

> Quanto acquistano i clienti che ricevono il coupon rispetto agli altri?

La domanda giusta è:

> Quanto avrebbero acquistato quegli stessi clienti se non avessero ricevuto il coupon?

Quel secondo risultato è il controfattuale.

### Perché il "prima e dopo" spesso non basta

Il team prova allora un'altra analisi:

- conversion rate dei clienti target nei 30 giorni precedenti: 17%;
- conversion rate nei 30 giorni successivi al coupon: 24%.

Differenza: +7 punti.

Ancora una volta, non è sufficiente.

Nel periodo successivo è iniziata la stagione natalizia. Il traffico organico è aumentato, il catalogo promozionale è cambiato e molti clienti avrebbero acquistato comunque.

Un confronto prima/dopo attribuisce al trattamento anche tutto ciò che è cambiato nel tempo.

### Un buon controfattuale è un buon confronto

L'inferenza causale può essere vista come una disciplina per costruire gruppi o situazioni comparabili.

Un confronto è credibile quando, in assenza dell'intervento, i gruppi avrebbero avuto risultati simili o dinamiche comparabili.

La randomizzazione è potente proprio perché, in media, rende il trattamento indipendente dalle caratteristiche preesistenti. Quando non possiamo randomizzare, dobbiamo cercare altre strategie di identificazione.

### Effetto medio, non magia individuale

Spesso non possiamo sapere se il coupon ha causato l'acquisto del singolo cliente. Possiamo però stimare l'effetto medio su una popolazione:

`ATE = E[Y(1) - Y(0)]`

Oppure l'effetto medio sui trattati:

`ATT = E[Y(1) - Y(0) | trattamento = 1]`

Questa distinzione non è accademica. Un programma può funzionare bene sui clienti che oggi lo ricevono ma molto meno se esteso a tutta la base clienti.

### Caso - Incentivo alla riattivazione

Un servizio subscription offre un mese gratuito ai clienti a rischio churn. Sul gruppo trattato il churn scende dal 18% al 10%.

Il management vuole offrire il mese gratuito a tutti.

Ma i clienti trattati erano stati selezionati perché avevano ancora almeno due login nell'ultimo mese. I clienti completamente inattivi non erano inclusi.

L'effetto osservato riguarda quindi un segmento specifico. Estendere la stima a tutta la popolazione è un problema di **generalizzazione**, non soltanto di calcolo.

> **Una stima causale risponde sempre a una domanda su una popolazione, un trattamento, un outcome e un contesto specifici.**

## Riferimenti

- Stanford University, *The Potential Outcomes Model*.
- Guido Imbens, *Potential Outcome and Directed Acyclic Graph Approaches to Causality*, Journal of Economic Literature.
