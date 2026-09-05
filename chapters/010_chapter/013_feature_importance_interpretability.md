## 10.13 Feature importance e interpretabilità: spiegare il modello senza inventare una leva

Quando un modello funziona bene, la domanda successiva è quasi inevitabile: **perché ha assegnato questo score?** Oppure: **quali informazioni usa di più?** Sono domande utili, ma non equivalgono a chiedere che cosa dovremmo modificare per cambiare l'outcome.

La prima coppia riguarda interpretabilità predittiva. L'ultima riguarda causalità e actionability.

### Caso simulato/composito — NovaBank

NovaBank prevede la chiusura del conto entro 60 giorni. Le feature più informative risultano:

1. contatti al call center;
2. riduzione del saldo;
3. reclami aperti;
4. riduzione dei login;
5. tenure.

Operations propone di ridurre i contatti al call center perché sono la feature più importante. Il modello non sostiene questa decisione: i contatti possono essere la conseguenza di problemi già esistenti e quindi un ottimo segnale di rischio senza essere una leva da sopprimere.

Il Capitolo 8 ci dà la distinzione corretta:

> **predictive importance ≠ treatment effect**.

### Prima validare il modello, poi interpretarlo

Scikit-learn sottolinea che feature importance su un modello che generalizza male è poco informativa. Prima chiediamo se il modello predice davvero fuori campione; soltanto dopo chiediamo quali feature contribuiscono a quella performance.

Riferimento: https://scikit-learn.org/stable/modules/permutation_importance.html

La permutation importance misura quanto peggiora una metrica quando una feature viene rimescolata. Se la performance scende molto, quella feature è importante **per quel modello, su quel dataset e rispetto a quella metrica**. Calcolarla su un held-out set aiuta a capire il contributo alla generalizzazione anziché al solo training fit.

### Caso reale documentato — Titanic e feature casuali

La documentazione scikit-learn aggiunge al dataset Titanic feature casuali e mostra come le impurity-based importance di un random forest possano attribuire peso elevato a variabili ad alta cardinalità anche quando non hanno vero valore predittivo fuori campione. La permutation importance su dati held-out rende più evidente il problema.

Riferimento: https://scikit-learn.org/stable/auto_examples/inspection/plot_permutation_importance.html

La lezione non è che una tecnica produca la “verità” e l'altra no. Ogni importance misura il comportamento di uno specifico modello in uno specifico contesto.

### Feature correlate condividono informazione

Revenue 30d, revenue 28d, orders 30d e AOV possono trasportare informazione sovrapposta. Se permutiamo una sola colonna, le altre possono conservarne una parte; l'importance individuale può quindi apparire bassa anche quando il gruppo concettuale è fondamentale.

Per questo è spesso utile guardare gruppi di feature, correlazioni, stabilità delle importance tra fold e periodi e ablation di intere famiglie. Se le importance cambiano molto mentre la performance resta stabile, potremmo osservare semplice sostituzione tra proxy ridondanti, non un cambio nel fenomeno business.

### Globale, locale e actionability sono tre livelli

L'interpretabilità globale prova a capire quali informazioni sostengono il ranking complessivo. Quella locale prova a spiegare perché un singolo account abbia score 0,87. Entrambe sono utili per debugging, review umana e controlli di plausibilità.

L'**actionability** aggiunge una domanda diversa: la feature è modificabile e abbiamo evidenza che modificarla produca l'effetto desiderato?

Una tabella rigorosa può separare i tre piani:

| Feature/gruppo | Predictive importance | Modificabile? | Evidenza causale? | Uso |
|---|---|---|---|---|
| failed payments | alta | parzialmente | da verificare | risk signal |
| tenure | media | no | non rilevante | segmentation/risk |
| response time support | media | sì | esperimento disponibile | possibile leva |

Questa struttura impedisce di trasformare automaticamente la feature importance in una intervention map.

### Interpretability drift come diagnostica

Se le feature più usate dal modello cambiano molto nel tempo possiamo avere nuovo comportamento della popolazione, cambi di feature engineering, sostituzione tra feature correlate, concept drift o retraining instability. Il cambiamento non è automaticamente un incidente, ma è un segnale utile da mettere in relazione con performance e data lineage.

La comunicazione corretta è:

> “Su questo validation set, il modello perde maggiormente performance quando questa informazione viene rimossa o permutata.”

Non:

> “Questa è la causa principale dell'outcome.”

> **Interpretare un modello significa capire come costruisce la previsione. Decidere che cosa cambiare nel mondo richiede una catena di evidenza diversa.**