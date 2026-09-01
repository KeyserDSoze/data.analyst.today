## 17.4 “Quale marketing crea vendite che altrimenti non avremmo avuto?”

### Caso simulato/composito: Helio Market

Un retailer omnicanale, **Helio Market**, investe 18 milioni di euro l'anno in advertising digitale.

Il CMO chiede:

> “Quale canale ci porta davvero più vendite?”

La dashboard last-click risponde subito: branded search.

ROAS attribuito: `11,8x`.

Sembra una risposta precisa. Ma il verbo “porta” nasconde due domande diverse:

1. quale canale compare nel percorso di conversione?
2. quante vendite in più esistono **a causa** della spesa su quel canale?

La prima è attribution.

La seconda è incrementality.

## Routing iniziale

| Elemento | Scelta |
|---|---|
| Decisione | riallocare il budget del prossimo trimestre |
| Failure cost | spostare milioni verso canali che catturano domanda esistente invece di crearla |
| Claim necessario | causale/incrementale per i grandi spostamenti di budget |
| Reversibilità | media: il budget può essere riallocato, ma il trimestre perso non torna |
| Incertezza critica | cannibalizzazione paid/organic e effetti ritardati |
| Stop rule | nessuna riallocazione materiale basata soltanto su attribution credit |

## 1. Attribution descrive un percorso, non un controfattuale

Un cliente:

- vede un video;
- visita il sito da social;
- riceve una newsletter;
- cerca il brand;
- clicca un annuncio branded;
- compra.

Il last-click assegna il credito finale alla ricerca branded.

Il first-click lo assegna al video.

Un modello data-driven può distribuire il credito in modo più sofisticato.

Ma nessuno di questi meccanismi, da solo, risponde alla domanda:

> “La vendita sarebbe avvenuta comunque senza quella spesa?”

Questo è il controfattuale che interessa alla decisione di budget.

## 2. Data Readiness Review: online e offline appartengono allo stesso sistema

Helio Market vende anche in negozio.

Molti utenti vedono advertising online e completano l'acquisto offline.

Il vecchio modello rendeva queste vendite quasi invisibili al marketing digitale.

Il team costruisce quindi, dove legalmente e tecnicamente consentito, un sistema che collega:

- campaign exposure;
- web sessions;
- app events;
- loyalty identity;
- ecommerce orders;
- store purchases;
- costi media;
- contribution margin.

La privacy boundary entra nel disegno: non tutta l'identità disponibile tecnicamente deve essere usata, e il matching deve essere coerente con purpose limitation, consenso e governance applicabile.

## Caso reale documentato: Hoff

Google Cloud documenta il caso del retailer **Hoff**, che voleva capire meglio come attività online e vendite nei negozi fisici fossero collegate. Hoff e il partner OWOX costruirono un sistema end-to-end che raccoglieva dati da più sorgenti in BigQuery e sviluppava nuovi modelli di revenue attribution. Il case study riporta un aumento del 17% del ROI della pubblicità online dopo l'uso delle nuove analisi.

Fonte: https://cloud.google.com/customers/hoff

Il claim corretto da portare nel libro è limitato a ciò che la fonte documenta:

- migliore integrazione tra dati online/offline;
- nuovi modelli di attribution;
- uso operativo dei risultati per ottimizzare il marketing;
- ROI online riportato dal case study in aumento del 17%.

Non dobbiamo trasformare questo caso in una prova che l'attribution model identificasse causalmente ogni vendita incrementale.

Questa distinzione è esattamente la lezione del capitolo.

## Caso reale documentato: Freshworks

Google Cloud documenta anche **Freshworks** come organizzazione che usa dati di campagne, conversioni, revenue e CRM per analizzare il ROI di migliaia di campagne e collegare marketing e customer lifecycle. La fonte riporta che la maggiore focalizzazione su campagne, regioni e keyword contribuì a un aumento del 50% del ROI.

Fonte: https://cloud.google.com/customers/freshworks

Anche qui il valore didattico è l'integrazione tra costo, conversione e revenue. La fonte non sostituisce un esperimento di incrementalità.

## 3. Il problema del branded search

Nel caso Helio Market, branded search mostra ROAS attribuito `11,8x`.

Ma molti utenti che cliccano l'annuncio stavano già cercando esplicitamente il marchio.

Il team formula due ipotesi concorrenti:

- **H1:** il paid branded protegge vendite che altrimenti andrebbero perse;
- **H2:** una parte rilevante dei click paid cannibalizza traffico organic/direct che avrebbe convertito comunque.

