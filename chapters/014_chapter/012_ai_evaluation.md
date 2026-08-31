# 14.11 Valutare i sistemi AI: non basta dire “sembra funzionare”

Quando un workflow analitico incorpora l'AI, serve una disciplina di evaluation simile a quella che useremmo per un modello, una pipeline o un esperimento.

Un assistente che genera SQL può sembrare molto bravo durante una demo e fallire proprio sui casi che contano di più: join many-to-many, filtri temporali, metriche con definizioni ambigue, edge case di null e cancellazioni.

## Dalla demo all'eval set

Costruiamo un insieme di casi realistici:

- domande semplici;
- domande ambigue;
- metriche con definizioni certificate;
- casi con dati mancanti;
- richieste che richiedono rifiuto o escalation;
- casi rari ma ad alto costo se sbagliati.

Per ciascun caso definiamo cosa significa successo.

Esempio per un agente SQL:

| Caso | Criterio di successo |
|---|---|
| revenue mensile | usa la metrica certificata e la data corretta |
| customer count | non duplica clienti dopo join |
| churn | rispetta la definizione ufficiale e la finestra temporale |
| richiesta non autorizzata | non accede al dataset sensibile |
| schema ambiguo | chiede chiarimento o esplicita l'assunzione |

## Caso pubblico: perché anche gli eval possono mentire

Nel 2026 OpenAI ha pubblicato un audit di SWE-Bench Pro mostrando che una quota rilevante dei task presentava problemi di costruzione o scoring. Il punto generale va oltre il coding: se il test è rotto, anche un punteggio preciso misura la cosa sbagliata.

Un eval deve quindi essere valutato a sua volta.

Domande utili:

- il task rappresenta davvero il lavoro reale?
- la rubric premia ciò che ci interessa?
- ci sono scorciatoie che il sistema può sfruttare?
- il ground truth è affidabile?
- il setup è cambiato tra una versione e l'altra?
- abbiamo revisionato manualmente un campione di successi e fallimenti?

OpenAI raccomanda di esplicitare quale claim un'evaluation intende supportare e di mostrare evidenze sulla validità del risultato. Anche Google Cloud suggerisce di confrontare judge model e valutazioni umane, usando human ratings come ground truth quando si calibra un valutatore automatico.

## AI che valuta AI

Possiamo usare un secondo modello per giudicare il primo. È utile per scalare, ma non elimina la necessità di controllo umano.

Una struttura robusta può essere:

1. test deterministici dove possibile;
2. metriche automatiche;
3. LLM-as-a-judge per aspetti qualitativi;
4. audit umano su campioni;
5. review umana obbligatoria sui casi ad alto rischio.

## Il vero KPI

L'obiettivo non è massimizzare un benchmark astratto. È ridurre errori reali nel workflow.

Per un agente analitico possiamo misurare:

- percentuale di query semanticamente corrette;
- percentuale di escalation corrette;
- errori di autorizzazione;
- precisione delle metriche;
- tempo risparmiato;
- costo per task valido;
- tasso di correzione umana;
- severità degli errori non intercettati.

**Un sistema AI non è affidabile perché ha prodotto cento risposte convincenti. È affidabile quando sappiamo in quali condizioni funziona, in quali fallisce e come intercettiamo quei fallimenti.**

### Fonti

- OpenAI, *A shared playbook for trustworthy third party evaluations*: https://openai.com/index/trustworthy-third-party-evaluations-foundations/
- OpenAI, *Separating signal from noise in coding evaluations*: https://openai.com/index/separating-signal-from-noise-coding-evaluations/
- Google Cloud, judge model evaluation: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models/evaluate-judge-model
