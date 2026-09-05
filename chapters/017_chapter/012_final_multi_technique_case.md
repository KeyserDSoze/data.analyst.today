## 17.11 OrbisMarket — “La crescita è sana?”

> **Caso simulato/composito.** Organizzazione, numeri e sequenza sono costruiti per la didattica.

OrbisMarket è un marketplace europeo con circa **9 milioni di ordini annui**. Nel Q3 il board vede GMV **+7%**, net revenue **+4%**, contribution margin **-13%**, repeat purchase **-3,4 pp**, delivery complaints **+22%**, nuovi seller **+31%** e marketing spend **+18%**.

Questa volta la domanda è volutamente larga:

> **La crescita è sana, e cosa dobbiamo cambiare prima del prossimo trimestre?**

È il caso più lungo del capitolo, ma non perché dobbiamo usare “tutto il libro”. È lungo perché la decisione contiene **più rischi indipendenti**: potremmo tagliare crescita sana, continuare a scalare un meccanismo economicamente distruttivo, investire milioni nella leva sbagliata o correggere una metrica senza correggere il processo che la genera.

Il Capstone Routing Canvas fissa quindi due tempi: una triage in **72 ore** e una decisione board in **10 giorni**. Il claim iniziale può essere diagnostico; un claim causale diventerà necessario soltanto se una leva costosa dipende da una relazione che la sola decomposition non può sostenere.

### Prima escalation: il -13% non ha ancora diritto di governare la decisione

Il primo lavoro non è capire *perché* il margine scenda. È dimostrare che il confronto significhi la stessa cosa nei due trimestri. Finance e Analytics riconciliano definizione e periodo, grain ordine/riga/spedizione, refund/cancellation timing, event date vs accounting date, nuovi seller fee, carrier surcharge e trattamento del marketing cost.

Emerge un cambio nel timing di contabilizzazione di alcuni refund. Circa **1,5 pp** del deterioramento apparente derivano da comparabilità contabile, non da peggioramento economico corrente.

Il problema resta reale, ma la prima stop rule scatta correttamente:

> **Nessun piano di taglio o investimento viene approvato usando il -13% grezzo.**

Qui l'Analytical Data Contract e la Data Readiness Review hanno già creato valore materiale. Non hanno spiegato il business; hanno impedito che il board agisse su una misura non ancora comparabile.

### Seconda escalation: la decomposition elimina alcune storie e ne concentra altre

Sul delta residuo il team costruisce un contribution-margin bridge: product margin, discount, shipping subsidy, refund, payment cost, support cost, seller incentive e marketing acquisition cost dove rilevante.

I driver principali sono **shipping subsidy, refund e mix verso seller/categorie con cost-to-serve più alto**. Gli sconti contribuiscono, ma non dominano. Questo basta per ridurre la credibilità della prima risposta commerciale “tagliamo le promozioni”.

L'EDA Evidence Map localizza poi il deterioramento nei **nuovi clienti degli ultimi tre mesi**, negli **ordini bulky**, in **due aree metropolitane** e nei seller entrati dopo una recente espansione del catalogo. Le nuove coorti hanno repeat rate inferiore e, nello stesso tempo, delivery service peggiore.

A questo punto due spiegazioni che sembravano concorrenti — “marketing porta clienti peggiori” e “la logistica sta peggiorando” — possono essere parti dello stesso processo. Customer mix e service quality non sono necessariamente indipendenti.

### Terza escalation: il lifecycle mostra dove la relazione diventa decision-critical

Il Lifecycle Diagnostic Map segue ordine → spedizione → consegna → complaint/refund → secondo acquisto. La retention a 60 giorni è molto peggiore tra clienti la cui prima consegna arriva oltre la promessa.

Questo è un finding forte e ancora osservazionale. Gli ordini tardivi possono differire per categorie, seller, customer mix, peso e promise date. Se la decisione fosse soltanto “dove investigare”, potremmo fermarci qui.

