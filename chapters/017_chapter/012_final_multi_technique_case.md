## 17.11 Caso finale: “La crescita è sana?”

### Caso simulato/composito: OrbisMarket

OrbisMarket è un marketplace europeo con circa 9 milioni di ordini annui.

Nel Q3 il board riceve questi numeri:

- GMV: `+7%`;
- net revenue: `+4%`;
- contribution margin: `-13%`;
- repeat purchase rate: `-3,4 pp`;
- delivery complaints: `+22%`;
- nuovi seller: `+31%`;
- marketing spend: `+18%`.

Il CEO non chiede:

> “Quale tecnica dobbiamo usare?”

Chiede:

> **“La crescita è sana, e cosa dobbiamo cambiare prima del prossimo trimestre?”**

Prima di leggere oltre, proviamo a fermarci.

Con questi soli numeri potremmo immaginare molte storie:

- customer acquisition di qualità peggiore;
- seller mix più debole;
- logistica deteriorata;
- sconti eccessivi;
- refund in crescita;
- costi di pagamento;
- nuova contabilizzazione;
- crescita volutamente meno profittevole ma strategicamente sensata;
- più cause contemporaneamente.

La maturità analitica consiste nel non innamorarsi della prima spiegazione disponibile.

## Routing iniziale

Il Capstone Routing Canvas viene compilato prima di aprire SQL.

| Elemento | Scelta |
|---|---|
| Decisione | quali leve correggere e quali investimenti mantenere nel Q4 |
| Failure cost | tagliare crescita sana oppure continuare a scalare un meccanismo economicamente distruttivo |
| Claim necessario | diagnostico su driver principali; causale sulle leve che richiedono interventi costosi |
| Tempo | 10 giorni per il board, 72 ore per una prima triage |
| Reversibilità | diversa per marketing, seller policy, capacità logistica e pricing |
| Switching question | quale evidenza ci farebbe scegliere una leva diversa? |

### Deliverable candidati

Non vengono attivati automaticamente tutti gli artefatti del libro.

Il team seleziona inizialmente:

1. **Analytical Brief**;
2. **Data Readiness Review**;
3. **EDA Evidence Map**;
4. **Lifecycle Diagnostic Map**;
5. **Analytical Data Contract** per contribution margin;
6. **Decision Record**.

Gli altri restano condizionali.

Per esempio, il **Causal Identification Brief** entra soltanto se una decisione importante dipende da una relazione che i dati descrittivi non possono sostenere.

## 1. Definire “crescita sana”

La prima discussione con il management produce una definizione operativa.

Una crescita è considerata sufficientemente sana se:

- il contribution profit assoluto non viene eroso oltre la soglia approvata;
- la customer economics delle nuove coorti converge verso target;
- service quality non deteriora oltre guardrail;
- la crescita non dipende da incentivi che richiedono spesa crescente per unità di risultato;
- eventuali sacrifici di margine sono intenzionali, misurati e reversibili.

Questa definizione è importante perché evita di trasformare “GMV cresce” o “margin % scende” in verdetti automatici.

## 2. Data Readiness Review: il primo -13% non è ancora una verità decisionale

Prima di interpretare il contribution margin:

- Finance e Analytics riconciliano definizione e periodo;
- viene controllato il grain ordine/riga/spedizione;
- si verificano refund e cancellation timing;
- si confrontano event date e accounting date;
- si controllano nuovi seller fee e carrier surcharge;
- si verifica se il marketing cost è incluso nello stesso modo dei trimestri precedenti.

Emerge un cambio di timing nella contabilizzazione di alcuni refund.

Circa `1,5 pp` del deterioramento apparente derivano da comparabilità contabile, non da peggioramento economico corrente.

Il problema resta reale.

Ma il primo numero non aveva ancora il diritto di sostenere la conclusione iniziale.

### Stop rule

> **Nessun piano di taglio o investimento viene approvato usando il -13% grezzo.**

## 3. Decomposition: quali componenti stanno consumando margine?

Il delta residuo viene decomposto in:

