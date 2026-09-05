## 3.2 Granularità: la risoluzione con cui il sistema ha osservato il fenomeno

La **granularità**, o *grain*, descrive che cosa rende distinta una riga. È una proprietà strutturale, ma ha conseguenze direttamente analitiche: determina quali conteggi sono legittimi, quali misure possono essere sommate e quali join rischiano di moltiplicare informazioni già presenti.

Una generica “tabella vendite” può infatti contenere una riga per ordine, una per prodotto nell'ordine, una per prodotto e giorno, una per negozio-prodotto-giorno oppure una per cliente e mese. Il nome della tabella non basta a distinguere questi casi. Serve una dichiarazione esplicita, per esempio:

> **Una riga rappresenta un prodotto presente in un singolo ordine.**

oppure:

> **Una riga rappresenta lo stock di un prodotto in un magazzino alla fine di una giornata.**

Microsoft descrive lo stesso principio nel dimensional modeling di Fabric: le chiavi dimensionali determinano la granularità dei fatti, cioè il livello atomico a cui vengono definiti. La documentazione distingue inoltre fact table transazionali e snapshot periodici proprio perché la struttura del fatto cambia il modo in cui le misure possono essere aggregate.[^ms-grain]

## Additività: il numero può essere corretto e la somma sbagliata

Consideriamo:

| order_id | product | line_amount | order_total |
|---|---|---:|---:|
| 1 | A | 40 | 100 |
| 1 | B | 60 | 100 |

Il grain è la riga d'ordine. `line_amount` appartiene a quel livello e può essere sommato: `40 + 60 = 100`. `order_total`, invece, è una proprietà dell'ordine replicata su ogni linea. Anche la query `SUM(order_total)` è perfettamente valida dal punto di vista sintattico, ma produce `200`, un numero senza significato economico.

Questo è uno degli errori più insidiosi dell'analytics: il database esegue correttamente un'operazione che il modello semantico non autorizza. Il grain decide quindi non soltanto *quali righe abbiamo*, ma anche *come possiamo usare le misure che contengono*.

## Le trasformazioni possono cambiare il grain

Supponiamo di avere `customers`, una riga per cliente, e `orders`, molte righe per cliente. Dopo una join, gli attributi del cliente vengono replicati su ogni ordine. Il dataset risultante non è più a livello cliente, anche se alcune colonne continuano a “sembrare” anagrafiche.

Da qui nasce un riflesso operativo importante:

> **Dopo ogni trasformazione che può moltiplicare o collassare righe, chiediti che cosa rappresenta adesso una riga.**

Non serve ancora conoscere tutte le tecniche di join, che affronteremo più avanti. Serve riconoscere che ogni cambio di cardinalità è anche un possibile cambio del significato dell'osservazione.

## Il grain dichiarato deve essere verificato nei dati

La documentazione, inoltre, può essere incompleta o obsoleta. Se una tabella viene descritta come “una riga per ordine” ma `order_id` compare più volte, non possiamo concludere subito che esistano duplicati da eliminare. Potrebbero esserci versioni successive, rettifiche, eventi, una chiave composta o un processo di caricamento che ha creato copie accidentali.

Il compito iniziale è quindi confrontare **grain dichiarato** e **grain osservato**. Dobbiamo sapere quale combinazione di colonne dovrebbe rendere unica una riga, verificare se quel vincolo regge, distinguere misure additive da valori già aggregati e controllare se il grain è rimasto stabile nel tempo.

Questi controlli non sono una checklist separata dal ragionamento. Sono le verifiche con cui dimostriamo che la rappresentazione fisica del dataset coincide con quella che intendiamo usare nell'analisi.

> **Comprendere la granularità significa capire a quale risoluzione il processo reale è diventato dato e quali operazioni quella risoluzione ci autorizza a fare.**

---

### Fonte

[^ms-grain]: Microsoft Learn, *Modeling Fact Tables in Warehouse — Microsoft Fabric*. https://learn.microsoft.com/en-us/fabric/data-warehouse/dimensional-modeling-fact-tables
