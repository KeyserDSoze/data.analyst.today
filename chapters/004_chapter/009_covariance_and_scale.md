## 4.8 Covarianza, correlazione e scala: standardizzare il numero non standardizza il problema

La covarianza aiuta a capire un'idea fondamentale: due variabili possono tendere a deviare dalla propria media nella stessa direzione o in direzioni opposte. È positiva quando valori sopra la media di una variabile si accompagnano spesso a valori sopra la media dell'altra, negativa quando accade il contrario.

Come intuizione è preziosa. Come numero di business, però, è difficile da confrontare perché dipende dalle unità di misura. Se trasformiamo ricavi da euro a centesimi, il fenomeno economico non cambia ma la covarianza sì. La correlazione di Pearson elimina questa dipendenza standardizzando la covarianza:

```text
correlazione = covarianza / (SD_X × SD_Y)
```

Il risultato diventa adimensionale e resta tra `-1` e `1`. Ma eliminare l'unità non elimina il contesto.

Immaginiamo una società di delivery che confronti ordini giornalieri e rider attivi a Torino e Bologna. La covarianza è molto più alta a Torino e il team conclude che quella città “dipende di più” dal numero di rider. Torino, però, ha quasi il doppio del volume medio. La scala amplifica naturalmente il movimento congiunto.

La correlazione produce invece:

```text
Torino:  0,63
Bologna: 0,79
```

Ora possiamo dire che, **in termini standardizzati**, le due variabili si muovono più strettamente insieme nel campione bolognese. Non possiamo ancora dire che aggiungere rider produca più ordini a Bologna. La standardizzazione ha risolto un problema di scala, non un problema di interpretazione.

Questo principio vale più in generale. Possiamo trasformare temperatura, fatturato, ticket e churn rate in z-score o coefficienti adimensionali, ma restano aperte le domande decisive: le popolazioni sono confrontabili? il periodo è lo stesso? esiste un trend comune? i segmenti sono mescolati? la relazione è lineare? la metrica rappresenta la stessa cosa nei due gruppi?

Per questo la covarianza è soprattutto utile per comprendere il concetto di movimento congiunto, mentre la correlazione è utile quando una scala standardizzata rende più leggibile il confronto. Nessuna delle due misura automaticamente importanza economica. Una correlazione modesta può riguardare un fenomeno da milioni di euro; una correlazione molto alta può descrivere una relazione operativamente irrilevante.

Non esiste quindi una soglia universale come `r > 0,7 = importante`. La rilevanza dipende dalla domanda, dalla robustezza del pattern, dalla popolazione a cui si applica e dalla decisione che potrebbe cambiare.

La sezione successiva aggiunge una delle fonti di contesto più importanti: il tempo. Due variabili possono muoversi insieme non perché una spieghi l'altra, ma perché entrambe seguono lo stesso calendario o trend.

> **Standardizzare un numero elimina l'unità. Non elimina le assunzioni che rendono quel numero interpretabile.**
