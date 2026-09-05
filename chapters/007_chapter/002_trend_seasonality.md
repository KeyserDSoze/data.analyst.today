## 7.1 Baseline temporale, trend e stagionalità: prima di dire “su” o “giù”

Una variazione temporale non ha significato da sola. Dire che le vendite sono scese del 12% è soltanto metà della frase: manca il riferimento rispetto al quale quel movimento viene giudicato. Ieri, la settimana precedente, lo stesso giorno della settimana, lo stesso periodo dell'anno precedente, il budget e un forecast stagionale possono produrre letture molto diverse dello stesso valore.

Il primo lavoro dell'analista temporale non è quindi scegliere un modello. È costruire una **baseline comparabile**: un riferimento che rappresenti in modo credibile ciò che ci saremmo aspettati date le condizioni del processo.

Dentro questa baseline convivono strutture diverse. Un **trend** è un movimento persistente di fondo; la **stagionalità** è un pattern che tende a ripetersi a periodicità relativamente stabile; un **ciclo** può durare a lungo senza avere un calendario fisso; festività mobili, payday, promozioni, scioperi o grandi eventi introducono invece effetti di calendario noti ma non necessariamente regolari. NIST tratta proprio stagionalità, run sequence, seasonal subseries e autocorrelazione come strumenti per rendere visibili queste strutture.[^nist-seasonality]

### Caso simulato/composito — L'e-commerce che “cresce del 31%”

A gennaio un e-commerce di elettronica presenta:

| Periodo | Ricavi |
| --- | ---: |
| Ottobre | 12,4 M€ |
| Novembre | 15,8 M€ |
| Dicembre | 16,2 M€ |
| Gennaio | 16,3 M€ |

Da ottobre a gennaio la crescita è circa **+31%**. Il CEO collega il miglioramento al nuovo motore di raccomandazione lanciato in ottobre. La sequenza è plausibile, ma il calendario racconta una storia più prudente: nei tre anni precedenti novembre e dicembre avevano sempre mostrato picchi legati a Black Friday e Natale, mentre gennaio rimaneva sostenuto dai saldi.

Quando l'analista confronta gennaio con gennaio, ottiene:

| Gennaio | Ricavi |
| --- | ---: |
| 2024 | 14,9 M€ |
| 2025 | 15,5 M€ |
| 2026 | 16,3 M€ |

La crescita anno su anno è circa **+5,2%**. Nessuno dei due numeri è aritmeticamente falso. Il +31% descrive un movimento dentro una finestra fortemente stagionale; il +5,2% prova almeno a confrontare periodi più simili. Nemmeno quest'ultimo numero, però, dimostra l'effetto causale del motore di raccomandazione: prezzi, traffico, assortimento, campagne e mix possono essere cambiati insieme.

Questo è il punto: una baseline migliore riduce una fonte di confusione, non trasforma automaticamente il confronto in causalità.

### Quando anche lo year-over-year inganna

Lo stesso periodo dell'anno precedente è spesso un buon riferimento, ma non una legge. Pasqua può cadere in una settimana diversa, Black Friday può spostarsi dentro il mese, il numero di giorni lavorativi può cambiare, un leap year può aggiungere un giorno e una promozione eccezionale può esistere in un solo anno. Se il business è cresciuto molto, inoltre, lo stesso valore assoluto può avere un significato completamente diverso.

Un'azienda B2B, per esempio, vede le fatture di maggio scendere del 4% anno su anno e interpreta il movimento come pipeline commerciale più debole. Dopo aver normalizzato per i giorni lavorativi, le fatture per giorno risultano invece **+1,8%**. Il totale mensile resta rilevante per capacità e cassa; il rate giornaliero è più informativo se la domanda è confrontare il ritmo commerciale. La baseline dipende dalla decisione.

Anche la scala può cambiare il modo in cui leggiamo la stagionalità. Se un e-commerce raddoppia di dimensione, un picco natalizio può passare da +200.000 € a +400.000 € pur restando quasi identico in termini percentuali. In processi di questo tipo una scala logaritmica o una struttura moltiplicativa può rappresentare meglio ciò che resta stabile.

Per questo una dashboard robusta può avere più riferimenti, purché il loro ruolo sia chiaro:

| Baseline | Domanda |
| --- | --- |
| periodo precedente | cosa è cambiato recentemente? |
| stesso periodo stagionale | siamo diversi dal pattern ricorrente? |
| budget/target | stiamo rispettando il piano? |
| forecast | il dato è insolito rispetto a ciò che il modello attendeva? |

Non serve mostrare tutto contemporaneamente. Serve poter completare una frase difendibile:

> **La metrica ______ è cambiata di ______ rispetto alla baseline ______, scelta perché ______. Il confronto tiene conto di ______ e non controlla ancora per ______.**

Una volta stabilito rispetto a quale passato il presente è davvero diverso, possiamo fare la domanda successiva: **quanto il processo conserva memoria da un periodo all'altro?**

[^nist-seasonality]: NIST/SEMATECH e-Handbook of Statistical Methods, “Seasonality”, https://www.itl.nist.gov/div898/handbook/pmc/section4/pmc443.htm
