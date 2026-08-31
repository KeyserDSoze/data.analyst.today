## 17.10 Finance e unit economics: quando crescere non significa migliorare
Le metriche aggregate di crescita possono nascondere un deterioramento economico.

Revenue, GMV, utenti o transazioni possono aumentare mentre il valore creato per unità peggiora.

Per questo l'analista deve spesso scendere dal totale al **unit economics**.

## Caso composito: NovaCompute

NovaCompute offre infrastruttura cloud a PMI europee.

Nel trimestre:

- revenue: +24%;
- clienti attivi: +31%;
- consumo compute: +42%.

Il board interpreta la crescita come segnale molto positivo.

Ma l'EBITDA margin scende dal 18% all'11%.

La prima spiegazione proposta è semplice:

> “Stiamo investendo per crescere.”

L'analista scompone invece l'economia per unità.

### Metriche costruite

Per cliente e workload calcola:

- revenue per compute hour;
- infrastructure cost per compute hour;
- support cost per cliente;
- gross margin per workload;
- cost-to-serve per segmento;
- contribution margin dopo incentivi commerciali.

Il risultato mostra che il nuovo segmento “AI batch workloads” cresce rapidamente, ma ha:

- sconti medi molto più alti;
- picchi di utilizzo su risorse costose;
- bassa prevedibilità;
- maggiore supporto tecnico;
- gross margin del 9%, contro il 38% del core business.

La crescita non è falsa.

È economicamente diversa.

## Dal totale alla funzione economica

Una metrica utile può essere:

`Contribution Margin per Workload = Revenue - Variable Infrastructure Cost - Variable Support Cost - Incentives`

Il punto non è trovare una formula universale.

È costruire una misura coerente con il modo in cui il business crea e consuma valore.

## Caso reale documentato: NXP e unit cost

AWS descrive come NXP Semiconductors abbia introdotto Cloud Intelligence Dashboards per ottenere visibilità più granulare sui costi dei workload, in particolare su attività HPC legate alla progettazione dei chip. Il caso riporta una riduzione del 75% dei costi di tooling FinOps e un aumento del 90% dell'efficienza FinOps; soprattutto, NXP usa l'analisi dei costi unitari di compute e storage per collegare consumo delle risorse e decisioni di allocazione.

Questo è un passaggio concettuale importante: il costo totale dice quanto spendiamo; il costo per unità aiuta a capire **perché** spendiamo e se la crescita è economicamente sana.

Fonte: AWS, *Analyzing unit costs using Cloud Intelligence Dashboards on AWS with NXP*.

## L'errore possibile: scegliere l'unità sbagliata

“Costo per cliente” può sembrare una buona metrica.

Ma se alcuni clienti fanno 100 transazioni al mese e altri 10 milioni, il denominatore nasconde la struttura reale del costo.

A seconda del business può essere più utile:

- costo per ordine;
- costo per transazione;
- costo per API call;
- costo per viaggio;
- costo per inference;
- costo per active seat;
- contribution margin per shipment.

L'unità deve riflettere il driver economico.

## La decisione

NovaCompute non decide di bloccare il segmento AI.

Decide di:

1. introdurre pricing legato ai picchi;
2. separare workload interruptible da premium;
3. limitare incentivi sui clienti con contribution margin negativo;
4. monitorare margin per cohort commerciale;
5. rivedere l'architettura per abbassare cost-to-serve.

## Metodo operativo

Quando crescita e profittabilità divergono:

1. riconciliare P&L e metriche operative;
2. identificare i driver variabili;
3. scegliere un'unità economicamente significativa;
4. segmentare per prodotto, cliente, canale e coorte;
5. distinguere costi di acquisizione, servizio e infrastruttura;
6. misurare il margine incrementale, non solo la revenue;
7. verificare se la crescita migliora o peggiora l'economia per unità.

> **Un business può crescere nei volumi e deteriorarsi nel valore. Il unit economics rende visibile questa differenza.**
