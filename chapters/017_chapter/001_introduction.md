# Capitolo 17 — Casi end-to-end di Data Analysis

## 17.0 Il problema reale non arriva con il nome della tecnica

Finora abbiamo costruito molti strumenti: Analytical Brief, Data Readiness Review, Evidence Map, Uncertainty Brief, Lifecycle Diagnostic Map, Temporal Decision Brief, Causal Identification Brief, Experiment Contract, Predictive Decision Card, Analytical Data Contract, Data Flow Architecture Map, Tooling Decision Record, AI Analysis Control Sheet, Decision Record e Decision Communication Pack.

Il rischio, arrivati qui, è trasformare quel patrimonio in una nuova checklist universale. Nel lavoro reale succede il contrario. Nessuno chiede «applica una Difference-in-Differences» o «costruisci un Predictive Decision Card». Arrivano richieste come «perché le vendite scendono?», «possiamo aumentare i prezzi?», «quali clienti dobbiamo contattare?» o «la campagna sta davvero creando valore?».

La parte più difficile non è ricordare quale tecnica conosciamo. È decidere **quale evidenza merita di essere prodotta e quale no**.

> **La domanda guida del capstone è: qual è il minimo insieme di evidenze sufficientemente affidabili per cambiare questa decisione?**

Questa formulazione cambia il modo in cui leggeremo i casi. Una reconciliation può essere la soluzione completa se il failure mode principale è semantico. Una decomposition può bastare per rifiutare un'azione generalizzata senza identificare causalmente ogni driver. Un esperimento può invece essere indispensabile quando la decisione richiede sapere se un intervento cambia davvero l'outcome. E qualche volta il risultato professionale sarà `WAIT FOR X`, `NO ACTION` o **non identificabile con i dati disponibili**.

Il capitolo non misura quindi la maturità dal numero di tecniche usate. La misura dalla qualità del **routing** e dalla disciplina dello **stopping**.

## Il Capstone Routing Canvas

Prima di entrare nei dati useremo un artefatto compatto. Il Canvas non prescrive il metodo; esplicita ciò che deve governarne la scelta.

```text
CAPSTONE ROUTING CANVAS

Decision:
Decision owner / deadline:

Failure cost:
- cost of acting wrongly
- cost of not acting
- cost of waiting

Claim needed:
- descriptive / diagnostic / predictive / causal / treatment / economic

Readiness risks:
- semantics / grain / identity / time / freshness / selection / leakage / exposure

Minimum evidence path:
- deliverables that close a real decision risk

Stop rule:
- DECIDE / PILOT / WAIT FOR X / BUY INFORMATION / NO ACTION / NOT IDENTIFIED
```

I campi sono volutamente pochi. Il **failure cost** ci impedisce di trattare ogni decisione con lo stesso grado di formalità. Il **claim needed** impedisce sia l'over-analysis — cercare causalità quando basta localizzare un problema — sia l'under-analysis — usare una correlazione quando stiamo per impegnare milioni su un trattamento. I **readiness risks** ricordano che un metodo sofisticato non può salvare una popolazione sbagliata o una metrica diventata semanticamente obsoleta. La **stop rule** ci obbliga a dichiarare in anticipo quando altra analisi smette di avere valore.

## L'Evidence Ledger

I casi verranno raccontati come storie, ma una storia end-to-end può creare un pericolo: dopo aver visto il finale, ogni indizio precedente sembra inevitabilmente parte della spiegazione. Per impedirlo manteniamo idealmente tre colonne.

| Stato | Significato |
|---|---|
| **Observed** | fatti direttamente sostenuti da dati e controlli disponibili |
| **Inferred** | interpretazioni che richiedono assunzioni esplicite |
| **Still unknown** | informazione che potrebbe ancora cambiare claim o scelta |

L'Evidence Ledger non deve comparire materialmente in ogni pagina. È la disciplina che impedisce al racconto di trasformare un'associazione osservata ieri in una causa “che sapevamo da sempre” oggi.

## Il Method Gate

Ogni tecnica che entra in un caso deve guadagnarsi il diritto di restare. La domanda è:

> **Se non facessimo questa analisi, quale rischio decisionale rimarrebbe aperto?**

Se non sappiamo rispondere, probabilmente stiamo aggiungendo complessità per dimostrare competenza, non per migliorare la scelta.

Questo significa anche che i deliverable precedenti sono **modulari**. Orion Living potrà fermarsi con Analytical Brief, readiness, decomposition e Decision Record; NorthPeak avrà bisogno anche di prediction ed experimentation; Atlas Streaming risolverà un incidente senza addestrare un nuovo anomaly model; OrbisMarket userà una catena più lunga perché la decisione finale contiene davvero più failure mode indipendenti.

## Il costo dell'altra analisi

«Facciamo un'altra analisi» non è gratis. Costa tempo, capacità, ritardo decisionale e spesso introduce nuovi gradi di libertà. Per questo, prima di salire di livello metodologico, chiediamo quale informazione potrebbe cambiare scelta, quanto costa ottenerla e se arriverà prima che la decisione perda valore.

È la continuità diretta con il Value of Information e il Decision Record dei capitoli precedenti. Il capstone aggiunge un principio pratico: **il valore del metodo è marginale rispetto all'evidenza che possediamo già**.

## Casi documentati e casi compositi

Quando una fonte pubblica affidabile documenta una pratica o un risultato reale, la useremo come **caso reale documentato** senza estendere il claim oltre ciò che la fonte sostiene. Quando serve seguire un'indagine completa con numeri, alternative e decisioni costruite appositamente, useremo un **caso simulato/composito** dichiarandolo esplicitamente.

Questa distinzione è particolarmente importante nel capstone: una customer story può dimostrare che un'organizzazione ha integrato dati, cambiato un processo o riportato un certo risultato; non dimostra automaticamente il meccanismo causale che vorremmo usare nella nostra decisione.

## AI nel capstone

L'AI può scrivere query, ampliare lo spazio delle ipotesi, cercare inconsistenze, preparare una decomposition o comprimere la comunicazione. Ma ogni delega deve mantenere il controllo corrispondente. Se genera SQL, servono invarianti e reconciliation; se propone una causa, serve il claim gate; se prepara una recommendation, deve ricevere alternative, economics e permission boundary.

Non esiste una corsia AI separata. Esiste lo stesso sistema analitico con un esecutore in più.

## Come leggere i casi

Non cerchiamo una sequenza fissa di dieci passaggi. Cerchiamo il momento in cui il routing cambia. In un caso la scoperta decisiva sarà che «vendite» significa net sales e non ordini. In un altro sarà che un churn score non misura persuadibilità. In un altro ancora un SRM bloccherà completamente un risultato apparentemente significativo.

Per ogni caso chiediamoci quindi:

1. quale decisione era realmente aperta;
2. quale failure cost dominava;
3. quale livello di claim serviva;
4. quale evidenza ha eliminato una spiegazione o un'opzione;
5. perché il team ha scelto di salire — oppure di non salire — a un metodo più forte;
6. quale stop rule ha chiuso la prima decisione;
7. quale informazione avrebbe cambiato il percorso.

Il Capitolo 18 partirà dal risultato di questo ragionamento. Una volta risolta una decisione, dovremo chiederci che cosa cambia quando la stessa capacità analitica deve funzionare ogni lunedì senza essere ricostruita da zero.

> **La maturità analitica appare quando sappiamo non soltanto produrre evidenza, ma scegliere il percorso minimo che merita fiducia, fermarci quando è sufficiente e riconoscere quando un'altra tecnica sarebbe soltanto ritardo mascherato da rigore.**
