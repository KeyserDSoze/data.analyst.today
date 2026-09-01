## 4.8 Covarianza, correlazione e scala: il numero dipende dall'unità, la struttura no

La **covarianza** misura se due variabili tendono a deviare dalla propria media nella stessa direzione.

È positiva quando valori sopra la media di una variabile tendono ad accompagnarsi a valori sopra la media dell'altra, negativa quando le deviazioni vanno in direzioni opposte.

Come idea è fondamentale.

Come numero di business, è spesso poco interpretabile perché dipende dalle unità di misura.

Se trasformiamo ricavi da euro a centesimi, la relazione economica non cambia ma la covarianza cambia scala.

La correlazione di Pearson può essere vista come una covarianza standardizzata:

```text
correlazione = covarianza / (SD_X × SD_Y)
```

Per questo è adimensionale e resta tra `-1` e `1`.

### Caso simulato/composito — Due città e una conclusione troppo veloce

Una società di delivery confronta ordini giornalieri e rider attivi:

```text
Torino:  covarianza molto più alta
Bologna: covarianza più bassa
```

Il team interpreta il risultato come:

> Torino dipende molto di più dal numero di rider.

Ma Torino ha quasi il doppio del volume medio.

La scala amplifica la covarianza.

La correlazione racconta:

```text
Torino:  0,63
Bologna: 0,79
```

Questo non dimostra che aggiungere rider produca più ordini a Bologna. Mostra soltanto che, **in termini standardizzati**, le due variabili si muovono più strettamente insieme nel campione bolognese.

### Standardizzare risolve la scala, non il contesto

Portare due variabili su scala standardizzata non rende automaticamente sensato il confronto.

Possiamo confrontare tecnicamente:

- temperatura;
- fatturato;
- numero di ticket;
- churn rate.

Ma il fatto che tutti abbiano uno z-score o una correlazione non crea un significato comune.

Restano domande come:

- la popolazione di riferimento è corretta?
- il periodo è comparabile?
- i segmenti sono mescolati?
- esiste un trend comune?
- la relazione è lineare?

Queste condizioni contano molto più dell'eleganza della standardizzazione.

### La covarianza come concetto, non come KPI

Per il Data Analyst è utile ricordare soprattutto questo:

> **correlazione e covarianza descrivono movimento congiunto, non importanza economica e non causalità.**

Una correlazione piccola su una variabile ad altissimo valore può essere economicamente importante. Una correlazione elevata può essere operativamente irrilevante.

Non esiste una soglia universale del tipo:

```text
r > 0,7 = importante
```

L'importanza dipende dalla domanda, dalla robustezza del pattern e dalla decisione che potrebbe cambiare.

### Una regola pratica

Usa la covarianza per capire l'idea del movimento congiunto.

Usa la correlazione quando una scala standardizzata aiuta il confronto.

Usa sempre grafici e contesto prima di attribuire significato al coefficiente.

> **Standardizzare un numero elimina l'unità. Non elimina le assunzioni.**