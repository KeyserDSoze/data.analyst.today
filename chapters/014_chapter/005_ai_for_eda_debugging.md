# 14.4 AI per EDA e debugging: un moltiplicatore di domande, non un sostituto dell'indagine

L'AI può essere molto utile nell'Exploratory Data Analysis perché riduce il costo di formulare, implementare e testare rapidamente nuove domande.

Può suggerire:

- distribuzioni da controllare;
- segmentazioni;
- anomalie;
- feature derivate;
- grafici;
- controlli sui missing;
- possibili cause di un errore di pipeline;
- query diagnostiche.

Il punto però non è farle "analizzare il dataset al posto nostro". Il punto è usare l'AI per aumentare il numero e la qualità delle verifiche che riusciamo a fare.

## Caso realistico: conversion crollata su Android

Una travel app osserva conversion dal 4,7% al 3,9% in due giorni.

L'analista chiede all'AI di proporre un piano EDA.

L'assistente suggerisce:

1. breakdown per OS;
2. versione app;
3. paese;
4. payment method;
5. funnel step;
6. error code;
7. confronto con rollout recenti.

I dati mostrano:

- iOS stabile;
- Android -21%;
- Android 14 molto peggio delle altre versioni;
- drop concentrato tra `payment_started` e `payment_success`;
- error code `WALLET_TOKEN_EXPIRED` quadruplicato.

L'AI non ha "scoperto" la causa da sola. Ha aiutato a strutturare rapidamente lo spazio di ricerca.

Il team mobile conferma un bug introdotto in una release del wallet SDK.

## La tecnica delle domande avversarie

Dopo una prima interpretazione, chiediamo all'AI di provare a smentirla.

Prompt:

> "La mia ipotesi è che il calo di conversion sia dovuto al nuovo SDK Android. Proponi almeno cinque spiegazioni alternative che produrrebbero un pattern simile e indica quale controllo dati distinguerebbe ogni ipotesi."

Possibili alternative:

- tracking rotto soltanto su Android;
- mix geografico cambiato;
- campagna paid acquisisce traffico peggiore;
- PSP specifico in outage;
- versione Android correlata con un mercato problematico.

Questa modalità è utile perché combatte confirmation bias sia umano sia generato dalla narrazione del modello.

## AI come debugger di pipeline

Supponiamo che una tabella giornaliera abbia il 17% di righe in meno.

Invece di chiedere:

> "Perché mancano dati?"

possiamo fornire:

- DAG della pipeline;
- row count per stage;
- timestamp;
- schema change recente;
- log degli errori;
- query di controllo.

E chiedere:

> "Costruisci una diagnosi per esclusione. Ordina le ipotesi per compatibilità con i sintomi e proponi il test più economico per falsificarle."

Questa formulazione spinge verso una procedura più scientifica.

## Caso realistico: il 17% di ordini "spariti"

Un data mart retail passa da 2,8 milioni a 2,32 milioni di order lines.

L'AI propone tre aree:

- ingestion incompleta;
- join che perde righe;
- filtro temporale.

I controlli mostrano:

- raw ingestion completa;
- Silver completa;
- perdita tra Silver e Gold;
- nuovo `INNER JOIN` con product master;
- 480.000 righe hanno nuovi SKU non ancora caricati nel master.

Il problema è quindi un join referenziale, non un source outage.

L'AI ha accelerato il debugging perché ha trasformato un sintomo generico in test sequenziali.

## EDA con AI: cosa non fare

È rischioso chiedere:

> "Analizza questo dataset e dimmi gli insight più importanti."

senza specificare:

- obiettivo;
- unità di analisi;
- contesto business;
- significato delle variabili;
- periodo;
- qualità del dato.

Il risultato sarà spesso una raccolta di pattern statisticamente veri ma business-wise irrilevanti.

## Il ruolo dell'analista: scegliere quali domande meritano costo

Con l'AI possiamo generare cento segmentazioni in pochi minuti. Questo crea un problema nuovo: **l'abbondanza di analisi può aumentare i falsi pattern**.

Più esploriamo, più è probabile trovare qualcosa che sembra interessante per caso.

Per questo dobbiamo mantenere:

- ipotesi prioritarie;
- correzione o cautela sul multiple testing;
- distinzione tra EDA e conferma;
- validazione su dati successivi o indipendenti.

> **L'AI aumenta la velocità con cui possiamo trovare pattern. Non aumenta automaticamente la probabilità che quei pattern siano veri, stabili o utili.**
