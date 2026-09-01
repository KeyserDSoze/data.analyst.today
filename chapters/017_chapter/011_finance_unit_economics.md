## 17.10 “Stiamo crescendo: perché il margine peggiora?”

### Caso simulato/composito: NovaCompute

NovaCompute offre infrastruttura cloud a PMI europee.

Nel trimestre:

- revenue: `+24%`;
- clienti attivi: `+31%`;
- consumo compute: `+42%`;
- EBITDA margin: `18% → 11%`.

Il board vede la crescita e propone una spiegazione rassicurante:

> “Stiamo investendo per crescere.”

Può essere vero.

Ma prima di accettare questa storia il CFO chiede:

> **“La nuova crescita sta costruendo valore o sta scalando un'economia peggiorativa?”**

## Routing iniziale

| Elemento | Scelta |
|---|---|
| Decisione | continuare a spingere il nuovo segmento, repricing o redesign cost-to-serve |
| Failure cost | scalare rapidamente workload a contribution margin troppo basso |
| Claim necessario | economico/diagnostico; causalità solo per interventi specifici |
| Reversibilità | media: pricing e incentivi si cambiano, contratti e capacità già venduta meno |
| Incertezza critica | allocazione dei costi e denominatore economico |
| Stop rule | non accelerare il segmento sulla sola revenue growth finché l'economia per unità non è riconciliata |

## 1. Crescita aggregata e creazione di valore sono cose diverse

Revenue, GMV, utenti o transazioni possono aumentare mentre il valore creato da ogni unità peggiora.

Questo accade quando il mix si sposta verso attività con:

- margine inferiore;
- costo di servizio superiore;
- incentivi più alti;
- maggiore volatilità;
- maggiore consumo di capitale o capacità.

Per capire NovaCompute dobbiamo quindi scendere dal totale al **driver economico**.

## 2. Prima riconciliare Finance e operations

Il team non parte dal dashboard cloud.

Riconcilia:

- revenue riconosciuta;
- crediti promozionali;
- infrastructure cost;
- support cost;
- partner fee;
- incentivi commerciali;
- costi shared allocati;
- periodizzazione.

L'obiettivo è costruire un **Analytical Data Contract** che definisca cosa entra e cosa non entra nel contribution margin operativo usato per la decisione.

Senza questa riconciliazione, due team potrebbero dire “margin per workload” intendendo costi diversi.

## 3. Scegliere l'unità economica giusta

“Costo per cliente” sembra naturale.

Ma alcuni clienti eseguono poche centinaia di job al mese e altri milioni.

Il denominatore cliente mescola economie molto diverse.

NovaCompute costruisce quindi più unità:

- revenue per compute hour;
- infrastructure cost per compute hour;
- support cost per workload;
- contribution margin per workload;
- margin per cliente/coorte commerciale;
- cost per unità di picco dove la capacità premium è il driver.

La formula di riferimento è:

`Contribution Margin per Workload = Revenue - Variable Infrastructure Cost - Variable Support Cost - Incentives`

Non è una formula universale.

È una rappresentazione del modo in cui **questo business** crea e consuma valore.

## 4. Il mix che cambia la storia

Il nuovo segmento `AI batch workloads` cresce molto rapidamente.

Ma presenta:

- sconti medi più alti;
- picchi di utilizzo su risorse costose;
- bassa prevedibilità;
- maggiore supporto tecnico;
- gross margin circa `9%`, contro `38%` del core business.

Il +24% di revenue non è falso.

È economicamente eterogeneo.

La nuova crescita pesa molto più sui costi variabili e sul supporto di quanto il totale faccia vedere.

## 5. Decomposition: volume, prezzo, mix, cost-to-serve

Il team decompone il deterioramento del margine in:

- più volume;
- mix verso AI batch;
- sconti;
- mix di risorse compute;
- utilization inefficiente;
- support intensity;
- costo unitario infrastrutturale.

Questo permette di distinguere due storie:

### “Stiamo investendo”

Costi temporanei o upfront che dovrebbero ridursi con scala/apprendimento.

### “Stiamo scalando un'unità debole”

Economia variabile strutturalmente povera che peggiora proprio aumentando il volume.

Nel caso NovaCompute esistono entrambe, ma la seconda spiega una quota materialmente importante.

## Caso reale documentato: NXP e unit-cost analysis

