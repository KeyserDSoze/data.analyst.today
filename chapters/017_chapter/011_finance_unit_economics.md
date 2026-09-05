## 17.10 NovaCompute — “Stiamo crescendo: perché il margine peggiora?”

> **Caso simulato/composito.** Organizzazione, numeri e sequenza sono costruiti per la didattica.

NovaCompute offre infrastruttura cloud a PMI europee. Nel trimestre revenue cresce del **24%**, i clienti attivi del **31%** e il consumo compute del **42%**, mentre l'EBITDA margin scende dal **18% all'11%**. Il board propone una lettura rassicurante: “stiamo investendo per crescere”. Il CFO fa una domanda più utile:

> **La nuova crescita sta costruendo valore o sta scalando un'economia peggiorativa?**

Il failure cost è evidente: accelerare un segmento con contribution economics strutturalmente deboli può trasformare la crescita in un moltiplicatore di perdita. Ma la risposta non richiede subito prediction o causal inference. Richiede prima un **denominatore economico difendibile**.

La stop rule è quindi: **non accelerare il nuovo segmento sulla sola revenue growth finché cost boundary e unit economics non riconciliano con Finance**.

### Il primo problema è decidere che cosa appartiene al costo dell'unità

Il team riconcilia revenue riconosciuta, crediti promozionali, infrastructure cost, support cost, partner fee, incentivi commerciali, shared cost e periodizzazione. L'Analytical Data Contract specifica quali componenti entrano nel contribution margin usato per la decisione e come i costi condivisi vengono allocati.

Questa fase è più importante di qualsiasi modello. Due team possono mostrare lo stesso “margin per workload” e includere costi diversi; una policy costruita su metriche con boundary differenti non è confrontabile.

Anche il denominatore richiede una scelta. “Costo per cliente” è naturale ma mescola account che eseguono poche centinaia di job al mese con altri che ne eseguono milioni. NovaCompute costruisce quindi più viste coordinate: revenue e infrastructure cost per compute hour, support cost e contribution margin per workload, margin per cliente/coorte commerciale e costo delle unità di picco dove la capacità premium è il vero driver.

La formula di riferimento del caso è:

```text
Contribution Margin per Workload
= Revenue
- Variable Infrastructure Cost
- Variable Support Cost
- Incentives
```

Non è una definizione universale. È il contratto con cui **questo business** decide quale attività crea o consuma valore.

AWS Cloud Intelligence Dashboards offre un esempio documentato del principio generale, senza bisogno di attribuire risultati a una singola azienda: la documentazione corrente descrive chargeback/showback, cost allocation e **unit metrics** come il costo medio orario di EC2; le guide SaaS mostrano inoltre come costruire metriche come cost per API call. L'utilità non sta nella dashboard in sé, ma nel collegare spend e usage a un'unità operativa interpretabile.[^aws-cid][^aws-unit]

### Il mix rivela che non tutta la crescita vale allo stesso modo

Il nuovo segmento `AI batch workloads` cresce molto più rapidamente del core, ma ha sconti medi superiori, picchi su risorse costose, bassa prevedibilità e maggiore support intensity. Il gross margin è circa **9%**, contro **38%** del core business.

Il +24% di revenue rimane vero. È però economicamente eterogeneo.

La decomposition separa volume, mix verso AI batch, sconti, mix di compute resource, utilization inefficiente, support intensity e costo unitario infrastrutturale. Questo rende possibile distinguere due fenomeni che l'EBITDA aggregato comprimeva insieme.

Una parte dei costi può essere un investimento transitorio: onboarding, engineering e supporto iniziale che si riducono con scala o apprendimento. Un'altra parte può essere **unit economics strutturalmente debole**: ogni nuova unità aggiunge revenue ma porta con sé abbastanza costo variabile da diluire il valore.

Nel caso NovaCompute esistono entrambe. La seconda è abbastanza materiale da impedire la decisione “continuiamo così perché stiamo crescendo”.

### Non serve sapere causalmente dove finisce ogni euro per correggere un boundary sbagliato

Gli unit economics possono a loro volta mentire se gli shared cost sono allocati arbitrariamente, il denominator è manipolabile, le unità differiscono per quality of service, alcuni costi sono differiti o un segmento scarica spese su un altro team. Per questo definition owner, grain, frequency, shared-cost rule, P&L reconciliation e versioning sono parte del KPI.

Ma una volta che il boundary è riconciliato, non serve attribuire causalmente ogni euro di infrastruttura prima di prendere la prima decisione. Il problema decisionale è già chiaro: il segmento AI non va né accelerato indiscriminatamente né chiuso prima di testare se pricing e cost-to-serve possono essere corretti.

Le alternative sono quindi tre. Continuare senza modifiche massimizza top-line ma rischia di scalare margin dilution. Chiudere il segmento protegge il margine nel breve e può distruggere un'opportunità strategica. La policy preferita è **economicamente differenziata**: pricing legato a picchi e workload type, distinzione interruptible/premium, limiti agli incentivi per account con contribution margin persistentemente negativo, margin review per coorte e redesign tecnico dove esiste un chiaro cost-to-serve driver.

Il Decision Record include anche un periodo di apprendimento e una soglia oltre la quale un workload rimasto sotto target richiede escalation o ridimensionamento.

La strategia cambia se cost-to-serve scende abbastanza con la scala, willingness-to-pay non sostiene il repricing, cambia il workload mix, utilization migliora, support cost resta alto oltre la fase iniziale o una nuova architettura modifica materialmente il costo unitario.

### Evidence Ledger

| Observed | Inferred | Still unknown |
|---|---|---|
| revenue +24%, compute +42%, EBITDA margin 18→11% | crescita e creazione di valore stanno divergendo | quanto del support/cost premium scenderà con scala |
| AI batch gross margin ~9% vs core 38% | pricing/cost-to-serve sono leve più mirate della chiusura | willingness-to-pay dopo repricing |
| sconti, picchi costosi e support intensity più alti | parte del deterioramento è strutturale, non solo investimento upfront | beneficio del redesign architetturale |

La headline executive può quindi dire:

> **La crescita è reale ma il mix è economicamente più debole: AI batch cresce più velocemente del core e porta gross margin molto inferiore per sconti, picchi costosi e support intensity. Non raccomandiamo di chiuderlo; proponiamo pricing e cost-to-serve differenziati con soglie economiche esplicite.**

L'outcome review segue contribution margin per workload, revenue/infrastructure cost per compute hour, support cost, utilization, incentive payback, retention e crescita assoluta del contribution profit. Un segmento può ridurre la margin percentage e aumentare profitto assoluto in modo attraente; anche la review deve quindi rispettare la funzione obiettivo originale.

**Percorso effettivo:** Analytical Data Contract → Data Readiness Review → EDA Evidence Map → Decision Record → Decision Communication Pack. Tooling Decision Record o Data Flow Architecture Map entrano soltanto se il redesign cost-to-serve diventa davvero un progetto infrastrutturale.

> **Unit economics non è dividere il costo totale per un numero comodo. È scegliere un'unità e un cost boundary che permettano di vedere se la crescita sta moltiplicando valore o soltanto attività.**

[^aws-cid]: AWS, *CUDOS, CID, KPI — Cloud Intelligence Dashboards on AWS*, https://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/cudos-cid-kpi.html
[^aws-unit]: AWS, *SaaS Unit Metrics — Cloud Intelligence Dashboards on AWS*, https://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/saas-unit-metrics.html
