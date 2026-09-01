## 13.14 Sintesi ed esercizi: scegliere è una decisione di design reversibile

Questo capitolo non assegna un vincitore tra spreadsheet, SQL, Python, R, notebook, BI, cloud, no-code e AI.

Costruisce un'abitudine diversa:

> **partire dalla responsabilità che il lavoro deve assumere e scegliere il minimo sistema capace di sostenerla.**

Lo stesso problema può cambiare strumento nel tempo perché cambiano:

- frequenza;
- scala;
- rischio;
- utenti;
- metodo;
- riproducibilità;
- ownership;
- dipendenze downstream.

Quindi la domanda non è soltanto:

> cosa usiamo?

È anche:

> **fino a quando questa scelta resta adeguata?**

### La catena del capitolo

```text
Decisione
→ problem shape
→ rischio e controlli
→ stage di maturità
→ alternative
→ TCO
→ ownership
→ scelta minima sufficiente
→ exit condition
→ review
```

Il risultato è il **Tooling Decision Record**.

### Cinque errori da riconoscere

**Tool-first thinking**  
Partire dalla tecnologia invece che dal bisogno.

**Premature industrialization**  
Costruire un prodotto prima di aver dimostrato valore o stabilizzato la domanda.

**Accidental production**  
Lasciare che un prototipo diventi critico senza una nuova design review.

**Local optimum**  
Scegliere il tool più comodo per il builder ignorando consumer, manutenzione e organizzazione.

**Sunk-cost tooling**  
Continuare con una soluzione inadeguata soltanto perché migrare sembra costoso.

L'AI può ridurre l'ultimo costo. Non elimina la necessità di verificare la migrazione.

---

## Esercizio 1 — La soluzione più semplice è un workbook?

**Caso simulato/composito.**

Una PMI riceve ogni mese quattro CSV da circa 25.000 righe ciascuno.

Il CFO vuole:

- consolidare ricavi;
- applicare cambi valuta;
- riconciliare con il ledger;
- produrre un report mensile;
- fare scenari budget.

Un consulente propone ingestion cloud, lakehouse, orchestrazione, semantic layer e dashboard enterprise.

### Compito

Costruisci un TDR che confronti almeno:

1. workbook + Power Query;
2. SQL database/warehouse leggero + workbook;
3. piattaforma enterprise proposta.

Devi dichiarare:

- scelta iniziale;
- livello di riproducibilità R0-R4;
- controlli minimi;
- owner;
- tre **exit condition** che obbligherebbero a riesaminare il workbook.

Non ricevi punti aggiuntivi per scegliere la soluzione più tecnologica.

---

## Esercizio 2 — Public Health England: quando un componente supera il suo contesto

Nel 2020 Public Health England comunicò che **15.841 casi positivi** erano rimasti fuori dalle statistiche giornaliere per un problema tecnico nel processo di caricamento; reporting contemporaneo collegò il failure mode al modo in cui venivano usati file/template Excel.[^phe-exercise]

### Domande

1. Perché la lezione non è semplicemente “non usare Excel”?  
2. Quali **exit condition** avrebbero potuto segnalare che il componente stava diventando critico?  
3. Quali dimensioni del TDR cambiano quando il dato influenza contact tracing nazionale?  
4. Quali controlli di volume/completeness avrebbero potuto rendere visibile il failure prima della pubblicazione?  
5. Che cosa distingue un tool appropriato da un **hidden production system**?

---

## Esercizio 3 — Il notebook diventato servizio

**Caso simulato/composito.**

Un notebook Python identifica ogni lunedì account a rischio churn.

All'inizio lo usa un analyst.

Sei mesi dopo:

- alimenta 60 Customer Success Manager;
- influenza €18 milioni di ARR;
- deve essere pronto entro le 07:00;
- fallisce una volta ogni tre settimane;
- usa credenziali locali;
- non esiste alert;
- la lista viene importata manualmente nel CRM.

