## 15.1 Finding, insight, explanation e implication: quattro livelli da non confondere

Uno degli errori più comuni nel lavoro analitico è chiamare *insight* qualsiasi numero non ovvio.

Ma sorpresa, spiegazione e utilità decisionale sono proprietà diverse.

### Livello 1 — Finding

> “La conversion desktop è stabile; quella mobile è scesa del 9%.”

Descrive il fenomeno.

### Livello 2 — Structure / localization

> “Il calo mobile è concentrato sulle sessioni che attraversano il nuovo checkout e spiega circa il 78% della perdita di ordini.”

Localizza dove vive il fenomeno.

### Livello 3 — Explanation hypothesis

> “Il nuovo checkout potrebbe aver introdotto frizione.”

Propone un meccanismo compatibile con l'evidenza.

### Livello 4 — Decision implication

> “Poiché il problema è concentrato in un flusso reversibile e ad alta esposizione, conviene congelare il rollout e testare il vecchio checkout come controllo.”

Collega l'evidenza a una scelta.

Questa sequenza evita due salti pericolosi:

```text
pattern → causa
pattern → azione
```

senza aver esplicitato né il livello di evidenza né le alternative.

### Insight come compressione decisionale

In questo libro useremo *insight* in senso operativo:

> **un insight è una sintesi dell'evidenza che modifica in modo materiale la rappresentazione del problema e quindi lo spazio delle decisioni plausibili.**

Non deve essere sempre causale.

Deve però rispondere almeno a una di queste domande:

- dove è concentrato il valore o il rischio?
- quale popolazione è diversa da quella che credevamo?
- quale assunzione precedente non regge?
- quale alternativa diventa più o meno attraente?
- quale ulteriore informazione vale la pena raccogliere?

### Caso simulato/composito — Paid Social sembrava il canale peggiore

Un e-commerce confronta repeat purchase a 90 giorni:

| Canale | Repeat rate |
|---|---:|
| Organic | 34% |
| Referral | 31% |
| Paid Search | 27% |
| Paid Social | 19% |

Il finding è chiaro:

> Paid Social ha la repeat rate più bassa.

Una possibile decisione immediata sarebbe tagliare il budget.

Il team segmenta però per tipo di cliente e scopre che Paid Social porta una quota molto più alta di **first-time category buyers**, che hanno retention inferiore in tutti i canali.

Dopo standardizzazione per mix, il gap si riduce fortemente.

Il finding non sparisce.

Cambia il suo significato.

Prima:

> “Paid Social acquisisce clienti peggiori.”

Dopo:

> “Una parte importante del gap di retention dipende dal mix di clienti acquisiti. La decisione sul budget deve separare channel execution, audience composition e activation post-acquisto.”

Il secondo insight apre tre alternative differenti:

```text
A — ridurre Paid Social
B — cambiare targeting
C — cambiare activation per quel mix di clienti
```

Il valore non è aver trovato una frase più sofisticata.

È aver evitato una falsa scelta binaria.

### Materialità: un pattern può essere vero e irrilevante

Supponiamo di trovare:

```text
conversion:
3,842% → 3,807%
```

Statisticamente il delta può anche essere preciso.

Ma se produce €4.000 di impatto annuo in un business da miliardi e richiede tre mesi di engineering, non è un insight prioritario.

Ogni finding dovrebbe quindi passare un **materiality check**:

```text
quanto cambia il KPI?
quanta popolazione coinvolge?
quale valore/rischio economico rappresenta?
quanto è persistente?
quanto è azionabile?
```

Materialità non significa soltanto euro.

Può includere:

- compliance;
- sicurezza;
- customer harm;
- reputazione;
- rischio operativo;
- fairness;
- strategia.

### Il decision-relevance test

Per ogni candidate insight chiediamo:

> **Se questa informazione fosse falsa, quale decisione cambierebbe?**

Se nessuna scelta cambia, potrebbe essere un finding interessante ma non decision-relevant.

Poi chiediamo:

> **Quale alternativa guadagna o perde credibilità grazie a questa evidenza?**

Se non sappiamo rispondere, siamo probabilmente ancora nella fase esplorativa.

### Un insight deve trasportare il proprio claim level

Il Capitolo 14 ha introdotto la disciplina del claim.

La stessa vale qui.

Esempio:

```text
finding:
refund rate +2,1 pp

localization:
82% del delta in due seller

hypothesis:
catalog quality deterioration

causal status:
non identificato

decision implication:
sospendere temporaneamente autopublish per quei seller e testare QC
```

Non serve trasformare l'ipotesi in causa per proporre una mitigazione reversibile.

Serve però essere chiari su ciò che sappiamo e ciò che stiamo usando come working hypothesis.

### Insight automatici: discovery, non decision authority

Strumenti moderni possono trovare automaticamente trend, anomalie e pattern.

La documentazione Power BI, per esempio, descrive funzionalità di Insights che cercano pattern nelle visualizzazioni.

Fonte: https://learn.microsoft.com/en-us/power-bi/explore-reports/end-user-insight-types

Queste funzioni aumentano la velocità di discovery.

Non risolvono automaticamente:

- materialità;
- stabilità;
- composizione;
- causalità;
- actionability;
- economics;
- alternative.

### Campo del Decision Record

Ogni insight che entra nella decisione dovrebbe essere sintetizzato così:

```text
finding:
materiality:
where concentrated:
what changed in our understanding:
claim level:
key alternative explanation:
decision implication:
```

> **L'automazione può aumentare il numero di finding. Il lavoro dell'analista è trasformare pochi finding in informazione che cambia davvero lo spazio delle scelte.**
