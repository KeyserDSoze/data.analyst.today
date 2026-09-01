## 16.10 Dashboard anti-pattern: quando l'interfaccia nasconde la decisione

Una dashboard può essere tecnicamente completa, aggiornata e perfino molto usata, ma restare un cattivo prodotto decisionale.

Gli anti-pattern più pericolosi non sono quelli “brutti”. Sono quelli che rendono difficile capire **che cosa conta, che cosa significa e che cosa fare**.

## Anti-pattern 1 — KPI wall

Ventiquattro card sulla home page non producono automaticamente una vista completa del business.

Producono spesso ventiquattro richieste concorrenti di attenzione.

Correzione:

- pochi KPI legati alle decisioni della pagina;
- baseline/target;
- exception materialmente rilevanti;
- drill-down separato.

## Anti-pattern 2 — Slicer cemetery

Dodici filtri visibili sembrano offrire libertà.

Possono invece obbligare l'utente a ricostruire ogni volta il contesto corretto.

Domande utili:

- quali filtri servono davvero alla decisione?
- quali dovrebbero essere fissati dalla definizione del prodotto?
- una combinazione di filtri può produrre un KPI semanticamente privo di senso?

L'interattività non deve trasformare il semantic contract in una scelta casuale dell'utente.

## Anti-pattern 3 — Metriche uguali con semantica diversa

Una pagina filtra `revenue` per `order_date`, un'altra per `invoice_date`, una terza per `payment_date`.

Le tre card portano lo stesso nome.

Questo è più pericoloso di un grafico sbagliato perché costruisce una falsa sensazione di coerenza.

La governance del Capitolo 11 viene prima della visualizzazione.

## Anti-pattern 4 — Traffic-light theater

Rosso, giallo e verde possono essere utili se le soglie derivano da una regola operativa.

Diventano teatro quando:

- la soglia è arbitraria;
- tutti i KPI devono per forza avere un colore;
- il rosso non ha owner né runbook;
- il verde nasconde un trend in deterioramento;
- il significato dipende solo dal colore.

Un semaforo senza conseguenza operativa è decorazione normativa.

## Anti-pattern 5 — Interactivity as design

> “L'informazione c'è, basta fare drill-down.”

Non è una giustificazione sufficiente.

La prima vista dovrebbe già rendere evidente se esiste un problema e perché merita attenzione. L'interattività serve ad approfondire, non a scoprire casualmente quale domanda la dashboard avrebbe dovuto rispondere.

## Anti-pattern 6 — Dashboard-as-database

Una tabella con 60 colonne, export illimitato e ogni metrica disponibile può essere utile come **data access surface**.

Non è necessariamente una dashboard.

Se tutti esportano in Excel prima di poter rispondere alla domanda, il prodotto sta probabilmente servendo un bisogno diverso da quello dichiarato.

La soluzione può essere mantenere entrambe le cose:

- decision dashboard;
- detail/export view.

Non obbligarle a essere lo stesso oggetto.

## Anti-pattern 7 — Mappe senza domanda geografica

Una mappa è appropriata quando posizione, distanza, contiguità o territorio fanno parte del problema.

Se dobbiamo solo confrontare revenue di 12 regioni, barre ordinate possono essere molto più precise.

La geografia non deve entrare perché “abbiamo un campo regione”.

## Anti-pattern 8 — Nessuna freshness o ownership

Un KPI rosso può produrre una decisione urgente.

Se il lettore non sa:

- quando il dato è aggiornato;
- se è finalizzato;
- chi possiede l'anomalia;
- quando arriverà il prossimo refresh;

la dashboard manca di informazioni operative fondamentali.

## Anti-pattern 9 — Hover-only truth

Se definizione, valore esatto, caveat o denominatore compaiono soltanto in un tooltip:

- possono sparire in screenshot e PDF;
- possono essere difficili con touch o assistive technology;
- non vengono percepiti da chi non sa che deve cercarli.

L'informazione decision-critical deve esistere anche senza hover.

## Anti-pattern 10 — Nessuna exit condition

Una dashboard nata per una decisione del 2024 può restare online nel 2027 anche se:

- il processo è cambiato;
- la metrica non è più ufficiale;
- nessuno la possiede;
- esiste una nuova fonte certificata.

Il risultato è una foresta di “fonti quasi autorevoli”.

Ogni dashboard dovrebbe avere:

- owner;
- audience;
- decisioni supportate;
- data di review;
- criterio di retirement o redesign.

## Caso simulato/composito — La dashboard che tutti volevano e nessuno usava

Una società industriale costruisce una home operations con 62 visualizzazioni distribuite in più tab.

Gli stakeholder avevano chiesto “tutti i dati”.

Dopo il rilascio, nei weekly review i manager continuano però a chiedere screenshot manuali agli analyst.

L'osservazione dell'uso mostra che le domande ricorrenti sono soltanto cinque:

1. backlog fuori soglia?
2. throughput sotto piano?
3. on-time delivery in deterioramento?
4. defect rate concentrato su quale linea?
5. chi deve intervenire questa settimana?

Il redesign parte da queste domande.

La home diventa una superficie di exception e decisione; il dettaglio resta disponibile altrove.

## Dashboard stress test

Prima della pubblicazione chiediamo a un utente reale, senza istruzioni del designer, di:

1. trovare il problema principale;
2. identificare baseline/target;
3. spiegare se il dato è aggiornato;
4. trovare il segmento che guida il delta;
5. dire quale azione sembra richiesta;
6. trovare definizione e fonte;
7. completare il compito senza usare il mouse, quando pertinente.

Se il dato esiste ma il task fallisce, **la dashboard non ha comunicato**.

> **Una dashboard non è un archivio di informazione. È un'interfaccia che deve trasformare segnali affidabili in attenzione, diagnosi e azione con il minimo attrito possibile.**

### Fonte

- Government Analysis Function, *Data visualisation: testing dashboards for design and accessibility*: https://analysisfunction.civilservice.gov.uk/policy-store/data-visualisation-testing-dashboards-for-design-and-accessibility/
