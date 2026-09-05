# Capitolo 16 — Data storytelling, dashboard ed executive communication

## 16.0 Comunicare bene significa comprimere senza deformare

Nel Capitolo 15 abbiamo costruito il **Decision Record**: una scelta esplicita tra alternative, sostenuta da evidenza, uncertainty, trade-off, switching value, guardrail e condizioni per cambiare idea. Il problema successivo non è più costruire la decisione, ma trasferirla a qualcun altro senza alterarne il significato.

Questa è la tesi del capitolo:

> **Una buona comunicazione analitica riduce il costo cognitivo senza aumentare la forza del claim, nascondere l'incertezza o cambiare il significato della decisione.**

La comunicazione non è quindi il momento in cui “abbelliamo” un'analisi già finita. È un nuovo passaggio della catena di qualità. Titolo, scala, baseline, ordine dei visual, precisione mostrata, colore, annotazioni e livello di dettaglio decidono quali relazioni diventano percettivamente dominanti. Se questa selezione non rispetta il Decision Record, possiamo trasformare dati corretti in una decisione peggiore senza falsificare nemmeno un numero.

### Un numero corretto può produrre una storia sbagliata

Immaginiamo una società SaaS che porta al leadership team il churn mensile. Il valore passa dal **2,8% al 3,4%** e la slide usa un asse verticale da 2,5% a 3,5% con il titolo **“Churn in forte accelerazione”**. La reazione immediata è spostare **€2 milioni** dal budget acquisition a retention.

La misura non è errata. Il problema emerge quando riportiamo nella comunicazione tre elementi rimasti nell'analisi: negli ultimi tre anni il churn ha oscillato tra **2,7% e 3,5%**; il **72% del delta** corrente proviene da una singola coorte annuale arrivata al rinnovo; i clienti attivati negli ultimi sei mesi sono sostanzialmente stabili. Il framing aveva reso dominante la lettura “crisi generalizzata”, mentre l'evidenza supportava una conclusione più circoscritta.

Una headline coerente con il Decision Record potrebbe diventare:

> **Il churn è salito al 3,4%, vicino al limite superiore dello storico; il deterioramento è concentrato nella coorte annuale in rinnovo. L'evidenza non supporta per ora una riallocazione generalizzata del budget.**

Lo stesso numero produce una scelta diversa perché baseline, composizione e scope del claim sono tornati visibili.

## La comunicazione come compressione semantica

Un'analisi può richiedere quaranta query, venticinque grafici esplorativi, dodici segmentazioni, robustness check e un modello. Il decision maker non ha bisogno di ripercorrere la cronologia dell'indagine; deve però poter accedere alla stessa evidenza a profondità differenti senza incontrare tre versioni diverse della verità.

Per questo useremo tre layer coerenti:

| Layer | Scopo |
|---|---|
| **Decision** | in circa 30 secondi: scelta aperta, recommendation, ragione principale, caveat e ask |
| **Evidence** | in 5–10 minuti: 2–4 elementi che discriminano davvero le alternative, con uncertainty e guardrail |
| **Provenance** | per audit: definizioni, dataset, query, metodi, controlli, freshness, versioni e appendix |

La sintesi è riuscita quando possiamo scendere dal titolo al dato sorgente senza scoprire che, durante la compressione, è cambiata popolazione, definizione, causal status o livello di certezza.

## Dal Decision Record alla Decision Communication Pack

Il deliverable canonico sarà la **Decision Communication Pack**. Non è necessariamente una slide o un file unico: è il contratto tra ciò che il Decision Record consente di sostenere e ciò che il pubblico vede.

```text
Decision Record
→ audience + decision question
→ evidence promotion
→ visual/context contract
→ uncertainty + alternatives
→ decision request
→ provenance
```

Una Pack minima deve rendere recuperabili almeno audience, decision question, headline, primary evidence, baseline/denominator, uncertainty decision-critical, alternative rilevanti, decision requested, guardrail e provenance.

Il criterio è importante: non partiamo dal dataset chiedendoci quale grafico “racconta meglio” la storia. Partiamo dalla decisione e chiediamo **quale minima evidenza deve essere resa facile da percepire perché quella scelta possa essere valutata correttamente**.

## Visualizzare significa progettare l'attenzione

Una linea facilita la lettura del cambiamento nel tempo; barre allineate rendono più facile confrontare magnitudini; uno scatter rende visibili relazione, dispersione e outlier; small multiples consentono di confrontare pattern con una grammatica comune; una tabella favorisce lookup e verifica precisa. Nessuna forma è “migliore” in assoluto: ognuna abbassa il costo cognitivo di alcuni confronti e può aumentare quello di altri.

La stessa logica vale per le dashboard. Microsoft raccomanda di partire dal pubblico, mettere in evidenza ciò che serve davvero e ridurre il clutter; la Government Analysis Function britannica nel 2026 insiste su user needs, gerarchia, testing reale, dispositivi diversi e forme alternative di accesso ai dati. La lezione che ci interessa è più generale del prodotto: **una dashboard utile organizza l'attenzione intorno a decisioni e anomalie, non intorno a tutto ciò che il sistema sa misurare**.[^ms-dashboard][^gaf-dashboard]

## Il limite etico del data storytelling

Comunicare significa selezionare. Selezionare significa inevitabilmente escludere qualcosa. La responsabilità professionale consiste nel non escludere proprio ciò che renderebbe la conclusione meno conveniente ma più corretta: una baseline sfavorevole, un intervallo che attraversa il break-even, un segmento contrario all'aggregato, una definizione cambiata, una spiegazione alternativa o un guardrail deteriorato.

Per questo il data storytelling non trasforma l'analista nell'avvocato della propria recommendation. Lo trasforma in un **curatore dell'evidenza decisionale**: deve rendere facile vedere ciò che conta senza rendere artificialmente facile accettare una scelta.

Il percorso del capitolo sarà quindi:

**Decision Record → evidence promotion → visual encoding → dashboard/gerarchia → contesto → uncertainty → executive summary → integrity → meeting → accessibility → provenance**.

Il Capitolo 17 partirà da qui per affrontare casi end-to-end: la comunicazione non sarà l'ultima vernice applicata al lavoro, ma l'ultimo passaggio che deve preservare il percorso analitico scelto.

[^ms-dashboard]: Microsoft Learn, *Tips for designing a great Power BI dashboard*, https://learn.microsoft.com/en-us/power-bi/create-reports/service-dashboards-design-tips
[^gaf-dashboard]: Government Analysis Function, *Data visualisation: testing dashboards for design and accessibility*, https://analysisfunction.civilservice.gov.uk/policy-store/data-visualisation-testing-dashboards-for-design-and-accessibility/
