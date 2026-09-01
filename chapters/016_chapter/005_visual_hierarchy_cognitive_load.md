## 16.4 Gerarchia visiva e cognitive load: progettare l'attenzione

Quando tutto sembra importante, niente lo è davvero.

Una pagina può contenere numeri corretti e fallire perché trasferisce al lettore troppo lavoro:

- capire dove guardare;
- distinguere segnale e contesto;
- ricordare una legenda lontana;
- confrontare scale;
- ricostruire quale numero è headline e quale è diagnostico;
- capire quali dettagli sono caveat e quali sono decorazioni.

Il cognitive load non è solo un problema estetico. È **rischio di interpretazione**.

## Il salience budget

Ogni pagina ha un budget limitato di attenzione.

Possiamo spenderlo con:

- posizione;
- dimensione;
- contrasto;
- spazio bianco;
- peso tipografico;
- colore;
- annotazioni.

Se usiamo massima enfasi su dieci elementi, non abbiamo dieci priorità. Abbiamo perso la gerarchia.

Una regola utile è classificare gli elementi:

### P1 — Decision-critical

Deve emergere immediatamente.

Esempi:

- recommendation;
- gap che supera una soglia;
- guardrail violato;
- caveat che cambia la decisione.

### P2 — Supporting evidence

Deve essere visibile senza competere con P1.

### P3 — Context / verification

Serve per capire o controllare, ma può vivere più in basso o in appendix.

La gerarchia visiva dovrebbe seguire questa gerarchia semantica.

## Caso simulato/composito — Quattro KPI, sedici colori

Una fintech prepara una dashboard rischio con quattro metriche centrali:

- default rate;
- loss given default;
- approval rate;
- fraud loss.

La pagina usa sedici colori per segmenti, prodotti, stati, alert e regioni.

Durante la review il management dedica diversi minuti a un segmento rosso che sembra critico.

Il rosso indica in realtà soltanto una categoria prodotto.

Il redesign usa:

- tono neutro per il contesto;
- enfasi riservata agli scostamenti decisionali;
- etichette dirette;
- simbolo/testo per gli alert;
- palette di categoria separata dal linguaggio di stato.

I numeri non cambiano. Cambia la probabilità di interpretarli correttamente.

## Ridurre il lavoro di memoria

Il lettore non dovrebbe ricordare continuamente:

- quale linea è l'anno corrente;
- quale colore è il target;
- quale unità usa il grafico precedente;
- quale filtro è attivo.

Quando possibile:

- etichettiamo direttamente le linee;
- mettiamo unità vicino ai numeri;
- mostriamo il filtro decision-critical in pagina;
- mettiamo l'annotazione vicino al punto a cui si riferisce;
- manteniamo lo stesso encoding per lo stesso concetto tra pagine.

La coerenza riduce il costo cognitivo cumulativo.

## Precision budget: più decimali non significa più rigore

`31,847362%` comunica precisione apparente.

La precisione mostrata dovrebbe dipendere dalla soglia decisionale.

Se nessuna decisione cambia per differenze inferiori a 0,1 punti percentuali, sei decimali non aiutano. Possono anzi rendere invisibile la vera incertezza.

Chiamiamo questo **precision budget**:

> mostriamo soltanto la precisione che il processo decisionale può realmente utilizzare e che il metodo può difendere.

## Spazio bianco come separazione semantica

Lo spazio bianco non è vuoto.

Comunica:

- questi elementi appartengono allo stesso gruppo;
- questo blocco è più importante;
- questa evidenza è distinta dalla raccomandazione;
- qui cambia livello di dettaglio.

Riempire ogni centimetro spesso aumenta la quantità di informazione visibile e diminuisce quella effettivamente utilizzabile.

## Il test dei tre secondi e dei dieci secondi

Mostriamo la pagina a una persona non coinvolta nell'analisi.

Dopo tre secondi chiediamo:

> “Che cosa ti sembra più importante?”

Dopo dieci:

> “Quale decisione o problema pensi che questa pagina stia evidenziando?”

Se le risposte non coincidono con l'intento, la gerarchia è sbagliata anche se ogni singolo elemento è corretto.

## La gerarchia non deve occultare il caveat

Un errore frequente è mettere la recommendation enorme e l'incertezza in piccolo.

Se il caveat attraversa lo switching value del Capitolo 15, è P1 anch'esso.

Esempio:

> “Progetto con beneficio centrale €1,2M”

ma range plausibile:

> “€0,4M–€1,9M contro costo €1,0M.”

Il range non è footnote. È parte del messaggio principale.

## Accessibilità e gerarchia

La gerarchia non può dipendere soltanto dal colore. W3C WCAG 2.2 richiede che il colore non sia l'unico mezzo per distinguere informazione; testo, forma, etichette e struttura devono fornire ridondanza.

Questa non è una limitazione creativa. È una buona disciplina comunicativa anche per chi vede perfettamente i colori.

> **La gerarchia visiva è una decisione su dove spendere l'attenzione del lettore. Va allocata con la stessa disciplina con cui allochiamo tempo e budget analitico.**

### Fonti

- W3C, *WCAG 2.2 — Understanding 1.4.1 Use of Color*: https://www.w3.org/WAI/WCAG22/Understanding/use-of-color.html
- Government Analysis Function, *Accessible charts: a checklist of the basics*: https://analysisfunction.civilservice.gov.uk/policy-store/accessible-charts-a-checklist-of-the-basics/
