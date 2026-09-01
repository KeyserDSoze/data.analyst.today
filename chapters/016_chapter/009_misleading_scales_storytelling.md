## 16.8 Storytelling senza manipolazione: il Visual Integrity Gate

Ogni visualizzazione seleziona una prospettiva.

Periodo, scala, denominatore, ordine, colori e confronto influenzano ciò che appare importante.

La selezione è inevitabile. La manipolazione no.

Per questo, prima di promuovere un visual nella Decision Communication Pack, applichiamo un **Visual Integrity Gate**.

## 1. La scala rappresenta onestamente la grandezza?

Nei bar chart la lunghezza della barra codifica direttamente la magnitudine. Se la baseline viene troncata, il rapporto visivo tra le barre non corrisponde più al rapporto tra i valori.

L'Office for National Statistics raccomanda di partire da zero per bar chart e altre forme in cui la lunghezza/area è l'encoding principale.

### Caso simulato/composito — “Performance quasi triplicata”

- controllo: 4,8%;
- nuova esperienza: 5,1%.

Con asse da 4,7% a 5,2%, la barra nuova può sembrare molte volte più alta.

Il delta reale è:

- +0,3 punti percentuali;
- circa +6,25% relativo.

Per una decisione possiamo mostrare:

- due barre con zero baseline;
- accanto, il delta `+0,3 pp`;
- intervallo di incertezza se rilevante.

Così rendiamo visibile la differenza senza falsificare la proporzione.

## 2. Truncation nei line chart: non sempre è sbagliata

Una linea non usa la lunghezza dalla baseline come encoding principale allo stesso modo di una barra.

Un asse ristretto può quindi essere utile per leggere variazioni piccole.

La disciplina richiesta è:

- scala chiaramente visibile;
- contesto sufficiente;
- nessuna omissione di una baseline decision-critical;
- evitare titoli che trasformano una piccola variazione in un evento enorme.

La regola non è “ogni asse deve partire da zero”. È **l'encoding non deve produrre un'impressione sproporzionata rispetto alla domanda**.

## 3. Period selection: il tempo può essere cherry-picked

Una campagna può apparire eccezionale confrontando la settimana di lancio con una settimana debole immediatamente precedente e ordinaria rispetto a:

- stesso periodo anno precedente;
- trend pre-campagna;
- gruppo di controllo;
- baseline stagionale.

Prima di scegliere la finestra chiediamo:

> “Quale confronto avremmo usato se il risultato fosse andato nella direzione opposta?”

Se la risposta cambia, abbiamo un rischio di framing opportunistico.

## 4. Dual axis: la correlazione può essere disegnata

Due serie con scale indipendenti possono essere ridimensionate fino a sovrapporsi quasi perfettamente.

Il lettore vede una relazione che dipende in parte dalla scelta delle scale.

Quando possibile preferiamo:

- due grafici allineati;
- indice rispetto a una baseline comune;
- scatter plot se la domanda è la relazione;
- coefficienti/statistiche se servono a quantificarla.

## 5. Area e volume: l'occhio può amplificare due volte

Se una quantità doppia viene rappresentata con un cerchio di raggio doppio, l'area diventa quattro volte maggiore.

Bubble chart, icone ridimensionate, mappe a simboli e visual 3D richiedono quindi cautela.

Chiediamoci se il lettore deve confrontare **lunghezza, area o volume** e se l'encoding è proporzionale alla quantità dichiarata.

## 6. Cumulative vs period: una curva che sale sempre può ingannare

Revenue cumulativa, utenti cumulativi e ticket cumulativi tendono quasi necessariamente a crescere.

Una curva crescente può quindi nascondere:

- rallentamento del run rate;
- peggioramento della crescita marginale;
- deterioramento della qualità.

Se la decisione riguarda il ritmo corrente, affianchiamo la misura di periodo o il delta marginale.

## 7. Il denominatore può cambiare il significato più del numeratore

> “Il 90% dei clienti è soddisfatto.”

può essere formalmente corretto e sostanzialmente fuorviante se il survey response rate è 12% o se la popolazione eleggibile esclude proprio gli utenti con problemi.

Un visual integrity check include quindi:

- numeratore;
- denominatore;
- eligibility;
- missing / non-response;
- eventuale cambio di popolazione.

## 8. Scale incoerenti tra small multiples

Due regioni possono sembrare avere volatilità simile se ogni pannello usa una scala diversa.

Quando l'obiettivo è confrontare magnitudini, usiamo scale coerenti. Se dobbiamo invece mostrare pattern interni con scale diverse, lo dichiariamo esplicitamente.

## 9. Il test della versione opposta

Proviamo a costruire, con gli stessi dati, la visualizzazione più convincente possibile per la conclusione opposta.

Poi confrontiamo:

- periodo;
- baseline;
- ordine;
- scala;
- denominatore;
- segmentazione;
- titolo.

Le differenze rivelano le scelte di framing che governano la percezione.

## 10. Il counterfactual visual test

Un controllo ancora più forte:

> **“Se questa evidenza non sostenesse la mia raccomandazione preferita, userei comunque la stessa forma e lo stesso titolo?”**

Se no, dobbiamo motivare la scelta o ridisegnare.

## Visual Integrity Gate

Prima della pubblicazione:

- [ ] scala coerente con l'encoding;
- [ ] periodo scelto dalla domanda, non dal risultato;
- [ ] baseline/target appropriati;
- [ ] denominatore ed eligibility verificabili;
- [ ] scale comparabili dove il confronto lo richiede;
- [ ] nessuna area/3D che amplifichi indebitamente la magnitudine;
- [ ] cumulativo distinto dal run rate quando necessario;
- [ ] titolo non più forte dell'evidenza;
- [ ] incertezza decision-critical visibile;
- [ ] opposite-framing test superato.

> **Il data storytelling non consiste nel trovare il framing più persuasivo. Consiste nel trovare il framing più informativo che continueremmo a difendere anche se il dato non sostenesse la nostra preferenza.**

### Fonte

- Office for National Statistics, *Axes and gridlines*: https://service-manual.ons.gov.uk/data-visualisation/guidance/axes-and-gridlines
