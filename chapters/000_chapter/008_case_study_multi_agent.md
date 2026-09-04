## 0.7 Caso end-to-end: dodici agenti, un analista, una decisione

**Caso simulato/composito.** Consideriamo una società SaaS B2B, **NovaSuite**, con circa €95 milioni di ARR.

Un lunedì mattina il CEO riceve un alert: il Net Revenue Retention enterprise è sceso dal 112% al 104%. Otto punti percentuali sono abbastanza per richiedere attenzione immediata, ma non dicono ancora che cosa sia successo. Potrebbero riflettere churn, contraction, minore expansion, un problema di misurazione o una combinazione di fenomeni diversi. La pressione organizzativa spinge verso una spiegazione rapida; il compito dell'analista è impedire che la velocità venga scambiata per evidenza.

Il responsabile analytics dispone di una squadra di agenti specializzati. Il vantaggio non sta nel chiedere a dodici agenti la stessa domanda e scegliere la risposta più convincente. Sta nel dare a ciascuno un ruolo diverso nella costruzione e nella critica dell'evidenza.

### Fase 1 — Decomporre prima di spiegare

L'analista parte dalla metrica e dalle sue possibili componenti. Prima di cercare una causa, vuole sapere se l'NRR è stato calcolato come previsto, se i dati sono sani e dove si concentra il delta.

| Agente | Mandato | Risultato iniziale |
|---|---|---|
| Metric definition | recuperare la definizione certificata di NRR | stessa base clienti, nuovi loghi esclusi |
| Data health | controllare freshness, completeness e schema | nessuna anomalia evidente |
| Reconciliation | confrontare ARR con Finance | differenza 0,4%, entro tolleranza |
| Segmentation | localizzare il delta | calo concentrato nell'enterprise europeo |
| Product usage | cercare cambiamenti di comportamento | uso di una feature premium in diminuzione |
| Support | analizzare ticket e temi | ticket performance in aumento |
| Pricing | ricostruire variazioni di listino | alcuni rinnovi europei hanno prezzi più alti |
| Release history | ricostruire i cambiamenti tecnici | release backend sei settimane prima |
| NRR decomposition | separare churn, contraction ed expansion | contraction è il contributo maggiore |
| Causal critic | contestare le prime spiegazioni | pricing e feature exposure sono confusi |
| Counterfactual search | cercare gruppi meno esposti | cluster e account con esposizione diversa |
| Executive draft | preparare una prima sintesi | propone di sospendere il nuovo listino |

La decomposizione dell'NRR cambia immediatamente la forma del problema. Dei circa otto punti percentuali persi, 2,1 arrivano dal churn, 4,7 dalla contraction e 1,2 dalla minore expansion. Il fenomeno dominante, quindi, non è «più clienti che se ne vanno», ma clienti esistenti che riducono il valore del contratto. Questa distinzione restringe lo spazio delle spiegazioni compatibili con i dati e sposta l'attenzione verso ciò che accade prima e durante i rinnovi.

### Fase 2 — Non confondere una sintesi elegante con una conclusione

L'agente incaricato dell'executive draft prova a chiudere il racconto rapidamente: «La riduzione NRR è probabilmente causata dall'aumento di prezzo europeo. Raccomandiamo di sospendere il nuovo listino». La frase è plausibile. È anche prematura.

Il responsabile analytics non la inoltra perché vede un conflitto ancora aperto fra pricing, utilizzo della feature, ticket performance e release backend. Invece di chiedere quale storia sia più intuitiva, prova a ordinarle nel tempo.

Per prima cosa verifica se l'aumento di prezzo precede davvero la contraction. Scopre che, per diversi account, la riduzione di seat o moduli compare prima del rinnovo con il nuovo listino. Questo non esclude che il pricing abbia un ruolo, ma gli impedisce di spiegare l'intero fenomeno.

Poi osserva il calo di utilizzo della feature premium. Anche qui la direzione causale non è ovvia: una feature può essere usata meno perché è diventata meno utile, ma anche perché è diventata più lenta o instabile. Serve quindi un evento precedente capace di spiegare sia l'usage sia l'aumento dei ticket.

La timeline ricostruita dagli agenti offre una sequenza coerente:

1. release backend;
2. aumento della latenza sui workload più pesanti;
3. riduzione nell'uso della feature premium;
4. aumento dei ticket performance;
5. riduzione di seat e moduli al rinnovo;
6. contraction ARR.

Questa catena non dimostra ancora causalità. Riduce però la plausibilità di una spiegazione che parta soltanto dal pricing, perché il deterioramento operativo precede diversi rinnovi e diversi cambiamenti contrattuali.

### Fase 3 — Cercare evidenze che possano smentire la storia

A questo punto il rischio è innamorarsi della nuova ipotesi tecnica con la stessa rapidità con cui l'agente si era innamorato di quella sul pricing. L'analista cerca quindi controlli che non dipendano dalla stessa storia.

