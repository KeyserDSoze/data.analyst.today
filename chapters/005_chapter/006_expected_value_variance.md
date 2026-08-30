## 5.5 Valore atteso e varianza: stessa media, decisione diversa

Il valore atteso riassume il risultato medio che ci aspetteremmo se un processo incerto potesse essere ripetuto molte volte.

Per una variabile discreta:

\[
E[X]=\sum_x x\,P(X=x)
\]

Nel business il valore atteso compare continuamente, anche quando non viene chiamato così.

Quando stimiamo il ricavo atteso di una campagna, il costo atteso di un guasto, il margine atteso di un portafoglio clienti o la perdita attesa per frode, stiamo combinando esiti possibili e probabilità.

### Caso realistico: due campagne con lo stesso ROI atteso

Un e-commerce deve scegliere tra due campagne promozionali.

La campagna A ha questi possibili esiti:

| Esito | Probabilità | Margine incrementale |
|---|---:|---:|
| Debole | 20% | 20.000 € |
| Normale | 60% | 80.000 € |
| Ottimo | 20% | 140.000 € |

Il valore atteso è:

\[
0,2\cdot20.000+0,6\cdot80.000+0,2\cdot140.000=80.000\,€
\]

La campagna B ha invece:

| Esito | Probabilità | Margine incrementale |
|---|---:|---:|
| Fallimento | 45% | -40.000 € |
| Buono | 10% | 80.000 € |
| Eccezionale | 45% | 200.000 € |

Anche qui il valore atteso è:

\[
0,45\cdot(-40.000)+0,10\cdot80.000+0,45\cdot200.000=80.000\,€
\]

Stesso valore atteso. Decisione completamente diversa.

La campagna A è relativamente stabile. La B è molto più rischiosa.

Se l'azienda ha poca liquidità, il 45% di probabilità di perdere 40.000 euro può essere inaccettabile. Se invece ha un portafoglio ampio di campagne indipendenti e può assorbire la volatilità, la B può diventare interessante.

### La varianza misura la dispersione attorno al valore atteso

La varianza di una variabile casuale è:

\[
Var(X)=E[(X-E[X])^2]
\]

La deviazione standard è la radice quadrata della varianza.

Il significato operativo è importante: due strategie con lo stesso valore medio possono produrre livelli di incertezza molto diversi.

### Caso realistico: forecasting della domanda

Due SKU hanno entrambi domanda media giornaliera di 120 unità.

SKU A:

- deviazione standard: 8 unità;
- domanda quasi sempre tra 105 e 135.

SKU B:

- deviazione standard: 47 unità;
- frequenti giornate sotto 60 o sopra 190.

Se il planner guarda soltanto la media, assegna a entrambi stock simili.

Ma il secondo SKU richiede più safety stock oppure una politica di riordino diversa.

La variabilità è parte della decisione.

### Il valore atteso non è una promessa

Supponiamo che una startup valuti un progetto con:

- 90% di probabilità di perdere 50.000 euro;
- 10% di probabilità di guadagnare 600.000 euro.

Il valore atteso è positivo:

\[
0,9\cdot(-50.000)+0,1\cdot600.000=15.000\,€
\]

Ma un solo progetto non verrà ripetuto infinite volte.

Il valore atteso da solo non risolve quindi la decisione. Servono anche:

- capacità di assorbire la perdita;
- frequenza con cui la decisione si ripete;
- dipendenza tra i rischi;
- vincoli di cassa;
- asimmetria delle conseguenze;
- utilità reale dei diversi esiti.

### Expected loss

In risk management è frequente ragionare in termini di perdita attesa.

Se una frode ha:

- probabilità 0,3%;
- perdita media 1.400 euro;

la perdita attesa per transazione è:

\[
0,003\cdot1.400=4,20\,€
\]

Questo numero può essere confrontato con il costo di una verifica manuale, di un controllo aggiuntivo o di un'assicurazione.

Ancora una volta il dato diventa decisione quando colleghiamo probabilità e conseguenza economica.

### La lezione

Una media senza dispersione è incompleta.

Un valore atteso senza distribuzione degli esiti può essere pericoloso.

Quando confrontiamo decisioni in condizioni di incertezza, chiediamo sempre:

**Qual è il risultato atteso? Quanto varia? Quanto è grave la coda negativa? Quante volte possiamo ripetere la decisione?**

È questa combinazione, non una singola metrica, che rende il ragionamento utile.
