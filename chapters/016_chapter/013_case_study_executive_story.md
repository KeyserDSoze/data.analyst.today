## 16.12 Caso studio — Dalla dashboard di picco alla decisione sulla capacità

**Caso simulato/composito.** Numeri, azienda e circostanze sono costruiti per la didattica.

## Il contesto

NorthRiver Logistics gestisce fulfilment e consegna per diversi retailer europei.

A sei settimane dal picco natalizio, il team operations deve decidere se acquistare **capacità temporanea aggiuntiva da un carrier esterno**.

Il contratto richiede un commitment minimo di €780.000.

La domanda non è:

> “Come sta andando la logistica?”

È:

> **“Dobbiamo comprare ora capacità aggiuntiva, e quanta?”**

## Il Decision Record disponibile

L'analisi produce tre alternative:

### A — Nessuna capacità extra

- costo incrementale: €0;
- rischio elevato di backlog se il forecast supera P50;
- alta esposizione a penali e ritardi.

### B — Capacità extra per 18.000 pacchi/giorno

- commitment: €780k;
- copertura sufficiente fino a uno scenario vicino a P80;
- parte della capacità può restare inutilizzata nello scenario basso.

### C — Capacità extra per 30.000 pacchi/giorno

- commitment: €1,24M;
- copertura molto ampia;
- rischio alto di overcapacity.

Recommendation analytics: **B**, con opzione di espansione contrattuale se due indicatori anticipatori superano soglia.

## La dashboard originale

La pagina preparata per il COO contiene:

- volumi giornalieri;
- forecast per deposito;
- forecast accuracy;
- backlog;
- cost per parcel;
- carrier utilization;
- SLA;
- overtime;
- staffing;
- weather;
- 13 filtri;
- due mappe;
- una tabella con 47 righe.

Tutto è utile a qualcuno.

Il COO però non riesce a capire in pochi minuti se deve firmare il contratto da €780k.

## Errore 1 — Mostrare il forecast senza la capacità

Il primo grafico mostra una previsione di picco a 162.000 pacchi/giorno.

Senza la linea di capacità interna, il numero non ha significato decisionale.

La prima visualizzazione viene quindi ridisegnata:

- forecast centrale;
- prediction interval P20–P80;
- capacità interna affidabile: 148.000 pacchi/giorno;
- capacità con opzione B: 166.000;
- data limite per attivare il contratto.

Titolo:

> **La capacità interna copre lo scenario centrale solo marginalmente; l'opzione B copre il picco fino a circa P80.**

Il visual non dice “comprate B”. Mostra il trade-off che rende B plausibile.

## Errore 2 — Nascondere l'asimmetria dei costi

La dashboard originale mostra `cost per parcel`, ma non mostra quanto costano gli errori opposti.

L'analisi stima:

### Under-capacity

Possibili effetti:

- penali SLA;
- expedited shipping;
- overtime;
- cancellazioni;
- customer support;
- rischio reputazionale.

Nello scenario centrale alto, il costo incrementale stimato è €1,4M–€2,2M.

### Over-capacity

Se la domanda resta bassa, parte del commitment da €780k non verrà utilizzata.

Il downside è più visibile e contrattualmente limitato.

La seconda pagina executive mostra quindi **downside asimmetrico**, non altri KPI operativi.

## Errore 3 — Forecast interval senza switching value

Dire:

> “Il P80 è 171.000 pacchi/giorno”

non basta.

Il Decision Record identifica il punto in cui B perde convenienza:

> se il picco aggiornato atteso scende sotto circa 151.000 pacchi/giorno e i costi di under-capacity restano sotto la stima base, il commitment non è più giustificato.

Questo valore entra nella Decision Communication Pack come **switching condition**.

## Errore 4 — Nessuna data maturity

Il forecast dipende anche dai preorder di tre retailer.

Uno dei feed è incompleto e verrà riconciliato entro 36 ore.

La prima dashboard non lo mostra.

La nuova pagina dice:

> **Forecast provisional: preorder retailer C completo all'82%; refresh finale atteso domani alle 18:00.**

Il COO può quindi decidere se:

- firmare subito;
- negoziare un'opzione di 48 ore;
- aspettare il feed finale.

L'incertezza viene collegata alla reversibilità.

## La Decision Communication Pack

### Audience

COO, CFO, Head of Logistics.

### Decision question

Acquistare capacità temporanea per il picco e quale opzione scegliere.

### Decision requested

Autorizzare l'opzione B, subordinata alla conferma del feed preorder entro 36 ore.

### Headline

> **La capacità interna è fragile nello scenario di domanda centrale-alto; 18.000 pacchi/giorno aggiuntivi coprono il rischio fino a circa P80 con downside finanziario limitato rispetto al costo potenziale di under-capacity.**

### Primary evidence

1. forecast distribution vs capacità;
2. costo under-capacity vs commitment;
3. scenario table A/B/C;
4. switching condition e data maturity.

### Caveat decision-critical

Feed preorder retailer C incompleto.

### Guardrail

Rivalutare se il forecast reconciliato scende sotto la switching condition.

### Provenance

- forecast version;
- timestamp;
- capacità affidabile per sito;
- contract terms;
- assunzioni sui costi SLA;
- appendix con forecast error storico.

## La prima slide

Non dice:

> “Peak readiness dashboard.”

Dice:

> **Decisione oggi: riservare 18k pacchi/giorno di capacità temporanea, con conferma finale dopo la reconciliation preorder.**

Sotto compaiono soltanto:

- capacità interna: 148k/giorno;
- forecast centrale: 162k;
- P80: 171k;
- capacità con B: 166k;
- commitment: €780k;
- under-capacity downside stimato nello scenario alto: €1,4–2,2M;
- caveat: feed retailer C all'82%.

## Il meeting

Il CFO chiede:

> “Perché non aspettare 36 ore?”

La risposta non è “perché il forecast è alto”.

È:

> “Possiamo aspettare se il carrier mantiene l'opzione senza repricing. Se la finestra commerciale chiude oggi, il costo di perdere la capacità è superiore al valore informativo atteso dal feed mancante. Sto verificando questo vincolo con procurement.”

Il COO chiede:

> “Perché non comprare 30k e stare tranquilli?”

La risposta:

> “L'opzione C migliora poco il downside nei nostri scenari plausibili ma aggiunge €460k di commitment. B resta la soluzione dominante fino a un picco molto più alto del P80 attuale.”

La comunicazione porta quindi il meeting sulle **alternative e sui threshold**, non sul catalogo dei KPI.

## La decisione

Procurement ottiene un'opzione di 24 ore senza repricing.

Il management sceglie:

1. attendere la reconciliation;
2. mantenere riservata B;
3. firmare se il forecast reconciliato resta sopra la switching condition;
4. rivalutare C soltanto se il nuovo P80 supera la capacità di B di oltre la safety margin concordata.

Il giorno successivo il forecast viene aggiornato e la decisione viene registrata nel Decision Record.

## La lezione

La dashboard originale conteneva più dati.

La Decision Communication Pack conteneva **più decisione**.

Il valore è nato da:

- partire dal Decision Record;
- mostrare forecast e capacità nella stessa grammatica;
- rendere visibile l'asimmetria dei costi;
- comunicare la maturity del dato;
- mostrare lo switching value;
- mantenere l'alternativa C visibile senza darle salienza indebita;
- collegare il caveat a una scelta reversibile.

> **Data storytelling non significa trasformare i dati in una storia convincente. Significa costruire un percorso di evidenze che consenta al destinatario di scegliere senza perdere il significato, l'incertezza e le alternative contenute nell'analisi originale.**
