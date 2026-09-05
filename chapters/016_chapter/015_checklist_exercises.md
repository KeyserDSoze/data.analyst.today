## 16.14 Decision Communication Pack: gate finale ed esercizi

Il prodotto finale del capitolo non è “un bel grafico”. È una **Decision Communication Pack** che preserva il Decision Record mentre riduce il costo cognitivo per il destinatario.

La Pack deve essere abbastanza compatta da guidare una decisione e abbastanza tracciabile da permettere a chi contesta un claim di risalire alla prova. Per questo il template finale conserva struttura operativa.

## Template canonico

```text
DECISION COMMUNICATION PACK

1. AUDIENCE
reader:
decision owner:
assumed knowledge:
who bears downside:

2. DECISION
choice between:
decision requested today:
deadline:

3. HEADLINE / CLAIM
headline:
claim level:
main caveat:

4. PRIMARY EVIDENCE
artifact 1: role / source / claim
artifact 2: role / source / claim
artifact 3: role / source / claim
artifact 4: role / source / claim

5. CONTEXT CONTRACT
metric definition:
population / denominator:
period:
baseline / target:
freshness:
maturity:
method break / event annotation:

6. UNCERTAINTY
what can change choice:
switching value:
distance from boundary:

7. ALTERNATIVES
preferred option:
strongest alternative:
business as usual if relevant:

8. VISUAL INTEGRITY
scale:
period selection:
denominator:
encoding:
opposite-framing test:

9. ACCESSIBILITY
redundant encoding:
contrast / labels:
no hover-only critical info:
alt text:
table/text alternative:
keyboard / focus if interactive:

10. MEETING
30-second opening:
challenge map:
claim-threatening conditions:
appendix:

11. PROVENANCE
Decision Record:
metric/data version:
data as-of:
analysis source:
owner:

12. LEARNING
decision taken:
review date:
next evidence / guardrail:
```

Il template non va riempito meccanicamente per ogni chart. Serve per comunicazioni in cui una cattiva compressione può cambiare la scelta.

## Communication Readiness Gate

La Pack può terminare in tre stati.

**READY** significa che decision question, claim, primary evidence, caveat decision-critical, integrity, accessibility e provenance sono coerenti con l'uso previsto.

**READY WITH CAVEATS** significa che la comunicazione è utilizzabile, ma un limite deve accompagnarla esplicitamente. Un esempio è un forecast abbastanza maturo per capacity planning preliminare ma ancora `PROVISIONAL` su un feed importante.

**NOT READY** è lo stato corretto quando la headline supera il claim, il dato è troppo immaturo, una definizione resta ambigua, il framing nasconde un'alternativa materiale, scala o denominatore alterano l'impressione oppure la provenance non è ricostruibile. La pressione del meeting non trasforma `NOT READY` in `READY`.

---

## Esercizio 1 — Dal Decision Record alla Pack

Decision Record sintetico:

- decisione: aumentare o no il prezzo del piano Pro;
- alternative: +0%, +3%, +7%;
- recommendation analytics: +3% con pilot;
- uplift revenue centrale: +4,2%;
- downside principale: renewal rate;
- switching value: la scelta cambia se renewal peggiora oltre 0,9 pp;
- evidenza causale: test precedente su un segmento, non sull'intera base;
- decision owner: CRO.

Costruisci una Pack di una pagina con headline, decision requested, massimo tre visual/table, caveat, alternative, switching value e provenance. Poi scrivi una headline deliberatamente troppo forte e spiega quale claim level viola.

---

## Esercizio 2 — Visual Integrity Gate

Conversion rate:

```text
control:   97,8%
treatment: 98,4%
```

Progetta tre rappresentazioni: una manipolativa, una tecnicamente corretta ma cognitivamente debole e una decision-ready. Per ciascuna indica scala, encoding, impressione probabile e rischio decisionale. La versione finale deve rendere visibili proporzione, delta e uncertainty rilevante.

---

## Esercizio 3 — Opposite-framing test

Una campagna mostra ROAS **4,1** nella settimana post-lancio contro **3,2** nella settimana precedente. Costruisci il framing più favorevole, il framing più sfavorevole usando confronti plausibili e infine il framing professionale. Elenca quali dati devi conoscere prima di scegliere: stagionalità, holdout, spend mix, delayed conversion, baseline storica o altro.

---

## Esercizio 4 — Dashboard da ridurre

Una executive dashboard contiene 28 KPI, 10 slicer, due mappe e 14 visual. Le decisioni settimanali reali sono riallocare inventory, intervenire sulle regioni sotto SLA, aggiornare il forecast e approvare eccezioni commerciali.

