# 14.2 Generare SQL e Python con l'AI: velocità enorme, responsabilità invariata

La generazione di codice è probabilmente uno degli usi più immediati dell'AI per un Data Analyst.

Una richiesta come:

> "Scrivi una query che calcoli retention D30 per cohort di signup"

può produrre in pochi secondi una struttura SQL che, scritta a mano, richiederebbe diversi minuti.

Lo stesso vale per Python:

- pulizia dati;
- aggregazioni;
- regressioni;
- grafici;
- test statistici;
- parsing di file;
- automazioni ripetitive.

Il vantaggio è reale. Ma il rischio è altrettanto reale: il codice generato può essere **plausibile, eseguibile e sbagliato**.

## Il test delle quattro correttezze

Prima di fidarsi di codice generato, distinguiamo quattro livelli.

### 1. Correttezza sintattica

Il codice gira?

### 2. Correttezza logica

Fa ciò che la formula o l'algoritmo dichiarano?

### 3. Correttezza semantica

Usa la definizione business giusta?

### 4. Correttezza decisionale

L'output supporta davvero la decisione per cui è stato creato?

Il livello 1 è quello che l'AI risolve meglio. I livelli 3 e 4 richiedono ancora fortissimo giudizio umano.

## Caso realistico: retention D30 calcolata perfettamente male

Un'app consumer vuole misurare la retention D30.

L'AI genera:

```sql
WITH signup AS (
    SELECT user_id, MIN(event_date) AS signup_date
    FROM events
    WHERE event_name = 'signup'
    GROUP BY 1
),
active_d30 AS (
    SELECT DISTINCT e.user_id
    FROM events e
    JOIN signup s USING (user_id)
    WHERE e.event_date = DATE_ADD(s.signup_date, INTERVAL 30 DAY)
)
SELECT
    COUNT(DISTINCT a.user_id) * 1.0 / COUNT(DISTINCT s.user_id) AS retention_d30
FROM signup s
LEFT JOIN active_d30 a USING (user_id);
```

La query è leggibile. Ma l'azienda definisce D30 retention come **qualunque attività tra giorno 27 e giorno 33**, perché l'uso del prodotto è settimanale.

In più:

- alcuni utenti fanno signup senza aver completato l'onboarding;
- gli account test interni non sono esclusi;
- `event_date` è in UTC mentre il prodotto usa local date per il reporting.

Il problema non è SQL. È la specifica.

## Chiedere test insieme al codice

Una buona pratica è non chiedere solo:

> "Scrivi la query."

ma:

> "Scrivi la query e proponi almeno cinque controlli per verificare grain, join cardinality, duplicati, null, perimetro e confronto con una metrica indipendente."

Per esempio:

```sql
-- controllo: una riga per user_id nella cohort
SELECT user_id, COUNT(*)
FROM cohort
GROUP BY 1
HAVING COUNT(*) > 1;
```

Oppure:

```sql
-- controllo: quanti utenti vengono persi dopo il join?
SELECT
  COUNT(DISTINCT s.user_id) AS before_join,
  COUNT(DISTINCT j.user_id) AS after_join
FROM signup s
LEFT JOIN joined_data j USING (user_id);
```

## AI come reviewer di codice

L'AI è utile non solo per scrivere, ma anche per criticare codice esistente.

Prompt utile:

> "Rivedi questa query come se dovessi approvarla per un KPI executive. Cerca duplicazioni da join, filtri impliciti, rischio di leakage temporale, denominatori instabili, date sbagliate e assunzioni non documentate. Non riscriverla subito: prima elenca i rischi."

Questa modalità può essere più preziosa della semplice generazione.

## Python: l'errore silenzioso è spesso più pericoloso dell'errore esplicito

In Python, un'eccezione visibile è fastidiosa ma utile. Più pericoloso è un risultato plausibile ottenuto con una trasformazione errata.

### Caso realistico: imputazione prima dello split

Un modello di churn viene preparato con:

```python
X_filled = imputer.fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(X_filled, y)
```

L'AI ha scritto codice valido.

Ma l'imputer è stato fit sull'intero dataset, quindi ha usato informazioni della distribuzione del test set. Il leakage può essere piccolo o grande, ma la procedura non è pulita.

Una pipeline corretta dovrebbe imparare preprocessing soltanto dai dati di training.

## Chiedere alternative, non una sola soluzione

Per un task non banale, è utile chiedere:

> "Proponi tre implementazioni: una SQL-only, una Python-only e una ibrida. Per ciascuna valuta leggibilità, costo computazionale, riproducibilità e facilità di manutenzione."

Questo aiuta a evitare che la prima soluzione generata venga automaticamente trattata come la migliore.

## Quando non delegare la scrittura del codice

È prudente mantenere controllo diretto quando:

- la query alimenta reporting finanziario o regolatorio;
- l'output modifica dati di produzione;
- esistono implicazioni di sicurezza o privacy;
- il costo computazionale può essere molto alto;
- il codice entra in una pipeline critica;
- il significato della metrica è ancora ambiguo.

In questi casi l'AI può assistere, ma review e test devono essere espliciti.

> **La generazione di codice abbassa il costo di scrivere una soluzione. Non abbassa il costo di dimostrare che quella soluzione è corretta.**
