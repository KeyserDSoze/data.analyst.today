## 5.15 Il p-value: cosa dice e, soprattutto, cosa non dice

Il p-value è probabilmente uno dei numeri più usati e più fraintesi dell'analisi quantitativa.

La definizione operativa è questa: assumendo che l'ipotesi nulla sia vera, il p-value misura quanto sarebbe insolito osservare un risultato almeno altrettanto estremo di quello ottenuto.

Non è la probabilità che l'ipotesi nulla sia vera. Non è la probabilità che il risultato sia dovuto al caso. Non è la probabilità che l'esperimento sia corretto. E non misura la grandezza dell'effetto.

### Caso realistico: p = 0,03 e una decisione da 2 milioni di euro

Un retailer europeo testa un nuovo algoritmo di raccomandazione. Il test coinvolge circa 1,4 milioni di sessioni. Il valore medio dell'ordine passa da 63,84 euro a 63,97 euro.

Differenza: 0,13 euro.

Il p-value risulta 0,03.

La prima slide preparata per il management contiene una frase semplice:

> Il nuovo algoritmo migliora significativamente l'average order value.

Statisticamente, il risultato può essere incompatibile con l'ipotesi di effetto esattamente nullo a un livello convenzionale del 5%. Ma questa frase lascia fuori quasi tutto ciò che serve per decidere.

L'implementazione completa del nuovo sistema costa 2 milioni di euro l'anno tra licenze, infrastruttura e manutenzione. L'incremento atteso di margine, dopo aver considerato resi e costi di serving, è stimato in circa 480.000 euro.

Il problema non è che p = 0,03 sia sbagliato. Il problema è usarlo come se significasse "il progetto conviene".

### La soglia 0,05 non è una legge naturale

La convenzione p < 0,05 è diventata così familiare da sembrare una frontiera oggettiva tra vero e falso. Non lo è.

Un risultato con p = 0,049 e uno con p = 0,051 sono praticamente indistinguibili dal punto di vista dell'evidenza, eppure processi decisionali troppo meccanici possono trattarli come opposti.

La American Statistical Association ha esplicitamente ricordato che conclusioni scientifiche, di business o di policy non dovrebbero dipendere esclusivamente dal superamento di una soglia di p-value. Ha inoltre chiarito che il p-value non misura la dimensione dell'effetto né la sua importanza pratica.[^asa-p]

### Il p-value dipende anche dalla dimensione del campione

Con campioni enormi, differenze minuscole possono produrre p-value piccoli. Con campioni piccoli, effetti economicamente importanti possono produrre p-value grandi.

Immaginiamo due test sul churn.

Esperimento A:

- 2.000.000 di clienti;
- churn controllo: 8,000%;
- churn trattamento: 7,950%;
- differenza: -0,05 punti percentuali.

Esperimento B:

- 1.200 clienti;
- churn controllo: 8,0%;
- churn trattamento: 6,4%;
- differenza: -1,6 punti percentuali.

È possibile che A produca un p-value molto più piccolo di B, pur avendo un effetto molto meno interessante per il business.

### Una migliore domanda da fare

Invece di chiedere soltanto:

> È statisticamente significativo?

un analyst dovrebbe chiedere:

> Quanto è grande l'effetto? Quanto è incerto? È compatibile con un beneficio economicamente rilevante? Quanto costa sbagliare decisione?

Queste domande spostano l'attenzione dal rituale statistico alla decisione.

### Una frase da evitare

"Il p-value è 0,18, quindi non c'è effetto."

Questa conclusione è logicamente troppo forte. Un p-value non piccolo può significare che i dati non forniscono sufficiente evidenza per distinguere l'effetto dal rumore nelle condizioni del test. Non dimostra che l'effetto sia zero.

La formulazione corretta è più simile a:

> Con i dati disponibili non abbiamo evidenza sufficiente per distinguere l'effetto osservato dalla variabilità campionaria; l'intervallo di confidenza include sia effetti piccoli sia effetti potenzialmente rilevanti.

È meno spettacolare, ma molto più utile.

[^asa-p]: American Statistical Association, *Statement on Statistical Significance and P-Values*, https://www.amstat.org/asa/files/pdfs/p-valuestatement.pdf
