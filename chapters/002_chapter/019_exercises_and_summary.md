## 2.18 Sintesi ed esercizi

Il Capitolo 1 aveva definito il lavoro analitico come una catena che collega problema, evidenza e decisione. Questo capitolo ha lavorato sul tratto che viene **prima dell'esecuzione**, quando le scelte sono ancora economiche da cambiare ma abbastanza importanti da determinare tutto ciò che verrà dopo.

L'Analytical Brief è il risultato di quel lavoro. Non è un modulo che aggiunge burocrazia alla richiesta: è il punto in cui una frase come “facci una dashboard clienti” viene costretta a dichiarare quale problema esista davvero, chi possa agire, quale outcome rappresenti il fenomeno, quali spiegazioni siano in competizione e quale evidenza abbia il diritto di cambiare la decisione.

La parte più importante del metodo è che questi elementi **non vivono separatamente**. La decisione stabilisce quanto costa sbagliare e quindi quanta evidenza serve. La definizione della metrica determina popolazione e maturazione. Le ipotesi determinano segmentazioni e requisiti dati. I gap nei dati possono ridurre la pretesa metodologica. Priorità e Value of Information decidono quanto investire; la stop rule stabilisce quando ulteriore lavoro non compra più informazione utile. Se le fonti non distinguono le alternative, “inconcludente” diventa una conclusione professionale, non uno spazio da riempire con una storia plausibile.

Il caso Velora Home ha mostrato perché questa disciplina conta. La richiesta iniziale suggeriva una dashboard e un possibile investimento in CRM. Il brief ha prima reso verificabile la Repeat Purchase Rate, poi il sanity check ha scoperto un problema di identity stitching che spiegava circa metà del deterioramento apparente. Solo dopo quella correzione il team ha analizzato il delta reale, evitando di allocare €600.000 sulla base di una metrica parzialmente rotta. Il brief non ha previsto la risposta; ha costruito le condizioni necessarie per accorgersi che la prima risposta non meritava fiducia.

Possiamo quindi leggere il percorso del capitolo come un'unica specifica che si costruisce progressivamente:

**Problema → Decisione → Stakeholder → Domanda → Metriche → Ipotesi → Scope → Baseline → Segmentazioni → Dati → Piano → Priorità → Stop rule**

Non sostituisce la catena analitica completa del Capitolo 1. È il contratto che la rende eseguibile.

### Esercizio 1 — Costruire un brief da una richiesta vaga

Richiesta:

> “Vorrei capire meglio i nostri clienti.”

Costruisci tre Analytical Brief diversi a partire dalla stessa frase:

1. uno per decidere come allocare budget marketing;
2. uno per ridurre churn;
3. uno per progettare un dashboard operativo per customer success.

Per ciascuno specifica almeno:

- problema;
- decision owner;
- domanda primaria;
- tipo di domanda;
- outcome;
- scope;
- baseline;
- dati required;
- output;
- stop rule.

Confronta quanto cambia il piano pur partendo dalla stessa richiesta.

### Esercizio 2 — Decision specification

Il CFO dice:

> “Il fatturato è sceso del 12%. Dobbiamo capire perché.”

Prima di pensare ai dati, scrivi:

- decisione da supportare;
- alternative realistiche;
- deadline;
- costo di un falso allarme;
- costo di non vedere un problema reale;
- risultato che sarebbe abbastanza materialmente importante da cambiare la scelta.

Poi formula la domanda analitica.

### Esercizio 3 — Metric contract

Scegli una delle seguenti metriche:

- churn rate;
- conversion rate;
- repeat purchase rate;
- margine per ordine;
- cliente attivo.

Compila:

```text
Ruolo nel brief:
Definizione business:
Formula:
Popolazione:
Numeratore/denominatore:
Unità/grain:
Finestra temporale:
Esclusioni:
Fonte/owner:
Baseline/target:
Guardrail:
Casi in cui non andrebbe usata:
```

### Esercizio 4 — Hypothesis register

La conversione mobile è diminuita dell'11%.

Genera almeno otto spiegazioni candidate, includendo obbligatoriamente:

- una spiegazione di prodotto;
- una di marketing mix;
- una di disponibilità/catalogo;
- una di misurazione/tracking.

Per ogni ipotesi annota:

- evidenza attesa se vera;
- evidenza che la indebolirebbe;
- dato necessario;
- costo di verifica;
- priorità.

### Esercizio 5 — Scope e maturazione

Devi misurare repeat purchase a 90 giorni.

Il dataset contiene clienti acquisiti fino a ieri.

Definisci:

- popolazione eleggibile;
- periodo di acquisizione utilizzabile;
- unità di analisi;
- evento che conta come secondo acquisto;
- trattamento di cancellazioni e resi;
- campo temporale;
- data a cui il dataset può considerarsi maturo.

