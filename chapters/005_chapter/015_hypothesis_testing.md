## 5.14 Test di ipotesi: quanto sono compatibili i dati con uno scenario di riferimento?

Un test di ipotesi non è una macchina che decide se un'affermazione è vera o falsa.

È un modo formale per porre una domanda più circoscritta:

> **Se uno specifico scenario di riferimento e le assunzioni del modello fossero adeguati, quanto sarebbe sorprendente osservare dati come quelli che abbiamo raccolto?**

L'**ipotesi nulla**, `H0`, rappresenta lo scenario rispetto al quale costruiamo il test. Spesso è “nessuna differenza” o “parametro uguale alla baseline”, ma non deve essere scelta meccanicamente.

L'**ipotesi alternativa**, `H1`, rappresenta l'insieme degli scenari alternativi considerati dal test.

Il punto importante è che il test valuta i dati **dentro un modello statistico**. Non certifica da solo:

- che il disegno dell'analisi sia corretto;
- che il campione sia rappresentativo;
- che una differenza sia causale;
- che l'effetto sia abbastanza grande da contare.

### Caso simulato/composito — Il livello di servizio è davvero sotto target?

Un'azienda B2B ha un impegno operativo: almeno il **90% dei ticket Priority 1** deve ricevere una prima risposta entro 30 minuti.

In un campione probabilistico di 1.200 ticket comparabili, 1.062 rispettano lo SLA.

La proporzione osservata è:

`1.062 / 1.200 = 88,5%`.

Il numero è sotto il target. La domanda inferenziale è:

> **La differenza osservata è abbastanza grande, rispetto alla variabilità campionaria, da essere difficilmente compatibile con un processo che soddisfa davvero il 90%?**

Una possibile formulazione è:

- `H0`: la proporzione di ticket entro SLA è almeno compatibile con il riferimento del 90%;
- `H1`: la proporzione è inferiore al riferimento.

Il test non dimostra che “il processo è definitivamente 88,5%”. E non spiega perché il livello di servizio sia peggiorato.

Quantifica soltanto un pezzo dell'evidenza rispetto allo scenario specificato.

### Prima del test vengono effetto, popolazione e disegno

Una sequenza debole è:

**dati → scegli test → guarda p-value → inventa interpretazione**.

Una sequenza più professionale è:

**domanda → popolazione → parametro/effetto → disegno → assunzioni → stima + intervallo → test → interpretazione**.

Prima del test dobbiamo sapere almeno:

- qual è il parametro o confronto di interesse;
- qual è la popolazione alla quale vogliamo generalizzare;
- quale differenza avrebbe valore pratico;
- come sono state generate le osservazioni;
- quali assunzioni statistiche sono richieste.

Altrimenti rischiamo di ottenere una risposta molto precisa a una domanda che non avevamo intenzione di porre.

### `H0 = nessun effetto` non è sempre la domanda utile

Immaginiamo che un nuovo processo riduca il tempo di gestione medio di **12 secondi** su ticket che durano mediamente 18 minuti.

Con abbastanza dati possiamo forse distinguere 12 secondi da zero.

Ma se il business considera interessante soltanto una riduzione di almeno 90 secondi, la vera domanda non è:

> “l'effetto è esattamente zero?”

È più vicina a:

> **“i dati sono compatibili con un miglioramento abbastanza grande da avere valore operativo?”**

Questa prospettiva ci porta a guardare effect size e intervalli, non soltanto un null puntuale.

### Un risultato non significativo non accetta automaticamente `H0`

Nel linguaggio classico del testing diciamo spesso:

> “non rifiutiamo `H0`”.

Non è equivalente a:

> “abbiamo dimostrato che `H0` è vera”.

I dati possono essere poco informativi. Il campione può essere piccolo. L'effetto reale può essere presente ma difficile da rilevare.

La sezione sul power renderà questo punto operativo.

### Il test non ripara il disegno

Supponiamo di confrontare due gruppi osservazionali con migliaia di casi e ottenere un p-value minuscolo.

Se i gruppi differiscono sistematicamente per paese, canale, tenure o rischio iniziale, il test può quantificare con grande precisione **una differenza osservata tra gruppi non comparabili**.

Non trasforma automaticamente quella differenza in effetto causale.

Per questo:

- Capitolo 8: identificazione causale;
- Capitolo 9: randomizzazione ed experimentation;
- Capitolo 5: inferenza statistica data una struttura di confronto dichiarata.

### L'output corretto non è “PASS/FAIL”

Dopo un test dovremmo conservare almeno:

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

Il test diventa così **un componente dell'evidenza**, non il timbro finale della decisione.

> **Il test chiede quanto i dati siano compatibili con un modello di riferimento. Non chiede al software di decidere che cosa dobbiamo credere o fare.**
