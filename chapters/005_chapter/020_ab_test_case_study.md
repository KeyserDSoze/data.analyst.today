## 5.19 Caso studio: l'A/B test che sembrava vincente

Una piattaforma e-commerce introduce una nuova pagina prodotto. L'obiettivo è aumentare la probabilità che un visitatore aggiunga un articolo al carrello e completi l'acquisto.

Il test dura 14 giorni.

Risultati grezzi:

| Metrica | Controllo | Variante |
|---|---:|---:|
| Utenti | 246.180 | 245.940 |
| Conversion rate | 4,82% | 5,01% |
| AOV | 71,40 € | 70,95 € |
| Revenue per visitor | 3,44 € | 3,55 € |
| Return rate | 7,9% | 9,6% |

La conversione cresce di 0,19 punti percentuali. Il p-value sulla conversione è 0,028.

La prima reazione è prevedibile: la variante vince.

### Il problema della metrica primaria

Prima del test, il team aveva definito come metrica primaria il revenue per visitor, non la conversione. La nuova pagina doveva aumentare il valore economico per visita, non semplicemente gli ordini.

Sul revenue per visitor l'effetto è positivo, ma l'intervallo di confidenza è ampio e il risultato non è conclusivo al livello scelto dal team.

Inoltre, il return rate aumenta di 1,7 punti percentuali.

Quando il team calcola il revenue netto dopo i resi, il vantaggio della variante si riduce quasi completamente.

### Il problema dei segmenti

Il product manager nota che su mobile la conversione cresce ancora di più e propone di lanciare almeno lì.

Il team analitico segmenta i risultati:

- desktop;
- mobile web;
- iOS;
- Android;
- nuovi utenti;
- utenti returning;
- traffico organico;
- paid search;
- paid social;
- direct.

Alcuni segmenti mostrano effetti molto positivi, altri negativi.

Ma questa segmentazione non era stata definita prima del test. Diventa quindi analisi esplorativa, utile per generare ipotesi, non per dichiarare vincitori definitivi.

### Il problema temporale

L'EDA per giorno mostra un altro dettaglio. Nei primi quattro giorni la variante performa molto bene. Nei giorni successivi la differenza si riduce.

Il lancio del test era coinciso con una campagna promozionale su una categoria premium. La variante mostrava più chiaramente contenuti editoriali e immagini di quella categoria, beneficiando in modo particolare della campagna.

Quindi una parte dell'effetto iniziale era legata al mix di traffico e prodotto.

### Il problema della novità

Una nuova interfaccia può generare comportamenti temporanei. Alcuni utenti esplorano di più perché la pagina è nuova; altri possono essere inizialmente disorientati.

Un test breve può catturare un novelty effect che non persiste nel lungo periodo.

### La decisione finale

Il team non dichiara la variante vincente né la scarta.

Decide di:

1. mantenere la conversione come metrica diagnostica ma non come unico criterio;
2. usare revenue netto per visitor come metrica economica principale;
3. estendere il test per coprire un ciclo promozionale completo;
4. monitorare return rate come guardrail;
5. predefinire due segmenti di interesse per il test successivo;
6. evitare conclusioni definitive dai segmenti scoperti a posteriori.

Dopo altre tre settimane, l'effetto sulla conversione resta positivo ma più piccolo: +0,11 punti percentuali. Il return rate rimane più alto di circa +1,2 punti. Il revenue netto per visitor è praticamente invariato.

La variante non viene lanciata.

### Perché questo test è utile

Un analyst inesperto avrebbe potuto fermarsi a:

> p = 0,028, quindi la variante vince.

Un analyst più maturo guarda invece:

- metrica primaria;
- effect size;
- intervallo di confidenza;
- guardrail metrics;
- costo economico;
- multiple testing;
- stabilità temporale;
- segmentazione;
- coerenza con la domanda iniziale.

Il vero lavoro dell'analista non è ottenere un p-value. È evitare che un numero statisticamente interessante diventi una decisione economicamente sbagliata.
