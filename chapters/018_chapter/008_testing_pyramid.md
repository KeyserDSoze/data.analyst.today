## 18.7 Testing pyramid: proteggere struttura, significato e decisione

Un singolo test non può garantire la qualità di un prodotto analitico perché gli errori nascono a livelli differenti.

Possiamo avere:

- schema rotto;
- duplicazione;
- join errato;
- volume incompleto;
- mapping sbagliato;
- metrica semanticamente diversa;
- series discontinuity;
- prodotto perfettamente corretto ma non più adatto alla decisione.

Per questo è utile una **testing pyramid**.

La metafora della piramide indica due cose:

1. alla base abbiamo molti controlli economici, frequenti e automatizzabili;
2. salendo abbiamo controlli meno numerosi, più costosi e più vicini al significato business.

La piramide non è una garanzia matematica.

È una strategia di difesa ridondante.

## Livello 0 — Source contract checks

Prima della trasformazione verifichiamo se la sorgente mantiene la propria promessa.

Esempi:

- partition arrivata;
- schema/versione attesi;
- primary identifier presente;
- source count;
- source freshness;
- required fields;
- event/version compatibility.

Questi controlli separano:

> “la trasformazione è sbagliata”

da

> “la sorgente non ha consegnato ciò che ci aspettavamo”.

## Livello 1 — Structural tests

Sono economici e numerosi.

Controllano:

- tipo;
- not null;
- uniqueness;
- accepted values;
- referential integrity;
- grain invariants;
- schema compatibility.

Sono necessari.

Non sono sufficienti.

Una tabella può rispettare perfettamente lo schema e duplicare revenue del 40%.

## Livello 2 — Transformation invariants

Qui testiamo proprietà della logica.

Esempi:

- una riga ordine non può generare due righe fatturabili senza una ragione esplicita;
- `net_revenue ≤ gross_revenue` in un contesto definito;
- opening balance + movements = closing balance;
- un cliente non può appartenere contemporaneamente a due segmenti esclusivi;
- il numero di righe dopo un join non può crescere oltre una soglia attesa.

Questi test iniziano a proteggere il **modello mentale** oltre allo schema.

## Livello 3 — Reconciliation tests

Confrontiamo output con una fonte o una vista indipendente.

Esempi:

- warehouse revenue vs ledger;
- completed orders vs captured payments;
- invoice total vs line-item aggregation;
- inventory snapshot vs operational source;
- payout total vs payment provider.

La reconciliation è potente perché verifica una proprietà di business end-to-end.

Per prodotti T3 può essere un blocking gate.

Per prodotti T1 può essere una review periodica.

## Livello 4 — Distribution and behavioral tests

Controllano se il dato si comporta in modo plausibile:

- volume;
- null rate;
- cardinalità;
- distribuzione;
- percentili;
- mix;
- drift;
- seasonal baseline;
- source contribution.

Questi controlli spesso devono distinguere **anomalia** da **errore**.

Una campagna può davvero raddoppiare il traffico.

Un'acquisizione può cambiare customer mix.

Per questo molti distribution test dovrebbero generare:

- `WARN`;
- investigation;
- contextual gate;

non sempre un blocco automatico.

## Livello 5 — Semantic tests

Qui chiediamo se il dato continua a rappresentare ciò che il business pensa.

Esempi:

- il denominatore della conversion è ancora valido?
- `completed_order` significa ancora la stessa cosa?
- gli account sospesi entrano nel churn?
- `revenue_date` è order, invoice o recognition date?
- la nuova trial policy rende comparabile la serie?
- il mapping di prodotto riflette ancora la nuova organizzazione?

Questi test sono più difficili perché richiedono conoscenza del dominio.

Alcuni possono essere automatizzati come invariant.

Altri richiedono una review nel change process.

## Caso simulato/composito: tutti i test tecnici verdi

Un retailer monitora `cancellation_rate`.

Passano:

- schema;
- not-null;
- accepted values;
- volume;
- range storico.

Durante un cambio operativo gli ordini bloccati automaticamente per frode passano da:

`cancelled`

a

`closed_by_system`.

Il cancellation rate appare migliorato.

Il numero non contiene un bug sintattico.

È cambiata la classificazione del fenomeno.

Un controllo semantico del tipo:

