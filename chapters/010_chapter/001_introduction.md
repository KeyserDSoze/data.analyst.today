# Capitolo 10 — Regressione e modelli predittivi per Data Analyst

## 10.1 Predire non significa capire

Quando un'organizzazione dice di voler "fare machine learning", spesso il problema reale è molto più concreto: stimare un valore futuro, ordinare clienti per rischio, prevedere una probabilità, anticipare una domanda, riconoscere casi anomali o decidere dove concentrare risorse limitate.

Per un Data Analyst, la parte più importante non è imparare una lunga lista di algoritmi. È capire **che cosa il modello sta cercando di stimare, con quali dati, per quale decisione e con quali conseguenze in caso di errore**.

Questo capitolo parte da due famiglie di modelli semplici ma potentissime:

- regressione lineare, quando il target è numerico;
- regressione logistica, quando il target è binario o probabilistico.

Sono modelli utili non perché siano sempre i più accurati, ma perché costringono a ragionare su relazione tra variabili, target, coefficienti, probabilità, errori e generalizzazione.

### Il caso di Northstar Logistics

Northstar Logistics gestisce consegne B2B per clienti industriali. Il management chiede un modello per prevedere il ritardo in ore di ogni spedizione.

Il team ha a disposizione:

- distanza;
- corriere;
- giorno della settimana;
- categoria merceologica;
- numero di colli;
- saturazione del deposito;
- meteo;
- ora prevista di partenza;
- ora effettiva di consegna.

L'ultima variabile rende il modello estremamente accurato.

Peccato che l'ora effettiva di consegna sia nota solo **dopo** che la consegna è avvenuta.

Quello non è un grande modello. È leakage.

Questo esempio contiene quasi tutto il capitolo: predizione, feature, tempo, validazione, metriche e disponibilità dell'informazione nel momento reale della decisione.

### Le tre domande prima del modello

Prima di aprire Python o chiedere a un LLM di generare codice, l'analista dovrebbe rispondere a tre domande.

**1. Cosa vogliamo prevedere?**

Non "il churn", ma per esempio:

> probabilità che un cliente attivo oggi cancelli l'abbonamento nei prossimi 60 giorni.

**2. Quando deve essere disponibile la previsione?**

Se il modello viene eseguito ogni lunedì mattina, tutte le feature devono essere conoscibili entro quel momento.

**3. Quale decisione prenderemo usando la previsione?**

Un risk score senza una policy operativa è solo un numero.

### Prediction e causalità sono problemi diversi

Supponiamo che un modello di churn scopra che i clienti che aprono molti ticket di assistenza hanno maggiore probabilità di cancellare.

Questo può essere utile per predire.

Non dimostra però che ridurre artificialmente il numero di ticket ridurrebbe il churn.

I ticket potrebbero essere un segnale di problemi sottostanti.

La predizione chiede:

> chi è più probabile che churni?

La causalità chiede:

> quale intervento ridurrebbe il churn?

Sono domande diverse e possono richiedere metodi diversi.

### Il principio guida del capitolo

> Un modello utile non è quello che produce il punteggio più impressionante in notebook. È quello che generalizza su dati futuri e migliora una decisione reale.

Nei prossimi paragrafi costruiremo questa idea passo dopo passo.
