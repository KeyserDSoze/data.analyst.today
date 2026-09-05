## 4.5 Confrontare gruppi: quando il totale mescola performance e composizione

Una distribuzione aggregata può diventare più comprensibile quando la separiamo in gruppi. Ma la segmentazione non è soltanto un modo per produrre più tabelle: cambia il significato del confronto perché rende visibile **chi compone ciascun totale**.

È questo il motivo per cui confronti apparentemente semplici — clienti nuovi contro esistenti, regione A contro B, prima contro dopo, campagna X contro Y — richiedono più attenzione della sottrazione tra due percentuali. I gruppi possono differire contemporaneamente per popolazione, esposizione, difficoltà, tempo e mix. Una differenza aggregata può quindi combinare il comportamento interno ai gruppi con il modo in cui quei gruppi sono composti.

Il caso storico delle ammissioni graduate alla University of California, Berkeley, rende il meccanismo particolarmente chiaro. Nei dati del 1973 risultavano **8.442 candidati uomini**, con un tasso di ammissione aggregato intorno al 44%, e **4.321 candidate donne**, con un tasso intorno al 35%. Guardato soltanto a quel livello, il gap suggeriva un processo complessivamente sfavorevole alle donne.

Bickel, Hammel e O'Connell mostrarono però che le decisioni erano prese nei singoli dipartimenti e che i dipartimenti avevano livelli di selettività molto diversi. Inoltre uomini e donne non presentavano domanda con la stessa distribuzione tra i campi di studio. Quando l'analisi teneva conto di questa struttura, il pattern aggregato cambiava sostanzialmente: emergevano poche unità decisionali con differenze statisticamente rilevanti e circa altrettante favorivano un sesso o l'altro; il pooling coerente con l'autonomia dei dipartimenti produceva addirittura un piccolo bias aggregato a favore delle donne.[^bickel-original]

Il punto non è usare il caso per dichiarare che “segmentare elimina la discriminazione”. Gli stessi autori osservavano che la diversa distribuzione delle candidature tra discipline rimandava a meccanismi sociali precedenti al momento dell'ammissione. La lezione analitica è più precisa: **un totale può mescolare meccanismi che operano a livelli diversi, e la composizione può cambiare la direzione del confronto**.

## Simpson's paradox come problema di pesi

Il cosiddetto **Simpson's paradox**, o Yule-Simpson effect, descrive situazioni in cui una relazione aggregata si attenua, scompare o può perfino invertirsi quando osserviamo separatamente gruppi rilevanti. Non c'è nulla di misterioso nel calcolo: il totale è una media pesata e i pesi dei sottogruppi possono essere molto diversi.

In un contesto commerciale, per esempio, potremmo osservare:

```text
Nord:   win rate 31%
Centro: win rate 24%
```

Prima di concludere che il team Nord “vende meglio”, dobbiamo sapere come sono distribuite le opportunità tra SMB, mid-market ed enterprise, inbound e outbound, territori maturi e territori nuovi. Se Nord riceve più opportunità facili e Centro una quota molto maggiore di account enterprise, il totale sta combinando **capacità di conversione e portfolio mix**.

Questa distinzione è già utile in EDA anche se non sappiamo ancora quale aggiustamento sarebbe corretto in senso causale. Possiamo mostrare che il confronto cambia dentro gruppi motivati dal processo e formulare nuove ipotesi. Non possiamo però assumere che ogni variabile debba essere “controllata”: segmentare per una conseguenza dell'azione studiata può rimuovere parte dell'effetto che ci interessa, mentre provare decine di tagli arbitrari aumenta la probabilità di trovare pattern casuali. I Capitoli 8 e 9 affronteranno questo problema con strumenti causali più forti.

## La scala della differenza è parte del confronto

Anche quando i gruppi sono ben definiti, dobbiamo distinguere variazione assoluta e relativa. Un conversion rate che passa dal 2% al 3% cresce di **1 punto percentuale** e del **50% rispetto alla baseline**. Entrambe le frasi sono corrette: la prima misura il delta sulla scala del tasso, la seconda lo rapporta al livello iniziale.

Una comunicazione completa può quindi dire: “conversion rate +1 pp, dal 2% al 3%, equivalente a +50% rispetto alla baseline”. Evitiamo così che il formato della percentuale diventi una scelta narrativa nascosta.

Prima di chiamare due gruppi “migliori” o “peggiori”, il controllo essenziale è chiedere se popolazione, periodo, metrica, denominatore ed esposizione siano comparabili e se pochi sottogruppi dominino il totale. Se il risultato aggregato cambia drasticamente quando osserviamo segmentazioni motivate dal processo, quella differenza non è un fastidio da eliminare: è **struttura da spiegare**.

Questa logica conduce direttamente al workflow EDA. La segmentazione è potente soltanto se resta collegata alla domanda e se ogni nuovo pattern viene trattato come evidenza da stressare, non come conclusione pronta.

> **Confrontare due numeri è facile. Il lavoro analitico comincia quando chiediamo quali popolazioni e quali pesi hanno prodotto quei due numeri.**

---

### Fonti

[^bickel-original]: P. J. Bickel, E. A. Hammel, J. W. O'Connell, *Sex Bias in Graduate Admissions: Data from Berkeley*, Science, 187(4175), 1975, pp. 398–404. https://doi.org/10.1126/science.187.4175.398
