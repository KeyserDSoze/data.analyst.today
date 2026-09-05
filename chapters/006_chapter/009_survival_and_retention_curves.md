## 6.8 Survival e retention curves: capire quando aumenta il rischio di uscita

Una dashboard può comprimere la retention in pochi punti — D1, D7, D30, M3, M6 — ma due coorti con lo stesso D30 possono avere storie completamente diverse. Una può perdere quasi tutti gli utenti nei primi giorni e poi stabilizzarsi; l'altra può decadere lentamente per tutto il mese.

La curva conserva quindi un'informazione che il singolo KPI elimina: **quando il lifecycle diventa fragile**.

In survival analysis consideriamo un tempo `T` fino a un evento, per esempio cancellazione, mancato rinnovo o guasto. La survival function è:

`S(t) = P(T > t)`

cioè la probabilità di superare il tempo `t` senza aver ancora osservato l'evento. NIST usa la stessa definizione nella reliability analysis.[^nist-survival] Nel lifecycle possiamo leggerla come la quota/probabilità che la relazione sopravviva oltre un certo punto del tempo.

### Streamly: il problema non era “nelle prime settimane”, ma vicino alla prima fatturazione

**Streamly**, servizio subscription di corsi video professionali, mostra retention **D7 76%**, **D30 58%**, **D90 43%**. Il Product Manager parla genericamente di deterioramento nelle prime settimane.

La curva giornaliera mostra qualcosa di più preciso: la discesa è relativamente regolare fino al giorno 18, poi accelera tra il giorno 19 e il giorno 24. Il trial gratuito dura **21 giorni**.

La domanda cambia immediatamente: che cosa succede quando l'utente si avvicina alla prima fatturazione? La segmentazione per esperienza precedente aggiunge un altro indizio: chi completa almeno un corso entro D14 ha retention D45 del **71%**, chi non ne completa nessuno del **29%**. Il pattern non dimostra ancora una causa, ma collega il momento di rischio a un possibile problema di valore non ancora raggiunto.

### Survival e hazard raccontano due aspetti diversi della stessa traiettoria

La survival curve dice quanti rimangono oltre ogni punto del tempo. La **hazard rate** guarda invece, tra coloro che sono ancora presenti al tempo `t`, quanto è elevato il rischio di uscita proprio in quel momento. NIST la definisce come un tasso di failure condizionato alla sopravvivenza fino a `t`.[^nist-hazard]

Questa seconda prospettiva è particolarmente utile nei lifecycle con eventi discreti: fine del trial, primo rinnovo, scadenza del metodo di pagamento, fine del supporto assistito, cambio di prezzo o stagione. Il rischio di churn raramente è uniforme lungo tutto il percorso.

### Il tempo osservato non è uguale per tutti

Una coorte entrata venti giorni fa non può ancora avere D90 osservato. Alcuni clienti sono ancora attivi semplicemente perché il nostro periodo di osservazione termina prima che sappiamo quando o se avverrà l'uscita. Questo è il problema del **right censoring**, una caratteristica centrale dei dati lifetime descritta anche dal NIST.[^nist-censoring]

Ignorarlo genera confronti distorti. Se a settembre confrontiamo una coorte di gennaio osservata per otto mesi con una coorte di agosto osservata per un solo mese e calcoliamo semplicemente “percentuale churnata fino a oggi”, gennaio avrà avuto molto più tempo per accumulare uscite. Le coorti devono essere confrontate alla stessa età oppure con metodi che trattino correttamente le osservazioni censurate.

Il Kaplan-Meier estimator nasce proprio per questo tipo di problema. Non serve derivarne qui la matematica; è più importante capire la logica: usiamo ogni soggetto finché è osservabile, non trattiamo come “retained per sempre” chi ha semplicemente raggiunto la fine della finestra senza evento, e aggiorniamo la sopravvivenza quando gli eventi avvengono.

Questa prospettiva non vale soltanto per il churn. Lo stesso linguaggio può descrivere il tempo fino ad activation, primo acquisto, secondo acquisto, upgrade, reactivation o completamento di un processo. Il tempo smette così di essere una semplice colonna e diventa parte del meccanismo.

Quando una dashboard mostra un solo punto di retention, la domanda da aggiungere è:

> **Dove cambia la pendenza della curva, quali eventi di lifecycle coincidono con quel punto e le coorti sono abbastanza mature da essere confrontate?**

Solo dopo aver capito quando aumenta il rischio ha senso chiedere che cosa succede a chi torna dopo essere uscito dal comportamento attivo.

[^nist-survival]: NIST/SEMATECH Engineering Statistics Handbook, *Reliability or survival function*: https://www.itl.nist.gov/div898/handbook/apr/section1/apr122.htm
[^nist-hazard]: NIST/SEMATECH Engineering Statistics Handbook, *Failure (or hazard) rate*: https://www.itl.nist.gov/div898/handbook/apr/section1/apr123.htm
[^nist-censoring]: NIST/SEMATECH Engineering Statistics Handbook, *Censoring*: https://www.itl.nist.gov/div898/handbook/apr/section1/apr131.htm
