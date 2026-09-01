## 4.6 Un workflow pratico per l'EDA: dalla domanda al registro delle ipotesi

L'EDA non dovrebbe essere una sequenza casuale di `groupby`, correlazioni e grafici.

Nel Capitolo 3 abbiamo già verificato che il dato sia utilizzabile. Qui partiamo quindi da un dataset **pronto o pronto con caveat** e da una domanda definita nell'Analytical Brief.

Il compito dell'EDA è restringere progressivamente lo spazio del problema senza confondere un pattern con una spiegazione.

### Passo 1 — Dichiarare il fenomeno che vogliamo descrivere

Scriviamo una domanda abbastanza precisa da guidare l'esplorazione.

Per esempio:

> **Il renewal rate trimestrale è sceso dall'81% al 74%: dove si concentra il cambiamento e quali caratteristiche lo accompagnano?**

Notare il linguaggio: non chiediamo ancora "che cosa lo ha causato?".

### Passo 2 — Costruire il quadro aggregato

Prima di segmentare tutto, descriviamo il fenomeno principale:

- livello corrente;
- baseline;
- variazione assoluta e relativa;
- volume del numeratore e del denominatore;
- eventuale andamento temporale;
- distribuzione, se la metrica deriva da una variabile continua.

Questo crea il punto di riferimento a cui torneremo dopo ogni drill-down.

### Passo 3 — Descrivere le distribuzioni importanti

Per le variabili numeriche osserviamo:

- centro;
- dispersione;
- percentili;
- forma;
- code;
- sensibilità a osservazioni influenti.

Per le categoriche osserviamo:

- frequenze;
- proporzioni;
- categorie dominanti;
- composizione tra gruppi e periodi.

Il punto non è calcolare tutto ciò che il software offre. È capire quali proprietà possono cambiare l'interpretazione del fenomeno.

### Passo 4 — Segmentare con una ragione

Scegliamo dimensioni motivate dal processo o dall'Analytical Brief:

- piano;
- canale;
- mercato;
- coorte;
- prodotto;
- tenure;
- device;
- tipologia di cliente.

Per ogni segmentazione chiediamo:

> **Se il pattern fosse molto diverso qui, cambierebbe la prossima decisione o la nostra ipotesi?**

Se la risposta è no, la segmentazione potrebbe essere soltanto rumore analitico.

### Passo 5 — Cercare relazioni, non cause

Dopo aver compreso le singole variabili, osserviamo:

- differenze tra gruppi;
- scatter plot;
- correlazioni;
- tabelle di contingenza;
- pattern condizionati;
- evoluzione temporale.

Ogni relazione interessante dovrebbe generare almeno una spiegazione alternativa.

Esempio:

> I clienti con più ticket hanno churn maggiore.

Possibili letture:

- i problemi che generano ticket aumentano il churn;
- i clienti già a rischio contattano più spesso il supporto;
- un segmento più complesso genera sia più ticket sia più churn;
- la relazione dipende dall'anzianità del cliente.

L'EDA costruisce lo spazio delle ipotesi. Non sceglie ancora il vincitore.

### Passo 6 — Stressare il pattern

Prima di chiamare qualcosa "insight", ripetiamo il confronto in modi plausibili:

- media vs mediana;
- periodi alternativi;
- con e senza settimane eccezionali;
- gruppi aggregati vs segmentati;
- valori assoluti vs tassi;
- con e senza osservazioni molto influenti;
- diverse definizioni coerenti con il caveat noto.

Se il risultato cambia completamente per una scelta ragionevole, il pattern è **fragile**.

Questa fragilità va conservata, non nascosta.

### Passo 7 — Tenere un registro delle ipotesi

Un output utile può essere una tabella come questa:

| Osservazione | Ipotesi candidata | Evidenza a favore | Spiegazioni alternative | Prossimo controllo |
|---|---|---|---|---|
| churn concentrato nei nuovi SMB | onboarding insufficiente | completion più bassa | acquisition mix | confronto per canale/coorte |
| P95 delivery alto nel weekend | capacity insufficiente | volumi +35% | mix geografico | segmentare per area |

Questo impedisce di perdere la distinzione tra fatti e interpretazioni durante l'esplorazione.

### Caso simulato/composito — Il rinnovo SaaS

Una piattaforma SaaS per studi professionali ha **18.200 clienti** e vede il renewal rate trimestrale scendere dall'81% al 74%.

**Piano:**

```text
Enterprise:   92% → 91%
Professional: 84% → 82%
Basic:        76% → 63%
```

**Tenure, dentro Basic:**

```text
>12 mesi: 78% → 76%
6–12 mesi: 73% → 70%
<6 mesi: 74% → 52%
```

**Canale, Basic con meno di 6 mesi:**

```text
organic:     69%
referral:    72%
paid search: 48%
affiliate:   44%
```

Le coorti più deboli coincidono con una promozione del 60% sui primi tre mesi.

La conclusione EDA corretta non è:

> Lo sconto causa churn.

È:

> Il deterioramento aggregato è concentrato nelle coorti Basic recenti acquisite via paid e affiliate durante la promozione; il ritorno al prezzo pieno è una spiegazione candidata, insieme a differenze nel customer fit e nel mix di acquisizione.

La domanda successiva diventa molto più precisa:

> **Quali differenze tra le coorti promozionali e quelle comparabili spiegano il minor rinnovo, e quale disegno permetterebbe di distinguere selezione da effetto della promozione?**

A quel punto l'EDA ha fatto il proprio lavoro.

### Quando fermare l'EDA

L'esplorazione può continuare per sempre. Dovremmo fermarci quando:

- sappiamo dove si concentra il fenomeno;
- i principali pattern sono stati stressati;
- abbiamo separato fatti e ipotesi;
- le spiegazioni concorrenti più importanti sono esplicite;
- il prossimo passo richiede un metodo diverso: inferenza, esperimento, causalità o modello.

> **L'output dell'EDA non è "ho guardato i dati". È una rappresentazione più precisa di ciò che sappiamo e delle domande che meritano il prossimo investimento analitico.**