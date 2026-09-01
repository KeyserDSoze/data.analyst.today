## 18.4 Change management: schema stabile non significa significato stabile

Un sistema analitico maturo non deve soltanto funzionare oggi.

Deve poter cambiare domani senza rendere invisibile **che cosa** è cambiato, **chi** è impattato e **se** la comparabilità è ancora valida.

Le sorgenti cambiano.

Le organizzazioni cambiano.

Le definizioni cambiano.

Le policy cambiano.

Le piattaforme cambiano.

Il problema non è evitare il cambiamento.

È impedire che un cambiamento legittimo si trasformi in un incidente semantico.

## Quattro tipi di change

Possiamo classificare una modifica almeno lungo quattro dimensioni.

### 1. Technical change

Esempi:

- engine SQL;
- orchestratore;
- storage;
- refactoring;
- performance optimization.

Può non cambiare l'output osservabile.

### 2. Structural change

Esempi:

- colonna rinominata;
- tipo modificato;
- chiave sostituita;
- schema nested.

È spesso facile da intercettare con contract e test.

### 3. Semantic change

Esempi:

- `active_customer` passa da 90 a 60 giorni;
- `completed` cambia da “consegnato” a “pagamento autorizzato”;
- revenue passa da gross a net;
- il denominatore di conversion include una nuova popolazione.

Questi cambi sono pericolosi proprio perché la pipeline può continuare a funzionare.

### 4. Operating change

Esempi:

- refresh da hourly a daily;
- supporto non più 24/7;
- fonte che diventa provisional;
- SLO rilassato;
- owner trasferito;
- prodotto destinato a un nuovo consumer critico.

Anche questo può cambiare il diritto di usare il dato.

## Il Compatibility Contract

Per ogni data product T2/T3 l'Analytics Operating Contract dovrebbe chiarire che cosa i consumer possono aspettarsi stabile.

Per esempio:

```text
primary key
+ grain
+ required fields
+ semantic meaning
+ metric definitions
+ freshness class
+ history policy
+ supported interface
+ deprecation notice window
```

Il Compatibility Contract non promette immobilità.

Promette che una modifica incompatibile sarà **riconoscibile e gestita**.

## Caso simulato/composito: schema verde, revenue sbagliata

Un marketplace riceve `order_status` dal sistema ordini.

Per anni:

`completed = pagamento acquisito + ordine consegnato`

Dopo una migrazione:

`completed = pagamento autorizzato`

La colonna:

- ha lo stesso nome;
- ha lo stesso tipo;
- contiene ancora il valore `completed`.

Passano:

- schema test;
- not-null test;
- accepted-values test.

Ma downstream:

- revenue viene anticipata;
- cancellation rate scende artificialmente;
- delivery metrics diventano incoerenti;
- Finance smette di riconciliare.

Questo è un **semantic breaking change**.

Il test decisivo non era sul tipo del campo.

Era sul **contratto di significato**.

## Breaking change: la domanda giusta

Una modifica è breaking non soltanto quando rompe una query.

È breaking se può cambiare una decisione o l'interpretazione senza che il consumer lo abbia accettato.

Quindi può essere breaking:

- ridurre una finestra temporale;
- aggiungere una popolazione;
- spostare un cut-off;
- cambiare currency conversion;
- ricalcolare una serie storica;
- modificare un mapping territorio;
- introdurre una nuova identity-resolution policy.

> **Se il significato della serie può cambiare mantenendo lo stesso nome, il change process deve essere più forte del solo schema test.**

## Versionare codice, semantica e decision boundary

Un prodotto critico dovrebbe versionare almeno:

- transformation code;
- metric definition;
- schema;
- mapping/configuration;
- test;
- documentation;
- access policy quando rilevante;
- Operating Contract.

Non tutto richiede un suffisso `_v2` nella tabella.

La versione può vivere in catalogo, metadata o semantic layer.

Ciò che conta è poter ricostruire:

> **“Quale logica e quale significato erano in vigore quando questa decisione è stata presa?”**

## Backfill policy: il passato non si riscrive per default

Quando una definizione cambia esistono almeno tre strategie.

### Full backfill

Ricalcolare il passato con la nuova logica.

Utile quando:

- i dati storici permettono un calcolo coerente;
- il nuovo significato deve essere confrontabile nel tempo;
- il costo è proporzionato.

Rischio:

- i report storici cambiano;
- decisioni passate sembrano basate su numeri che allora non esistevano.

### Forward-only

Nuova logica da una data esplicita.

Utile quando:

- la realtà business è cambiata;
- il passato non è ricostruibile;
- mantenere la discontinuità è più onesto.

Richiede annotazione chiara.

### Dual reporting

Vecchia e nuova logica convivono durante la migrazione.

Utile per:

- quantificare l'impatto;
- preparare consumer;
- aggiornare threshold;
- validare downstream.

L'errore è lasciare che la strategia emerga accidentalmente dall'implementazione.

## Change classification

Non ogni modifica richiede lo stesso processo.

