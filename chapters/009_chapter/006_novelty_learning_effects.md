## 9.5 Novelty, learning e durata: abbastanza utenti non significa abbastanza tempo

Un test può raggiungere la numerosità pianificata molto prima di aver osservato il comportamento che ci interessa.

Questo accade soprattutto nei prodotti ad alto traffico.

La durata sperimentale deve coprire non solo il **sample requirement**, ma anche il tempo necessario perché:

- gli utenti vedano il trattamento più volte;
- novelty e learning si stabilizzino;
- maturino outcome ritardati;
- entrino cicli weekday/weekend o business cycle rilevanti.

### Caso simulato/composito — La homepage che vince soltanto perché è nuova

Una media company testa una homepage più dinamica.

| Exposure age | Delta pagine/sessione B vs A |
|---|---:|
| giorni 1–3 | +6,7% |
| giorni 4–7 | +2,2% |
| giorni 8–14 | +0,4% |

Se guardassimo soltanto il calendario del test, potremmo dire che “l'effetto decade”.

Ma una domanda migliore è:

> **quanta esperienza ha ciascun utente con la variante?**

Un utente arrivato al giorno 12 del test può essere alla sua prima exposure. Un returning user può essere alla decima.

Per questo è utile distinguere **experiment age** ed **exposure age**.

### Novelty effect

Un cambiamento può generare temporaneamente:

- curiosità;
- più esplorazione;
- click aggiuntivi;
- attenzione superiore;
- comportamento meno routinario.

Il movimento iniziale può diminuire quando la feature diventa normale.

Questo non significa che ogni effetto decrescente sia novelty. Può essere anche:

- cambio nel mix degli utenti esposti;
- campagna temporanea;
- bug risolto;
- weekday mix;
- regressione verso la media.

Serve segmentare per tenure di exposure e contesto.

### Learning effect

Il movimento può andare nella direzione opposta.

Un software B2B introduce una nuova interfaccia di reporting.

Prima settimana:

- task completion: -5,8%;
- tempo task: +13%;
- errori: +19%.

Quarta settimana:

- task completion: +4,1%;
- tempo task: -11%;
- errori: -7%.

Un test troppo breve avrebbe misurato soprattutto il **costo di apprendimento**, non l'effetto steady-state.

La domanda decisionale deve quindi chiarire:

> vogliamo conoscere l'effetto immediato del rollout o quello dopo che gli utenti hanno imparato?

Entrambi possono essere importanti.

### Duration floor: il minimo temporale indipendente dal sample size

Supponiamo che QuickPay raggiunga il sample size in 36 ore.

Potremmo comunque imporre:

```text
sample requirement: raggiunto
minimum calendar duration: 14 giorni
reason: due cicli weekday/weekend + returning exposure
```

Questa non è superstizione del tipo “ogni test deve durare due settimane”.

La durata minima deve derivare dal processo:

- weekend vs feriali;
- payroll/payday;
- ciclo di rinnovo;
- frequenza di riacquisto;
- latency dell'outcome;
- learning atteso.

### Outcome maturity

Alcune metriche non sono mature al momento dell'azione iniziale.

Esempio QuickPay:

```text
ordine creato: t0
cancellazione possibile: entro 24h
chargeback: può emergere molto dopo
reso: giorni/settimane
```

Se la decisione usa `valid_order_after_24h`, l'ultimo giorno di traffico richiede almeno 24 ore di maturazione prima dell'analisi finale.

La data di fine enrollment e la data di fine observation non sono necessariamente la stessa.

### New vs returning users

Separare:

- first exposure;
- repeated exposure;
- nuovi utenti;
- utenti abituati alla vecchia esperienza;

può chiarire se stiamo misurando:

- valore strutturale;
- surprise;
- migration cost;
- learning.

Non tutte le segmentazioni devono guidare una causal claim separata; possono essere diagnostics pre-specificati del comportamento nel tempo.

### Stagionalità dell'esperimento

Il Capitolo 7 ci ha insegnato che il martedì non è necessariamente intercambiabile con il sabato.

Un esperimento deve quindi chiedersi:

- il traffico copre il normale mix settimanale?
- coincide con Black Friday o saldi?
- una campagna marketing crea popolazione insolita?
- il test attraversa un release event?

Un test randomizzato protegge da molti shock comuni contemporanei perché A e B li attraversano insieme. Ma la **generalizzazione** del risultato può essere limitata se il periodo è eccezionale.

### Duration card

```text
Sample size requirement:
Expected time to reach it:
Minimum calendar duration:
Cycles that must be covered:
Outcome maturation lag:
Expected novelty:
Expected learning:
Exposure-age diagnostics:
New vs returning user plan:
Exceptional calendar events:
Analysis date after maturity:
```

> **Il sample size risponde a “quanta informazione?”. La durata risponde anche a “quale fase del comportamento abbiamo osservato?”.**
