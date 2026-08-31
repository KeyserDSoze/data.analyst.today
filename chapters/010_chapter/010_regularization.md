## 10.10 Regularizzazione: accettare un po' di errore per ottenere più stabilità

Quando un modello diventa troppo complesso, una strategia comune consiste nel penalizzare la complessità stessa.

Questa idea prende il nome di **regularizzazione**.

In termini intuitivi, la regularizzazione dice al modello:

> non cercare di spiegare ogni minima oscillazione del training set; preferisci una soluzione un po' più semplice e più stabile.

### L1 e L2 senza trasformarle in formule decorative

Nella regressione, due approcci classici sono:

- **L2 / Ridge**: penalizza coefficienti molto grandi e tende a ridurli;
- **L1 / Lasso**: può portare alcuni coefficienti esattamente a zero, producendo una forma di selezione delle variabili.

L'obiettivo non è rendere il modello “più elegante”.

È migliorare la generalizzazione quando molte variabili rischiano di adattarsi troppo al campione disponibile.

### Caso simulato: BrightTel e 180 segnali di churn

BrightTel costruisce un modello per prevedere il churn dei clienti mobile.

Il dataset contiene 180 feature:

- utilizzo dati;
- chiamate al supporto;
- pagamenti in ritardo;
- variazioni di traffico;
- device;
- promozioni;
- rete;
- comportamenti digitali.

Una regressione logistica senza regularizzazione produce coefficienti enormi su alcune feature rare.

Per esempio, una variabile che identifica utenti con una specifica combinazione di device e promozione appare fortemente associata al churn, ma riguarda soltanto 73 clienti su 140.000.

Sul training set sembra informativa.

Nei mesi successivi quasi scompare.

Con una penalizzazione L2, i coefficienti estremi vengono ridotti e il modello diventa meno sensibile a queste coincidenze.

Con L1, alcune feature quasi ridondanti vengono eliminate.

Il risultato non è spettacolare sul training set:

| Modello | AUC training | AUC validation |
|---|---:|---:|
| non regolarizzato | 0,88 | 0,74 |
| Ridge | 0,83 | 0,77 |
| Lasso | 0,81 | 0,76 |

Il modello “peggiore” sul training set è migliore dove conta davvero.

### Regolarizzazione e interpretabilità

La regularizzazione può aiutare anche l'interpretabilità, ma non bisogna esagerare.

Un coefficiente portato a zero da Lasso non dimostra che la variabile sia causalmente irrilevante.

Significa soltanto che, **dato quel modello, quelle feature, quella penalizzazione e quel campione**, il modello può ottenere una buona soluzione senza usare quella variabile.

Se due feature sono molto correlate, il modello può conservarne una e ridurre l'altra quasi arbitrariamente.

### Il parametro di penalizzazione

Una penalizzazione troppo debole può lasciare il modello quasi invariato.

Una penalizzazione troppo forte può invece produrre underfitting.

Anche qui non esiste un valore “giusto” in assoluto.

Il parametro va scelto tramite validation o cross-validation.

### Metodo operativo

Usa la regularizzazione quando:

- hai molte feature rispetto alle osservazioni;
- esiste multicollinearità;
- i coefficienti sono instabili;
- il gap tra training e validation è elevato;
- vuoi una soluzione più parsimoniosa.

Ma ricordati che la regularizzazione non risolve:

- leakage;
- bias di selezione;
- target definito male;
- drift;
- assenza di segnale;
- causalità confusa con predizione.

È uno strumento per controllare la complessità, non una cura universale.