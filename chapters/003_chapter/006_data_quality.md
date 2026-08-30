## 3.5 Data quality: qualità rispetto a quale uso?

Dire che un dataset è "di buona qualità" non basta. La qualità del dato deve essere valutata rispetto all'uso che ne vogliamo fare.

Un dataset può essere perfettamente adeguato per una dashboard mensile e inadatto per un sistema antifrode in tempo reale. Può essere sufficiente per stimare un trend aggregato ma troppo incompleto per analizzare singoli clienti.

IBM descrive la data quality come il grado con cui i dati soddisfano criteri quali accuratezza, completezza, validità, consistenza, unicità, tempestività e fitness for purpose. Le sei dimensioni più comunemente adottate sono accuracy, completeness, consistency, timeliness, validity e uniqueness.  
Fonti: IBM, *What is Data Quality?* https://www.ibm.com/think/topics/data-quality ; IBM, *Data Quality Dimensions* https://www.ibm.com/think/topics/data-quality-dimensions

### 1. Accuracy

Il valore rappresenta correttamente il fenomeno reale?

Esempio: l'indirizzo di spedizione registrato è quello effettivamente utilizzato?

L'accuracy è difficile da misurare solo guardando il dataset perché spesso richiede una fonte esterna o una "source of truth".

### 2. Completeness

I valori necessari sono presenti?

Possiamo misurare la percentuale di valori nulli, ma la completezza non coincide semplicemente con `NOT NULL`.

Una data di nascita può essere presente nel 100% dei record ma contenere valori di default come `1900-01-01`. Formalmente non è nulla; semanticamente è mancante.

### 3. Consistency

I dati rispettano regole coerenti tra record, tabelle e sistemi?

Esempio: lo stesso cliente risulta "Italia" nel CRM e "France" nel sistema ordini.

### 4. Timeliness

Il dato è disponibile abbastanza rapidamente per la decisione?

Un dato perfettamente accurato consegnato tre settimane dopo può avere qualità insufficiente per una decisione operativa giornaliera.

### 5. Validity

Il valore rispetta formato, tipo, dominio e regole definite?

Esempi:

- percentuale tra 0 e 100;
- `end_date >= start_date`;
- paese appartenente a una lista valida;
- quantità non negativa quando il processo non ammette valori negativi.

### 6. Uniqueness

I record che dovrebbero essere unici lo sono davvero?

Duplicati di clienti, transazioni o ordini possono gonfiare metriche e alterare segmentazioni.

### Fitness for purpose

La lezione più importante è che le dimensioni di qualità non devono essere valutate nel vuoto.

Supponiamo che il 10% dei clienti non abbia il campo `profession`.

È grave?

Dipende.

Per calcolare il fatturato totale probabilmente no.

Per costruire una segmentazione basata sulla professione potrebbe essere un problema critico.

Quindi una valutazione professionale della qualità segue la forma:

> **Problema di qualità + dimensione interessata + impatto sulla domanda analitica.**

Non basta scrivere "ci sono missing values". Dobbiamo spiegare quali conclusioni potrebbero essere distorte da quei missing values.
