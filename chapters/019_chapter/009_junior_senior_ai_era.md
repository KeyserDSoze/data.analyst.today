## 19.8 Junior, senior e scope di responsabilità nell'era AI

L'AI non elimina la differenza tra junior e senior.

Rende più debole uno dei vecchi segnali della differenza: **la quantità di esecuzione tecnica che una persona riesce a produrre senza assistenza**.

Un junior può oggi generare molto rapidamente:

- query;
- codice;
- grafici;
- modelli baseline;
- documentazione;
- presentazioni.

Questo può comprimere anni di attrito operativo.

Non comprime automaticamente anni di esposizione a:

- incidenti;
- metriche ambigue;
- stakeholder in conflitto;
- esperimenti falliti;
- dati incompleti;
- false causal claim;
- forecast sbagliati;
- rollout con effetti collaterali;
- sistemi che cambiano significato senza cambiare schema.

La seniority si sposta quindi verso **scope di responsabilità e qualità del judgment**.

## Quattro dimensioni della seniority

### 1. Ambiguity span

Quanto è poco definito il problema che riesci a strutturare?

Un junior lavora meglio quando:

- task;
- dati;
- output;
- criteri di accettazione

sono abbastanza chiari.

Un senior riesce a trasformare una richiesta come:

> “La crescita è sana?”

in un percorso di decisione e evidenza senza chiedere che il problema venga già pre-segmentato.

### 2. Failure span

Quanto è grave il failure mode che sei capace di anticipare e governare?

Non soltanto:

- syntax error;
- query lenta;

ma anche:

- semantic drift;
- leakage;
- selection;
- causal overclaim;
- metric gaming;
- operational capacity mismatch;
- irreversible rollout.

### 3. Coordination span

Quante dipendenze sai orchestrare?

- stakeholder;
- team;
- semantic owner;
- engineer;
- specialist;
- agent;
- external source;
- decision owner.

Più aumenta il sistema, meno il lavoro è individuale.

### 4. Decision span

Quanto vicino sai accompagnare l'evidenza verso:

- alternative;
- trade-off;
- recommendation;
- policy;
- rollout;
- feedback loop?

La seniority cresce quando questi quattro span aumentano senza perdere rigore.

## Una progressione più utile

### Junior — Task reliability

Sa:

- eseguire task relativamente ben definiti;
- usare AI e tool;
- controllare grain, denominatori e output di base;
- chiedere chiarimenti;
- riconoscere quando non è sicuro;
- documentare cosa ha fatto.

Success metric:

> **l'output è corretto e sa spiegare i controlli principali.**

### Mid-level — Problem ownership

Sa:

- trasformare problemi moderatamente ambigui;
- scegliere metodi;
- costruire ipotesi;
- coordinare stakeholder;
- progettare verification;
- collegare evidence e recommendation.

Success metric:

> **l'analisi riduce davvero una decision uncertainty.**

### Senior — Decision/system ownership

Sa:

- definire risk/claim level;
- anticipare failure mode;
- orchestrare persone e agenti;
- progettare stop/escalation;
- scegliere cosa non analizzare;
- proteggere semantica e causalità;
- collegare decisione a economics e rollout;
- rendere il processo riutilizzabile quando necessario.

Success metric:

> **il sistema prende decisioni migliori senza dipendere dalla sua presenza continua.**

### Lead / Principal — Organizational capability

Sa migliorare:

- standard;
- operating model;
- metric governance;
- experimentation culture;
- AI/agent governance;
- talent development;
- decision quality cross-team.

Success metric:

> **molte persone e sistemi lavorano meglio perché la capacità è stata incorporata nell'organizzazione.**

## Caso simulato/composito: stesso agente, due risultati professionali

Un junior e un senior ricevono:

> “Perché la conversion è scesa del 12%?”

Entrambi hanno lo stesso agente.

L'agente produce:

- SQL;
- breakdown geografico;
- device segmentation;
- grafici;
- cinque spiegazioni plausibili.

Il junior sceglie l'ipotesi con correlazione più forte.

Il senior prima controlla:

1. definizione e denominator;
2. data readiness;
3. traffic mix;
4. release/change log;
5. timing dell'anomalia;
6. alternative hypothesis.

Scopre che:

- la definizione di conversion è cambiata due settimane prima;
- paid traffic ha spostato il mix;
- una release è sovrarappresentata nel segmento residuo.

Il vantaggio senior non è aver scritto più SQL.

È aver capito **in quale ordine il sistema poteva ingannarlo**.

## Il problema dell'apprendistato

Storicamente molte intuizioni venivano costruite attraverso attività ripetitive:

- pulizia;
- query semplici;
- debugging;
- reconciliation;
- reporting manuale;
- code review.

Se l'AI assorbe immediatamente tutta questa superficie, un junior può ottenere output senior-looking senza aver attraversato abbastanza failure mode.

Questo crea un problema di **experience compression apparente**.

La produzione accelera.

L'esperienza no.

## Non serve conservare lavoro inutile

La risposta non è obbligare un junior a passare sei mesi a copiare CSV “perché così si impara”.

Serve progettare apprenticeship più deliberato.

Per esempio:

- review di query AI con bug nascosti;
- metric definition exercise;
- data incident shadowing;
- causal claim critique;
- experiment design review;
- forecast stress test;
- postmortem;
- decision record review;
- agent eval failure analysis.

Meno lavoro ripetitivo senza feedback.

Più esposizione intenzionale ai failure mode.

## Review depth come strumento di crescita

Per un junior, la review può essere più profonda:

- leggere SQL completo;
- ricostruire denominator;
- spiegare join;
- verificare sample;
- replicare un risultato.

Con esperienza, parte della review può diventare risk-based.

Ma dovrebbe essere una **compressione conquistata**, non una fiducia concessa automaticamente perché l'agente ha una buona reputazione.

## La seniority non è sapere tutto

Un senior forte dice anche:

> “Qui non ho sufficiente profondità.”

E coinvolge:

- statistician;
- security;
- legal/privacy;
- ML engineer;
- domain expert;
- Finance.

Escalare correttamente un rischio che non possiamo governare è un comportamento senior.

## Una definizione più robusta

> **La seniority nell'era AI si misura sempre meno dalla quantità di lavoro che sappiamo eseguire da soli e sempre più dall'ampiezza di ambiguità, rischio e responsabilità che sappiamo governare senza perdere il controllo su significato ed evidenza.**
