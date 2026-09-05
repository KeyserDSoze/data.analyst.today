## 18.7 Testing strategy: proteggere struttura, significato e decisione

Un singolo test non può garantire la qualità di un prodotto analitico perché gli errori nascono a livelli differenti. Possiamo avere schema rotto, duplicazione, join errato, volume incompleto, mapping sbagliato, semantic drift, serie storica non più comparabile o un prodotto perfettamente corretto che non serve più la decisione per cui era stato costruito.

Per questo la testing strategy deve essere letta come una **difesa a strati**. La metafora della piramide resta utile: alla base abbiamo controlli economici e frequenti; salendo, i test diventano meno numerosi, più costosi e più vicini al significato business. Ma la misura della maturità non è il numero di test. È la **failure-mode coverage**: quali errori materialmente pericolosi conosciamo e quale strato li ferma prima che raggiungano il consumer?

## Dalla sorgente al significato

Il primo strato sono i **source contract checks**: partition arrivata, schema atteso, identifier, source count, freshness, required fields e compatibilità di versione. Servono a separare un errore di trasformazione da una sorgente che non ha consegnato ciò che prometteva.

Seguono gli **structural tests**: tipo, not null, uniqueness, accepted values, referential integrity e grain invariant. Sono economici e necessari, ma proteggono la forma del dato, non la sua verità economica. Una tabella può rispettare perfettamente lo schema e duplicare revenue del 40%.

Gli **invariant di trasformazione** iniziano a proteggere il modello mentale: una riga d'ordine non può generare due righe fatturabili senza una ragione, `net_revenue ≤ gross_revenue` nel contesto definito, opening balance + movements = closing balance, un customer non appartiene contemporaneamente a segmenti esclusivi, una join non può espandere righe oltre una soglia attesa.

Poi arriva la **reconciliation**, spesso il gate più forte perché confronta l'output con una vista indipendente: warehouse revenue vs ledger, completed orders vs captured payments, invoice total vs line item, inventory snapshot vs operational source. Per un prodotto T3 può essere blocking; per T1 può bastare una review periodica. Il principio non cambia: un controllo end-to-end cattura failure che molti test locali non possono vedere.

## Distribution test: anomalia non significa errore

Volume, null rate, cardinalità, distribuzioni, percentili, mix, drift e seasonal baseline aiutano a rilevare cambiamenti che meritano attenzione. Ma una campagna può davvero raddoppiare il traffico e un'acquisizione può cambiare customer mix. Per questo molti distribution test devono generare `WARN` o investigation, non blocco automatico.

La soglia dipende dalla variabilità naturale e dal costo dei due errori: pubblicare un dato sbagliato oppure interrompere inutilmente il servizio. Anche la data quality contiene una decision theory implicita.

## Il test più difficile: il dato significa ancora la stessa cosa?

I **semantic tests** chiedono se il prodotto rappresenti ancora ciò che il business pensa. Il denominatore della conversion è ancora valido? `completed_order` significa la stessa cosa? Gli account sospesi entrano nel churn? `revenue_date` è order, invoice o recognition date? Una nuova trial policy rende ancora comparabile la serie?

Un retailer monitora `cancellation_rate`. Schema, not-null, accepted values, volume e range storico sono tutti verdi. Durante un cambio operativo, però, gli ordini bloccati per frode passano dalla label `cancelled` a `closed_by_system`. Il KPI sembra migliorare. Non c'è un bug sintattico; è cambiata la classificazione del fenomeno.

Un invariant semantico più robusto — “quale quota di ordini termina senza fulfillment, indipendentemente dalla label?” — avrebbe reso visibile la discontinuità. Questo esempio spiega perché il test deve nascere dal failure mode, non dalla colonna disponibile.

## Consumer e decision test: anche un prodotto corretto può diventare obsoleto

Al livello più alto chiediamo se il prodotto continua a servire il processo per cui esiste. Arriva prima della deadline? I consumer comprendono metrica e caveat? Un nuovo workflow rende obsoleto il KPI? I threshold sono ancora coerenti con il denominatore? Il report contiene ancora le informazioni necessarie alla decisione?

Questi controlli possono essere UAT, business-owner review, scenario walkthrough o fit-for-purpose review periodica. Sono meno automatizzabili, ma proteggono un failure mode che nessun schema test può catturare: **la decisione è cambiata mentre il prodotto è rimasto fermo**.

## Recovery test: rilevare non basta

Un sistema critico deve anche dimostrare di saper recuperare. Replay, backfill, restore, fallback source, stale snapshot, rollback e re-certification non dovrebbero essere procedure provate per la prima volta durante un incidente. Google SRE tratta testing e recovery come parti della reliability engineering.

Fonte: https://sre.google/sre-book/testing-reliability/

La domanda operativa è:

> **Abbiamo mai provato il recovery prima di averne bisogno?**

## Ogni test deve avere una disposition

Un test senza policy di risposta è un numero in più. Gli stati devono essere chiari.

- `BLOCKING`: il prodotto non può essere certificato. Esempi: Finance reconciliation T3 fuori tolerance, chiave critica duplicata, source coverage materialmente incompleta, semantic contract incompatibile.
- `WARNING`: il prodotto può essere servito con caveat o richiede investigation. Esempi: mix anomalo, volume sopra baseline, freshness vicina alla soglia.
- `INFORMATIONAL`: segnale utile a trend o manutenzione, senza azione immediata.

Questa distinzione riduce alert fatigue e impedisce che tutto diventi rosso.

## Failure-mode coverage: la vera matrice di test

Una testing strategy matura parte dai rischi della decisione:

| Failure mode | Controllo | Gate |
|---|---|---|
| store POS mancante | source coverage | BLOCK |
| revenue duplicata da join | reconciliation | BLOCK |
| category mix insolito | distribution | WARN |
| `active_customer` ridefinito | semantic change review | BLOCK |
| report non più usato | adoption review | RETIRE candidate |

Questa tabella è più utile di una percentuale astratta di coverage. Dice che cosa stiamo proteggendo, dove lo intercettiamo e quale azione segue.

Anche i test hanno owner e lifecycle. Una threshold può diventare obsoleta, un alert può generare falsi positivi per mesi, un invariant può non rappresentare più il processo. Per prodotti critici dobbiamo sapere chi approva il test, quale failure mode copre, chi modifica la soglia e quale azione genera. Un alert ignorato da sei mesi non è più un controllo.

## Profondità per tier

T0 può vivere con sanity check esplorativi. T1 aggiunge structural test, basic invariant e freshness. T2 richiede source contract, invariant, reconciliation, distribution, semantic gate e post-deploy verification. T3 aggiunge tutto ciò che è materialmente necessario, inclusi independent reconciliation, controlled change, recovery test e audit evidence.

La regola resta la stessa del capitolo: **il failure cost determina il controllo**, non il desiderio di costruire una piattaforma sofisticata.

> **La data quality non è una batteria di test verdi. È una rete di evidenze che rende difficile a un errore materialmente importante attraversare tutti i livelli e arrivare indisturbato alla decisione.**

Una rete di controlli affidabile ha però un costo. Il passo successivo è rendere leggibile quanto paghiamo per mantenere quella promessa e se il service level acquistato crea davvero valore.