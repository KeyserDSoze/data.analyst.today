## 2.11 L'Analytical Brief: il contratto prima dell'analisi

A questo punto possiamo riunire le scelte delle sezioni precedenti in un unico documento.

Un **Analytical Brief** è una specifica breve che descrive che cosa stiamo cercando di capire, perché conta, quale evidenza serve e quando il lavoro sarà sufficientemente completo.

Non è un project charter da dieci pagine.

Per molte analisi basta una pagina.

La sua funzione è creare allineamento **prima** che l'esecuzione renda costoso cambiare direzione.

### I campi essenziali

#### 1. Problema di business

Quale risultato, rischio o opportunità ha generato la richiesta?

> La repeat purchase rate dei nuovi clienti sembra essersi deteriorata.

#### 2. Decisione

Quale scelta deve diventare più informata?

> Decidere se intervenire su acquisizione, post-purchase experience o campagne di riattivazione.

Annotare anche owner, alternative, deadline e costo principale dell'errore.

#### 3. Domanda analitica primaria

Deve essere abbastanza specifica da guidare dati e metodo.

> Quali segmenti e quali cambiamenti osservabili spiegano maggiormente il calo della repeat purchase rate a 90 giorni rispetto alle coorti comparabili?

#### 4. Tipo di domanda e pretesa massima

> Diagnostica. L'analisi genererà e restringerà ipotesi; non attribuirà automaticamente causalità agli eventuali driver osservati.

Questa riga impedisce che il deliverable venga giudicato secondo una promessa metodologica diversa da quella concordata.

#### 5. Metriche

Specificare:

- outcome primaria;
- driver principali;
- guardrail, se rilevanti;
- formula e popolazione;
- target o soglie decisionali note.

#### 6. Scope

Definire:

- popolazione eleggibile;
- esclusioni;
- unità di analisi;
- periodo;
- data/time field;
- maturazione;
- fuori scope.

#### 7. Baseline

Con quale riferimento giudicheremo il cambiamento e perché è comparabile?

#### 8. Segmentazioni previste

Quali gruppi potrebbero cambiare la spiegazione o la decisione?

#### 9. Ipotesi prioritarie

Non una lista infinita, ma le spiegazioni principali e l'evidenza che le rafforzerebbe o indebolirebbe.

#### 10. Requisiti dati

Quali dati sono required, useful o proxy? Quali gap conosciamo già?

#### 11. Metodo iniziale

Qual è il percorso analitico minimo che può rispondere alla domanda?

Per esempio:

1. data sanity check;
2. ricostruzione outcome;
3. confronto con baseline;
4. decomposizione e segmentazione;
5. test delle ipotesi prioritarie;
6. quantificazione dell'impatto economico.

Non serve pre-specificare ogni query. Serve impedire che il metodo venga scelto soltanto dopo aver visto il risultato che vogliamo spiegare.

#### 12. Limiti e rischi noti

Quali problemi potrebbero rendere l'analisi meno affidabile?

- tracking cambiato;
- piccolo campione;
- identità cliente instabile;
- popolazioni non comparabili;
- proxy imperfetti;
- dati ancora immaturi.

#### 13. Output

Che cosa serve davvero?

- memo decisionale;
- notebook riproducibile;
- dataset;
- dashboard;
- modello;
- esperimento proposto.

L'output deriva dalla decisione, non il contrario.

#### 14. Stop rule

Quando l'evidenza sarà sufficiente per consegnare?

Esempio:

> “Concludiamo la prima fase quando abbiamo validato la metrica, localizzato almeno l'80% del delta osservato e testato le tre ipotesi prioritarie, oppure quando emerge un limite dati che impedisce di distinguerle.”

La soglia non deve essere sempre numerica, ma dovrebbe impedire l'analisi infinita.

#### 15. Criterio di successo

Non:

> “Dashboard consegnata.”

Meglio:

> “Il decision owner dispone di evidenza sufficiente per scegliere se intervenire e sa quali incertezze rimangono.”

### Template riutilizzabile

```text
Problema di business:

Decisione:
Decision owner:
Alternative:
Deadline/frequenza:
Costo principale dell'errore:

Domanda analitica primaria:
Tipo di domanda / pretesa massima:
Domande secondarie:

Outcome metric:
Driver metrics:
Guardrails:
Target/soglia, se nota:

Popolazione:
Esclusioni:
Unità di analisi:
Periodo / campo temporale:
Maturazione:
Fuori scope:

Baseline:
Segmentazioni previste:

Ipotesi prioritarie:

Dati required:
Dati useful/proxy:
Gap noti:

Metodo iniziale:
Limiti/rischi:

Output:
Stop rule:
Criterio di successo:
```

### Il brief è vivo, ma non invisibilmente mutevole

Nuove informazioni possono richiedere una modifica del piano. È normale.

La disciplina consiste nel **aggiornare esplicitamente il brief** quando cambiano domanda, metrica, scope o livello di evidenza richiesto, invece di lasciare che l'analisi evolva senza che stakeholder e analyst se ne accorgano.

In un ambiente in cui AI e strumenti self-service possono produrre output quasi immediatamente, il brief è ancora più prezioso: introduce pochi minuti di attrito nel punto in cui l'attrito costa meno.

> **Un buon brief non rallenta l'analisi. Rende più difficile andare velocemente nella direzione sbagliata.**
