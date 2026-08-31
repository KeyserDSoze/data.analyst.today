## 8.9 Matching e propensity score: costruire un confronto più credibile

Quando non possiamo randomizzare, spesso il primo problema è che gruppo trattato e gruppo di controllo sono diversi già prima dell'intervento.

Immaginiamo una società B2B SaaS che offre un programma di onboarding premium ai clienti considerati più promettenti. Dopo sei mesi, il team Customer Success presenta un risultato impressionante:

- churn clienti con onboarding premium: **6,8%**;
- churn clienti senza onboarding premium: **12,9%**.

La conclusione sembra ovvia: l'onboarding premium dimezza quasi il churn.

Ma il programma non era stato assegnato casualmente. I clienti premium avevano mediamente:

- ARR iniziale più alto;
- team interni più grandi;
- maggiore maturità digitale;
- più utenti attivi nella prima settimana;
- account manager dedicati.

Quindi la differenza osservata può riflettere sia l'effetto dell'onboarding sia il fatto che i clienti trattati fossero diversi in partenza.

### Matching

L'idea del matching è cercare, per ogni unità trattata, una o più unità non trattate sufficientemente simili rispetto alle caratteristiche osservate rilevanti.

Per esempio possiamo confrontare un cliente trattato con:

- ARR simile;
- stessa industry;
- dimensione aziendale simile;
- stesso mercato geografico;
- activation iniziale simile;
- stessa anzianità contrattuale.

Dopo il matching, il confronto può diventare:

- churn trattati: **6,8%**;
- churn controlli comparabili: **8,4%**.

L'effetto apparente passa quindi da **-6,1 punti percentuali** a **-1,6 punti**.

Il programma potrebbe ancora essere utile, ma molto meno di quanto suggerisse il confronto grezzo.

### Propensity score

Quando le caratteristiche da bilanciare sono molte, si può sintetizzare la probabilità di ricevere il trattamento in un unico punteggio:

> **propensity score = P(trattamento | caratteristiche osservate prima del trattamento)**

Due clienti con propensity score simile hanno, sulla base delle variabili osservate, una probabilità simile di entrare nel programma.

Il matching sul propensity score prova quindi a confrontare unità con simile probabilità di trattamento.

La World Bank descrive il propensity score matching come un metodo quasi-sperimentale che costruisce un gruppo di controllo artificiale abbinando unità trattate e non trattate con caratteristiche osservate simili. Sottolinea anche il limite fondamentale: se esistono confondenti non osservati importanti, il bias può rimanere elevato.

### Common support

Un errore frequente è forzare confronti dove non esiste una vera controparte.

Se tutti i clienti enterprise sopra 500.000 euro di ARR hanno ricevuto il programma premium, non esistono clienti enterprise simili non trattati con cui confrontarli.

In quella zona manca **overlap** o **common support**.

Non è un problema che si risolve con un algoritmo più sofisticato. È una limitazione del disegno.

### Variabili pre-treatment

Nel propensity score devono entrare caratteristiche definite prima dell'intervento.

Inserire, per esempio, `weekly_active_users` misurato dopo l'onboarding potrebbe controllare proprio una parte del meccanismo attraverso cui il trattamento produce effetto.

### Caso operativo: il programma VIP

Una piattaforma marketplace introduce un servizio VIP per i seller con performance elevate.

Risultato grezzo a dodici mesi:

| Gruppo | Seller retention |
|---|---:|
| VIP | 91% |
| Non VIP | 72% |

Dopo matching per fatturato precedente, categorie vendute, rating, anzianità, numero di ordini e paese:

| Gruppo comparabile | Seller retention |
|---|---:|
| VIP | 91% |
| Matched non-VIP | 86% |

Il programma sembra ancora associato a una retention migliore, ma il grosso del vantaggio iniziale derivava dalla selezione dei seller migliori.

### Regola pratica

> **Il matching può rendere più comparabili i gruppi sulle variabili osservate. Non può rendere osservabile ciò che nei dati non esiste.**

### Riferimenti

- World Bank, *Impact Evaluation in Practice*, capitolo sul matching.
- World Bank DIME Wiki, *Propensity Score Matching*.
