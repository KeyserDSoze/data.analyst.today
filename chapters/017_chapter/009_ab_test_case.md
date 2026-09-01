## 17.8 “Il test è positivo: possiamo fare rollout?”

### Caso simulato/composito: VelaPay

VelaPay introduce un checkout semplificato.

Dopo 14 giorni:

- controllo: `71,4%`;
- variante: `72,3%`;
- uplift assoluto: `+0,9 pp`;
- p-value: `0,018`.

La frase che arriva in Slack è:

> “Test vinto. Rollout?”

Il capstone comincia da una domanda più rigorosa:

> **L'esperimento è abbastanza affidabile e il profilo beneficio/rischio è abbastanza favorevole da cambiare la policy di prodotto?**

## Routing iniziale

| Elemento | Scelta |
|---|---|
| Decisione | rollout 100%, rollout graduale o nessun rollout |
| Failure cost | spedire una variante dannosa o bloccare una variante utile |
| Claim necessario | causale, perché il test è progettato proprio per identificare l'effetto |
| Reversibilità | alta con rollout progressivo |
| Incertezza critica | integrità randomizzazione + guardrail economici |
| Stop rule | nessuna conclusione finché SRM/data quality non sono spiegati |

## 1. Il primary metric non è tutta la decisione

L'analista controlla i guardrail e trova:

- payment authorization rate: stabile;
- chargeback rate: `0,42% → 0,57%`;
- support contacts: `+6%`;
- Android low-end: conversione `-1,8 pp`;
- anomalia di allocazione associata a una versione obsoleta dell'SDK.

Il risultato principale è positivo.

La decisione non è ancora pronta.

Esistono almeno tre domande:

1. possiamo fidarci del confronto?
2. il beneficio supera i danni collaterali?
3. l'eterogeneità è reale o rumore esplorativo?

## 2. Experiment Contract prima dell'analisi

L'Experiment Contract originale specificava:

- unità di randomizzazione;
- split atteso;
- primary metric;
- guardrail;
- MDE;
- durata minima;
- criteri di esclusione;
- policy per segment analysis;
- stopping rule;
- rollout policy prevista in caso di esito positivo.

Questo documento è ciò che permette di distinguere una sorpresa legittima da una metrica scelta dopo aver visto i dati.

## 3. Sample Ratio Mismatch: il risultato può essere numericamente corretto e sperimentalmente inaffidabile

Il test presenta un lieve ma statisticamente chiaro **Sample Ratio Mismatch**.

Il team non lo tratta come una nota tecnica.

È un trust gate.

### Caso reale documentato: Microsoft e SRM

Microsoft Research documenta gli SRM come sintomo di problemi che possono nascere in assignment, execution, logging, join o analysis. La raccomandazione è di non fidarsi dei risultati finché la causa del mismatch non è stata diagnosticata.

Fonte: https://www.microsoft.com/en-us/research/publication/diagnosing-sample-ratio-mismatch-in-online-controlled-experiments-a-taxonomy-and-rules-of-thumb-for-practitioners/

Microsoft racconta anche un caso reale su un image carousel MSN. Una variante appariva peggiorare engagement; l'esperimento aveva però un SRM. L'indagine mostrò che un algoritmo di bot detection stava filtrando in modo sproporzionato utenti molto coinvolti nella variante. Corretto il problema, la direzione del risultato si invertì.

Fonte: https://www.microsoft.com/en-us/research/articles/diagnosing-sample-ratio-mismatch-in-a-b-testing/

La lezione è forte:

> **un p-value non ripara un confronto la cui comparabilità è stata compromessa.**

## 4. Root-cause dell'SRM

Nel caso VelaPay, l'SDK obsoleto gestisce in modo diverso una parte dell'assegnazione/telemetria su specifici device.

Il team separa quindi:

- problema di assignment;
- problema di exposure logging;
- problema di event loss;
- vero effetto del trattamento.

Finché la root-cause non è chiusa, l'esito resta `BLOCKED` per rollout globale.

Questa è una vera **stop condition**.

## 5. Significatività non equivale a valore economico

Anche eliminando il problema di integrità, `+0,9 pp` sulla conversione non basta.

VelaPay introduce un outcome economico:

**incremental gross profit per 1.000 checkout**

che incorpora:

- conversione aggiuntiva;
- fee;
- chargeback;
- support cost;
- refund/fraud effect rilevanti.

Ora il test può essere valutato sulla decisione, non soltanto sulla metrica più visibile.

## 6. Segmenti: investigare senza trasformare rumore in policy

Il calo Android low-end è decision-critical perché:

- il segmento è grande;
- l'effetto potenziale è materialmente negativo;
- esiste una plausibile spiegazione tecnica.

Ma il team evita di cercare decine di sottogruppi finché non trova quello “interessante”.

La segment analysis segue una gerarchia:

1. segmenti pre-specificati;
2. segmenti operativamente critici;
3. analisi esplorativa marcata come tale;
4. conferma separata prima di creare policy permanente.

## 7. Seconda fase: correggere, poi ristabilire fiducia

Dopo aver corretto l'allocazione, VelaPay esegue una nuova fase limitata.

Il nuovo test mostra:

- uplift più piccolo;
- intervallo compatibile con beneficio moderato;
- nessun deterioramento materialmente rilevante dei chargeback;
- Android low-end stabile;
- support contacts entro guardrail.

La decisione cambia da `BLOCKED` a `APPROVED FOR RAMP`.

## 8. Decision Record: dal risultato alla rollout policy

Le alternative sono:

### A — Rollout immediato 100%

Massimizza velocità, ma aumenta blast radius.

### B — Nessun rollout

Molto prudente, ma spreca evidenza positiva dopo la correzione.

### C — Rollout progressivo con gate

1. 10% utenti, osservazione 72 ore;
2. 50% se chargeback, latency e support restano entro soglia;
3. 100% solo se primary metric e guardrail restano coerenti;
4. rollback automatico/manuale se una stop condition viene superata.

La scelta è C.

Questo è il punto in cui experimentation incontra decision engineering.

## 9. Decision Communication Pack

La headline non è:

> “p = 0,018: B vince.”

È:

> **“Il primo test mostrava uplift ma non era affidabile a causa di un problema di allocazione. Dopo la correzione, il beneficio resta positivo e i guardrail sono stabili. Raccomandiamo ramp 10% → 50% → 100% con rollback se chargeback o latency superano soglia.”**

Il pack mostra:

- effect size e intervallo;
- trust checks;
- guardrail;
- economics;
- segmenti critici;
- rollout/rollback plan.

## 10. Outcome review

Dopo il rollout misuriamo:

- conversione;
- gross profit per 1.000 checkout;
- chargeback;
- support contacts;
- latency/crash;
- effetti per device critici;
- novelty/decay nel tempo.

Un esperimento non termina quando il notebook produce una stella di significatività.

Termina quando l'evidenza è stata trasformata in una policy operativa controllabile.

## Cosa abbiamo scelto di non fare

Non serve ripetere tutta la teoria inferenziale del Capitolo 5 né tutta la meccanica del Capitolo 9.

Qui il punto è selezionare i gate che possono invalidare **questa decisione**.

La catena è:

**Experiment Contract → trust checks → Uncertainty Brief → Decision Record → Decision Communication Pack → rollout gate → outcome review**

> **Un A/B test non produce una decisione. Produce evidenza causale che deve ancora superare integrità, economia, guardrail e rollout risk.**
