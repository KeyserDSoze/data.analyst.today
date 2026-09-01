## 5.20 Uncertainty Brief: come consegnare una stima senza nascondere ciò che non sappiamo

Il Capitolo 5 non dovrebbe lasciarci con una collezione di formule.

Dovrebbe lasciarci con un nuovo deliverable professionale.

Dopo:

**Analytical Brief → Data Readiness Review → EDA Evidence Map**

aggiungiamo:

> **Uncertainty Brief**

È una scheda che obbliga l'analista a rendere espliciti **stima, popolazione, precisione, assunzioni, bias non quantificati, dimensione dell'effetto e soglia decisionale**.

### Il template

```text
DOMANDA INFERENZIALE
Quale parametro, differenza o rischio stiamo cercando di stimare?

POPOLAZIONE TARGET
Su chi o su che cosa vogliamo generalizzare?

DATI / DISEGNO
Come sono entrate le osservazioni nel campione?
Qual è la numerosità informativa reale?

STIMA
Qual è il valore o effect size osservato?

PRECISIONE
Standard error / confidence interval appropriato.

MODELLO E ASSUNZIONI
Indipendenza? Distribuzione? Unità di analisi? Sampling design?

BIAS NON CONTENUTI NELL'INTERVALLO
Selection, nonresponse, measurement, drift, definizioni, confounding...

TEST, SE UTILE
H0, p-value e criterio pre-specificato.

POWER / INFORMATIVITÀ
Il disegno era capace di distinguere l'effetto che ci interessa?

MOLTEPLICITÀ
Quante metriche, segmenti o specificazioni sono state esplorate?

SOGLIA BUSINESS
Qual è il più piccolo effetto che cambierebbe davvero la decisione?

CONCLUSIONE CALIBRATA
Che cosa sostengono i dati? Che cosa non sostengono?

PROSSIMO PASSO
Agire, raccogliere altri dati, confermare, sperimentare o fermarsi?
```

Questo template non deve diventare burocrazia. Per un'analisi semplice può occupare mezza pagina. Per una decisione ad alto rischio può diventare una review molto più approfondita.

Il principio è sempre lo stesso:

> **più forte è la decisione che vogliamo sostenere, più chiaramente dobbiamo dichiarare che cosa rende forte — o fragile — l'evidenza.**

### Un esempio breve

Immaginiamo una survey customer success.

```text
DOMANDA
Qual è la quota di clienti enterprise soddisfatti del nuovo onboarding?

POPOLAZIONE TARGET
Clienti enterprise attivati nel trimestre.

DISEGNO
Survey inviata a 4.800 clienti; 1.120 risposte.
Risposta volontaria, quindi possibile nonresponse bias.

STIMA
CSAT positivo: 74%.

PRECISIONE
CI 95% da campionamento, sotto assunzioni semplici: circa 71%–77%.

BIAS NON NEL CI
I clienti con onboarding fallito rispondono meno frequentemente.

SOGLIA BUSINESS
Il rollout richiede evidenza ragionevole che il CSAT sia almeno 70%.

CONCLUSIONE
La stima osservata supera il target e il CI di campionamento è prevalentemente sopra 70%,
ma la sottorappresentazione dei clienti con onboarding problematico può produrre bias positivo.
Non presentiamo quindi il 74% come stima definitiva dell'intera popolazione.

PROSSIMO PASSO
Collegare survey e dati operativi, aumentare follow-up dei nonrespondent e fare sensitivity analysis.
```

Notiamo la differenza rispetto a:

> **“Il CSAT è 74% ±3%, quindi siamo sopra target.”**

La seconda frase sembra più semplice. È anche più forte di quanto il disegno consenta.

### Le dieci domande da fare prima di dichiarare un risultato

1. **Popolazione** — a chi voglio generalizzare?
2. **Selezione** — come sono entrati i casi nei dati?
3. **Unità** — quante osservazioni realmente indipendenti ho?
4. **Effetto** — quanto è grande la differenza o il parametro?
5. **Precisione** — quanto potrebbe variare la stima per campionamento?
6. **Bias** — quali errori importanti non sono rappresentati dall'intervallo?
7. **Test** — che cosa dice realmente il p-value e quale modello presume?
8. **Power** — il disegno poteva rilevare un effetto che conta?
9. **Molteplicità** — quante possibilità avevamo di trovare un segnale?
10. **Decisione** — l'effetto è abbastanza grande da cambiare ciò che facciamo?

