## 16.13 Accessibilità: progettare ridondanza, non aggiungere una nota alla fine

Una visualizzazione è incompleta se il significato essenziale esiste soltanto per chi:

- distingue perfettamente i colori;
- usa un mouse;
- vede il tooltip;
- legge testo piccolo;
- usa lo stesso monitor del designer;
- può interpretare una forma grafica senza alternativa testuale.

L'accessibilità non è un controllo cosmetico dopo la pubblicazione.

È un requisito della **trasmissione dell'evidenza**.

## Il principio più importante: redundant encoding

W3C WCAG 2.2 stabilisce che il colore non deve essere l'unico mezzo per comunicare informazione, distinguere elementi o indicare un'azione.

Per l'analytics questo suggerisce una regola più generale:

> **Ogni informazione decision-critical dovrebbe avere almeno una seconda via di percezione quando la prima può essere fragile.**

Esempi:

- colore + label;
- linea + stile/marker + direct label;
- alert rosso + icona + testo `OUT OF SLA`;
- grafico + alt text;
- visual interattivo + tabella di supporto;
- tooltip + valore essenziale già visibile.

Questa ridondanza aiuta anche chi non usa tecnologie assistive: screenshot, proiettori, stampa in scala di grigi e display piccoli eliminano spesso parte dell'encoding originale.

## Non affidarsi al solo colore

Debole:

- verde = sopra target;
- rosso = sotto target;
- nessuna label.

Più robusto:

- `▲ +3,2 pp — sopra target`;
- `▼ -4,1 pp — sotto target`;
- colore come rinforzo, non come unica informazione.

Il contrasto da solo non risolve il problema se il lettore deve riconoscere *quale* colore rappresenta uno stato.

## Contrasto: testo e oggetti informativi devono restare percepibili

WCAG distingue contrasto del testo e contrasto degli oggetti grafici necessari alla comprensione.

Questo conta per:

- linee sottili;
- marker;
- bordi di input e filtri;
- focus indicator;
- elementi di chart indispensabili.

Se un oggetto può praticamente scomparire su uno schermo o in high-contrast mode, non può essere l'unico portatore dell'informazione.

## Alt text: descrivere il takeaway, non disegnare con le parole

Alt text debole:

> “Grafico a linee blu e verde con asse X mesi e asse Y percentuale.”

Alt text utile:

> “On-time delivery scende dal 96,1% al 91,2% tra aprile e giugno, sotto il target del 95%; il deterioramento è concentrato nelle regioni Nord-Ovest.”

L'obiettivo è trasferire **l'informazione necessaria alla decisione**, non riprodurre verbalmente ogni pixel.

Per un visual complesso possiamo offrire:

- alt text breve;
- descrizione estesa;
- tabella sottostante;
- link ai dati.

## Screen reader e ordine di lettura

Microsoft documenta che gli oggetti Power BI navigabili da tastiera sono generalmente compatibili con screen reader e che il lettore può annunciare titolo, tipo di visual e alt text impostato.

Questo rende importanti:

- titoli significativi;
- alt text aggiornato;
- ordine di tab/focus logico;
- nomi chiari per bottoni e slicer;
- evitare oggetti decorativi che inquinano la navigazione.

Una pagina che visivamente sembra ordinata può risultare caotica se il focus percorre gli elementi in una sequenza arbitraria.

## Keyboard-first test

Per dashboard interattive proviamo a completare i task principali senza mouse:

- navigare tra visual e controlli;
- cambiare un filtro;
- aprire dettaglio;
- tornare indietro;
- trovare il dato principale;
- accedere all'alternativa tabellare.

Se una decisione dipende da un'interazione impossibile da tastiera, abbiamo creato una barriera funzionale.

## Hover non è una superficie affidabile per la verità

Non lasciamo esclusivamente nel tooltip:

- denominatore;
- caveat principale;
- valore che supera la soglia;
- definizione del KPI;
- stato provisional/final.

L'hover può non esistere su touch, screenshot, esportazioni, screen reader o PDF.

## Caso simulato/composito — Il dashboard che funzionava solo sul monitor del designer

Un team prepara una dashboard con:

- testo da 9 px;
- grigio chiaro su fondo bianco;
- otto tonalità vicine;
- insight principali soltanto nei tooltip;
- alert rappresentati da rosso/verde;
- ordine di tab non configurato.

Sul monitor dell'analyst appare elegante.

Nel board meeting:

- il proiettore appiattisce i colori;
- le label non si leggono;
- lo screenshot non contiene i tooltip;
- un partecipante chiede continuamente quale serie corrisponda a quale linea.

Il redesign introduce:

- direct labels;
- contrasto maggiore;
- testo e simboli per gli stati;
- takeaway visibili senza hover;
- tabella di supporto;
- alt text;
- ordine di navigazione testato.

L'accessibilità migliora e, contemporaneamente, diminuisce il cognitive load per tutti.

## Un dashboard non sarà perfettamente accessibile in ogni forma

La Government Analysis Function britannica sottolinea che i dashboard interattivi possono essere difficili da usare con alcune tecnologie assistive e raccomanda di offrire alternative appropriate: testo, alt text, tabelle, download e canali di supporto.

Questa è una lezione importante:

> **non dobbiamo fingere che una singola visualizzazione interattiva sia un formato universale.**

La Decision Communication Pack può prevedere più rappresentazioni della stessa evidenza.

## Accessibility Gate

Prima della pubblicazione verifichiamo:

- [ ] nessuna informazione essenziale dipende solo dal colore;
- [ ] testo e oggetti informativi hanno contrasto sufficiente;
- [ ] titoli, unità e label sono leggibili;
- [ ] takeaway e caveat essenziali esistono senza hover;
- [ ] visual importanti hanno alt text utile;
- [ ] esiste una forma tabellare/testuale per contenuti complessi;
- [ ] ordine di lettura/focus è sensato;
- [ ] task principali sono utilizzabili da tastiera, quando applicabile;
- [ ] la pagina funziona a dimensione ridotta e su dispositivi diversi;
- [ ] screenshot/PDF non perdono il significato centrale.

> **L'accessibilità non consiste nel fare una versione speciale per alcuni utenti. Consiste nel progettare il significato in modo che non dipenda da un solo canale fragile.**

### Fonti

- W3C, *WCAG 2.2 — Use of Color*: https://www.w3.org/WAI/WCAG22/Understanding/use-of-color.html
- W3C, *WCAG 2.2 — Non-text Contrast*: https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html
- Microsoft Learn, *Design Power BI reports for accessibility*: https://learn.microsoft.com/en-us/power-bi/create-reports/desktop-accessibility-creating-reports
- Government Analysis Function, *Data visualisation: testing dashboards for design and accessibility*: https://analysisfunction.civilservice.gov.uk/policy-store/data-visualisation-testing-dashboards-for-design-and-accessibility/
