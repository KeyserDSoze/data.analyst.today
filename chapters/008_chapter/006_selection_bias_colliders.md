## 8.5 Selection bias e collider: quando il campione costruisce una relazione

Un dataset può essere perfettamente pulito e rappresentare comunque male la relazione causale che ci interessa. Il bias può nascere prima dell'analisi, nel processo che decide chi viene registrato, chi rimane osservabile e quali righe superano i filtri finali.

### Caso simulato/composito — I migliori venditori sembrano usare meno il CRM

Un'azienda B2B analizza soltanto le opportunità arrivate alla fase finale della pipeline. All'interno di quel campione, i commerciali con meno attività registrate nel CRM mostrano un win rate più alto. La conclusione “documentare troppe attività riduce la performance” sembra compatibile con i dati, ma ignora il meccanismo di selezione.

L'arrivo alla fase finale è favorito sia dalla qualità iniziale del lead sia dall'intensità commerciale:

```text
qualità lead --------> fase finale <-------- intensità commerciale
```

`fase finale` è un **collider**. Condizionando sul fatto che un'opportunità abbia raggiunto quella fase possiamo creare un'associazione tra qualità del lead e intensità commerciale che nella popolazione originaria non esisteva nello stesso modo. Per questo “controllare una variabile importante” non è sempre prudente: se la variabile è un collider, l'adjustment può aprire proprio il percorso non causale che volevamo evitare.

Lo stesso problema compare nelle survey. Se risponde solo il **18%** dei clienti e la probabilità di risposta aumenta sia tra utenti molto coinvolti sia tra utenti estremamente insoddisfatti, un'analisi dei soli rispondenti può mostrare relazioni che dipendono dal meccanismo di risposta. Il problema non è semplicemente il response rate basso; è **da che cosa dipende la probabilità di entrare nel campione**.

### Survivorship bias e code che spariscono

Una forma frequente di selection bias consiste nell'osservare solo chi rimane abbastanza a lungo da essere misurato. Succede quando studiamo retention dei soli clienti ancora attivi, produttività dei dipendenti rimasti, performance degli SKU sopravvissuti a una razionalizzazione o tempi di consegna dei soli ordini effettivamente consegnati.

Consideriamo un marketplace che confronta i tempi medi dei soli ordini consegnati entro 30 giorni: **2,8 giorni** per il corriere nuovo contro **3,4 giorni** per quello storico. Il nuovo corriere sembra migliore finché non scopriamo che ha molti più ordini non consegnati entro 30 giorni, esclusi dalla tabella. Il filtro ha rimosso proprio parte della coda negativa che dovrebbe pesare nella decisione.

La selezione diventa ancora più delicata quando il trattamento influenza la probabilità di restare osservabili:

```text
trattamento -> sopravvivenza nel campione <- severità iniziale
```

Perfino dopo una randomizzazione, analizzare soltanto i sopravvissuti o eliminare unità post-treatment può rompere la comparabilità iniziale.

### La tabella è l'ultimo passaggio di un funnel

Prima di aprire il notebook conviene chiedere:

> **Quale processo deve attraversare un'unità per comparire in questa tabella?**

Una rappresentazione semplice è:

```text
popolazione target
    ↓
eleggibile
    ↓
registrata nel sistema
    ↓
ha outcome osservabile
    ↓
passa i filtri analitici
    ↓
campione finale
```

A ogni passaggio dobbiamo chiederci se la selezione dipende dal trattamento, dall'outcome o da cause dell'uno e dell'altro. La scheda operativa minima resta volutamente strutturata:

```text
Popolazione target:
Popolazione realmente osservabile:
Filtri prima dell'analisi:
Filtri dopo il trattamento:
Chi manca?
Perché manca?
La probabilità di essere osservato dipende da trattamento/outcome?
Quale conclusione cambierebbe includendo gli esclusi?
```

Hernán e Robins trattano la selection bias come un problema strutturale del causal model: condizionare su variabili generate da cause multiple, incluse conseguenze del trattamento, può introdurre associazioni che non rappresentano l'effetto desiderato.[^whatif-selection]

> **La tabella finale non è la popolazione. È il risultato di un processo di selezione che deve entrare nel ragionamento causale.**

A questo punto serve un modo per rendere esplicite tutte queste ipotesi — cause comuni, mediatori, collider, variabili non osservate e timing. È il ruolo dei DAG.

[^whatif-selection]: Hernán, M.A. & Robins, J.M., *Causal Inference: What If*, capitoli su confounding e selection bias: https://www.hsph.harvard.edu/miguel-hernan/wp-content/uploads/sites/1268/2024/04/hernanrobins_WhatIf_26apr24.pdf
