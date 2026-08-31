## 2.16 Quando l'analisi è inconcludente

Una stop rule deve prevedere anche un esito che molte culture aziendali trattano male:

> **non abbiamo abbastanza evidenza per sostenere una conclusione più forte.**

Non è necessariamente un fallimento dell'analista.

Può essere la conclusione corretta del brief.

### Perché un'analisi può non concludere

Tra le cause più comuni:

- campione troppo piccolo;
- dato troppo rumoroso;
- metrica o tracking non comparabili;
- variabile importante non osservata;
- gruppi troppo diversi per il confronto richiesto;
- periodo troppo breve;
- dati non ancora maturi;
- effetto plausibile ma troppo piccolo rispetto alla precisione disponibile;
- più spiegazioni rimangono compatibili con gli stessi pattern.

L'errore professionale non è incontrare uno di questi limiti. È nasconderlo dietro una storia più sicura di quanto i dati permettano.

### Tre affermazioni da non confondere

**1. Non abbiamo trovato evidenza di un effetto.**

Il test o l'analisi non hanno prodotto evidenza convincente.

**2. Abbiamo evidenza che un effetto materialmente rilevante è improbabile.**

Questa è una conclusione più forte e richiede dati sufficientemente informativi da escludere una parte importante degli effetti plausibili.

**3. I dati non distinguono tra presenza e assenza di un effetto rilevante.**

L'incertezza rimane troppo ampia.

La prima e la terza frase vengono spesso trasformate impropriamente in “non c'è effetto”.

### Un risultato inconcludente deve comunque produrre informazione

Una buona consegna dovrebbe spiegare:

- che cosa abbiamo verificato;
- che cosa mostrano i dati;
- quale conclusione non possiamo sostenere;
- perché;
- quale decisione può essere presa comunque;
- quale nuova informazione avrebbe il maggiore valore.

Per esempio:

> “Nei dati disponibili il flow B mostra retention a 30 giorni superiore di circa 3 punti percentuali, ma il campione è piccolo e l'intervallo compatibile con i dati include sia un effetto trascurabile sia un effetto materialmente utile. Non raccomandiamo un rollout globale sulla base di questa evidenza. Il prossimo passo con maggiore valore è estendere l'esperimento fino al campione pianificato mantenendo invariata la metrica primaria.”

Questa risposta è più utile di:

> “Non è emerso niente.”

### Anche “non agire” può essere una decisione

Se l'evidenza è insufficiente, le opzioni possono essere:

- raccogliere più dati;
- progettare un esperimento;
- migliorare la misurazione;
- usare un proxy con limiti espliciti;
- scegliere l'opzione più reversibile;
- non intervenire per ora.

L'assenza di una conclusione causale non impedisce sempre qualsiasi decisione. Cambia il livello di rischio con cui dobbiamo prenderla.

### Il link con il Value of Information

Quando l'analisi è inconcludente, la domanda successiva non dovrebbe essere automaticamente:

> “Come possiamo analizzare ancora?”

Meglio chiedere:

> **“Quale informazione aggiuntiva avrebbe la probabilità più alta di cambiare la decisione?”**

Forse serve più campione. Forse serve una fonte che oggi non esiste. Forse nessuna informazione aggiuntiva vale il costo perché le alternative portano comunque alla stessa scelta.

### AI e pressione a chiudere la storia

Un sistema generativo tende a produrre una risposta completa anche quando le evidenze rimangono ambigue.

Il Capitolo 0 ha fissato il principio di supervisione. In questo contesto la regola pratica è semplice: **non premiare la completezza narrativa più della completezza dell'evidenza**.

### Campo del brief/output

Per analisi ad alto rischio può essere utile pre-accettare tre possibili esiti:

```text
A. Evidenza sufficiente per raccomandare un'azione.
B. Evidenza sufficiente per escludere alcune azioni ma non scegliere tra le restanti.
C. Evidenza insufficiente: specificare il prossimo dato/test con maggiore Value of Information.
```

> **L'abilità professionale non consiste nell'avere sempre una risposta netta. Consiste nel sapere quale affermazione i dati hanno guadagnato il diritto di sostenere.**
