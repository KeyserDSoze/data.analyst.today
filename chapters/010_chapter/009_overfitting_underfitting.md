## 10.9 Overfitting e underfitting: quando il modello impara troppo o troppo poco

Un modello predittivo non deve semplicemente adattarsi bene ai dati che ha già visto. Deve riuscire a **generalizzare**.

Questa parola è centrale.

Un modello generalizza quando riesce a produrre previsioni utili anche su dati nuovi, provenienti dallo stesso tipo di processo reale ma non usati durante l'addestramento.

Due errori opposti possono impedirlo:

- **underfitting**: il modello è troppo semplice e non cattura pattern importanti;
- **overfitting**: il modello è troppo adattato ai dati di training e finisce per imparare anche rumore, coincidenze e dettagli non replicabili.

### Caso simulato: FalconCredit e il modello che sembrava perfetto

FalconCredit, società di credito al consumo, vuole stimare il rischio di insolvenza entro 90 giorni.

Il primo modello usa poche variabili:

- reddito dichiarato;
- rapporto rata/reddito;
- anzianità lavorativa;
- storico dei ritardi;
- importo richiesto.

Sul training set ottiene AUC 0,71 e sul test set 0,70.

Il data science team costruisce poi un modello molto più complesso con centinaia di feature, interazioni e variabili derivate.

Risultati:

| Modello | AUC training | AUC test |
|---|---:|---:|
| semplice | 0,71 | 0,70 |
| complesso | 0,94 | 0,73 |

La direzione iniziale del progetto interpreta il 0,94 come una prova di enorme progresso.

Ma quel numero misura soprattutto quanto bene il modello ricorda e ricostruisce il training set.

Il miglioramento reale su dati nuovi è molto più modesto: da 0,70 a 0,73.

Se un'ulteriore versione arrivasse a:

- AUC training 0,99;
- AUC test 0,68;

avremmo un segnale ancora più evidente di overfitting.

### Il gap train-validation

Un modo semplice per ragionare è confrontare performance su training e validation/test.

Un pattern tipico di overfitting è:

```text
training score      molto alto
validation score    significativamente più basso
```

Un pattern tipico di underfitting è invece:

```text
training score      basso
validation score    basso
```

Nel secondo caso il modello non riesce nemmeno a rappresentare bene il segnale disponibile nei dati di training.

### Bias e variance come intuizione

Il problema viene spesso descritto attraverso il compromesso tra **bias** e **variance**.

Un modello con alto bias tende a essere troppo rigido. Sbaglia sistematicamente perché rappresenta male la struttura reale.

Un modello con alta variance è invece troppo sensibile alle peculiarità del campione di training: piccole variazioni nei dati possono produrre modelli molto diversi.

Non serve trasformare il Data Analyst in un teorico del machine learning per usare bene questa idea.

La domanda operativa è:

> il modello sta imparando un pattern stabile o sta imparando la storia particolare del dataset che gli abbiamo dato?

### Un errore frequente: premiare la complessità

In molti progetti esiste una pressione implicita verso modelli più sofisticati.

Un modello con 300 feature, gradient boosting e tuning esteso sembra più avanzato di una regressione logistica con 18 variabili.

Ma sofisticazione tecnica e valore operativo non sono sinonimi.

Se il modello semplice:

- generalizza quasi altrettanto bene;
- è più stabile;
- è più interpretabile;
- richiede meno dati;
- costa meno da mantenere;
- è più facile da monitorare;

può essere la scelta migliore.

### Caso pubblico documentato: l'esempio di scikit-learn

La documentazione ufficiale di scikit-learn mostra un esempio didattico in cui modelli polinomiali di complessità crescente vengono usati per approssimare una funzione non lineare.

Il modello troppo semplice produce underfitting. Un modello di complessità intermedia approssima bene il pattern. Un modello troppo complesso si adatta quasi perfettamente ai dati osservati ma generalizza peggio.

L'esempio viene valutato tramite cross-validation proprio per mostrare la differenza tra adattamento al training set e capacità di generalizzare.

Fonte: https://scikit-learn.org/stable/auto_examples/model_selection/plot_underfitting_overfitting.html

### Metodo operativo

Quando confronti modelli diversi, non guardare soltanto la metrica migliore ottenuta sul training set.

Controlla almeno:

1. performance su validation/test;
2. differenza train-validation;
3. stabilità tra fold o periodi temporali;
4. sensibilità a piccole variazioni dei dati;
5. complessità necessaria per ottenere il miglioramento;
6. costo di manutenzione del modello.

Il modello migliore non è quello che racconta meglio il passato.

È quello che mantiene utilità quando incontra il futuro.