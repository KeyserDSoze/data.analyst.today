## 5.8 Campionamento: la popolazione che osserviamo determina ciò che possiamo inferire

Quando vogliamo dire qualcosa su una popolazione più ampia a partire da un sottoinsieme di osservazioni, il modo in cui quel sottoinsieme è entrato nei dati diventa parte integrante dell'analisi.

Il campionamento non risponde soltanto alla domanda:

> **Quanti casi osserviamo?**

Risponde soprattutto a:

> **Quale relazione esiste tra i casi osservati e la popolazione su cui vogliamo concludere?**

### Popolazione target, sampling frame e campione non sono la stessa cosa

Supponiamo che una catena retail con 1.240 punti vendita voglia stimare il tempo medio di attesa alla cassa.

- **Popolazione target:** tutti i negozi e i clienti che vogliamo descrivere.
- **Sampling frame:** l'insieme di negozi che possiamo effettivamente selezionare e misurare.
- **Campione:** i negozi e i periodi che osserviamo davvero.

Se scegliamo gli 80 store che rispondono per primi alla richiesta del team analytics, il campione è comodo ma il meccanismo di selezione può favorire negozi con manager più organizzati, processi migliori o minore pressione operativa.

La statistica successiva non può rendere casuale una selezione che non lo era.

### Caso reale documentato — Il Literary Digest e i milioni di risposte che non bastarono

Uno degli esempi storici più memorabili di questo problema è il sondaggio elettorale del **Literary Digest** del 1936 negli Stati Uniti.

Il magazine distribuì milioni di schede e ricevette circa **due milioni di risposte**. Il risultato prevedeva una vittoria netta di Alf Landon su Franklin D. Roosevelt.

La previsione fu clamorosamente sbagliata: Roosevelt vinse le elezioni.

Pew Research Center, ricostruendo la storia del campionamento moderno, osserva che i nominativi del Digest provenivano soprattutto da fonti come registri automobilistici ed elenchi telefonici, che non rappresentavano uniformemente la popolazione del periodo. Sottolinea inoltre che anche altri fattori contribuirono all'errore e che indagini basate su campioni molto più piccoli ma meglio progettati ottennero risultati più accurati.[^pew-digest]

AAPOR ricorda lo stesso episodio come uno dei fallimenti che contribuirono all'affermazione dei metodi di campionamento più rigorosi.[^aapor-nps]

Il messaggio per il Data Analyst è potentissimo:

> **milioni di osservazioni non compensano automaticamente un meccanismo di selezione distorto.**

### Caso simulato/composito — Il 91% di utenti soddisfatti

Una società finanziaria lancia una nuova app. Dopo due settimane mostra una survey solo agli utenti che hanno effettuato almeno tre accessi.

Rispondono 4.800 persone e il 91% si dichiara soddisfatto.

Il numero è statisticamente preciso per i **rispondenti raggiunti da quel meccanismo**.

Ma la popolazione sulla quale il management vuole concludere è più ampia: tutti gli utenti invitati a utilizzare la nuova app.

Gli utenti che hanno aperto l'app una sola volta, quelli che hanno abbandonato durante l'attivazione e quelli che non sono riusciti a completare il setup non hanno quasi possibilità di entrare nel campione.

Il problema non è `n = 4.800`.

È il percorso:

**utente invitato → attiva l'app → effettua almeno tre accessi → vede la survey → decide di rispondere**.

Ogni freccia può selezionare un sottoinsieme diverso dalla popolazione target.

### Random sampling: utile, non magico

In un campione probabilistico le unità hanno probabilità di selezione note secondo il disegno adottato. Questo ci fornisce una base molto più solida per quantificare l'incertezza di campionamento.

Ma anche un buon disegno può richiedere stratificazione o pesi quando la popolazione è eterogenea.

Nel caso dei negozi potremmo stratificare per:

- area geografica;
- dimensione;
- volume;
- formato urbano/extraurbano;
- presenza di self-checkout.

L'obiettivo non è far assomigliare il campione alla popolazione su ogni colonna disponibile. È assicurarsi che il disegno rappresenti adeguatamente le dimensioni che possono essere importanti per la stima.

### Sampling error e bias sono problemi differenti

Il **sampling error** nasce dal fatto che campioni diversi producono stime leggermente diverse.

Il **bias di selezione, coverage o nonresponse** nasce invece quando il processo di osservazione rende alcune parti della popolazione sistematicamente più o meno rappresentate.

Aumentare `n` riduce il primo in molte condizioni. Non elimina automaticamente il secondo.

AAPOR insiste proprio sulla necessità di distinguere il margine di campionamento dalle altre componenti dell'errore di survey.[^aapor-standards]

### La scheda di campionamento

Prima di generalizzare da un campione, documenta:

```text
Popolazione target:
Sampling frame:
Unità di campionamento:
Metodo di selezione:
Periodo di raccolta:
Tasso / meccanismo di risposta:
Segmenti potenzialmente sottorappresentati:
Pesi o aggiustamenti applicati:
Popolazione alla quale è realmente difendibile generalizzare:
```

Questa scheda vale più di molti decimali aggiuntivi.

> **L'inferenza non parte dalla formula dell'intervallo. Parte dal percorso con cui le osservazioni sono entrate nel campione.**

[^pew-digest]: Pew Research Center, *Sample Surveys and the 1940 Census*: https://www.pewresearch.org/social-trends/2012/04/02/sample-surveys-and-the-1940-census/
[^aapor-nps]: AAPOR, *Report of the Task Force on Non-Probability Sampling*: https://aapor.org/wp-content/uploads/2022/11/NPS_TF_Report_Final_7_revised_FNL_6_22_13-1.pdf
[^aapor-standards]: AAPOR, *Transparency Initiative*: https://aapor.org/standards-and-ethics/transparency-initiative/