- product margin;
- discount;
- shipping subsidy;
- refund;
- payment cost;
- support cost;
- seller incentive;
- marketing acquisition cost dove rilevante.

I driver principali risultano:

1. shipping subsidy;
2. refund;
3. mix verso seller e categorie con cost-to-serve più alto.

Gli sconti contribuiscono, ma non dominano.

Questa fase produce una visualizzazione con ruolo `orient`: un contribution-margin bridge.

## 4. Segmentazione: dove si concentra il deterioramento?

Il team non cerca il segmento con il grafico più spettacolare.

Costruisce una Evidence Map coerente con le ipotesi.

Il deterioramento è concentrato in:

- nuovi clienti acquisiti negli ultimi tre mesi;
- ordini bulky;
- due aree metropolitane;
- seller entrati dopo una recente espansione del catalogo.

Le nuove coorti hanno repeat rate inferiore, ma anche delivery service peggiore.

Quindi due spiegazioni inizialmente concorrenti — “marketing porta clienti peggiori” e “la logistica sta peggiorando” — possono essere collegate.

Il customer mix e la qualità del servizio non sono necessariamente fenomeni indipendenti.

## 5. Lifecycle Diagnostic Map: il problema continua dopo il checkout

Il team osserva il percorso:

**ordine → spedizione → consegna → eventuale reclamo/refund → secondo acquisto**

La retention a 60 giorni è molto peggiore tra clienti che ricevono la prima consegna oltre la promessa.

Questo è un finding importante.

Non è ancora un effetto causale.

Le aree con consegne peggiori possono avere:

- categorie diverse;
- seller diversi;
- customer mix diverso;
- ordini più pesanti;
- promise date differenti.

A questo punto il claim richiesto dalla decisione diventa più forte.

Se vogliamo spendere milioni in capacità o cambiare il routing, dobbiamo capire se migliorare delivery reliability può plausibilmente cambiare anche economics e repeat purchase.

## 6. Causal Identification Brief: solo ora entra la causalità

Il team cerca variation utile.

Una modifica operativa al consolidamento degli ordini è stata introdotta gradualmente in alcuni hub ma non in altri nello stesso momento.

Questo crea un'opportunità quasi-sperimentale.

Il team verifica:

- pre-trend;
- composizione degli hub;
- timing rollout;
- cambi concorrenti;
- spillover;
- definizione dell'esposizione;
- robustezza a specifiche alternative.

L'evidenza suggerisce che il nuovo schema abbia:

- aumentato delivery time di circa `0,8 giorni` negli ordini bulky più esposti;
- ridotto repeat purchase a 60 giorni di circa `2,1 pp` nel segmento più esposto.

Il team non scrive:

> “Abbiamo dimostrato che la logistica causa tutto il churn.”

Scrive:

> **“Il disegno quasi-sperimentale sostiene un effetto materialmente negativo del nuovo consolidamento su delivery time e repeat purchase nel segmento più esposto, pur con limiti di identificazione residui.”**

Il claim rimane proporzionato al design.

## 7. Temporal Decision Brief: quanto problema richiede capacità?

Operations propone una risposta semplice:

> “Aggiungiamo capacità ovunque.”

Il forecast mostra però che i picchi sono concentrati in finestre e hub specifici.

Una capacità fissa generalizzata costerebbe circa `€6,8M` annui.

Una combinazione di:

- capacità flessibile;
- routing alternativo;
- soglie di volume;
- promise date più realistiche;

ha costo atteso molto inferiore.

Il forecast entra quindi solo quando la domanda decisionale lo richiede: **quanta capacità, dove e quando?**

## 8. Experiment Contract: separare una buona idea da una buona policy

Il team identifica due interventi testabili:

### A — Surcharge selettivo

Sugli ordini bulky sotto una determinata soglia economica.

### B — Promise date realistica + routing alternativo

Con gestione diversa degli ordini ad alto rischio di ritardo.

Primary metric:

**contribution margin per visitatore**.

Guardrail:

- checkout conversion;
- cancellation;
- delivery time;
- refund;
- repeat purchase;
- customer complaint.

