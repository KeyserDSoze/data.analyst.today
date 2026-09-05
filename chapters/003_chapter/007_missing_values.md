## 3.6 Missing values: l'assenza ha una causa

Un valore mancante non è una cella vuota da riempire. È una traccia del processo che ha prodotto — o non prodotto — quell'informazione.

Può mancare perché il campo non era previsto nel vecchio sistema, perché l'utente non ha risposto, perché l'evento non è ancora avvenuto, perché una pipeline non ha caricato il valore, perché la join non ha trovato corrispondenza oppure perché il dato è stato rimosso o anonimizzato. In altri casi il missing non appare come `NULL` ma come un codice sentinella: `-1`, `9999`, `unknown`, `1900-01-01`.

Queste situazioni producono lo stesso sintomo visivo — “manca un valore” — ma implicano popolazioni e rischi diversi. La gestione del missing deve quindi partire dalla causa, non dalla tecnica di imputazione.

## Prima di trattare il missing, capire chi riguarda

Supponiamo che `cancellation_date` sia nulla per un abbonamento ancora attivo. Non abbiamo un errore: il null rappresenta correttamente l'assenza dell'evento di cancellazione. Riempirlo con una data media inventerebbe un fatto che non è avvenuto.

Ora consideriamo `delivery_date` mancante soprattutto per un corriere con problemi d'integrazione. Se quel corriere è anche quello che consegna più lentamente, calcolare il late delivery rate soltanto sui record completi elimina proprio una parte della popolazione più problematica. Il missing non è neutrale: il meccanismo che lo genera è collegato all'outcome.

Una join introduce un terzo significato. Se colleghiamo ordini e catalogo e alcuni `product_id` non trovano corrispondenza, le colonne del catalogo diventano nulle. Quel valore non significa “il prodotto non possiede questa informazione”, ma **“non siamo riusciti a collegare il record alla dimensione attesa”**. Trattarlo come un semplice null nasconderebbe un problema di relazione o di identità.

Per questo, prima di qualsiasi imputazione, servono quattro domande concatenate: il valore dovrebbe esistere per questo record? Perché potrebbe mancare? Il missing si concentra in un segmento, un periodo o una condizione collegata all'outcome? E che cosa cambia nella conclusione se escludiamo, manteniamo o stimiamo quel valore?

## La percentuale aggregata può mentire

Un missing rate complessivo può apparire rassicurante e nascondere un break di processo. Immaginiamo `support_reason` mancante nel 6% dei record. Il totale sembra modesto, ma la serie temporale racconta altro:

| Periodo | Missing rate |
|---|---:|
| gennaio–giugno | 0,8% |
| luglio | 4,1% |
| agosto | 31,7% |

A questo punto il problema non è più “il campo è incompleto”. È diventato “che cosa è cambiato a luglio e agosto?”. Una release, una migrazione, un nuovo flusso operativo o una sorgente diversa possono aver modificato il modo in cui il dato viene raccolto.

Lo stesso controllo va fatto lungo le dimensioni plausibilmente legate al processo: canale, Paese, dispositivo, carrier, segmento cliente. Il missing acquista significato quando osserviamo **chi viene sistematicamente escluso**.

## Imputare è una scelta modellistica

Media, mediana, forward fill e modelli di imputazione possono essere appropriati in alcuni contesti, ma nessuna tecnica recupera automaticamente la verità. Un valore imputato resta una stima costruita per preservare determinate proprietà e ne può alterare altre.

Nel lavoro del Data Analyst la disciplina più importante viene prima della tecnica:

> **Prima spiega il missing. Poi misura chi riguarda. Solo alla fine decidi come trattarlo e quanto la scelta modifica la conclusione.**

La gestione dei valori mancanti non è housekeeping. Può cambiare popolazione, distribuzioni e comparabilità; quindi può cambiare direttamente la decisione che l'analisi pretende di supportare.
