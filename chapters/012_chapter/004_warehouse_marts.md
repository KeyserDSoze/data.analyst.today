## 12.3 Data warehouse e data mart: integrare per analizzare

Un **data warehouse** è un ambiente progettato per raccogliere, integrare e rendere interrogabili dati provenienti da più sistemi con finalità analitiche.

Non è semplicemente "un database più grande".

Il suo valore nasce dal fatto che può diventare il luogo in cui:

- sorgenti diverse vengono integrate;
- identità e chiavi vengono riconciliate;
- la storia viene preservata;
- la qualità viene controllata;
- i dati vengono modellati per l'analisi;
- le definizioni diventano più stabili e condivise.

Microsoft continua a indicare il dimensional modeling e lo star schema come approcci maturi per workload analitici: dimensioni per descrivere entità e facts per registrare osservazioni ed eventi a un grain definito.

## Data mart

Un data mart è normalmente un sottoinsieme orientato a un dominio o a una funzione, ad esempio:

- Finance;
- Sales;
- Marketing;
- Supply Chain;
- Product.

Può essere fisicamente separato oppure essere semplicemente un insieme curato di tabelle, viste o schemi all'interno di una piattaforma condivisa.

### Il vantaggio

Un buon mart riduce la distanza tra il dato tecnico e il linguaggio del business.

Un analyst di Finance dovrebbe poter trovare entità come:

- invoice;
- payment;
- cost center;
- revenue recognition;
- fiscal period.

Non dovrebbe dover ricostruire ogni volta queste entità da trenta tabelle applicative.

## Caso realistico: cinque revenue diverse

**OrionCloud**, SaaS B2B, cresce tramite acquisizioni e si ritrova con:

- CRM Salesforce;
- billing system storico;
- nuovo billing system;
- ERP Finance;
- database applicativo.

Cinque team calcolano la revenue mensile.

I risultati per giugno sono:

| Team | Revenue |
|---|---:|
| Finance | €12,8M |
| Sales | €13,6M |
| Product Analytics | €14,1M |
| Customer Success | €13,2M |
| CEO dashboard | €13,9M |

Nessuna query contiene un evidente errore di sintassi.

Le differenze derivano da:

- invoice date vs service period;
- gross vs net of credits;
- valuta al cambio corrente vs storico;
- account test inclusi;
- revenue booked vs recognized.

Costruire un warehouse non risolve automaticamente il problema, ma crea il luogo in cui la riconciliazione può diventare esplicita.

Il team definisce quindi una fact `revenue_recognition` con grain:

> una riga per contratto, prodotto e mese di competenza.

Finance mantiene la responsabilità della definizione contabile, mentre Sales dispone di una metrica separata per booked ARR.

Il risultato non è "una metrica per tutto". È **una semantica esplicita per ogni decisione**.

## Quando il warehouse diventa troppo centrale

Anche una piattaforma centralizzata può creare problemi se ogni richiesta richiede un team centrale.

Il rischio è passare da:

> tutti producono numeri diversi

alla situazione opposta:

> nessuno riesce a ottenere un dato senza aprire un ticket.

Per questo molte architetture moderne combinano:

- fondazioni dati condivise;
- ownership per dominio;
- modelli certificati;
- self-service controllato.

### Regola pratica

Il warehouse dovrebbe ridurre il costo marginale delle nuove analisi.

Se ogni nuovo KPI richiede ricostruire da zero sorgenti, join e definizioni, il problema non è solo SQL: manca un livello di modellazione riusabile.

### Fonte pubblica

Microsoft Learn, *Understand star schema and the importance for Power BI*:
https://learn.microsoft.com/en-us/power-bi/guidance/star-schema
