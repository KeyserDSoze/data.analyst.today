## 3.5 Data quality: qualità rispetto a quale decisione?

Dire che un dataset è "di buona qualità" è troppo generico.

La qualità del dato deve essere valutata rispetto all'uso che ne vogliamo fare. Un dataset può essere adeguato per un trend mensile e inadatto per prendere una decisione sul singolo cliente. Può essere abbastanza tempestivo per il reporting finanziario e troppo lento per un sistema operativo che deve reagire in pochi minuti.

Il Government Data Quality Framework britannico propone sei dimensioni fondamentali — **completeness, uniqueness, consistency, timeliness, validity e accuracy** — e insiste su un principio particolarmente utile per l'analista: non tutte le dimensioni hanno la stessa importanza per ogni uso. La priorità dipende dai bisogni dell'utente e dal contesto decisionale.[^gov-dq]

### Completezza

Il dataset contiene i record e i valori che dovrebbero esserci?

La completezza non coincide con `NOT NULL`.

Una data di nascita valorizzata come `1900-01-01` può essere formalmente presente ma semanticamente mancante. E un campo opzionale può avere molti null senza creare alcun problema per la domanda che stiamo studiando.

La domanda utile non è:

> Quanti valori mancano?

ma:

> **Manca qualcosa che potrebbe cambiare la conclusione?**

### Unicità

Le entità che dovrebbero comparire una volta sono davvero rappresentate una sola volta?

Un record può essere duplicato anche se non è una copia byte-per-byte. Due anagrafiche con indirizzi differenti possono riferirsi alla stessa persona; due righe con timestamp di caricamento diversi possono rappresentare lo stesso ordine.

L'unicità è quindi una proprietà semantica prima ancora che tecnica.

### Consistenza

Valori che descrivono lo stesso fenomeno si contraddicono?

Esempi:

- lo stesso cliente è `Italy` nel CRM e `France` nel billing;
- un contratto risulta chiuso nella sorgente operativa e attivo nel mart analitico;
- la stessa metrica usa definizioni diverse in due dashboard.

La consistenza può essere interna al dataset oppure tra sistemi differenti.

### Tempestività

Il dato arriva abbastanza presto per essere utile?

Un valore molto accurato disponibile tre settimane dopo può essere perfetto per un consuntivo e inutile per una decisione giornaliera.

La tempestività include anche la **freshness**: quanto è recente il dato rispetto al momento in cui lo stiamo utilizzando?

### Validità

Il valore rispetta formato, tipo, dominio e regole previste?

Esempi:

- percentuale tra 0 e 100 quando il processo lo richiede;
- `end_date >= start_date`;
- valuta appartenente a un elenco ammesso;
- stato ordine appartenente all'enum previsto.

Un valore valido, però, può essere comunque inaccurato. `country = IT` è formalmente valido anche se il cliente vive in Francia.

### Accuratezza

Il dato corrisponde abbastanza bene alla realtà?

Questa è spesso la dimensione più difficile da verificare guardando soltanto il dataset, perché richiede una fonte esterna, una riconciliazione o una conoscenza indipendente del fenomeno.

Se il sistema registra 10.000 consegne ma il vettore ne certifica 9.400, il problema non si risolve osservando soltanto la tabella analitica.

### Caso reale documentato — quando qualità significa accettare un trade-off

Il Government Data Quality Framework usa come esempio il passaggio dell'Office for National Statistics britannico a stime mensili del PIL. Rendere il dato disponibile più rapidamente migliora la tempestività, ma può richiedere un compromesso rispetto alla quantità di informazione e alla precisione ottenibile in quella fase.[^gov-dq]

È un esempio importante perché mostra che la qualità non è una gara a massimizzare ogni dimensione contemporaneamente.

A volte il business preferisce:

- un dato preliminare oggi, con incertezza dichiarata;
- invece di un dato più completo tra un mese.

In altri contesti la scelta corretta è l'opposto.

### Dalla qualità generica all'impatto analitico

Per ogni problema individuato, documentiamo tre cose:

| Problema | Dimensione | Possibile impatto sulla domanda |
|---|---|---|
| 18% di `delivery_date` mancanti | Completezza | Il late delivery rate può essere sottostimato |
| duplicati su `order_id` | Unicità | Ordini e revenue possono essere sovrastimati |
| dati aggiornati con 36 ore di ritardo | Tempestività | Il monitoraggio giornaliero non rappresenta ancora il giorno precedente |
| cambio enum non documentato | Validità/consistenza | Segmentazioni storiche non comparabili |

Questa tabella è più utile di una generica etichetta "data quality: poor".

### La regola del capitolo

> **Un problema di data quality diventa analiticamente importante quando possiamo spiegare quale conclusione o decisione potrebbe distorcere.**

Non dobbiamo perfezionare ogni colonna. Dobbiamo rendere affidabili le parti del dato da cui dipende la nostra inferenza.

[^gov-dq]: UK Government Data Quality Hub, *The Government Data Quality Framework*. https://www.gov.uk/government/publications/the-government-data-quality-framework/the-government-data-quality-framework