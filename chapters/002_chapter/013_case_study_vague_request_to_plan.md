## 2.12 Caso end-to-end: da “facci una dashboard clienti” a un piano analitico

**Caso simulato/composito.** Velora Home è un retailer omnicanale di prodotti per la casa. Il CRM contiene circa 1,8 milioni di profili cliente e l'e-commerce rappresenta una quota crescente dei ricavi.

Il responsabile commerciale apre una richiesta:

> **“Ci serve una dashboard clienti perché ultimamente ci sembra che stiano andando peggio.”**

La frase contiene un output desiderato, ma non ancora un problema analitico.

### Passo 1 — Scoprire la preoccupazione reale

Durante una breve intervista emerge che il management non è genericamente preoccupato per “i clienti”.

Ha osservato una metrica interna secondo cui la percentuale di nuovi clienti che effettua un secondo acquisto entro 90 giorni sarebbe scesa dal **33,8% al 27,1%** in circa sei mesi.

Il problema di business diventa:

> la capacità di trasformare il primo ordine in una relazione ripetuta potrebbe essersi deteriorata.

### Passo 2 — Specificare la decisione

Il team deve decidere dove concentrare circa €600.000 di budget del trimestre successivo.

Le alternative principali sono:

- onboarding e CRM post-primo ordine;
- campagne di riattivazione;
- revisione delle promozioni di acquisizione;
- interventi sull'esperienza di consegna;
- nessun intervento specifico finché il fenomeno non è confermato.

Il decision owner è il Commercial Director insieme al CRM Lead.

Ora sappiamo perché il numero conta.

### Passo 3 — Definire la metrica

La metrica viene formalizzata così:

**Repeat Purchase Rate 90d = clienti con almeno un secondo ordine valido entro 90 giorni / nuovi clienti pienamente osservabili per almeno 90 giorni**

“Ordine valido” esclude test, cancellazioni integrali e ordini fraudolenti annullati.

La popolazione esclude i clienti troppo recenti per avere maturato 90 giorni di osservazione.

Questa definizione evita un errore comune: trattare clienti ancora immaturi come se avessero già fallito il secondo acquisto.

### Passo 4 — Dichiarare il tipo di domanda

La prima fase è **diagnostica**.

Il brief esplicita:

> “Vogliamo verificare se il deterioramento è reale, localizzarlo e restringere le spiegazioni plausibili. Le associazioni osservate non verranno interpretate automaticamente come effetti causali delle promozioni o dell'esperienza di consegna.”

Questa frase sarà importante più avanti.

### Passo 5 — Definire baseline e segmentazioni

La baseline primaria sono coorti mensili comparabili degli ultimi 18 mesi, con attenzione allo stesso periodo dell'anno precedente.

Segmentazioni prioritarie:

- canale di acquisizione;
- primo prodotto/categoria;
- sconto sul primo ordine;
- paese;
- valore del primo ordine;
- ritardo rispetto alla promessa di consegna;
- presenza di contatti con il supporto.

Ogni segmentazione è collegata a un'ipotesi o a una possibile azione.

### Passo 6 — Costruire il registro delle ipotesi

Tra le spiegazioni candidate:

1. mix di acquisizione spostato verso canali con minore repeat rate;
2. promozioni una tantum che attirano clienti poco propensi al riacquisto;
3. mix prodotti del primo ordine cambiato;
4. peggioramento dei tempi di consegna;
5. aumento di problemi post-acquisto;
6. aumento prezzi;
7. stagionalità;
8. cambiamento del sistema di identificazione cliente.

L'ultima ipotesi viene trattata come prioritaria perché può essere verificata rapidamente e, se vera, compromettere l'intero outcome.

### Passo 7 — Tradurre in requisiti dati

Dati **required**:

- customer identity storicizzata;
- ordini validi con data e importo;
- data di prima acquisizione;
- cancellazioni e rimborsi.

Dati **useful**:

- acquisition channel;
- categoria del primo ordine;
- sconto;
- promessa e data effettiva di consegna;
- support interactions;
- paese.

