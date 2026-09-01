## 4.2 Variabilità: la media dice dove siamo, la dispersione dice quanto possiamo fidarci del centro

Due processi possono avere la stessa media e produrre esperienze completamente diverse.

Per questo una misura di posizione dovrebbe quasi sempre essere accompagnata da una misura di **dispersione**.

### Caso simulato/composito — Due magazzini con la stessa produttività media

Due centri logistici processano in media **118 ordini per addetto al giorno**.

Se guardiamo soltanto la media, sembrano equivalenti.

Nelle ultime sei settimane, però:

- nel magazzino A quasi tutti i valori giornalieri cadono tra 108 e 128;
- nel magazzino B alcuni giorni scendono a 65 e altri superano 170.

Il secondo processo non ha necessariamente lavoratori "più eterogenei". La variabilità potrebbe derivare da turni, mix di ordini, sistemi, domanda, staffing o altre condizioni operative.

Ciò che possiamo dire descrittivamente è più semplice:

> **la media rappresenta molto meglio il comportamento abituale del magazzino A che quello del magazzino B.**

Per Operations questa differenza è concreta: capacità di pianificazione, buffer, SLA e rischio di picchi dipendono dalla dispersione, non solo dal valore medio.

### Range: intuitivo ma fragile

Il **range** è:

```text
massimo - minimo
```

È facile da leggere, ma dipende interamente da due osservazioni. Un singolo valore eccezionale può farlo esplodere.

È quindi utile soprattutto come primo controllo, non come unica misura di variabilità.

### Varianza e deviazione standard

La **varianza** riassume gli scarti quadratici dalla media.

La **deviazione standard** è la radice quadrata della varianza e torna nell'unità originale della variabile.

Il suo vantaggio è che incorpora tutte le osservazioni. Il limite è lo stesso della media: valori estremi possono influenzarla molto.

Dire:

```text
media = 100
SD = 4
```

racconta un processo molto diverso da:

```text
media = 100
SD = 38
```

anche se il valore centrale coincide.

### IQR: la dispersione della metà centrale

L'**interquartile range** è:

```text
IQR = Q3 - Q1
```

e descrive la larghezza del 50% centrale della distribuzione.

È meno influenzato dalle code e diventa particolarmente utile quando il fenomeno è asimmetrico.

Media + deviazione standard e mediana + IQR non sono coppie rivali. Sono due modi di descrivere aspetti differenti della distribuzione.

### Coefficiente di variazione: confrontare dispersione relativa

Quando le grandezze hanno scale molto diverse, possiamo incontrare il **coefficiente di variazione**:

```text
CV = deviazione standard / media
```

Una deviazione standard di 10 euro è enorme rispetto a una media di 20 e piccola rispetto a una media di 2.000.

Il CV può aiutare a esprimere la dispersione in termini relativi, ma non va usato meccanicamente. Diventa difficile da interpretare quando la media è vicina a zero o quando la scala non possiede uno zero significativo.

### Variabilità non significa automaticamente rumore

Una distribuzione ampia può nascondere:

- segmenti differenti;
- stagionalità;
- processi operativi diversi;
- concentrazione di rischio;
- comportamento reale dei clienti;
- errori di misura già identificati nella Data Readiness Review.

L'EDA non deve "ridurre la variabilità". Deve capire **come è organizzata**.

Se la deviazione complessiva è elevata ma ogni segmento è stabile, la dispersione aggregata potrebbe essere soprattutto una questione di composizione. Se ogni segmento è a sua volta instabile, il fenomeno è diverso.

### Un modo migliore di comunicare

Invece di:

> Il tempo medio di evasione è 4,2 ore.

potremmo dire:

> Il tempo mediano è 3,7 ore; metà degli ordini cade tra 2,8 e 5,1 ore, mentre una coda di casi molto lenti porta la media a 4,2.

La seconda frase racconta il comportamento della distribuzione, non soltanto il suo centro.

> **La dispersione non è un dettaglio statistico attorno alla media. È spesso la parte del fenomeno che determina rischio, capacità e qualità dell'esperienza.**