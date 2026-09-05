## 5.19 Caso end-to-end — Quando un risultato “significativo” non basta

> **Caso simulato/composito.** Il confronto A/B serve qui a rendere concreti i concetti inferenziali del capitolo. Disegno e gestione operativa degli esperimenti — randomizzazione, SRM, contaminazione, durata, stopping, CUPED e rollout — saranno trattati nel Capitolo 9.

Una piattaforma e-commerce confronta per 14 giorni una nuova pagina prodotto con la versione corrente. Al termine vede questi risultati:

| Metrica | Controllo | Variante |
|---|---:|---:|
| Utenti | 246.180 | 245.940 |
| Purchase conversion | 4,82% | 5,01% |
| AOV | 71,40 € | 70,95 € |
| Revenue per visitor | 3,44 € | 3,55 € |
| Return rate | 7,9% | 9,6% |

La conversione aumenta di **+0,19 punti percentuali**, circa **+3,9%** in termini relativi, e il confronto produce `p = 0,028`.

La prima lettura del team è immediata:

> **“La variante vince.”**

Quella frase contiene però più certezza e più decisione di quanta ne abbia ancora prodotta l'analisi.

## La prima sorpresa non è statistica: è nella domanda

Prima dell'esperimento il team aveva dichiarato come metrica primaria **revenue per visitor**, non purchase conversion. La conversione era una metrica diagnostica importante, ma il prodotto doveva aumentare il valore economico per visita.

Il `p = 0,028` non diventa falso per questo. Cambia il suo ruolo nell'insieme dell'evidenza. Se scegliamo dopo il test la metrica che mostra il risultato più favorevole, trasformiamo un segnale diagnostico in claim principale e introduciamo una forma di molteplicità che il singolo p-value non rappresenta.

La domanda torna quindi a essere quella prevista: **la nuova pagina aumenta abbastanza il valore economico per visita da meritare rollout?**

## L'effect size apre il problema economico

Il +0,19 pp di conversione è il primo pezzo da interpretare. Su una baseline del 4,82% equivale a circa +3,9% relativo. Se l'effetto persistesse, produrrebbe più ordini.

Ma la tabella mostra contemporaneamente che l'AOV scende da 71,40 € a 70,95 € e il return rate cresce dal 7,9% al 9,6%. Una metrica localmente positiva non basta quindi a descrivere l'economia del sistema.

Supponiamo che l'analisi della conversione produca una stima di **+0,19 pp**, con CI 95% circa **+0,02 / +0,36 pp**. Il team stima inoltre che, dati costi e margini, serva almeno **+0,15 pp di conversione equivalente a parità di qualità economica** per giustificare il rollout.

La migliore stima supera la soglia. L'intervallo, però, attraversa il break-even: contiene sia scenari quasi nulli sia miglioramenti più interessanti.

Il risultato non è quindi semplicemente “positivo”. È:

> **La stima centrale supera la soglia economica, ma l'incertezza comprende anche scenari che non la raggiungono.**

## Il guardrail cambia la storia più del p-value

L'aumento del return rate di **+1,7 pp** obbliga il team a ricalcolare il valore netto. Quando i resi vengono sottratti dal beneficio economico, gran parte del vantaggio apparente scompare.

Questo è esattamente ciò che il p-value della conversione non può sapere. Il test quantifica un pezzo specifico dell'evidenza; non contiene il costo dei resi, il margine o le dipendenze tra metriche economiche.

A questo punto la frase “la variante vince” non è soltanto troppo sicura. Sta ottimizzando la metrica sbagliata rispetto alla decisione dichiarata.

## L'esplorazione successiva produce ipotesi, non eccezioni retroattive

Il team prova allora a capire dove il segnale sia più forte. Esplora desktop, mobile web, iOS, Android, nuovi utenti, returning e i principali canali di acquisizione. Alcuni segmenti, soprattutto mobile, sembrano molto promettenti.

Questa è una scoperta utile. Non era però un claim confermativo pre-specificato. Il risultato deve quindi entrare nel registro delle ipotesi:

> **Possibile effetto eterogeneo su mobile; da verificare nel prossimo test.**

Trasformarlo immediatamente in “la variante funziona sicuramente su mobile” significherebbe dimenticare quante opportunità di trovare un segmento interessante abbiamo creato dopo aver visto il risultato globale.

## Anche un esperimento ben stimato vive dentro un periodo storico

C'è infine un'altra forma di incertezza che il confidence interval della conversione non contiene. Il segnale è particolarmente forte nei primi quattro giorni, proprio mentre è attiva una campagna premium.

Questo non implica necessariamente un difetto statistico del confronto. Solleva una domanda di **generalizzazione temporale**: l'effetto medio dei 14 giorni rappresenta anche settimane future senza quella campagna?

Sampling uncertainty e validità esterna non sono la stessa cosa. Possiamo avere una stima molto precisa per la popolazione osservata e restare incerti sulla persistenza dell'effetto quando cambiano condizioni commerciali, mix o calendario.

## L'Uncertainty Brief del caso

Il valore del capitolo è raccogliere questi livelli nello stesso posto:

| Campo | Sintesi |
|---|---|
| **Domanda** | La nuova pagina aumenta valore economico per visita abbastanza da meritare rollout? |
| **Popolazione osservata** | Utenti eleggibili nei 14 giorni del confronto. |
| **Metrica primaria** | Revenue per visitor. |
| **Segnale diagnostico** | Conversion +0,19 pp; `p = 0,028`. |
| **Precisione** | CI conversione include effetti piccoli e materialmente interessanti. |
| **Soglia business** | Circa +0,15 pp equivalente, subordinata a margine/return. |
| **Guardrail** | Return rate +1,7 pp: peggioramento rilevante. |
| **Molteplicità** | Segmenti mobile/channel esplorati a posteriori. |
| **Bias/incertezza non nel CI** | Possibile dipendenza dalla campagna premium e dalla finestra temporale. |
| **Conclusione** | Evidenza di aumento conversione, ma non evidenza sufficiente di aumento del valore netto. |
| **Prossimo passo** | Nuovo test pre-specificato su metrica economica netta e segmenti prioritari. |

Questa tabella contiene più informazione decisionale del `p = 0,028` perché spiega **che cosa il test ha imparato, che cosa la decisione richiede e quali incertezze restano fuori dal test**.

Il team non effettua quindi un rollout generale. Usa il risultato per progettare il confronto successivo con metrica primaria economica netta, return rate come guardrail esplicito, segmenti prioritari pre-specificati e durata sufficiente a includere condizioni commerciali più normali.

Il Capitolo 9 mostrerà come progettare quel test. Qui la lezione è già completa: un risultato statisticamente interessante diventa evidenza decisionale soltanto quando dimensione, precisione, popolazione, molteplicità, guardrail e valore economico vengono letti nello stesso sistema.

> **L'inferenza non deve produrre un'etichetta `WIN / LOSE`. Deve impedire che una stima più precisa di una singola metrica diventi una decisione più sicura di quanto l'insieme dell'evidenza consenta.**
