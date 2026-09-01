## 16.9 Tabelle, ranking e small multiples: scegliere tra pattern e precisione

Non tutto deve diventare un grafico.

La domanda utile è:

> **“Il destinatario deve percepire un pattern o recuperare un valore preciso?”**

Questa distinzione evita molta visualizzazione decorativa.

## Quando la tabella è la forma migliore

Una tabella è spesso superiore quando il lettore deve:

- trovare un valore specifico;
- confrontare numeri molto vicini;
- leggere più metriche per la stessa entità;
- verificare una soglia;
- individuare owner e azione;
- utilizzare il contenuto come lista operativa.

Esempio decisionale:

| Regione | OTD | Target | Gap | Ordini a rischio | Owner |
|---|---:|---:|---:|---:|---|
| Nord-Ovest | 91,2% | 95% | -3,8 pp | 4.120 | Ops A |
| Centro | 94,6% | 95% | -0,4 pp | 780 | Ops B |
| Sud | 96,1% | 95% | +1,1 pp | 210 | Ops C |

Una tabella ordinata per gap può essere più utile di tre gauge.

## Ranking: ordinare significa proporre una priorità

Una tabella non è neutrale nemmeno nell'ordine.

Possibili ordinamenti:

- valore assoluto;
- delta;
- severità;
- impatto economico;
- rischio;
- alfabetico.

Se l'obiettivo è prioritizzare interventi, l'ordine alfabetico nasconde la decisione. Se l'obiettivo è lookup, può essere invece appropriato.

Dobbiamo rendere esplicita la regola di ranking quando ha significato decisionale.

## Small multiples: molti pattern, una grammatica comune

### Caso simulato/composito — 18 regioni, 18 linee

Una società logistica vuole confrontare l'on-time delivery di 18 regioni negli ultimi 24 mesi.

Un line chart con 18 serie contiene tutto ma rende difficile seguire qualsiasi regione.

Gli small multiples usano:

- un pannello per regione;
- stessa finestra temporale;
- stessa scala quando la magnitudine deve essere confrontabile;
- stesso encoding per target ed eventi.

Emergono subito tre famiglie:

- regioni stabilmente forti;
- deterioramenti progressivi;
- shock temporanei con recovery.

La ripetizione della stessa grammatica riduce il costo cognitivo.

## Scale coerenti: quando servono davvero

Se vogliamo confrontare **magnitudini**, scale diverse tra pannelli possono ingannare.

Se vogliamo confrontare soltanto **forma interna del pattern**, scale locali possono avere valore, ma vanno rese evidenti.

Una soluzione possibile è mostrare:

- small multiples con scala comune nella vista decisionale;
- versione normalizzata o locale nell'appendix diagnostica.

## Sparklines: contesto temporale dentro una tabella

Una tabella operativa può aggiungere una piccola sparkline per rispondere contemporaneamente:

- quanto vale oggi?
- è un problema nuovo o persistente?

La sparkline non deve sostituire assi o dettaglio quando il trend è il cuore del claim. Serve come contesto compatto.

## Conditional formatting: segnale, non pittura

Colorare ogni cella crea spesso una heatmap involontaria.

La formattazione condizionale dovrebbe evidenziare soltanto:

- violazioni di soglia;
- top/bottom materialmente rilevanti;
- cambiamenti che richiedono azione.

E deve avere una codifica alternativa al colore: simbolo, testo, ordinamento o label.

## Table-first per l'audit

Anche quando la pagina executive usa grafici, la Decision Communication Pack dovrebbe offrire una forma tabellare per:

- numeri esatti;
- accessibilità;
- verifica;
- export;
- provenance.

La Government Analysis Function sottolinea che i dashboard interattivi non sono pienamente accessibili a tutti e raccomanda alternative come tabelle di supporto, testo e download dei dati.

## Una regola operativa

- **pattern** → grafico;
- **lookup** → tabella;
- **molti pattern comparabili** → small multiples;
- **priorità operativa** → tabella ordinata con soglie e owner;
- **audit/accessibilità** → tabella o underlying data disponibile.

> **La sofisticazione di una visualizzazione non si misura dal numero di encoding. Si misura da quanto rapidamente il destinatario riesce a svolgere il compito cognitivo corretto.**

### Fonti

- Office for National Statistics, *Axes and gridlines*: https://service-manual.ons.gov.uk/data-visualisation/guidance/axes-and-gridlines
- Government Analysis Function, *Data visualisation: testing dashboards for design and accessibility*: https://analysisfunction.civilservice.gov.uk/policy-store/data-visualisation-testing-dashboards-for-design-and-accessibility/
