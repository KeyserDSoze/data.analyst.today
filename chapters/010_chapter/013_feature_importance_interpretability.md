## 10.13 Feature importance e interpretabilità: spiegare il modello, non inventare una leva

Quando un modello funziona bene, la domanda successiva è quasi inevitabile:

> **perché ha assegnato questo score?**

Oppure:

> **quali informazioni usa di più?**

Sono domande utili. Ma non sono equivalenti a:

> **che cosa dovremmo cambiare per modificare l'outcome?**

La prima coppia riguarda interpretabilità predittiva. L'ultima riguarda causalità e intervento.

### Caso simulato/composito — NovaBank

NovaBank prevede chiusura del conto entro 60 giorni.

Le feature più informative nel modello sono:

1. contatti al call center;
2. riduzione del saldo;
3. reclami aperti;
4. riduzione dei login;
5. tenure.

Il responsabile operations propone:

> "Riduciamo i contatti al call center: è la feature più importante del churn."

Il modello non sostiene questa conclusione.

I contatti possono essere una conseguenza di problemi già esistenti. Sono utili per anticipare il rischio, non necessariamente una leva da ridurre.

Il Capitolo 8 ci dà il linguaggio corretto: **feature predictive importance ≠ treatment effect**.

### Prima regola: valutare il modello prima dell'importance

Scikit-learn sottolinea un punto spesso dimenticato: feature importance su un modello che generalizza male è poco utile.

Prima chiediamo:

> il modello predice davvero fuori campione?

Solo dopo:

> quali feature contribuiscono a quella performance?

Fonte: https://scikit-learn.org/stable/modules/permutation_importance.html

### Permutation importance

La permutation importance misura quanto peggiora una metrica quando una feature viene rimescolata, rompendo il rapporto che il modello stava usando.

Se la performance scende molto, quella feature è importante **per quel modello, su quel dataset e rispetto a quella metrica**.

Queste condizioni devono essere parte della frase.

Un'importance calcolata sul training set può premiare feature che aiutano l'overfitting. Per capire il contributo alla generalizzazione è spesso più informativo calcolarla su validation/test appropriato.

### Caso reale documentato — Titanic con feature casuali

La documentazione scikit-learn aggiunge al dataset Titanic feature casuali e confronta importance degli alberi basata su impurity con permutation importance.

Le impurity-based importance possono attribuire peso elevato a feature ad alta cardinalità anche quando non hanno vero valore predittivo fuori campione.

Permutation importance calcolata su dati held-out rende più evidente il problema.

Fonte: https://scikit-learn.org/stable/modules/permutation_importance.html

La lezione non è che una tecnica sia sempre "vera" e l'altra "falsa". È che ogni importance misura qualcosa di specifico e deve essere interpretata nel contesto della generalizzazione.

### Feature correlate: l'informazione può essere condivisa

Supponiamo che il modello usi:

- revenue 30d;
- orders 30d;
- AOV 30d;
- revenue 28d.

Se permutiamo una feature, le altre possono conservare molta informazione equivalente.

L'importance individuale può quindi essere bassa anche se il **gruppo concettuale** è fondamentale.

Viceversa, con feature ridondanti, coefficienti o ranking di importance possono cambiare molto tra retraining pur lasciando performance quasi invariata.

Per questo può essere utile analizzare:

- gruppi di feature;
- correlazioni;
- stabilità delle importance tra periodi/fold;
- performance dopo ablation di un intero gruppo.

### Interpretabilità globale e locale

**Globale** risponde a domande come:

- quali informazioni sostengono maggiormente il ranking complessivo?
- quali pattern usa mediamente il modello?

**Locale** risponde a:

- perché questo account ha score 0,87?
- quali feature hanno contribuito maggiormente a questo caso?

Un explanation locale è particolarmente utile per:

- debugging;
- review umana;
- supporto operativo;
- controlli di plausibilità.

Ma anche una spiegazione locale descrive il comportamento del modello. Non è automaticamente una prescrizione causale.

### Actionability: un terzo concetto ancora diverso

Una feature può essere:

- molto predittiva e non modificabile, come tenure;
- modificabile ma non causalmente efficace;
- causalmente importante ma poco predittiva individualmente;
- sia predittiva sia una leva plausibile.

Conviene quindi non chiamare automaticamente le feature importanti "drivers".

Una tabella più rigorosa può essere:

| Feature/gruppo | Predictive importance | Modificabile? | Evidenza causale? | Uso |
|---|---|---|---|---|
| failed payments | alta | parzialmente | da verificare | risk signal |
| tenure | media | no | non rilevante | segmentation/risk |
| response time support | media | sì | esperimento disponibile | possibile leva |

Questa struttura impedisce di passare direttamente dal modello alla strategia.

### Interpretability drift

Se le feature importance cambiano molto nel tempo possiamo avere:

- nuovo comportamento della popolazione;
- cambi di feature engineering;
- sostituzione tra feature correlate;
- concept drift;
- retraining instability.

Il cambio non è automaticamente un incidente, ma può essere un ottimo segnale diagnostico.

### Regola di comunicazione

Preferisci:

> **"Su questo validation set, il modello perde maggiormente performance quando questa informazione viene rimossa o permutata."**

oppure:

> **"Per questo caso, queste feature contribuiscono maggiormente allo score secondo il metodo di explanation adottato."**

Non:

> "Questa è la causa principale dell'outcome."

> **Interpretare un modello significa capire come costruisce la previsione. Decidere che cosa cambiare nel mondo richiede un'altra catena di evidenza.**
