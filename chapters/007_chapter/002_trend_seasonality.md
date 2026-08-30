## 7.1 Trend, stagionalità e cicli: non tutto ciò che si ripete è rumore

Una serie temporale può muoversi per ragioni diverse contemporaneamente. Un modo utile per iniziare è pensare a tre componenti:

- **trend**: movimento di fondo nel medio-lungo periodo;
- **stagionalità**: pattern che si ripetono con periodicità relativamente stabile;
- **residuo**: ciò che resta dopo aver spiegato le strutture sistematiche principali.

In alcuni contesti è utile distinguere anche i **cicli**, che possono durare mesi o anni ma non hanno necessariamente una periodicità rigida.

Il NIST descrive la stagionalità come una fluttuazione periodica e mostra come possa essere individuata con grafici temporali, seasonal subseries plot, box plot per periodo e autocorrelazione.

### Caso: un e-commerce che “cresce del 31%”

A gennaio 2026, un e-commerce di elettronica presenta al board questo dato:

| Periodo | Ricavi |
|---|---:|
| Ottobre | 12.4 M€ |
| Novembre | 15.8 M€ |
| Dicembre | 16.2 M€ |
| Gennaio | 16.3 M€ |

Da ottobre a gennaio il business sembra cresciuto di circa il 31%.

Il CEO chiede se il nuovo motore di raccomandazione lanciato a ottobre stia funzionando.

L'analista evita di rispondere direttamente. Recupera tre anni di dati mensili e osserva che ogni anno novembre e dicembre salgono fortemente per Black Friday e Natale, mentre gennaio rimane alto per i saldi.

Confrontando gennaio anno su anno:

| Gennaio | Ricavi |
|---|---:|
| 2024 | 14.9 M€ |
| 2025 | 15.5 M€ |
| 2026 | 16.3 M€ |

La crescita 2026 vs 2025 è circa +5.2%, non +31%.

Il motore di raccomandazione potrebbe comunque avere un effetto, ma il confronto ottobre-gennaio non permette di isolarlo.

### Pattern settimanali

La stagionalità non è solo annuale. Un marketplace può avere:

- meno ordini il lunedì;
- picco il venerdì sera;
- più cancellazioni la domenica;
- maggiore utilizzo dell'app durante il tragitto casa-lavoro.

Se confrontiamo il lunedì corrente con la domenica precedente, possiamo interpretare come deterioramento ciò che è semplicemente un pattern settimanale.

### Eventi di calendario

Una serie può inoltre essere influenzata da:

- festività mobili;
- payday;
- Black Friday;
- fine trimestre;
- chiusure aziendali;
- eventi sportivi;
- campagne promozionali;
- cambi normativi;
- scioperi;
- condizioni meteo eccezionali.

Questi eventi non sono necessariamente “stagionalità” nel senso stretto. Spesso sono regressori esterni o eventi speciali da trattare esplicitamente.

### Regola operativa

Prima di dichiarare che una metrica sta crescendo o diminuendo, chiedi:

1. rispetto a quale periodo?
2. il periodo è comparabile?
3. esiste una stagionalità nota?
4. ci sono festività o campagne diverse?
5. il mix di clienti/prodotti/canali è cambiato?

> **Una variazione temporale non ha significato senza un baseline appropriato.**

## Fonti

- NIST, *Seasonality*: https://itl.nist.gov/div898/handbook/pmc/section4/pmc443.htm
- NIST, *Common Approaches to Univariate Time Series*: https://www.itl.nist.gov/div898/handbook/pmc/section4/pmc444.htm
