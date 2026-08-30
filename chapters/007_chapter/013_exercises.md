## 7.12 Esercizi pratici

Gli esercizi di questo capitolo non chiedono soltanto di calcolare metriche. Chiedono di decidere che cosa fidarsi, che cosa verificare e come trasformare un forecast in una decisione.

### Esercizio 1 — Vendite settimanali e stagionalità

Una catena di negozi osserva le vendite settimanali di una categoria per 104 settimane.

La serie mostra:

- crescita media del 7% annuo;
- picchi ricorrenti a novembre e dicembre;
- calo a gennaio;
- un picco eccezionale nella settimana 47 dell'ultimo anno.

Domande:

1. Quali componenti temporali cercheresti?
2. Confronteresti la settimana 47 con la settimana precedente o con la stessa settimana dell'anno precedente?
3. Quali informazioni business richiederesti prima di classificare il picco come anomalia?
4. Quale baseline useresti per un forecast a quattro settimane?

### Esercizio 2 — Il MAPE che mente

Due modelli prevedono la domanda di cinque SKU:

| SKU | Vendite reali | Errore A | Errore B |
|---|---:|---:|---:|
| A | 2 | 1 | 0 |
| B | 4 | 2 | 1 |
| C | 200 | 20 | 30 |
| D | 500 | 35 | 60 |
| E | 1.200 | 70 | 140 |

Gli SKU C, D ed E generano l'85% del margine.

Domande:

- quale modello potrebbe risultare migliore usando una metrica percentuale non pesata?
- quale informazione economica manca?
- come costruiresti una valutazione più utile per operations?

### Esercizio 3 — Forecast e regime change

Una piattaforma subscription prevede il churn mensile usando gli ultimi 30 mesi. Da settembre entra in vigore un nuovo pricing che aumenta del 18% il costo dei piani più popolari.

Il modello non contiene una variabile di prezzo.

Devi preparare il forecast di churn per ottobre-dicembre.

Scrivi una nota analitica di massimo 150 parole che specifichi:

- perché il forecast storico è fragile;
- che cosa faresti nell'immediato;
- quali scenari presenteresti al management;
- quali dati monitoreresti nelle prime settimane.

### Esercizio 4 — Anomalia o problema dati?

Alle 09:00 di martedì un dashboard mostra un calo del 42% negli ordini rispetto al martedì precedente.

Il CEO chiede una spiegazione immediata.

Hai questi segnali:

- traffico web -3%;
- checkout avviati -4%;
- pagamenti registrati -41%;
- ticket customer care nella norma;
- ultimo completamento della pipeline pagamenti alle 06:10 invece delle 08:30.

Qual è la tua prima ipotesi? Quali controlli fai prima di parlare di comportamento cliente?

### Esercizio 5 — Intervallo di previsione e capacità

Un contact center prevede 18.000 chiamate per lunedì.

Intervallo 80%: 16.900-19.400.

Intervallo 95%: 16.100-20.600.

La capacità standard è 18.700 chiamate. Un turno extra costa 9.000 €, mentre superare la capacità genera mediamente 35.000 € di costi tra outsourcing, SLA e customer dissatisfaction.

Non hai abbastanza informazioni per calcolare una decisione ottima esatta. Spiega però quali probabilità e costi vorresti stimare prima di decidere se attivare il turno extra.

### Esercizio 6 — Board meeting

Il forecast annuale del fatturato è 126 M€ con intervallo 95% di 112-141 M€. Il budget ufficiale è 134 M€.

Il CEO chiede:

> "Quindi raggiungeremo il budget oppure no?"

Prepara una risposta da Data Analyst senior che:

- non eluda la domanda;
- non trasformi l'incertezza in certezza;
- distingua forecast, target e scenario;
- proponga una decisione o un trigger operativo.

### Autovalutazione

A fine capitolo dovresti saper spiegare, senza software:

- perché ordine temporale e autocorrelazione contano;
- differenza tra trend e stagionalità;
- perché una anomalia non è automaticamente un errore;
- perché serve una baseline;
- differenza concettuale tra MAE, RMSE e MAPE;
- perché validare un forecast sul training set è insufficiente;
- perché l'incertezza cresce con l'orizzonte;
- quando un regime change può rendere obsoleto un buon modello;
- perché il miglior forecast statistico non coincide necessariamente con la migliore decisione aziendale.
