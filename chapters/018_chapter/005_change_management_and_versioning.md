## 18.4 Change management: schema stabile non significa significato stabile

Un prodotto analitico che scala deve poter cambiare senza costringere i consumer a scoprire **dopo** una decisione che il numero significava qualcosa di diverso. Il problema non è evitare il cambiamento: sorgenti, organizzazioni, policy, metriche e piattaforme cambieranno comunque. Il problema è rendere il cambiamento riconoscibile, classificabile e reversibile quanto basta al failure cost.

Questa sezione nasce direttamente dal self-service. Un consumer può usare un prodotto in autonomia solo se sa quali parti della promessa sono stabili e come viene comunicata un'incompatibilità. Per questo una breaking change non è soltanto quella che rompe una query. È breaking ogni modifica che può cambiare l'interpretazione o una decisione senza che il consumer l'abbia accettata.

## Quattro famiglie di change

Un **technical change** — engine SQL, orchestratore, refactoring, storage o ottimizzazione — può lasciare invariato l'output. Uno **structural change** modifica colonna, tipo, chiave o schema ed è spesso intercettabile da contract e test. Un **semantic change** modifica ciò che il dato rappresenta: `active_customer` passa da 90 a 60 giorni, `completed` cambia significato, revenue passa da gross a net, il denominatore di conversione include una nuova popolazione. Un **operating change** modifica refresh, SLO, owner, supporto, fonte provisional o criticality del prodotto.

Le ultime due categorie sono le più pericolose proprio perché il codice può continuare a funzionare. Un sistema analitico maturo deve quindi versionare non soltanto schema e transformation code, ma la **decision boundary** che il prodotto promette di mantenere.

## Schema verde, revenue sbagliata

Un marketplace riceve `order_status` dal sistema ordini. Per anni `completed` significa `pagamento acquisito + ordine consegnato`. Dopo una migrazione, senza cambiare nome o tipo della colonna, `completed` diventa `pagamento autorizzato`.

Schema test, not-null e accepted-values passano. Downstream, però, revenue viene anticipata, cancellation rate scende artificialmente e le metriche di delivery diventano incoerenti. Finance smette di riconciliare.

Non abbiamo un bug di struttura. Abbiamo un **semantic breaking change**. Il controllo decisivo non era “il valore `completed` esiste ancora?”, ma “il consumer può continuare ad assumere che `completed` rappresenti lo stesso stato del processo?”.

Questo esempio definisce il **Compatibility Contract** per i prodotti T2/T3. Non promette immobilità; promette che primary key, grain, required fields, semantic meaning, metric definitions, freshness class, history policy e interfacce supportate non cambieranno in modo incompatibile senza una procedura riconoscibile.

## Versionare ciò che può cambiare una decisione

Un prodotto critico dovrebbe permettere di ricostruire transformation code, metric definition, schema, mapping/configuration, test, documentazione e Operating Contract in vigore quando un numero è stato prodotto. Non serve aggiungere `_v2` a ogni tabella. La versione può vivere in catalogo, metadata o semantic layer. Serve però poter rispondere alla domanda:

> **Quale logica e quale significato erano in vigore quando questa decisione è stata presa?**

Questo vale anche per configuration data apparentemente innocui: mapping territoriali, liste di esclusione, threshold, calendar, currency source e business-day definition possono cambiare un KPI quanto una query SQL. Se una configurazione cambia il significato, ha bisogno di owner e traceability.

## Backfill: il passato non si riscrive per default

Quando cambia la semantica, la strategia storica è parte del change design. Un **full backfill** ricalcola il passato con la nuova logica: utile per la comparabilità, ma rischia di far sembrare che decisioni passate siano state prese su numeri che allora non esistevano. Un approccio **forward-only** mantiene la discontinuità quando il business è davvero cambiato o il passato non è ricostruibile. Un **dual reporting** fa convivere vecchia e nuova versione per misurare l'impatto, aggiornare threshold e preparare i consumer.

Non esiste una scelta sempre migliore. L'errore è lasciare che il comportamento storico emerga accidentalmente dall'implementazione.