Il brief rende subito visibile che l'identità cliente è un requisito critico, non un dettaglio di implementazione.

### Passo 8 — Il sanity check cambia il problema

Durante la verifica emerge che sei mesi prima Velora Home ha migrato parte dell'e-commerce a un nuovo identity provider.

Per alcuni clienti che acquistano una seconda volta da dispositivo diverso, il secondo ordine viene collegato a un nuovo `customer_id` anziché al profilo originale.

La repeat purchase rate grezza stava quindi confondendo:

- vero mancato riacquisto;
- mancato riconoscimento dello stesso cliente.

Dopo una ricostruzione controllata dell'identità, il trend cambia:

- metrica originaria: **33,8% → 27,1%**;
- metrica corretta: **33,6% → 30,4%**.

Circa metà del deterioramento apparente era un artefatto di misurazione.

Ma non tutto.

Rimane un calo reale di circa **3,2 punti percentuali** da spiegare.

### Passo 9 — L'analisi diagnostica localizza il delta residuo

La decomposizione mostra che la parte maggiore del calo residuo è concentrata nei clienti:

- acquisiti tramite paid social;
- entrati con sconto iniziale superiore al 25%;
- con primo ordine in poche categorie fortemente promosse.

Questa combinazione spiega circa il 60% del delta residuo rispetto alle coorti di riferimento.

I clienti con consegne in ritardo mostrano anch'essi repeat rate più bassa, ma il ritardo è aumentato soprattutto nelle stesse categorie promozionate. L'effetto di logistica e mix prodotto non è ancora separato in modo credibile.

Il brief impedisce una conclusione eccessiva:

> non possiamo dire che “gli sconti causano bassa retention” soltanto perché il segmento scontato ha risultati peggiori.

Potrebbe esserci selezione: le promozioni attirano clienti con caratteristiche diverse.

### Passo 10 — La decisione cambia

La richiesta iniziale suggeriva una dashboard generica e possibili campagne CRM.

L'evidenza porta a un piano diverso:

1. correggere e monitorare permanentemente l'identity stitching;
2. evitare di usare la vecchia serie storica senza ricostruzione;
3. rivedere la qualità economica delle campagne paid-social ad alto sconto;
4. separare in un'analisi successiva l'effetto del mix promozionale da quello della delivery experience;
5. progettare un test su incentivi/onboarding invece di assumere che la correlazione osservata sia causale.

Il team non investe immediatamente i €600.000 in riattivazione.

Prima corregge la misurazione e ridisegna il successivo esperimento.

### L'Analytical Brief finale

**Problema di business:** repeat purchase dei nuovi clienti potenzialmente in deterioramento.

**Decisione:** dove allocare il budget retention/acquisition del prossimo trimestre.

**Domanda primaria:** il calo della repeat purchase rate 90d è reale e, se sì, quali segmenti e cambiamenti osservabili spiegano maggiormente il delta?

**Tipo:** diagnostica; nessuna attribuzione causale automatica.

**Outcome:** repeat purchase rate 90d su clienti pienamente maturi.

**Baseline:** coorti mensili storiche e year-over-year comparabile.

**Segmentazioni:** canale, sconto, primo prodotto, paese, delivery, support.

**Dati required:** identità storica + ordini validi.

**Rischio principale noto:** migrazione identity provider.

**Output:** memo decisionale + dataset/cohort view validata; dashboard soltanto per metriche che meritano monitoraggio ricorrente.

**Stop rule della prima fase:** validare la metrica, spiegare la parte materialmente rilevante del delta e identificare quali ipotesi richiedono un test successivo.

### La lezione

La richiesta era:

> “Facci una dashboard clienti.”

Il problema reale era:

> “Possiamo fidarci del deterioramento osservato, dove si concentra e quale decisione vale la pena prendere?”

La differenza tra le due frasi è il lavoro analitico prima dell'analisi.

> **Non automatizzare una richiesta prima di avere stabilito quale problema, quale decisione e quale evidenza devono governarla.**
