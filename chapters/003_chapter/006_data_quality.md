## 3.5 Data quality: qualità rispetto a quale uso?

Dire che un dataset è “di buona qualità” è quasi sempre troppo vago per essere utile. La qualità del dato esiste rispetto a uno scopo: un dataset può essere abbastanza affidabile per osservare un trend mensile e troppo fragile per decidere sul singolo cliente; può essere sufficientemente tempestivo per un consuntivo e inutilizzabile per un processo operativo che deve reagire in pochi minuti.

Il Government Data Quality Framework britannico organizza il problema in sei dimensioni — **completeness, uniqueness, consistency, timeliness, validity e accuracy** — ma la parte più importante per l'analista è il principio che le accompagna: non tutte hanno lo stesso peso in ogni contesto. La qualità va valutata in funzione dell'uso e dell'impatto dell'errore.[^gov-dq]

Questo evita un equivoco frequente: trattare il data quality come una gara a rendere perfetta ogni colonna. Il nostro compito è capire quali proprietà devono essere abbastanza affidabili perché la domanda dell'Analytical Brief rimanga difendibile.

## Sei dimensioni, un solo criterio: l'impatto sulla conclusione

La **completezza** chiede se sono presenti i record e i valori necessari. Non coincide con `NOT NULL`: `1900-01-01` può essere una data formalmente valorizzata e semanticamente mancante, mentre un null in un campo opzionale può essere perfettamente legittimo. La domanda utile è se l'assenza può cambiare la popolazione o la conclusione.

L'**unicità** riguarda il numero di rappresentazioni per un'entità che dovrebbe essere unica. Come abbiamo visto con l'identità, due record possono essere duplicati anche quando differiscono in alcuni attributi, e due righe identiche possono essere legittime se rappresentano eventi distinti.

La **consistenza** riguarda contraddizioni tra valori che pretendono di descrivere lo stesso fenomeno. Un cliente può risultare `Italy` nel CRM e `France` nel billing; un contratto può essere chiuso nella sorgente operativa e attivo nel mart; due dashboard possono usare lo stesso nome per metriche definite diversamente. La contraddizione può essere interna al dataset o attraversare sistemi diversi.

La **timeliness** chiede se il dato arriva abbastanza presto per la decisione. Un valore molto accurato disponibile tre settimane dopo può essere perfetto per il reporting finanziario e inutile per il controllo giornaliero. Qui rientra anche la freshness: quanto è recente la fotografia che stiamo usando?

La **validity** verifica che un valore rispetti formato, tipo, dominio e regole dichiarate. `end_date >= start_date`, una valuta appartenente all'elenco supportato o uno stato presente nell'enum sono esempi di vincoli verificabili. Ma un valore valido può essere comunque sbagliato: `country = IT` è formalmente ammesso anche se il cliente vive in Francia.

L'**accuracy**, infine, riguarda la corrispondenza con la realtà. È spesso la dimensione più difficile da verificare guardando soltanto la tabella, perché richiede una fonte indipendente, una riconciliazione o conoscenza del processo. Se il sistema registra 10.000 consegne e il vettore ne certifica 9.400, il dataset da solo non può dimostrare quale totale rappresenti meglio il fenomeno.

## La qualità contiene trade-off

Il framework britannico usa anche il tema del trade-off fra tempestività, accuratezza e quantità d'informazione: rendere disponibile un dato prima può significare lavorare con una fotografia meno matura.[^gov-dq] Non è necessariamente un difetto. È una scelta che va resa visibile.

Per un'operazione reversibile possiamo preferire un dato preliminare oggi, accompagnato da caveat. Per una decisione regolata o difficile da invertire potremmo invece aspettare una riconciliazione più completa. La domanda non è quale versione sia “migliore” in assoluto, ma quale sia adeguata al rischio che stiamo assumendo.

Per questo un issue di qualità dovrebbe essere documentato insieme al suo impatto analitico:

| Problema | Dimensione | Possibile impatto sulla domanda |
|---|---|---|
| 18% di `delivery_date` mancanti | Completezza | Il late delivery rate può essere sottostimato |
| duplicati su `order_id` | Unicità | Ordini e revenue possono essere sovrastimati |
| dati aggiornati con 36 ore di ritardo | Tempestività | Il monitoraggio giornaliero non rappresenta ancora il giorno precedente |
| cambio enum non documentato | Validità/consistenza | Segmentazioni storiche non comparabili |

La tabella vale più dell'etichetta “data quality: poor” perché collega la proprietà tecnica alla conseguenza possibile.

> **Un problema di data quality diventa analiticamente importante quando sappiamo spiegare quale conclusione o decisione potrebbe distorcere.**

Non dobbiamo perfezionare ogni campo. Dobbiamo rendere affidabili le parti del dato da cui dipende la nostra inferenza.

---

### Fonte

[^gov-dq]: UK Government Data Quality Hub, *The Government Data Quality Framework*. https://www.gov.uk/government/publications/the-government-data-quality-framework/the-government-data-quality-framework
