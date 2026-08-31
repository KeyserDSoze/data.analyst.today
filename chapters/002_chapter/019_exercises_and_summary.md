## 2.18 Sintesi ed esercizi

Il Capitolo 2 ha trasformato la mentalità analitica del Capitolo 1 in un oggetto operativo: l'**Analytical Brief**.

Il brief collega una richiesta di business a una specifica sufficientemente precisa da guidare dati, metodo ed esecuzione senza anticipare artificialmente la risposta.

Il percorso del capitolo è:

**Problema → Decisione → Stakeholder → Domanda → Metriche → Ipotesi → Scope → Baseline → Segmentazioni → Dati → Piano → Priorità → Stop rule**

Non sostituisce la catena analitica completa del Capitolo 1. È la parte che dobbiamo progettare **prima** di eseguirla.

### Idee chiave

- Una richiesta descrive spesso un sintomo o un deliverable, non ancora il problema analitico.
- La decisione determina profondità, timing e formato dell'analisi.
- Requester, decision owner, domain expert, data owner ed end user possono essere persone diverse.
- Le metriche nel brief devono avere un ruolo: outcome, driver, guardrail o soglia.
- Le ipotesi sono spiegazioni candidate; una buona ipotesi include anche ciò che potrebbe indebolirla.
- Scope significa popolazione, unità di analisi, tempo, esclusioni e fuori-scope.
- Una baseline rende il numero interpretabile, ma non è automaticamente un controfattuale causale.
- Le segmentazioni prioritarie devono poter cambiare spiegazione o azione.
- I dati required, useful e proxy non sono la stessa cosa.
- Un gap di misurazione scoperto prima dell'analisi è un risultato utile.
- Prioritizzazione e Value of Information aiutano a decidere quanto investire nell'analisi.
- Una stop rule protegge sia dalla superficialità sia dall'analisi infinita.
- “Inconcludente” è un possibile esito professionale, non una risposta da nascondere.

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

## Chiusura

Un buon brief non garantisce una buona analisi.

Ma rende molto più visibili le condizioni che una buona analisi dovrà rispettare.

Nel prossimo capitolo entreremo nella materia prima del lavoro: il dato. A quel punto la domanda non sarà più soltanto “quali informazioni ci servono?”, ma:

> **“Le fonti che abbiamo rappresentano davvero ciò che il brief presume, e con quale qualità?”**
