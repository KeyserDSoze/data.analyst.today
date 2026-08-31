## 13.14 Sintesi ed esercizi: lo strumento è una decisione di design

Questo capitolo non vuole trasformare Excel, SQL, Python, R, BI, cloud o no-code in categorie rivali.

Vuole costruire un'abitudine più utile:

> **prima capisco il problema, poi scelgo lo strumento.**

Il Data Analyst moderno dovrebbe essere abbastanza competente con più ambienti da non essere costretto a vedere ogni problema attraverso un solo martello.

La competenza più importante non è sapere tutto di ogni tool. È riconoscere:

- cosa può essere risolto rapidamente;
- cosa deve diventare ripetibile;
- cosa deve essere centralizzato;
- cosa richiede codice;
- cosa richiede un semantic layer;
- cosa richiede infrastruttura;
- cosa invece non richiede nulla di tutto questo.

### Checklist finale del capitolo

Prima di iniziare un lavoro analitico, chiediti:

- Qual è la decisione?
- Qual è il grain del dato?
- Quanto è grande il problema realmente?
- Dove risiedono i dati?
- Il lavoro è esplorativo o ricorrente?
- Chi consumerà l'output?
- Quanto deve essere fresco?
- Quanto è costoso un errore?
- Quanto deve essere riproducibile?
- Quale parte dovrebbe essere centralizzata?
- Quale parte può rimanere locale?
- Chi manterrà la soluzione tra sei mesi?
- Qual è il TCO, non solo il prezzo?
- Qual è il costo dell'attesa?
- Possiamo partire più semplicemente?

---

## Esercizio 1 — Excel o piattaforma dati?

Una PMI riceve ogni mese quattro file CSV da circa 25.000 righe ciascuno.

Il CFO vuole:

- consolidare ricavi;
- applicare una tabella di cambi valuta;
- produrre un report mensile;
- fare scenari sul budget.

Un consulente propone una piattaforma cloud completa con ingestion, lakehouse, orchestrazione e dashboard enterprise.

### Domande

1. Quale soluzione useresti come prima implementazione?
2. Quali segnali ti farebbero cambiare architettura?
3. Quali parti devono essere riproducibili anche se si usa Excel?
4. Qual è il rischio di sovra-ingegnerizzare il problema?

---

## Esercizio 2 — Il notebook diventato critico

Un notebook Python identifica ogni lunedì i clienti a rischio churn.

All'inizio lo usa un solo analyst.

Sei mesi dopo:

- alimenta 60 Customer Success Manager;
- influenza €18 milioni di ARR;
- deve essere pronto entro le 07:00;
- fallisce circa una volta ogni tre settimane;
- usa credenziali salvate localmente;
- nessuno riceve alert quando fallisce.

### Domande

1. Il notebook è ancora un prototipo?
2. Quali requisiti di produzione sono emersi?
3. Quali componenti industrializzeresti per primi?
4. Quale ruolo dovrebbe possedere ciascuna parte della soluzione?

---

## Esercizio 3 — Dashboard o query?

Il direttore commerciale chiede una dashboard per rispondere a una sola domanda:

> "Quali 20 account hanno perso più pipeline rispetto allo stesso trimestre dell'anno scorso?"

La risposta serve per una riunione domani mattina e non è chiaro se verrà mai riutilizzata.

### Domande

1. Costruiresti subito una dashboard?
2. Quale sarebbe il percorso minimo per rispondere bene?
3. In quale momento la dashboard diventerebbe giustificata?

---

## Esercizio 4 — Tool moderno, problema sbagliato

Un team vuole introdurre un motore real-time per aggiornare ogni 10 secondi il KPI di customer lifetime value.

Il valore viene usato dal management una volta al mese per pianificare il budget.

### Domande

1. Qual è il mismatch tra architettura e decisione?
2. Quale requisito di freschezza proporresti?
3. Quale costo nascosto introduce il real-time?
4. Esistono parti del sistema che potrebbero invece meritare real-time?

---

## Esercizio 5 — SQL o Python?

Un retailer deve calcolare vendite, margine, resi e clienti attivi su 4 miliardi di righe già presenti nel warehouse.

Un analyst propone di estrarre i dati in pandas perché conosce meglio Python.

### Domande

1. Dove dovrebbe avvenire la maggior parte dell'aggregazione?
2. Quando Python diventerebbe utile?
3. Qual è la differenza tra scegliere un tool per familiarità e sceglierlo per adeguatezza?

---

## Esercizio 6 — Il workflow no-code

Un processo no-code integra CRM, advertising, email e billing.

Ha 170 blocchi e viene modificato da quattro persone senza version control.

Il costo licenza è soltanto €250 al mese, ma il team dedica circa 35 ore mensili alla manutenzione.

### Domande

1. Come stimeresti il TCO reale?
2. Quali segnali indicano che il processo ha superato il suo contesto ideale?
3. Lo riscriveresti completamente? Perché potrebbe essere una cattiva idea?
4. Quale percorso incrementale di migrazione proporresti?

---

## Esercizio 7 — Caso completo: Aurora Health Devices

Aurora vende dispositivi medicali B2B in 17 paesi.

La direzione vuole un sistema che identifichi account con rischio di mancato rinnovo.

Situazione iniziale:

- CRM in SaaS;
- billing in ERP;
- usage telemetry nel cloud;
- support ticket in un altro SaaS;
- 24.000 account;
- 400 milioni di eventi di utilizzo al mese;
- 32 account manager;
- capacità operativa: circa 600 interventi al mese.

Il team propone quattro strade:

**A.** esportare tutto mensilmente in Excel;

**B.** fare tutte le trasformazioni nel BI tool;

**C.** creare dataset centrali in SQL, usare Python per il modello e pubblicare gli score in BI;

**D.** costruire subito una piattaforma streaming completa che aggiorni lo score ogni minuto.

### Compito

Costruisci una raccomandazione che consideri:

- decisione;
- grain;
- volume;
- frequenza necessaria;
- capacità operativa;
- riproducibilità;
- ownership;
- costi;
- rischio;
- passaggio da prototipo a produzione.

Non limitarti a scegliere una lettera. Spiega perché le altre alternative sono meno adatte.

### Una possibile linea di ragionamento

La soluzione C è probabilmente il punto di partenza più equilibrato.

Ma la motivazione è più importante della scelta:

- il volume degli eventi rende poco sensato spostare tutto localmente;
- le trasformazioni condivise meritano centralizzazione;
- Python è appropriato per modellazione e validazione;
- BI è adatto alla distribuzione verso account manager;
- uno score al minuto non crea valore se il team interviene su base giornaliera o settimanale;
- 600 interventi mensili impongono una soglia e una prioritizzazione economica, non soltanto una buona AUC;
- la soluzione può iniziare come prototipo e poi acquisire logging, scheduling, test e monitoring quando dimostra valore.

Il punto finale del capitolo è questo:

> **La maturità analitica non consiste nell'usare più tecnologia. Consiste nel sapere quanta tecnologia serve per rendere una decisione migliore, senza trasformare la complessità in un obiettivo.**
