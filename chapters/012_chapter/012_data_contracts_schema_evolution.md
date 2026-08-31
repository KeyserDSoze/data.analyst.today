## 12.12 Data contracts e schema evolution: cambiare senza rompere tutto

Molti incidenti dati non nascono da una query sbagliata, ma da una sorgente che cambia senza che i consumer lo sappiano.

Una colonna viene rinominata. Un tipo passa da intero a stringa. Un campo prima obbligatorio diventa opzionale. Un evento cambia significato ma mantiene lo stesso nome.

Tecnicamente il sistema puo' continuare a funzionare.

Semanticamente, pero', il dato puo' essere gia' rotto.

### Il data contract

Un **data contract** rende esplicita l'interfaccia tra chi produce un dato e chi lo consuma.

Può includere:

- schema;
- tipi;
- significato dei campi;
- chiavi;
- regole di nullability;
- freshness;
- completezza;
- ownership;
- compatibilita' attesa;
- policy di evoluzione.

Google Cloud descrive i data contract come accordi formali e machine-readable tra producer e consumer, includendo schema, semantica, metriche di qualita' e SLO come freshness e completeness.

### Caso pubblico: VMO2

Google Cloud ha documentato l'uso dei data contract da parte di Virgin Media O2 per supportare prodotti dati e AI su scala.

Il punto interessante non e' il formato specifico del contratto, ma il cambio organizzativo: la qualita' non viene trattata soltanto come controllo downstream, bensì come responsabilita' esplicita gia' all'interfaccia tra producer e consumer.

### Caso realistico: FleetOne

FleetOne gestisce telemetria per 180.000 veicoli.

Il payload contiene:

```json
{
  "vehicle_id": "A8821",
  "speed": 74,
  "engine_temp": 91
}
```

Il team firmware rilascia una nuova versione e aggiunge:

```json
"battery_health": 0.88
```

Un cambiamento additivo potrebbe essere relativamente innocuo.

Due settimane dopo, pero', `speed` viene cambiato da km/h a m/s per allinearsi a uno standard interno. Il nome della colonna rimane `speed`.

Le pipeline continuano a funzionare.

Il dashboard mostra improvvisamente una riduzione enorme della velocita' media.

Non c'e' un errore tecnico evidente. C'e' un errore **semantico**.

### Schema evolution

Le piattaforme moderne possono gestire alcune evoluzioni di schema automaticamente.

Databricks Auto Loader, per esempio, supporta modalita' diverse per nuovi campi e cambiamenti di schema: aggiunta automatica di colonne, rescue dei dati inattesi, oppure fail esplicito quando compaiono nuove colonne.

Questa flessibilita' e' utile, ma non risolve una domanda fondamentale:

> il nuovo schema conserva lo stesso significato business?

Un sistema puo' adattarsi perfettamente a una nuova colonna e continuare a calcolare una metrica sbagliata.

### Compatibilita'

Possiamo pensare a tre categorie semplici.

**Backward compatible**  
I consumer esistenti continuano a funzionare.

Esempio: aggiungere una colonna opzionale.

**Breaking change**  
I consumer devono essere aggiornati.

Esempio: rinominare `customer_id` in `account_id` senza alias o versione.

**Semantic breaking change**  
La struttura puo' rimanere identica, ma cambia il significato.

Esempio:

```text
revenue
prima: lordo IVA inclusa
poi: netto IVA esclusa
```

Questo terzo caso e' spesso il piu' pericoloso per l'analista.

### Versionare quando serve

Una soluzione pragmatica e' introdurre una nuova versione:

```text
orders_v1
orders_v2
```

oppure versionare il contratto/evento.

Non bisogna abusare delle versioni, ma un breaking change nascosto costa spesso piu' della complessita' di una migrazione esplicita.

### Metodo operativo

Prima di modificare una sorgente critica chiedere:

1. quali consumer dipendono da questo campo?
2. il cambiamento e' strutturale o semantico?
3. e' backward compatible?
4. esistono test contrattuali?
5. serve una nuova versione?
6. qual e' il piano di migrazione?
7. per quanto tempo convivranno vecchio e nuovo formato?

**Schema evolution e' un problema tecnico. Semantic evolution e' un problema analitico. Servono entrambi sotto controllo.**

---

### Fonti pubbliche

- Google Cloud, caso VMO2 sui data contracts.
- Databricks, documentazione su schema inference ed evolution in Auto Loader.
