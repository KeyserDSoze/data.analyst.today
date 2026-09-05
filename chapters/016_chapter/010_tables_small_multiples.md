## 16.9 Tabelle, ranking e small multiples: scegliere tra pattern e precisione

Non tutto deve diventare un grafico. Prima della forma chiediamo se il destinatario deve **percepire un pattern** oppure **recuperare un valore preciso**. Questa distinzione elimina molta visualizzazione decorativa.

Una tabella è spesso la scelta migliore quando il lettore deve verificare una soglia, confrontare numeri vicini, leggere più metriche per la stessa entità, trovare un owner o usare il contenuto come lista operativa. Consideriamo:

| Regione | OTD | Target | Gap | Ordini a rischio | Owner |
|---|---:|---:|---:|---:|---|
| Nord-Ovest | 91,2% | 95% | -3,8 pp | 4.120 | Ops A |
| Centro | 94,6% | 95% | -0,4 pp | 780 | Ops B |
| Sud | 96,1% | 95% | +1,1 pp | 210 | Ops C |

Se la decisione è prioritizzare interventi, una tabella ordinata per gap comunica meglio di tre gauge. Se il compito fosse invece lookup amministrativo, un ordine alfabetico potrebbe essere più appropriato. **Anche l'ordinamento propone una priorità**, quindi deve essere coerente con il task.

### Small multiples: una grammatica comune per molti pattern

Una società logistica vuole confrontare l'on-time delivery di **18 regioni negli ultimi 24 mesi**. Un unico line chart con 18 serie contiene tutti i dati ma rende difficile seguire qualunque regione. Gli small multiples riducono il problema usando un pannello per regione, stessa finestra temporale e stesso encoding per target ed eventi.

Con una scala comune emergono rapidamente tre famiglie: regioni stabilmente forti, deterioramenti progressivi e shock temporanei con recovery. La ripetizione della grammatica riduce il costo cognitivo e rende comparabili i pattern.

La scala, però, dipende ancora dalla domanda. Se dobbiamo confrontare **magnitudini**, pannelli con scale diverse possono ingannare. Se dobbiamo confrontare soltanto la **forma interna** del trend, scale locali possono avere valore, purché siano evidenti. Una soluzione pratica può mostrare la scala comune nel decision layer e una vista normalizzata nell'appendix diagnostica.

### Sparklines: contesto compatto, non sostituto del grafico

Una tabella operativa può aggiungere una sparkline per rispondere contemporaneamente a “quanto vale oggi?” e “è un problema nuovo o persistente?”. La sparkline è utile come contesto compatto, ma non dovrebbe sostituire un chart con assi e annotazioni quando il trend è il cuore del claim.

### Conditional formatting: segnale, non pittura

Colorare ogni cella crea spesso una heatmap involontaria. La formattazione condizionale dovrebbe essere riservata a violazioni di soglia, top/bottom materialmente rilevanti o cambiamenti che richiedono azione. E deve avere una seconda codifica — testo, simbolo, label o ordinamento — perché il colore non può essere l'unico canale informativo.

### Table-first per audit e accessibilità

Anche quando la pagina executive usa grafici, la Decision Communication Pack dovrebbe offrire una forma tabellare o underlying data per numeri esatti, verifica, export, accessibilità e provenance. La Government Analysis Function 2026 sottolinea che dashboard interattivi possono non essere pienamente accessibili e raccomanda contenuti alternativi, inclusi testo, tabelle e dati scaricabili.[^gaf-dashboard]

La regola operativa può restare molto semplice:

- **pattern** → grafico;
- **lookup** → tabella;
- **molti pattern comparabili** → small multiples;
- **priorità operativa** → tabella ordinata con soglia e owner;
- **audit/accessibilità** → underlying table o alternativa testuale disponibile.

> **La sofisticazione di una visualizzazione non si misura dal numero di encoding. Si misura da quanto rapidamente il destinatario riesce a svolgere il compito cognitivo corretto.**

[^gaf-dashboard]: Government Analysis Function, *Data visualisation: testing dashboards for design and accessibility*, https://analysisfunction.civilservice.gov.uk/policy-store/data-visualisation-testing-dashboards-for-design-and-accessibility/