### Compito

1. Classifica il processo da P0 a P3.  
2. Elenca i nuovi obblighi comparsi.  
3. Progetta una migrazione incrementale: cosa lasci nel notebook e cosa estrai per primo?  
4. Definisci un **shadow run/parity test**.  
5. Scrivi il nuovo TDR e il rollback.  
6. Indica quale parte appartiene al Capitolo 10 e quale al tool/production design.

---

## Esercizio 4 — SQL, Python o tutti e due?

**Caso simulato/composito.**

Un retailer deve produrre feature di comportamento da 4 miliardi di eventi già presenti nel warehouse e poi stimare un modello di propensity.

Un analyst propone di esportare tutto in pandas perché conosce meglio Python.

Un altro propone di implementare anche il modello interamente in SQL perché “così non esce niente dal warehouse”.

### Compito

Costruisci una strategia **pushdown / pull-out**:

- quali trasformazioni fai nel motore dati;
- qual è il grain del dataset che esce;
- quali calcoli appartengono all'ambiente modellistico;
- dove ritorna l'output;
- come eviti copie inutili;
- come verifichi semantic parity.

Nel TDR spiega perché **nessuna delle due preferenze personali** è una motivazione sufficiente.

---

## Esercizio 5 — Il workflow no-code da 170 blocchi

**Caso simulato/composito.**

Un workflow integra CRM, advertising, email e billing.

Ha:

- 170 blocchi;
- 14 branch;
- quattro persone che lo modificano;
- nessun version control affidabile;
- 35 ore mensili di manutenzione;
- licenza €250/mese.

Assumi un costo interno medio di €65/ora.

### Compito

1. Calcola almeno il costo annuale di licenza + manutenzione.  
2. Elenca altre voci TCO da stimare.  
3. Proponi un **complexity budget**.  
4. Decidi se fare big rewrite o migrazione incrementale e difendi la scelta.  
5. Scrivi tre exit condition che il team avrebbe dovuto dichiarare quando il workflow era ancora piccolo.

---

## Esercizio 6 — Reproducible Analytical Pipeline

La Government Analysis Function del Regno Unito promuove le Reproducible Analytical Pipelines per ridurre passaggi manuali e aumentare riproducibilità, auditabilità, efficienza e quality assurance.[^rap-exercise]

### Scenario

Un ente produce ogni mese un indicatore pubblico mediante:

```text
CSV ricevuto via email
→ pulizia manuale
→ workbook
→ copia/incolla in presentazione
→ pubblicazione
```

### Compito

1. Assegna il livello di riproducibilità R0-R4 attuale.  
2. Progetta una transizione a R2, poi R3, poi R4.  
3. Per ogni passaggio indica **quale beneficio ottieni e quale costo introduci**.  
4. Spiega perché “riscrivere tutto in Python” non è automaticamente la risposta corretta.  
5. Quale parte del workflow dovrebbe essere versionata? Quale dato deve invece essere identificabile senza stare necessariamente in Git?

---

## Esercizio 7 — Dashboard o risposta domani mattina?

**Caso simulato/composito.**

Il direttore commerciale chiede:

> Quali 20 account hanno perso più pipeline rispetto allo stesso trimestre dell'anno scorso?

La risposta serve domani alle 09:00.

Non è chiaro se la domanda verrà mai ripetuta.

### Compito

Confronta:

- query + tabella annotata;
- notebook;
- dashboard BI.

Nel TDR devi includere:

- time-to-first-reliable-evidence;
- costo dell'attesa;
- soluzione più reversibile;
- condizione che giustificherebbe successivamente il dashboard.

---

## Esercizio 8 — Caso completo: Aurora Health Devices

**Caso simulato/composito.**

Aurora vende dispositivi medicali B2B in 17 paesi.

La direzione vuole identificare account a rischio di mancato rinnovo.

Contesto:

