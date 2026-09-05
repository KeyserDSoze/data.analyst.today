## 19.12 Conclusione — Al timone, anche quando il lavoro cambia

Questo libro è iniziato con una provocazione semplice: l'AI può fare sempre più lavoro, ma la responsabilità di capire che cosa stiamo consegnando resta nostra.

Dopo diciannove capitoli possiamo rendere quella frase più precisa. Il problema non è difendere il lavoro manuale, dimostrare di saper scrivere una query più velocemente di un agente o conservare ogni attività che in passato rendeva riconoscibile il mestiere. Il problema professionale è **usare una quantità crescente di capacità senza perdere il controllo su intento, significato, evidenza, rischio e decisione**.

Quando produrre una query era costoso, una parte importante del valore stava inevitabilmente nella query. Quando quella produzione diventa più economica, diventano più visibili i colli di bottiglia che erano già lì: capire quale domanda meriti l'analisi, quale dato rappresenti davvero il fenomeno, quale definizione sia autorevole, quale confronto sia valido, quanta incertezza contenga la stima, quale claim possiamo sostenere e quale nuova informazione potrebbe farci cambiare idea.

La tecnologia non elimina questi problemi. Può aumentarne il blast radius, perché una specifica sbagliata può trasformarsi più rapidamente in migliaia di output coerenti tra loro e plausibili alla vista.

Per questo il libro non ha sostenuto che SQL, statistica, data modeling, forecasting o experimentation smetteranno di servire. Ha mostrato che la tecnica assume più funzioni contemporaneamente. Serve a **eseguire**, naturalmente, ma anche a **verificare** e a **progettare**. Se l'AI comprime una parte dell'esecuzione, le altre due funzioni acquistano peso. Chi non capisce grain non può verificare un join; chi non comprende sampling non può calibrare l'incertezza; chi non comprende causalità non sa distinguere una spiegazione plausibile da un effetto identificato; chi non comprende il business non sa quale metrica valga la pena ottimizzare.

La capacità di delegare nasce quindi dalla capacità di capire che cosa stiamo delegando.

I segnali sul lavoro disponibili oggi non ci offrono una profezia e non ne abbiamo bisogno. L'ILO stima che circa un lavoratore su quattro si trovi in un'occupazione con qualche grado di esposizione alla GenAI e considera, per la maggior parte dei lavori esposti, la trasformazione più plausibile della completa sostituzione. Il World Economic Forum vede AI e big data tra le skill in maggiore crescita mentre analytical thinking resta centrale. Microsoft descrive nel *Work Trend Index 2026* una possibile evoluzione verso maggiore human agency mentre agenti e AI assorbono più execution. Sono prospettive diverse, tutte insufficienti a descrivere il 2035 con precisione, ma abbastanza coerenti da dirci che task, skill e operating model stanno già cambiando.

Fonti pubbliche:
- https://www.ilo.org/publications/generative-ai-and-jobs-2025-update
- https://www.weforum.org/publications/the-future-of-jobs-report-2025/digest/
- https://www.microsoft.com/en-us/worklab/work-trend-index/agents-human-agency-and-the-opportunity-for-every-organization

La strategia robusta non è indovinare quale scenario vincerà. È costruire capacità che conservino valore in scenari diversi.

È anche la logica che ha attraversato il libro fin dall'inizio. Siamo partiti da numeri che sembravano semplici e abbiamo scoperto che dietro ciascuno esisteva una decisione sul significato. Abbiamo imparato che una tabella può essere tecnicamente valida e semanticamente sbagliata; che una correlazione può essere forte senza autorizzare una causal claim; che un forecast può avere una metrica migliore e una policy peggiore; che un esperimento può avere un p-value convincente e restare `BLOCKED`; che una dashboard può essere disponibile e non essere fit for decision; che un agente può completare il task e avere comunque troppa authority.

Statistica, SQL, causalità, experimentation, architecture, AI e comunicazione non sono quindi discipline isolate accostate in un manuale. Sono modi differenti di proteggere **il percorso tra realtà e decisione**. Per ogni problema abbiamo cercato il minimo insieme di controlli necessario a far crescere il livello del claim senza farlo crescere più rapidamente dell'evidenza.

Nel Capitolo 0 avevamo scritto:

> **Puoi delegare all'AI l'esecuzione.  
> Puoi delegare all'AI l'esplorazione.  
> Puoi delegare all'AI la prima bozza.  
> Puoi delegare all'AI perfino parte della verifica.  
> Non puoi delegare la responsabilità di capire ciò che stai consegnando.**

Essere al timone, dopo tutto il percorso fatto, non significa eseguire personalmente ogni manovra. Significa sapere dove stiamo cercando di andare, quali strumenti e persone possono aumentare la nostra capacità, quali segnali meritano fiducia, quali condizioni richiedono escalation e quale rischio stiamo accettando quando decidiamo di procedere. Più il sistema diventa potente, meno il timone coincide con la micro-esecuzione e più coincide con **direzione, controllo e accountability**.

Questo richiede anche la disponibilità a lasciare andare parte del vecchio lavoro. Alcuni task verranno automatizzati; altri perderanno valore relativo; alcune skill non meriteranno più lo stesso investimento. Conservare artificialmente l'attrito non rende una professione più nobile. La maturità sta nel delegare ciò che può essere delegato, ricostruire profondità dove la verification reserve si sta assottigliando e riconoscere i nuovi failure mode che emergono quando aumenta la capacità del sistema.

Per questo il capitolo finale termina con un Personal Career Operating Plan e non con una lista dei software da imparare. Il piano ci chiede quale responsabilità vogliamo possedere, quale decision span abbiamo già costruito, dove esiste depth reale, quale dominio stiamo imparando, quanto possiamo delegare e quali competenze devono restare vive per meritare quella delega. Non ingegnerizza la carriera. Ci costringe soltanto a essere intenzionali su dove accumuliamo capitale professionale.

Alla fine possiamo tornare anche alla definizione più semplice del mestiere:

> **Il Data Analyst è la persona che trasforma domande ambigue e dati imperfetti in evidenza sufficientemente affidabile da migliorare una decisione.**

In alcune aziende questo significherà ancora riconciliare tre file che non tornano. In altre significherà dirigere agenti, mantenere semantic contract e progettare eval o decision system. Gli strumenti, le interfacce e perfino il titolo cambieranno. Resterà la stessa responsabilità: sapere che cosa stiamo misurando, quanto possiamo fidarci, quale evidenza manca, che cosa potrebbe falsificare la conclusione e se l'informazione prodotta cambia davvero una scelta.

Se sappiamo rispondere a queste domande, non abbiamo bisogno di competere con la macchina sul numero di righe di SQL scritte in un'ora. Stiamo facendo un lavoro diverso e più difficile: decidere quando una risposta merita di diventare evidenza.

Siamo ancora al timone.

> **Gli strumenti cambieranno. Il timone resta una responsabilità.**