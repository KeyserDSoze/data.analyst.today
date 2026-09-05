## 14.11 Valutare i sistemi AI: dall'impressione di qualità a un claim supportato

Quando un workflow incorpora l'AI, la frase "nelle prove sembra funzionare bene" non è un criterio di release. Un eval deve sostenere un **claim operativo specifico**. Per esempio:

> Su domande revenue nel perimetro Finance, il sistema usa la metrica certificata, rispetta la data economica, non oltrepassa i permessi e chiede escalation quando la richiesta è ambigua.

Questo claim è molto più utile di "il nostro agente SQL è accurato al 94%" perché indica quali failure mode renderebbero il sistema non idoneo.

La sequenza di design è:

```text
claim
→ failure modes
→ cases
→ ground truth
→ scoring
→ threshold / release decision
```

Per un agente analitico la suite può includere casi con due metriche Revenue di cui una legacy, `order_created_at` vs `payment_captured_at`, join many-to-many, feed D+1 immaturo, confronto osservazionale che invita a causal language, richiesta su tabella HR fuori scope e schema ambiguo che dovrebbe produrre `MUST ASK` o `STOP`.

### Preferire controlli deterministici quando possibile

Non tutto deve essere giudicato da un altro LLM. Se possiamo verificare deterministicamente che la tabella è autorizzata, la metric id è certificata, la query non contiene azioni distruttive, il grain non viola un'invariante e il risultato riconcilia entro tolleranza, usiamo quei controlli.

Una gerarchia sana può essere:

```text
1. deterministic checks
2. reference / ground-truth comparisons
3. statistical metrics
4. model-based judge per aspetti qualitativi
5. human review
```

I livelli non sono una classifica di prestigio: servono a errori diversi.

### Anche il benchmark può essere rotto

Nel luglio 2026 OpenAI ha pubblicato un audit di SWE-Bench Pro. La pipeline automatizzata ha segnalato il `27,4%` dei task come problematici, mentre la campagna di annotazione umana ne ha identificati il `34,1%`; la stima complessiva è circa il `30%` di task rotti. Tra i problemi documentati: test troppo rigidi, prompt sottospecificati, coverage insufficiente e prompt fuorvianti o in conflitto con l'aspettativa del test.

Fonte: https://openai.com/index/separating-signal-from-noise-coding-evaluations/

La lezione per l'analytics è generale: **se il gold standard è sbagliato, un punteggio perfettamente calcolato può aumentare la fiducia in una misura invalida**.

Per questo validiamo anche l'eval: il task rappresenta il lavoro reale? La distribuzione riflette frequenza o rischio? Il ground truth è affidabile? La rubric premia il comportamento desiderato? Esistono shortcut o leakage? L'ambiente di test assomiglia abbastanza al deployment? Abbiamo ispezionato manualmente sia pass sia fail?

### Il sistema testato è più del modello

Nel 2026 OpenAI ha proposto un playbook per valutazioni di terze parti che insiste su due elementi: il **claim** che l'eval vuole sostenere e l'evidenza che il risultato sia valido. Per sistemi agentici vanno descritti almeno modello, reasoning setting, tool access, harness, safeguards e budget di turn, token, tentativi, tempo e costo; vanno inoltre cercati failure come shortcut, contamination, broken problems o comportamenti che distorcono il risultato.

Fonte: https://openai.com/index/trustworthy-third-party-evaluations-foundations/

Questo è essenziale per il nostro capitolo: **model + tools + harness + budget + safeguards** è il sistema effettivamente valutato.

### LLM-as-a-judge è uno strumento, non il ground truth

Un judge model può scalare valutazioni qualitative su chiarezza, rispetto di una rubric o confronto pairwise. Ma anche il judge deve essere calibrato. Google Cloud documenta approcci che confrontano autorater con human-preference data e misurano l'allineamento con valutazioni umane.

Fonte: https://cloud.google.com/blog/products/ai-machine-learning/evaluating-large-language-models-in-business

Un pattern pratico è:

```text
human-rated sample
→ calibrate judge
→ use judge at scale
→ periodic human audit
→ recalibrate after meaningful changes
```

### Media alta, failure critico

Un'accuracy globale può nascondere casi rari ma inaccettabili. Se 990 task ordinari sono corretti al 98% e 10 task sensibili sono corretti al 50%, la media resta alta ma il sistema fallisce metà dei casi che contano di più. La suite deve quindi stratificare almeno per frequenza, severità, detectability e reversibilità, con tolleranze molto più basse per accessi non autorizzati o azioni critiche.

Dobbiamo inoltre misurare **escalation e rifiuto**, non soltanto risposta: quando il sistema chiede chiarimento, dichiara dato insufficiente, produce `PROVISIONAL`, rifiuta una richiesta fuori scope o esegue `STOP`. In alcuni task non procedere è la risposta corretta.

### Regression eval e produzione

Cambiare prompt, modello, tool, permessi, semantic model, retrieval corpus o orchestration può modificare il comportamento. Ogni cambiamento materiale dovrebbe attivare almeno smoke eval, critical regression suite, confronto con produzione e inspection dei failure cambiati prima del release.

Dopo il deploy continuiamo a misurare correction rate umano, escalation, false escalation, semantic error, authorization violations, costo per task riuscito, latency, tool call, failure severity e drift delle richieste. Gli incidenti reali diventano nuovi casi della regression suite.

Una **Eval Card** può registrare claim, release candidate, sistema testato, permission boundary, dataset/versione, risk strata, ground truth, deterministic checks, judge/calibration, human audit, critical failure tolerance, blind spot e release decision.

> **Non chiedere quanto è bravo il modello. Chiedi quale claim sul sistema vuoi autorizzare, quale evidenza lo sostiene e quali errori non sei ancora in grado di vedere.**
