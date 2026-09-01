## 5.5 Valore atteso e rischio: la media degli esiti non basta per decidere

Il **valore atteso** combina esiti possibili e probabilità. Risponde a una domanda del tipo:

> **Se potessimo ripetere molte volte una decisione nelle stesse condizioni, quale risultato medio produrrebbe?**

Per una variabile discreta:

\[
E[X]=\sum_x x\,P(X=x)
\]

Nel lavoro analitico il concetto compare continuamente:

- ricavo atteso di una campagna;
- perdita attesa da frode;
- costo atteso di un guasto;
- valore atteso di un lead;
- margine atteso di una decisione di pricing.

Ma il valore atteso non contiene da solo tutta la decisione.

### Caso simulato/composito — Due campagne, stesso valore atteso

Un e-commerce deve scegliere tra due campagne promozionali.

**Campagna A**

| Esito | Probabilità | Margine incrementale |
|---|---:|---:|
| Debole | 20% | 20.000 € |
| Normale | 60% | 80.000 € |
| Ottimo | 20% | 140.000 € |

Valore atteso:

`0,20 × 20.000 + 0,60 × 80.000 + 0,20 × 140.000 = 80.000 €`.

**Campagna B**

| Esito | Probabilità | Margine incrementale |
|---|---:|---:|
| Fallimento | 45% | -40.000 € |
| Buono | 10% | 80.000 € |
| Eccezionale | 45% | 200.000 € |

Anche qui:

`0,45 × (-40.000) + 0,10 × 80.000 + 0,45 × 200.000 = 80.000 €`.

Stesso valore atteso. Distribuzione degli esiti completamente diversa.

Se l'azienda non può permettersi una perdita di 40.000 €, la Campagna B può essere inaccettabile anche con expected value positivo. Se invece gestisce centinaia di iniziative poco correlate e può assorbire la volatilità, la valutazione può cambiare.

Il punto è:

> **expected value e tolleranza al rischio sono concetti distinti.**

### Varianza e deviazione standard descrivono quanto gli esiti si disperdono

La varianza misura la dispersione degli esiti attorno al valore atteso:

\[
Var(X)=E[(X-E[X])^2]
\]

La deviazione standard riporta la misura nell'unità originale.

Questa idea collega probabilità e decisione: due strategie con la stessa media possono avere code e volatilità molto diverse.

### Caso simulato/composito — Due SKU da 120 unità al giorno

Due prodotti hanno domanda media di 120 unità al giorno.

- SKU A: deviazione standard 8;
- SKU B: deviazione standard 47.

Una policy di riordino costruita soltanto sulla media li tratterebbe quasi allo stesso modo.

Ma il secondo SKU espone il business a un rischio molto maggiore di stock-out o overstock.

Per operations interessa quindi almeno la coppia:

> **domanda attesa + distribuzione dell'errore attorno alla domanda attesa**.

Il Capitolo 7 trasformerà questa intuizione in forecast e intervalli predittivi.

### Expected loss: collegare probabilità e conseguenza

Supponiamo che una certa classe di transazioni abbia:

- probabilità di frode: 0,3%;
- perdita media se la frode avviene: 1.400 €.

La perdita attesa per transazione è:

`0,003 × 1.400 € = 4,20 €`.

Se un controllo aggiuntivo costa 0,40 € a transazione e riduce significativamente la perdita attesa, può avere senso economico. Se costa 12 €, probabilmente no — a meno che non riduca anche altri rischi importanti.

Questo è il ponte tra statistica e decisione:

**probabilità × conseguenza**.

### Il valore atteso non è una promessa né un ordine automatico

Consideriamo un progetto con:

- 90% di probabilità di perdere 50.000 €;
- 10% di probabilità di guadagnare 600.000 €.

Expected value:

`0,90 × (-50.000) + 0,10 × 600.000 = +15.000 €`.

Dire “il progetto vale +15.000 €” senza altro sarebbe fuorviante.

Un solo progetto non verrà necessariamente ripetuto molte volte. La perdita può compromettere la liquidità. Gli esiti possono essere correlati con altri rischi aziendali. Il management può avere vincoli che rendono alcuni downside non accettabili.

Per questo il Capitolo 15, dedicato alla decisione, aggiungerà elementi come:

- scenari;
- sensitività;
- soglie decisionali;
- value of information;
- costi asimmetrici;
- capacità di assorbire il downside.

Qui fissiamo la base probabilistica.

### Quattro domande prima di confrontare decisioni incerte

1. Qual è il valore atteso?
2. Quanto sono dispersi gli esiti?
3. Quanto è grave la coda negativa?
4. La decisione è ripetibile abbastanza volte da rendere il valore medio una guida utile?

> **Una strategia non è “buona” perché ha expected value positivo. È buona rispetto a obiettivi, vincoli e distribuzione degli esiti.**
