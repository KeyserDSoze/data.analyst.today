## 16.8 Storytelling senza manipolazione: il Visual Integrity Gate

Ogni visualizzazione seleziona una prospettiva. Periodo, scala, denominatore, ordine, colore e confronto influenzano ciò che appare importante. La selezione è inevitabile; la manipolazione no.

Per questo un visual che entra nella Decision Communication Pack deve superare un **Visual Integrity Gate**. La domanda non è soltanto “il numero è corretto?”, ma **l'impressione prodotta dal visual resta proporzionata al claim che il dato può sostenere?**

### Scala ed encoding devono raccontare la stessa magnitudine

Nei bar chart la lunghezza della barra codifica direttamente il valore. Un asse troncato rompe questa proporzione. L'Office for National Statistics raccomanda quindi una baseline a zero per barre e aree.[^ons-axis]

Consideriamo control **4,8%** e treatment **5,1%**. Con un asse da 4,7% a 5,2% la seconda barra può sembrare molte volte più grande. Il delta reale è **+0,3 punti percentuali**, circa **+6,25% relativo**. Una rappresentazione decision-ready può usare barre con zero baseline e rendere esplicito il delta, eventualmente con uncertainty. Così mostriamo la differenza senza falsificare il rapporto visivo.

Per line chart e scatter il principio cambia. Poiché i punti non sono rappresentati come lunghezza dalla baseline, un asse ristretto può essere legittimo per leggere variazioni piccole, purché scala e contesto siano chiari. Il problema non è “zero sempre”: è evitare che l'encoding crei un'impressione sproporzionata rispetto alla domanda.[^ons-axis]

## Il tempo può essere selezionato opportunisticamente

Una campagna può sembrare eccellente rispetto alla settimana immediatamente precedente e ordinaria rispetto a trend pre-campagna, stesso periodo dell'anno precedente, baseline stagionale o controllo. Prima di scegliere la finestra chiediamo:

> **Quale confronto avremmo usato se il risultato fosse andato nella direzione opposta?**

Se cambieremmo il periodo solo perché l'esito è meno favorevole, abbiamo un problema di framing, non di grafica.

## Dual axis, area e cumulativi

Due serie su assi indipendenti possono essere scalate fino a sovrapporsi quasi perfettamente. Se la domanda è la relazione, due grafici allineati, una baseline comune o uno scatter spesso rendono più visibile quanto la correlazione dipenda dal dato e quanto dalle scale.

Anche area e volume possono amplificare la percezione. Se una quantità doppia viene rappresentata con un cerchio di raggio doppio, l'area quadruplica. Bubble chart, icone ridimensionate e visual 3D devono quindi dimostrare di aggiungere informazione, non soltanto salienza.

Le misure cumulative hanno un failure mode diverso: revenue cumulativa, utenti cumulativi o ticket cumulativi tendono quasi inevitabilmente a salire. Se la decisione riguarda il ritmo corrente, dobbiamo affiancare run rate o delta marginale per non trasformare una curva sempre crescente in prova di salute.

## Denominatore, eligibility e scale tra pannelli

“90% soddisfatti” può essere formalmente vero e materialmente fuorviante se il response rate è 12% o l'eligibility esclude gli utenti con problemi. Il gate deve quindi poter ricostruire numeratore, denominatore, missing/non-response e cambi di popolazione.

Negli small multiples, scale indipendenti possono far sembrare simili regioni con volatilità molto diversa. Se il compito è confrontare magnitudini, usiamo scale coerenti. Se il compito è confrontare la forma interna, scale locali possono essere accettabili ma devono essere dichiarate.

## L'opposite-framing test

Un controllo molto potente consiste nel provare a costruire, con gli stessi dati, la visualizzazione più convincente possibile per la conclusione opposta. Confrontiamo periodo, baseline, ordine, scala, denominatore, segmentazione e titolo. Le differenze ci mostrano quali scelte di framing governano la percezione.

Poi applichiamo una domanda ancora più dura:

> **Se questa evidenza non sostenesse la recommendation che preferisco, userei comunque la stessa forma e lo stesso titolo?**

Se la risposta è no, dobbiamo motivare la differenza o ridisegnare.

## Visual Integrity Gate

Questo artefatto merita di restare scansionabile:

- [ ] scala coerente con l'encoding;
- [ ] periodo scelto dalla domanda, non dal risultato;
- [ ] baseline/target appropriati;
- [ ] denominator ed eligibility verificabili;
- [ ] scale comparabili quando il confronto lo richiede;
- [ ] nessuna area/3D che amplifichi indebitamente la magnitudine;
- [ ] cumulativo distinto dal run rate quando necessario;
- [ ] titolo non più forte dell'evidenza;
- [ ] uncertainty decision-critical visibile;
- [ ] opposite-framing test superato.

> **Il data storytelling non consiste nel trovare il framing più persuasivo. Consiste nel trovare il framing più informativo che continueremmo a difendere anche se il dato non sostenesse la nostra preferenza.**

[^ons-axis]: Office for National Statistics, *Axes and gridlines*, https://service-manual.ons.gov.uk/data-visualisation/guidance/axes-and-gridlines
