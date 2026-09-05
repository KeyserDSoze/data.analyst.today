## 16.12 Caso studio — NorthRiver Logistics: dalla dashboard di picco alla decisione sulla capacità

> **Nota editoriale:** NorthRiver Logistics è un caso simulato/composito. Numeri, organizzazione e sequenza sono costruiti per la didattica.

A sei settimane dal picco natalizio, NorthRiver Logistics deve decidere se acquistare capacità temporanea aggiuntiva da un carrier esterno. Il contratto richiede un commitment minimo di **€780.000**. La domanda, quindi, non è “come sta andando la logistica?”, ma:

> **Dobbiamo comprare ora capacità aggiuntiva, e quanta?**

Il Decision Record ha già trasformato il problema in tre alternative. Con **A — nessuna capacità extra** il costo incrementale è zero, ma il rischio di backlog, penali e ritardi cresce se la domanda supera lo scenario centrale. **B — +18.000 pacchi/giorno** costa €780k e porta la capacità totale a circa **166.000 pacchi/giorno**, sufficiente fino a uno scenario vicino a P80. **C — +30.000 pacchi/giorno** richiede **€1,24M** e riduce ulteriormente il rischio di under-capacity, ma aumenta molto il rischio di overcapacity.

Analytics preferisce **B**, con una condizione di espansione contrattuale se gli indicatori anticipatori superano soglia.

### La dashboard originale contiene più informazione della decisione

La pagina preparata per il COO include volumi giornalieri, forecast per deposito, forecast accuracy, backlog, cost per parcel, carrier utilization, SLA, overtime, staffing, weather, tredici filtri, due mappe e una tabella da 47 righe. Tutto può essere utile a qualcuno; quasi nulla, però, rende immediatamente chiaro se firmare il contratto da €780k.

La revisione parte quindi non dal layout, ma dal Decision Record.

### Forecast senza capacità: un numero senza decision boundary

Il primo grafico mostra un forecast di picco a **162.000 pacchi/giorno**. Preso da solo non dice se il sistema è in pericolo. La capacità interna affidabile è **148.000**; con l'opzione B sale a **166.000**; il P80 del forecast è **171.000**.

La visualizzazione viene quindi ricostruita sulla stessa grammatica: forecast centrale e range P20–P80, capacità interna, capacità con B e deadline contrattuale. La headline diventa:

> **La capacità interna copre solo marginalmente lo scenario centrale; l'opzione B copre gran parte del rischio fino a circa P80.**

Il visual non ordina di comprare B. Rende percepibile il trade-off che rende B una candidata credibile.

### La seconda informazione non è un altro KPI: è l'asimmetria del downside

La dashboard originale mostra `cost per parcel`, ma non rende visibile la differenza tra sbagliare per difetto e sbagliare per eccesso.

Nello scenario centrale-alto, l'under-capacity può produrre penali SLA, expedited shipping, overtime, cancellazioni, customer support e danno reputazionale. Il costo incrementale stimato è **€1,4M–€2,2M**. Il downside dell'over-capacity è invece più circoscritto: parte del commitment da €780k potrebbe restare inutilizzata.

La pagina executive non aggiunge altri KPI operativi. Mostra questa asimmetria, perché è ciò che discrimina B da A.

### Prediction interval senza switching value non basta

Sapere che P80 è 171k non dice ancora quando dovremmo cambiare scelta. Il Decision Record individua una switching condition: se il forecast aggiornato del picco scende sotto circa **151.000 pacchi/giorno** e il costo atteso dell'under-capacity resta sotto la stima base, il commitment B non è più giustificato.

Questa soglia entra nella Pack accanto al forecast. L'incertezza diventa così una regola di decisione, non un intervallo da commentare.

### Data maturity: il caveat che può comprare tempo

Il forecast usa anche i preorder di tre retailer. Uno dei feed è completo soltanto all'**82%** e verrà riconciliato entro 36 ore. Se questo fatto rimane nascosto, il COO vede un numero centrale come se fosse finalizzato. La nuova pagina dichiara:

> **Forecast PROVISIONAL — preorder retailer C completo all'82%; reconciliation attesa domani alle 18:00.**

Ora l'incertezza produce alternative operative reali: firmare subito, negoziare un'opzione di 24–48 ore oppure aspettare il dato maturo. La data quality non è più una footnote tecnica; diventa parte della reversibilità della decisione.

## La Decision Communication Pack

Per COO, CFO e Head of Logistics la Pack principale contiene una sola decision question: acquistare capacità temporanea e scegliere quale opzione. L'ask è autorizzare B **subordinatamente alla conferma del feed preorder**.

La headline può essere:

> **La capacità interna è fragile nello scenario centrale-alto; +18k pacchi/giorno coprono gran parte del rischio fino a P80 con un downside finanziario limitato rispetto al costo potenziale di under-capacity.**

Il decision layer rende visibili soltanto i dati che cambiano la scelta:

| Elemento | Valore |
|---|---:|
| Capacità interna affidabile | 148k/giorno |
| Forecast centrale | 162k/giorno |
| P80 | 171k/giorno |
| Capacità con B | 166k/giorno |
| Commitment B | €780k |
| Downside under-capacity scenario alto | €1,4M–€2,2M |
| Feed retailer C | 82% — PROVISIONAL |

L'evidence layer contiene forecast distribution vs capacità, confronto del downside A/B/C e switching condition. Il provenance layer conserva forecast version, timestamp, capacità per sito, contract terms, assunzioni sui costi SLA e storico degli errori di forecast.

### Il meeting usa la Pack per confrontare alternative

Il CFO chiede perché non aspettare 36 ore. La risposta non è “perché il forecast è alto”, ma: **possiamo aspettare se il carrier mantiene l'opzione senza repricing; se la finestra commerciale chiude oggi, il costo potenziale di perdere capacità può superare il valore informativo del feed mancante**. Procurement deve quindi chiarire proprio quel vincolo.

Il COO chiede perché non comprare 30k e stare tranquilli. La risposta torna al ranking: C aggiunge **€460k** di commitment rispetto a B e migliora poco il downside nei futuri plausibili attuali; diventa interessante solo con un picco molto più alto del P80 corrente.

La discussione rimane così sulle alternative e sulle soglie invece di tornare al catalogo dei KPI.

### La decisione

Procurement ottiene un'opzione di **24 ore senza repricing**. Il management sceglie di attendere la reconciliation mantenendo riservata B, firmare se il forecast maturo resta sopra la switching condition e rivalutare C soltanto se il nuovo P80 supera la capacità di B oltre la safety margin concordata.

Il giorno successivo il forecast viene aggiornato e la scelta effettiva torna nel Decision Record.

La dashboard originale conteneva più dati. La nuova Pack contiene **più decisione** perché mette nella stessa superficie forecast, capacità, downside, maturity e switching value.

> **Data storytelling non significa trasformare i dati in una storia convincente. Significa costruire un percorso di evidenze che consenta al destinatario di scegliere senza perdere il significato, l'incertezza e le alternative contenute nell'analisi originale.**
