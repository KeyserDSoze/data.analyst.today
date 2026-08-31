## 6.12 Caso studio: il piano di recupero che rischiava di colpire i clienti sbagliati

Una piattaforma B2B in abbonamento, **OpsPilot**, nota che il gross revenue retention trimestrale è sceso dal 93,8% al 90,9% in due trimestri.

Il CEO chiede al team Data di “identificare i clienti a rischio e salvarli prima che sia troppo tardi”.

La richiesta sembra chiara. In realtà contiene almeno quattro problemi diversi:

- definire cosa significa “a rischio”;
- capire quali coorti stanno peggiorando;
- distinguere segnali da cause;
- identificare azioni realmente utili.

### Primo passo: segmentare il problema

OpsPilot divide gli account per:

- dimensione cliente;
- piano;
- mese di acquisizione;
- canale commerciale;
- utilizzo delle feature principali;
- tempo al primo valore;
- numero di utenti attivi;
- ticket support;
- presenza o meno dell'integrazione ERP.

Il peggioramento è fortemente concentrato nei clienti acquisiti negli ultimi nove mesi tramite un nuovo partner commerciale.

Il churn di quel segmento è quasi doppio rispetto agli account acquisiti dal sales team interno.

### Secondo passo: guardare l'activation

Il partner genera molti clienti, ma il comportamento iniziale è diverso:

| Metrica nei primi 14 giorni | Sales interno | Partner |
|---|---:|---:|
| setup completato | 84% | 78% |
| almeno 3 utenti invitati | 76% | 51% |
| integrazione ERP attiva | 68% | 29% |
| primo workflow automatizzato | 72% | 38% |
| median time-to-value | 3,1 giorni | 8,7 giorni |

Il volume di acquisition era cresciuto. La qualità dell'activation era peggiorata.

### Terzo passo: costruire le curve

Le survival curve mostrano che le due popolazioni rimangono relativamente simili nei primi 45 giorni. La divergenza aumenta tra il secondo e il quarto mese.

Questo coincide con il momento in cui il supporto onboarding smette di essere proattivo e il cliente dovrebbe essere ormai autonomo.

Gli account partner che non hanno attivato l'integrazione ERP entro 30 giorni mostrano una probabilità di churn a sei mesi molto superiore.

Ancora una volta, questo non prova che “installare ERP” causi retention. Potrebbe essere un proxy per maturità, complessità del cliente o qualità dell'onboarding.

### Quarto passo: il modello di rischio

Il team costruisce un semplice modello predittivo e trova come principali segnali:

- nessuna automazione usata nelle ultime tre settimane;
- meno del 40% degli utenti invitati ancora attivi;
- integrazione ERP assente;
- aumento dei ticket su configurazione;
- mancata partecipazione alle sessioni di onboarding.

Il modello identifica circa 1.200 account ad alto rischio.

Il Customer Success team può però gestirne solo 300.

Se si usa soltanto il risk score, vengono selezionati i 300 clienti con maggiore probabilità di churn. Ma molti di loro hanno già comunicato la decisione di non rinnovare o stanno chiudendo l'attività.

Sono facili da prevedere e difficili da salvare.

### Quinto passo: distinguere rischio da recuperabilità

Il team introduce quindi un secondo criterio: la **actionability**.

Un account è prioritario quando combina:

- rischio elevato;
- valore economico significativo;
- segnali che indicano un problema potenzialmente risolvibile;
- tempo sufficiente prima del rinnovo.

La lista dei 300 clienti cambia radicalmente.

### Il test operativo

OpsPilot sperimenta due interventi su account comparabili:

- gruppo A: contatto standard del Customer Success;
- gruppo B: sessione tecnica dedicata per completare ERP integration e primo workflow;
- gruppo di controllo: processo normale.

Dopo due cicli di rinnovo, il gruppo B mostra un miglioramento della retention maggiore rispetto al semplice contatto generico, soprattutto tra gli account che avevano iniziato ma non completato la configurazione.

Il progetto non si conclude con “abbiamo un churn model”. Si conclude con un sistema decisionale:

**Cohort → Activation → Risk → Actionability → Intervention → Measurement**

Questo è il passaggio da analytics descrittiva a decision intelligence.

### La lezione

Il CEO aveva chiesto di identificare i clienti a rischio.

La domanda migliore era:

> Quali clienti sono a rischio, quali sono economicamente importanti, quali possiamo ancora influenzare e quale intervento modifica realmente la loro probabilità di rinnovo?

La seconda domanda richiede più lavoro. Ma è la domanda che può cambiare il risultato economico.
