## 3.17 Sintesi ed esercizi

Questo capitolo ha un obiettivo semplice ma decisivo: imparare a non trattare un dataset come una verità già pronta.

Prima dell'analisi vengono la comprensione della struttura, della granularità, dell'identità, dei timestamp, dei null, dei duplicati, delle trasformazioni e della provenienza.

Un analista efficace non chiede soltanto:

> "Che cosa posso calcolare con questi dati?"

Chiede anche:

> "Che cosa rappresentano davvero questi dati, come sono stati prodotti e in quali condizioni posso fidarmi di loro?"

### Esercizio 1 — L'ordine duplicato

Hai una tabella con queste colonne:

```text
order_id
customer_id
order_date
product_id
quantity
unit_price
```

La chiave `order_id` compare più volte.

Prima di eliminare i duplicati, elenca almeno cinque spiegazioni possibili per cui questo comportamento potrebbe essere corretto.

Suggerimento: chiediti quale sia la vera granularità della tabella.

### Esercizio 2 — Il cliente scomparso

Un dataset CRM contiene 980.000 clienti a gennaio e 742.000 a febbraio.

Il business non ha registrato una perdita di clienti simile.

Costruisci un piano di investigazione ordinando i controlli che faresti nei primi trenta minuti.

Non scrivere ancora codice. Scrivi il ragionamento.

### Esercizio 3 — Revenue A contro Revenue B

Due dashboard mostrano per marzo:

- Dashboard Finance: €6,42 milioni
- Dashboard Sales: €6,81 milioni

Elenca almeno dieci possibili motivi della differenza e costruisci una reconciliation table ipotetica.

### Esercizio 4 — Missing non casuale

In una survey di soddisfazione il 38% dei clienti non ha compilato la domanda sul reddito.

Gli utenti premium mostrano solo il 9% di missing, mentre gli utenti free il 46%.

Perché sarebbe pericoloso sostituire i valori mancanti con la media generale? Quali ipotesi faresti sul meccanismo di missingness?

### Esercizio 5 — Il timestamp giusto

Un e-commerce possiede:

```text
created_at
paid_at
shipped_at
delivered_at
cancelled_at
refunded_at
```

Quale data useresti per:

- vendite giornaliere commerciali;
- ricavi contabilizzati;
- performance logistica;
- tasso di cancellazione;
- analisi della customer experience?

Motiva ogni risposta.

### Esercizio 6 — Progetta cinque test automatici

Per una tabella `orders_daily`, definisci cinque controlli automatici di data quality. Per ciascuno specifica:

- regola;
- soglia;
- severità;
- possibile causa del fallimento;
- team da avvisare.

### Caso finale — Ventiquattro ore prima del board

Sei l'analista responsabile del report mensile di una società subscription.

Il board è domani mattina.

Il report mostra:

- MRR +7,4%;
- nuovi clienti +12,1%;
- churn sceso dal 4,8% al 3,1%;
- ARPU invariato.

Sembra un mese eccellente.

Durante un controllo noti però tre anomalie:

1. la tabella subscription contiene il 6% di record in più del mese precedente;
2. circa 18.000 subscription hanno `cancelled_at = NULL` nonostante risultino chiuse nel billing system;
3. una nuova pipeline è entrata in produzione undici giorni fa.

Hai quattro ore per decidere se pubblicare i KPI.

Scrivi il tuo piano operativo.

Dovresti specificare:

1. quali metriche bloccheresti immediatamente;
2. quali riconciliazioni faresti;
3. quali controlli eseguiresti sulla nuova pipeline;
4. quali stakeholder coinvolgeresti;
5. cosa comunicheresti al management se non riuscissi a risolvere tutto entro la scadenza.

Questo esercizio non ha una singola risposta corretta. Il punto è dimostrare che sai trattare la qualità del dato come parte integrante della decisione, non come attività di pulizia preliminare.

### Domande di autovalutazione

Alla fine del capitolo dovresti saper spiegare con parole tue:

- cosa significa granularità;
- perché una primary key non è soltanto un dettaglio tecnico;
- la differenza tra evento e snapshot;
- perché un missing value può contenere informazione;
- perché un outlier non va eliminato automaticamente;
- cosa significa riconciliare due metriche;
- cosa descrive un data contract;
- cosa può e non può garantire un controllo automatico;
- perché lineage e semantica influenzano direttamente l'analisi.

Se una di queste risposte non è chiara, torna alla sezione corrispondente e prova a costruire un esempio concreto prima di procedere.
