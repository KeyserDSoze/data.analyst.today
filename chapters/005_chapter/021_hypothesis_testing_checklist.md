## 5.20 Checklist operativa: prima di dichiarare un risultato

Prima di scrivere "il test è significativo", fermati e controlla l'intera catena.

### 1. La domanda è chiara?

Quale decisione deve supportare il test? Qual è la metrica primaria? Quale effetto sarebbe abbastanza grande da cambiare la decisione?

### 2. Il confronto è valido?

I gruppi sono comparabili? L'assegnazione è casuale? Esistono differenze preesistenti? Ci sono contaminazioni tra controllo e trattamento?

### 3. Il campione è adeguato?

Il test ha potenza sufficiente per rilevare l'effetto minimo rilevante? Il campione è rappresentativo della popolazione su cui verrà presa la decisione?

### 4. Le assunzioni del metodo sono ragionevoli?

Indipendenza, forma distributiva, varianze, struttura temporale e unità di analisi sono compatibili con il test scelto?

### 5. Quanto è grande l'effetto?

Non fermarti al p-value. Riporta differenza assoluta, differenza relativa quando utile, intervallo di confidenza e una misura dell'effetto coerente con il problema.

### 6. Quanto è incerto?

L'intervallo include effetti economicamente irrilevanti? Include anche effetti negativi? La stima è abbastanza precisa da sostenere una decisione?

### 7. Quanti test hai eseguito?

La metrica era definita prima? Hai analizzato decine di segmenti o KPI? Se sì, considera il problema della molteplicità e distingui chiaramente analisi esplorativa e confermativa.

### 8. Esistono guardrail metrics?

Un miglioramento locale può produrre danni altrove. Conversione più alta ma resi maggiori. Tempi più bassi ma costi superiori. Engagement più alto ma retention peggiore.

### 9. Il risultato è stabile?

Controlla giorno per giorno, per coorti temporali e per segmenti predefiniti. Verifica se l'effetto dipende da campagne, festività, incidenti tecnici o cambi di mix.

### 10. Cambia davvero la decisione?

Questa è la domanda finale.

Un risultato statisticamente interessante che non modifica alcuna azione può essere informativo, ma non necessariamente decisionale.

### Come scrivere una conclusione robusta

Una conclusione professionale potrebbe avere questa struttura:

> La variante aumenta la conversione di +0,19 punti percentuali rispetto al controllo. L'effetto è statisticamente incompatibile con l'ipotesi di differenza nulla al livello predefinito, ma il beneficio economico si riduce dopo aver considerato l'aumento dei resi. Il revenue netto per visitor rimane incerto e l'intervallo include effetti prossimi allo zero. Non raccomandiamo il rollout completo; proponiamo un test più lungo con revenue netto come metrica primaria e return rate come guardrail.

Questa conclusione contiene dato, incertezza, contesto e decisione.

## Esercizi

### Esercizio 1 — Il p-value perfetto

Un marketplace testa un nuovo badge "Best price" su 3,5 milioni di utenti. La conversione passa da 2,841% a 2,873%, con p = 0,004. L'implementazione costa 1,1 milioni di euro l'anno.

Quali informazioni chiedi prima di raccomandare il rollout?

### Esercizio 2 — Test inconcludente

Un prodotto B2B mostra churn al 7,2% nel controllo e al 5,9% nel trattamento, ma il campione contiene solo 430 clienti per gruppo e il p-value è 0,19.

Scrivi una conclusione che non confonda "assenza di evidenza" con "evidenza di assenza".

### Esercizio 3 — Multiple testing

Un team misura 80 KPI e trova 6 metriche con p < 0,05. Nessuna era stata definita come primaria.

Come interpreteresti il risultato? Quale sarebbe il prossimo esperimento?

### Esercizio 4 — Tipo I o tipo II?

Per un sistema antifrode, descrivi un falso positivo e un falso negativo. Assegna un costo plausibile a entrambi e discuti come questo dovrebbe influenzare la soglia decisionale.

### Esercizio 5 — Significativo ma inutile

Un algoritmo riduce il tempo medio di risposta del supporto da 4 ore e 18 minuti a 4 ore e 11 minuti su 900.000 ticket, con un p-value estremamente piccolo.

Quali metriche aggiuntive useresti per capire se l'intervento genera valore reale?

### Esercizio 6 — Disegna un test prima di vedere i dati

Definisci un A/B test per una nuova pagina pricing SaaS specificando:

- ipotesi nulla e alternativa;
- metrica primaria;
- almeno due guardrail metrics;
- effetto minimo business-rilevante;
- popolazione;
- durata minima;
- segmenti definiti prima dell'esperimento;
- criterio decisionale.

Se riesci a compilare questi elementi prima di guardare il risultato, hai già ridotto una parte importante del rischio di autoinganno analitico.
