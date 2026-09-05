## 17.3 Vectora — “Possiamo aumentare i prezzi senza distruggere valore?”

> **Caso simulato/composito.** Organizzazione, numeri e sequenza sono costruiti per la didattica.

Vectora, e-commerce di elettronica, considera un aumento medio dei prezzi del **6%** per recuperare margine. Il CFO chiede quanto volume verrebbe perso e la richiesta sembra invitare a stimare un'elasticità unica. Ma la decisione vera è diversa: **in quali categorie un prezzo più alto aumenta il contribution profit senza distruggere abbastanza volume, acquisizione, retention o posizionamento competitivo da rendere la scelta negativa?**

Il failure cost è asimmetrico. Un test limitato è reversibile; un repricing generalizzato può cambiare customer mix, competitor response e percezione del brand. Per questo la stop rule iniziale è: **nessun +6% uniforme basato sulla sola correlazione storica prezzo-volume**.

### La prima evidenza serve soprattutto a distruggere l'idea della media

Nei dati storici alcuni prodotti più costosi vendono anche di più. La relazione non è una prova che alzare il prezzo aumenti la domanda: bestseller, brand strength, disponibilità, stock, lifecycle, promozioni e competitor pricing influenzano contemporaneamente prezzo e unità vendute. Il prezzo è una decisione del business, non un trattamento assegnato casualmente.

L'Analytical Brief sposta quindi l'outcome da revenue o unità a **contribution profit per visitatore**. I guardrail sono conversione, nuovi clienti, repeat purchase, stock turnover, cancellazioni, complaints e price index rispetto a competitor comparabili. Questa scelta evita di dichiarare vincente una strategia che aumenta il margine percentuale ma distrugge profitto assoluto.

L'EDA Evidence Map separa variazione nel tempo sullo stesso SKU, differenze cross-sectional, promozioni, stock, competitor price index, stagionalità, traffico/channel mix e cambi assortimento. Il risultato più importante è che **l'elasticità media non è una rappresentazione utile del catalogo**. Gli accessori commodity sono molto più elastici; i prodotti premium esclusivi meno; le categorie con molti competitor comparabili sono più sensibili; stock scarcity e product lifecycle modificano ulteriormente la risposta.

A questo punto il problema non è stimare “l'elasticità di Vectora”. È capire dove siamo lontani o vicini alla **decision boundary**.

### Scenario e switching value decidono dove comprare altra evidenza

Per ogni categoria il team costruisce scenari prudente, centrale e severo usando prezzo, volume atteso, costo prodotto, costi variabili, promozioni ed effetti operativi. Il +6% generalizzato risulta fragile: in alcune categorie il contribution profit cresce, in altre la perdita di volume distrugge valore, in altre ancora il range plausibile attraversa la soglia tra aumentare e non aumentare.

Questa distanza dallo switching threshold guida il method gate.

- **Lontano dalla soglia, rischio basso:** la decisione può procedere con evidenza storica e rollout controllato; un esperimento ulteriore ha poco valore marginale.
- **Vicino alla soglia:** piccole differenze nell'elasticità cambiano la scelta; qui il valore di informazione è alto e un Experiment Contract può guadagnarsi il diritto di esistere.
- **Contesto fortemente interferente:** sostituzione tra SKU, competitor reaction o assortimento instabile rendono difficile un test locale; il claim deve restare circoscritto e la policy più reversibile.

Vectora usa quindi test geografici o subset di SKU soltanto nel secondo gruppo, con guardrail definiti prima del lancio. L'esperimento non serve a dimostrare genericamente che il prezzo influenza la domanda. Serve a ridurre **l'incertezza che può cambiare il ranking delle alternative**.

### Anche un test valido può essere locale

Un price experiment può modificare il contesto che cerca di misurare. I clienti confrontano SKU trattati e non trattati; i competitor possono reagire; esistono substitution effects; una finestra breve non osserva repeat purchase; un prezzo diverso può cambiare il mix dei clienti acquisiti.

Per questo anche un test randomizzato non autorizza automaticamente la frase “questo è il prezzo ottimale per i prossimi sei mesi”. Può identificare un effetto locale in una finestra e in una popolazione definite. Il Decision Record deve portarsi dietro quello scope.

### La policy nasce diversa dall'idea iniziale

Le alternative diventano tre. **A — +6% generalizzato** è semplice ma ignora eterogeneità e rischio competitivo. **B — nessun aumento** protegge volume ma rinuncia a margine in segmenti poco elastici. **C — repricing selettivo** usa aumenti nell'ordine del **4–7%** sui segmenti meno elastici e lontani dalla soglia, nessun aumento sulle commodity ad alta comparabilità, test limitati sulle categorie intermedie e rollback se contribution profit o guardrail superano le soglie concordate.

La scelta è **C**. Non esiste un singolo numero di elasticità che “ha prodotto” la decisione. La decisione nasce dalla combinazione tra eterogeneità, economics, uncertainty e reversibilità.

### Evidence Ledger

| Observed | Inferred | Still unknown |
|---|---|---|
| response storica molto eterogenea per categoria | alcuni segmenti hanno pricing power maggiore | risposta di lungo periodo dopo repricing |
| +6% non è robusto negli scenari | commodity ad alta comparabilità sono più fragili | competitor reaction |
| alcune categorie sono lontane dallo switching value | test ha alto valore solo vicino alla boundary | substitution effect completo tra SKU |

La headline executive può quindi evitare la falsa precisione dell'elasticità media:

> **Un +6% uniforme non è robusto: l'economia cambia materialmente per categoria. Esistono segmenti con spazio di prezzo, commodity dove il volume perso supera il beneficio e un gruppo intermedio in cui l'incertezza giustifica test limitati.**

L'outcome review segue contribution profit per visitor, unità, conversione, nuovi clienti, repeat purchase, competitor price index, stock turnover e sostituzione tra SKU. La policy viene aggiornata se cambiano competitor, mix, costi o distanza dalle switching threshold.

**Percorso effettivo:** Analytical Brief → EDA Evidence Map → Uncertainty Brief → Causal Identification Brief dove il confronto storico è insufficiente → Experiment Contract solo nelle categorie decision-critical → Decision Record → Decision Communication Pack.

Il percorso è volutamente selettivo: non serve un modello strutturale perfetto di domanda per tutto il catalogo e non serve testare ogni SKU.

> **Il metodo più forte va comprato dove l'incertezza può cambiare decisione, non dove è semplicemente possibile fare un'analisi più sofisticata.**
