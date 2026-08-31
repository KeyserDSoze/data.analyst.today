## 18.9 Adoption: un prodotto analitico non ha successo perché esiste
Una dashboard può essere perfetta e non essere usata.

Un modello può essere accurato e non cambiare alcuna decisione.

Un semantic layer può essere tecnicamente elegante e non ridurre le metriche duplicate.

Per questo la qualità di un prodotto analitico non si misura soltanto con uptime e data quality.

Serve misurare anche **adozione e impatto**.

## Metriche di utilizzo

Possibili indicatori:

- utenti attivi;
- frequenza di utilizzo;
- retention degli utenti del prodotto;
- query o report consultati;
- percentuale di decisioni/processi che usano il prodotto;
- tempo medio dalla domanda alla risposta.

Ma anche qui bisogna evitare vanity metrics.

Mille visualizzazioni non significano mille decisioni migliori.

## Metriche di fiducia

Possiamo misurare:

- numero di riconciliazioni fallite;
- incidenti per mese;
- tempo medio di risoluzione;
- percentuale di KPI certificati;
- numero di definizioni duplicate;
- quota di report costruiti su semantic layer approvati.

## Metriche di outcome

Sono le più difficili e le più importanti.

Esempi:

- riduzione del tempo di planning;
- riduzione degli errori di forecast;
- diminuzione degli stock-out;
- incremento del tasso di decisioni sperimentate prima del rollout;
- riduzione del tempo speso a riconciliare numeri discordanti;
- miglioramento del margine o del servizio attribuibile a decisioni supportate dal prodotto.

## Caso realistico: 1.200 utenti, zero impatto

Un'azienda lancia un portale self-service.

Dopo sei mesi:

- 1.200 utenti registrati;
- 18.000 sessioni;
- 320 dashboard create.

Il progetto viene dichiarato un successo.

Ma le riunioni executive continuano a iniziare con:

> “Quale revenue stiamo usando?”

Un audit trova 23 definizioni attive di `active_customer` e 11 di `net_revenue`.

L'adozione è alta.

La standardizzazione è bassa.

Il prodotto ha democratizzato l'accesso, non il significato.

## North Star del prodotto analitico

Una possibile domanda guida è:

> **Quante decisioni importanti vengono prese più velocemente e con meno ambiguità grazie a questo sistema?**

Non sempre potremo trasformarla in una singola metrica.

Ma è una domanda migliore di “quante dashboard abbiamo?”.

## Adoption come problema di prodotto

Se un asset non viene usato, non è automaticamente colpa degli utenti.

Potrebbe avere:

- scarsa discoverability;
- definizioni poco comprensibili;
- latency troppo alta;
- workflow separato dal processo reale;
- mancanza di fiducia;
- troppi dati e poche decisioni;
- nessun owner che ne accompagni l'adozione.

> **Il valore analitico viene realizzato quando un'informazione affidabile entra davvero nel flusso di una decisione.**
