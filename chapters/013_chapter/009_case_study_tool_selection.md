## 13.8 Case study — Northstar Mobility: il problema non è scegliere un tool, ma progettare il flusso
Northstar Mobility gestisce servizi di mobilità urbana in 14 città europee.

Il COO chiede un sistema per monitorare ogni mattina:

- corse completate;
- cancellazioni;
- disponibilità mezzi;
- incidenti;
- revenue per città;
- customer support backlog.

In più, il team Operations vuole poter investigare rapidamente anomalie locali.

Il primo dibattito interno parte male.

Una persona propone Excel perché «tutti lo sanno usare». Un'altra vuole Python perché «è più professionale». Il team BI vuole costruire tutto in Power BI. Data Engineering propone un nuovo streaming layer.

Tutti stanno parlando dello strumento prima di aver scomposto il problema.

## 13.8.1 Scomporre la domanda

Il team analytics definisce quattro bisogni distinti.

### Bisogno A — KPI ufficiali giornalieri

Serve un set stabile di metriche, aggiornato entro le 7:30.

### Bisogno B — investigazione ad hoc

Gli analyst devono poter esplorare città, fasce orarie, vehicle type e cause di cancellazione.

### Bisogno C — alert operativo

Se la disponibilità mezzi in una città scende sotto una soglia, Operations deve ricevere un alert rapidamente.

### Bisogno D — analisi mensile profonda

Ogni mese il team Strategy studia retention, pricing, elasticità e performance per coorte.

Quattro bisogni diversi non richiedono necessariamente un unico strumento.

## 13.8.2 La prima architettura proposta: tutto in Excel

Il team Operations propone di esportare ogni mattina i dati in un workbook centrale.

### Vantaggi

- familiarità;
- rapidità iniziale;
- facile modifica manuale.

### Problemi

- milioni di eventi;
- refresh fragile;
- versioning debole;
- accesso concorrente;
- KPI duplicabili;
- difficile gestione di alert;
- rischio di copie locali.

Excel rimane utile per scenari e prototipi, ma non come backbone.

## 13.8.3 La seconda proposta: tutto in Python

Un data scientist propone notebook Python per KPI, alert e report.

### Vantaggi

- flessibilità;
- automazione;
- analisi avanzata.

### Problemi

- consumo difficile per utenti business;
- semantic definitions sparse nel codice;
- notebook non ideale per dashboard executive;
- manutenzione maggiore per KPI semplici.

Python è utile per analisi profonde, ma non è il miglior front-end per il COO.

## 13.8.4 La terza proposta: tutto in streaming

Data Engineering propone una pipeline near-real-time per tutti i dati.

Il team quantifica però il requisito.

Il COO accetta dati aggiornati entro 45 minuti. Solo l'alert sulla disponibilità richiede latenza inferiore a 5 minuti.

Costruire streaming completo per tutte le metriche sarebbe una soluzione molto più costosa del bisogno.

## 13.8.5 La soluzione ibrida

Il team sceglie:

1. **warehouse/lakehouse centrale** per dati storici e trasformazioni condivise;
2. **SQL** per costruire fact e metriche operative;
3. **semantic layer + BI** per KPI ufficiali;
4. **streaming limitato** solo agli eventi necessari agli alert operativi;
5. **Python/R notebook** per analisi mensili, modelli e investigazioni avanzate;
6. **Excel** per scenari finanziari e simulazioni veloci durante le riunioni;
7. **AI assistant** per accelerare query e documentazione, con test e reconciliation obbligatori.

Nessuno strumento «vince».

Il sistema funziona perché ogni strumento viene usato nel tratto del problema in cui ha il miglior rapporto tra potenza, semplicità e controllo.

## 13.8.6 Il risultato dopo sei mesi

Prima del redesign:

- 7 report manuali;
- 4 definizioni di cancellazione;
- aggiornamento mattutino completato tra le 9:00 e le 11:00;
- circa 16 ore settimanali di lavoro manuale;
- alert basati su controlli umani.

Dopo il redesign:

- KPI ufficiali disponibili alle 7:15;
- definizioni centralizzate;
- alert disponibilità in pochi minuti;
- report manuali ridotti drasticamente;
- analyst liberi di dedicare più tempo a diagnosi e decisioni.

Il beneficio più importante non è tecnologico.

È che il team smette di discutere «Excel vs Python vs BI» e inizia a ragionare in termini di **funzione del componente**.

## 13.8.7 La matrice pratica di scelta

| Problema | Strumento candidato |
|---|---|
| Analisi rapida e scenari | Excel / foglio |
| Query su grandi dati strutturati | SQL |
| Statistica, ML, simulazioni | Python / R |
| EDA e prototipazione programmabile | Notebook |
| KPI condivisi e monitoraggio | BI + semantic layer |
| Pipeline e storage scalabile | Cloud data platform |
| Workflow semplici e ripetitivi | No-code / low-code |
| Generazione e revisione assistita | AI + verifica umana |

Questa tabella non è una legge. È un punto di partenza.

## 13.8.8 Il test finale prima di scegliere

Prima di adottare uno strumento chiediamo:

1. Qual è il problema analitico?
2. Quanto spesso si ripete?
3. Quanto dato dobbiamo elaborare?
4. Chi consumerà il risultato?
5. Quanto deve essere riproducibile?
6. Chi lo manterrà?
7. Quanto costa operarlo?
8. Qual è il rischio se fallisce?
9. È un prototipo o un sistema?
10. Stiamo aggiungendo complessità perché serve o perché possiamo?

> **La maturità tecnica non consiste nell'usare strumenti sofisticati. Consiste nel sapere quando la sofisticazione non serve.**
