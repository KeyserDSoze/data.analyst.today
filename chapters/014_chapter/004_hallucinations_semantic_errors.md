## 14.3 Confabulation, semantic error e narrative overreach: capire dove l'output può rompersi

Una risposta palesemente assurda è spesso meno pericolosa di una risposta convincente che fallisce in un punto nascosto della catena. Per verificare bene un output AI non basta chiedere "è giusto?". Dobbiamo chiederci **in quale boundary potrebbe essere sbagliato**, perché errori diversi richiedono controlli diversi.

Una classificazione compatta aiuta:

| Failure class | Che cosa succede | Controllo principale |
|---|---|---|
| Entity / factual confabulation | compare un oggetto o fatto non supportato | existence / source verification |
| Structural error | oggetti reali vengono collegati nel modo sbagliato | grain, keys, cardinality, population reconciliation |
| Semantic error | un campo vero rappresenta il concetto sbagliato | metric/date/filter contract |
| Computational error | il calcolo implementa male una regola corretta | fixture, unit test, independent calculation |
| Narrative overreach | i numeri sono corretti ma il testo supera l'evidenza | claim classification |
| Action overreach | il sistema compie un'azione oltre l'autorizzazione | permission + approval gate |

Questa tassonomia è più utile di usare "hallucination" per qualunque problema, perché indica anche **come falsificare l'output**.

### Campo reale, concetto sbagliato

Microsoft Learn documenta un esempio molto istruttivo in Power BI: a una domanda sul paese con il profitto più alto nel 2024/2023, Copilot applica il filtro temporale alla colonna **Birthday** della tabella Customer invece della date table corretta. Il campo esiste, il filtro è tecnicamente valido e l'output può sembrare plausibile; il concetto temporale, però, è sbagliato.

Fonte: https://learn.microsoft.com/en-us/power-bi/create-reports/copilot-semantic-models

È un **semantic error**, non un problema di sintassi. La mitigazione può richiedere un semantic model meno ambiguo, AI data schemas, istruzioni, verified answers e soprattutto capacità del reviewer di vedere quali campi e filtri sono stati usati. Un prompt migliore può aiutare, ma non sostituisce il boundary semantico.

### +18,3% non è un treatment effect

Un retailer invia una campagna CRM a clienti VIP. La conversion osservata è `14,2%` nei trattati e `12,0%` nei non trattati. L'AI calcola correttamente:

```text
(14,2 - 12,0) / 12,0 = +18,3%
```

Poi scrive: "La campagna ha aumentato la conversion del 18,3%." L'aritmetica è corretta; il claim no. I destinatari erano selezionati perché più attivi e di maggior valore, quindi il confronto osservazionale non identifica l'effetto incrementale della campagna. Il claim consentito è molto più limitato:

> La conversion osservata è 2,2 punti percentuali più alta nel gruppo trattato; il confronto osservazionale non identifica l'effetto causale della campagna.

Qui la Control Sheet deve poter dire semplicemente:

```text
causal claim allowed: NO
```

### Claim ladder

Per impedire che il linguaggio promuova automaticamente la certezza, usiamo una **claim ladder**:

| Livello | Claim consentito |
|---|---|
| L0 — Extraction | il valore è 4,6% |
| L1 — Description | è aumentato di 0,8 punti |
| L2 — Localization / association | il delta è concentrato nei clienti con tenure <90 giorni |
| L3 — Prediction | il modello stima maggiore probabilità futura per questo gruppo |
| L4 — Causal claim | l'intervento produce una differenza nel risultato |
| L5 — Recommendation | l'azione A è preferibile date evidenza, costi e vincoli |

Ogni gradino richiede evidenza aggiuntiva. Un sistema non può salire di livello perché sa produrre una frase più fluida.

### Triangolazione significa percorsi realmente diversi

Per un KPI importante possiamo confrontare una query AI-generated con la metrica semantica certificata, una reconciliation Finance/Operations e l'ordine di grandezza storico. Se l'AI produce €13,8M e percorsi indipendenti producono circa €12,4M, chiedere al modello "sei sicuro?" non aggiunge evidenza. Dobbiamo ispezionare popolazione, date, join, filtri, duplicati e versione della definizione.

Anche la triangolazione può essere falsa se i percorsi condividono la stessa dipendenza. Tre agenti che leggono la stessa metrica errata non sono tre conferme indipendenti. Torneremo su questo punto nei failure mode organizzativi.

### Verification depth proporzionata alla conseguenza

Il NIST Generative AI Profile raccomanda gestione e valutazione del rischio proporzionate al contesto. Nel nostro workflow la conseguenza pratica può essere questa:

| Output | Conseguenza | Gate minimo |
|---|---|---|
| spiegazione sintassi | bassa | review rapida |
| query esplorativa | moderata | fixture + sanity check |
| KPI management | alta | reconciliation + peer review |
| recommendation economica rilevante | alta | evidence review + assumptions |
| write/action automatico | molto alta | eval + permission + approval/rollback |

Fonte: https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence

La AI Analysis Control Sheet registra quindi failure class potenziali, claim richiesto e supportato, controlli fattuali/strutturali/semantici/computazionali, reconciliation indipendente, authorization e incertezza non risolta.

> **Non verificare un output AI chiedendoti soltanto se è giusto. Chiediti dove potrebbe essere sbagliato: oggetto, struttura, significato, calcolo, interpretazione o azione. Ogni classe richiede un controllo diverso.**
