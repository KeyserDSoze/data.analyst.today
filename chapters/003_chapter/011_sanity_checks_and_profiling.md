## 3.10 Sanity check e data profiling: prima di descrivere il business, descrivi il dataset

Prima di cercare pattern sofisticati conviene costruire una fotografia elementare del dato. Non perché i controlli semplici siano “junior”, ma perché molte anomalie costose diventano visibili proprio quando confrontiamo ciò che **abbiamo** con ciò che **ci aspettiamo**.

Il profiling non coincide con un `describe()` o con una collezione di statistiche descrittive. Minimi, massimi, medie e quantili sono utili soltanto quando diventano confronti contro un modello del processo: quante righe dovrebbero esserci, quale periodo dovrebbe essere coperto, quali chiavi dovrebbero essere uniche, quali categorie dovrebbero comparire, quali latenze sono normali.

La differenza tra riepilogo e profiling sta nella baseline. `2.000.000 righe` è un dato descrittivo; se ieri la stessa fonte ne conteneva 2,4 milioni e il business non è cambiato, la differenza diventa una pista investigativa.

## Profilare significa cercare rotture nel processo

Un set minimo di controlli dovrebbe permetterci di ricostruire volume, cardinalità delle chiavi, intervallo temporale, missing dei campi critici, distribuzioni principali, valori fuori dominio, duplicati al grain atteso, record orfani e freshness. Ma questi controlli diventano davvero utili quando vengono osservati nel tempo e lungo le dimensioni che possono spiegare un cambiamento.

### Caso simulato/composito — Il giorno con il doppio delle letture

VerdeMare Energy gestisce impianti fotovoltaici e riceve ogni notte le letture dei contatori. Un analista deve calcolare la produzione media giornaliera di luglio. Il dataset contiene circa 46 milioni di letture e nessun errore evidente a livello di schema.

Prima dell'analisi conta i record per giorno. Quasi tutto il mese oscilla attorno a **1,48 milioni** di righe; il 18 luglio compaiono **2,96 milioni**.

Esattamente il doppio.

Il recovery di una pipeline aveva ricaricato la stessa giornata. Non serviva un algoritmo sofisticato di anomaly detection: bastava conoscere il volume atteso e guardare la serie temporale prima di calcolare la metrica di business.

La stessa logica vale per i missing. Un `missing_rate(delivery_date) = 4,8%` può sembrare moderato finché non viene scomposto per carrier:

```text
Carrier A: 0,7%
Carrier B: 1,1%
Carrier C: 19,4%
```

A quel punto la domanda non è più “quanti valori mancano?”, ma “che cosa succede nell'integrazione del Carrier C?”. Il profiling ha trasformato una proprietà aggregata in un'ipotesi sul processo.

## Il tempo e le categorie hanno memoria

Un dataset può essere valido riga per riga e incompleto come storia. Giorni mancanti, volumi che cambiano improvvisamente, timestamp futuri, backfill, nuove timezone o categorie che compaiono dopo una release sono tutti segnali che il sistema di produzione è cambiato.

Anche i campi categoriali raccontano queste transizioni. Un `country` con valori `IT`, `ITA`, `Italy`, `Italia`, `italy` e `NULL` non è soltanto “sporco”: può rivelare che più sistemi stanno contribuendo alla stessa colonna con standard differenti. Normalizzare le etichette senza capire l'origine può nascondere proprio il confine fra le sorgenti.

Per questo i controlli migliori derivano da **invarianti** o aspettative esplicite: un ordine dovrebbe avere almeno una riga d'ordine; la popolazione degli account non dovrebbe diminuire del 20% senza un evento noto; una valuta deve appartenere al dominio previsto; la data massima deve essere compatibile con la SLA di aggiornamento.

Quando queste aspettative si dimostrano stabili e importanti, potranno diventare controlli automatici. Prima, però, servono a guidare la lettura iniziale del dataset.

La disciplina dei primi minuti può essere riassunta in poche domande collegate: quante righe ho e quante dovrei averne? Quale periodo sto osservando? Quali chiavi dovrebbero essere uniche? Dove manca il dato? Quali categorie o distribuzioni sono cambiate recentemente? Quale evento di sistema potrebbe spiegare la rottura?

> **Il profiling non dimostra che il dataset sia corretto. Serve a trovare rapidamente i motivi per cui potrebbe non esserlo e a trasformarli in domande verificabili sul processo che lo produce.**
