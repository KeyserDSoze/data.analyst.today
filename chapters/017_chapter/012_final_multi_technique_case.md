## 17.11 Caso finale: una decisione, molte tecniche
I problemi reali raramente arrivano etichettati come “regressione”, “A/B test”, “forecasting” o “causal inference”.

Arrivano così:

> “Perché stiamo perdendo margine e cosa dobbiamo fare?”

## Caso composito: OrbisMarket

OrbisMarket è un marketplace europeo con 9 milioni di ordini annui.

Nel Q3:

- GMV: +7%;
- net revenue: +4%;
- contribution margin: -13%;
- repeat purchase rate: -3,4 pp;
- delivery complaints: +22%.

Tre funzioni propongono tre spiegazioni:

- Marketing: “il problema è il mix di clienti acquisiti”;
- Operations: “il problema è la logistica”;
- Commercial: “i seller stanno alzando i prezzi”.

L'analista non sceglie una spiegazione. Costruisce una sequenza di verifiche.

## Step 1 — Data quality e semantica

Prima di interpretare il -13%:

- riconcilia contribution margin con Finance;
- controlla il grain ordine/riga/spedizione;
- verifica refund e cancellation timing;
- confronta event date e accounting date;
- controlla nuovi seller fee e carrier surcharge.

Scopre che circa 1,5 pp del calo apparente derivano da un cambio di timing nella contabilizzazione di alcuni rimborsi.

Il deterioramento resta reale, ma è più piccolo del primo alert.

## Step 2 — Decomposition

Il delta residuo viene scomposto in:

- product margin;
- discount;
- shipping subsidy;
- refunds;
- payment cost;
- customer support cost;
- seller incentives.

I driver principali sono shipping subsidy e refunds.

## Step 3 — Segmentation e cohort analysis

Il deterioramento è concentrato in:

- nuovi clienti acquisiti negli ultimi tre mesi;
- ordini bulky;
- due aree metropolitane;
- seller entrati dopo una recente espansione del catalogo.

Le coorti nuove hanno repeat rate più basso, ma anche livelli di servizio peggiori.

Quindi “qualità del marketing” e “logistica” non sono spiegazioni indipendenti.

## Step 4 — Funnel e behavioral analysis

Il funnel post-acquisto mostra:

ordine → spedizione → consegna → eventuale reclamo → secondo acquisto.

Il calo di retention è molto più forte tra clienti che ricevono la prima consegna oltre la promessa.

Ma questa correlazione non dimostra causalità: clienti, categorie e aree possono differire.

## Step 5 — Causal reasoning

Il team cerca variation utile.

Una modifica operativa è stata introdotta gradualmente solo in alcuni hub.

L'analista costruisce un confronto quasi-sperimentale tra hub simili prima e dopo il rollout, verificando trend pre-intervento e composizione.

L'evidenza suggerisce che il nuovo schema di consolidamento abbia aumentato il tempo di consegna di circa 0,8 giorni negli ordini bulky e ridotto il repeat purchase a 60 giorni di circa 2,1 pp nel segmento più esposto.

L'analista evita comunque una formulazione troppo forte: il design è utile ma non perfetto.

## Step 6 — Forecasting e capacità

Operations propone di aggiungere capacità ovunque.

Il forecast mostra però che i picchi sono concentrati in finestre e hub specifici.

Un aumento generalizzato di capacità costerebbe €6,8M annui.

Una combinazione di capacità flessibile, routing e soglie di volume ha costo atteso molto inferiore.

## Step 7 — Experimentation

Il team testa due interventi:

A. surcharge sugli ordini bulky sotto una certa soglia;
B. promise date più realistica + routing alternativo.

L'obiettivo primario non è semplicemente conversione checkout.

È contribution margin per visitatore, con guardrail su conversione, cancellazioni, delivery time e repeat purchase.

La variante B riduce leggermente la conversione iniziale ma migliora delivery reliability e margine atteso per cliente.

## Step 8 — Decision economics

Il team confronta tre opzioni:

| Opzione | Costo annuo stimato | Effetto atteso | Reversibilità |
|---|---:|---|---|
| Capacità fissa generalizzata | €6,8M | alta protezione picchi | bassa |
| Capacità flessibile + routing | €2,9M | effetto mirato | media-alta |
| Solo surcharge | €0,4M | protegge margine ma rischia conversione | alta |

La scelta finale combina routing/capacità flessibile con surcharge selettivo e promise date più realistica.

## Step 9 — Comunicazione

L'executive summary non dice:

> “La retention è calata per la logistica.”

Dice:

> “Dopo aver corretto un effetto contabile, il deterioramento del contribution margin è concentrato negli ordini bulky e nelle nuove coorti di due aree metropolitane. L'evidenza più forte collega una parte del problema al nuovo consolidamento logistico, che aumenta i ritardi nei segmenti più esposti. Un rollout mirato di routing alternativo e capacità flessibile ha miglior rapporto impatto/costo rispetto all'espansione generalizzata. Raccomandiamo rollout progressivo, con surcharge selettivo e monitoraggio di delivery reliability, contribution margin e repeat purchase.”

## Step 10 — Misurazione dopo la decisione

Dopo otto settimane:

- on-time delivery: +6,7 pp;
- contribution margin bulky: +3,2 pp;
- support contacts: -11%;
- repeat purchase nel segmento target: +1,5 pp;
- conversion checkout: -0,3 pp.

La decisione non ha ottimizzato ogni metrica.

Ha migliorato il sistema complessivo.

## Cosa abbiamo usato davvero?

Nel caso sono entrati:

- data quality;
- SQL e semantic reasoning;
- decomposition;
- segmentation;
- cohorts;
- funnel;
- causal inference;
- forecasting;
- experimentation;
- unit economics;
- decision analysis;
- storytelling.

Nessuna tecnica era “il capitolo giusto”.

Il problema ha richiesto una catena.

> **La maturità analitica appare quando smettiamo di chiedere quale tecnica usare e iniziamo a chiedere quale sequenza di evidenze serve per prendere una decisione migliore.**
