## 18.6 Automazione e CI/CD analitica
Quando un'analisi diventa ricorrente, la domanda non è più soltanto:

> “Funziona oggi?”

Diventa:

> “Continuerà a funzionare quando cambieranno dati, codice, schema, persone e contesto?”

È qui che il lavoro analitico incontra pratiche tipiche dell'ingegneria del software: version control, review, test automatici, ambienti separati, deployment controllato e rollback.

## Dall'automazione fragile all'automazione governata

Un processo ricorrente può essere automatizzato in molti modi.

La versione fragile è:

1. uno script gira ogni mattina;
2. se non dà errore, assumiamo che il risultato sia corretto;
3. il report viene aggiornato;
4. nessuno sa esattamente cosa è cambiato.

La versione governata aggiunge una catena di controlli:

**modifica → review → test → ambiente di validazione → deployment → monitoraggio → rollback possibile**

Il punto non è imitare DevOps per moda.

Il punto è riconoscere che una trasformazione dati può introdurre un errore di business tanto grave quanto un bug applicativo.

## Caso realistico: il KPI che cambia senza rompersi

Una SaaS company usa `active_customer` come denominatore per il Net Revenue Retention.

Un analytics engineer modifica una condizione per escludere account in grace period.

La query gira.

I test di sintassi passano.

Il dashboard si aggiorna.

La NRR scende da 108,4% a 104,9%.

Tecnicamente nulla è rotto.

Semanticamente è cambiata la popolazione misurata.

Se il cambiamento non viene versionato e validato come breaking change, il management può interpretare il nuovo valore come peggioramento reale del business.

## Che cosa dovrebbe entrare in una pipeline CI/CD analitica

Non serve lo stesso rigore per ogni notebook esplorativo. Ma quando un asset alimenta decisioni ricorrenti, dovremmo considerare almeno:

- controllo sintattico e compilazione;
- test su schema e tipi;
- test di unicità e chiavi;
- test di volumi e range plausibili;
- test di riconciliazione;
- confronto con baseline o versione precedente;
- validazione delle metriche principali;
- review umana per modifiche semantiche;
- deploy progressivo quando possibile.

## Deployment progressivo anche per i dati

Molte organizzazioni pensano al deployment dei dati come a un interruttore: vecchio modello spento, nuovo modello acceso.

Ma possiamo usare strategie più prudenti:

- eseguire vecchia e nuova trasformazione in parallelo;
- confrontare metriche per alcuni giorni;
- pubblicare il nuovo dataset a un gruppo limitato di utenti;
- mantenere temporaneamente entrambe le versioni;
- definire criteri espliciti di rollback.

Questo è particolarmente importante per semantic layer e KPI executive.

## La regola

> **Automazione non significa eliminare il controllo. Significa incorporare il controllo nel processo.**
