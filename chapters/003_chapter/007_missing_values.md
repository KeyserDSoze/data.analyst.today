## 3.6 Missing values: l'assenza ha una causa

Un valore mancante non è semplicemente una cella vuota da riempire.

È il risultato di un processo.

Può mancare perché:

- l'informazione non è stata richiesta;
- l'utente non ha risposto;
- il campo non esisteva nel vecchio sistema;
- la pipeline non lo ha caricato;
- il dato non è applicabile;
- l'evento non è ancora avvenuto;
- il valore è stato rimosso o anonimizzato;
- una join non ha trovato corrispondenza;
- il sistema usa codici sentinella come `-1`, `9999`, `unknown` o `1900-01-01`.

Queste cause producono lo stesso aspetto visivo — "manca un valore" — ma hanno significati analitici molto diversi.

### Quattro domande prima di qualsiasi imputazione

Davanti a un campo incompleto chiediamoci:

1. **Dovrebbe esistere per questo record?**
2. **Perché potrebbe mancare?**
3. **La probabilità che manchi è collegata a un segmento o all'outcome?**
4. **Che cosa cambia se escludiamo, manteniamo o stimiamo quel valore?**

La quarta domanda impedisce di trasformare il cleaning in un automatismo.

### Missing strutturale: il valore non dovrebbe esserci

Se `cancellation_date` è nulla per un abbonamento ancora attivo, non abbiamo un errore. Il null descrive correttamente lo stato del processo.

Lo stesso vale per `delivery_date` quando l'ordine è ancora in transito.

Riempire questi valori con una data media non "completa" il dataset. Inventa un evento che non è ancora avvenuto.

### Missing da processo: qualcosa non è stato osservato

Supponiamo invece che `delivery_date` manchi soprattutto per un corriere che ha avuto problemi di integrazione.

A quel punto il missing non è neutrale. Se quel vettore è anche quello con più ritardi, calcolare il late delivery rate soltanto sugli ordini con data presente può produrre una stima troppo ottimistica.

Il problema non è il numero di null in sé. È **chi viene escluso dal calcolo**.

### Missing introdotto dalla trasformazione

Una join può creare valori mancanti anche quando entrambe le sorgenti erano complete.

Se colleghiamo ordini e catalogo prodotti e alcuni `product_id` non trovano corrispondenza, le colonne del catalogo diventano nulle.

Quel missing significa:

> "non siamo riusciti a collegare questo record"

non:

> "il prodotto non possiede questa informazione".

È una distinzione essenziale.

### Codici sentinella: il missing che sembra un valore

Un campo può risultare completo al 100% e contenere comunque assenze mascherate.

Esempi:

```text
birth_date = 1900-01-01
income = -1
country = UNKNOWN
postal_code = 99999
```

Per questo il profiling dei missing deve includere anche valori convenzionali e categorie anomale, non soltanto `NULL`.

### La percentuale aggregata può nascondere il problema

Supponiamo che `support_reason` abbia il 6% di missing complessivo.

Sembra modesto.

Poi lo scomponiamo nel tempo:

| Periodo | Missing rate |
|---|---:|
| gennaio–giugno | 0,8% |
| luglio | 4,1% |
| agosto | 31,7% |

Il problema non è strutturale al dataset. È comparso recentemente.

La domanda successiva diventa: **cosa è cambiato a luglio/agosto?** Release, migrazione, processo operativo, sorgente?

Lo stesso controllo va fatto per segmento, canale, paese, dispositivo o qualsiasi dimensione plausibilmente collegata alla raccolta del dato.

### Imputare non significa recuperare la verità

Media, mediana, forward fill e modelli di imputazione possono essere appropriati in alcuni contesti. Ma un valore imputato resta una stima.

Prima di scegliere una tecnica dobbiamo sapere quale proprietà vogliamo preservare e quale bias rischiamo di introdurre.

Per il Data Analyst la regola più utile è:

> **Prima spiega il missing. Poi quantifica chi riguarda. Solo alla fine decidi come trattarlo.**

La gestione dei valori mancanti non è housekeeping. Può cambiare popolazione, distribuzioni, comparabilità e quindi la decisione finale.