Spiega come cambierebbe la metrica se includessi clienti non ancora osservabili per 90 giorni.

### Esercizio 6 — Baseline sbagliata

Un retailer comunica che gennaio è cresciuto del 14% rispetto a dicembre.

Elenca almeno quattro motivi per cui questo confronto potrebbe essere poco informativo.

Poi proponi:

- una baseline stagionale;
- una baseline rispetto al piano;
- un confronto operativo;
- un confronto che sarebbe necessario per sostenere una pretesa causale più forte.

### Esercizio 7 — Data requirements e gap

La domanda è:

> “Il nuovo onboarding riduce il churn?”

Elenca i dati che vorresti avere, classificandoli come:

- required;
- useful;
- proxy.

Poi immagina che non esista un campo affidabile che indichi quale onboarding abbia visto il cliente.

Scrivi come cambieresti:

- domanda;
- livello di pretesa;
- dati da raccogliere in futuro;
- eventuale esperimento successivo.

### Esercizio 8 — Priorità e Value of Information

Hai quattro richieste:

- anomalia su una metrica secondaria senza decisioni collegate;
- churn enterprise +20% prima del rinnovo annuale;
- forecast di capacità per un'espansione irreversibile;
- richiesta estetica di redesign di un report già utilizzabile.

Costruisci una scorecard con:

- impatto;
- urgenza;
- incertezza riducibile;
- costo analitico.

Poi indica quale prima analisi minima eseguiresti per ciascuna richiesta prima di impegnare altro tempo.

### Esercizio 9 — Stop rule

Hai scoperto che l'85% del calo delle vendite proviene da due categorie che hanno avuto stock-out ripetuti.

Definisci:

- controlli minimi prima di concludere;
- analisi che faresti ancora;
- analisi che non faresti;
- una stop rule esplicita;
- una condizione che ti obbligherebbe invece a riaprire lo scope.

### Esercizio 10 — Conclusione inconcludente

Due onboarding flow differiscono di 3 punti percentuali nella retention osservata, ma il campione è piccolo e l'incertezza ampia.

Scrivi:

1. una conclusione troppo sicura;
2. una conclusione tecnicamente corretta;
3. una conclusione executive;
4. il prossimo dato o test con maggiore Value of Information.

### Esercizio 11 — AI come supporto al brief

Usa un sistema AI per generare possibili ipotesi, dati richiesti e controlli per un calo del conversion rate.

Non chiedergli di “risolvere il problema”.

Confronta il suo output con il tuo brief e annota:

- quali ipotesi nuove sono utili;
- quali ignorano il contesto del dominio;
- quali dati suggeriti non esistono;
- quali definizioni ha assunto senza dichiararle;
- quali elementi meritano davvero di essere aggiunti al piano.

L'obiettivo è usare l'AI come generatore di alternative, non come owner del brief.

## Domande di autovalutazione

Alla fine del capitolo dovresti saper rispondere a queste domande:

1. So distinguere problema di business, decisione e domanda analitica?
2. So identificare chi chiede, chi decide, chi conosce il dominio e chi possiede la metrica?
3. So assegnare un ruolo alle metriche nel brief?
4. So costruire un registro delle ipotesi che includa evidenza contraria?
5. So definire scope, popolazione, unità e maturazione?
6. So scegliere una baseline coerente con la domanda?
7. So distinguere segmentazioni pre-specificate ed esplorative?
8. So trasformare esigenze informative in dati required, useful e proxy?
9. So decidere quanto approfondire usando priorità e Value of Information?
10. So definire una stop rule?
11. So consegnare in modo utile un risultato inconcludente?
12. So produrre un Analytical Brief di una pagina prima di aprire il tool?

## Chiusura — Il brief incontra i dati

Un buon brief non garantisce una buona analisi. Può però rendere molto più visibili le condizioni che l'analisi dovrà rispettare e, soprattutto, le assunzioni che le fonti dovranno essere in grado di sostenere.

Finora abbiamo scritto cose come “identità cliente coerente”, “ordine valido”, “campo temporale”, “fonte disponibile” o “dato completo”. Nel brief queste espressioni sono requisiti. Nel prossimo capitolo diventeranno domande empiriche.

Dovremo aprire le sorgenti e verificare se l'identità è davvero stabile, se le chiavi sono uniche al grain dichiarato, se il tracking è comparabile nel tempo, se gli eventi arrivano con la latenza attesa e se le trasformazioni conservano il significato su cui abbiamo costruito il piano.

Il passaggio è importante: il Capitolo 2 ha definito **quale realtà vorremmo osservare**. Il Capitolo 3 verificherà quanto i dati disponibili riescano davvero a rappresentarla.
