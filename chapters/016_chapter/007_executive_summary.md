## 16.6 Executive summary: una vista corta del Decision Record

Un executive summary non è il riassunto abbreviato dell'analisi. È la **vista decisionale** del Decision Record: deve permettere a chi decide di capire rapidamente quale scelta è aperta, quale opzione preferiamo, quali evidenze la discriminano, quale downside può cambiarla e che cosa deve essere deciso oggi.

La regola pratica è **answer first, evidence second**. Non significa nascondere il metodo, ma spostarlo nel layer in cui serve a valutare il claim.

Una struttura robusta è:

```text
Decision requested
→ Recommendation
→ Evidence che discrimina le alternative
→ Business impact / downside
→ Uncertainty + switching value
→ Next step / owner
```

### Dal record alla pagina executive

Supponiamo che il Decision Record confronti rollout generalizzato, rollout selettivo e ulteriore pilot. Analytics raccomanda il rollout selettivo perché l'uplift è concentrato su due segmenti; il downside principale è il support load e sopra **+11% di ticket** la preferenza cambia; il decision owner è il VP Product.

La pagina executive può comprimere tutto questo senza cambiare semantica:

> **Decisione richiesta:** approvare rollout al 40% sui segmenti A e B.  
> **Perché:** l'uplift è positivo nei segmenti target e il valore resta favorevole negli scenari rilevanti.  
> **Rischio:** il support load è il guardrail più fragile; sopra +11% cambieremmo scelta.  
> **Proposta:** rollout graduale con review tra due settimane e stop sulla soglia concordata.

La sintesi non inventa una nuova storia. Conserva decisione, evidenza, downside e condizione di revisione.

### Caso simulato/composito — Da 18 slide a una decisione leggibile

Un marketplace fashion analizza l'aumento dei resi. L'analyst prepara 18 slide su categorie, seller, sizing, paese, device e tenure. Il COO interrompe con la domanda più importante: **“Quale decisione devo prendere?”**

La prima pagina viene ricostruita intorno alla scelta. Il return rate è aumentato di **2,1 punti percentuali** e l'**81% del delta** è concentrato in tre seller e due categorie. Nei seller interessati cresce la quota di articoli con sizing inconsistente dopo un onboarding catalogo accelerato; il costo incrementale trimestrale tra reverse logistics e refund handling è circa **€640k**. La concentrazione è robusta, ma il ruolo causale della nuova procedura non è ancora isolato.

La recommendation diventa quindi: sospendere temporaneamente l'autopublish per i seller ad alto rischio e finanziare quattro settimane di quality control, con guardrail su time-to-publish e seller activation. Le altre slide non spariscono: diventano evidence layer e appendix.

## Tre profondità, una sola semantica

Il decision layer da 30 secondi contiene ask, recommendation, ragione e caveat. L'evidence layer da 5–10 minuti contiene i visual che discriminano le alternative, più scenario, switching value e guardrail. Il provenance layer conserva definizioni, query, metodi, robustness check, segmenti e assunzioni.

La qualità della Pack dipende dal fatto che questi tre layer non producano tre narrative incompatibili. Se la pagina executive dice “causa” e l'appendix dice “associazione”, la sintesi ha fallito.

## Titoli conclusivi, ma claim-safe

“Revenue by region” descrive il contenuto ma non aiuta la decisione. “La Germania spiega il 64% del gap revenue europeo” dichiara un finding verificabile. “La Germania causa il calo europeo” è invece un claim più forte della decomposition geografica.

Il titolo può quindi essere assertivo quando completa una frase supportata dall'evidenza. Non può usare la brevità per salire di livello epistemico.

Un buon **headline test** verifica quattro cose: se il destinatario leggesse soltanto il titolo, riceverebbe il claim corretto? capirebbe se è descrittivo, predittivo o causale? vedrebbe il caveat principale se può cambiare la scelta? saprebbe quale decisione gli viene chiesta?

## La recommendation non deve cancellare le alternative

Una pagina executive non deve mostrare una longlist completa, ma quando il trade-off è materiale almeno l'alternativa più credibile deve restare visibile. Altrimenti la comunicazione diventa advocacy: il lettore vede soltanto l'opzione preferita e perde il confronto che le ha dato valore nel Capitolo 15.

> **Un executive summary riuscito non racconta tutto. Conserva però tutte le informazioni che potrebbero rendere diversa la decisione.**
