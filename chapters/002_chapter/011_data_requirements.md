## 2.10 Dai requisiti analitici ai requisiti dati

Una volta chiarita la domanda, bisogna tradurla in dati necessari.

Questo passaggio sembra tecnico, ma è ancora profondamente analitico.

Supponiamo che la domanda sia:

> **Perché la retention dei nuovi clienti è diminuita negli ultimi sei mesi?**

Non basta dire "servono i dati clienti".

Dobbiamo specificare:

- identificativo cliente;
- data di acquisizione;
- canale di acquisizione;
- prodotto o piano iniziale;
- eventi di utilizzo;
- transazioni;
- rinnovi;
- cancellazioni;
- eventuali ticket di supporto;
- prezzi e promozioni applicate;
- modifiche di prodotto avvenute nel periodo;
- paese o mercato;
- definizione di cliente attivo.

### Requisiti minimi

Per ogni variabile o tabella richiesta dovremmo sapere almeno:

1. cosa rappresenta;
2. qual è la granularità;
3. qual è la chiave;
4. con quale frequenza viene aggiornata;
5. quale periodo storico è disponibile;
6. quali valori mancanti sono possibili;
7. quali trasformazioni vengono applicate;
8. chi è responsabile della fonte;
9. se esistono cambiamenti di definizione nel tempo.

### Il concetto di grain

Il *grain* è il livello elementare rappresentato da una riga.

Una riga può rappresentare:

- un ordine;
- una riga d'ordine;
- una sessione;
- un cliente al giorno;
- un evento;
- un pagamento;
- un ticket.

Confondere il grain è una delle cause più frequenti di doppio conteggio.

Se una tabella contiene una riga per ordine e la uniamo a una tabella con più righe per pagamento, il numero di ordini potrebbe moltiplicarsi dopo la JOIN.

Per questo, prima di scrivere una query, l'analista dovrebbe riuscire a completare la frase:

> **Una riga di questa tabella rappresenta...**

### Dati disponibili e dati necessari non coincidono

Un principio importante è non confondere:

**"quali dati abbiamo?"**

con:

**"quali dati servirebbero per rispondere correttamente?"**

A volte i dati necessari non esistono.

Questa non è una sconfitta dell'analisi. È un risultato.

L'analista deve poter concludere:

> "Con le informazioni disponibili possiamo descrivere il fenomeno, ma non possiamo distinguere tra queste due spiegazioni. Per farlo servirebbe misurare X."

### Data lineage mentale

Anche senza essere Data Engineer, l'analista dovrebbe ricostruire il percorso principale del dato:

**evento reale → sistema sorgente → registrazione → trasformazione → warehouse/lakehouse → semantic layer → report/analisi**

Ogni passaggio può introdurre errori o modificare il significato.

### Requisiti dati come contratto

Una buona specifica dati trasforma una domanda astratta in un contratto verificabile.

Per esempio:

| Campo | Significato | Grain | Fonte | Necessario per |
|---|---|---|---|---|
| customer_id | cliente univoco | cliente | CRM | coorti |
| signup_date | data acquisizione | cliente | CRM | anzianità |
| event_date | evento utilizzo | evento | product analytics | engagement |
| cancel_date | cancellazione | contratto | billing | churn |

Questo documento riduce incomprensioni tra analyst, business e data engineering.

Nell'era dell'AI diventa ancora più importante, perché un agente può generare query molto rapidamente ma non può correggere una semantica che nessuno ha chiarito.
