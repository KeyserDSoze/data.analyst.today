## 16.14 Decision Communication Pack: gate finale ed esercizi

Il prodotto finale del capitolo non è “un bel grafico”.

È una **Decision Communication Pack** che preserva il Decision Record mentre riduce il costo cognitivo per il destinatario.

## Il template

### 1. Audience

- chi deve leggere?
- chi deve decidere?
- quali conoscenze possiamo assumere?
- quale stakeholder sostiene il downside della scelta?

### 2. Decision question

Scrivere la scelta in forma esplicita:

> **“Dobbiamo scegliere tra...”**

Se non esistono alternative reali, probabilmente stiamo preparando un report e non una comunicazione decisionale.

### 3. Decision requested

Che cosa chiediamo oggi?

- approve;
- reject;
- pilot;
- wait for X;
- escalate;
- monitor;
- allocate budget;
- change policy.

### 4. Headline / claim level

Una frase che:

- risponde alla domanda;
- non supera la forza dell'evidenza;
- non nasconde il caveat che potrebbe cambiare la scelta.

### 5. Primary evidence

Massimo 2–4 elementi nella vista principale.

Per ciascuno:

- ruolo `orient / compare / diagnose / decide / verify`;
- fonte;
- definizione;
- periodo;
- visual/table scelto;
- claim sostenuto.

### 6. Context Contract

- baseline;
- target;
- denominatore/population;
- freshness;
- provisional/final;
- methodological break;
- event annotation.

### 7. Uncertainty e switching value

- quale incertezza è decision-critical?
- attraversa la soglia che cambierebbe scelta?
- il caveat è visibile nel layer executive?

### 8. Alternatives

Almeno l'alternativa più credibile deve restare rappresentata quando il trade-off è materiale.

La comunicazione non deve trasformare la recommendation in un'unica opzione apparentemente possibile.

### 9. Visual Integrity Gate

- scala corretta;
- periodo non cherry-picked;
- denominatore coerente;
- encoding proporzionale;
- confronto appropriato;
- titolo claim-safe;
- opposite-framing test superato.

### 10. Accessibility Gate

- il colore non è l'unico encoding;
- informazioni essenziali esistono senza hover;
- contrasto e label sono leggibili;
- alt text utile;
- forma tabellare/testuale disponibile quando necessaria;
- navigazione da tastiera verificata se il prodotto è interattivo.

### 11. Meeting plan

Preparare:

- opening di 30 secondi;
- challenge map;
- appendix;
- regola per `answer now / appendix / claim-threatening / follow-up`.

### 12. Provenance e learning

- link al Decision Record;
- metric definitions;
- analysis source;
- version/timestamp;
- owner;
- decisione effettivamente presa;
- data di review.

## Communication Readiness Gate

Prima della consegna assegniamo uno stato.

### READY

- decision question chiara;
- claim sostenuto;
- evidenza sufficiente;
- caveat decision-critical visibile;
- visual integrity e accessibility gate superati;
- provenance disponibile.

### READY WITH CAVEATS

La comunicazione può essere usata, ma un limite deve accompagnarla esplicitamente.

Esempio:

> “Forecast utilizzabile per capacity planning preliminare; preorder retailer C ancora provisional.”

### NOT READY

Blocchiamo la comunicazione decisionale se:

- la headline supera il claim consentito;
- il dato è troppo immaturo;
- una definizione è ambigua;
- il framing nasconde un'alternativa materiale;
- un errore di scala/denominatore altera il messaggio;
- non possiamo ricostruire la provenance.

La pressione del meeting non trasforma `NOT READY` in `READY`.

---

## Esercizio 1 — Dal Decision Record alla Pack

Hai questo Decision Record sintetico:

- decisione: aumentare o no il prezzo del piano Pro;
- alternative: +0%, +3%, +7%;
- recommendation analytics: +3% con pilot;
- uplift revenue centrale: +4,2%;
- downside principale: renewal rate;
- switching value: la scelta cambia se renewal peggiora oltre 0,9 pp;
- evidenza causale: test precedente su un segmento, non sull'intera base;
- decision owner: CRO.

Costruisci una Decision Communication Pack di una pagina con:

1. headline;
2. decision requested;
3. massimo tre visual/table;
4. caveat;
5. alternative;
6. switching value;
7. appendix/provenance.

Poi scrivi una headline **troppo forte** e spiega perché non è consentita.

## Esercizio 2 — Visual Integrity Gate

Conversion rate:

- control: 97,8%;
- treatment: 98,4%.

Progetta tre rappresentazioni:

1. una deliberatamente manipolativa;
2. una tecnicamente corretta ma cognitivamente debole;
3. una decision-ready che mostri proporzione, delta e incertezza.

Per ciascuna identifica:

- scala;
- encoding;
- impressione probabile;
- rischio di decisione.

## Esercizio 3 — Opposite framing test

Una campagna mostra ROAS 4,1 nella settimana post-lancio contro 3,2 nella settimana precedente.

