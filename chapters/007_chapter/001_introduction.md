# Capitolo 7 - Serie temporali, anomalie e forecasting

> Una serie temporale non è una tabella con una colonna data. È una sequenza in cui l'ordine degli eventi contiene informazione.

Quando un analista osserva vendite giornaliere, ticket aperti per ora, ordini settimanali, utenti attivi mensili o consumo energetico ogni cinque minuti, non sta più guardando semplicemente un insieme di osservazioni indipendenti. Sta osservando un processo che evolve nel tempo.

Questa differenza cambia il modo in cui dobbiamo ragionare.

Due punti consecutivi possono essere collegati. Un lunedì può assomigliare ad altri lunedì. Dicembre può comportarsi in modo diverso da giugno. Un picco può essere un'anomalia, ma può anche essere Black Friday. Una caduta può indicare un problema commerciale, ma anche una pipeline che non ha caricato metà giornata.

Il NIST sottolinea che le serie temporali possono presentare struttura interna come autocorrelazione, trend e stagionalità e che questa struttura deve essere considerata nell'analisi e nella modellazione.

Questo capitolo non parte dai modelli più sofisticati. Parte da una domanda più importante:

> **Che cosa nel tempo è segnale, che cosa è struttura prevedibile, che cosa è rumore e che cosa potrebbe essere un errore di dato?**

Impareremo a distinguere trend, stagionalità, cicli, shock, autocorrelazione e anomalie; a costruire baseline di forecast; a valutare le previsioni con metriche appropriate; a comunicare intervalli e incertezza; e soprattutto a riconoscere i casi in cui prevedere è possibile ma non utile.

## Un caso realistico: il lunedì in cui “crollano le vendite”

Alle 9:12 di un lunedì mattina il direttore commerciale di una catena retail scrive al team analytics:

> “Le vendite di ieri sono crollate del 24%. Cosa sta succedendo?”

Il dashboard mostra:

| Giorno | Ricavi |
|---|---:|
| Domenica precedente | 1.84 M€ |
| Domenica corrente | 1.40 M€ |
| Variazione | -23.9% |

La prima lettura sembra allarmante.

Ma l'analista controlla tre elementi.

Primo: la domenica precedente coincideva con un weekend promozionale nazionale.

Secondo: confrontando la stessa domenica dell'anno precedente, i ricavi sono in realtà +3.1%.

Terzo: 37 negozi su 412 non hanno ancora inviato la chiusura di cassa della giornata.

Dopo la correzione del caricamento, i ricavi salgono a 1.51 M€. Il confronto corretto non è più -23.9%, ma circa -18% contro una giornata promozionale eccezionale e +4.6% contro la domenica comparabile dell'anno precedente.

La storia è completamente diversa.

Questo caso introduce tre principi che useremo per tutto il capitolo:

1. il confronto temporale deve essere coerente;
2. stagionalità ed eventi speciali possono imitare anomalie;
3. prima di spiegare un movimento bisogna verificare che il dato sia completo.

## Fonti

- NIST/SEMATECH e-Handbook of Statistical Methods, *Introduction to Time Series Analysis*: https://www.itl.nist.gov/div898/handbook/pmc/section4/pmc4.htm
