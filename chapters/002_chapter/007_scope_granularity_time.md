## 2.6 Scope: popolazione, unità di analisi e tempo

Una domanda può sembrare precisa e produrre comunque risultati incompatibili se persone diverse immaginano popolazioni, unità di analisi o finestre temporali diverse.

Per questo il brief deve fissare lo **scope** prima che inizi l'estrazione dei dati.

Il Capitolo 3 entrerà nel dettaglio tecnico di grain, chiavi, eventi e snapshot. Qui ci interessa la specifica analitica: **che cosa deve essere dentro e fuori dall'indagine?**

### Popolazione

Chi o che cosa è eleggibile per l'analisi?

Esempi:

- tutti i clienti con contratto attivo all'inizio del mese;
- nuovi clienti acquisiti tra gennaio e giugno;
- ordini completati e non integralmente rimborsati;
- sessioni web non interne e non bot;
- prodotti disponibili per almeno l'80% del periodo.

Scrivere “clienti” o “ordini” non basta quando esistono stati e condizioni diverse.

Una buona popolazione contiene anche le **esclusioni intenzionali**.

### Unità di analisi

Qual è l'entità elementare a cui attribuiamo il fenomeno?

Possiamo ragionare a livello di:

- evento;
- sessione;
- ordine;
- cliente;
- account;
- prodotto;
- negozio;
- giorno o coorte.

Questa scelta non è soltanto tecnica.

Se la domanda è “quale percentuale di clienti riacquista?”, il cliente è un'unità naturale. Se la domanda è “dove fallisce il pagamento?”, probabilmente servono tentativi o eventi. Se stiamo valutando una policy assegnata per negozio, analizzare ogni transazione come osservazione indipendente può dare un'immagine ingannevole.

Prima della query dobbiamo riuscire a completare:

> **“Una osservazione nella mia analisi rappresenta…”**

### Periodo e campo temporale

Anche “ultimo trimestre” è ambiguo se non specifichiamo quale evento determina il periodo.

Un ordine può avere:

- `created_at`;
- `paid_at`;
- `shipped_at`;
- `delivered_at`;
- `returned_at`.

La data corretta dipende dal fenomeno.

Nel brief annotiamo almeno:

- campo temporale principale;
- timezone, se rilevante;
- inizio e fine della finestra;
- eventuale periodo di maturazione necessario;
- ritardo con cui il dato diventa completo.

La **maturazione** è particolarmente importante per metriche future rispetto all'evento iniziale. Per misurare retention a 90 giorni non possiamo trattare come pienamente osservabili clienti acquisiti dieci giorni fa.

### Stock e flow

Lo scope dovrebbe inoltre chiarire se stiamo misurando uno stato in un istante o un evento durante un intervallo.

**Stock**:
- clienti attivi a fine mese;
- inventario disponibile oggi;
- pipeline aperta al 31 marzo.

**Flow**:
- nuovi clienti acquisiti nel mese;
- ordini ricevuti;
- ticket aperti;
- revenue riconosciuta durante il trimestre.

Confrontare uno stock con un flow senza rendere esplicito il modello temporale produce facilmente KPI confusi.

### Scope creep

Definire lo scope serve anche a impedire che una domanda si espanda durante l'esecuzione.

Partiamo dal churn enterprise europeo e, dopo due giorni, qualcuno chiede di includere anche SMB, pricing globale, support e tre anni di storico. Le nuove domande possono essere valide, ma devono essere trattate come ampliamento del brief, non come dettaglio gratuito.

Ogni espansione modifica costo, tempi e potenzialmente la decisione supportata.

### Campo del brief

```text
Popolazione eleggibile:
Esclusioni:
Unità di analisi:
Grain richiesto per i dati:
Campo temporale principale:
Timezone:
Finestra di analisi:
Periodo di maturazione:
Data latency / data complete as of:
Fuori scope:
```

> **Lo scope non serve a limitare la curiosità. Serve a sapere esattamente a quale popolazione e a quale periodo potremo applicare la conclusione.**
