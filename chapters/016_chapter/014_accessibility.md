## 16.13 Accessibilità: progettare ridondanza, non aggiungere una nota alla fine

Una visualizzazione è incompleta se il significato essenziale esiste soltanto per chi distingue perfettamente i colori, usa un mouse, vede il tooltip, legge testo piccolo e dispone dello stesso schermo del designer. L'accessibilità non è quindi un controllo cosmetico dopo la pubblicazione: è un requisito della **trasmissione dell'evidenza**.

Il principio più utile per l'analytics è la **ridondanza**. WCAG 2.2 stabilisce che il colore non debba essere l'unico mezzo per comunicare informazione o distinguere elementi.[^wcag-color] Possiamo generalizzare: ogni informazione decision-critical dovrebbe avere almeno una seconda via di percezione quando la prima è fragile.

Questo significa, per esempio, usare colore + label, linea + marker + direct label, un alert rosso accompagnato da icona e testo `OUT OF SLA`, un grafico con alt text e una visualizzazione interattiva con tabella di supporto. La ridondanza aiuta anche chi non usa tecnologie assistive: proiettori, screenshot, stampa in scala di grigi, display piccoli e PDF eliminano spesso parte dell'encoding originale.

### Colore e contrasto

Un semplice verde/rosso senza label chiede al colore di trasportare l'intero significato. Una forma più robusta può mostrare `▲ +3,2 pp — sopra target` oppure `▼ -4,1 pp — sotto target`, lasciando al colore un ruolo di rinforzo.

WCAG distingue inoltre il contrasto del testo e quello degli oggetti grafici necessari alla comprensione.[^wcag-contrast] Linee sottili, marker, focus indicator e bordi di controlli non possono essere l'unico portatore di informazione se rischiano di scomparire in condizioni di visualizzazione differenti.

### Alt text: trasferire il takeaway

Un alt text come “grafico a linee blu e verde” descrive l'oggetto ma non trasferisce la sua evidenza. Se il visual sostiene una decisione, una descrizione più utile è:

> **On-time delivery scende dal 96,1% al 91,2% tra aprile e giugno, sotto il target del 95%; il deterioramento è concentrato nel Nord-Ovest.**

L'obiettivo non è disegnare il grafico con le parole. È rendere disponibile il takeaway e, quando necessario, offrire una descrizione estesa o una tabella sottostante.

### Navigazione e ordine di lettura

Una pagina che appare ordinata visivamente può risultare caotica quando il focus attraversa gli oggetti in sequenza arbitraria. Microsoft documenta per Power BI l'importanza di titoli significativi, alt text, ordine di tab logico e controlli navigabili da tastiera.[^ms-access]

Per questo un test utile prova a completare i task principali senza mouse: trovare il dato centrale, attraversare filtri, aprire il dettaglio, tornare indietro e accedere all'alternativa tabellare. Se una decisione dipende da un'interazione impossibile da tastiera, abbiamo creato una barriera funzionale.

### Hover non è una superficie affidabile per la verità

Denominatore, caveat principale, valore oltre soglia, stato `PROVISIONAL` o definizione del KPI non devono vivere soltanto in tooltip. L'hover può sparire su touch, screenshot, export, PDF o percorsi assistivi. Se l'informazione può cambiare la decisione, deve essere percepibile anche senza interazione opzionale.

### Caso simulato/composito — La dashboard che funzionava solo sul monitor del designer

Un team costruisce una dashboard con testo da **9 px**, grigio chiaro su bianco, otto tonalità vicine, insight principali nei tooltip, alert solo rosso/verde e tab order non configurato. Sul monitor dell'analyst appare elegante. Nel board meeting il proiettore appiattisce i colori, le label diventano illeggibili, lo screenshot perde i tooltip e i partecipanti chiedono continuamente quale linea rappresenti quale serie.

Il redesign introduce direct label, contrasto maggiore, testo e simboli per gli stati, takeaway visibili senza hover, tabella di supporto, alt text e ordine di navigazione testato. L'accessibilità migliora e, nello stesso momento, diminuisce il cognitive load per tutti.

La Government Analysis Function 2026 sottolinea infatti che i dashboard interattivi possono essere difficili da usare con alcune tecnologie assistive e raccomanda alternative come testo, alt text, tabelle e download dei dati.[^gaf-access]

## Accessibility Gate

Questo controllo merita di restare operativo:

- [ ] nessuna informazione essenziale dipende soltanto dal colore;
- [ ] testo e oggetti informativi hanno contrasto sufficiente;
- [ ] titoli, unità e label sono leggibili;
- [ ] takeaway e caveat essenziali esistono senza hover;
- [ ] i visual importanti hanno alt text utile;
- [ ] esiste una forma tabellare/testuale per contenuti complessi;
- [ ] ordine di lettura/focus è sensato;
- [ ] i task principali sono utilizzabili da tastiera, quando applicabile;
- [ ] la pagina funziona a dimensione ridotta e su dispositivi diversi;
- [ ] screenshot/PDF non perdono il significato centrale.

> **L'accessibilità non consiste nel creare una versione speciale per alcuni utenti. Consiste nel progettare il significato in modo che non dipenda da un solo canale fragile.**

[^wcag-color]: W3C, *WCAG 2.2 — Use of Color*, https://www.w3.org/WAI/WCAG22/Understanding/use-of-color.html
[^wcag-contrast]: W3C, *WCAG 2.2 — Non-text Contrast*, https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html
[^ms-access]: Microsoft Learn, *Design Power BI reports for accessibility*, https://learn.microsoft.com/en-us/power-bi/create-reports/desktop-accessibility-creating-reports
[^gaf-access]: Government Analysis Function, *Data visualisation: testing dashboards for design and accessibility*, https://analysisfunction.civilservice.gov.uk/policy-store/data-visualisation-testing-dashboards-for-design-and-accessibility/
