## 1.13 Caso studio: “Le vendite stanno scendendo”

**Caso simulato/composito.** Una buona teoria analitica diventa utile quando regge davanti a una richiesta concreta.

Immaginiamo che il direttore commerciale dica:

> “Le vendite stanno scendendo. Voglio capire perché.”

La frase sembra chiara. In realtà contiene quasi tutte le ambiguità affrontate nel capitolo.

### 1.13.1 Prima domanda: che cosa significa “vendite”?

La parola può indicare:

- fatturato lordo;
- fatturato netto;
- numero di ordini;
- unità vendute;
- margine;
- valore medio dell'ordine;
- ordini completati;
- ordini acquisiti ma non ancora evasi.

Se due persone usano definizioni diverse, possono costruire analisi entrambe tecnicamente corrette e arrivare a conclusioni incompatibili.

Il direttore chiarisce che gli interessa il **fatturato netto degli ordini completati**, perché sta decidendo se intervenire su pricing, marketing o assortimento nel trimestre successivo.

La richiesta è già diventata più analizzabile.

### 1.13.2 Seconda domanda: rispetto a che cosa?

Dire che una metrica “scende” implica una baseline.

Possiamo confrontare con:

- mese precedente;
- stesso mese dell'anno precedente;
- media mobile;
- budget;
- forecast;
- periodo pre-promozione.

Il business è stagionale, quindi il confronto con il mese precedente sarebbe debole. L'analista usa soprattutto lo stesso periodo dell'anno precedente e il forecast, verificando che il perimetro dei negozi sia comparabile.

Il calo risulta circa del 10% in entrambi i confronti.

### 1.13.3 Scomporre prima di spiegare

Una prima identità utile è:

**Ricavi = numero di ordini × valore medio dell'ordine**

Il valore medio è quasi stabile. Gli ordini sono diminuiti.

Possiamo quindi continuare:

**Ordini = traffico qualificato × conversion rate**

Il traffico complessivo è stabile, mentre la conversione diminuisce.

Le identità non sono modelli causali. Sono un **issue tree** che trasforma una domanda generica in componenti osservabili.

### 1.13.4 Segmentare prima di costruire una storia

Il calo non è uniforme.

L'analista trova che:

- il segmento enterprise cresce;
- il consumer diminuisce;
- quasi tutto il delta viene dall'e-commerce;
- desktop è stabile;
- mobile mostra il peggioramento principale;
- clienti esistenti sono relativamente stabili;
- la perdita si concentra nei nuovi visitatori mobile.

Ora la domanda non è più:

> “Perché le vendite sono scese?”

ma:

> “Perché la conversione dei nuovi visitatori mobile è peggiorata?”

Questa è una riduzione enorme dello spazio investigativo.

### 1.13.5 Prima di cercare cause di business, escludere un artefatto

L'analista controlla:

- freshness delle sorgenti;
- ordini mancanti;
- duplicati;
- cambio di definizione di `completed_order`;
- fusi orari;
- modifiche al tracking mobile;
- riconciliazione del fatturato con una fonte indipendente.

Il fenomeno rimane.

Questo passaggio è poco spettacolare, ma evita di costruire una spiegazione sofisticata di un bug nella pipeline.

### 1.13.6 Dal pattern alle ipotesi

Negli stessi giorni sono avvenuti diversi cambiamenti:

- nuova versione del checkout mobile;
- variazione del mix delle campagne;
- modifica delle condizioni di spedizione su alcuni mercati;
- promozioni su categorie specifiche.

Il team potrebbe scegliere la prima storia plausibile e fermarsi.

L'analista invece formula ipotesi concorrenti e cerca osservazioni che le distinguano.

La decomposizione del funnel mostra che il peggioramento principale avviene tra selezione del metodo di pagamento e conferma.

Il pattern inizia subito dopo il rollout del nuovo checkout ed è molto più forte sugli utenti effettivamente esposti alla nuova versione.

Questo non dimostra ancora da solo una causa, ma rende il problema tecnico una priorità investigativa.

### 1.13.7 Quando l'evidenza è sufficiente per agire

L'analista stima che circa il 75% del calo osservato sia concentrato nel funnel mobile interessato dal rollout.

Il checkout è reversibile rapidamente e il costo di aspettare è elevato.

La decisione non richiede quindi una prova causale perfetta prima di qualsiasi intervento.

Il team decide di:

1. verificare tecnicamente gli errori e la telemetria del nuovo checkout;
2. sospendere ulteriori rollout;
3. ripristinare temporaneamente la versione precedente per una parte del traffico;
4. confrontare conversione e failure rate;
5. misurare se il recupero del funnel si traduce anche in ordini e fatturato.

L'analisi non termina con la diagnosi.

La risposta del sistema all'intervento diventa nuova evidenza.

### 1.13.8 Dove può aiutare l'AI

Un assistente AI può accelerare molti passaggi:

- generare query di segmentazione;
- proporre decomposizioni;
- scrivere controlli;
- sintetizzare log o anomalie;
- produrre visualizzazioni esplorative;
- suggerire ipotesi rivali.

Ma la definizione di fatturato, la baseline, la decisione e il livello di evidenza necessario derivano dal contesto del problema.

La documentazione Microsoft su Copilot in Power BI offre un esempio concreto dello stesso principio: prompt e output dipendono dalla qualità e dalla semantica del modello sottostante.

Riferimento:
- https://learn.microsoft.com/en-us/power-bi/create-reports/copilot-semantic-models

### Regola operativa

> **Prima di spiegare un cambiamento, localizzalo. Prima di localizzarlo, definisci metrica e confronto. Prima di definire metrica e confronto, chiarisci la decisione.**