- CRM SaaS;
- billing ERP;
- usage telemetry cloud;
- ticketing SaaS;
- 24.000 account;
- 400 milioni di usage event al mese;
- 32 account manager;
- capacità operativa: circa 600 interventi al mese;
- score sufficiente una volta al giorno;
- dati cliente soggetti a controlli di accesso;
- primo proof of value richiesto in sei settimane.

Il team considera:

**A.** export mensile completo in spreadsheet;

**B.** tutta la logica nel BI tool;

**C.** dataset condivisi in SQL, Python per il modello, score pubblicato in tabella certificata e BI/CRM per il consumo;

**D.** piattaforma streaming che aggiorna lo score ogni minuto;

**E.** nessun modello per ora: semplice regola di usage decline + valore account, testata come baseline.

### Compito finale

Costruisci un **Tooling Decision Record completo** con:

```text
decision / action
stage P0-P3
data location and scale
frequency / freshness
method required
baseline
consumers
risk
reproducibility R0-R4
candidate comparison
chosen design
TCO categories
ownership / bus factor
controls
why simpler is insufficient OR sufficient
why more complex is premature
promotion gate
exit conditions
review date
```

Poi rispondi a tre domande.

1. **Qual è la soluzione minima che permette di imparare se la prioritizzazione crea valore?**  
2. **Quale parte industrializzeresti solo dopo il proof of value?**  
3. **Quale evidenza ti farebbe decidere di non costruire affatto il modello ML?**

La risposta migliore potrebbe non essere C dal primo giorno.

Per esempio, E può essere una baseline molto economica e informativa. Se una regola semplice produce già una buona prioritizzazione e il limite principale è la capacità di intervento, un modello più sofisticato deve dimostrare valore incrementale prima di meritare il suo TCO.

Questa è precisamente la disciplina del capitolo.

## Tooling Decision Record — template finale

```text
TOOLING DECISION RECORD

Decision / use case:
Business owner:
Current stage: explore | prototype | recurring | production
Decision deadline:
Expected solution lifetime:

Data location:
Input scale / growth:
Sources:
Frequency:
Freshness:
Method:
Human interaction:
Downstream consumers:

Impact if wrong:
Impact if late/unavailable:
Sensitive data:
Reproducibility: R0-R4
Audit/recovery requirement:

Builder:
Long-term owner:
Reviewers:
Bus factor:
Platform support:

Candidates considered:
- do nothing / manual
- existing process
- ...

Chosen tool / combination:
Responsibility of each component:
Why sufficient now:
Why simpler is insufficient:
Why more complex is premature:
Known limitations:
Required controls:

TCO:
- build
- run
- maintenance
- coordination
- skills
- reliability
- migration
- expected error
- delay

EXIT CONDITION:
Review if ...

Review date:
```

## Chiusura del capitolo

Un buon Data Analyst non deve essere neutrale rispetto agli strumenti.

Deve conoscerne abbastanza bene proprietà, limiti e costi da saper scegliere.

Ma non deve trasformare quella conoscenza in identità:

> sono un analyst Excel.  
> sono un analyst Python.  
> faccio tutto in SQL.  
> tutto deve stare nel cloud.

Queste frasi descrivono un'abitudine, non un metodo.

Il metodo professionale è:

**problema → requisiti → alternativa minima → verifica → ownership → exit condition**.

> **La maturità analitica non consiste nell'usare più tecnologia. Consiste nel sapere quanta tecnologia comprare oggi, quale complessità rimandare e quale segnale ci dirà che è arrivato il momento di cambiare.**

[^phe-exercise]: Public Health England, *PHE statement on delayed reporting of COVID-19 cases*, https://www.gov.uk/government/news/phe-statement-on-delayed-reporting-of-covid-19-cases
[^rap-exercise]: UK Government Analysis Function, *Reproducible Analytical Pipelines (RAP)*, https://analysisfunction.civilservice.gov.uk/reproducible-analytical-pipelines/
