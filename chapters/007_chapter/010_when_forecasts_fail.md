## 7.9 Quando non fidarsi del forecast

Un forecast può essere statisticamente ben costruito e comunque diventare rapidamente inutile.

Le serie temporali assumono, in modi diversi a seconda del modello, che il futuro conservi almeno una parte della struttura osservata nel passato. Quando il processo cambia, questa assunzione può rompersi.

### Regime change

Pensiamo a un'azienda di food delivery che abbia addestrato un modello sulla domanda degli ultimi tre anni.

Il modello ha imparato:

- picco il venerdì sera;
- domanda più alta con pioggia;
- calo ad agosto;
- crescita graduale del 12% annuo.

Poi l'azienda modifica radicalmente le fee di consegna.

La domanda cambia quasi immediatamente. Il vecchio pattern non rappresenta più lo stesso processo economico.

Il modello continua a produrre numeri precisi, ma sta proiettando una relazione che non esiste più nelle stesse condizioni.

### Caso realistico: il forecast che non conosceva il nuovo contratto

Una società industriale produce componenti per tre grandi clienti automotive.

Per due anni il forecast mensile ha un errore medio inferiore al 6%. Il modello viene quindi usato per pianificare turni e materie prime.

A gennaio uno dei clienti firma un contratto quadro che sposta il 35% degli ordini verso un concorrente. L'informazione è nota al commerciale, ma non è ancora presente nei dati storici.

Il modello prevede 48.000 pezzi per marzo. Gli ordini reali sono 34.500.

Dal punto di vista matematico il modello ha fatto quello che poteva: ha extrapolato il passato. Dal punto di vista aziendale, però, il forecast era già obsoleto il giorno in cui il contratto è stato firmato.

Questo caso mostra perché il forecasting non può essere separato dal contesto.

### Eventi strutturali che richiedono cautela

Un analista dovrebbe aumentare il livello di attenzione quando compaiono:

- cambi di prezzo;
- acquisizioni o fusioni;
- modifiche importanti al prodotto;
- nuovi competitor;
- cambi normativi;
- pandemie o shock macroeconomici;
- cambiamenti nel tracking;
- migrazioni di sistemi;
- ingresso in nuovi mercati;
- promozioni eccezionali;
- variazioni forti nella capacità produttiva;
- cambiamenti nel mix clienti.

### Forecast e causalità

Un modello può imparare che due segnali anticipano la domanda, ma questo non significa che li abbia interpretati causalmente.

Se per due anni la spesa marketing cresce prima delle vendite, il modello può usare questo pattern. Se l'azienda cambia strategia e investe marketing proprio nei periodi di domanda debole, la relazione storica può invertirsi.

### Drift

Possiamo distinguere almeno tre forme utili di drift:

**Data drift**: cambia la distribuzione degli input.

**Concept drift**: cambia la relazione tra input e outcome.

**Business drift**: cambia il processo reale che genera i dati, magari per una decisione aziendale.

L'ultimo è particolarmente importante per il Data Analyst perché spesso emerge prima nelle conversazioni con business e operations che nei test statistici.

### Un forecast deve avere condizioni di validità

Ogni forecast importante dovrebbe essere accompagnato da alcune assunzioni operative, per esempio:

> La previsione assume prezzi invariati, capacità produttiva stabile e nessuna campagna promozionale straordinaria nel periodo.

Questo non rende la previsione debole. La rende più onesta e utilizzabile.

> **Il modello conosce il passato registrato nei dati. Non conosce automaticamente le decisioni che stanno cambiando il futuro.**