La variante B riduce leggermente la conversione iniziale ma migliora delivery reliability e valore atteso per cliente.

Questo è un esempio importante: una variante può “perdere” una metrica locale e migliorare il sistema complessivo.

## 9. Decision economics: le alternative reali

Il Decision Record confronta:

| Opzione | Costo annuo stimato | Effetto atteso | Reversibilità | Rischio principale |
|---|---:|---|---|---|
| Capacità fissa generalizzata | €6,8M | alta protezione picchi | bassa | overcapacity |
| Capacità flessibile + routing | €2,9M | effetto mirato | medio-alta | execution complexity |
| Solo surcharge | €0,4M | protegge margine | alta | conversion/customer perception |
| Status quo | ~€0 diretto | nessuna correzione | alta | deterioramento continua |

La scelta non è una singola opzione pura.

Il team raccomanda:

- capacità flessibile e routing nei nodi esposti;
- promise date più realistica;
- surcharge selettivo soltanto dove l'economia lo giustifica;
- stop condition su conversion e customer complaints;
- monitoraggio di repeat purchase e contribution margin.

## 10. Decision Communication Pack

La prima pagina del board non contiene dieci tecniche.

Contiene una decisione.

### Headline

> **“Dopo aver corretto un effetto contabile, il deterioramento del margine è concentrato negli ordini bulky e nelle nuove coorti di due aree. L'evidenza più forte collega una parte materiale del problema al nuovo consolidamento logistico. Un intervento mirato su routing, capacità flessibile e promise date ha rapporto impatto/costo migliore della capacità generalizzata.”**

### Evidence hierarchy

1. margin bridge;
2. concentration map;
3. lifecycle evidence;
4. quasi-experimental estimate con caveat;
5. capacity scenarios;
6. experiment result;
7. option economics.

### Decision requested

Approvare rollout progressivo del pacchetto mirato e non l'espansione fissa generalizzata.

### Switching condition

Rivalutare se:

- l'effetto operativo non si replica;
- costi flessibili superano soglia;
- repeat purchase non migliora;
- conversion loss da surcharge supera il beneficio economico;
- il mix Q4 cambia sostanzialmente.

## 11. Outcome review: separare decision quality e outcome luck

Dopo otto settimane:

- on-time delivery: `+6,7 pp`;
- contribution margin bulky: `+3,2 pp`;
- support contacts: `-11%`;
- repeat purchase nel segmento target: `+1,5 pp`;
- checkout conversion: `-0,3 pp`.

Il sistema non ottimizza ogni metrica.

Migliora il trade-off complessivo che il Decision Record aveva dichiarato rilevante.

Il team effettua comunque una review distinta:

### Qualità della decisione ex ante

- alternative considerate?
- evidenza proporzionata?
- downside espliciti?
- switching condition definite?

### Outcome ex post

- i meccanismi si sono mossi come previsto?
- quali assunzioni erano sbagliate?
- cosa aggiornare nel modello mentale?

Una buona decisione può avere un outcome sfavorevole per shock imprevisti. Una cattiva decisione può essere fortunata.

Il capstone deve insegnare entrambe le distinzioni.

## 12. Quali deliverable abbiamo usato davvero?

Nel caso OrbisMarket entrano:

- Analytical Brief;
- Analytical Data Contract;
- Data Readiness Review;
- EDA Evidence Map;
- Lifecycle Diagnostic Map;
- Causal Identification Brief;
- Temporal Decision Brief;
- Experiment Contract;
- Uncertainty Brief;
- Decision Record;
- Decision Communication Pack.

Non entrano automaticamente:

- Predictive Decision Card;
- Tooling Decision Record;
- Data Flow Architecture Map;
- AI Analysis Control Sheet.

Potrebbero diventare necessari in una diversa implementazione, ma non servono per rendere difendibile la decisione descritta.

Questa è la lezione finale del capitolo.

> **La maturità analitica non appare quando riusciamo a usare molte tecniche. Appare quando sappiamo quale sequenza di evidenze serve, quale claim possiamo sostenere e quale lavoro sarebbe soltanto complessità aggiuntiva.**