Ridisegna l'architettura in **decision layer**, **diagnostic layer** ed **evidence/export layer**. Per ogni elemento rimosso dalla home spiega quale task serviva e perché non è decision-critical nella prima vista.

---

## Esercizio 5 — Uncertainty communication

Un progetto costa **€1,0M**. Il beneficio centrale è **€1,25M**, con range plausibile **€0,55M–€1,85M**. Il CFO vuole una sola cifra sulla slide.

Prepara una comunicazione sbagliata e una headline corretta. Disegna la forma che mostra range e break-even e discuti la scelta se un pilot da **€80k** potesse ridurre fortemente l'incertezza.

---

## Esercizio 6 — Meeting challenge

Durante una presentazione il CFO scopre che un segmento contiene una riclassificazione recente. Scrivi come gestiresti quattro casi differenti: errore locale con claim invariato, dettaglio disponibile in appendix, problema claim-threatening e follow-up non blocking. L'obiettivo non è apparire sicuri, ma diagnosticare l'impatto sul Decision Record.

---

## Esercizio 7 — Accessibility audit

Prendi una dashboard reale o pubblica e verifica color-only encoding, contrasto, dimensione del testo, hover-only information, alt text, keyboard navigation, ordine di lettura, disponibilità di tabella/dati, comportamento su schermo piccolo e leggibilità in screenshot/PDF.

Proponi almeno cinque modifiche e indica quali migliorano anche la comprensione per utenti senza esigenze assistive specifiche.

Riferimenti:

- W3C, *Web Content Accessibility Guidelines (WCAG) 2.2*, https://www.w3.org/TR/WCAG22/
- Microsoft Learn, *Design Power BI reports for accessibility*, https://learn.microsoft.com/en-us/power-bi/create-reports/desktop-accessibility-creating-reports

---

## Esercizio 8 — NorthRiver, secondo round

Riprendi il caso 16.12. Il feed preorder finale riduce il forecast centrale da **162k a 153k pacchi/giorno** e P80 da **171k a 164k**. La capacità interna resta **148k**. Il carrier propone di ridurre il commitment B da **€780k a €620k** in cambio di una capacità massima di **163k**.

Aggiorna Decision Record, switching value, recommendation, headline, primary visual e decision requested. Indica quali parti della vecchia Pack diventano obsolete e non devono essere riutilizzate per inerzia.

---

## Esercizio 9 — Accessibility by design

Usa WCAG 2.2 e la guida Microsoft per progettare un mini-standard interno per dashboard: color policy, contrast, alt text, keyboard/focus, table alternative, test su device e ownership del controllo. Distingui requisiti di accessibilità da semplici preferenze estetiche.

---

## Esercizio 10 — Decision Communication Pack completa

Scegli una decisione reale o simulata e produci:

1. Decision Record sintetico;
2. decision layer da 30 secondi;
3. evidence layer con massimo quattro visual;
4. provenance/appendix;
5. Context Contract;
6. Visual Integrity Gate;
7. Accessibility Gate;
8. script di apertura del meeting;
9. challenge map;
10. stato finale `READY / READY WITH CAVEATS / NOT READY`.

La verifica finale non riguarda la bellezza del materiale. Chiedi se una persona può capire la scelta più rapidamente **senza** ricevere un claim più forte, una uncertainty più piccola o un'alternativa meno credibile di quelle contenute nel Decision Record.

## Chiusura del capitolo

Il Capitolo 15 ha costruito la decisione rispetto ad alternative, rischio, uncertainty e reversibilità. Questo capitolo ha aggiunto una responsabilità: **preservare quelle proprietà durante la compressione**.

La catena finale è:

```text
Decision Record
→ Decision Communication Pack
→ interpretazione / challenge
→ scelta
→ azione
→ learning
```

Questo prepara il Capitolo 17. Nei casi end-to-end non basterà scegliere il metodo analitico corretto: dovremo anche scegliere **quale evidenza merita di arrivare alla decisione e con quale forma**, senza trasformare il capstone in una dimostrazione di tecniche.

> **La comunicazione analitica è riuscita quando rende la decisione più facile da capire senza renderla artificialmente più facile da accettare.**

### Fonti

- W3C, *Web Content Accessibility Guidelines (WCAG) 2.2*, https://www.w3.org/TR/WCAG22/
- Microsoft Learn, *Design Power BI reports for accessibility*, https://learn.microsoft.com/en-us/power-bi/create-reports/desktop-accessibility-creating-reports
- Government Analysis Function, *Data visualisation: testing dashboards for design and accessibility*, https://analysisfunction.civilservice.gov.uk/policy-store/data-visualisation-testing-dashboards-for-design-and-accessibility/
