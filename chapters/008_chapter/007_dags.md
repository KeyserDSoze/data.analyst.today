## 8.6 DAG: disegnare il problema prima di stimarlo

Un Directed Acyclic Graph, o DAG, è un grafo orientato che rappresenta ipotesi causali tra variabili.

Non serve essere causal scientist per usarlo bene. Per un Data Analyst può diventare soprattutto uno strumento di disciplina mentale.

### Caso - La campagna di reactivation

Un'app subscription vuole misurare l'effetto di una campagna email sul ritorno degli utenti inattivi.

Le variabili principali sono:

- engagement precedente;
- probabilità di ricevere la campagna;
- apertura dell'email;
- ritorno nell'app;
- churn futuro.

Un primo DAG intuitivo potrebbe essere:

```text
engagement_precedente -> campagna
engagement_precedente -> ritorno
campagna -> apertura -> ritorno -> churn
```

Già questo schema fa emergere due questioni.

Primo: l'engagement precedente è un possibile confondente del rapporto tra campagna e ritorno.

Secondo: l'apertura dell'email è una conseguenza della campagna. Se vogliamo stimare l'effetto totale della campagna sul ritorno, controllare per apertura può essere sbagliato perché bloccherebbe parte del meccanismo attraverso cui la campagna produce effetto.

### Variabili pre-trattamento e post-trattamento

Questa distinzione è fondamentale.

Le variabili pre-trattamento descrivono il mondo prima dell'intervento. Possono aiutarci a rendere i gruppi comparabili.

Le variabili post-trattamento possono invece essere:

- mediatori dell'effetto;
- conseguenze indirette;
- segnali generati dall'intervento.

Inserirle automaticamente come controlli può cambiare la domanda causale che stiamo stimando.

### Caso - Formazione commerciale

Un'azienda vuole misurare l'effetto di un corso di vendita sul revenue trimestrale.

Dopo il corso misura anche:

- numero di chiamate;
- numero di demo;
- pipeline creata.

Queste variabili sono probabilmente parte del meccanismo:

```text
training -> più chiamate -> più demo -> più pipeline -> revenue
```

Se una regressione "controlla" per chiamate, demo e pipeline, rischia di rimuovere proprio i canali attraverso cui il corso potrebbe funzionare.

### Il DAG non dimostra che le frecce siano vere

Un DAG è una rappresentazione delle nostre assunzioni, non una prova empirica.

Il suo valore è rendere esplicite ipotesi che altrimenti rimarrebbero nascoste nel codice.

Due analyst possono costruire DAG diversi. Questa non è una debolezza: rende visibile il disaccordo sul processo causale e permette di discuterlo con domain expert.

### Una procedura semplice

Prima di una stima causale:

1. identifica trattamento e outcome;
2. elenca le cause plausibili del trattamento;
3. elenca le cause plausibili dell'outcome;
4. collega le variabili con frecce temporaneamente e causalmente plausibili;
5. separa ciò che avviene prima e dopo il trattamento;
6. chiedi quali percorsi creano associazione non causale;
7. decidi quali variabili controllare sulla base del problema, non solo della disponibilità nel database.

> **Un buon DAG non rende semplice la causalità. Rende visibili le assunzioni che altrimenti il modello nasconderebbe.**

## Riferimenti

- Guido W. Imbens, *Potential Outcome and Directed Acyclic Graph Approaches to Causality: Relevance for Empirical Practice in Economics*.
