## 18.6 Automazione e CI/CD: incorporare il controllo, non automatizzare la speranza

Quando un'analisi diventa ricorrente, la domanda non è più soltanto “funziona oggi?”, ma **come possiamo cambiarla decine o centinaia di volte senza perdere il diritto di fidarci del risultato?** È qui che pratiche di software engineering come version control, review, test automatici, ambienti separati, release e rollback diventano rilevanti per analytics.

Non perché un data team debba imitare DevOps per moda. Perché una modifica SQL, una configurazione o un semantic change possono alterare una decisione senza produrre un errore tecnico evidente.

DORA definisce continuous delivery come la capacità di rilasciare rapidamente e in modo sicuro e sostenibile e avverte che fare deployment più spesso senza migliorare processo, architettura e capability tende ad aumentare failure e burnout.

Fonte: https://dora.dev/capabilities/continuous-delivery/

La traduzione per analytics è semplice: **prima si rende esplicito il controllo, poi lo si automatizza**.

## Il controllo manuale che non doveva essere rimosso

Immaginiamo un processo settimanale: export, mapping, formula, controllo con Finance, pubblicazione. Automatizziamo export, mapping e formula; poi eliminiamo la reconciliation perché “ora la pipeline è automatica”. Abbiamo aumentato velocità riducendo il solo gate che confrontava l'output con una fonte indipendente.

La sequenza corretta è diversa:

```text
understand recurring work
→ remove unnecessary steps
→ make semantics explicit
→ define tests + ownership
→ automate
→ observe
→ improve
```

Schedulare lo script non trasforma un processo in prodotto. Lo rende soltanto ricorrente.

## Il KPI che cambia senza rompersi

Una società SaaS usa `active_customer` nel denominatore dell'executive retention. Un analytics engineer esclude gli account in grace period. La query compila, gira, non produce null e mantiene schema e tipo. Il KPI passa da `108,4%` a `104,9%`.

Il sistema tecnico è sano. Il cambiamento è decision-critical.

Una delivery chain che controlla solo syntax e schema non protegge il consumer. Per un prodotto T2 serve una sequenza più vicina a:

```text
proposed change
→ static / structural checks
→ logic + contract tests
→ reconciliation
→ semantic diff
→ consumer impact analysis
→ approval at the right ownership level
→ shadow / pre-production run
→ deploy
→ post-deploy verification
→ certification
```

Non tutti gli asset richiedono tutti i gate. Il criticality tier decide profondità e costo del processo.

## Semantic diff: il test che rende visibile il giudizio necessario

Uno dei controlli più potenti prima di una release è confrontare vecchio e nuovo output. Non chiediamo soltanto se “i test passano”, ma quali righe e metriche cambiano, di quanto, in quali segmenti, se il delta è atteso e se attraversa una soglia decisionale.

| Metrica | Old | New | Delta | Atteso? |
|---|---:|---:|---:|---|
| Active customers | 184.320 | 176.940 | -4,0% | sì |
| NRR | 108,4% | 104,9% | -3,5 pp | sì, effetto denominatore |
| Churn rate | 2,8% | 2,9% | +0,1 pp | da investigare |

Il semantic diff non decide se la modifica sia corretta. Dice **dove il giudizio umano è ancora necessario**. È esattamente il tipo di controllo che l'automazione deve preparare, non sostituire.

## Development, validation e production separano esperimento e promessa

Un asset esplorativo deve poter cambiare rapidamente. Un asset certificato non dovrebbe essere modificato direttamente nella superficie che alimenta decisioni business-critical. La separazione può essere fisica o logica, ma i ruoli sono chiari: development consente di costruire e rompere; validation usa dati rappresentativi, contract e metric diff; production contiene soltanto versioni che hanno superato i gate richiesti dal tier.

Microsoft, nei maturity level della Fabric Adoption Roadmap, associa contenuti più essenziali al decision making a separazione più forte tra sviluppo/test e produzione, supporto definito e change management controllato.

Fonte: https://learn.microsoft.com/en-us/power-bi/guidance/fabric-adoption-roadmap-maturity-levels

## Shadow run, dual run e rollout progressivo

Una breaking change non deve necessariamente apparire a tutti nello stesso istante. Vecchio e nuovo prodotto possono convivere temporaneamente per quantificare delta, aggiornare threshold e verificare casi limite. `revenue_v1` e `revenue_v2` per due closing cycle non sono duplicazione permanente: sono **observability del cambiamento**.

Lo stesso principio abilita rollout progressivi: semantic model a un gruppo pilota, API versionata, dual-read per alcuni consumer, canary su una regione o nuova metrica visibile inizialmente soltanto a Finance e Analytics. Più grande il blast radius, maggiore il valore di una fase limitata.

## Rollback nei dati: il codice può tornare indietro, la decisione no

Nel software rollback spesso significa ripristinare una versione. Nei dati dobbiamo distinguere almeno tre cose. Il **code rollback** può riportare la logica precedente. Il **data replay/backfill** può ricostruire output già scritti. Ma il **consumer impact** può essere irreversibile: un report è stato esportato, una comunicazione inviata, una decisione presa.

Per questo il recovery plan deve includere cache, snapshot, backfill, consumer notification e re-certification. Riparare la tabella non annulla automaticamente ciò che è già accaduto downstream.

## Configuration is code quando la configurazione decide il numero

Molti incidenti non nascono dal SQL ma da mapping territoriali, liste di esclusione, threshold, currency rate source, calendar o business-day definition. Se un file CSV può modificare un KPI materiale, non è “solo configurazione”: deve avere owner, versioning, review proporzionata e traceability.

Questo completa il senso della CI: dobbiamo versionare tutto ciò che può cambiare la promessa, non soltanto il codice che gli ingegneri riconoscono come software.

## Prima, durante e dopo il deploy

Una delivery chain affidabile combina test prima del release, controllo durante il rollout e osservazione dopo. Il post-deploy check deve confermare freshness, plausibilità, reconciliation, superficie consumer e SLO. Una CI perfetta con un deployment manuale fragile è incompleta; un deployment automatico che pubblica output senza consumer impact check lo è altrettanto.

Possiamo monitorare deployment frequency, lead time change→production, change fail rate, hotfix, incident causati da release, tempo di certification e toil residuo. La velocità è utile soltanto se non compra throughput sacrificando reliability.

Il criticality tier rimane la regola di proporzione. T0 può vivere con version control consigliato. T1 aggiunge review e test base. T2 richiede semantic diff, reconciliation, change classification, rollback/fallback e post-deploy verification. T3 può richiedere segregazione, audit, independent verification e recovery testato.

> **Automazione non significa eliminare il controllo umano o tecnico. Significa spostare i controlli ripetibili dal ricordo delle persone alla pipeline, lasciando al giudizio umano le modifiche di significato e rischio che una regola non può approvare da sola.**

Per sapere quali controlli automatizzare, però, serve una domanda più precisa: quali failure mode vogliamo impedire che attraversino indisturbati la delivery chain? È il compito della testing strategy.