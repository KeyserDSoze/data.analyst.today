## 0.1 Diventare manager di N agenti

Il salto più importante non è passare da Excel a Python, da SQL a un LLM o da un notebook a un agente. È passare da **esecutore di task** a **orchestratore di capacità**.

Un analista AI-native può coordinare agenti diversi per data discovery, SQL, data quality, metriche, forecasting, causalità, visualizzazione, documentazione, code review ed executive communication. La novità non sta soltanto nell'accelerare ciascuna di queste attività. Sta nel poterle far procedere contemporaneamente, purché il lavoro sia scomposto in modo sensato e i risultati possano poi essere ricomposti in un'unica decisione.

Qui emerge il primo limite importante. Possiamo parallelizzare l'esecuzione molto più facilmente di quanto possiamo parallelizzare il giudizio. Dieci agenti possono cercare dieci piste nello stesso momento; qualcuno deve comunque stabilire quali evidenze siano compatibili, quali si contraddicano, quali dipendano dalla stessa assunzione sbagliata e quali siano abbastanza forti da cambiare una decisione.

> **Possiamo parallelizzare l'esecuzione; non possiamo dare per scontato che si parallelizzi anche il giudizio.**

### Caso simulato/composito: dieci agenti, una sola decisione

Un marketplace vede il Gross Merchandise Value scendere del 9% in Spagna. Il responsabile analytics non apre dieci dashboard a caso e non chiede a dieci agenti di «spiegare il calo». Scompone il problema e assegna a ciascun agente un mandato diverso.

| Agente | Compito | Primo risultato |
|---|---|---|
| Data health | controllare completezza e freshness | feed ordini completo al 99,8% |
| Funnel | localizzare il punto di rottura | calo nella conversione checkout |
| Payments | analizzare i fallimenti | payment failures in aumento |
| Releases | ricostruire i deploy | release mobile due giorni prima |
| Segmentation | cercare concentrazioni | calo soprattutto su iOS |
| Geography | decomporre il delta | Madrid e Barcellona spiegano il 71% |
| Hypothesis | proporre spiegazioni | release iOS come ipotesi principale |
| SQL review | controllare logica e metrica | query coerenti con il GMV certificato |
| Counter-hypothesis | cercare spiegazioni rivali | incidente di un provider di pagamento |
| Executive draft | preparare una sintesi | propone rollback della release |

In pochi minuti il team virtuale ha prodotto più piste di quante una persona avrebbe potuto esplorare nello stesso tempo. Ma proprio l'ultima riga della tabella mostra il rischio. L'agente incaricato della sintesi ha ricevuto il compito di produrre una raccomandazione e, davanti a due spiegazioni concorrenti — release iOS e incidente del provider — può essere spinto dalla forma stessa del mandato a trasformare un conflitto ancora aperto in una conclusione netta.

Qui serve il timoniere. L'analista non chiede quale ipotesi «sembra più probabile» e non vota fra agenti. Cerca invece osservazioni che distinguano davvero le due spiegazioni. Se il problema è la release, dovrebbe concentrarsi sugli utenti che l'hanno ricevuta; se è il provider, dovrebbe comparire anche fuori da iOS fra chi usa quel provider. Diventano quindi decisive la combinazione fra versione installata e provider di pagamento, la presenza del problema su iOS con provider alternativi, la presenza dello stesso errore sul provider coinvolto fuori da iOS e la sequenza temporale fra deploy e incidente. Segmenti non esposti possono funzionare come controlli naturali e aiutare a separare due storie che, viste solo a livello aggregato, sembrano entrambe plausibili.

Gli agenti hanno moltiplicato la capacità investigativa. Il lavoro dell'analista è trasformare quella capacità in una **gerarchia di evidenze**, non in una maggioranza di opinioni.

### Disegnare ruoli, non una catena di consenso

Un workflow agentico diventa fragile quando ogni passaggio assume corretto l'output del precedente. Se il primo agente interpreta male una metrica, il secondo può scrivere una query perfetta sulla metrica sbagliata, il terzo visualizzarla con grande chiarezza e il quarto produrre una sintesi molto convincente. La qualità formale cresce a ogni passaggio mentre l'errore iniziale rimane intatto.

Per evitare questa propagazione conviene separare le funzioni, anche quando non corrispondono a quattro componenti tecniche distinte. I **worker agents** producono analisi, codice, ricerche o trasformazioni. I **critic/review agents** hanno invece il mandato di cercare errori, controesempi e ipotesi rivali. Un **control layer** applica test deterministici, reconciliation e policy che non dipendono dal giudizio del modello. Infine il **human owner** risolve conflitti, valuta l'incertezza e decide quale livello di fiducia sia appropriato rispetto all'uso dell'output. Il punto non è costruire sempre una piccola burocrazia di agenti, ma evitare che produzione, verifica e decisione coincidano nello stesso passaggio senza alcuna frizione.

### Manager non significa micromanager

Essere al timone non significa leggere ogni token o riscrivere ogni query. Significa preparare il mandato in modo che l'agente sappia dove può muoversi e il team sappia come valutarne il lavoro. Prima che un task importante parta, alcuni elementi devono quindi essere espliciti e riutilizzabili:

- **scope** — che cosa può fare l'agente;
- **input** — a quali dati e strumenti può accedere;
- **obiettivo** — quale risultato deve produrre;
- **definition of done** — quando il task può considerarsi concluso;
- **checks** — quali verifiche sono obbligatorie;
- **escalation** — quali condizioni richiedono intervento umano;
- **budget** — quante iterazioni, tempo e costo può consumare;
- **authority** — quali azioni può eseguire senza approvazione.

Questa lista si guadagna il diritto di rimanere tale perché funziona come un piccolo contratto operativo. Non descrive otto idee indipendenti: definisce gli otto campi che rendono verificabile un mandato. Senza questi confini, un prompt può essere linguisticamente preciso e restare operativamente ambiguo.

Quando N agenti possono lavorare contemporaneamente, il collo di bottiglia si sposta di conseguenza. Produrre query, grafici o memo diventa meno raro; diventano più rari la capacità di scegliere le priorità, scomporre bene il problema, coordinare dipendenze, risolvere conflitti fra evidenze e riconoscere assunzioni sbagliate. Soprattutto, qualcuno deve decidere quando l'analisi è sufficiente e assumersi la responsabilità della conclusione.

Per questo analytical thinking, business understanding e semantica acquistano valore proprio mentre l'esecuzione tecnica diventa più accessibile.

> **Il futuro dell'analista non è competere con dieci agenti. È saper dirigere dieci agenti verso una risposta che meriti fiducia.**