L'attribution dashboard non può discriminare bene tra H1 e H2.

## 4. Causal Identification Brief: quale variation può aiutarci?

Il team cerca un disegno che produca un confronto credibile.

Dove operativamente possibile, pianifica una riduzione controllata della pressione paid branded in mercati confrontabili, definendo prima:

- unità geografica;
- periodo pre-test;
- controllo di trend e composizione;
- spesa effettivamente ridotta;
- outcome totale, non soltanto click paid;
- spillover tra aree;
- criteri di stop.

Nel caso simulato, durante il test:

- i click paid branded scendono molto;
- una quota migra verso organic;
- le vendite totali diminuiscono molto meno dei click;
- l'incremental ROAS risulta molto più basso del ROAS attribuito.

Il canale non è “inutile”.

Il suo **credito attribuito** è semplicemente diverso dal suo **valore incrementale**.

## 5. Il problema opposto: prospecting sottovalutato

Per video prospecting accade il contrario.

Last-click assegna poco credito perché molte conversioni arrivano giorni dopo tramite direct o search.

I test geografici del caso simulato indicano un effetto incrementale maggiore di quanto suggerisse l'attribution dashboard.

Questo mostra un punto importante:

> attribution può sovrastimare un canale e sottostimarne un altro nello stesso sistema.

## 6. MMM, experiment e attribution rispondono a domande differenti

Helio Market smette di cercare “il modello unico”.

Usa:

### Attribution

Per descrivere customer journey e assist tra touchpoint.

### Experimentation

Per stimare incrementalità quando esiste variation controllabile e il rischio lo giustifica.

### Marketing Mix Modeling

Per ragionare su allocazioni aggregate, canali difficili da randomizzare e dinamiche di lungo periodo, con le relative assunzioni.

### Marginal ROI

Per rispondere alla domanda economicamente più utile:

> “Dove produce più valore il **prossimo euro** di budget?”

Questo è diverso dal chiedere chi meriti il credito per l'euro già speso.

## 7. Decision Record

Le alternative sono:

### A — Riallocare usando ROAS last-click

Facile e veloce, ma con alto rischio di cannibalizzazione nascosta.

### B — Aspettare esperimenti perfetti su ogni canale

Più rigoroso in teoria, ma impraticabile e costoso.

### C — Sistema di evidenza ibrido

- attribution per il percorso;
- experiment sui grandi spostamenti testabili;
- MMM per livello aggregato;
- marginal ROI per allocazione;
- contribution margin e new-customer economics come outcome;
- refresh periodico perché la risposta marginale cambia con la spesa.

La scelta è C.

## 8. Switching condition

Una riallocazione materiale viene approvata soltanto se:

- il range plausibile dell'incremental ROI resta sopra la soglia economica;
- la conclusione non dipende da un singolo modello fragile;
- cannibalizzazione e lag principali sono inclusi;
- l'allocazione rimane robusta a scenari ragionevoli.

Se l'incertezza attraversa la soglia, il valore di un test aggiuntivo può superare il costo dell'attesa.

## 9. Decision Communication Pack

La headline non è:

> “Branded search ha ROAS 11,8x.”

È:

> **“Il ROAS attribuito sovrastima il valore incrementale del branded search e sottovaluta parte del prospecting. Per il prossimo trimestre proponiamo di riallocare il budget usando evidenza incrementale e marginal ROI, non il solo credito di conversione.”**

Il pack mostra:

1. attributed vs incremental revenue;
2. esperimenti e loro limiti;
3. marginal ROI con intervalli/scenari;
4. effetti paid/organic;
5. decisione richiesta e budget delta.

## 10. Outcome review

Il nuovo framework misura:

- attributed revenue;
- incremental revenue;
- marginal ROAS;
- CAC;
- payback period;
- new-customer rate;
- contribution margin;
- cannibalizzazione paid/organic;
- risposta marginale al variare della spesa.

## Cosa abbiamo scelto di non fare

Non proviamo ad attribuire causalmente ogni singola conversione a ogni touchpoint.

È spesso una pretesa superiore all'identificabilità del sistema.

La catena effettiva è:

**Analytical Brief → Data Readiness Review → Causal Identification Brief → Experiment Contract dove possibile → Uncertainty Brief → Decision Record → Decision Communication Pack**

con attribution e MMM come strumenti complementari, non come oracoli.

> **Attribution racconta chi era presente nel percorso. Incrementality cerca di capire chi ha cambiato il percorso. Marginal ROI decide dove dovrebbe andare il prossimo euro.**
