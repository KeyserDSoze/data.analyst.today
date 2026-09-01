## 6.12 Caso end-to-end: costruire una Lifecycle Diagnostic Map

Il capitolo ha introdotto molte viste: segmenti, coorti, funnel, activation, retention, survival, reactivation, valore e rischio.

Il pericolo è usarle come nove dashboard indipendenti.

Il loro valore aumenta quando convergono in un unico oggetto decisionale: una **Lifecycle Diagnostic Map**.

La mappa deve rispondere, in ordine, a queste domande:

**chi → quando → dove → primo valore → persistenza → valore economico → rischio → actionability → prossimo metodo**.

### Caso simulato/composito: OpsPilot

**OpsPilot** è una piattaforma B2B in abbonamento. Negli ultimi due trimestri la Gross Revenue Retention trimestrale è scesa dal 93,8% al 90,9%.

Il CEO chiede:

> Identificate i clienti a rischio e salvateli prima che sia troppo tardi.

La richiesta sembra operativa, ma contiene domande diverse.

Prima di costruire un modello, il team ricostruisce il lifecycle.

### 1. Chi — segmentazione del valore perso

Il peggioramento non è uniforme.

| Segmento | GRR precedente | GRR attuale |
| --- | ---: | ---: |
| Enterprise | 95,1% | 94,4% |
| Mid-market | 94,0% | 90,8% |
| SMB | 91,7% | 88,9% |

La perdita maggiore è in mid-market e SMB.

Segmentando per canale commerciale emerge un pattern ancora più forte: i clienti acquisiti tramite un nuovo partner hanno GRR nettamente inferiore rispetto a quelli acquisiti dal sales team interno.

Il problema passa da “la retention peggiora” a:

> il valore perso è concentrato nei clienti recenti mid-market/SMB provenienti dal nuovo partner.

### 2. Quando — coorti di acquisizione e di go-live

Il team confronta le coorti alla stessa età.

Le coorti precedenti all'introduzione del partner hanno retention M6 relativamente stabile. Le coorti entrate nei nove mesi successivi peggiorano progressivamente.

Ma emerge anche un dettaglio importante: il contratto non è un buon `t0`.

Gli account partner hanno un intervallo più lungo tra firma e go-live. Il team riallinea quindi le coorti alla **prima automazione eseguita in produzione**.

La differenza si riduce, ma non scompare.

Questo evita di attribuire al prodotto una parte del ritardo che apparteneva al processo commerciale e implementativo.

### 3. Dove — il funnel di onboarding

Nei primi quattordici giorni:

| Passaggio | Sales interno | Partner |
| --- | ---: | ---: |
| Setup base completato | 84% | 78% |
| Almeno 3 utenti invitati | 76% | 51% |
| Integrazione ERP attiva | 68% | 29% |
| Primo workflow automatizzato | 72% | 38% |

Il maggiore drop-off è tra setup iniziale e adozione collaborativa/integrata.

Non è un problema generico di signup. È un problema nel passaggio da configurazione a utilizzo operativo.

### 4. Primo valore — activation e time-to-value

OpsPilot aveva definito “activated” ogni account che completava il setup.

L'analista propone un candidato più vicino al valore:

> almeno tre utenti attivi, integrazione ERP funzionante e primo workflow automatizzato entro quattordici giorni.

Con questa definizione:

- sales interno: activation 61%;
- partner: activation 24%.

Il median time-to-value è:

- sales interno: 3,1 giorni;
- partner: 8,7 giorni.

Gli account che raggiungono il candidato di activation entro sette giorni mostrano retention successiva molto più alta.

È una associazione importante, non ancora una prova che ridurre il TTV causi da solo il miglioramento.

### 5. Persistenza — la curva mostra il momento fragile

Le survival curve delle due popolazioni sono relativamente vicine nei primi quarantacinque giorni.

La divergenza accelera tra il secondo e il quarto mese.

Questo coincide con la fine dell'onboarding proattivo.

Il team scopre quindi un secondo problema: molti account partner non diventano realmente autonomi prima che il supporto intensivo termini.

La domanda operativa cambia ancora:

> il problema non è solo raggiungere il primo valore; è rendere il comportamento abbastanza stabile da sopravvivere alla fine del supporto guidato.

### 6. Valore economico — non tutti gli account a rischio hanno la stessa priorità

Il team calcola l'ARR a rischio e il contribution margin per segmento.

Alcuni account con rischio elevato hanno contratti molto piccoli. Altri, con rischio leggermente inferiore, rappresentano una quota molto maggiore del valore economico.

La priorità non può quindi essere definita soltanto dal churn rate.

Per ogni account vengono tenute separate:

- probabilità/rischio osservato;
- ARR e margine a rischio;
- tempo al rinnovo;
- stato del lifecycle.

### 7. Risk model — chi è più probabile che esca?

Il team costruisce un modello predittivo semplice.

I principali segnali includono:

- nessuna automazione nelle ultime tre settimane;
- meno del 40% degli utenti invitati ancora attivi;
- integrazione ERP assente;
- aumento dei ticket di configurazione;
- mancata partecipazione alle sessioni di onboarding.

Il modello identifica circa 1.200 account ad alto rischio.

Il Customer Success team può gestirne soltanto 300.

### 8. Actionability — chi possiamo ancora influenzare?

I 300 risk score più alti includono molti account che:

- hanno già comunicato la decisione di non rinnovare;
- stanno chiudendo una divisione;
- hanno completato la migrazione verso un concorrente.

Sono facili da prevedere, ma poco recuperabili.

OpsPilot aggiunge quindi un livello di actionability.

Un account è prioritario se combina:

- rischio significativo;
- valore economico materiale;
- problema potenzialmente risolvibile;
- tempo sufficiente prima del rinnovo;
- stakeholder ancora coinvolti.

La lista dei 300 cambia radicalmente.

### 9. Intervento — il lifecycle analysis non dimostra ancora cosa funziona

Il team considera due interventi:

- contatto generico del Customer Success;
- sessione tecnica dedicata a ERP integration e primo workflow.

Il lifecycle analysis suggerisce che il secondo è più coerente con il punto di rottura osservato.

Ma non basta osservare che i clienti che ricevono più supporto rinnovano di più: potrebbero essere selezionati in modo diverso.

Per attribuire un effetto all'intervento serve un disegno causale o sperimentale adeguato.

Questo è il punto in cui il Capitolo 6 deve fermarsi intenzionalmente.

### 10. La Lifecycle Diagnostic Map

Il team sintetizza l'indagine in una pagina:

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

Questa tabella non sostituisce l'analisi. La comprime in una forma difendibile.

### Il punto più importante: separare evidenza e inferenza

La presentazione finale non dice:

> Il partner causa churn perché non configura ERP.

Dice:

> Il deterioramento è concentrato nelle nuove coorti del canale partner. Questi account raggiungono meno spesso l'activation operativa, impiegano più tempo a ottenere valore e divergono soprattutto dopo la fine del supporto proattivo. L'assenza dell'integrazione ERP è un forte segnale, ma non abbiamo ancora dimostrato che completarla sia di per sé la causa della maggiore retention. Proponiamo di testare un intervento tecnico mirato sugli account ancora influenzabili.

È una conclusione meno aggressiva. È anche molto più solida.

### Dal KPI alla decisione

Il percorso completo del capitolo diventa:

**KPI aggregato → segmento → coorte → funnel → activation/TTV → curva → valore → rischio → actionability → evidenza mancante → prossimo metodo**

Questo è ciò che trasforma retention e churn da percentuali di dashboard in una diagnosi del lifecycle.
