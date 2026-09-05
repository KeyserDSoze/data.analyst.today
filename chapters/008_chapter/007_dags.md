## 8.6 DAG: disegnare le assunzioni prima di scrivere la regressione

Un **Directed Acyclic Graph (DAG)** non serve principalmente a rendere elegante una presentazione. Serve a rendere visibili le ipotesi causali che altrimenti resterebbero nascoste dentro una selezione di feature o una formula di regressione.

Harvard CAUSALab usa una formulazione efficace già nel titolo di uno dei suoi materiali didattici: **“Draw Your Assumptions Before Your Conclusions”**.[^causalab-dag] È esattamente il ruolo che il DAG ha per un Data Analyst: costringerci a dire quali relazioni riteniamo plausibili prima che il modello produca un coefficiente.

### Caso simulato/composito — Campagna di reactivation

Una subscription app vuole stimare l'effetto di una campagna email sul ritorno degli utenti inattivi. Tra le variabili disponibili ci sono engagement pre-campagna, eleggibilità, email ricevuta, apertura, ritorno nell'app e churn successivo. Un modello causale plausibile è:

```text
engagement_pre -> email
engagement_pre -> ritorno
email -> apertura -> ritorno -> churn
email -----------------> ritorno
```

Il disegno chiarisce immediatamente due ruoli che in una tabella potrebbero sembrare simili. `engagement_pre` precede il trattamento e può aprire un backdoor path tra email e ritorno; `apertura` avviene dopo l'invio ed è un possibile **mediatore**. Se vogliamo l'effetto totale dell'invio, controllare automaticamente per `open_email` può eliminare parte del meccanismo che stiamo cercando di misurare.

Questo è il motivo per cui, nella causal inference, la feature selection non può essere lasciata interamente a una procedura predittiva. La domanda non è “quali variabili aiutano a prevedere `Y`?”, ma “quali variabili devo condizionare — e quali devo evitare — per identificare l'effetto definito?”.

Tre strutture ricorrono continuamente:

```text
Confondente:  Z -> T
               Z -> Y

Mediatore:    T -> M -> Y

Collider:     T -> C <- U -> Y
```

Un confondente pre-treatment può richiedere adjustment; un mediatore può essere parte dell'effetto totale; un collider può creare bias se lo condizioniamo. Tutti e tre possono risultare “correlati con treatment e outcome” in un dataset. È il causal model a distinguerli.

### Dal totale al meccanismo

Supponiamo che un'azienda voglia stimare l'effetto di un training commerciale sul revenue trimestrale:

```text
training -> chiamate -> demo -> pipeline -> revenue
     \-----------------------------------> revenue
```

Se la domanda è “qual è l'effetto totale del training?”, controllare per chiamate, demo e pipeline rischia di bloccare una parte dell'effetto stesso. Se invece chiediamo “quanto dell'effetto passa attraverso la pipeline?”, stiamo formulando un problema di mediazione e introduciamo assunzioni ulteriori. La variabile corretta da controllare dipende quindi dall'**estimand**, non da una regola universale.

Un DAG utile deve contenere anche ciò che non misuriamo. Se una motivazione non osservata influenza sia l'adesione al training sia il revenue, possiamo rappresentarla come `U_motivazione`. Il fatto che non esista nel warehouse non la rende causalmente irrilevante; al contrario, il grafo rende visibile perché una strategia puramente osservazionale potrebbe non identificare l'effetto.

Il DAG non dimostra che le frecce siano vere. È un modello del mondo e può essere contestato. Questo è un vantaggio: analyst e domain expert possono discutere quali relazioni mancano, distinguere conoscenza forte da ipotesi debole e verificare se modelli alternativi richiedono adjustment set diversi. L'assunzione, una volta disegnata, diventa criticabile.

Il tempo rimane parte del grafo. Quando il processo è dinamico può essere utile espanderlo:

```text
usage_t-1 -> treatment_t -> usage_t+1 -> outcome_t+2
     \-------------------------------> outcome_t+2
```

Una variabile misurata dopo il trattamento non diventa un confondente preesistente soltanto perché compare come colonna numerica.

Nel **Causal Identification Brief** il DAG può restare semplice, ma prima di una causal claim seria dovremmo poter dichiarare quali cause comuni aprono backdoor path, quali variabili sono mediatori, dove possono esserci collider, quali cause importanti non sono osservate, quali misure sono post-treatment e se esistono spillover tra unità.

> **Il DAG non rende vere le assunzioni. Le rende visibili, e questo è già un enorme miglioramento rispetto a lasciarle implicite nel codice.**

[^causalab-dag]: Harvard T.H. Chan School of Public Health, CAUSALab, materiali e corsi su causal diagrams e confounding adjustment: https://hsph.harvard.edu/research/causalab/onlinecourses/
