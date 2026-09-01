## 13.4 BI: scegliere una superficie di consumo quando la domanda si stabilizza

Il Capitolo 11 ha trattato la semantica delle metriche e il Capitolo 12 il serving layer dell'architettura.

Qui il problema è più semplice:

> **Quando un risultato deve smettere di essere un'analisi personale e diventare un'interfaccia ricorrente per altri utenti?**

È questo il momento in cui gli strumenti di Business Intelligence diventano particolarmente utili.

### BI non è “fare grafici”

Un dashboard è soltanto l'ultima superficie di una catena.

Per essere utile nel tempo deve appoggiarsi a:

- dati sufficientemente stabili;
- definizioni condivise;
- refresh affidabile;
- permessi;
- ownership;
- percorsi di drill-down coerenti.

Il motivo per scegliere BI non è quindi la disponibilità di visualizzazioni.

È la necessità di **distribuire una domanda ricorrente**.

### Caso simulato/composito — il sesto dashboard non risolve cinque conversion rate

Un SaaS ha cinque dashboard con conversion rate tra 7,4% e 11,8%.

Ogni team usa un denominatore diverso:

- lead;
- qualified lead;
- opportunity;
- trial;
- activated account.

La tentazione è creare un dashboard executive “ufficiale”.

Ma se le definizioni non vengono prima separate e nominate, il sesto dashboard aggiunge un altro numero al conflitto.

La soluzione può essere:

```text
lead_to_opportunity_conversion
trial_to_activation_conversion
checkout_to_paid_conversion
```

con owner e significato dichiarati.

BI serve poi a distribuire queste metriche. Non a inventarne il significato.

### La domanda deve essere abbastanza stabile

Un errore frequente è industrializzare troppo presto una fase diagnostica.

### Caso simulato/composito — dashboard per un'indagine che cambia ogni giorno

Strategy deve capire un calo di contribution margin.

Il primo giorno guarda mix e sconti.

Il secondo emergono freight e resi.

Il terzo servono FX, marketplace fee e nuove cohort.

Se costruiamo subito un dashboard formalizzato, ogni nuova ipotesi diventa una modifica al prodotto BI.

In una fase del genere è spesso più efficiente:

```text
SQL / notebook → investigazione
                 ↓
          pattern stabile
                 ↓
           BI / monitoraggio
```

> **La BI industrializza una domanda. Non dovrebbe essere il costo di scoprire quale domanda dobbiamo fare.**

### Self-service: libertà sul consumo, non anarchia sulla definizione

Un buon ambiente self-service consente agli utenti di:

- filtrare;
- segmentare;
- cambiare periodo;
- esplorare dimensioni;
- fare drill-down;

senza dover ricostruire da zero:

- numeratori;
- denominatori;
- calendario;
- identity logic;
- filtri fondamentali.

Questo è il confine tra **exploration** e **semantic ownership**.

### Quando BI è una buona scelta

BI è particolarmente sensata quando:

- la domanda è ricorrente;
- il pubblico è ampio o non tecnico;
- gli stessi KPI vengono consultati ripetutamente;
- serve refresh automatico;
- servono permessi e distribuzione controllata;
- la visualizzazione/interazione è parte del prodotto;
- il dato deve essere consumato senza scrivere codice.

È meno naturale come ambiente principale per:

- ricerca metodologica;
- analisi una tantum;
- simulazioni sofisticate;
- domande ancora instabili;
- debugging profondo del dato.

### Dashboard as product, non dashboard as archive

Quando scegliamo BI, una domanda utile è:

> quale comportamento vogliamo rendere più facile?

Per esempio:

```text
Operations → vedere eccezioni e agire
Sales      → prioritizzare account
Finance    → monitorare actual vs plan
Executive  → capire scostamento e decisione richiesta
```

Se il dashboard contiene “tutto ciò che potremmo mostrare”, probabilmente non abbiamo ancora definito bene il prodotto.

Il Capitolo 16 entrerà nel design visuale. Qui ci interessa il **fit dello strumento rispetto al consumo**.

### Campo del Tooling Decision Record

Per una soluzione BI annotiamo:

```text
recurring question:
consumer personas:
usage frequency:
certified metrics required:
interaction needed:
refresh / freshness:
access model:
ownership:
upstream source of truth:
exploratory needs kept outside BI:
exit / redesign condition:
```

### Regola operativa

> **Scegli BI quando devi rendere economico e coerente il consumo ripetuto di una domanda abbastanza stabile. Non costruire un dashboard per evitare di fare prima l'analisi.**
