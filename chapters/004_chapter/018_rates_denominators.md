## 4.17 Conteggi, proporzioni e tassi: il denominatore cambia la storia

Un numero assoluto dice **quanto** è successo. Un tasso prova a dire **quanto è successo rispetto all'esposizione o alla popolazione rilevante**.

È una distinzione semplice e potentissima.

### Caso: il magazzino con più incidenti

La società industriale **IronPeak Components** gestisce tre stabilimenti. Nel trimestre registra questi incidenti di sicurezza:

| Stabilimento | Incidenti |
|---|---:|
| Torino | 18 |
| Verona | 11 |
| Bari | 9 |

Il primo report mette Torino in rosso: ha il doppio degli incidenti di Bari.

Poi un analista aggiunge le ore lavorate:

| Stabilimento | Incidenti | Ore lavorate |
|---|---:|---:|
| Torino | 18 | 610.000 |
| Verona | 11 | 280.000 |
| Bari | 9 | 170.000 |

Se esprimiamo gli incidenti per 100.000 ore lavorate:

- Torino: 2,95;
- Verona: 3,93;
- Bari: 5,29.

La graduatoria si ribalta.

Torino ha più incidenti assoluti perché è il sito più grande. Bari ha il rischio relativo più alto.

### Il denominatore è una scelta analitica

Il CDC definisce un tasso come una misura di un evento in relazione a una popolazione o unità di esposizione e sottolinea che i conteggi sono comparabili direttamente soltanto quando le popolazioni hanno dimensioni simili.[^cdc-rates]

In business analytics lo stesso principio ricompare continuamente.

Non basta sapere:

- 420 resi;
- 1.900 ticket;
- 75 churn;
- 22 frodi;
- 3.100 conversioni.

Serve sapere: **su quanti casi possibili?**

Un return rate può essere:

\[
\frac{resi}{ordini}
\]

oppure:

\[
\frac{unità\ restituite}{unità\ vendute}
\]

Sono due metriche diverse.

Un cliente che compra dieci articoli e ne restituisce uno produce un ordine con reso ma un return rate per unità del 10%.

### Denominatori incoerenti

Un marketplace osserva che il seller A ha 240 reclami e il seller B soltanto 90.

A prima vista A sembra peggiore.

Ma A ha 120.000 ordini e B 18.000.

Reclami per 1.000 ordini:

- A: 2,0;
- B: 5,0.

Se però B vende prodotti molto più complessi e costosi, anche questo confronto potrebbe non essere sufficiente. Potremmo dover normalizzare per categoria, valore dell'ordine o tipologia di cliente.

Il denominatore corretto dipende dalla domanda.

### Quando il denominatore cambia nel tempo

Un altro errore frequente emerge nei trend.

Una piattaforma registra:

- gennaio: 900 cancellazioni;
- giugno: 1.100 cancellazioni.

Le cancellazioni sono aumentate del 22%.

Ma gli abbonati attivi sono passati da 25.000 a 40.000.

Il tasso mensile di cancellazione è quindi passato dal 3,6% al 2,75%.

Il conteggio peggiora, il tasso migliora.

Nessuno dei due è falso. Rispondono a domande diverse.

### Il controllo del denominatore

Prima di interpretare una percentuale, un analista dovrebbe riuscire a completare questa frase senza esitazioni:

> Il numeratore conta __________, il denominatore rappresenta __________, nel periodo __________, per la popolazione __________.

Se non è possibile farlo, la metrica non è ancora sufficientemente definita.

[^cdc-rates]: CDC, “Describing Epidemiologic Data”, *Field Epidemiology Manual*, https://www.cdc.gov/field-epi-manual/php/chapters/describing-epi-data.html
