## 18.12 Checklist ed esercizi
## Checklist: quando un'analisi sta diventando un prodotto analitico

Prima di trasformare un'analisi ricorrente in sistema, chiediamoci:

- esiste una decisione ricorrente chiaramente supportata?
- esiste un owner di business?
- esiste un owner tecnico/analitico?
- le metriche hanno definizioni certificate?
- grain, filtri, timezone e regole temporali sono espliciti?
- esistono target di freshness e completezza?
- sappiamo cosa succede quando il dato è in ritardo?
- esistono test strutturali, statistici, di riconciliazione e semantici?
- le modifiche sono versionate e reviewate?
- esiste una strategia di rollback?
- costi e workload sono attribuibili?
- misuriamo adoption e impatto, non soltanto utilizzo?
- eventuali agenti AI hanno scope, authority, stop condition ed escalation?
- possiamo ricostruire come è stato prodotto un output importante?

Se molte risposte sono “no”, probabilmente non abbiamo ancora un prodotto analitico: abbiamo un insieme di asset.

## Esercizio 1 — Il report fragile

Ogni mattina alle 8:00 un report commerciale viene inviato automaticamente a 200 manager.

Negli ultimi tre mesi:

- è arrivato in ritardo 7 volte;
- due volte ha mostrato dati incompleti;
- nessuno sa quale versione della metrica pipeline coverage sia ufficiale;
- il processo costa circa €9.000 al mese;
- il 60% dei destinatari non apre mai il report.

Progetta:

1. gli SLO principali;
2. il set minimo di test;
3. l'ownership;
4. una strategia di adoption;
5. una strategia di cost management;
6. i criteri per decidere se il report debba continuare a esistere.

## Esercizio 2 — Breaking change

Il team Product cambia la definizione di `trial_started`.

Prima l'evento veniva emesso alla creazione dell'account.

Ora viene emesso al primo utilizzo effettivo di una feature premium.

Domande:

- quali metriche downstream potrebbero cambiare?
- quali test tecnici non rileverebbero il problema?
- quali stakeholder devono approvare?
- serve una nuova versione della metrica?
- come comunicheresti il cambio in una serie storica?

## Esercizio 3 — AI analyst agent

Un agente può:

- interrogare il warehouse;
- creare SQL;
- generare grafici;
- inviare una sintesi su Slack;
- aprire ticket di data incident.

Non può modificare il warehouse.

Definisci:

- scope;
- strumenti consentiti;
- logging;
- eval;
- stop condition;
- escalation;
- livelli di approvazione.

Poi considera una seconda versione dell'agente che può anche sospendere automaticamente una campagna marketing da €500.000 al mese.

Quali controlli devono cambiare?

## Esercizio 4 — Misurare il valore

Una nuova piattaforma self-service ha:

- 2.400 utenti registrati;
- 61% utenti attivi mensili;
- 490 dashboard;
- 38 metriche certificate;
- 74 metriche duplicate non certificate;
- 11 incidenti di dati al mese;
- 4 ore medie di riconciliazione prima del monthly business review.

Proponi un sistema di metriche che distingua:

- adoption;
- reliability;
- semantic consistency;
- business impact;
- cost efficiency.

## Esercizio 5 — Architettura proporzionata

Tre processi:

**A.** forecast trimestrale aggiornato una volta al mese;

**B.** monitoraggio frodi con decisione in pochi secondi;

**C.** dashboard executive consultata ogni mattina.

Disegna per ciascuno:

- latency target;
- data pipeline;
- testing;
- osservabilità;
- livello di automazione;
- budget operativo;
- approccio a failure e rollback.

L'obiettivo non è costruire l'architettura più avanzata.

È costruire quella coerente con il costo dell'errore e il valore della velocità.

## Chiusura del capitolo

Un'organizzazione matura non dipende da un analista eroico che sa dove sono tutti i file, ricorda tutte le eccezioni e aggiusta ogni problema a mano.

Costruisce un sistema nel quale conoscenza, semantica, controlli e responsabilità sono incorporati nel processo.

Il passaggio è:

**analisi → asset → prodotto → sistema → capacità organizzativa**

E a ogni passaggio cambiano le responsabilità dell'analista.

> **La vera scalabilità non è fare più analisi con le stesse persone. È fare in modo che le decisioni possano continuare a essere supportate bene anche quando aumentano utenti, dati, automazione e complessità.**