Operations, però, propone un investimento di milioni in capacità e routing. Il failure cost cambia: ora la decisione richiede sapere se migliorare delivery reliability **può plausibilmente cambiare anche repeat purchase ed economics**. È questo nuovo claim — non il desiderio di usare causal inference — che attiva il Causal Identification Brief.

Una modifica al consolidamento degli ordini è stata introdotta gradualmente in alcuni hub ma non in altri. Il team controlla pre-trend, composizione, timing, cambi concorrenti, spillover, exposure e robustness. Il quasi-esperimento sostiene un effetto negativo di circa **+0,8 giorni di delivery time** sugli ordini bulky più esposti e **-2,1 pp di repeat purchase a 60 giorni** nel segmento più esposto.

Il claim resta circoscritto:

> **Il disegno quasi-sperimentale sostiene un effetto materialmente negativo del nuovo consolidamento su delivery time e repeat purchase nel segmento più esposto, con limiti di identificazione residui.**

Non abbiamo “dimostrato che la logistica causa tutto il churn”. Abbiamo guadagnato abbastanza evidenza per trattare una leva operativa costosa come plausibilmente value-creating.

### Quarta escalation: causalità non dice quanta capacità comprare

Operations propone “aggiungiamo capacità ovunque”. Il causal finding non risponde a **quanto, dove e quando**. Questa nuova domanda giustifica il Temporal Decision Brief.

Il forecast mostra picchi concentrati in finestre e hub specifici. Capacità fissa generalizzata costa circa **€6,8M annui**; una combinazione di capacità flessibile, routing alternativo, volume threshold e promise date più realistiche ha un costo atteso molto inferiore.

Il forecast non viene usato perché il caso “contiene una serie temporale”. Entra perché la decisione è diventata una capacity allocation sotto uncertainty.

### Quinta escalation: una leva plausibile deve diventare una policy testabile

Il team identifica due interventi reversibili: un **surcharge selettivo** sugli ordini bulky sotto una soglia economica e una combinazione **promise date realistica + routing alternativo** sugli ordini ad alto rischio di ritardo.

Ora l'Experiment Contract ha un compito distinto dal quasi-esperimento precedente. Non deve spiegare retrospettivamente il consolidamento; deve scegliere una policy futura. Il primary outcome è **contribution margin per visitatore**, con guardrail su checkout conversion, cancellation, delivery time, refund, repeat purchase e customer complaints.

Nel caso simulato la seconda variante riduce leggermente la conversione iniziale ma migliora delivery reliability e valore atteso per cliente. È il tipo di trade-off che un funnel locale potrebbe giudicare “perdita” mentre il sistema complessivo considera miglioramento.

### Solo ora le alternative sono abbastanza caratterizzate

Il Decision Record confronta:

| Opzione | Costo annuo stimato | Effetto atteso | Reversibilità | Rischio principale |
|---|---:|---|---|---|
| Capacità fissa generalizzata | €6,8M | alta protezione picchi | bassa | overcapacity |
| Capacità flessibile + routing | €2,9M | effetto mirato | medio-alta | execution complexity |
| Solo surcharge | €0,4M | protegge margine | alta | conversion/customer perception |
| Status quo | ~€0 diretto | nessuna correzione | alta | deterioramento continua |

La recommendation è un pacchetto mirato: capacità flessibile e routing nei nodi esposti, promise date più realistica, surcharge soltanto dove l'economia lo giustifica, stop condition su conversion/complaints e monitoraggio di repeat purchase e contribution margin.

Non è la soluzione più semplice da raccontare. È quella che meglio rispetta **dove** il problema è stato identificato e **quanto** rischio siamo disposti a comprare.

### Evidence Ledger prima del board

