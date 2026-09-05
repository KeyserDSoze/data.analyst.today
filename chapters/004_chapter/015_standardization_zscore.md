## 4.14 Z-score: un valore è eccezionale soltanto rispetto a una popolazione

Un numero assoluto non contiene da solo il proprio contesto. `82` può essere enorme, modesto o perfettamente ordinario. Lo **z-score** rende esplicita una forma particolare di confronto: misura la distanza di un'osservazione dalla media della propria distribuzione in unità di deviazione standard.

```text
z = (valore - media) / deviazione standard
```

`z = 0` indica un valore sulla media; `z = +2` un'osservazione due deviazioni standard sopra; `z = -1,5` una posizione una deviazione e mezza sotto. La scala originale scompare, ma soltanto dopo aver scelto **quale popolazione fornisce media e deviazione standard**.

È questa scelta, più della formula, a determinare il significato.

Consideriamo **Northstar Retail**, 84 negozi molto diversi per dimensione e mercato. Un ranking di fatturato assoluto mette Milano Centro a **€1,84M** e Aosta a **€0,21M**. Se interpretiamo il ranking come performance, stiamo confondendo dimensione del negozio e capacità di generare ricavi.

Il team passa allora al fatturato per metro quadrato e definisce peer group comparabili. Nei grandi negozi urbani la media è `€1.420/m²`, la deviazione standard `€160/m²` e Milano Centro raggiunge `€1.650/m²`, circa `z = +1,44`. Nei piccoli negozi di provincia la media è `€910/m²`, SD `€70/m²` e Aosta arriva a `€1.075/m²`, circa `z = +2,36`.

Aosta continua ad avere il fatturato assoluto più basso, ma è molto più eccezionale **rispetto al proprio contesto operativo**. Lo z-score non ha scoperto una verità che il fatturato nascondeva; ha cambiato la domanda da “chi produce più ricavi?” a “chi si discosta maggiormente dai propri peer?”.

## La reference population viene prima della standardizzazione

Possiamo calcolare uno z-score anche mescolando flagship cittadini, outlet, store aeroportuali e piccoli negozi turistici. Il risultato sarà matematicamente valido, ma media e deviazione standard descriveranno un miscuglio di processi. Dichiarare un valore “due sigma sopra la media” non serve a molto se la media di riferimento non rappresenta un confronto sensato.

Per la stessa ragione uno z-score elevato non significa automaticamente “evento quasi impossibile”. Soglie come `|z| > 2` o `|z| > 3` acquistano un'interpretazione probabilistica specifica soltanto sotto assunzioni sulla distribuzione, in particolare quando si invoca la normale. Distribuzioni asimmetriche, multimodali o a code pesanti possono produrre molti valori lontani dalla media senza che siano errori.

Lo z-score rimane comunque utile per confrontare performance relative dentro peer group, evidenziare valori che meritano ispezione, mettere variabili su una scala comune o misurare quanto un valore corrente sia distante da una baseline storica appropriata. Ma standardizzazione e comparabilità non sono sinonimi: non corregge mix, differenze temporali, metriche incoerenti o causalità.

Quando la distribuzione è fortemente asimmetrica, mediana, percentili, IQR o ranking percentile possono descrivere la posizione relativa in modo più robusto. Il box plot della prossima sezione è precisamente uno di questi strumenti: riassume centro e dispersione senza costruire tutto attorno alla media.

> **Uno z-score dice quanto un valore è lontano dal centro della distribuzione di riferimento. La scelta analitica decisiva è quale distribuzione meriti di essere il riferimento.**
