## 5.8 Campionamento: prima della precisione viene la popolazione

Quando usiamo un sottoinsieme di osservazioni per dire qualcosa su una popolazione più ampia, il modo in cui quei casi sono entrati nei dati diventa parte della conclusione. L'inferenza non comincia dal confidence interval: comincia dalla relazione tra **chi volevamo osservare e chi siamo riusciti davvero a osservare**.

È utile distinguere tre oggetti. La **popolazione target** è l'insieme sul quale vogliamo concludere. Il **sampling frame** è l'insieme di unità che il nostro processo può effettivamente raggiungere e selezionare. Il **campione** è ciò che finisce davvero nell'analisi.

Immaginiamo una catena retail con 1.240 punti vendita che voglia stimare il tempo medio di attesa alla cassa. Se scegliamo gli 80 store che rispondono per primi alla richiesta del team analytics, abbiamo certamente 80 osservazioni utilizzabili. Non sappiamo però se quei negozi rappresentino l'intera rete. Manager più organizzati, processi meno sotto pressione o una migliore strumentazione possono rendere alcuni store più propensi a partecipare. La statistica successiva può quantificare molto bene l'incertezza **dentro quel meccanismo di selezione** senza renderlo casuale a posteriori.

## Due milioni di risposte e la previsione sbagliata

Il sondaggio del **Literary Digest** del 1936 è diventato un esempio storico proprio perché mostra quanto la numerosità possa creare un falso senso di sicurezza. Il magazine ricevette circa **due milioni di risposte** e predisse una netta vittoria di Alf Landon su Franklin D. Roosevelt. Roosevelt vinse invece le elezioni.

Pew Research Center ricostruisce che i nominativi utilizzati dal Digest provenivano soprattutto da fonti come registri automobilistici ed elenchi telefonici, che non rappresentavano uniformemente la popolazione del periodo; altre componenti contribuirono all'errore, ma sondaggi basati su campioni casuali molto più piccoli furono più accurati.[^pew-digest]

Il punto non è celebrare il campione piccolo. È capire che **n non può correggere il percorso con cui una parte della popolazione viene esclusa o sovrarappresentata**.

La stessa dinamica appare ogni giorno nei prodotti digitali. Supponiamo che una società finanziaria mostri una survey sulla nuova app soltanto agli utenti che hanno effettuato almeno tre accessi. Rispondono 4.800 persone e il 91% si dichiara soddisfatto.

Il management vuole parlare di “soddisfazione degli utenti della nuova app”, ma il dato descrive un percorso molto più selettivo:

**utente invitato → attiva l'app → effettua almeno tre accessi → vede la survey → decide di rispondere**.

Gli utenti che hanno abbandonato durante l'attivazione, quelli che non sono riusciti a completare il setup e quelli che hanno aperto l'app una sola volta hanno pochissime possibilità di entrare nel campione. Il 91% può essere stimato con grande precisione tra i rispondenti e continuare a essere una rappresentazione troppo ottimista dell'esperienza complessiva.

## Random sampling: una base inferenziale, non una magia

Un disegno probabilistico assegna alle unità probabilità di selezione note secondo la procedura scelta. Questo rende molto più difendibile il collegamento tra campione e popolazione e permette di quantificare il sampling error secondo il disegno.

Non significa che ogni campione casuale semplice sia sempre la scelta migliore. Una rete di negozi può richiedere stratificazione per area, dimensione, volume, formato urbano o presenza di self-checkout se queste caratteristiche influenzano fortemente ciò che stiamo stimando. Lo scopo non è far assomigliare il campione alla popolazione su ogni colonna disponibile, ma impedire che il disegno perda sistematicamente dimensioni che contano per la domanda.

AAPOR tratta il sampling error come una sola componente del total survey error e distingue coverage, measurement e nonresponse.[^aapor-definitions] Aumentare la numerosità riduce in molte condizioni il primo problema; non elimina automaticamente gli altri.

Questa distinzione è essenziale anche quando non stiamo facendo una survey. Un log applicativo può osservare soltanto utenti autenticati; un CRM soltanto clienti identificabili; un dataset di support soltanto chi ha scelto di aprire un ticket. Il **meccanismo di osservazione** è sempre parte del significato dell'inferenza.

Per questo una scheda di campionamento merita di rimanere un artefatto strutturato:

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

La scheda non promette rappresentatività. Costringe a dichiarare **fino a dove la nostra evidenza può viaggiare senza cambiare popolazione sotto i piedi**.

> **L'inferenza non parte dalla formula dell'intervallo. Parte dal percorso con cui le osservazioni sono diventate il nostro campione.**

---

### Fonti

[^pew-digest]: Pew Research Center, *Sample Surveys and the 1940 Census*. https://www.pewresearch.org/social-trends/2012/04/02/sample-surveys-and-the-1940-census/
[^aapor-definitions]: AAPOR, *Standard Definitions*, 10th edition. https://aapor.org/standards-and-ethics/standard-definitions/
