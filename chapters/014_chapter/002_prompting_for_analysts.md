## 14.1 Prompting per analisti: trasformare una richiesta vaga in una specifica verificabile
Un prompt analitico efficace non è una formula magica. È una specifica di lavoro.

La differenza tra:

> "Analizza le vendite"

e:

> "Confronta il net revenue delle ultime 8 settimane con le 8 precedenti, a parità di perimetro negozi, separando volume, prezzo e mix; usa `payment_captured_at` come data economica, escludi ordini cancellati e rimborsati integralmente, segnala segmenti con contributo assoluto > €50k e non formulare conclusioni causali"

non è principalmente una differenza di stile. È una differenza di qualità analitica.

## Un framework pratico: Q-C-D-M-V-O

Per richieste non banali, possiamo strutturare il prompt in sei blocchi.

### 1. Q — Question

Qual è la domanda business?

### 2. C — Context

Quale decisione deve supportare l'analisi? Quali definizioni aziendali contano?

### 3. D — Data

Quali tabelle, campi, grain e finestre temporali sono ammessi?

### 4. M — Method

Quale tipo di confronto o metodo vogliamo? Descrittivo, diagnostico, predittivo, causale?

### 5. V — Verification

Quali controlli deve eseguire l'AI prima di dare il risultato?

### 6. O — Output

Come deve essere restituito il risultato?

## Caso realistico: "Perché il churn è salito?"

Una SaaS company osserva churn mensile dal 3,8% al 4,6%.

Prompt debole:

> "Analizza perché il churn è aumentato."

Un LLM potrebbe produrre una lista plausibile: prezzo, onboarding, supporto, concorrenza.

Il problema è che queste non sono evidenze. Sono ipotesi.

Prompt migliore:

> "Analizza l'aumento del logo churn dal 3,8% al 4,6% tra Q1 e Q2. Usa account attivi a inizio mese come denominatore. Segmenta per cohort di acquisizione, piano, paese, tenure e activation status. Verifica prima eventuali cambi nella definizione del churn o nel tracking. Distingui evidenze osservate, ipotesi e possibili confondenti. Non usare linguaggio causale se il design non lo supporta. Restituisci una tabella dei driver ordinata per contributo al delta e un elenco di verifiche successive."

Ora il modello ha più possibilità di produrre un output utile e auditabile.

## Chiedere all'AI di esplicitare le assunzioni

Una tecnica semplice ma potente è chiedere:

> "Prima di scrivere codice, elenca le assunzioni che stai facendo su grain, date, filtri, definizioni delle metriche e cardinalità dei join."

Questo sposta errori potenziali da impliciti a visibili.

### Esempio

Richiesta:

> "Calcola l'ARPU mensile per mercato."

L'AI potrebbe assumere:

- revenue netta o lorda?
- utenti attivi medi o utenti attivi almeno una volta nel mese?
- mercato del billing o del consumo?
- valuta convertita a quale FX rate?
- utenti trial inclusi?

Senza queste decisioni, il codice può essere corretto ma la metrica indefinita.

## Prompting iterativo, non one-shot

Per analisi complesse è spesso più sicuro dividere il lavoro.

### Passo 1 — piano

> "Proponi un piano di analisi senza scrivere codice."

### Passo 2 — verifica del piano

L'analista corregge scope, grain, metriche e assunzioni.

### Passo 3 — generazione

> "Ora genera la query per il solo step 1."

### Passo 4 — test

> "Proponi tre sanity check per verificare che la query non duplichi righe e che il denominatore sia corretto."

### Passo 5 — interpretazione

Solo dopo i controlli si chiede un summary.

Questo approccio riduce il rischio che una singola risposta incorpori un errore iniziale e lo propaghi fino alla conclusione.

## Prompt che separano fatti, inferenze e ipotesi

Una struttura utile è chiedere tre sezioni distinte:

1. **Fatti osservati nei dati**
2. **Interpretazioni plausibili**
3. **Ipotesi che richiedono ulteriori dati o test**

Esempio:

| Livello | Esempio |
|---|---|
| Fatto | conversion mobile è scesa da 4,2% a 3,5% |
| Interpretazione | il peggioramento è concentrato su Android 14 |
| Ipotesi | un bug del wallet potrebbe aver aumentato gli errori di pagamento |

Questa separazione è particolarmente importante perché i modelli generativi tendono a produrre narrazioni fluenti anche quando l'evidenza è debole.

## Caso pubblico: Microsoft Copilot e semantic model

La documentazione Microsoft su Copilot in Power BI raccomanda prompt specifici e un semantic model ben preparato. Nomi ambigui, campi duplicati, descrizioni povere e organizzazione debole del modello aumentano la probabilità di risposte inattese.

È un punto fondamentale: il prompting non può compensare indefinitamente una semantica aziendale incoerente.

## Checklist del prompt analitico

Prima di inviare una richiesta importante, chiediti:

- la domanda decisionale è chiara?
- ho definito la metrica?
- ho specificato grain e popolazione?
- ho indicato la finestra temporale corretta?
- ho distinto analisi descrittiva da causale?
- ho indicato ciò che l'AI non deve assumere?
- ho chiesto controlli e sanity check?
- l'output è strutturato in modo verificabile?

> **Un buon prompt non serve a convincere l'AI a essere intelligente. Serve a rendere esplicito il problema che noi stessi dobbiamo aver capito.**

### Fonti

- OpenAI, *Best practices for prompt engineering*, https://help.openai.com/en/articles/6654000-how-to-use-ai-models-effectively
- Microsoft Learn, *Use Copilot with semantic models in Power BI*, https://learn.microsoft.com/en-us/power-bi/create-reports/copilot-semantic-models
