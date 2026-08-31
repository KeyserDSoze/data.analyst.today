## 10.11 Cross-validation: non fidarsi di un solo split

Un singolo train/test split può essere utile, ma può anche raccontare una storia troppo dipendente da come sono cadute le osservazioni nei due insiemi.

La **cross-validation** nasce per stimare in modo più robusto la capacità di generalizzazione del modello.

L'idea classica è dividere il dataset in più parti, dette fold. Il modello viene addestrato su alcuni fold e validato su quello rimanente, ripetendo il processo più volte.

### Caso simulato: MedSupply e il modello instabile

MedSupply vuole prevedere quali ordini ospedalieri subiranno ritardi superiori a 48 ore.

Il primo modello viene valutato con un solo split casuale e ottiene AUC 0,82.

Sembra ottimo.

Il team ripete però la validazione su cinque fold:

| Fold | AUC |
|---|---:|
| 1 | 0,83 |
| 2 | 0,81 |
| 3 | 0,74 |
| 4 | 0,79 |
| 5 | 0,72 |

Media: 0,778.

La domanda interessante non è più soltanto “qual è l'AUC media?”.

Diventa:

> perché il modello crolla in alcuni fold?

L'analisi mostra che due fold contengono molte più consegne internazionali, un processo operativo diverso rispetto alle spedizioni domestiche.

La cross-validation non ha solo fornito una stima più prudente. Ha fatto emergere un problema di **eterogeneità del processo**.

### Cross-validation e tempo

Con dati temporali, il classico k-fold casuale può essere scorretto.

Se stai prevedendo il futuro, non dovresti addestrare il modello usando dati successivi al periodo che stai simulando come validation.

Un approccio più realistico può essere:

```text
train: gennaio-giugno   validate: luglio
train: gennaio-luglio   validate: agosto
train: gennaio-agosto   validate: settembre
```

Questo tipo di valutazione rispetta la direzione temporale.

### Caso simulato: Finora e il backtest troppo ottimista

Finora costruisce un modello di default.

Con cross-validation casuale ottiene AUC 0,86.

Con split temporale:

- training 2024, test Q1 2025: 0,81;
- training fino a Q1 2025, test Q2 2025: 0,78;
- training fino a Q2 2025, test Q3 2025: 0,75.

Nel frattempo la composizione dei clienti e le politiche di credito sono cambiate.

La random cross-validation mescolava vecchi e nuovi regimi e nascondeva il deterioramento.

### Cross-validation non sostituisce il test finale

Se usi la cross-validation per scegliere modello, feature e iperparametri, quella procedura è parte del processo di sviluppo.

È quindi utile mantenere comunque un test set finale non toccato, quando il contesto lo consente.

### Caso pubblico documentato: learning e validation curves in scikit-learn

La documentazione ufficiale di scikit-learn mostra come confrontare training score e validation score per diagnosticare underfitting e overfitting. Un training score elevato con validation score molto più basso indica alta variance; due score entrambi bassi indicano invece alto bias.

Fonte: https://scikit-learn.org/stable/modules/learning_curve.html

### Metodo operativo

Prima di scegliere una strategia di validation, chiediti:

1. qual è l'unità indipendente reale?
2. ci sono gruppi che non devono essere spezzati tra train e test?
3. esiste una dimensione temporale?
4. il modello verrà applicato a clienti, mercati o periodi nuovi?
5. la validation simula davvero il deployment?

La validazione migliore non è quella statisticamente più sofisticata.

È quella che assomiglia di più al futuro che il modello dovrà affrontare.