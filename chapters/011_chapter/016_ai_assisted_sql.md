## 11.15 AI-assisted SQL: accelerare la sintassi senza delegare il significato

Gli assistenti AI possono già generare SQL da linguaggio naturale, completare query, spiegare codice e suggerire correzioni.

Microsoft Fabric, per esempio, documenta funzionalità Copilot che trasformano richieste in linguaggio naturale in T-SQL, propongono completamenti e possono spiegare o correggere query. La documentazione raccomanda comunque di specificare con chiarezza colonne, aggregazioni e filtri e di rivedere la query generata prima di eseguirla.[^ms-copilot]

Questa evoluzione cambia il lavoro dell'analista.

Scrivere una `ROW_NUMBER()` corretta diventa più economico.

Capire **quale grain deve avere il risultato**, invece, non viene automaticamente risolto.

### Caso realistico: una query perfetta per la domanda sbagliata

Un analyst di **HelioTravel** chiede a un assistente AI:

> Mostrami il revenue medio per cliente per paese negli ultimi 12 mesi.

L'assistente genera una query plausibile:

```sql
SELECT
    c.country,
    SUM(o.revenue) / COUNT(DISTINCT o.customer_id) AS avg_revenue_per_customer
FROM orders o
JOIN customers c
  ON o.customer_id = c.customer_id
WHERE o.order_date >= CURRENT_DATE - INTERVAL '12 months'
GROUP BY c.country;
```

La query compila.

Il risultato è formalmente coerente con il prompt.

Ma il business voleva rispondere a una domanda diversa:

> Quanto vale mediamente un cliente acquisito in ciascun paese nei primi 12 mesi dalla sua acquisizione?

Serviva quindi una finestra relativa alla data di acquisizione del singolo cliente, non gli ultimi 12 mesi di calendario.

L'AI non ha fatto un errore SQL.

Ha eseguito fedelmente una richiesta ambigua.

### Il prompt deve includere semantica

Un buon prompt SQL dovrebbe specificare almeno:

- grain del risultato;
- tabella o entità di partenza;
- definizione della metrica;
- data da usare;
- filtri;
- trattamento dei `NULL`;
- comportamento dei join;
- esclusioni importanti;
- eventuale necessità di mantenere righe senza match.

Esempio migliore:

```text
Voglio una riga per paese di acquisizione.
Per ogni cliente acquisito nel 2025, calcola il net revenue generato nei 365 giorni successivi alla sua acquisition_date.
Escludi ordini cancellati, sottrai refund, mantieni anche clienti con zero ordini e usa country_at_acquisition, non il paese corrente.
```

Non garantisce che la query sia corretta, ma riduce l'ambiguità.

### Protocollo di verifica in sette passaggi

#### 1. Leggere la query prima di eseguirla

Capire quali tabelle usa, con quali join e quale grain produce.

#### 2. Controllare le cardinalità

Prima e dopo ogni join:

```sql
COUNT(*)
COUNT(DISTINCT business_key)
```

#### 3. Testare su pochi record conosciuti

Scegliere 3-5 clienti o ordini di cui possiamo ricostruire manualmente il risultato.

#### 4. Riconciliare i totali

Se la query calcola revenue:

```text
somma finale
vs
fonte finanziaria / modello certificato
```

#### 5. Provare edge case

- cliente senza ordini;
- refund totale;
- doppia valuta;
- cambio segmento;
- evento tardivo;
- riga duplicata.

#### 6. Chiedere all'AI di criticare la propria query

Prompt utile:

```text
Elenca almeno cinque modi in cui questa query potrebbe produrre risultati semanticamente sbagliati anche se viene eseguita senza errori. Controlla grain, join cardinality, date, NULL e denominatori.
```

La seconda risposta non è una garanzia, ma può accelerare la review.

#### 7. Salvare test e definizioni, non solo la query

Una query generata oggi può essere rigenerata domani in modo diverso.

Il vero asset dovrebbe includere:

- definizione della metrica;
- grain;
- test;
- lineage;
- query versionata.

### AI e query distruttive

Gli assistenti moderni possono anche suggerire DDL o DML.

La documentazione Microsoft distingue modalità read-only e modalità che richiedono approvazione esplicita per operazioni che modificano dati o schema.[^ms-copilot-overview]

Anche senza una protezione integrata, la regola professionale è semplice:

**una query generata da AI che modifica dati va trattata come codice non revisionato.**

Prima di un `UPDATE`, `DELETE`, `MERGE`, `DROP` o `CREATE OR REPLACE`:

- verificare l'ambiente;
- verificare il `WHERE`;
- fare preview delle righe coinvolte;
- usare transazioni se disponibili;
- avere rollback o backup;
- applicare least privilege.

### Dove l'AI crea davvero valore

L'AI è particolarmente utile per:

- ricordare sintassi rara;
- tradurre tra dialetti SQL;
- generare boilerplate;
- creare CTE leggibili;
- spiegare query legacy;
- suggerire test;
- produrre una prima bozza di documentazione;
- aiutare a leggere execution plan.

Il guadagno è reale.

Ma proprio perché la sintassi costa meno, aumenta il valore della verifica.

> **L'AI può generare SQL. L'analista resta responsabile di ciò che quel SQL significa.**

[^ms-copilot]: Microsoft Learn, *Query your SQL database in Fabric*, https://learn.microsoft.com/en-us/fabric/database/sql/query
[^ms-copilot-overview]: Microsoft Learn, *Microsoft Copilot in the SQL Database workload overview*, https://learn.microsoft.com/en-us/fabric/database/sql/copilot-sql-database
