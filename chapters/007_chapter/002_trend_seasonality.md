## 7.1 Baseline temporale, trend e stagionalità: prima di dire “su” o “giù”

Una variazione temporale ha significato solo rispetto a una **baseline**.

Dire che le vendite sono scese del 12% è incompleto finché non sappiamo rispetto a cosa:

- ieri;
- la stessa settimana precedente;
- lo stesso giorno della settimana;
- lo stesso periodo dell'anno precedente;
- il budget;
- un forecast che incorpora calendario e stagionalità.

Il primo lavoro dell'analista temporale non è quindi scegliere un modello. È costruire un confronto che rappresenti ragionevolmente ciò che sarebbe stato atteso.

### Trend, stagionalità, ciclo ed eventi speciali

È utile distinguere quattro strutture.

**Trend** — movimento persistente di fondo nel medio-lungo periodo.

**Stagionalità** — pattern che tende a ripetersi con periodicità relativamente stabile: ora del giorno, giorno della settimana, mese, trimestre.

**Ciclo** — espansioni e contrazioni che possono durare molto, ma non hanno necessariamente una periodicità fissa.

**Calendar/event effect** — festività mobili, promozioni, payday, eventi sportivi, chiusure, scioperi o altri eventi con calendario noto ma non necessariamente regolare.

NIST descrive la stagionalità come una fluttuazione periodica e suggerisce strumenti come run sequence plot, seasonal subseries plot, box plot per periodo e autocorrelazione per renderla visibile.[^nist-seasonality]

### Caso simulato/composito — L'e-commerce che “cresce del 31%”

A gennaio un e-commerce di elettronica presenta:

| Periodo | Ricavi |
| --- | ---: |
| Ottobre | 12,4 M€ |
| Novembre | 15,8 M€ |
| Dicembre | 16,2 M€ |
| Gennaio | 16,3 M€ |

Da ottobre a gennaio: circa +31%.

Il CEO collega il miglioramento al nuovo motore di raccomandazione lanciato in ottobre.

L'analista recupera tre anni di dati. Novembre e dicembre hanno sempre picchi legati a Black Friday e Natale; gennaio rimane sostenuto dai saldi.

Il confronto tra gennaio comparabili è:

| Gennaio | Ricavi |
| --- | ---: |
| 2024 | 14,9 M€ |
| 2025 | 15,5 M€ |
| 2026 | 16,3 M€ |

La crescita anno su anno è circa +5,2%.

Nessuno dei due numeri è aritmeticamente falso. Ma solo uno dei due confronti prova a controllare la stagionalità annuale.

E nemmeno +5,2% dimostra l'effetto del motore di raccomandazione: prodotto, prezzi, traffico, assortimento e campagne possono essere cambiati nello stesso periodo.

### Year-over-year non è sempre la risposta

Il confronto con lo stesso periodo dell'anno precedente è spesso utile, ma può fallire quando:

- Pasqua cambia settimana;
- Black Friday cade in una diversa parte del mese;
- cambia il numero di giorni lavorativi;
- un leap year aggiunge un giorno;
- il business è cresciuto o contratto strutturalmente;
- una promozione eccezionale esiste in un solo anno.

Una baseline deve quindi rispettare **calendario e processo**, non solo la distanza temporale.

### Caso breve — Il mese con un giorno lavorativo in meno

Un'azienda B2B vede le fatture emesse a maggio scendere del 4% anno su anno.

La conclusione iniziale è “pipeline commerciale più debole”.

Dopo aver normalizzato per giorni lavorativi, le fatture per giorno risultano invece +1,8%.

Il totale mensile e il rate giornaliero rispondono a due domande diverse. Per la capacità operativa il totale conta; per confrontare il ritmo commerciale il dato normalizzato può essere più informativo.

### Stagionalità moltiplicativa

In alcuni business l'ampiezza della stagionalità cresce con il livello della serie.

Se un e-commerce raddoppia di dimensione, il picco di Natale può passare da +200.000 € a +400.000 € pur restando simile in termini percentuali.

In questi casi ragionare solo in differenze assolute può far sembrare che la stagionalità stia “peggiorando”. Una scala logaritmica o un modello moltiplicativo può descrivere meglio il fenomeno.

### Baseline multiple per decisioni diverse

Una dashboard temporale robusta può mostrare più di una baseline:

| Baseline | Domanda |
| --- | --- |
| periodo precedente | cosa è cambiato recentemente? |
| stesso periodo stagionale | siamo diversi dal pattern ricorrente? |
| budget/target | stiamo rispettando il piano? |
| forecast | il dato è insolito rispetto a ciò che il modello attendeva? |

Non serve mostrarle tutte in ogni grafico. Serve sapere quale domanda stiamo facendo.

### La regola operativa

Prima di descrivere una variazione temporale completa:

> **La metrica ______ è cambiata di ______ rispetto alla baseline ______, scelta perché ______. Il confronto tiene conto di ______ e non controlla ancora per ______.**

Questa frase impedisce che “+12%” o “-8%” diventino storie senza calendario.

[^nist-seasonality]: NIST/SEMATECH e-Handbook of Statistical Methods, “Seasonality”, https://www.itl.nist.gov/div898/handbook/pmc/section4/pmc443.htm
