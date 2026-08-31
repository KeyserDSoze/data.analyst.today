## 10.16 Checklist operativa per modelli predittivi

Prima di considerare un modello “pronto”, verifica l'intero percorso.

### Problema

- Qual è la decisione che il modello deve supportare?
- Il target rappresenta davvero quella decisione?
- Qual è l'orizzonte temporale della previsione?
- Qual è l'unità di previsione: cliente, ordine, transazione, account, macchina?

### Dati

- Le feature sono disponibili **al momento della previsione**?
- Esistono feature che contengono informazione futura?
- Il target è costruito senza leakage?
- Missing, categorie rare e anomalie sono gestiti in modo coerente?
- Il training set rappresenta la popolazione futura?

### Validation

- Lo split simula il deployment reale?
- Serve uno split temporale o per gruppo?
- La performance è stabile tra fold, segmenti e periodi?
- Il test finale è rimasto indipendente dal tuning?

### Modello

- Esiste una baseline semplice?
- Il modello complesso migliora davvero la generalizzazione?
- Il gap training-validation è ragionevole?
- La regularizzazione è stata valutata?
- La complessità aggiunta è giustificata dal valore ottenuto?

### Metriche

- La metrica scelta riflette il problema business?
- Nei problemi sbilanciati hai controllato precision e recall?
- Hai verificato calibration?
- La soglia è scelta sulla base dei costi e della capacità operativa?

### Interpretazione

- Le feature importance sono calcolate su dati adeguati?
- Hai evitato di presentarle come cause?
- Hai controllato feature correlate e proxy?
- Sai spiegare quali informazioni usa il modello?

### Deployment

- Chi è il proprietario del modello?
- Come vengono trasformati gli score in azioni?
- La capacità operativa è coerente con il volume di alert?
- Esiste un fallback se il modello non è disponibile?
- Esiste una procedura di rollback?

### Monitoring

- Controlli qualità dei dati?
- Controlli data drift?
- Controlli distribuzione degli score?
- Controlli calibration e performance quando arrivano le label?
- Controlli metriche business downstream?
- Sai quando fare retraining?

### La domanda finale

Prima di approvare un modello, prova a completare questa frase:

> “Se il modello sbaglia, la conseguenza concreta è…”

Se non sai rispondere, non hai ancora collegato davvero il modello alla decisione.