## 5.10 Errore standard: quanto è stabile una stima

L'errore standard misura la variabilità di una statistica da campione a campione.

Per una media, in condizioni standard:

\[
SE(\bar{x}) = \frac{s}{\sqrt{n}}
\]

La formula è semplice. Le implicazioni sono profonde.

A parità di variabilità dei dati, aumentando la dimensione del campione la stima diventa più stabile. Ma la precisione migliora con la radice quadrata di n, non linearmente.

Raddoppiare il campione non dimezza l'errore standard.

Per dimezzarlo, servono circa quattro volte le osservazioni.

### Caso realistico: il KPI del piccolo mercato che cambia continuamente

Una piattaforma di food delivery confronta il tempo medio di consegna in due città.

Milano:

- 48.200 ordini al mese;
- media: 31,4 minuti;
- deviazione standard: 9,8 minuti.

Parma:

- 620 ordini al mese;
- media: 29,9 minuti;
- deviazione standard: 10,1 minuti.

A prima vista Parma sembra migliore.

La settimana successiva:

- Milano: 31,2 minuti;
- Parma: 33,1 minuti.

Poi Parma scende a 30,4.

Il management inizia a chiedere spiegazioni operative ogni volta che il KPI di Parma si muove di due o tre minuti.

Ma il vero problema è che il KPI di Parma è molto più rumoroso perché è calcolato su un volume molto più piccolo.

La stessa deviazione standard individuale produce una precisione della media molto diversa quando n cambia radicalmente.

### Rumore del processo e incertezza della stima non sono la stessa cosa

La deviazione standard descrive quanto variano le singole osservazioni.

L'errore standard descrive quanto varia la stima ottenuta dal campione.

Sono concetti collegati, ma non equivalenti.

Un processo può avere tempi di consegna molto variabili ma, se osserviamo milioni di ordini, conoscere con grande precisione la sua media.

Al contrario, un processo relativamente stabile può avere una media stimata con poca precisione se osserviamo pochissimi casi.

### Il rischio delle classifiche aziendali

Molte classifiche interne ordinano punti vendita, agenti, stabilimenti o team sulla base di KPI calcolati su volumi molto diversi.

Questo tende a spingere le unità con pochi casi verso gli estremi della classifica.

Non perché siano necessariamente le migliori o le peggiori, ma perché hanno più variabilità campionaria.

Un team con 20 opportunità commerciali può mostrare un win rate del 70% un mese e del 40% quello successivo. Un team con 4.000 opportunità difficilmente oscillerà così tanto senza un cambiamento reale.

### Una domanda da aggiungere alle dashboard

Ogni volta che confronti una metrica tra gruppi, chiediti:

> Qual è il denominatore e quanto è stabile questa stima?

Il numero di osservazioni non deve essere nascosto dietro il KPI.

Spesso è parte integrante del KPI stesso.

### Fonti

[^nist-se]: NIST/SEMATECH e-Handbook of Statistical Methods, *Glossary*, voce “standard error”, https://www.itl.nist.gov/div898/handbook/glossary.htm
