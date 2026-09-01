## 3.1 Osservazioni, variabili e unità di analisi

La prima lettura di un dataset dovrebbe partire da due domande semplici:

1. **che cosa rappresenta una riga?**
2. **che cosa rappresenta una colonna?**

Sembrano domande elementari. In realtà costringono a distinguere tre concetti che vengono spesso confusi: record, entità e osservazione.

Un **record** è una rappresentazione memorizzata dal sistema. Un'**entità** è l'oggetto reale o concettuale che ci interessa, per esempio un cliente, un ordine o un prodotto. Un'**osservazione** è l'unità che stiamo effettivamente studiando in quell'analisi.

Le tre cose possono coincidere. Ma non è garantito.

Consideriamo questa tabella:

| order_id | customer_id | product_id | quantity | price |
|---|---|---|---:|---:|
| 1001 | C17 | P8 | 2 | 35.00 |
| 1001 | C17 | P4 | 1 | 12.00 |

Il nome `order_id` potrebbe indurci a pensare che ogni riga sia un ordine. Ma lo stesso ordine compare due volte. La riga rappresenta più probabilmente **un prodotto all'interno di un ordine**.

Questa differenza cambia immediatamente il significato dei conteggi. Due righe non significano due ordini. Significano due linee osservate per lo stesso ordine.

Lo stesso problema compare in molti domini:

- un cliente può avere più contratti;
- un contratto può avere più versioni;
- un ticket può produrre molti eventi di stato;
- una visita web può contenere molte page view;
- un pagamento può avere più tentativi;
- un prodotto può avere uno snapshot per ogni magazzino e giorno.

Per questo una delle frasi più utili dell'intero capitolo è:

> **Una riga di questa tabella rappresenta...**

Finché non possiamo completarla in modo preciso, qualsiasi metrica è ancora sospetta.

### L'unità di analisi dipende dalla domanda

Il dataset possiede un grain fisico, ma l'analisi possiede anche una propria unità logica.

Se vogliamo studiare il valore medio degli ordini, l'unità analitica è l'ordine anche quando la sorgente è a livello di riga d'ordine. Se vogliamo studiare il mix di prodotto, la riga d'ordine può essere invece il livello corretto. Se vogliamo capire la retention, potremmo dover ricostruire una vista a livello cliente o coorte.

Questo significa che **il livello al quale i dati sono registrati e il livello al quale vogliamo ragionare non sono sempre uguali**.

Il passaggio tra i due deve essere esplicito.

### Una variabile è più del suo tipo tecnico

Una colonna può essere `INTEGER`, `VARCHAR`, `DATE` o `BOOLEAN`, ma il tipo tecnico non ci dice ancora cosa stiamo misurando.

`age = 37` può significare:

- età dichiarata alla registrazione;
- età calcolata oggi;
- età al momento dell'evento;
- età derivata da una data di nascita forse incompleta.

`status = active` può indicare:

- contratto non cancellato;
- login negli ultimi 30 giorni;
- account non disabilitato;
- cliente che genera ancora ricavi.

Per ogni variabile importante dovremmo quindi conoscere almeno:

- **significato di business**;
- **tipo tecnico**;
- **dominio dei valori possibili**;
- **unità di misura**, se applicabile;
- **momento di validità**;
- **processo che la produce**.

### Esempio realistico: `closed` non significa necessariamente risolto

In un sistema di assistenza una riga rappresenta un ticket e la colonna `status` contiene `closed`.

Un'analisi ingenua potrebbe utilizzare il numero di ticket chiusi come misura dei problemi risolti.

Poi il domain expert spiega che il sistema chiude automaticamente dopo 14 giorni anche i ticket senza risposta del cliente.

Il campo è tecnicamente corretto. Il valore `closed` è valido. Ma la variabile non rappresenta il concetto che l'analista aveva in mente.

È questo il passaggio centrale del data understanding:

**struttura fisica → significato semantico → unità analitica**.

Solo dopo possiamo iniziare a calcolare.