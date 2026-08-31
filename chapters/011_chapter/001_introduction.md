# Capitolo 11 — SQL, trasformazione del dato e data modeling per l'analisi

## 11.0 Il problema non è scrivere query: è costruire numeri di cui possiamo fidarci

SQL viene spesso insegnato come un linguaggio di sintassi: `SELECT`, `JOIN`, `GROUP BY`, funzioni finestra, CTE. Tutto corretto, ma incompleto.

Nel lavoro reale un analyst raramente fallisce perché non ricorda la sintassi esatta di una funzione. Molto più spesso fallisce perché:

- unisce tabelle a granularità diverse;
- duplica righe senza accorgersene;
- sceglie il denominatore sbagliato;
- tratta una tabella eventi come se fosse una tabella snapshot;
- aggrega prima di aver definito il grain corretto;
- confonde data di ordine, data di spedizione e data di competenza;
- ricostruisce una metrica in modo diverso rispetto al team Finance;
- usa una dimensione corrente per reinterpretare il passato;
- crea una query tecnicamente corretta che risponde alla domanda sbagliata.

Il punto centrale di questo capitolo è quindi semplice:

> **SQL è il linguaggio con cui formalizziamo una parte del nostro modello mentale dei dati. Se il modello mentale è sbagliato, una query perfettamente valida può produrre un risultato perfettamente sbagliato.**

### Caso simulato — Aurora Market e i 3,8 milioni di euro apparsi dal nulla

Aurora Market, marketplace europeo di prodotti per la casa, prepara il board meeting trimestrale. Il dashboard principale mostra ricavi Q2 pari a 48,6 milioni di euro, contro 44,8 milioni nel trimestre precedente.

La crescita sembra essere dell'8,5%.

Il team Finance però comunica un numero diverso: 44,9 milioni.

La prima reazione è cercare un errore nel sistema contabile. Invece il problema è nella query analitica.

La tabella `orders` contiene una riga per ordine. La tabella `order_lines` contiene più righe per ordine. La tabella `payments` può contenere più tentativi o movimenti per lo stesso ordine.

La query del dashboard unisce direttamente tutte e tre:

```sql
SELECT
    SUM(ol.quantity * ol.unit_price) AS revenue
FROM orders o
JOIN order_lines ol
    ON o.order_id = ol.order_id
JOIN payments p
    ON o.order_id = p.order_id
WHERE o.order_date >= '2026-04-01'
  AND o.order_date < '2026-07-01';
```

La sintassi è valida.

Il problema è semantico.

Un ordine con quattro linee e due movimenti di pagamento diventa otto righe dopo il join. Il fatturato delle linee viene duplicato.

Quando l'analyst ricostruisce il grain delle tre tabelle, scopre che circa il 14% degli ordini possiede più di un record in `payments`, soprattutto dopo l'introduzione di un nuovo flusso di autorizzazione carta.

La query non è diventata sbagliata quando è stata eseguita. Era sbagliata nel momento in cui è stato ignorato il grain.

### Le domande che vengono prima di SQL

Prima di iniziare una query, l'analyst dovrebbe riuscire a rispondere almeno a queste domande:

1. Qual è l'entità o evento elementare che voglio misurare?
2. Qual è il grain di ogni tabella coinvolta?
3. Quali chiavi sono davvero uniche?
4. Il join è uno-a-uno, uno-a-molti o molti-a-molti?
5. Quali misure sono additive e quali no?
6. Quale dimensione temporale rappresenta la domanda di business?
7. Sto misurando uno stock, un flusso o uno stato?
8. La definizione della metrica esiste già in un layer condiviso?

Nel resto del capitolo useremo SQL non come fine, ma come strumento per rendere esplicite queste decisioni.

### Obiettivo del capitolo

Alla fine dovremo saper passare da una richiesta come:

> “Fammi il revenue per cliente, canale e mese, confrontalo con l'anno scorso e mostrami i clienti che stanno rallentando”

non direttamente a una query, ma a una sequenza più robusta:

**domanda → grain → fonti → chiavi → trasformazioni → modello → metrica → validazione → query → interpretazione**.

---

**Riferimenti**

Microsoft Learn, *Understand star schema and the importance for Power BI*: https://learn.microsoft.com/en-us/power-bi/guidance/star-schema

Microsoft Learn, *Dimensional modeling in Microsoft Fabric Warehouse*: https://learn.microsoft.com/en-us/fabric/data-warehouse/dimensional-modeling-overview
