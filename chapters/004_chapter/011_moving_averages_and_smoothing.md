## 4.10 Moving average e smoothing: cambiare lente senza cambiare i dati

Le serie operative sono rumorose.

Una media mobile può aiutare a rendere visibile il movimento di fondo, ma introduce una scelta: **quale parte del passato vogliamo comprimere in ogni punto?**

Lo smoothing non crea nuova evidenza. Cambia il modo in cui osserviamo quella già disponibile.

### Caso simulato/composito — Il crollo del martedì

Un marketplace B2B registra normalmente circa 8.200 ordini al giorno.

Martedì 14 maggio scende a 5.900: **-28%**.

L'escalation è immediata.

L'analista guarda però:

- serie giornaliera grezza;
- media mobile a 7 giorni;
- pagamenti completati nei giorni successivi;
- calendario degli incidenti operativi.

Scopre che lunedì sera un importante provider bancario ha avuto un'interruzione e molte transazioni sono state completate mercoledì.

La media mobile a 7 giorni resta quasi invariata.

La conclusione corretta è doppia:

- martedì è esistito un problema reale di esperienza e conversione temporanea;
- non emerge un deterioramento persistente del volume settimanale.

Lo smoothing non cancella l'incidente. Lo colloca nella scala temporale corretta.

### La finestra determina la domanda

Una finestra di 7 giorni e una di 90 giorni non sono due versioni più o meno "precise" della stessa statistica.

Rispondono a domande differenti.

**Finestra breve**

- reagisce velocemente;
- conserva più rumore;
- utile per cambiamenti recenti.

**Finestra lunga**

- stabilizza maggiormente;
- reagisce lentamente;
- utile per il movimento di fondo;
- può mascherare cambiamenti recenti importanti.

La finestra dovrebbe riflettere frequenza naturale del fenomeno e orizzonte decisionale.

### Trailing vs centered moving average

Per il monitoraggio operativo è comune usare una **trailing moving average**: il valore di oggi usa soltanto oggi e i giorni precedenti.

Una **centered moving average** usa invece osservazioni prima e dopo il punto centrale. È utile per descrivere storicamente la struttura, ma usa informazione futura rispetto al giorno rappresentato.

Quindi non dovrebbe essere presentata come se fosse una misura disponibile in tempo reale.

Questa distinzione diventerà ancora più importante quando parleremo di forecasting e leakage temporale.

### Lo smoothing introduce ritardo

Se una metrica cambia davvero di livello oggi, una media mobile incorpora ancora molti valori del vecchio regime.

Più lunga è la finestra, più lentamente il valore smussato si adegua.

Questo produce una tensione inevitabile:

**ridurre rumore ↔ reagire rapidamente**.

Non esiste una finestra universalmente ottimale.

### Il rischio cosmetico

Lo smoothing diventa pericoloso quando viene usato per rendere il grafico più gradevole o rassicurante.

Un outage di due ore può scomparire in una media giornaliera. Un picco di difettosità può essere quasi invisibile nella media settimanale. Una brusca inversione recente può apparire modesta in una finestra di 90 giorni.

Per questo nell'EDA conviene spesso mostrare:

- serie originale;
- versione smussata;
- finestra usata;
- eventi importanti annotati.

NIST descrive le moving average come un metodo semplice di smoothing per rendere più visibile la componente sottostante di una serie, ma la scelta della tecnica dipende dal comportamento del processo.[^nist-smoothing]

### Non usare la media mobile come prova di trend

Una linea smussata che sale non dimostra che esista un trend stabile nel senso statistico, né dice quanto durerà.

In questo capitolo la usiamo come strumento esplorativo.

L'analisi formale di trend, stagionalità, autocorrelazione e forecast appartiene al Capitolo 7.

> **Lo smoothing è una lente. Una lente può chiarire una struttura oppure nascondere un dettaglio decisivo: dobbiamo sapere quale dei due effetti stiamo producendo.**

[^nist-smoothing]: NIST/SEMATECH, *What are Moving Average or Smoothing Techniques?*. https://www.itl.nist.gov/div898/handbook/pmc/section4/pmc42.htm