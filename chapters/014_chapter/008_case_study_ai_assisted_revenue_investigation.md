## 14.7 Case study — Un'indagine revenue con AI: più veloce, ma soltanto dopo aver costruito i controlli
Questa storia è simulata ma costruita per riflettere un workflow realistico in un'azienda digitale.

## Il contesto

Aurelia Travel gestisce una piattaforma di prenotazione in 11 mercati europei.

Il lunedì mattina il CFO riceve un alert:

- net revenue settimana corrente: €18,7M;
- settimana precedente: €20,4M;
- variazione: -8,3%.

Il CEO chiede una risposta entro due ore.

L'analyst apre il copilota interno collegato al semantic layer e scrive:

> "Spiegami il calo di net revenue dell'ultima settimana rispetto alla precedente e identifica i tre driver principali."

L'AI restituisce in meno di un minuto:

1. Francia: -€720k;
2. hotel urban: -€510k;
3. mobile app: -€430k.

Conclusione proposta:

> "Il calo è principalmente dovuto a una riduzione della domanda mobile in Francia, soprattutto sugli hotel urbani."

La risposta è veloce, coerente e quasi completamente sbagliata.

## Step 1 — Verificare prima il numero headline

L'analista non parte dai driver. Parte dalla metrica.

Chiede:

> "Mostrami esattamente quale misura, date field, filtri e tabelle hai usato per calcolare net revenue."

Scopre che il copilota ha usato una misura `Revenue` presente nel modello ma non certificata, che rappresenta gross booking value al netto delle sole cancellazioni immediate.

La misura ufficiale finance è `Net_Revenue_Final`, che include commissioni, refund e adjustment tardivi.

Valore corretto:

- settimana corrente: €19,35M;
- precedente: €20,10M;
- delta: -3,7%.

L'AI ha sovrastimato il problema di oltre quattro punti percentuali.

## Step 2 — Verificare freshness e completeness

L'analista controlla gli SLO del dato:

| Dataset | Freshness | Completezza |
|---|---:|---:|
| bookings | 07:15 | 99,99% |
| payments | 07:20 | 99,97% |
| refunds | 07:10 | 99,98% |
| advertising | 06:55 | 100% |
| partner adjustments | 11:00 | 82% |

Il dataset `partner_adjustments` non è ancora finalizzato.

Storicamente aggiunge circa €250–350k alla settimana, ma la quota varia molto per mercato.

Quindi il -3,7% è ancora provvisorio.

## Step 3 — Chiedere all'AI un piano diagnostico, non una conclusione

Prompt:

> "Non formulare ancora una spiegazione. Proponi un decomposition plan che separi volume, conversion, average booking value, cancellation/refund rate, commission rate e mix geografico. Indica per ciascun blocco quali metriche certificate usare e quali sanity check eseguire."

Il piano è valido e permette di accelerare il lavoro.

## Step 4 — Il decomposition

Dopo i controlli emergono:

- traffico: -0,6%;
- conversion: -2,8%;
- average booking value: +1,1%;
- cancellation/refund: leggermente peggiore;
- commission rate: stabile.

Il calo è quindi più vicino a un problema di conversion che di domanda complessiva.

## Step 5 — Segmentazione

L'AI genera SQL per scomporre la conversion per:

- market;
- device;
- app/web;
- payment method;
- destination type;
- acquisition channel.

La prima query mostra un forte peggioramento su mobile app Francia.

Ma l'analyst chiede un test di composizione:

> "Verifica se il mix di app version è cambiato e se il calo rimane entro ciascuna versione."

Risultato:

| App version | Share prev. | Share curr. | Conversion prev. | Conversion curr. |
|---|---:|---:|---:|---:|
| 8.41 | 62% | 18% | 4,9% | 4,8% |
| 8.42 | 21% | 67% | 4,8% | 3,7% |
| altro | 17% | 15% | 4,5% | 4,4% |

Il problema è concentrato sulla 8.42.

## Step 6 — Funnel e log

L'AI suggerisce di confrontare il funnel.

La caduta si concentra tra:

`payment_started -> payment_authorized`

Il rate di errore PSP aumenta dal 2,1% al 6,8% sulla versione 8.42, ma soltanto per carte salvate.

Un release note tecnico segnala che la 8.42 ha modificato il token refresh delle stored cards.

Il team engineering riproduce il bug.

## Step 7 — Evitare una falsa causalità geografica

Perché sembrava un problema Francia?

La Francia aveva la quota maggiore di utenti già migrati alla 8.42 e un utilizzo più alto delle stored cards.

Il paese era quindi un **proxy del rollout**, non la causa.

Questa distinzione cambia la decisione.

La risposta sbagliata sarebbe stata:

> "La domanda mobile in Francia sta peggiorando."

La risposta migliore è:

> "La riduzione di conversion è concentrata sugli utenti della versione 8.42 che pagano con carte salvate. La Francia appare più colpita perché il rollout della versione e l'uso delle stored cards sono più elevati. Il pattern è compatibile con il bug di token refresh confermato da engineering."

## Step 8 — Quantificare l'impatto

L'analista usa una stima semplice basata su volumi e differenza di conversion.

Impatto stimato:

- booking persi: 8.900–10.600;
- net revenue persa: €510k–€620k;
- intervallo ampio per effetto di refund e partner adjustment non ancora finalizzati.

La decisione:

1. rollback della 8.42 per stored cards;
2. blocco del rollout ulteriore;
3. monitoraggio conversion e payment error;
4. aggiornamento CFO alle 12:00 con dati finalizzati.

## Dove l'AI ha creato valore

L'AI ha ridotto il tempo necessario per:

- scrivere query;
- proporre decomposition;
- generare segmentazioni;
- trovare controlli diagnostici;
- riassumere i risultati;
- preparare la comunicazione.

Senza AI l'indagine avrebbe potuto richiedere gran parte della mattinata.

## Dove l'AI avrebbe creato danno senza controllo

La prima risposta aveva tre problemi:

1. metrica non certificata;
2. dataset non finalizzato;
3. associazione geografica interpretata come driver.

La velocità avrebbe amplificato l'errore.

## Il workflow finale

La procedura che Aurelia formalizza dopo l'incidente è:

**Question → Certified metric → Data health → AI plan → Generated queries → Sanity checks → Decomposition → Alternative hypotheses → Human interpretation → Decision**

Inoltre introduce una regola:

> nessun output AI su KPI executive può essere pubblicato se non mostra metrica certificata, timestamp di freshness e query/filtri utilizzati.

## Lezione del caso

AI-assisted analytics funziona meglio quando l'organizzazione ha già:

- semantic layer;
- metriche certificate;
- data quality metadata;
- lineage;
- ownership;
- procedure di verifica.

L'AI non sostituisce queste fondamenta. Le sfrutta.

> **Quando l'esecuzione diventa quasi istantanea, il collo di bottiglia si sposta dalla produzione della risposta alla dimostrazione che la risposta merita fiducia.**