AWS documenta come **NXP Semiconductors** abbia implementato Cloud Intelligence Dashboards per ottenere maggiore visibilità su costi e utilizzo cloud, inclusi workload HPC legati alla progettazione dei chip. Il case study riporta una riduzione del 75% dei costi di tooling FinOps e un aumento del 90% dell'efficienza FinOps; soprattutto, descrive l'uso di unit-cost analysis su compute e storage per individuare inefficienze e supportare decisioni di allocazione.

Fonte: https://aws.amazon.com/solutions/case-studies/npx-cid/

Il punto didattico non è che una dashboard produca automaticamente risparmio.

È che il costo totale risponde a:

> “quanto spendiamo?”

mentre un unit cost ben scelto aiuta a rispondere:

> **“quale attività sta generando quella spesa e con quale economia?”**

## 6. L'errore possibile: unit economics senza boundary

Anche il costo per unità può mentire se:

- i shared cost vengono allocati arbitrariamente;
- il denominatore è manipolabile;
- le unità non sono comparabili per qualità/servizio;
- i costi differiti vengono esclusi;
- un segmento scarica costi su un altro team.

Per questo la metrica deve avere:

- definition owner;
- cost boundary;
- grain;
- frequency;
- reconciliation con P&L;
- regola per shared cost;
- versione.

Questo trasforma il KPI in un oggetto governato, non in una formula locale.

## 7. Decision Record

NovaCompute confronta:

### A — Continuare la crescita senza modifiche

Massimizza top-line ma rischia di scalare margin dilution.

### B — Chiudere il segmento AI

Protegge margine nel breve ma può distruggere un'opportunità strategica prima di correggere pricing/cost-to-serve.

### C — Rendere economicamente differenziata la policy

1. pricing legato ai picchi e al tipo di workload;
2. separazione tra interruptible e premium;
3. limite agli incentivi sui clienti con contribution margin negativo persistente;
4. margin review per coorte commerciale;
5. redesign architetturale per abbassare cost-to-serve;
6. threshold di escalation per workload che restano sotto target dopo il periodo di apprendimento.

La scelta è C.

## 8. Switching condition

La strategia cambia se:

- cost-to-serve diminuisce abbastanza da rendere il segmento competitivo;
- willingness-to-pay risulta insufficiente;
- il workload mix cambia;
- l'utilization migliora con scala;
- il support cost non scende dopo la fase iniziale;
- una nuova architettura modifica materialmente il costo unitario.

Il Decision Record registra queste condizioni prima che il board giudichi la scelta soltanto dal risultato trimestrale.

## 9. Decision Communication Pack

La headline non è:

> “EBITDA margin -7 punti.”

È:

> **“La crescita è reale ma il mix è economicamente più debole: il segmento AI batch cresce più velocemente del core e porta gross margin molto inferiore per sconti, picchi costosi e support intensity. Non raccomandiamo di chiuderlo; proponiamo pricing e cost-to-serve differenziati con soglie economiche esplicite.”**

Il pack mostra:

1. revenue growth vs contribution growth;
2. margin bridge;
3. unit economics per workload;
4. scenario dopo repricing/cost reduction;
5. threshold che decide continuazione o ridimensionamento.

## 10. Outcome review

Metriche:

- contribution margin per workload;
- revenue per compute hour;
- infrastructure cost per compute hour;
- support cost;
- utilization;
- incentive payback;
- retention del segmento;
- crescita assoluta del contribution profit.

La metrica finale non deve essere soltanto “margin % è salito?”.

Un segmento può ridurre la percentuale di margine ma aumentare profitto assoluto in modo economicamente attraente. Anche qui serve capire la funzione obiettivo.

## Cosa abbiamo scelto di non fare

Non serve un modello predittivo complesso per riconoscere un deterioramento di unit economics.

Non serve attribuire causalmente ogni euro di infrastruttura prima di correggere pricing evidentemente disallineato.

La catena è:

**Analytical Data Contract → Data Readiness Review → EDA Evidence Map → Decision Record → Decision Communication Pack**

con Tooling Decision Record o Data Flow Architecture Map soltanto se la soluzione richiede cambiare davvero infrastruttura, non per completare una checklist.

> **Un business può crescere nei volumi e deteriorarsi nel valore. Il unit economics rende visibile la differenza soltanto se l'unità e il boundary economico sono quelli giusti.**
