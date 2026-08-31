## 4.14 Standardizzare per confrontare: lo z-score

Confrontare numeri espressi su scale diverse è uno dei problemi più comuni nell'analisi esplorativa. Un valore di 82 può essere alto, basso o perfettamente normale: dipende dalla distribuzione da cui proviene.

Lo **z-score** risponde a una domanda semplice:

> Quanto è distante questa osservazione dalla media, espressa in deviazioni standard?

La formula è:

\[
z = \frac{x - \mu}{\sigma}
\]

Dove `x` è il valore osservato, `μ` la media e `σ` la deviazione standard.

Uno z-score pari a `0` indica un valore uguale alla media. Uno z-score pari a `+2` indica un valore due deviazioni standard sopra la media. Uno z-score pari a `-1,5` indica un valore una deviazione standard e mezza sotto la media.

### Caso: quali negozi stanno davvero performando in modo anomalo?

Una catena retail, che chiameremo **Northstar Retail**, gestisce 84 negozi. Il management vuole identificare i punti vendita con performance eccezionalmente alte o basse.

Il primo report ordina i negozi per fatturato mensile. In cima compare Milano Centro con 1,84 milioni di euro; in fondo Aosta con 210 mila euro.

La conclusione iniziale sembra ovvia: Milano è il negozio migliore, Aosta il peggiore.

Ma i negozi hanno dimensioni, bacini d'utenza e superfici molto differenti. Il team decide allora di osservare il fatturato per metro quadrato all'interno di gruppi omogenei di negozi.

Nel segmento dei negozi urbani grandi:

- media: 1.420 €/m²;
- deviazione standard: 160 €/m²;
- Milano Centro: 1.650 €/m².

Lo z-score di Milano è circa:

\[
(1650 - 1420) / 160 = 1,44
\]

È un risultato molto buono, ma non straordinario.

Nel segmento dei piccoli negozi di provincia:

- media: 910 €/m²;
- deviazione standard: 70 €/m²;
- Aosta: 1.075 €/m².

Lo z-score di Aosta è:

\[
(1075 - 910) / 70 \approx 2,36
\]

Il negozio con il fatturato assoluto più basso è, rispetto al proprio contesto, uno dei migliori dell'intera rete.

### Standardizzare non significa rendere tutto confrontabile

Lo z-score è utile solo se il confronto ha senso. Standardizzare fatturati di negozi profondamente diversi non elimina automaticamente le differenze strutturali.

Prima della formula viene sempre la domanda:

**Qual è la popolazione di riferimento corretta?**

Uno z-score calcolato sull'intera rete potrebbe mischiare flagship store, outlet, piccoli punti vendita turistici e negozi aeroportuali. Il risultato sarebbe matematicamente corretto ma analiticamente debole.

### Z-score e anomalie

È comune usare soglie come `|z| > 2` o `|z| > 3` per segnalare valori insoliti. Non sono leggi universali.

Se la distribuzione è fortemente asimmetrica, multimodale o presenta code pesanti, media e deviazione standard possono descriverla male. In questi casi percentili, IQR o metodi robusti possono essere più appropriati.

Un buon analista non chiede soltanto:

> Quanto è grande lo z-score?

Chiede anche:

> La distribuzione rende sensato usare lo z-score?

Questa distinzione diventerà ancora più importante quando parleremo di probabilità e inferenza statistica.
