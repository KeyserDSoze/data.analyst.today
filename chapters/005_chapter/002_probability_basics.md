## 5.1 Eventi, probabilità e frequenze

La probabilità parte da un'idea semplice: definire con chiarezza **che cosa può accadere**.

Un evento può essere:

- un cliente che rinnova;
- una transazione che viene rifiutata;
- un ordine che arriva in ritardo;
- un lead che converte;
- una macchina che si guasta entro trenta giorni;
- una campagna che raggiunge almeno il target minimo.

Il primo errore possibile è trattare l'evento in modo ambiguo.

“Cliente perso” può significare nessun acquisto negli ultimi 90 giorni, cancellazione formale dell'abbonamento, mancato rinnovo annuale o riduzione del contratto sotto una certa soglia.

Prima della probabilità viene quindi, ancora una volta, la definizione.

### Caso realistico: un antifrode che “blocca troppo”

Una fintech europea elabora circa 420.000 pagamenti con carta al giorno.

Il team risk osserva che lo 0,62% delle transazioni viene bloccato dal sistema antifrode.

La prima reazione del product team è negativa:

> “Stiamo bloccando più di 2.600 pagamenti al giorno. Dobbiamo abbassare la sensibilità.”

Il Data Analyst ricostruisce però il quadro completo.

Su 420.000 pagamenti:

- 2.604 vengono bloccati;
- 417.396 vengono autorizzati;
- tra i bloccati, 1.710 risultano effettivamente fraudolenti dopo verifica;
- tra gli autorizzati, circa 590 vengono successivamente classificati come frode.

La frequenza grezza dei blocchi dice poco.

Le domande giuste diventano:

- qual è la probabilità che una transazione bloccata sia realmente fraudolenta?
- qual è la probabilità di frode tra le transazioni lasciate passare?
- quanto costa un falso positivo?
- quanto costa un falso negativo?

Il linguaggio probabilistico trasforma un numero isolato in una struttura decisionale.

### Frequenza osservata e probabilità

Supponiamo di osservare 200.000 ordini e 14.000 resi.

La frequenza osservata dei resi è:

\[
\frac{14.000}{200.000}=0,07
\]

ovvero 7%.

Possiamo utilizzare quel 7% come stima della probabilità di reso di un ordine futuro solo se il contesto è sufficientemente comparabile.

Se metà degli ordini futuri appartiene a una nuova categoria con comportamento completamente diverso, il 7% storico può essere una stima molto debole.

La probabilità non vive separata dal processo che genera i dati.

### Complemento

Se la probabilità di un evento \(A\) è \(P(A)\), la probabilità che l'evento non si verifichi è:

\[
P(A^c)=1-P(A)
\]

Se la probabilità storica di rinnovo è 82%, la probabilità di mancato rinnovo è 18%.

La formula è banale. L'utilità pratica è meno banale.

Un'azienda può parlare per anni di “82% renewal rate” e non vedere immediatamente che sta perdendo quasi un cliente su cinque a ogni ciclo di rinnovo.

Il modo in cui formuliamo la stessa probabilità può cambiare la percezione del problema.

### Probabilità congiunta

Consideriamo due eventi:

- \(A\): il cliente utilizza il prodotto almeno quattro volte alla settimana;
- \(B\): il cliente rinnova.

Possiamo essere interessati alla probabilità che entrambi avvengano:

\[
P(A \cap B)
\]

Questa probabilità congiunta è particolarmente importante quando analizziamo comportamenti multipli.

Un SaaS potrebbe scoprire che:

- 46% dei clienti usa il prodotto almeno quattro volte a settimana;
- 78% rinnova;
- 42% utilizza il prodotto almeno quattro volte a settimana **e** rinnova.

Questi tre numeri raccontano cose diverse.

### Probabilità non significa certezza individuale

Se un modello assegna a un cliente una probabilità di churn del 70%, non significa che quel cliente “churnerà al 70%”.

Il cliente farà una cosa o l'altra.

Il 70% descrive la nostra incertezza o la frequenza attesa in una popolazione di casi comparabili.

Se prendessimo 10.000 clienti ai quali il modello assegna circa il 70% e il modello fosse ben calibrato, ci aspetteremmo approssimativamente 7.000 churn.

Questa interpretazione diventerà importante quando parleremo di modelli predittivi.

### Il principio operativo

Quando compare una probabilità in un'analisi, chiediamo sempre:

**Qual è l'evento? Qual è la popolazione? Qual è la finestra temporale? Quali condizioni stiamo assumendo stabili?**

Senza queste quattro informazioni, una probabilità rischia di essere solo un numero con il simbolo `%`.
