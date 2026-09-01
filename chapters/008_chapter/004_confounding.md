## 8.3 Confondenti: capire perché i gruppi erano diversi prima del trattamento

Il confounding nasce quando il processo che assegna l'esposizione crea gruppi che differiscono anche per cause dell'outcome.

In forma intuitiva:

```text
Z -> trattamento
Z -> outcome
```

`Z` apre un percorso non causale tra trattamento e outcome.

La conseguenza è importante: il confronto grezzo mescola l'effetto che vogliamo stimare con differenze già presenti tra i gruppi.

### Caso simulato/composito — La campagna display che sembrava triplicare la conversione

Un e-commerce osserva:

| Gruppo | Conversion rate |
|---|---:|
| Esposti agli annunci | 5,8% |
| Non esposti | 2,1% |

La piattaforma pubblicitaria, però, mostra più annunci proprio agli utenti che hanno visitato siti della categoria, cercato prodotti simili o dimostrato recente intento d'acquisto.

Una rappresentazione plausibile è:

```text
intento preesistente -> probabilità di esposizione
intento preesistente -> probabilità di acquisto
esposizione ----------> possibile effetto sull'acquisto
```

Il `+3,7 pp` osservato contiene sia selezione sia possibile effetto advertising.

### “Associato a trattamento e outcome” non basta come definizione operativa

Una variabile non va controllata solo perché è correlata con entrambe le cose.

Per decidere se aggiustare dobbiamo chiederci **dove si trova nel processo causale**.

Una variabile può essere:

- causa comune pre-trattamento — potenziale confondente;
- semplice predittore dell'outcome;
- mediatore generato dal trattamento;
- collider;
- proxy imperfetto di un confondente;
- conseguenza dell'outcome.

Il ruolo, non la correlazione, determina se il controllo aiuta o danneggia.

### Caso simulato/composito — Prezzo del gelato e temperatura

Una catena di gelaterie trova una correlazione positiva tra prezzo medio e quantità venduta.

Il management potrebbe concludere che aumentare il prezzo aumenta la domanda.

Ma nei giorni più caldi:

- la domanda aumenta;
- alcuni store attivano pricing dinamico;
- il prezzo medio cresce.

```text
temperatura -> prezzo
     |
     +-------> domanda
```

Confrontare giornate climaticamente molto diverse attribuisce al prezzo una parte dell'effetto della temperatura.

### “Controlliamo per tutte le colonne” è un anti-pattern causale

Una regressione con cinquanta feature non è automaticamente più causale di una con cinque.

Aggiungere indiscriminatamente variabili può:

- bloccare mediatori e cambiare l'estimand;
- aprire percorsi attraverso collider;
- introdurre misure post-trattamento;
- aumentare instabilità e extrapolation;
- dare un falso senso di completezza.

Il set di adjustment dovrebbe essere giustificato da una storia causale e dal timing delle variabili.

### Confondenti osservati e non osservati

Alcune cause comuni possono essere ben misurate:

- storico acquisti;
- dimensione account;
- tenure;
- area geografica;
- utilizzo prima del trattamento;
- calendario.

Altre sono più difficili:

- motivazione;
- reale intenzione di acquisto;
- qualità del management;
- urgenza;
- relazione commerciale;
- severità di un problema non registrata.

Matching, weighting e regressione possono bilanciare o aggiustare **ciò che osserviamo**.

Non eliminano per definizione il confounding non osservato.

### Il processo di assegnazione viene prima del dataset

Una domanda spesso più utile di “quali feature abbiamo?” è:

> **Perché questa persona ha ricevuto il trattamento?**

Intervistare chi prende la decisione operativa può rivelare variabili assenti dal database.

Per esempio:

> “Offriamo lo sconto solo quando il procurement minaccia esplicitamente di andarsene.”

Se `minaccia_di_churn` non è registrata, nessuna regressione sul CRM può controllarla direttamente.

### Confounding by indication

In molti processi aziendali l'intervento viene attivato proprio perché il rischio è elevato:

- più supporto ai clienti in difficoltà;
- più sconti ai clienti che minacciano churn;
- più manutenzione agli impianti fragili;
- più visite manageriali ai negozi peggiori.

Il trattamento può quindi apparire associato a outcome peggiori anche quando è utile.

Questo meccanismo ritornerà nel caso finale del capitolo.

### Scheda minima sul confounding

Prima di aggiustare un confronto osservazionale, documenta:

```text
Trattamento:
Outcome:
Cause plausibili del trattamento:
Cause plausibili dell'outcome:
Cause comuni plausibili:
Quali sono pre-trattamento?
Quali sono misurate?
Quali importanti non sono misurate?
Quali variabili NON dobbiamo controllare e perché?
```

> **Il confounding non è un difetto del coefficiente. È una conseguenza del modo in cui il mondo ha prodotto i gruppi che stiamo confrontando.**
