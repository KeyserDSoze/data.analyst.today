## 1.14 Gli errori tipici dell'analista

Molti errori analitici non nascono da una formula sbagliata. Nascono prima, nella definizione del problema, nella scelta dei dati o nell'interpretazione.

### 1.14.1 Partire dallo strumento

Aprire Power BI, Excel o un notebook prima di chiarire la domanda porta facilmente a produrre output senza una decisione associata.

### 1.14.2 Confondere disponibilità del dato e rilevanza del dato

Il fatto che un campo sia presente nel database non significa che sia utile. Al contrario, informazioni importanti possono non essere disponibili e richiedere nuove raccolte o proxy.

### 1.14.3 Accettare le metriche come se fossero naturali

Ogni metrica incorpora definizioni. Un “cliente attivo” può significare login negli ultimi 30 giorni, acquisto negli ultimi 90, contratto non scaduto o altro ancora.

### 1.14.4 Cercare subito la causa

Un pattern può essere reale senza che la prima spiegazione sia corretta. Correlazione temporale, segmentazione e plausibilità non bastano da sole a dimostrare causalità.

### 1.14.5 Guardare solo le medie

Le medie possono nascondere distribuzioni, code, sottogruppi e fenomeni di composizione. Una media stabile può coesistere con cambiamenti profondi nei segmenti.

### 1.14.6 Cambiare il denominatore senza accorgersene

Molti KPI sono rapporti. Se cambia la popolazione di riferimento, il valore può cambiare anche senza un cambiamento sostanziale nel comportamento individuale.

### 1.14.7 Ignorare la qualità e il lineage del dato

Una tabella “pronta” può contenere deduplicazioni, filtri, join o trasformazioni di cui l'analista non conosce la logica. Comprendere da dove arriva il dato è parte dell'analisi.

### 1.14.8 Fermarsi al grafico

Un grafico interessante non è ancora un insight. Bisogna collegare il pattern a una domanda, un'ipotesi e una possibile azione.

### 1.14.9 Nascondere l'incertezza

Presentare una stima come se fosse certa può rendere il messaggio più semplice, ma peggiora la qualità decisionale. È meglio comunicare intervalli, limiti e assunzioni rilevanti.

### 1.14.10 Usare l'AI come autorità

L'AI è un acceleratore, non una fonte di verità. Il NIST AI Risk Management Framework sottolinea la necessità di gestire i rischi dei sistemi generativi lungo il loro ciclo di vita, inclusi valutazione, monitoraggio e controllo. Anche la documentazione Microsoft per Copilot in Power BI raccomanda agli utenti di valutare criticamente gli output e ricorda che risposte scorrette possono produrre decisioni e azioni scorrette.

### Regola operativa

> L'errore più pericoloso non è quello evidente. È quello che produce un risultato plausibile, ben presentato e perfettamente coerente con una domanda formulata male.

### Riferimenti

- NIST, *Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile*: https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence
- Microsoft Learn, *Use Copilot with semantic models in Power BI*: https://learn.microsoft.com/en-us/power-bi/create-reports/copilot-semantic-models