Costruisci:

- il framing più favorevole alla campagna;
- il framing più sfavorevole usando dati plausibili aggiuntivi;
- la visualizzazione che useresti professionalmente.

Indica quali confronti devi conoscere prima di scegliere la versione finale: stagionalità, holdout, spend mix, delayed conversion, baseline storica o altro.

## Esercizio 4 — Dashboard da ridurre

Una executive dashboard contiene 28 KPI, 10 slicer, due mappe e 14 visual.

Le decisioni settimanali reali sono:

1. riallocare inventory;
2. intervenire sulle regioni sotto SLA;
3. aggiornare il forecast;
4. approvare eccezioni commerciali.

Ridisegna l'architettura in:

- executive/decision layer;
- diagnostic layer;
- evidence/export layer.

Per ogni elemento eliminato spiega perché non appartiene alla home.

## Esercizio 5 — Uncertainty communication

Un progetto costa €1,0M.

Beneficio stimato:

- point estimate: €1,25M;
- range plausibile: €0,55M–€1,85M.

Il CFO vuole una sola cifra sulla slide.

Prepara:

- una comunicazione sbagliata;
- una headline corretta;
- la forma visiva che mostra il threshold;
- la decisione che suggeriresti se un pilot da €80k potesse ridurre fortemente l'incertezza.

## Esercizio 6 — Meeting challenge

Durante una presentazione il CFO scopre che un segmento contiene una riclassificazione recente.

Scrivi quattro possibili risposte, una per ogni classe:

- local error, claim unchanged;
- evidence in appendix;
- claim-threatening;
- follow-up non blocking.

L'obiettivo non è apparire sicuri. È diagnosticare l'impatto sulla decisione.

## Esercizio 7 — Accessibility audit

Prendi una dashboard reale o pubblica e verifica:

- color-only encoding;
- contrasto;
- dimensione del testo;
- hover-only information;
- alt text;
- keyboard navigation;
- ordine di lettura;
- disponibilità di tabella/dati;
- comportamento su schermo piccolo;
- leggibilità in screenshot o PDF.

Proponi almeno cinque modifiche e indica quali migliorano anche la comprensione per tutti gli utenti.

## Esercizio 8 — Caso NorthRiver, secondo round

Riprendi il caso 16.12.

Il feed preorder finale riduce il forecast centrale da 162k a 153k pacchi/giorno e P80 da 171k a 164k.

La capacità interna resta 148k.

Il carrier propone però di ridurre il commitment dell'opzione B da €780k a €620k in cambio di una capacità massima di 163k.

Aggiorna:

- Decision Record;
- switching value;
- recommendation;
- headline;
- primary visual;
- decision requested.

Spiega quale parte della vecchia Pack diventa obsoleta e deve essere sostituita.

## Esercizio 9 — Caso pubblico: accessibility by design

Leggi le linee guida W3C WCAG 2.2 e la guida Microsoft per l'accessibilità dei report Power BI.

Progetta un mini standard interno per dashboard analitiche con:

- color policy;
- contrast;
- alt text;
- keyboard/focus;
- table alternative;
- test su device;
- ownership del controllo.

Distingui requisiti di accessibilità da semplici preferenze estetiche.

## Esercizio 10 — Decision Communication Pack completa

Scegli una decisione reale o simulata e produci:

1. Decision Record sintetico;
2. Pack executive da 30 secondi;
3. evidence layer da massimo quattro visual;
4. appendix/provenance;
5. Context Contract;
6. Visual Integrity Gate;
7. Accessibility Gate;
8. script di apertura del meeting;
9. challenge map;
10. stato finale `READY / READY WITH CAVEATS / NOT READY`.

## Chiusura del capitolo

Il Capitolo 15 ci ha insegnato che una decisione deve essere valutata rispetto ad alternative, rischio, incertezza e reversibilità.

Questo capitolo aggiunge un'altra responsabilità:

> **preservare quelle proprietà quando l'analisi viene compressa per essere comunicata.**

Una buona visualizzazione non sostituisce una buona analisi.

Una buona analisi non garantisce una buona decisione.

Una buona decisione può essere comunicata male.

La professionalità consiste nel mantenere la catena integra:

**Decision Record → Communication Pack → interpretazione → scelta → azione → learning**.

> **La comunicazione analitica è riuscita quando rende la decisione più facile da capire senza renderla artificialmente più facile da accettare.**

### Fonti per gli esercizi

- W3C, *Web Content Accessibility Guidelines (WCAG) 2.2*: https://www.w3.org/TR/WCAG22/
- Microsoft Learn, *Design Power BI reports for accessibility*: https://learn.microsoft.com/en-us/power-bi/create-reports/desktop-accessibility-creating-reports
- Government Analysis Function, *Data visualisation: testing dashboards for design and accessibility*: https://analysisfunction.civilservice.gov.uk/policy-store/data-visualisation-testing-dashboards-for-design-and-accessibility/
