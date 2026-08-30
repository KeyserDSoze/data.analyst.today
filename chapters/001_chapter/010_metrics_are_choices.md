## 1.9 Una metrica non è un numero: è una scelta

Una delle idee più importanti dell'analisi dati è anche una delle più facili da sottovalutare:

> **Una metrica non viene semplicemente trovata nei dati. Viene definita.**

Il database contiene eventi, importi, date, stati, identificativi e relazioni. Ma concetti come "cliente attivo", "fatturato", "conversione", "retention", "churn", "margine" o "engagement" richiedono una definizione.

Questo significa che molte discussioni apparentemente tecniche sono in realtà discussioni sul significato.

### Lo stesso concetto può avere più definizioni corrette

Prendiamo il termine **cliente attivo**.

Potremmo definirlo come:

- un cliente che ha effettuato almeno un acquisto negli ultimi 30 giorni;
- un cliente che ha effettuato almeno un acquisto negli ultimi 90 giorni;
- un cliente con almeno due acquisti nell'ultimo anno;
- un cliente che ha effettuato il login nell'ultimo mese;
- un cliente con un abbonamento non scaduto;
- un cliente che genera ancora ricavi.

Qual è la definizione corretta?

Dipende dalla domanda.

Per un servizio in abbonamento, lo stato contrattuale potrebbe essere sufficiente. Per un e-commerce, un intervallo di 30 giorni potrebbe essere troppo breve. Per un prodotto utilizzato una volta l'anno, sarebbe assurdo classificare come inattivo chi non acquista da tre mesi.

La metrica è quindi una formalizzazione del modello mentale con cui interpretiamo il business.

### Il problema del fatturato

Anche "fatturato" sembra un concetto elementare finché non proviamo a implementarlo.

Dobbiamo decidere:

- ordini creati o ordini pagati?
- data dell'ordine, del pagamento o della spedizione?
- importo lordo o netto?
- IVA inclusa o esclusa?
- sconti inclusi?
- resi sottratti?
- cancellazioni escluse?
- costi di spedizione inclusi?
- conversione delle valute a quale tasso?

Due dashboard possono visualizzare numeri differenti pur partendo dallo stesso database, semplicemente perché implementano definizioni differenti.

Quando questo accade, il problema non è necessariamente nei dati.

Potrebbe essere nella semantica.

### Numeratore, denominatore e popolazione

Le metriche basate su rapporti sono particolarmente pericolose.

Supponiamo di voler misurare il tasso di conversione:

**conversion rate = acquisti / visite**

Sembra semplice. Ma che cosa conta come visita?

- sessioni?
- utenti unici?
- visite a una pagina prodotto?
- utenti che hanno visto il checkout?

E che cosa conta come acquisto?

- ordine creato?
- pagamento autorizzato?
- pagamento completato?
- ordine non successivamente cancellato?

La formula matematica può rimanere identica mentre il significato della metrica cambia radicalmente.

### Il denominatore spesso è più importante del numeratore

Molti errori analitici derivano da un denominatore sbagliato.

Se diciamo che il 20% dei clienti ha effettuato un secondo acquisto, dobbiamo sapere chi entra nel denominatore.

Tutti i clienti storici?

Solo quelli che hanno avuto abbastanza tempo per effettuare un secondo ordine?

Solo quelli acquisiti in un determinato periodo?

Se includiamo clienti acquisiti ieri, stiamo introducendo un bias evidente: non hanno ancora avuto il tempo materiale di dimostrare retention.

### Metriche assolute e metriche relative

Anche la scelta tra valori assoluti e relativi modifica l'interpretazione.

Un prodotto può mostrare:

- +10.000 € di fatturato;
- +2% di crescita.

Un altro:

- +5.000 € di fatturato;
- +40% di crescita.

Quale sta andando meglio?

Non esiste una risposta universale. Dipende se stiamo ottimizzando dimensione, crescita, marginalità, rischio o qualche altra variabile.

### Le metriche influenzano il comportamento

Una metrica non è soltanto uno strumento di osservazione. Quando diventa un obiettivo, influenza le persone.

Se un call center viene valutato esclusivamente sulla durata media delle chiamate, gli operatori avranno un incentivo a chiudere velocemente le conversazioni anche quando il problema del cliente non è realmente risolto.

Se una squadra commerciale viene premiata soltanto sul fatturato, potrebbe privilegiare vendite a basso margine o clienti problematici.

Se un prodotto digitale ottimizza soltanto il tempo trascorso nell'app, potrebbe aumentare engagement senza aumentare soddisfazione o valore reale per l'utente.

L'analista deve quindi chiedersi non soltanto "come calcolo questa metrica?", ma anche:

> **Quale comportamento incoraggia questa metrica quando diventa un obiettivo?**

### Semantic layer e coerenza organizzativa

Nelle moderne piattaforme analytics questo problema viene affrontato anche attraverso modelli e layer semantici: definizioni centralizzate di metriche, relazioni e logica di business che possono essere riutilizzate in report differenti.

Microsoft descrive i semantic model di Power BI come una rappresentazione logica di un dominio analitico che incorpora metriche, terminologia aziendale e relazioni. La documentazione più recente sottolinea inoltre che metriche curate e logica di business standardizzata aumentano la coerenza delle analisi e diventano particolarmente importanti quando gli utenti interrogano i dati attraverso sistemi AI.

Questo punto sarà ripreso in modo tecnico nei capitoli dedicati alla modellazione e all'architettura. Qui è sufficiente comprendere la conseguenza analitica:

**se il significato di una metrica non è condiviso, automatizzare le query non risolve il problema. Lo automatizza.**

### Una scheda minima per ogni metrica importante

Per le metriche critiche conviene documentare almeno:

1. nome;
2. definizione in linguaggio naturale;
3. formula;
4. numeratore e denominatore;
5. popolazione inclusa;
6. popolazione esclusa;
7. granularità temporale;
8. fonte dati;
9. regole per valori mancanti, resi e cancellazioni;
10. owner della definizione;
11. casi in cui la metrica non dovrebbe essere utilizzata.

### Domande da fare prima di fidarsi di una metrica

- Che cosa misura realmente?
- Quale fenomeno vuole rappresentare?
- Qual è l'unità di analisi?
- Chi entra nel denominatore?
- Quali eventi sono esclusi?
- Da quale momento temporale viene calcolata?
- È confrontabile tra periodi e segmenti?
- La definizione è cambiata nel tempo?
- Quale comportamento incentiva?
- Esiste una fonte autorevole della definizione?

Queste domande diventano ancora più importanti nell'era dell'AI.

Un agente può generare in pochi secondi una query perfettamente valida chiamata `customer_retention_rate`.

Ma se nessuno ha definito che cosa significhi retention per quell'azienda, il nome della query sta soltanto nascondendo una decisione concettuale non ancora presa.

### Fonti e approfondimenti

- Microsoft Learn, *Power BI semantic models*: https://learn.microsoft.com/en-us/power-bi/connect-data/semantic-models-third-party
- Microsoft Learn, *Get started with metric sets*: https://learn.microsoft.com/en-gb/power-bi/create-reports/get-started-metrics
- Microsoft Learn, *Optimize your semantic model for Copilot in Power BI*: https://learn.microsoft.com/en-us/power-bi/create-reports/copilot-evaluate-data