La telemetria infrastrutturale mostra che la latenza p95 sui workload enterprise europei è aumentata del 38% dopo la release. È un segnale importante, ma ancora correlazionale. Il confronto con i clienti enterprise statunitensi aggiunge informazione perché gran parte di loro è servita da un cluster diverso e non mostra lo stesso aumento. La relazione diventa ancora più specifica quando gli account che usano intensamente la feature colpita mostrano contraction molto più elevato degli account meno esposti.

Infine arriva il controllo che indebolisce direttamente l'ipotesi pricing: anche clienti che non hanno ancora ricevuto il nuovo listino mostrano un calo di usage. Questa osservazione non prova che il prezzo sia irrilevante; mostra però che il deterioramento operativo esiste anche dove l'aumento di prezzo non può esserne la causa.

Le evidenze cominciano così a formare una gerarchia. Una coincidenza temporale da sola sarebbe debole. Telemetria, differenze fra cluster, intensità di esposizione e account non ancora soggetti al nuovo listino puntano nella stessa direzione seguendo percorsi diversi.

### Fase 4 — Calibrare il linguaggio alla forza dell'evidenza

Con questo insieme di segnali sarebbe facile passare da «pricing» a «release backend» e ripetere lo stesso errore, soltanto con una storia diversa. L'analista evita quindi di dire: «Abbiamo dimostrato che la release ha causato il calo di NRR». L'evidenza è osservazionale e non giustifica una certezza così forte.

La conclusione viene formulata in modo più preciso:

> “La principale ipotesi supportata dai dati è che la release backend abbia degradato le performance per workload enterprise europei, riducendo l'adozione della feature premium e contribuendo alla contraction al rinnovo. Il pricing può avere amplificato il fenomeno in alcuni account, ma non ne spiega la sequenza temporale principale.”

Questa formulazione è meno spettacolare della prima risposta automatica, ma è più utile perché separa ciò che l'evidenza sostiene con forza da ciò che resta ancora possibile.

### Fase 5 — Scegliere un'azione che produca anche nuova evidenza

Il team non effettua immediatamente un rollback globale e non annulla il listino. Entrambe sarebbero azioni ampie rispetto al livello di certezza raggiunto. Sceglie invece una mitigazione sui cluster europei e sospende ulteriori rollout, così da intervenire sul meccanismo tecnico più plausibile senza trasformare l'ipotesi in un fatto acquisito.

Per le 72 ore successive monitora latenza e usage, mentre gli account più colpiti vengono contattati per raccogliere segnali operativi aggiuntivi. Il pricing resta invariato finché il suo contributo non viene isolato meglio. La decisione è quindi mirata, osservabile e in buona parte reversibile; soprattutto, è progettata per produrre nuova informazione. Se la mitigazione riduce la latenza e l'usage torna a crescere proprio nei segmenti esposti, l'ipotesi tecnica guadagna forza. Se non accade, il team dovrà riaprire il modello causale.

È questo il passaggio che trasforma l'analisi da esercizio esplicativo a sistema decisionale: l'azione non serve soltanto a «fare qualcosa», ma a ridurre l'incertezza senza assumere più rischio del necessario.

### Che cosa ha fatto davvero l'analista?

L'analista non ha scritto personalmente tutte le query, costruito ogni grafico, letto manualmente migliaia di ticket o preparato la prima bozza del memo. Il suo contributo non si misura quindi nel volume di esecuzione manuale.

Ha definito con precisione il fenomeno da misurare e lo ha scomposto in mandati diversi. Ha separato produzione, critica e decisione, riconosciuto un conflitto fra spiegazioni e chiesto controlli indipendenti quando una storia sembrava diventare troppo convincente. Ha usato la sequenza temporale per eliminare interpretazioni incompatibili, distinto correlazione, plausibilità e causalità, calibrato il linguaggio alla forza dell'evidenza e scelto un'azione proporzionata al rischio e capace di generare nuova informazione.

Gli agenti hanno svolto gran parte dell'esecuzione. L'analista ha governato il **sistema di evidenze**.

Il contrasto più utile, alla fine, è fra due modi di rispondere al CEO. Il primo è: «L'AI dice che è il pricing». Il secondo è molto meno comodo, ma molto più professionale:

> “Il pricing è emerso come prima ipotesi, ma non regge completamente alla verifica temporale. Abbiamo evidenza più forte su una degradazione backend che precede il calo di utilizzo e la contraction. Il pattern compare nella telemetria e nei segmenti più esposti, mentre account senza nuovo listino mostrano comunque il calo di usage. Propongo una mitigazione mirata e 72 ore di monitoraggio prima di modificare il pricing.”

Entrambe le risposte possono essere state prodotte con la stessa tecnologia. Solo una dimostra leadership analitica.

> **Il valore dell'analista non sta nel numero di task che esegue personalmente. Sta nella qualità del sistema di decisione che riesce a dirigere.**
