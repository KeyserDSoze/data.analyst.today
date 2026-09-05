## 2.2 Specificare la decisione prima di progettare l'output

Molte richieste arrivano già travestite da soluzione. “Mi fai una dashboard?”, “mi serve un report settimanale”, “vorrei vedere questi KPI” sembrano requisiti chiari perché nominano un deliverable. In realtà stanno saltando il passaggio più importante: **quale comportamento, controllo o scelta dovrebbe migliorare grazie a quell'output?**

La domanda conta perché il formato utile dipende dalla decisione. Un responsabile logistico che ogni mattina deve capire quali spedizioni richiedono intervento ha bisogno di freschezza, soglie e un'interfaccia ricorrente. Un product team che deve capire perché la conversione è scesa del 12% può ottenere più valore da una EDA mirata e da un memo che da una dashboard permanente. Un team commerciale che deve scegliere tra sconto, spedizione gratuita e nessun intervento ha invece bisogno di confrontare scenari, impatto economico, guardrail e incertezza.

Lo stesso ecosistema dati può alimentare tutti e tre i casi. Cambia il prodotto analitico perché cambia ciò che qualcuno deve fare dopo averlo letto.

## La decision specification

Per questo il brief dovrebbe rendere espliciti pochi elementi, ma sostanziali. Dobbiamo sapere quale decisione è in gioco, chi ha l'autorità di prenderla, quali alternative sono realmente disponibili, entro quando la scelta deve essere fatta e che cosa costa sbagliare. Quando possibile conviene anticipare anche la soglia che renderebbe un risultato abbastanza importante da modificare la scelta.

Questi campi non sono metadati amministrativi. Modificano direttamente il disegno dell'analisi. Una decisione irreversibile giustifica più evidenza di un test facilmente annullabile. Una decisione che si ripete ogni mattina può richiedere automazione e monitoring, mentre una scelta unica può essere servita meglio da un'analisi ad hoc. Se il decision owner non può realmente scegliere tra le alternative che stiamo modellando, stiamo ottimizzando uno spazio decisionale che non esiste.

Una formula semplice aiuta a verificare il collegamento:

> **“Se scoprissimo che ________, il decision owner potrebbe decidere di ________.”**

Se nessun risultato plausibile completa la seconda parte della frase, il lavoro può avere valore informativo, ma non dovremmo chiamarlo decision support senza spiegare quale processo lo userà.

## Soglie prima del risultato, quando è possibile

Definire in anticipo una soglia non è sempre realistico, ma provarci è utile. Supponiamo che un nuovo processo logistico debba essere valutato per un rollout. Il team potrebbe concordare:

> “Se il nuovo processo riduce il tempo di evasione di almeno il 10% senza aumentare gli errori oltre 0,5 punti percentuali, valuteremo il rollout.”

Questa specifica cambia la domanda analitica. Non basta più chiedere se il tempo medio è sceso: dobbiamo stimare la dimensione del miglioramento e osservare contemporaneamente il guardrail sugli errori. Inoltre evitiamo di spostare retrospettivamente il criterio di successo dopo aver visto i risultati.

Il Capitolo 15 approfondirà expected value, soglie e trade-off decisionali. Qui l'obiettivo è più elementare: impedire che il metodo e il deliverable vengano progettati prima di sapere come il risultato verrà usato.

Il campo operativo del brief rimane deliberatamente strutturato:

```text
Decisione:
Decision owner:
Alternative disponibili:
Deadline/frequenza:
Costo principale dell'errore:
Soglia o criterio d'azione, se definibile:
```

> **Prima di scegliere il formato dell'output, specifica il comportamento che quell'output dovrebbe rendere più informato.**