| Observed | Inferred / identified under assumptions | Still unknown |
|---|---|---|
| GMV +7%, net rev +4%, CM grezzo -13% | ~1,5 pp del deterioration è comparability accounting | mix Q4 futuro |
| shipping subsidy/refund/cost-to-serve dominano residuo | consolidamento ha effetto negativo locale su delivery | piena generalizzabilità oltre hub/segmento |
| problema concentrato in bulky, nuove coorti, 2 metro | delivery deterioration contribuisce al repeat decline nel segmento esposto | risposta di lungo periodo dei customer |
| quasi-experiment: +0,8d delivery, -2,1pp D60 repeat | capacity/routing mirato è più coerente della capacità universale | costo flessibile in scenari estremi |
| test: B migliora reliability/value, con lieve conversion loss | | |

La prima pagina del board non elenca le tecniche. Dice:

> **Dopo aver corretto un effetto contabile, il deterioramento del margine è concentrato negli ordini bulky e nelle nuove coorti di due aree. L'evidenza più forte collega una parte materiale del problema al nuovo consolidamento logistico. Un intervento mirato su routing, capacità flessibile e promise date ha rapporto impatto/costo migliore della capacità generalizzata.**

La evidence hierarchy rende recuperabili margin bridge, concentration map, lifecycle evidence, quasi-experimental estimate con caveat, capacity scenarios, experiment result e option economics. La decisione richiesta è approvare rollout progressivo del pacchetto mirato e **non** l'espansione fissa generalizzata.

Le switching condition restano esplicite: rivalutare se l'effetto operativo non si replica, i costi flessibili superano soglia, repeat purchase non migliora, la conversion loss da surcharge supera il beneficio o il mix Q4 cambia sostanzialmente.

### Outcome review: un buon finale non rende inevitabile il percorso

Dopo otto settimane on-time delivery migliora di **6,7 pp**, contribution margin bulky di **3,2 pp**, support contacts scendono dell'**11%**, repeat purchase nel segmento target aumenta di **1,5 pp** e checkout conversion peggiora di **0,3 pp**.

Il pacchetto non ottimizza ogni metrica. Migliora il trade-off che il Decision Record aveva definito importante.

Il risultato positivo, però, non riscrive la storia come se ogni passaggio fosse stato ovvio. La decision review separa ancora qualità del ragionamento ex ante, execution fidelity e outcome luck: quali alternative erano note, quali assunzioni erano fragili, quali meccanismi si sono mossi come previsto e quali prior vanno aggiornate.

### Perché questo caso è lungo e gli altri no

OrbisMarket ha usato Analytical Brief, Analytical Data Contract, Data Readiness Review, EDA Evidence Map, Lifecycle Diagnostic Map, Causal Identification Brief, Temporal Decision Brief, Experiment Contract, Uncertainty Brief, Decision Record e Decision Communication Pack. Non ha usato Predictive Decision Card, Tooling Decision Record, Data Flow Architecture Map o AI Analysis Control Sheet.

La lunghezza non dimostra maggiore maturità. È il risultato di una sequenza in cui **ogni nuova evidenza apriva un nuovo rischio decisionale indipendente**:

```text
metric comparability
→ residual driver
→ lifecycle relation
→ causal lever
→ capacity requirement
→ future policy
→ economics / decision
```

Se uno di questi rischi non fosse esistito, il metodo corrispondente avrebbe dovuto essere eliminato.

Il ponte al Capitolo 18 nasce esattamente qui. Se OrbisMarket dovesse rifare ogni settimana margin reconciliation, bulky-risk monitoring, capacity scenario e rollout guardrail, questa catena non potrebbe restare una sequenza di analisi ad hoc. Dovrebbe diventare un **servizio analitico operato nel tempo**, con owner, SLO, change policy e incident process.

> **La maturità analitica non appare quando riusciamo a usare molte tecniche. Appare quando ciascuna tecnica entra perché chiude un rischio preciso, e quando sappiamo che la stessa capacità — se diventa ricorrente — dovrà essere trasformata da progetto in sistema.**