### Low-risk / compatible

- typo documentale;
- nuova colonna opzionale;
- ottimizzazione con output invariato.

Può avere review leggera.

### Material compatible change

- nuova dimensione;
- miglioramento quality;
- performance change che potrebbe influire su latency.

Richiede test e consumer awareness proporzionata.

### Breaking structural/semantic change

- grain;
- key;
- denominator;
- business definition;
- history rewrite;
- freshness commitment.

Richiede:

- impact analysis;
- approvazione owner appropriati;
- migration plan;
- consumer notice;
- rollback/fallback;
- version strategy.

## Caso reale documentato: Microsoft e change management

La Microsoft Fabric Adoption Roadmap tratta il change management come una disciplina necessaria a ridurre disruption e perdita di produttività. La guida raccomanda di:

1. descrivere stato prima/dopo;
2. stimare l'impatto;
3. identificare le priorità;
4. implementare incrementi gestibili;
5. creare action plan per ogni fase, includendo quando possibile un rollback plan.

Fonte: https://learn.microsoft.com/en-us/power-bi/guidance/fabric-adoption-roadmap-change-management

La stessa guida sottolinea che il cambiamento è un problema di **persone**, non soltanto di tool e processo.

Per l'analytics questo è evidente: modificare una metrica significa modificare dashboard, abitudini, threshold, KPI e spesso incentivi.

## Consumer impact analysis

Prima di una breaking change, il team dovrebbe sapere:

- quali dashboard dipendono dal prodotto;
- quali query/job;
- quali modelli ML;
- quali agenti AI;
- quali report esterni;
- quali threshold/alert;
- quali processi manuali;
- quali owner.

Lineage aiuta, ma non basta se i consumer non sono registrati o interrogano export locali.

Per prodotti critici può servire un **consumer registry** o almeno un meccanismo di subscription alle change notice.

## Change notice

Una notice utile risponde in modo operativo:

```text
what changes
why
effective date
old vs new meaning
expected numerical impact
history/backfill policy
assets affected
migration action required
owner/support
rollback/fallback
```

Una mail generica:

> “Da lunedì aggiorniamo il modello dati.”

non è change management.

## Threshold migration

Un cambio semantico può rendere obsolete le soglie decisionali.

Se `active_customer` cambia popolazione, possono cambiare:

- target;
- alert threshold;
- forecast baseline;
- model feature distribution;
- executive traffic-light status.

Quindi la migrazione deve considerare **semantic threshold debt**.

Non basta che il nuovo numero sia corretto.

Le decision rule che lo consumano devono essere corrette rispetto alla nuova definizione.

## Deprecation: il debito invisibile dell'analytics

Molti ecosistemi accumulano:

- `dashboard_final`;
- `dashboard_final_v2`;
- `revenue_old`;
- `customer_new`;
- tabelle duplicate;
- metriche non certificate;
- report senza owner.

Ogni asset obsoleto aumenta la probabilità che:

- un nuovo analyst scelga quello sbagliato;
- un agente AI recuperi una definizione superata;
- un consumer continui a usare un sistema non più supportato.

Per questo gli asset dovrebbero poter avere stati:

```text
EXPERIMENTAL
→ SUPPORTED
→ CERTIFIED
→ DEPRECATED
→ RETIRED
```

Non tutte le fasi sono obbligatorie, ma lo stato deve essere leggibile.

## Deprecation policy

Una deprecazione può specificare:

- sostituto consigliato;
- data fine supporto;
- consumer noti;
- migration guide;
- read-only period;
- rimozione accesso;
- archival requirement;
- owner della chiusura.

Se nessuno è owner del retirement, la probabilità è che l'asset resti per sempre.

## Change failure rate per analytics

DORA avverte che fare deployment più spesso senza migliorare processi, architettura e pratiche tecniche può aumentare failure rate e burnout; la continuous delivery non è semplicemente “eseguire il vecchio processo più velocemente”.

Fonte: https://dora.dev/capabilities/continuous-delivery/

Lo stesso vale nell'analytics.

Automatizzare release senza:

- test;
- contract;
- preview;
- impact analysis;
- rollback;

rende semplicemente più veloce la produzione di breaking change.

Possiamo quindi monitorare:

- percentuale release con rollback/hotfix;
- incidenti causati da change;
- consumer breakage;
- tempo di recovery;
- breaking change senza notice;
- deprecation incomplete.

## Il Change Gate nell'Operating Contract

Per una modifica materiale:

```text
change proposed
→ classify risk
→ identify consumers
→ validate semantic impact
→ test
→ compare old/new
→ approve
→ communicate
→ deploy progressively if useful
→ monitor
→ rollback or certify
```

Questo processo deve essere leggero per T1 e più rigoroso per T3.

Il punto non è rallentare il cambiamento.

È **ridurre il costo delle sorprese**.

> **Un sistema analitico che scala non evita le breaking change. Fa in modo che una breaking change non venga scoperta retroattivamente da qualcuno che sta già prendendo una decisione.**
