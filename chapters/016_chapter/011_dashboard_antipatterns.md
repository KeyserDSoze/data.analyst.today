## 16.10 Dashboard anti-pattern: quando l'interfaccia nasconde la decisione

Una dashboard può essere tecnicamente completa, aggiornata e perfino molto usata, ma restare un cattivo prodotto decisionale. Gli anti-pattern più pericolosi non sono quelli “brutti”: sono quelli che rendono difficile capire **che cosa conta, che cosa significa e che cosa fare**.

Molti failure mode diversi hanno la stessa radice: la dashboard prova a delegare all'utente il lavoro che il prodotto avrebbe dovuto fare prima.

### Quando tutto compete con tutto

Il **KPI wall** è il caso più evidente. Ventiquattro card sulla home non producono una vista completa del business; producono ventiquattro richieste concorrenti di attenzione. La correzione non è scegliere card più belle, ma ridurre la home ai KPI legati alle decisioni di quella pagina, con baseline, target ed exception materialmente rilevanti. Il dettaglio resta disponibile nel layer diagnostico.

Lo **slicer cemetery** fallisce in modo simile. Dodici filtri visibili sembrano offrire libertà ma possono obbligare l'utente a ricostruire ogni volta il contesto corretto. Alcuni filtri devono essere fissati dal semantic contract; altre combinazioni non dovrebbero nemmeno essere ammesse se producono KPI privi di significato.

### Quando la superficie sembra coerente ma la semantica non lo è

Tre pagine possono mostrare una card chiamata `revenue` e usare rispettivamente `order_date`, `invoice_date` e `payment_date`. Il design coerente costruisce allora una **falsa sensazione di comparabilità**. La governance del Capitolo 11 viene prima della visualizzazione: un'interfaccia uniforme non rende uniformi metriche diverse.

Lo stesso vale per i semafori. Rosso, giallo e verde sono utili quando la soglia ha significato operativo, esiste un owner e il cambio di stato comporta una conseguenza definita. Se la soglia è arbitraria, il rosso non ha runbook e il verde nasconde un trend in deterioramento, abbiamo **traffic-light theater**: una codifica normativa senza decision policy.

### Interattività non significa design

“L'informazione c'è, basta fare drill-down” non è sufficiente. La prima vista dovrebbe già rendere evidente se esiste un problema e perché merita attenzione. L'interattività serve ad approfondire, non a scoprire casualmente quale domanda la dashboard avrebbe dovuto rispondere.

All'estremo opposto troviamo la **dashboard-as-database**: sessanta colonne, export illimitato e ogni metrica disponibile. Può essere una buona data access surface, ma non necessariamente una dashboard. Se tutti esportano in Excel prima di poter rispondere alla domanda, il prodotto sta servendo un bisogno diverso da quello dichiarato. Decision dashboard e detail/export view possono coesistere senza essere lo stesso oggetto.

### Forme che esistono perché il dato le permette

Una mappa ha senso quando posizione, distanza, contiguità o territorio sono parte del problema. Se dobbiamo semplicemente confrontare revenue di dodici regioni, barre ordinate possono essere molto più precise. La geografia non deve entrare solo perché esiste una colonna `region`.

Lo stesso principio vale per qualsiasi visual: la disponibilità dell'encoding nel tool non è una ragione per usarlo.

### Verità nascoste in hover e stato del dato invisibile

Un KPI rosso può innescare una decisione urgente. Se il lettore non sa quando il dato è aggiornato, se è finalizzato, chi possiede l'anomalia o quando arriverà il prossimo refresh, manca una parte del significato operativo.

Non possiamo nemmeno lasciare caveat, denominatore o definizione soltanto in tooltip. L'**hover-only truth** scompare negli screenshot, nei PDF, su touch e in molti percorsi assistivi. L'informazione decision-critical deve sopravvivere senza interazione opzionale.

### Nessuna exit condition

Una dashboard nata per una decisione del 2024 può restare online nel 2027 anche se il processo è cambiato, la metrica non è più ufficiale e nessuno la possiede. Il risultato è una foresta di fonti “quasi autorevoli”. Per questo ogni dashboard ricorrente dovrebbe avere owner, audience, decisioni supportate, review date e criterio di retirement o redesign.

### Caso simulato/composito — Tutti la volevano, nessuno la usava

Una società industriale costruisce una home operations con **62 visualizzazioni** distribuite su più tab perché gli stakeholder avevano chiesto “tutti i dati”. Dopo il rilascio, nei weekly review i manager continuano però a chiedere screenshot manuali agli analyst.

Osservando il lavoro reale emergono soltanto cinque domande ricorrenti: backlog fuori soglia? throughput sotto piano? on-time delivery in deterioramento? defect rate concentrato su quale linea? chi deve intervenire questa settimana?

Il redesign parte da queste domande. La home diventa una superficie di exception e decisione; il dettaglio rimane altrove. Il prodotto contiene meno informazione immediatamente visibile e serve meglio il lavoro.

## Dashboard stress test

Prima della pubblicazione un utente reale, senza istruzioni del designer, dovrebbe riuscire a trovare il problema principale, identificare baseline/target, capire freshness e maturity, localizzare il segmento che guida il delta, dire quale azione sembra richiesta e trovare definizione e fonte. Quando pertinente, deve poter completare il task anche senza mouse.

La Government Analysis Function raccomanda proprio user testing, riduzione del clutter, alternative accessibili e verifica su diversi device.[^gaf-test]

> **Una dashboard non è un archivio di informazione. È un'interfaccia che deve trasformare segnali affidabili in attenzione, diagnosi e azione con il minimo attrito possibile.**

[^gaf-test]: Government Analysis Function, *Data visualisation: testing dashboards for design and accessibility*, https://analysisfunction.civilservice.gov.uk/policy-store/data-visualisation-testing-dashboards-for-design-and-accessibility/
