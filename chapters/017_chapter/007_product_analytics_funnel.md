## 17.6 “Cosa si è rotto nell'onboarding?”: forse niente

### Caso simulato/composito: PulseNote

PulseNote è un SaaS di collaborazione con 420.000 utenti attivi mensili e un modello freemium.

Nel giro di sei settimane il tasso di activation dei nuovi account scende dal 43% al 35%.

Il product manager chiede:

> “Cosa si è rotto nell'onboarding?”

È una domanda plausibile, ma contiene già una spiegazione: che qualcosa **si sia rotto** nel prodotto.

Il capstone comincia proprio qui: prima di scegliere una tecnica, dobbiamo verificare se la domanda è formulata in modo troppo stretto.

## Routing iniziale

| Elemento | Scelta |
|---|---|
| Decisione | correggere onboarding, cambiare acquisition mix o ridefinire activation |
| Failure cost | ottimizzare un passaggio che non rappresenta più il valore reale |
| Claim necessario | diagnostico prima, causale solo per il redesign |
| Reversibilità | alta per test di onboarding; media per riallocazione marketing |
| Incertezza critica | mix shift vs degradazione dell'esperienza |
| Stop rule | non ridisegnare il flow finché non sappiamo se il calo esiste a parità di popolazione |

## 1. Il funnel localizza una perdita, non ne identifica la causa

Il funnel aggregato mostra:

| Step | Prima | Dopo | Delta |
|---|---:|---:|---:|
| Signup completato | 100% | 100% | — |
| Workspace creato | 82% | 80% | -2 pp |
| Primo invito inviato | 61% | 52% | -9 pp |
| Primo documento condiviso | 49% | 41% | -8 pp |
| Activation entro 7 giorni | 43% | 35% | -8 pp |

Il punto di rottura sembra evidente: **primo invito**.

La prima storia disponibile sarebbe:

> “Il flow di invito ha peggiorato la conversione.”

Ma un funnel descrive **dove** osserviamo la perdita. Non dimostra automaticamente **perché** la perdita esista.

## 2. Data Readiness Review

Prima di intervenire, l'analista controlla:

- definizione di activation;
- event coverage per versione;
- duplicate/missing event;
- finestra temporale;
- nuovi template;
- cambi di acquisition source;
- country e device mix;
- account aziendali vs individuali.

Il tracking è stabile.

Il cambiamento principale è nella popolazione in ingresso.

## 3. Mix shift: il funnel non era necessariamente rotto

Il calo è quasi tutto concentrato negli account acquisiti tramite una nuova campagna paid rivolta a freelance e studenti.

Nel segmento storico B2B il funnel è praticamente stabile.

Prima della campagna:

- 68% account aziendali;
- 32% individuali.

Dopo:

- 47% account aziendali;
- 53% individuali.

Gli utenti individuali hanno meno probabilità di invitare qualcuno perché spesso usano PulseNote da soli.

Il funnel aggregato peggiora, ma non abbiamo ancora evidenza che l'esperienza sia peggiorata.

È cambiata la popolazione che attraversa una metrica progettata per il vecchio comportamento dominante.

## 4. La metrica può diventare semanticamente obsoleta

La definizione di activation era:

> “workspace creato + almeno un invito + almeno un documento condiviso entro sette giorni”.

Era sensata quando il prodotto era quasi interamente collaborativo.

Con l'arrivo di single-player users, quella metrica rischia di confondere:

- mancata creazione di valore;
- percorso di valore differente.

La domanda quindi cambia da:

> “Come aumentiamo gli inviti?”

a:

> **“Quali comportamenti precoci predicono valore e retention nei due segmenti?”**

Questo è un problema di lifecycle semantics, non soltanto di funnel conversion.

## 5. Lifecycle Diagnostic Map: due percorsi di valore

L'analista costruisce due activation path.

### Collaborativo

Workspace → invito → documento condiviso → ritorno di almeno due membri.

### Individuale

