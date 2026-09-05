## 17.1 Orion Living — “Le vendite stanno scendendo”

> **Caso simulato/composito.** Organizzazione, numeri e sequenza sono costruiti per la didattica.

Orion Living, catena retail multicanale, chiude il mese con un alert: **-11,2% YoY**. Il CEO chiede se sia un problema di domanda, prezzo o execution e il management sta già valutando promozioni per recuperare volume. Il failure cost principale è quindi immediato: se la spiegazione è sbagliata, l'azienda può spendere milioni in sconti, comprimere ulteriormente il margine e lasciare intatto il vero problema.

Per la decisione delle prossime 72 ore non serve ancora identificare causalmente ogni determinante delle vendite. Serve capire se l'evidenza giustifica una promozione generalizzata oppure indica che il valore si sta perdendo altrove. La prima stop rule è perciò semplice: **nessuna azione commerciale finché il -11,2% non è semanticamente e contabilmente riconciliato**.

### Il primo routing cambia su una parola: “vendite”

Il board usa “vendite” come se fosse una metrica univoca. Il controllo iniziale mostra invece che il -11,2% riguarda **net sales**, non ordini né gross sales. Questa distinzione cambia il percorso prima ancora di aprire un modello.

L'Analytical Brief minimale fissa quindi net sales come metrica decisionale, popolazione di ordini consumer completati e confronto YoY da rendere omogeneo. Poi il team costruisce una bridge tra ciò che accade prima dell'ordine e ciò che accade dopo:

| Componente | Variazione |
|---|---:|
| Sessioni | -2,1% |
| Conversione | -0,4 pp |
| Unità per ordine | quasi stabile |
| Prezzo medio | +3,8% |
| Return rate osservato | 7,4% → 10,9% |

La narrativa “la domanda è crollata” perde rapidamente forza. Traffico e conversione peggiorano, ma la parte più anomala del gap emerge dopo l'acquisto. Questa decomposition è già decision-relevant: rende meno plausibile che uno sconto generalizzato sia la prima leva da usare.

Il team approfondisce la concentrazione. Net sales scendono del **3,1%** negli store, del **5,4%** sul web desktop e del **24,8%** sulla mobile app. Il deterioramento è inoltre forte nell'arredo voluminoso, su iOS e in tre mercati che spiegano circa il **64% del delta**. A questo punto la release iOS diventa una working hypothesis naturale, ma l'Evidence Ledger la mantiene nella colonna **Inferred**, non in Observed.

### La readiness cambia di nuovo la storia

Prima di collegare il fenomeno a release o logistica, il team verifica event completeness, definizione del return rate, date di ordine/consegna/reso, versioni app realmente esposte, policy di reso, refund recognition e product mix.

Qui emerge il secondo cambio di routing: nello stesso periodo la finestra di reso è passata da **30 a 45 giorni in due mercati**. Il return rate `7,4% → 10,9%` è quindi un confronto tra processi commerciali non completamente omogenei. Il +3,5 pp osservato non ha il diritto di diventare automaticamente “deterioramento operativo”.

Dopo aver standardizzato il mix prodotto e confrontato finestre di reso omogenee, l'aumento comparabile scende a circa **+1,4 pp**. Il residuo è molto più informativo: circa **0,8 pp** sono concentrati sugli ordini bulky, circa **0,4 pp** sugli utenti esposti alla nuova esperienza iOS, con una quota diffusa restante.

Nel bulky il lead time medio aumenta di **1,7 giorni**, i resi per prodotto danneggiato crescono fortemente e tre carrier spiegano gran parte del deterioramento. I mercati più colpiti coincidono inoltre con quelli in cui è cambiato il network di consegna. Questi fatti rendono più credibile un problema operativo localizzato. Non autorizzano però ancora la frase “la logistica ha causato il -11,2%” né trasformano l'associazione iOS in treatment effect.

### La prima decisione può chiudersi prima della causalità globale

La domanda urgente era se stimolare domanda con sconti generalizzati. Per questa scelta l'evidenza è già sufficiente. Sappiamo che la domanda aggregata non spiega la maggioranza del gap; una quota materiale del problema nasce dopo l'ordine; il deterioramento residuo è fortemente concentrato in flussi operativi specifici; una promozione generalizzata agirebbe poco su quei driver e ridurrebbe il margine.

Il Decision Record confronta quindi tre opzioni. **A — sconto generalizzato** può aiutare conversione ma interviene male sui resi e comprime il margine. **B — nessuna azione** evita costi immediati ma lascia proseguire danni e ritardi. **C — intervento mirato** combina audit dei carrier bulky nei tre mercati critici, test su packaging/carrier, monitoraggio separato di gross sales/returns/net sales e una verifica controllata della componente iOS sospetta.

La scelta è **C**. Non perché il team abbia dimostrato una causa unica, ma perché C è robusta alle spiegazioni ancora plausibili e mantiene alto il valore informativo delle azioni successive.

Per il sotto-problema iOS la stop rule è diversa. Se il costo di rollback è materiale, la semplice associazione non basta: serve ricostruire esposizione, comparabilità ed eventualmente attivare un Causal Identification Brief o un confronto sperimentale. Il capstone, quindi, non termina tutte le domande allo stesso livello.

### Evidence Ledger al momento della decisione

| Observed | Inferred | Still unknown |
|---|---|---|
| net sales -11,2% YoY | execution pesa più della domanda nel residuo | effetto causale della release iOS |
| sessioni -2,1%, conversion -0,4 pp | network bulky plausibilmente contribuisce al deterioramento | quota causale precisa dei carrier |
| policy reso 30→45 giorni in 2 mercati | sconto generalizzato è poco allineato ai driver | risposta di conversion a eventuale promo |
| return-rate comparabile circa +1,4 pp | | |
| bulky: lead time +1,7 giorni, damage returns in aumento | | |

La Decision Communication Pack può quindi usare una headline calibrata:

> **Il gap di net sales non è principalmente un calo generalizzato della domanda. Dopo aver corretto policy di reso e mix, il deterioramento residuo è concentrato negli ordini bulky e in una parte del rollout iOS. Non raccomandiamo sconti generalizzati; proponiamo interventi mirati su carrier, packaging e verifica del rollout.**

L'outcome review misura return rate bulky, damage-related returns, lead time, net sales per session, conversion iOS, complaints e contribution margin. Il team non costruisce churn model, MMM, forecast complesso o un modello causale globale delle vendite: nessuno di questi oggetti è necessario per chiudere la prima decisione.

**Percorso minimo effettivo:** Analytical Brief → Data Readiness Review → EDA Evidence Map → Decision Record → Decision Communication Pack. Il Causal Identification Brief resta condizionale sul solo sotto-problema iOS.

> **Il valore del capstone non è arrivare alla causa più sofisticata. È sapere quando una diagnosi sufficientemente affidabile ha già eliminato l'azione sbagliata.**
