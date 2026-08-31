# 15.7 Decision threshold: quando l'evidenza è sufficiente per agire

Una delle domande più difficili nel lavoro analitico non è:

> “Qual è la risposta?”

ma:

> **“Quanta evidenza ci serve prima di prendere una decisione?”**

Ogni decisione ha una soglia implicita.

Se il costo di un falso positivo è basso e l'azione è reversibile, possiamo agire con meno certezza.

Se invece la decisione è costosa, irreversibile o impatta clienti, persone o compliance, la soglia deve salire.

## La soglia dipende dall'azione, non solo dal dato

Immaginiamo due casi.

### Caso A — Cambiare il testo di una landing page

Costo: basso.

Reversibilità: alta.

Rischio: limitato.

Possiamo accettare una soglia di evidenza relativamente modesta e testare rapidamente.

### Caso B — Chiudere un canale di acquisizione da 12 milioni di euro l'anno

Costo potenziale: molto alto.

Reversibilità: media.

Rischio strategico: alto.

Qui non basta una correlazione osservata in un dashboard.

## Decision threshold come trade-off tra errori

Possiamo pensare alla soglia decisionale in termini di due errori:

- **agire quando non avremmo dovuto**;
- **non agire quando avremmo dovuto**.

La scelta dipende da quale errore costa di più.

Un sistema antifrode tollererà probabilmente una certa quota di falsi positivi se il costo delle frodi non intercettate è enorme.

Un sistema che blocca automaticamente utenti legittimi deve invece considerare con molta più attenzione il costo del falso positivo.

## Caso realistico: il pricing di Meridian Cloud

Meridian Cloud vede una riduzione del conversion rate nel segmento SMB dopo un aumento prezzi.

L'analisi iniziale stima:

- conversione: -2,1 punti percentuali;
- ARPU: +11%;
- ricavo netto per visitor: +4,3%.

Un manager propone di annullare subito l'aumento.

Ma la decisione corretta non dipende solo dal calo di conversione.

Bisogna chiedere:

- il revenue per visitor è migliorato?
- il churn successivo è aumentato?
- il segmento è strategico?
- il nuovo prezzo riduce support cost o aumenta ticket?
- l'effetto è temporaneo o persistente?

Il fatto che una metrica peggiori non significa che la decisione complessiva sia sbagliata.

## Una regola pratica

La soglia di evidenza dovrebbe crescere con:

- costo della decisione;
- irreversibilità;
- impatto su persone;
- incertezza causale;
- dipendenza da assunzioni fragili;
- difficoltà di rollback.

E dovrebbe diminuire quando:

- il test è economico;
- l'azione è reversibile;
- possiamo imparare rapidamente dal risultato;
- il costo dell'inazione è alto.

**Non esiste una soglia universale di “abbastanza evidenza”. Esiste una soglia coerente con il rischio della decisione.**
