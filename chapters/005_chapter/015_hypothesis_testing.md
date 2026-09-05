## 5.14 Test di ipotesi: confrontare i dati con uno scenario di riferimento

Un test di ipotesi non decide se una frase sul mondo è vera o falsa. Costruisce una domanda più stretta:

> **Se uno specifico scenario di riferimento e le assunzioni del modello fossero adeguati, quanto sono compatibili con essi i dati che abbiamo osservato?**

L'**ipotesi nulla**, `H0`, definisce lo scenario rispetto al quale costruiamo il test. L'**ipotesi alternativa**, `H1`, descrive ciò che il procedimento considera in opposizione a quello scenario. Spesso `H0` assume “nessuna differenza”, ma questa scelta non deve diventare rituale: il riferimento utile dipende dalla domanda.

NIST descrive i test come procedure che usano dati campionari per valutare un'affermazione su un parametro e ricorda un punto importante: **non rifiutare** un'ipotesi non equivale a dimostrarla vera.[^nist-tests]

## Un livello di servizio sotto target

Un'azienda B2B promette che almeno il **90% dei ticket Priority 1** riceva una prima risposta entro 30 minuti. In un campione probabilistico di 1.200 ticket comparabili, 1.062 rispettano lo SLA:

`1.062 / 1.200 = 88,5%`.

La stima puntuale è sotto il target. La domanda inferenziale è se uno scarto di questa dimensione sia plausibile come sola variabilità campionaria per un processo realmente compatibile con il 90%.

Possiamo quindi formulare un test con uno scenario nullo coerente con il riferimento del 90% e un'alternativa che rappresenti una performance inferiore. Il risultato del test non ci dirà **perché** lo SLA sia peggiorato e non stabilirà che il processo “è definitivamente 88,5%”. Quantificherà soltanto quanto il campione sia compatibile con il riferimento sotto le assunzioni dichiarate.

Questa differenza è fondamentale perché impedisce al test di assumersi responsabilità che appartengono al disegno e al contesto.

## Il test arriva dopo la domanda, non prima

Una sequenza debole è:

**dati → scegli un test → guarda il p-value → costruisci la storia**.

Una sequenza più difendibile è:

**domanda → popolazione → parametro/effetto → disegno → assunzioni → stima e intervallo → test → interpretazione**.

Prima di calcolare la statistica dobbiamo sapere a quale popolazione vogliamo generalizzare, quale effetto ci interessa, come sono state generate le osservazioni e quale differenza sarebbe abbastanza grande da contare. Altrimenti il software può produrre una risposta molto precisa a una domanda che il business non aveva mai posto.

## Lo zero statistico non è sempre la soglia decisionale

Immaginiamo che un nuovo processo riduca il tempo medio di gestione di **12 secondi** su ticket che durano circa 18 minuti. Con un dataset enorme potremmo distinguere 12 secondi da un effetto esattamente nullo.

Se il business implementerebbe il processo soltanto per un miglioramento di almeno 90 secondi, però, il confronto con zero non è il problema principale. La domanda utile è più vicina a:

> **I dati sono compatibili con un miglioramento abbastanza grande da cambiare la decisione?**

Questa prospettiva sposta naturalmente l'attenzione verso effect size, intervalli e soglie business. Il test resta utile, ma smette di essere il centro esclusivo dell'analisi.

## “Non significativo” non significa “nessun effetto”

Se un test non produce evidenza sufficiente contro `H0`, possono esistere spiegazioni molto diverse. L'effetto reale può essere vicino a zero; può essere piccolo; può essere materialmente interessante ma stimato con poca precisione; il disegno può essere inefficiente. Per questo “non rifiutiamo `H0`” non va tradotto in “abbiamo dimostrato che non esiste effetto”.

La sezione sul power renderà questa distinzione operativa: un test poco informativo non deve diventare una sentenza negativa sul fenomeno.

## Il test non ripara gruppi non comparabili

Un p-value minuscolo ottenuto confrontando due gruppi osservazionali con migliaia di casi può descrivere con grande precisione **una differenza tra gruppi sistematicamente diversi**. Se cambiano paese, canale, tenure o rischio iniziale, il test non trasforma automaticamente quella differenza in effetto causale.

Questo mantiene chiari i confini del libro: il Capitolo 5 tratta l'inferenza statistica dentro una struttura di confronto dichiarata; il Capitolo 8 affronterà l'identificazione causale; il Capitolo 9 randomizzazione ed experimentation.

Per questo l'output di un test non dovrebbe essere una cella `PASS / FAIL`, ma un piccolo fascicolo di evidenza:

```text
Parametro / effetto stimato:
Intervallo di confidenza:
Scenario H0:
Statistica / p-value:
Assunzioni importanti:
Dimensione campionaria effettiva:
Effetto minimo business-rilevante:
Fonti di bias non incluse nel test:
```

Il test diventa così ciò che dovrebbe essere: **un componente dell'evidenza, non il timbro finale della decisione**.

> **Un test chiede quanto i dati siano compatibili con uno scenario di riferimento. Non delega al software ciò che dobbiamo credere o fare.**

---

### Fonte

[^nist-tests]: NIST/SEMATECH, *Quantitative Techniques — Hypothesis Tests*. https://itl.nist.gov/div898/handbook/eda/section3/eda35.htm
