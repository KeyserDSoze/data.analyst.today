## 4.6 Un workflow pratico per l'Exploratory Data Analysis

L'EDA non dovrebbe essere una sequenza casuale di grafici. Deve essere un processo disciplinato.

Un buon workflow può essere organizzato in sei passaggi.

### 1. Capire la domanda

Prima di aprire il dataset, scrivere in una frase cosa vogliamo capire.

Esempio:

**"Perché il tasso di rinnovo degli abbonamenti è sceso dal 81% al 74% negli ultimi quattro mesi?"**

### 2. Verificare la struttura del dataset

Controllare:

- numero di righe e colonne;
- grain;
- chiavi;
- periodo coperto;
- missing values;
- duplicati;
- definizioni delle variabili.

### 3. Descrivere le variabili singolarmente

Per le numeriche:

- media;
- mediana;
- percentili;
- dispersione;
- distribuzione;
- outlier.

Per le categoriche:

- frequenze;
- quote percentuali;
- categorie rare;
- valori inattesi.

### 4. Segmentare

Confrontare il fenomeno per dimensioni plausibili:

- paese;
- canale;
- piano;
- coorte;
- prodotto;
- device;
- customer tenure;
- periodo.

### 5. Cercare relazioni

Una volta compresi i singoli campi possiamo cercare pattern tra variabili: correlazioni, differenze tra gruppi, trend temporali e combinazioni inattese.

### 6. Annotare domande, non solo risultati

L'EDA produce spesso più domande che risposte.

Questo non è un fallimento.

È esattamente il suo scopo.

## Caso completo: il rinnovo SaaS

Una piattaforma SaaS per studi professionali ha 18.200 clienti attivi. Il renewal rate trimestrale è sceso dall'81% al 74%.

La prima dashboard mostra un calo distribuito apparentemente su tutto il portafoglio.

L'analista esegue l'EDA.

### Primo taglio: piano commerciale

- Enterprise: 92% → 91%
- Professional: 84% → 82%
- Basic: 76% → 63%

Il problema è soprattutto nel Basic.

### Secondo taglio: customer tenure

Nel piano Basic:

- clienti da oltre 12 mesi: 78% → 76%
- clienti da 6-12 mesi: 73% → 70%
- clienti da meno di 6 mesi: 74% → 52%

Ora il problema è ancora più circoscritto.

### Terzo taglio: canale di acquisizione

Tra i clienti Basic con meno di 6 mesi:

- organic: 69%
- referral: 72%
- paid search: 48%
- affiliate: 44%

### Quarto taglio: mese di acquisizione

Il crollo coincide con due coorti acquisite durante una promozione aggressiva con sconto del 60% sui primi tre mesi.

A questo punto l'analista non conclude ancora che "lo sconto causa churn".

Formula invece una nuova ipotesi:

> la promozione potrebbe aver acquisito clienti con fit peggiore o aspettative diverse, producendo un calo del rinnovo quando il prezzo torna normale.

L'EDA ha trasformato un problema enorme e vago in una domanda molto più precisa.

Da:

**"Perché il renewal rate è sceso?"**

A:

**"Perché le coorti Basic acquisite tramite paid e affiliate durante la promozione mostrano un rinnovo molto inferiore dopo il ritorno al prezzo pieno?"**

Ora possiamo progettare un'analisi diagnostica più seria.

### La lezione

L'EDA non è il punto finale dell'analisi.

È il processo con cui impariamo abbastanza sul dataset e sul fenomeno da porre domande migliori.
