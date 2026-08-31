# 15.11 Checklist: dall'analisi alla decisione

Prima di chiudere un'analisi importante, possiamo usare una checklist semplice.

## Problema

- La decisione da prendere è chiara?
- Sappiamo chi la deve prendere?
- Abbiamo definito l'orizzonte temporale?
- Conosciamo il costo dell'inazione?

## Evidenza

- Le metriche sono definite correttamente?
- Il grain è coerente con la domanda?
- I dati sono freschi e completi?
- Stiamo distinguendo correlazione e causalità?
- Abbiamo cercato spiegazioni alternative?

## Impatto

- Abbiamo quantificato la dimensione economica o operativa?
- Il finding è materialmente rilevante?
- Quali segmenti spiegano il risultato?
- Quali gruppi potrebbero essere danneggiati?

## Incertezza

- Quali assunzioni governano la raccomandazione?
- Qual è l'intervallo plausibile?
- Abbiamo fatto sensitivity analysis?
- Conosciamo gli switching values principali?
- Quale nuova informazione potrebbe cambiare la decisione?

## Alternative

- Abbiamo considerato almeno una vera alternativa?
- Esiste una soluzione più piccola, economica o reversibile?
- Possiamo fare un pilot?
- Possiamo rinviare parte dell'impegno preservando optionality?

## Decisione

- La soglia di evidenza è proporzionata al rischio?
- Chi è l'owner della decisione?
- Quali sono le condizioni di go/no-go?
- Esistono stop condition e rollback?

## Dopo la decisione

- Come misureremo l'effetto?
- Qual è la baseline?
- Quando faremo la review?
- Abbiamo registrato aspettative e assunzioni prima dell'esito?
- Faremo un post-mortem se il risultato diverge dalle attese?

## La domanda finale

Prima di premere “send”, chiediamoci:

> **Se il decision maker seguisse esattamente la mia raccomandazione, sarei in grado di spiegare perché il livello di evidenza è adeguato al rischio che stiamo assumendo?**

Se la risposta è no, l'analisi non è ancora finita.
