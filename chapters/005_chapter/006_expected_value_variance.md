## 5.5 Valore atteso e rischio: la media degli esiti non è ancora una decisione

Una distribuzione ci dice quali risultati consideriamo possibili e con quale probabilità. Il **valore atteso** comprime quella distribuzione in un singolo numero:

`E[X] = Σ_x x · P(X = x)`.

In termini intuitivi risponde a una domanda controfattuale e ripetibile: **se potessimo affrontare molte volte lo stesso tipo di decisione nelle stesse condizioni, quale risultato medio emergerebbe?**

È un concetto potentissimo per ricavi attesi, perdite da frode, costi di guasto, valore di un lead o pricing. Ma, proprio perché comprime una distribuzione, può nascondere differenze decisive tra strategie che hanno la stessa media.

## Stesso expected value, mondi diversi

Un e-commerce deve scegliere tra due campagne promozionali.

**Campagna A**

| Esito | Probabilità | Margine incrementale |
|---|---:|---:|
| Debole | 20% | 20.000 € |
| Normale | 60% | 80.000 € |
| Ottimo | 20% | 140.000 € |

Il valore atteso è 80.000 €.

**Campagna B**

| Esito | Probabilità | Margine incrementale |
|---|---:|---:|
| Fallimento | 45% | -40.000 € |
| Buono | 10% | 80.000 € |
| Eccezionale | 45% | 200.000 € |

Anche qui il valore atteso è 80.000 €.

Trattare le due campagne come equivalenti significherebbe cancellare quasi tutta l'informazione utile. La prima concentra gli esiti attorno a valori positivi; la seconda accetta quasi una probabilità su due di perdere 40.000 € in cambio di una coda positiva molto più grande.

Se l'azienda ha liquidità limitata o la perdita di 40.000 € compromette altri progetti, la Campagna B può essere inaccettabile nonostante l'expected value positivo. Se invece l'impresa prende centinaia di decisioni simili e poco correlate ed è in grado di assorbirne la volatilità, la valutazione può cambiare. **Expected value e tolleranza al rischio descrivono cose diverse.**

La varianza formalizza una parte di questa differenza:

`Var(X) = E[(X − E[X])²]`.

La deviazione standard riporta la dispersione nell'unità originale. Non esaurisce il rischio — soprattutto quando le code sono asimmetriche — ma impedisce di confondere strategie con lo stesso centro e distribuzioni molto diverse.

## La media della domanda non basta per dimensionare la capacità

Due SKU vendono in media 120 unità al giorno. Il primo ha deviazione standard 8, il secondo 47. Una policy di riordino costruita soltanto sulla media tratterebbe i due prodotti quasi allo stesso modo, mentre il secondo espone il business a un rischio molto maggiore di stock-out e overstock.

Per operations la quantità utile è quindi almeno la coppia:

> **domanda attesa + distribuzione dell'errore attorno alla domanda attesa**.

Nel Capitolo 7 useremo la stessa idea per forecast e intervalli predittivi. Qui serve vedere il principio: la media descrive dove tende a stare il processo; la dispersione decide quanto spesso possiamo trovarci molto lontani da quel centro.

## Dalla probabilità alla conseguenza

Un'altra applicazione del valore atteso collega direttamente rischio e costo. Se una classe di transazioni ha probabilità di frode dello 0,3% e la perdita media quando la frode avviene è 1.400 €, la perdita attesa per transazione è:

`0,003 × 1.400 € = 4,20 €`.

Un controllo aggiuntivo da 0,40 € per transazione può avere senso se riduce abbastanza quella perdita attesa. Uno da 12 € difficilmente si giustifica sulla sola frode attesa, a meno che non protegga anche altri rischi rilevanti.

La formula `probabilità × conseguenza` è semplice, ma cambia la qualità della decisione perché sposta l'attenzione dalla sola frequenza dell'evento al **costo economico dell'errore**.

## Quando l'expected value non è la guida sufficiente

Consideriamo infine un progetto con il 90% di probabilità di perdere 50.000 € e il 10% di probabilità di guadagnarne 600.000. Il valore atteso è:

`0,90 × (-50.000) + 0,10 × 600.000 = +15.000 €`.

Dire semplicemente “il progetto vale +15.000 €” sarebbe una compressione pericolosa. L'iniziativa può essere una tantum, la perdita può creare un problema di liquidità, gli esiti possono essere correlati ad altri rischi aziendali e il management può avere vincoli che rendono il downside non accettabile.

Per questo il Capitolo 15 aggiungerà scenari, sensibilità, soglie decisionali, Value of Information, costi asimmetrici e reversibilità. Qui basta fissare una disciplina: quando due alternative sono incerte, non confrontiamo soltanto il loro valore medio. Guardiamo anche **quanto sono dispersi gli esiti, quanto è grave la coda negativa e se la decisione è abbastanza ripetibile da rendere la media di lungo periodo una guida utile**.

> **Una strategia non diventa buona perché ha expected value positivo. Diventa valutabile quando expected value, distribuzione degli esiti e capacità di assorbire il downside vengono letti insieme.**
