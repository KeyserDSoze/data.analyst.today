## 1.13 Caso studio: “Le vendite stanno scendendo”

Una buona teoria analitica diventa utile quando regge davanti a una richiesta reale. Immaginiamo che il direttore commerciale dica semplicemente:

> “Le vendite stanno scendendo. Voglio capire perché.”

A prima vista sembra una richiesta chiara. In realtà contiene numerose ambiguità.

### 1.13.1 Prima domanda: cosa significa “vendite”?

La parola può indicare:

- fatturato lordo;
- fatturato netto;
- numero di ordini;
- unità vendute;
- margine;
- valore medio dell'ordine;
- ordini completati;
- ordini acquisiti, anche se non ancora evasi.

Se due persone usano definizioni diverse, possono produrre analisi entrambe tecnicamente corrette e arrivare a conclusioni opposte.

### 1.13.2 Seconda domanda: rispetto a cosa?

Dire che una metrica “scende” implica un confronto. Bisogna esplicitarlo.

Possibili baseline:

- mese precedente;
- stesso mese dell'anno precedente;
- media mobile degli ultimi dodici mesi;
- budget;
- forecast;
- periodo pre-promozione;
- benchmark di mercato.

Un calo rispetto al mese precedente potrebbe essere perfettamente normale in un business stagionale. Lo stesso valore, confrontato con l'anno precedente, potrebbe invece essere un segnale importante.

### 1.13.3 Terza domanda: il calo è uniforme?

La prima analisi dovrebbe decomporre il fenomeno.

Per esempio:

**Ricavi = numero di ordini × valore medio dell'ordine**

Se il fatturato diminuisce, almeno una delle due componenti deve essere cambiata.

Ma possiamo continuare:

**Ordini = traffico × conversion rate**

E ancora:

**Fatturato = clienti × frequenza di acquisto × valore medio dell'ordine**

Queste decomposizioni non sono formule universali. Sono modi di costruire un albero del problema.

L'obiettivo è passare da una frase generica a componenti osservabili.

### 1.13.4 Segmentare prima di spiegare

Supponiamo che il fatturato sia diminuito del 10%.

Un'analisi aggregata potrebbe nascondere che:

- il segmento enterprise è cresciuto del 15%;
- il segmento consumer è diminuito del 18%;
- una sola area geografica spiega quasi tutto il calo;
- un prodotto ad alto volume è temporaneamente non disponibile;
- i clienti esistenti sono stabili, mentre le nuove acquisizioni sono diminuite.

La domanda “perché le vendite sono scese?” diventa quindi una serie di domande più precise.

### 1.13.5 Dal pattern all'ipotesi

Dopo aver localizzato il problema possiamo formulare spiegazioni plausibili.

Se il calo è concentrato nei nuovi clienti, potremmo indagare:

- riduzione del traffico;
- aumento del costo di acquisizione;
- peggioramento della conversione;
- cambiamento nelle campagne;
- problemi nel checkout;
- variazioni di prezzo;
- modifiche alle condizioni di spedizione;
- errori di tracking.

Il dato non ci consegna automaticamente la spiegazione. Ci permette di restringere lo spazio delle spiegazioni possibili.

### 1.13.6 Verificare che il fenomeno non sia un artefatto

Prima di cercare cause di business bisogna escludere cause tecniche.

Per esempio:

- una sorgente dati non è stata aggiornata;
- alcuni ordini non vengono caricati nel warehouse;
- è cambiata la definizione di “ordine completato”;
- una migrazione ha modificato i codici prodotto;
- il fuso orario sposta transazioni da un giorno all'altro;
- una tabella contiene duplicati;
- resi e cancellazioni sono stati contabilizzati diversamente.

Questo passaggio è spesso poco visibile, ma distingue un'analisi affidabile da una conclusione prematura.

### 1.13.7 Quando fermarsi

Una buona analisi non deve spiegare tutto. Deve produrre abbastanza evidenza per una decisione.

Supponiamo di scoprire che il 75% della diminuzione deriva da un calo della conversione mobile iniziato subito dopo il rilascio di una nuova versione del checkout.

A questo punto l'azione più razionale potrebbe essere:

1. verificare tecnicamente il funnel mobile;
2. confrontare vecchia e nuova versione;
3. identificare il punto di drop-off;
4. correggere il problema;
5. misurare se la conversione torna verso il livello precedente.

L'analisi continua dopo l'azione. La verifica dell'effetto è parte del lavoro.

### 1.13.8 Il ruolo dell'AI nel caso studio

Un assistente AI può accelerare quasi ogni fase operativa:

- generare SQL per segmentare gli ordini;
- proporre decomposizioni;
- produrre codice Python;
- sintetizzare anomalie;
- suggerire visualizzazioni;
- aiutare a documentare le ipotesi.

Ma non conosce automaticamente la definizione corretta di fatturato, il motivo per cui una determinata baseline è rilevante o la decisione che il direttore commerciale deve prendere.

La documentazione Microsoft su Copilot per Power BI avverte esplicitamente che prompt vaghi, modelli semantici ambigui e una preparazione insufficiente possono produrre risposte inaccurate o persino fuorvianti. Questo è un caso concreto del principio sviluppato in questo capitolo: l'automazione dell'esecuzione non elimina la necessità di definire bene il problema e la semantica dei dati.

### Regola operativa

> Prima di spiegare un cambiamento, scomponilo. Prima di scomporlo, definisci la metrica. Prima di definire la metrica, chiarisci quale decisione deve supportare.

### Riferimenti

- Microsoft Learn, *Use Copilot with semantic models in Power BI*: https://learn.microsoft.com/en-us/power-bi/create-reports/copilot-semantic-models
