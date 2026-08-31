## 0.1 Diventare manager di N agenti

Il salto più importante non è passare da Excel a Python, da SQL a un LLM o da un notebook a un agente.

È passare da **esecutore di task** a **orchestratore di capacità**.

Un analista AI-native può coordinare agenti diversi per data discovery, SQL, data quality, metriche, forecasting, causalità, visualizzazione, documentazione, code review ed executive communication.

La novità non è soltanto che ciascuno di questi compiti può essere accelerato. È che più attività possono essere eseguite contemporaneamente.

Ma c'è un limite fondamentale:

> **possiamo parallelizzare l'esecuzione; non possiamo dare per scontato che si parallelizzi anche il giudizio.**

### Caso simulato/composito: dieci agenti, una sola decisione

Un marketplace vede il Gross Merchandise Value scendere del 9% in Spagna.

Il responsabile analytics non apre dieci dashboard a caso. Scompone il problema e assegna ruoli distinti.

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

In pochi minuti il team virtuale ha prodotto più piste di quante una persona avrebbe potuto esplorare nello stesso tempo.

Ma l'ultima riga della tabella mostra il rischio.

L'agente incaricato della sintesi ha ricevuto il compito di produrre una raccomandazione. Davanti a due spiegazioni concorrenti — release iOS e incidente del provider — può essere spinto a trasformare un conflitto ancora aperto in una conclusione netta.

Qui serve il timoniere.

L'analista non chiede semplicemente quale ipotesi “sembra più probabile”. Chiede quali osservazioni distinguono le due spiegazioni:

- quali utenti hanno ricevuto davvero la release?
- quale provider di pagamento usavano?
- il problema compare anche su iOS con provider alternativi?
- compare sul provider coinvolto anche fuori da iOS?
- la sequenza temporale coincide meglio con il deploy o con l'incidente?
- esistono segmenti che funzionano come controllo naturale?

Gli agenti hanno moltiplicato la capacità investigativa. L'analista deve trasformarla in una **gerarchia di evidenze**.

### Disegnare ruoli, non una catena di consenso

Un errore frequente è costruire workflow in cui ogni agente assume corretto l'output del precedente.

Se il primo interpreta male una metrica, il secondo può scrivere una query perfetta sulla metrica sbagliata, il terzo può visualizzarla bene e il quarto può produrre una sintesi molto convincente.

La qualità formale aumenta. L'errore iniziale rimane.

Una struttura più robusta separa almeno quattro funzioni:

1. **worker agents** — producono analisi, codice, ricerche o trasformazioni;
2. **critic/review agents** — cercano errori, ipotesi rivali e controesempi;
3. **control layer** — esegue test deterministici, reconciliation e policy;
4. **human owner** — risolve conflitti, valuta l'incertezza e decide il livello di fiducia appropriato.

Il punto non è inserire sempre quattro componenti diverse. È evitare che produzione, verifica e decisione coincidano nello stesso passaggio senza frizioni.

### Manager non significa micromanager

Essere al timone non significa leggere ogni token o riscrivere ogni query.

Un manager di agenti deve invece rendere espliciti alcuni elementi prima che il lavoro parta:

- **scope** — che cosa può fare l'agente;
- **input** — a quali dati e strumenti può accedere;
- **obiettivo** — quale risultato deve produrre;
- **definition of done** — quando il task può considerarsi concluso;
- **checks** — quali verifiche sono obbligatorie;
- **escalation** — quali condizioni richiedono intervento umano;
- **budget** — quante iterazioni, tempo e costo può consumare;
- **authority** — quali azioni può eseguire senza approvazione.

Questi elementi trasformano un prompt generico in un mandato operativo.

### Il collo di bottiglia cambia

Quando N agenti possono lavorare contemporaneamente, il collo di bottiglia si sposta.

Non è più soltanto produrre query, grafici o memo. Diventa:

- scegliere le priorità;
- decomporre bene il problema;
- coordinare dipendenze;
- risolvere conflitti tra evidenze;
- riconoscere assunzioni sbagliate;
- decidere quando l'analisi è sufficiente;
- assumersi la responsabilità della conclusione.

Per questo analytical thinking, business understanding e semantica acquistano valore proprio mentre l'esecuzione tecnica diventa più accessibile.

> **Il futuro dell'analista non è competere con dieci agenti. È saper dirigere dieci agenti verso una risposta che meriti fiducia.**
