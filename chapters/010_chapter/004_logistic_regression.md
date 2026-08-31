## 10.4 Regressione logistica: stimare una probabilità, non solo una classe

Quando il target è binario — churn sì/no, frode sì/no, conversione sì/no, default sì/no — una delle baseline più utili è la regressione logistica.

La regressione logistica non predice direttamente una classe. Stima una probabilità tra 0 e 1, che può poi essere trasformata in una decisione tramite una soglia.

La funzione logistica è:

\[
p(y=1|x)=\frac{1}{1+e^{-z}}
\]

con:

\[
z = \beta_0 + \beta_1x_1 + \dots + \beta_px_p
\]

Scikit-learn implementa la regressione logistica come classificatore regolarizzato e supporta diverse penalizzazioni e solver.

Fonte: https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html

### Caso realistico: AtlasTel e il churn a 60 giorni

AtlasTel offre servizi internet a piccole imprese. Vuole identificare ogni lunedì i clienti con maggiore rischio di churn nei successivi 60 giorni.

Il dataset storico contiene:

- anzianità del cliente;
- fatture insolute negli ultimi 90 giorni;
- variazione del traffico dati;
- ticket tecnici;
- outage sperimentati;
- variazione del prezzo;
- numero di chiamate al supporto;
- utilizzo del portale self-service;
- churn entro 60 giorni.

Il modello produce probabilità come:

| Cliente | Probabilità stimata di churn |
|---|---:|
| A | 0,08 |
| B | 0,23 |
| C | 0,64 |
| D | 0,81 |

La domanda operativa non è ancora risolta.

Chi contattiamo?

Se il team Customer Success può chiamare 2.000 clienti a settimana, la soglia deve riflettere capacità, costo, valore cliente ed efficacia dell'intervento.

### Odds e coefficienti

La regressione logistica è lineare nei log-odds:

\[
\log\left(\frac{p}{1-p}\right)=\beta_0+\beta_1x_1+\dots
\]

Esponenziando un coefficiente otteniamo un odds ratio.

Se `exp(β)=1,5`, un aumento di un'unità della feature è associato a odds del risultato circa 1,5 volte maggiori, a parità delle altre variabili.

Attenzione: odds e probabilità non sono la stessa cosa.

Passare dal 10% al 15% di probabilità non equivale allo stesso cambiamento in odds del passaggio dal 50% al 55%.

### Caso AtlasTel: un coefficiente che inganna

Nel primo modello, `numero_chiamate_supporto` ha un coefficiente positivo molto forte.

Il management propone:

> “Dobbiamo ridurre le chiamate al supporto.”

È la conclusione sbagliata.

Le chiamate sono un **segnale** di problemi tecnici e amministrativi. Impedire al cliente di chiamare non risolve la causa sottostante.

Il modello è predittivo. Non è un manuale causale degli interventi.

### Dalla probabilità alla decisione

Una probabilità stimata può alimentare diverse policy:

- top 5% dei clienti più a rischio;
- tutti i clienti sopra 0,70;
- clienti sopra 0,40 ma solo se CLV > 5.000 euro;
- clienti con expected loss superiore al costo dell'intervento.

L'ultima formulazione è spesso più vicina alla decision intelligence.

Se:

\[
Expected\ Loss = P(churn) \times Value\ at\ Risk
\]

allora due clienti con la stessa probabilità di churn possono avere priorità molto diversa.

### Errore tipico

Valutare un modello logit solo con accuracy al threshold 0,5.

La soglia 0,5 non ha nulla di magico. È una scelta decisionale.

La qualità del modello deve essere separata dalla policy con cui trasformiamo probabilità in azioni.