## Il change process deve seguire il rischio

Una correzione documentale o una nuova colonna opzionale può avere review leggera. Una nuova dimensione o una modifica di performance che influenza latency può richiedere test e consumer awareness. Un cambio di grain, key, denominator, business definition, history policy o freshness commitment deve invece attivare impact analysis, owner appropriati, migration plan, notice, fallback e strategy di versioning.

Microsoft tratta il change management nella Fabric Adoption Roadmap come una disciplina che protegge persone e processi dalla disruption, non come un'attività di puro deployment. La guida raccomanda di descrivere il prima/dopo, stimare l'impatto, procedere per incrementi gestibili e costruire action plan che includano rollback quando possibile.

Fonte: https://learn.microsoft.com/en-us/power-bi/guidance/fabric-adoption-roadmap-change-management

Questo è particolarmente importante nell'analytics perché una metrica non vive soltanto in una tabella. Vive in dashboard, alert, target, forecast baseline, incentivi, modelli e meeting. Cambiarne il significato genera anche **semantic threshold debt**: un target o un semaforo costruito sul vecchio denominatore può diventare sbagliato anche se la nuova metrica è corretta.

## Consumer impact: lineage è necessario ma non sufficiente

Prima di una breaking change dobbiamo sapere quali dashboard, query, job, modelli ML, agenti AI, export, alert e processi manuali dipendono dal prodotto. Il lineage tecnico aiuta, ma non vede sempre file locali, snapshot esportate o dipendenze non registrate. Per prodotti critici può servire un consumer registry o almeno una subscription alle change notice.

Una notice operativa dovrebbe dire:

```text
what changes
why
effective date
old vs new meaning
expected numerical impact
history / backfill policy
assets affected
migration action required
owner / support
rollback / fallback
```

“Da lunedì aggiorniamo il modello dati” non è change management. È una comunicazione che scarica il lavoro interpretativo sul consumer.

## Deprecation: cambiare significa anche chiudere

La stessa disciplina serve a fine vita. `dashboard_final`, `dashboard_final_v2`, `revenue_old` e `customer_new` non sono soltanto disordine estetico: aumentano la probabilità che un analyst o un agente AI scelga un asset non più supportato. Per questo gli asset dovrebbero poter avere stati leggibili come:

```text
EXPERIMENTAL
→ SUPPORTED
→ CERTIFIED
→ DEPRECATED
→ RETIRED
```

Una deprecation policy definisce sostituto, end-of-support, consumer noti, migration guide, read-only period, archival requirement e owner della chiusura. Se nessuno possiede il retirement, il portfolio cresce senza limite.

## Delivery più veloce non compensa un change process debole

DORA definisce continuous delivery come la capacità di rilasciare rapidamente e con basso rischio e avverte esplicitamente che aumentare la frequenza senza redesign di processo e architettura può aumentare failure rate e burnout.

Fonte: https://dora.dev/capabilities/continuous-delivery/

Per analytics la conseguenza è diretta: release automation senza contract, test, semantic diff, impact analysis e rollback rende semplicemente più veloce la produzione di breaking change. Per questo possiamo osservare anche change fail rate, hotfix, incidenti causati da release, consumer breakage e deprecation incomplete.

Un **Change Gate** T2/T3 può restare semplice nella forma:

```text
change proposed
→ classify risk
→ identify consumers
→ validate semantic impact
→ test + old/new comparison
→ approve at the right ownership level
→ communicate
→ deploy progressively if useful
→ monitor
→ rollback or certify
```

Il processo deve essere più leggero per T1 e più rigoroso per T3. Il suo scopo non è rallentare il cambiamento: è ridurre il costo delle sorprese.

> **Un sistema analitico che scala non evita le breaking change. Fa in modo che una breaking change non venga scoperta retroattivamente da qualcuno che sta già usando il numero per decidere.**

Quando change, ownership e reliability sono espliciti, possiamo finalmente distribuire la responsabilità organizzativa senza distribuire anche l'ambiguità.