> “quale quota di ordini termina senza fulfillment, indipendentemente dalla label?”

avrebbe reso visibile la discontinuità.

## Livello 6 — Consumer / decision tests

Il livello più alto verifica se il prodotto continua a servire il processo per cui è stato costruito.

Esempi:

- il dashboard permette ancora di prendere la decisione prima della deadline?
- la metric definition è compresa dai consumer?
- il nuovo flow operativo ha reso obsoleto un KPI?
- un threshold continua a essere coerente con il nuovo denominatore?
- il report contiene tutte le alternative richieste dal Decision Record?

Questi controlli possono includere:

- UAT;
- business-owner review;
- scenario walkthrough;
- periodic fit-for-purpose review.

Una dashboard può passare tutti i test dati ed essere comunque **decisionally obsolete**.

## Livello 7 — Recovery tests

Un sistema non è davvero affidabile soltanto perché sa rilevare errori.

Deve sapere recuperare.

Per prodotti critici testiamo anche:

- replay;
- backfill;
- restore;
- fallback source;
- stale snapshot;
- rollback;
- re-certification.

La domanda è:

> **“Abbiamo mai provato il recovery prima di averne bisogno?”**

Google SRE tratta testing e recovery come parte della reliability engineering, non come attività separate dal funzionamento del servizio.

Fonte: https://sre.google/sre-book/testing-reliability/

## Blocking, warning e informational

Un test senza una policy di risposta è soltanto un numero.

Ogni controllo dovrebbe avere una disposition.

### BLOCKING

Il prodotto non può essere certificato.

Esempi:

- Finance reconciliation T3 fuori tolerance;
- chiave critica duplicata;
- fonte materialmente incompleta;
- semantic contract incompatibile.

### WARNING

Il prodotto può essere servito con caveat o richiede investigation.

Esempi:

- mix anomalo;
- volume sopra baseline;
- freshness vicina alla soglia.

### INFORMATIONAL

Trend utile per capacity/maintenance, senza azione immediata.

Questo evita che tutto diventi rosso.

## Test coverage deve seguire il failure mode, non le colonne

Una metrica comune nella software engineering è code coverage.

Nell'analytics una misura più utile è spesso **failure-mode coverage**.

Chiediamo:

- quali errori materialmente pericolosi conosciamo?
- quale test li intercetta?
- a quale livello?
- prima o dopo la pubblicazione?
- esiste un gap?

Esempio:

| Failure mode | Controllo | Gate |
|---|---|---|
| store POS mancante | source coverage | BLOCK |
| revenue duplicated by join | reconciliation | BLOCK |
| unusual category mix | distribution | WARN |
| active-customer definition changed | semantic change review | BLOCK |
| report no longer used | adoption review | RETIRE candidate |

La testing strategy è più forte quando nasce dai rischi della decisione.

## Test ownership

Anche i test hanno owner.

Un test può diventare obsoleto.

Una threshold può non riflettere più il business.

Per prodotti critici dovremmo sapere:

- chi approva il test;
- chi modifica la threshold;
- quale failure mode protegge;
- quando è stato rivisto;
- quale azione genera.

Un alert ignorato per sei mesi non è più un controllo.

## False positive e false negative dei controlli

Se un quality test genera continuamente falsi allarmi, il team lo bypasserà.

Se è troppo permissivo, dà falsa fiducia.

La threshold deve essere calibrata rispetto a:

- variabilità naturale;
- stagionalità;
- business events;
- costo di investigation;
- costo di pubblicare dato sbagliato.

Anche la data quality ha una decision theory implicita.

## Testing pyramid per tier

### T0

- controlli esplorativi;
- sanity check manuali.

### T1

- structural;
- basic invariants;
- freshness;
- owner review.

### T2

- source contract;
- structural;
- invariants;
- reconciliation;
- distribution;
- semantic gate;
- post-deploy verification.

### T3

- tutto ciò che è materialmente necessario;
- independent reconciliation;
- controlled change;
- recovery test;
- audit evidence.

Il numero di test non determina la maturità.

La maturità è coprire i failure mode che contano senza creare una macchina di alert inutili.

> **La data quality non è una batteria di test verdi. È una rete di evidenze che rende difficile a un errore materialmente importante attraversare tutti i livelli e arrivare indisturbato alla decisione.**
