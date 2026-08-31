# 16.13 Accessibilità: una visualizzazione che non tutti possono leggere è una visualizzazione incompleta

L'accessibilità non è un dettaglio grafico. È parte della qualità della comunicazione.

Una dashboard può essere statisticamente corretta e comunque fallire se una parte del pubblico non riesce a distinguere categorie, leggere etichette o comprendere il messaggio senza affidarsi esclusivamente al colore.

La Government Analysis Function britannica raccomanda, tra le altre cose, di ridurre clutter, evitare decorazioni superflue e progettare grafici compatibili con i requisiti di accessibilità.

Fonte: https://analysisfunction.civilservice.gov.uk/policy-store/charts-a-checklist/

## Non affidarsi solo al colore

Se rosso significa "problema" e verde significa "ok", cosa succede a chi non distingue bene quei colori?

Possiamo aggiungere:

- etichette;
- simboli;
- pattern solo quando utili;
- testo esplicito;
- ordinamento;
- contrasto sufficiente.

Il colore può rinforzare un messaggio, ma non dovrebbe essere l'unico veicolo informativo.

## Etichette e unità

Un asse con valori `5, 10, 15` senza unità costringe il lettore a cercare altrove se si tratta di percentuali, milioni di euro o giorni.

Le linee guida ONS raccomandano di esplicitare simboli come `%` e valuta direttamente dove aiutano la lettura.

Fonte: https://service-manual.ons.gov.uk/data-visualisation/guidance/chart-text

## Caso realistico: il report che funzionava solo sul monitor dell'analyst

Un team prepara una dashboard con testo piccolo, palette a basso contrasto e tooltip che contengono quasi tutto il dettaglio importante.

Sul monitor del creatore è elegante.

Durante una riunione proiettata in una sala grande:

- le etichette non si leggono;
- due serie sembrano dello stesso colore;
- i tooltip non sono disponibili nello screenshot inviato al board.

Il problema non è estetico.

È che l'informazione critica non arriva al destinatario.

## Test pratici

Prima di pubblicare:

- guardiamo la visualizzazione a dimensione ridotta;
- proviamo in scala di grigi;
- verifichiamo che titolo e takeaway siano leggibili senza hover;
- controlliamo contrasto e dimensione del testo;
- chiediamo a una persona non coinvolta nell'analisi di interpretarla.

**La comunicazione è riuscita solo quando il destinatario può effettivamente ricevere il significato che volevamo trasmettere.**
