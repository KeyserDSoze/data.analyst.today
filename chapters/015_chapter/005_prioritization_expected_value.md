# 15.4 Prioritizzare: impatto atteso, confidenza e costo

Quando un'analisi produce dieci possibili azioni, il problema successivo non è più capire i dati.

È scegliere dove intervenire prima.

Una struttura semplice può combinare:

- impatto potenziale;
- probabilità che l'intervento funzioni;
- costo;
- tempo;
- rischio;
- reversibilità.

## Un punteggio non sostituisce il giudizio

Framework come ICE, RICE o score interni possono aiutare, ma non trasformano automaticamente problemi diversi in numeri comparabili.

Un punteggio è utile quando rende esplicite le assunzioni.

Diventa pericoloso quando nasconde discussioni importanti dietro una formula.

## Caso realistico: cinque idee, una sola squadra

Un prodotto fintech ha cinque iniziative possibili:

| Iniziativa | Valore annuo potenziale | Confidenza | Costo stimato | Tempo |
|---|---:|---:|---:|---:|
| Ridurre payment failures | €1,8M | Alta | €220k | 6 settimane |
| Nuovo referral program | €2,5M | Bassa | €500k | 4 mesi |
| Migliorare onboarding KYC | €1,1M | Alta | €140k | 5 settimane |
| Nuova dashboard merchant | €600k | Media | €250k | 3 mesi |
| Pricing optimization | €3,4M | Media | €800k | 6 mesi |

La tentazione è scegliere il valore massimo: pricing optimization.

Ma il team analitico scopre che il problema dei payment failures è già ben localizzato, la soluzione è tecnicamente semplice e il valore è altamente plausibile.

La scelta razionale può essere iniziare da lì.

## Expected value semplificato

Una forma utile è:

**Valore atteso = beneficio potenziale × probabilità di successo − costo**

Non va interpretata come matematica perfetta.

Serve a obbligarci a distinguere tra:

- grande opportunità ma altamente incerta;
- opportunità più piccola ma molto credibile;
- progetto costoso e difficile da invertire;
- quick win con ritorno rapido.

## Non ignorare la capacità operativa

Un modello può identificare 40.000 clienti ad alta probabilità di churn.

Se il customer success team può contattarne solo 2.000, la decisione non è “chi è a rischio?”.

È:

> “Quali 2.000 clienti hanno il più alto valore incrementale atteso da un intervento?”

Questo riporta al principio già incontrato nei capitoli su causalità e predizione: risk score e treatment effect non sono la stessa cosa.

## Il miglior progetto può essere non fare nulla

Esistono situazioni in cui il valore atteso dell'intervento è negativo.

Per esempio:

- problema piccolo;
- alta incertezza;
- implementazione costosa;
- rischio di effetti collaterali;
- alternative migliori.

Dire “non interveniamo ora” può essere una decisione analiticamente ottima.

> **La priorità non è trovare l'idea più grande. È trovare la prossima azione con il miglior rapporto tra valore atteso, evidenza e costo.**
