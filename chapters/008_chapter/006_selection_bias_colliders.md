## 8.5 Selection bias e collider: quando il campione crea una relazione

Non tutte le distorsioni nascono da una variabile che causa sia trattamento sia outcome. A volte il problema nasce dal fatto che analizziamo solo una parte selezionata della popolazione.

### Caso - I venditori migliori sembrano usare meno il CRM

Un'azienda B2B analizza soltanto le opportunità che hanno raggiunto la fase finale della pipeline. Tra queste osserva che i venditori che registrano meno attività nel CRM hanno un win rate più alto.

La direzione commerciale conclude che documentare troppe attività faccia perdere tempo e riduca le vendite.

Ma per arrivare alla fase finale un'opportunità può avere due caratteristiche che aiutano molto:

- elevata qualità iniziale del lead;
- forte attività commerciale.

Se selezioniamo soltanto le opportunità arrivate alla fase finale, finiamo per confrontare casi in cui una qualità più bassa può essere compensata da maggiore attività e viceversa.

Condizionare sulla selezione può creare una relazione artificiale tra variabili che nella popolazione completa non hanno quella relazione.

### Un collider in forma intuitiva

Immaginiamo:

`qualità lead -> arrivo alla fase finale <- intensità commerciale`

L'arrivo alla fase finale è influenzato da entrambe le variabili. È quindi un punto di collisione delle due frecce: un **collider**.

Se analizziamo solo le opportunità che hanno raggiunto quella fase, stiamo condizionando sul collider e possiamo introdurre un'associazione spuria tra qualità del lead e intensità commerciale.

### Caso - Soddisfazione dei clienti che rispondono al survey

Un servizio digitale invia un questionario NPS a tutti i clienti. Risponde il 18%.

Tra i rispondenti, chi usa più frequentemente il prodotto sembra meno soddisfatto.

Il team propone di ridurre notifiche e funzionalità avanzate.

Ma la probabilità di rispondere è maggiore sia per:

- utenti estremamente coinvolti;
- utenti molto insoddisfatti.

Analizzando soltanto chi risponde, si studia una popolazione selezionata attraverso un meccanismo legato alle variabili di interesse.

### Forme comuni di selection bias nel lavoro quotidiano

Il problema compare quando analizziamo solo:

- clienti sopravvissuti abbastanza a lungo;
- utenti che completano l'onboarding;
- lead diventati opportunità;
- dipendenti ancora presenti in azienda;
- ordini effettivamente consegnati;
- persone che rispondono a una survey;
- ticket escalati;
- campagne che hanno ottenuto abbastanza volume da essere mantenute attive.

La domanda da fare è:

> **Perché questa unità è entrata nel dataset che sto analizzando?**

### Caso - Analisi dei tempi di consegna

Un marketplace vuole capire se il nuovo corriere è più veloce. L'analisi include solo ordini consegnati entro 30 giorni.

Il nuovo corriere ha un tempo medio di 2,8 giorni, il vecchio 3,4.

Successivamente emerge che il nuovo corriere ha anche una percentuale maggiore di ordini non consegnati entro 30 giorni. Questi ordini sono stati esclusi dal dataset.

Il filtro ha eliminato proprio una parte importante dei casi peggiori.

### Regola operativa

Prima di interpretare qualsiasi relazione chiediamo:

1. qual è la popolazione target?
2. attraverso quali filtri entra nel dataset?
3. i filtri dipendono dal trattamento, dall'outcome o da loro cause?
4. chi manca dall'analisi?
5. come cambierebbe la conclusione includendo gli esclusi?

> **Un dataset può essere tecnicamente perfetto e statisticamente distorto perché il problema è nel processo di selezione che lo ha creato.**
