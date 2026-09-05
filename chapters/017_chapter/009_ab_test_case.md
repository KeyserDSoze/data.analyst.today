## 17.8 VelaPay — “Il test è positivo: possiamo fare rollout?”

> **Caso simulato/composito**, con un caso Microsoft reale documentato sul Sample Ratio Mismatch.

VelaPay testa un checkout semplificato. Dopo 14 giorni il controllo converte al **71,4%**, la variante al **72,3%**: uplift assoluto **+0,9 pp**, `p = 0,018`. In Slack arriva la frase prevedibile: “Test vinto. Rollout?”.

Il capstone deve resistere proprio a questa compressione. Il test può aver prodotto un numero statisticamente significativo e non avere ancora **autorità decisionale**. Prima di chiedere se B vince, dobbiamo sapere se il confronto è credibile e se il beneficio supera i danni collaterali.

### Il risultato più importante del primo test è `BLOCKED`

L'Experiment Contract originale rende verificabili primary metric, unità di randomizzazione, split atteso, MDE, durata, guardrail, criteri di esclusione, segment analysis e rollout policy. Ed è proprio confrontando l'esecuzione con quel contratto che emergono segnali contrari alla narrativa “test vinto”.

Payment authorization è stabile, ma chargeback passa da **0,42% a 0,57%**, i support contacts crescono del **6%** e Android low-end mostra conversion **-1,8 pp**. Soprattutto compare un'anomalia di allocazione/telemetria collegata a una versione obsoleta dell'SDK e lo split presenta un **Sample Ratio Mismatch** statisticamente chiaro.

Un SRM non è un caveat da scrivere sotto il p-value. È un trust gate.

Microsoft Research documenta gli SRM come sintomo di problemi che possono nascere in assignment, execution, logging, join o analysis e raccomanda di diagnosticarli prima di usare il risultato per una decisione.[^ms-srm-paper] In un caso pubblico su un image carousel MSN, una variante sembrava ridurre engagement; il test aveva però un SRM e l'indagine mostrò che il bot detection filtrava in modo sproporzionato utenti molto coinvolti nella variante. Dopo la correzione, la direzione apparente del risultato si invertì.[^ms-srm-case]

La lezione per VelaPay è netta: **un p-value non ripara un confronto la cui comparabilità può essere compromessa**.

Il team distingue quindi assignment, exposure logging, event loss e treatment effect. Finché non sa quale dei primi tre ha generato il mismatch, lo stato corretto è:

```text
EXPERIMENT STATUS: BLOCKED
rollout authority: NONE
```

Questo è il finale professionale della prima fase. Non “positive with caveats”, non “rollout prudente”: **BLOCKED**.

### Ripristinare la fiducia richiede nuova evidenza, non una spiegazione convincente

La root cause viene ricondotta all'SDK obsoleto. Dopo la correzione VelaPay esegue una nuova fase limitata invece di reinterpretare retroattivamente il test originale. Il nuovo risultato mostra uplift più piccolo, intervallo compatibile con beneficio moderato, nessun peggioramento materialmente rilevante dei chargeback, Android low-end stabile e support contacts entro guardrail.

Ora la conversazione può spostarsi dall'integrità all'economia. La conversione da sola non è l'outcome decisionale: il team usa **incremental gross profit per 1.000 checkout**, includendo conversione aggiuntiva, fee, chargeback, support cost e refund/fraud effect rilevanti.

Anche il precedente segnale Android viene trattato con disciplina. È decision-critical perché il segmento è grande e il downside plausibile, ma non autorizza una ricerca libera di decine di sottogruppi. I segmenti pre-specificati e quelli operativamente critici vengono distinti dalle analisi esplorative; una policy permanente richiede conferma separata.

A questo punto lo stato cambia davvero:

```text
EXPERIMENT STATUS: APPROVED FOR RAMP
```

La differenza tra i due stati non è retorica. Prima mancava il diritto di interpretare il comparison; dopo abbiamo un confronto credibile e un profilo benefit/guardrail accettabile.

### Dal test alla policy di rollout

Restano tre alternative. Un rollout immediato al 100% massimizza velocità ma anche blast radius. Nessun rollout ignora evidenza utile ormai ripristinata. VelaPay sceglie un ramp progressivo:

1. **10%** degli utenti e osservazione per **72 ore**;
2. **50%** se chargeback, latency e support restano entro soglia;
3. **100%** soltanto se primary metric e guardrail rimangono coerenti;
4. rollback se una stop condition viene superata.

L'esperimento produce quindi una causal estimate; il Decision Record la trasforma in una **policy reversibile**.

### Evidence Ledger

| Observed | Inferred | Still unknown |
|---|---|---|
| primo test +0,9 pp, p=0,018 | il primo uplift non è decision-authoritative | effetto stabile al 100% rollout |
| SRM + SDK anomaly | comparabilità del primo test compromessa | novelty/decay di lungo periodo |
| primo chargeback 0,42→0,57%; contacts +6% | | |
| dopo fix: uplift moderato, guardrail stabili | ramp controllato è proporzionato al rischio | |

La headline executive deve conservare questa storia di fiducia ripristinata:

> **Il primo test mostrava uplift ma non era affidabile a causa di un problema di allocazione. Dopo la correzione, il beneficio resta positivo e i guardrail sono stabili. Raccomandiamo ramp 10% → 50% → 100% con rollback sulle soglie concordate.**

Dopo il rollout si monitorano conversione, gross profit per 1.000 checkout, chargeback, support contacts, latency/crash, device critici e novelty/decay.

**Percorso effettivo:** Experiment Contract → trust checks → **BLOCKED** → correzione + nuova evidenza → Uncertainty Brief → Decision Record → Decision Communication Pack → ramp gate → outcome review.

> **Il caso non insegna che un A/B test produce una decisione. Insegna che la prima decisione può essere rifiutarsi di usare un risultato finché il sistema non ha riguadagnato il diritto di fidarsi del confronto.**

[^ms-srm-paper]: Microsoft Research, *Diagnosing Sample Ratio Mismatch in Online Controlled Experiments: A Taxonomy and Rules of Thumb for Practitioners*, https://www.microsoft.com/en-us/research/publication/diagnosing-sample-ratio-mismatch-in-online-controlled-experiments-a-taxonomy-and-rules-of-thumb-for-practitioners/
[^ms-srm-case]: Microsoft Research, *Diagnosing Sample Ratio Mismatch in A/B testing*, https://www.microsoft.com/en-us/research/articles/diagnosing-sample-ratio-mismatch-in-a-b-testing/
