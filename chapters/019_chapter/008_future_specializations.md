## 19.7 Specializzazioni future: scegliere problemi che sopravvivono ai tool

Provare a indovinare i job title del 2035 ha poco valore. I nomi cambiano rapidamente e descrivono responsabilità diverse tra aziende. È più robusto chiedere quali **classi di problema** continueranno a essere abbastanza costose, ambigue e rischiose da richiedere profondità e judgment anche quando una parte crescente dell'esecuzione sarà automatizzata.

Una specializzazione utile può essere pensata come l'intersezione tra **problema/domain × metodo × operating responsibility**. In questa prospettiva, le direzioni interessanti non sono previsioni di titoli: sono territori in cui possiamo accumulare capitale professionale.

| Classe di problema | Domanda che deve restare governata | Capacità che acquistano valore |
|---|---|---|
| Measurement e semantic systems | persone e agenti stanno parlando dello stesso fenomeno? | metric definition, entity/grain, semantic layer, measurement change, lineage, contract, certification/deprecation |
| Experimentation e causal decisioning | quale cambiamento produce davvero un effetto, per chi e sotto quali condizioni? | experiment design, causal inference, heterogeneity, interference, guardrail, incremental value, rollout |
| Revenue, pricing e growth economics | quale leva crea valore incrementale invece di spostare credito tra metriche? | pricing, elasticity, incrementality, retention economics, unit economics, scenario e threshold |
| Operational decision analytics | come trasformiamo incertezza in staffing, inventory, routing, capacity o risk policy? | forecasting, asymmetric loss, service level, scenario planning, optimization literacy, feedback loop |
| Analytics reliability e decision infrastructure | come resta affidabile una decisione ricorrente quando crescono consumer e automazione? | SLO, ownership, testing, observability, incident/recovery, change, cost-to-serve, adoption, retirement |
| AI/agent evaluation analytics | il sistema automatico sta creando valore affidabile o soltanto activity? | eval design, severity-weighted error, human correction, escalation/abstention, cost per accepted outcome, observability, authority evaluation |
| Domain decision specialization | quali meccanismi del settore cambiano davvero economia e rischio? | domain depth + analytical breadth + decision ownership |

Queste aree non sono compartimenti stagni. Measurement e semantic systems, per esempio, attraversano Analytics Engineering e Governance; operational analytics può richiedere forecasting e optimization specialistica; experimentation può incontrare product analytics, causal inference e economics. Il punto non è trovare un'etichetta perfetta, ma costruire depth attorno a un problema reale.

L'area AI/agent evaluation rende particolarmente visibile questa logica. Immaginiamo un'azienda in cui un agente prepara la prima bozza delle analisi settimanali. Dopo due mesi il `92%` dei report viene generato automaticamente. Come metrica di automazione sembra un successo. Ma il team scopre che il `31%` richiede correzioni sostanziali, il `14%` contiene almeno un problema semantico, il tempo di review è aumentato e i junior tendono ad accettare output senza escalation più spesso dei senior.

Il KPI ha misurato **activity**, non qualità del servizio. La domanda professionale diventa quindi come costruire una scorecard che osservi task success con criteri verificabili, first-pass acceptance, severity-weighted error, human correction time, escalation appropriata, cost per accepted output, downstream incident e decision impact. È un problema sufficientemente ricco da richiedere metodo, dominio operativo e ownership anche se nessun mercato del lavoro userà mai il titolo “Agent Analytics Analyst”.

Lo stesso vale per le specializzazioni di dominio. Payments risk, healthcare operations, supply chain, insurance pricing, marketplace economics, subscription growth o energy planning restano interessanti quando combinano domain depth, analytical breadth e decision ownership. Il vantaggio non nasce dal conoscere più schermate di un software, ma dal riconoscere failure mode e meccanismi che un sistema generalista vede soltanto come correlazioni.

Per scegliere dove approfondire, quindi, non serve inseguire ciò che appare più futuristico. Conviene cercare un problema ricorrente e costoso, con assunzioni non banali, abbastanza profondità da richiedere studio serio, un dominio in cui accumulare contesto, responsabilità che possa crescere e feedback reale sugli outcome. Una specializzazione così costruita è più resistente del badge su uno strumento.

La contrapposizione tra generalista e specialista diventa meno utile. Un profilo forte può essere generalista nel routing dei problemi, specialista in una o due aree ad alto valore, competente nel dominio e abbastanza maturo da coinvolgere specialisti più profondi quando il failure cost lo richiede.

Il *Future of Jobs Report 2025* segnala contemporaneamente crescita delle competenze AI/big data e persistenza dell'analytical thinking tra le core skill. Non ci dice quali titoli esisteranno nel 2035, ma rende poco credibile l'idea che tecnologia e capacità analitica si muovano in direzioni opposte.

Fonte: https://www.weforum.org/publications/the-future-of-jobs-report-2025/

> **Non specializzarti nel nome del tool. Specializzati in un problema abbastanza importante da sopravvivere a più generazioni di tool.**