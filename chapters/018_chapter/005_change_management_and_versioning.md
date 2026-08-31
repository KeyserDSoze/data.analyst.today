# 18.4 Versionamento, change management e compatibilità

Un sistema analitico maturo non deve soltanto funzionare oggi.

Deve poter cambiare domani senza rendere invisibile ciò che è cambiato.

Le pipeline cambiano.

Le sorgenti cambiano.

Le definizioni business cambiano.

Le organizzazioni cambiano.

Il problema non è evitare il cambiamento.

È renderlo controllabile.

## Quando una modifica rompe il significato

Immaginiamo che una società cambi la definizione di “active customer”.

Prima:

> almeno un ordine negli ultimi 90 giorni.

Dopo:

> almeno un ordine negli ultimi 60 giorni.

La modifica sembra semplice.

Ma impatta:

- dashboard executive;
- segmentazioni CRM;
- modelli churn;
- forecast;
- obiettivi commerciali;
- serie storiche;
- benchmark trimestrali.

Se aggiorniamo la formula senza registrare il cambiamento, il grafico storico può mostrare una discontinuità che sembra un fenomeno business ma è soltanto una nuova definizione.

## Semantic breaking change

Nel software siamo abituati a parlare di breaking change.

Anche i dati hanno breaking change.

Possono essere:

- **strutturali** — una colonna cambia nome o tipo;
- **semantici** — il campo mantiene nome e tipo ma cambia significato;
- **temporali** — cambia la logica con cui viene assegnata una data;
- **popolazionali** — cambia chi entra nel denominatore;
- **operativi** — cambia freshness o frequenza di aggiornamento.

I più pericolosi sono spesso quelli semantici, perché non fanno fallire la pipeline.

Continuano a produrre numeri.

## Caso realistico: schema stabile, significato rotto

Un marketplace riceve dal sistema ordini un campo `order_status`.

Per anni `completed` significa ordine pagato e consegnato.

Dopo una migrazione, il team sorgente ridefinisce `completed` come ordine con pagamento autorizzato.

Il tipo di dato resta stringa.

I valori restano apparentemente gli stessi.

Nessun test di schema fallisce.

Ma:

- revenue viene anticipata;
- cancellation rate diminuisce artificialmente;
- delivery metrics vengono distorte;
- Finance non riconcilia più.

Questo è un data incident semantico.

## Versionare ciò che conta

Un sistema serio dovrebbe versionare almeno:

- codice di trasformazione;
- definizioni metriche;
- schema dei data product;
- mapping critici;
- configurazioni;
- test;
- documentazione.

Per alcune metriche può essere utile mantenere esplicitamente versioni parallele durante una transizione.

Esempio:

- `active_customer_v1`;
- `active_customer_v2`.

Non è elegante come sostituire tutto immediatamente.

Ma rende la migrazione osservabile.

## Backfill o non backfill?

Quando una logica cambia, dobbiamo decidere se riscrivere il passato.

### Backfill completo

Ricalcoliamo tutta la storia con la nuova logica.

Utile quando vogliamo comparabilità coerente nel tempo.

### Forward-only

La nuova definizione vale da una data in avanti.

Utile quando la realtà o i dati storici non permettono un ricalcolo affidabile.

### Dual reporting

Manteniamo entrambe le versioni temporaneamente.

Utile quando il business deve capire l'impatto del cambiamento.

Nessuna scelta è sempre corretta.

L'errore è non sceglierla esplicitamente.

## Change notice

Per i prodotti critici, una modifica dovrebbe avere una nota chiara:

- cosa cambia;
- perché;
- quando entra in vigore;
- quali asset sono impattati;
- se il passato viene ricalcolato;
- quali differenze aspettarsi;
- chi è l'owner;
- come segnalare problemi.

## Deprecation è parte del design

Molti ecosistemi analitici si riempiono di asset “temporanei” che nessuno osa cancellare.

Dashboard duplicate.

Tabelle obsolete.

Metriche con suffissi `_new`, `_final`, `_final2`.

Questo aumenta la probabilità che utenti o agenti AI scelgano l'asset sbagliato.

La deprecazione deve essere progettata.

Un asset può avere stati come:

- experimental;
- certified;
- deprecated;
- retired.

Databricks, per esempio, include oggi segnali di certification e deprecation nelle proprie capacità semantiche proprio per distinguere asset autorevoli da asset superati.

## Compatibility contract

Un data product maturo dovrebbe comunicare cosa i consumer possono aspettarsi che resti stabile.

Per esempio:

- chiavi principali;
- granularità;
- naming;
- tipi di dato;
- semantic meaning;
- freshness;
- finestra di preavviso per breaking change.

Questo è un contratto sociale oltre che tecnico.

## Una regola utile

> **Se una modifica può cambiare una decisione senza cambiare il nome di una metrica, deve essere trattata come una breaking change.**

Scalare significa anche permettere all'organizzazione di evolvere senza trasformare ogni evoluzione in una perdita di fiducia nei dati.

## Fonti

- Databricks, *Unity Catalog semantics*: https://docs.databricks.com/gcp/en/uc-semantics
- Microsoft, *Data Processing Standards for AI and Analytics*: https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/data/operational-standards-data-processing-standards-unify-data-platform
