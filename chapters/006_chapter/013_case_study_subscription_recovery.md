## 6.12 Caso end-to-end: costruire una Lifecycle Diagnostic Map

Segmenti, coorti, funnel, activation, survival, reactivation, economics e risk score diventano pericolosi quando finiscono in dashboard separate e ognuno produce una storia propria. Il loro valore emerge quando convergono in una stessa diagnosi.

La **Lifecycle Diagnostic Map** serve proprio a questo: seguire la catena **chi → quando → dove → primo valore → persistenza → valore economico → rischio → actionability → prossimo metodo**.

### OpsPilot: “trovate i clienti a rischio” è una richiesta troppo avanti nel processo

**OpsPilot** è una piattaforma B2B in abbonamento. In due trimestri la Gross Revenue Retention scende dal **93,8% al 90,9%**. Il CEO chiede di identificare i clienti a rischio e salvarli prima che sia troppo tardi.

La richiesta sembra già pronta per un churn model. Il team sceglie invece di ricostruire prima il lifecycle.

La perdita non è uniforme:

| Segmento | GRR precedente | GRR attuale |
| --- | ---: | ---: |
| Enterprise | 95,1% | 94,4% |
| Mid-market | 94,0% | 90,8% |
| SMB | 91,7% | 88,9% |

Mid-market e SMB spiegano gran parte del deterioramento. Aprendo per canale commerciale, emerge che i clienti acquisiti tramite un nuovo partner hanno GRR nettamente inferiore rispetto a quelli acquisiti dal sales team interno. Il problema non è più “la retention peggiora”, ma **il valore perso è concentrato nei clienti recenti mid-market/SMB provenienti dal nuovo partner**.

Le coorti alla stessa età mostrano che il deterioramento compare nei nove mesi successivi al lancio del partner. Ma il contratto firmato si rivela un `t0` poco adatto: gli account partner impiegano più tempo fra firma e go-live. Il team riallinea quindi le coorti alla **prima automazione eseguita in produzione**. Il gap si riduce, ma non scompare. Una parte della differenza apparteneva al processo commerciale/implementativo; una parte rimane nel lifecycle d'uso.

A quel punto il funnel dei primi quattordici giorni mostra dove le traiettorie divergono:

| Passaggio | Sales interno | Partner |
| --- | ---: | ---: |
| Setup base completato | 84% | 78% |
| Almeno 3 utenti invitati | 76% | 51% |
| Integrazione ERP attiva | 68% | 29% |
| Primo workflow automatizzato | 72% | 38% |

Il problema non vive nel signup. Nasce nel passaggio da configurazione iniziale a uso collaborativo e integrato.

OpsPilot chiamava “activated” qualunque account che completasse il setup. L'analista propone un candidato più vicino al valore: **almeno tre utenti attivi, integrazione ERP funzionante e primo workflow automatizzato entro quattordici giorni**. Con questa definizione l'activation è **61%** per il sales interno e **24%** per il partner. Il median time-to-value è **3,1 giorni** contro **8,7 giorni**.

Gli account che raggiungono il candidato entro sette giorni mostrano retention successiva molto più alta. È un segnale forte, non la prova che ridurre il TTV produrrebbe automaticamente più rinnovi.

La curva di survival aggiunge un altro elemento. Le due popolazioni sono relativamente vicine nei primi quarantacinque giorni; la divergenza accelera fra il secondo e il quarto mese, proprio quando termina l'onboarding proattivo. Il problema non sembra quindi limitarsi al raggiungimento del primo valore: molti account partner arrivano a quel valore lentamente e non diventano abbastanza autonomi prima che il supporto intensivo finisca.

### Dal rischio al valore a rischio

A questo punto il team potrebbe ancora commettere un errore: trattare tutti gli account fragili come equivalenti. ARR e contribution margin mostrano invece che alcuni account ad altissimo rischio sono piccoli, mentre altri con rischio leggermente inferiore rappresentano molto più valore economico.

Per ogni account vengono quindi mantenuti separati rischio osservato, ARR/margine a rischio, tempo al rinnovo e stato del lifecycle.

Solo ora viene costruito un modello predittivo. Fra i segnali principali emergono nessuna automazione nelle ultime tre settimane, meno del **40%** degli utenti invitati ancora attivi, integrazione ERP assente, aumento dei ticket di configurazione e mancata partecipazione alle sessioni di onboarding. Il modello identifica circa **1.200 account ad alto rischio**.

Customer Success può seguirne soltanto **300**.

Se il team prende i 300 score più alti, trova molti account che hanno già comunicato il mancato rinnovo, stanno chiudendo una divisione o hanno completato una migrazione verso un concorrente. Sono prevedibili, ma poco recuperabili. La priorità viene allora definita come combinazione di rischio significativo, valore economico materiale, problema ancora plausibilmente risolvibile, tempo sufficiente prima del rinnovo e stakeholder ancora coinvolti.

La lista cambia radicalmente.

### La diagnosi indica l'intervento da testare, non il suo effetto

OpsPilot considera due azioni: contatto generico del Customer Success oppure sessione tecnica dedicata a integrazione ERP e primo workflow. La seconda è più coerente con il punto di rottura osservato. Ma osservare che i clienti che ricevono più supporto rinnovano di più non basterebbe: potrebbero essere selezionati in modo diverso.

Questo è il punto in cui il lifecycle analysis deve fermarsi intenzionalmente. Ha ristretto il problema abbastanza da progettare un test sensato; non deve fingere di aver già misurato l'effetto dell'intervento.

La mappa finale comprime l'indagine in una pagina:

| Campo | Evidenza OpsPilot |
| --- | --- |
| KPI iniziale | GRR trimestrale 93,8% → 90,9% |
| Chi | nuove coorti mid-market/SMB del canale partner |
| Quando | deterioramento nelle coorti entrate dopo il lancio del partner |
| Dove | setup → collaborazione/integration → primo workflow |
| Activation | candidato: 3 utenti + ERP + workflow entro 14 giorni |
| Time-to-value | partner 8,7 giorni vs interno 3,1 |
| Momento fragile | divergenza tra mese 2 e mese 4, dopo fine supporto proattivo |
| Valore | ARR a rischio concentrato in una parte degli account mid-market |
| Predittori | usage in calo, ERP assente, utenti attivi in calo, ticket configurazione |
| Actionability | escludere account già persi; privilegiare problemi ancora risolvibili |
| Cosa sappiamo | il deterioramento è localizzato e preceduto da bassa activation/TTV più lungo |
| Cosa non sappiamo | quale intervento produce causalmente più rinnovi |
| Prossimo metodo | disegno sperimentale/causale sull'intervento di onboarding tecnico |

La conclusione finale non è “il partner causa churn perché non configura ERP”. È più calibrata:

> **Il deterioramento è concentrato nelle nuove coorti del canale partner. Questi account raggiungono meno spesso l'activation operativa, impiegano più tempo a ottenere valore e divergono soprattutto dopo la fine del supporto proattivo. L'assenza dell'integrazione ERP è un forte segnale, ma non abbiamo ancora dimostrato che completarla sia di per sé la causa della maggiore retention. Proponiamo di testare un intervento tecnico mirato sugli account ancora influenzabili.**

Questa è la funzione della Lifecycle Diagnostic Map: trasformare retention e churn da percentuali di dashboard in una diagnosi abbastanza precisa da sapere **quale domanda viene dopo**.