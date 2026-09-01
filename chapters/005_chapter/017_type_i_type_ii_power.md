## 5.16 Errori di tipo I, tipo II e power: progettare quanta evidenza ci serve

Ogni procedura inferenziale può portare a una conclusione sbagliata.

La statistica non elimina questo rischio. Lo rende esplicito e, almeno in parte, progettuale.

Nel linguaggio classico del testing:

- **errore di tipo I:** rifiutiamo `H0` quando lo scenario nullo è vero;
- **errore di tipo II:** non rifiutiamo `H0` quando esiste l'effetto considerato nell'alternativa.

Nel lavoro dell'analista questi errori diventano più comprensibili se li traduciamo in decisioni.

### Caso simulato/composito — Un nuovo processo di picking

Una rete logistica valuta un nuovo sistema di picking che promette di ridurre gli errori di preparazione.

Il rollout nazionale richiede:

- nuovi scanner;
- formazione;
- modifica dei processi;
- circa 4 milioni di euro di investimento.

**Falso positivo / tipo I:** concludiamo che il nuovo processo produce un beneficio quando il segnale osservato era compatibile con il rumore. Investiamo milioni senza ottenere il miglioramento atteso.

**Falso negativo / tipo II:** concludiamo che non c'è evidenza sufficiente di beneficio quando il processo riduce davvero gli errori abbastanza da generare valore. Rinunciamo a un'opportunità reale.

I due costi non sono necessariamente uguali.

Per questo `α = 0,05` e `power = 80%` non dovrebbero essere trattati come numeri rituali scollegati dal contesto.

### Alpha controlla un rischio sotto il modello, non il costo economico

Nel quadro frequentista, `α` è il tasso di errore di tipo I che il procedimento è progettato a controllare sotto determinate assunzioni.

Ridurre `α` rende più difficile dichiarare evidenza contro `H0`, ma può anche aumentare il rischio di non rilevare effetti reali se non aumentiamo l'informazione disponibile.

NIST sottolinea proprio il trade-off tra errori di tipo I e II: non possiamo spingerli entrambi arbitrariamente verso zero senza modificare campione, disegno o altre proprietà del test.[^nist-errors]

Quindi la domanda non è:

> “Perché usiamo il 5%?”

ma:

> **“Quanto costerebbe un falso positivo in questa decisione, e quanta evidenza vogliamo pretendere prima di agire?”**

### Power: probabilità di rilevare un effetto specifico

La **potenza statistica** non è una proprietà generica del test del tipo “questo esperimento ha power 80%”.

È la probabilità, sotto un effetto specificato e le altre assunzioni del disegno, che la procedura produca il risultato decisionale previsto contro `H0`.

Dipende da:

- dimensione dell'effetto;
- numerosità effettiva;
- variabilità;
- livello `α`;
- struttura del test e del disegno.

Più piccolo è l'effetto che vogliamo rilevare, più informazione serve in genere.

### Caso simulato/composito — “Il test non ha funzionato”

Un prodotto digitale parte da conversione 3,0%. Il business considera interessante un miglioramento di almeno **+0,15 punti percentuali**, fino a 3,15%.

Dopo pochi giorni osserva:

- controllo: 3,01%;
- variante: 3,19%;
- 8.000 utenti per gruppo.

Il risultato non supera la soglia inferenziale predefinita.

Il product manager conclude:

> “La variante non funziona.”

Ma l'esperimento era stato avviato senza una vera pianificazione della potenza e il campione era molto più piccolo di quello necessario per distinguere con affidabilità un delta dell'ordine di +0,15 pp.

Il risultato corretto è:

> **“Il test corrente non ha abbastanza informazione per discriminare bene l'effetto business-rilevante che avevamo in mente.”**

Non è la stessa cosa di dimostrare effetto zero.

### Minimum Effect of Interest prima della sample size

La power analysis parte da una domanda business:

> **Qual è il più piccolo effetto che cambierebbe davvero la nostra decisione?**

Solo dopo ha senso chiedere quanti casi servono.

Se il business non implementerebbe mai per un miglioramento inferiore a +0,5 pp, progettare il test per trovare con grande precisione +0,05 pp può essere uno spreco di traffico e tempo.

Il Capitolo 9 userà questa idea nella progettazione degli A/B test, con MDE, durata, unità di randomizzazione, guardrail e stopping rules.

### “Non significativo” può voler dire cose diverse

Un risultato non significativo può essere compatibile con:

- effetto realmente vicino a zero;
- effetto positivo ma piccolo;
- effetto materialmente interessante ma stima troppo rumorosa;
- effetto eterogeneo che si cancella nell'aggregato;
- disegno poco efficiente.

Per distinguerli servono soprattutto:

- effect size;
- confidence interval;
- power rispetto agli effetti che contano;
- contesto del disegno.

### Una matrice decisionale più utile di `significant / not significant`

| Evidenza | Effetto business-rilevante plausibile? | Lettura |
|---|---|---|
| Precisa e vicino a zero | No | Evidenza utile di effetto trascurabile |
| Imprecisa e vicino a zero | Sì | Inconclusivo: serve più informazione |
| Precisa e materialmente positivo | Sì | Evidenza forte da portare alla decisione |
| Imprecisa ma molto positivo | Sì | Segnale interessante, ancora incerto |

La statistica diventa più utile quando smette di produrre una sola etichetta.

> **Power non serve a garantire che troveremo un risultato significativo. Serve a evitare di fare una domanda importante con uno strumento troppo debole per risponderle.**

[^nist-errors]: NIST, *Comparing Instruments*, Technical Note 2106: https://nvlpubs.nist.gov/nistpubs/TechnicalNotes/NIST.TN.2106.pdf