Workspace → creazione di tre note → utilizzo in almeno tre giorni diversi → ritorno entro sette giorni.

Nel segmento individuale, il secondo percorso è molto più associato alla retention a 30 giorni rispetto all'invio di un invito.

Questo non basta ancora a dimostrare che “tre note causano retention”.

Ma è sufficiente per dire che il vecchio KPI non misura bene il percorso di valore del nuovo segmento.

## 6. Tre ipotesi concorrenti

Ora il team distingue:

1. **traffico di bassa qualità** — il segmento nuovo ha scarso valore economico;
2. **metrica sbagliata** — il segmento crea valore ma attraverso un altro percorso;
3. **opportunità prodotto** — esiste un use case single-player che merita onboarding e packaging differenti.

Per discriminare tra queste ipotesi servono:

- retention 30/60 giorni;
- conversione a paid;
- cost-to-acquire;
- willingness to collaborate;
- feature adoption;
- support/contact rate;
- cohort economics.

## 7. L'errore possibile: ottimizzare il passaggio visibile

Se il team ridisegnasse immediatamente il bottone `Invite`, potrebbe aumentare artificialmente gli inviti senza aumentare il valore.

Potrebbe perfino:

- generare spam;
- peggiorare la UX;
- confondere utenti individuali;
- aumentare un KPI che non predice più retention.

Questo è un esempio di **metric gaming involontario**: il team ottimizza ciò che è facile misurare invece del comportamento che crea valore.

## 8. Experiment Contract: testare il percorso, non il bottone

Il team costruisce un test di onboarding differenziato per il nuovo segmento.

### Variante A

Onboarding collaborativo standard.

### Variante B

Onboarding che permette di scegliere `uso individuale` o `uso con team` e propone azioni coerenti.

Primary outcome:

- activation path coerente con l'intento dichiarato.

Guardrail:

- retention a 30 giorni;
- paid conversion;
- support contacts;
- spam/invite complaints;
- time-to-first-value.

L'esperimento non chiede soltanto quale schermata produce più click.

Chiede quale onboarding porta più utenti verso un comportamento associato a valore reale.

## 9. Decision Record

Le alternative sono:

### A — Riparare il flow invite per tutti

Facile, ma tratta il sintomo aggregato come causa.

### B — Abbandonare la nuova campagna

Riduce il mix shift, ma può eliminare un segmento economicamente interessante prima di averlo capito.

### C — Separare percorsi e misurare economia per segmento

- due activation path;
- onboarding differenziato;
- retention e monetizzazione separate;
- test del nuovo flow;
- rivalutazione dell'economia della campagna;
- eventuale revisione del KPI aziendale di activation.

La scelta è C.

## 10. Decision Communication Pack

La headline non è:

> “Activation è scesa di 8 punti.”

È:

> **“Il calo aggregato di activation è quasi interamente un mix shift: il nuovo segmento individuale attraversa un percorso di valore diverso e rende obsoleta parte della metrica attuale. Proponiamo activation path separati e un test di onboarding differenziato prima di concludere che il prodotto sia peggiorato.”**

## 11. Outcome review

Il post-decision review misura:

- retention 30/60 giorni per percorso;
- paid conversion;
- time-to-first-value;
- CAC e payback per segmento;
- adoption delle feature core;
- stabilità della nuova definizione di activation.

## Cosa abbiamo scelto di non fare

Non serve un churn model per spiegare il calo iniziale.

Non serve causal inference sofisticata per riconoscere che la popolazione è cambiata e la metrica non è più fit for purpose.

Serve invece un esperimento quando passiamo dalla diagnosi al redesign.

La catena è:

**Data Readiness Review → Lifecycle Diagnostic Map → EDA Evidence Map → Experiment Contract → Decision Record → Decision Communication Pack**

> **Un funnel indica dove guardare. La maturità analitica comincia quando ci chiediamo se quello step rappresenta ancora il valore che pensavamo rappresentasse.**
