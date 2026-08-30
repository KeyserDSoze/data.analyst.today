## 3.6 Missing values: l'assenza è anch'essa informazione

Un valore mancante non è semplicemente una cella vuota. È il risultato di un processo.

Può mancare perché:

- l'informazione non è stata richiesta;
- l'utente non ha risposto;
- il campo non era disponibile nel vecchio sistema;
- la pipeline ha fallito;
- il dato non è applicabile;
- l'evento non è ancora avvenuto;
- il valore è stato rimosso per ragioni di privacy;
- una join non ha trovato corrispondenza;
- il sistema utilizza codici sentinella come `0`, `-1`, `9999`, `unknown` o date convenzionali.

Queste cause non sono equivalenti.

### Missing non significa sempre errore

Se `cancellation_date` è nulla per un abbonamento ancora attivo, il missing è perfettamente informativo.

Se `delivery_date` è nulla perché l'ordine non è ancora stato consegnato, sostituirla con una data media sarebbe concettualmente sbagliato.

Se invece `customer_age` è nulla perché un modulo non ha salvato correttamente il campo, siamo davanti a un problema di raccolta.

### Missingness e bias

Il rischio maggiore nasce quando i valori mancanti non sono distribuiti casualmente.

Immaginiamo un sondaggio sulla soddisfazione in cui rispondono soprattutto i clienti molto soddisfatti e quelli molto insoddisfatti. Il valore medio osservato non descrive necessariamente tutti i clienti.

Per questo prima di imputare o eliminare righe dobbiamo chiedere:

- Quanto manca?
- In quali periodi?
- In quali segmenti?
- Il missing è concentrato in una sorgente specifica?
- È comparso dopo una release o una migrazione?
- Il fatto che il valore manchi è collegato all'outcome che stiamo studiando?

### Profilare i missing

Un controllo iniziale semplice è calcolare per ogni campo:

```text
missing_rate = valori_mancanti / numero_totale_record
```

Ma la percentuale aggregata non basta.

Un campo con il 5% di missing complessivo potrebbe averne:

- 0% fino a giugno;
- 40% da luglio in poi.

Oppure il missing potrebbe riguardare esclusivamente clienti di un determinato paese.

### Imputare non significa recuperare la verità

Tecniche come media, mediana, forward fill o modelli predittivi possono essere utili in alcuni contesti. Ma un valore imputato è una stima, non una nuova osservazione reale.

Per un Data Analyst la regola iniziale dovrebbe essere:

> **Prima spiega perché il dato manca. Solo dopo decidi cosa farne.**

La gestione dei missing values non è quindi un'operazione di pulizia automatica. È una decisione analitica che può modificare popolazione, distribuzioni, confronti e conclusioni.
