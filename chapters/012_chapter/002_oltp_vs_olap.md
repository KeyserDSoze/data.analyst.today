## 12.1 OLTP vs OLAP: il sistema che registra non è sempre il sistema che analizza

Una delle distinzioni più utili per un Data Analyst è quella tra sistemi **OLTP** e sistemi **OLAP**.

In termini semplici:

- un sistema OLTP è ottimizzato per eseguire transazioni operative rapidamente e in modo consistente;
- un sistema OLAP è ottimizzato per interrogazioni analitiche, aggregazioni e scansioni su grandi volumi di dati.

### Un esempio concreto

Pensiamo a un e-commerce.

Quando un cliente conferma un ordine, il sistema operativo deve:

1. creare l'ordine;
2. aggiornare lo stock;
3. registrare il pagamento;
4. mantenere consistenza tra più entità;
5. rispondere in tempi molto bassi.

Questa è una responsabilità tipica OLTP.

Quando, invece, il CFO chiede:

> Qual è stato il margine netto per categoria, paese e coorte cliente negli ultimi 24 mesi?

la query deve probabilmente:

- leggere milioni di ordini;
- unire clienti, prodotti, costi, promozioni e resi;
- aggregare per più dimensioni;
- confrontare periodi storici.

Questo è un workload analitico.

### Perché non fare tutto direttamente sul database operativo?

Per piccoli contesti può funzionare. Ma quando scala, emergono problemi:

- query pesanti competono con il traffico operativo;
- lo schema è progettato per transazioni, non per facilità analitica;
- la storia può essere incompleta o sovrascritta;
- integrare più sistemi diventa difficile;
- business logic e definizioni metriche si moltiplicano nelle query degli analisti.

### Caso realistico: il report che rallenta il checkout

**UrbanBike**, marketplace di biciclette e accessori, ha inizialmente un solo database PostgreSQL usato sia dall'applicazione sia dagli analisti.

Ogni lunedì mattina una query di reporting calcola vendite, resi e commissioni su circa 180 milioni di righe.

Dopo la crescita internazionale, il team nota che tra le 8:30 e le 9:15:

- il tempo medio del checkout sale da 420 ms a 1,8 secondi;
- aumentano i timeout;
- il conversion rate scende leggermente.

La query SQL non era sbagliata. Era eseguita nel **posto sbagliato**.

La soluzione è separare il workload operativo da quello analitico attraverso replica/ingestion e un ambiente analitico dedicato.

## Schema operativo vs schema analitico

Uno schema OLTP tende spesso a essere più normalizzato per ridurre ridondanza e preservare consistenza.

Uno schema analitico può essere intenzionalmente più denormalizzato o modellato dimensionalmente per rendere più semplici e performanti le domande di business.

Questa differenza spiega perché una fact table vendite con dimensioni prodotto, cliente e data può essere molto più utile per l'analisi rispetto a decine di tabelle operative perfettamente normalizzate.

### Regola pratica

Prima di interrogare una tabella chiediti:

- è una sorgente operativa o analitica?
- contiene storia completa?
- è sicuro eseguire query pesanti?
- esiste una replica o un modello curato?
- qual è la latenza tra operatività e disponibilità analitica?

Il punto non è evitare sempre i database operativi. È capire **quando la comodità di leggere direttamente dalla sorgente crea un rischio analitico o operativo**.
