# Capitolo 16 — Data storytelling, dashboard ed executive communication

## 16.0 Comunicare bene significa comprimere senza deformare

Nel Capitolo 15 abbiamo costruito il **Decision Record**: decisione, alternative, evidenza, incertezza, trade-off, switching value, raccomandazione, owner e condizioni di revisione.

Il lavoro non è ancora finito.

Una decisione può essere analiticamente ben costruita e venire comunque comunicata in modo da:

- enfatizzare il dettaglio sbagliato;
- nascondere l'incertezza che conta;
- far sembrare causale un'associazione;
- trasformare una variazione piccola in una crisi visiva;
- sommergere il decision maker sotto informazioni corrette ma irrilevanti;
- lasciare implicita la domanda più importante: **che cosa dobbiamo decidere adesso?**

Il problema della comunicazione analitica non è quindi rendere i dati più belli.

È **ridurre il costo cognitivo senza ridurre l'integrità dell'evidenza**.

## Compressione informativa e perdita di significato

Un'analisi può contenere:

- 40 query;
- 25 grafici esplorativi;
- 12 segmentazioni;
- tre robustness check;
- un modello;
- un intervallo di incertezza;
- cinque alternative;
- una raccomandazione.

Il CEO non leggerà tutto prima del meeting.

Questo non significa che il rigore debba sparire. Significa che dobbiamo costruire **livelli di accesso alla stessa evidenza**.

Una buona comunicazione permette almeno tre letture:

1. **30 secondi** — qual è la decisione e perché conta;
2. **5–10 minuti** — quali evidenze sostengono la raccomandazione e quale incertezza può cambiarla;
3. **audit** — come sono stati definiti metriche, filtri, metodi, fonti e controlli.

La sintesi è buona quando i tre livelli restano semanticamente coerenti.

## Caso simulato/composito — Il churn che sembrava una crisi

Una società SaaS presenta al leadership team il churn mensile degli ultimi dodici mesi.

Il numero è corretto:

- churn precedente: 2,8%;
- churn corrente: 3,4%.

La slide mostra una linea con asse verticale da 2,5% a 3,5% e un titolo:

> **Churn in forte accelerazione**

La reazione immediata è spostare €2 milioni dal budget acquisition a retention.

Prima della decisione emergono però tre elementi rimasti fuori dalla slide:

- negli ultimi tre anni il churn mensile ha oscillato tra 2,7% e 3,5%;
- il 72% del delta corrente proviene da una singola coorte annuale arrivata al rinnovo;
- il churn dei clienti attivati negli ultimi sei mesi è stabile.

Il grafico non era falso.

Il numero non era falso.

Il **framing aveva reso cognitivamente dominante una lettura non sufficientemente supportata**.

La comunicazione corretta potrebbe diventare:

> **Il churn è salito a 3,4%, vicino al limite superiore dello storico. Il deterioramento è concentrato nella coorte annuale in rinnovo; non vediamo per ora un peggioramento generalizzato. Raccomandiamo un intervento mirato sulla coorte e monitoraggio per due cicli, non una riallocazione generalizzata del budget.**

Lo stesso dato produce una decisione diversa perché è cambiato il contesto decisionale.

## Dal Decision Record alla Decision Communication Pack

Il deliverable centrale di questo capitolo sarà la **Decision Communication Pack**.

Non è necessariamente un file unico. È un contratto tra ciò che abbiamo deciso di sostenere e ciò che il pubblico vedrà.

Una versione minima contiene:

| Campo | Domanda |
|---|---|
| Audience | Chi deve capire o decidere? |
| Decision question | Quale scelta è aperta? |
| Headline | Qual è il messaggio principale consentito dall'evidenza? |
| Evidence | Quali 2–4 elementi sono sufficienti a sostenerlo? |
| Context | Quale baseline, target, denominatore o evento è indispensabile? |
| Uncertainty | Quale incertezza può cambiare la decisione? |
| Alternatives | Quali opzioni devono restare visibili? |
| Decision requested | Che cosa chiediamo al destinatario oggi? |
| Guardrail / next step | Cosa monitoriamo dopo? |
| Provenance | Dove troviamo definizioni, dati, metodo e appendix? |

Il principio è:

**Decision Record → Decision Communication Pack**

non:

**dataset → grafico interessante → storia**.

## Visualizzare significa scegliere cosa rendere facile da vedere

Ogni forma visiva rende alcune relazioni più immediate di altre.

- una linea facilita la lettura del cambiamento nel tempo;
- barre allineate facilitano il confronto tra categorie;
- uno scatter plot facilita la lettura di relazione, dispersione e outlier;
- small multiples facilitano il confronto di pattern ripetuti;
- una tabella facilita il recupero di valori precisi.

La scelta del grafico è quindi una scelta su **quale struttura rendere percettivamente dominante**.

Per questo non è neutrale.

## Dashboard non significa archivio di KPI

Microsoft raccomanda di progettare dashboard partendo dal pubblico, mettere in evidenza le informazioni più importanti e ridurre il clutter. La Government Analysis Function britannica, nelle linee guida 2026 sul testing dei dashboard, insiste inoltre su user needs, accessibilità, test su dispositivi diversi e disponibilità di contenuti alternativi ai grafici interattivi.

Il principio generale è più importante di qualsiasi tool:

> **Una dashboard utile organizza l'attenzione intorno a decisioni e anomalie; non espone semplicemente tutto ciò che il sistema sa misurare.**

## Il limite etico della comunicazione

Comunicare significa selezionare.

Selezionare significa inevitabilmente escludere qualcosa.

La responsabilità professionale consiste nel non escludere proprio ciò che renderebbe la conclusione meno conveniente ma più corretta:

- una baseline sfavorevole alla nostra storia;
- un intervallo ampio;
- un segmento che contraddice l'aggregato;
- una definizione cambiata;
- una spiegazione alternativa;
- un guardrail deteriorato.

Il data storytelling non deve trasformare l'analista in un avvocato della propria raccomandazione.

Deve trasformarlo in un **curatore dell'evidenza decisionale**.

## Il percorso del capitolo

Costruiremo la Decision Communication Pack attraverso:

**audience → domanda → evidence hierarchy → visual encoding → contesto → incertezza → executive summary → storytelling integrity → dashboard design → meeting → accessibilità → provenance**.

La tesi centrale è:

> **Una buona comunicazione analitica comprime la complessità senza aumentare la forza del claim, nascondere l'incertezza o cambiare il significato della decisione.**

### Fonti

- Microsoft Learn, *Tips for designing a great Power BI dashboard*: https://learn.microsoft.com/en-us/power-bi/create-reports/service-dashboards-design-tips
- Government Analysis Function, *Data visualisation: testing dashboards for design and accessibility*: https://analysisfunction.civilservice.gov.uk/policy-store/data-visualisation-testing-dashboards-for-design-and-accessibility/
