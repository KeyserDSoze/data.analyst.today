## 2.12 Caso studio: da "facci una dashboard clienti" a un piano analitico

Consideriamo una richiesta reale e volutamente vaga:

> **"Ci serve una dashboard clienti perché ultimamente ci sembra che stiano andando peggio."**

Un approccio orientato allo strumento potrebbe partire subito da Power BI, Tableau o un notebook.

Un approccio analitico parte invece da una serie di chiarimenti.

### Passo 1 — Identificare il problema di business

Dopo un confronto con il responsabile commerciale emerge che la preoccupazione vera è questa:

> Il numero di clienti che effettuano un secondo acquisto entro 90 giorni sembra diminuito.

La richiesta non è quindi "fare una dashboard". È capire se la **repeat purchase rate** si sta deteriorando e cosa fare.

### Passo 2 — Identificare la decisione

Il team deve decidere se:

- modificare il programma di onboarding;
- introdurre campagne di riattivazione;
- cambiare promozioni o condizioni commerciali;
- intervenire su prodotti o servizio.

Questo restringe il campo dell'analisi.

### Passo 3 — Formalizzare la metrica

Definiamo:

**Repeat Purchase Rate 90d = clienti con almeno un secondo acquisto entro 90 giorni / clienti eleggibili osservabili per almeno 90 giorni**

Questa definizione evita un errore comune: includere clienti acquisiti troppo recentemente per poter sapere se effettueranno un secondo acquisto entro 90 giorni.

### Passo 4 — Scegliere la baseline

Confrontiamo:

- coorti mensili degli ultimi 18 mesi;
- stesso periodo dell'anno precedente;
- media storica pre-cambiamento.

### Passo 5 — Costruire le ipotesi

Possibili spiegazioni:

1. è cambiato il mix dei canali di acquisizione;
2. sono aumentati clienti attratti da sconti una tantum;
3. è cambiato il mix prodotti del primo ordine;
4. i tempi di consegna sono peggiorati;
5. la customer experience post-acquisto è peggiorata;
6. i prezzi sono aumentati;
7. il fenomeno è stagionale;
8. il tracking è cambiato.

### Passo 6 — Definire le segmentazioni

Analizziamo almeno:

- canale di acquisizione;
- paese;
- primo prodotto acquistato;
- fascia di valore del primo ordine;
- presenza di sconto;
- nuovo vs cliente già noto in altri canali;
- tempi di consegna;
- ticket di supporto.

### Passo 7 — Tradurre in requisiti dati

Servono:

- customer_id;
- order_id;
- order_date;
- net_revenue;
- product/category;
- discount;
- acquisition_channel;
- geography;
- shipment_date/delivery_date;
- support interactions;
- refund/cancellation status.

### Passo 8 — Verificare il processo di misurazione

Scopriamo che sei mesi prima è stato modificato il sistema di identificazione cliente.

Prima di concludere che la retention è peggiorata, dobbiamo quindi verificare se alcuni secondi acquisti vengono ora registrati sotto identità differenti.

Questa verifica potrebbe cambiare completamente l'analisi.

### Passo 9 — Disegnare l'analisi

Sequenza proposta:

1. validazione qualità e continuità del dato;
2. calcolo della repeat purchase rate per coorte;
3. confronto con baseline;
4. decomposizione per segmenti;
5. analisi dei contributi al cambiamento aggregato;
6. verifica delle ipotesi principali;
7. quantificazione dell'impatto economico;
8. raccomandazioni e prossimi test.

### Passo 10 — Decidere l'output

La prima consegna non sarà una dashboard permanente.

Sarà un **analytical memo** con:

- evidenze principali;
- grafici essenziali;
- segmenti responsabili del cambiamento;
- ipotesi supportate o respinte;
- limiti dell'analisi;
- raccomandazioni operative.

Solo se il fenomeno dovrà essere monitorato continuativamente avrà senso trasformare alcune metriche in dashboard.

### L'Analytical Brief finale

**Decisione:** capire se e dove intervenire per aumentare il secondo acquisto entro 90 giorni.

**Domanda primaria:** quali fattori e segmenti spiegano il cambiamento della repeat purchase rate a 90 giorni?

**Metrica:** clienti con secondo ordine entro 90 giorni / clienti pienamente osservabili per 90 giorni.

**Baseline:** coorti storiche e stesso periodo dell'anno precedente.

**Popolazione:** nuovi clienti con almeno 90 giorni di osservabilità.

**Ipotesi:** acquisition mix, discounting, product mix, delivery experience, customer support, pricing, tracking.

**Output:** memo decisionale e, solo successivamente se utile, monitoraggio ricorrente.

### La lezione

La richiesta iniziale era una dashboard.

Il problema reale era una decisione sulla retention.

Questa distanza tra richiesta e bisogno è uno degli spazi in cui un Data Analyst crea più valore.

> **Non bisogna automatizzare la richiesta prima di aver capito il problema.**