Se una di queste domande non ha risposta, non significa necessariamente che l'analisi sia inutilizzabile. Significa che il caveat deve entrare nel livello di fiducia della conclusione.

## Sintesi del capitolo

Abbiamo costruito una progressione unica:

**evento → probabilità → condizionamento → dipendenza → distribuzione → expected value → aggiornamento → campionamento → sampling distribution → standard error → CLT → confidence interval → sample size → test → p-value → errori/power → materialità → multiple testing → Uncertainty Brief**.

Le idee da conservare sono poche ma profonde.

**Più dati ≠ dati migliori.**

La numerosità riduce soprattutto una parte del rumore casuale; non corregge automaticamente bias e definizioni.

**Deviazione standard ≠ standard error.**

Una descrive la variabilità delle osservazioni; l'altro la precisione di una stima.

**Confidence interval ≠ intervallo che contiene tutti gli errori dell'analisi.**

Quantifica una forma specifica di incertezza sotto un modello e un disegno.

**p-value ≠ probabilità che H0 sia vera.**

E `p < 0,05` non è una decisione.

**Non significativo ≠ nessun effetto.**

Un test può essere inconcludente perché non contiene abbastanza informazione.

**Significativo ≠ importante.**

Effect size, incertezza ed economia devono essere letti insieme.

**Esplorare molto cambia il significato di ciò che troviamo.**

Multiple testing e scelte a posteriori devono essere dichiarati.

### La frase da portare al capitolo successivo

> **Una buona analisi non elimina l'incertezza. La misura abbastanza bene da impedire alla conclusione di essere più sicura dei dati.**

Il Capitolo 6 tornerà a una domanda di business molto concreta: clienti e utenti non si comportano tutti allo stesso modo. Useremo segmenti, coorti, funnel e retention per capire **dove** si concentra un comportamento e **come evolve** lungo il lifecycle.

L'incertezza appresa qui rimane con noi: ogni tasso di retention, ogni confronto tra coorti e ogni segmento piccolo dovrà essere letto anche in funzione della sua base informativa.

## Esercizi

### Esercizio 1 — Il milione di risposte

Una piattaforma raccoglie un milione di rating volontari e ottiene soddisfazione del 92,4% con un intervallo di campionamento strettissimo.

Sai però che solo gli utenti che completano almeno cinque sessioni vedono la survey.

Costruisci un Uncertainty Brief. Spiega perché aumentare ancora il numero di risposte non risolve il problema principale.

### Esercizio 2 — Stima precisa ma irrilevante

Un cambiamento riduce il churn da 6,000% a 5,970% su 8 milioni di clienti.

La stima è molto precisa e il p-value è minuscolo.

Quali numeri economici servono prima di decidere? Scrivi una conclusione che non usi le parole “vince” o “funziona”.

### Esercizio 3 — Effetto importante ma test debole

Un prodotto B2B osserva:

- controllo: churn 7,2%;
- trattamento: 5,9%;
- 430 clienti per gruppo;
- intervallo molto ampio;
- `p = 0,19`.

Scrivi tre conclusioni:

1. una sbagliata che confonde non-significativo con effetto zero;
2. una tecnicamente corretta;
3. una conclusione decisionale che consideri anche il valore potenziale dell'effetto e il costo di raccogliere nuovi dati.

### Esercizio 4 — Il segmento trovato dopo 120 tentativi

Un team prova 120 segmentazioni e trova un gruppo con `p = 0,009` e uplift del 14%.

Come cambia la tua interpretazione sapendo quante analisi sono state fatte? Quali dati useresti per confermare il segnale?

### Esercizio 5 — Type I e Type II come euro

Per un nuovo controllo antifrode, definisci:

- falso positivo;
- falso negativo;
- costo medio dei due errori;
- prevalenza della frode;
- volume mensile;
- quale errore vorresti ridurre maggiormente e perché.

Poi spiega perché questa decisione non può essere presa guardando soltanto accuracy o p-value.

### Esercizio 6 — Costruire il proprio Uncertainty Brief

Scegli una metrica del tuo dominio — conversion, churn, difetti, delivery SLA, NPS, forecast error o altro — e compila l'intero template del capitolo.

L'esercizio è riuscito se, alla fine, sai dire non soltanto:

> **“qual è il numero?”**

ma anche:

> **“quanto lo conosco bene, che cosa non è dentro quell'incertezza e quanto dovrebbe essere diverso per cambiare una decisione?”**
