## 3.15 Controlli automatici: trasformare le aspettative in segnali

Una Data Readiness Review manuale può dirci che il dataset di oggi è plausibile.

Non garantisce che lo sarà domani.

Quando una fonte alimenta analisi ricorrenti, alcune aspettative scoperte durante il profiling dovrebbero diventare controlli automatici.

Il ruolo dell'analista non è necessariamente implementare tutta l'infrastruttura di observability. È però spesso l'analista a conoscere **quali violazioni cambierebbero il significato di una metrica**.

### Dal sanity check alla regola

Durante un'indagine possiamo osservare:

> La tabella clienti contiene normalmente tra 2,3 e 2,5 milioni di account.

Se quella proprietà è importante per i report, può diventare una regola:

```text
2.300.000 <= row_count(customer_daily) <= 2.550.000
```

Oppure possiamo scoprire che:

> `order_id` deve essere unico nel dataset degli ordini completati.

Anche questa aspettativa può diventare un test.

La guida britannica per i data quality action plan raccomanda proprio di definire regole di qualità collegate allo scopo del dato, con target e livelli di performance, invece di misurare indiscriminatamente ogni campo.[^gov-dq-plan]

### Cinque famiglie di controlli

**1. Schema**

Verificano che la struttura attesa esista.

Esempi:

- colonna critica presente;
- tipo compatibile;
- enum non modificato senza gestione;
- unità o metadati obbligatori disponibili.

**2. Constraint e dominio**

Verificano regole locali.

Esempi:

- chiave unica;
- range ammesso;
- data coerente con il processo;
- stato appartenente ai valori previsti.

**3. Relazioni**

Controllano che collegamenti attesi tra dataset siano plausibili.

Esempio: la quota di ordini con `product_id` non riconosciuto deve restare sotto una soglia accettabile.

**4. Volume e freshness**

Controllano se il dato è arrivato e se la quantità osservata è compatibile con il processo.

**5. Distribuzione e composizione**

Verificano cambiamenti inattesi nelle caratteristiche del dataset.

Esempi:

- improvviso aumento dei null;
- una categoria che passa dal 12% al 70%;
- distribuzione degli importi completamente diversa dallo storico;
- segmento che scompare.

### Caso simulato/composito — 420.000 account scomparsi

Una società SaaS possiede circa **2,4 milioni di account**.

Ogni notte una pipeline aggiorna la tabella usata da CRM e dashboard.

Alle 7:20 un controllo sul volume segnala:

```text
row_count(customer_daily) = 1.981.442
expected range = 2.300.000 - 2.550.000
STATUS = FAIL
```

Il team scopre che una modifica alla trasformazione ha introdotto un `INNER JOIN` con la tabella dei consensi marketing.

Gli account privi di consenso sono scomparsi dal dataset.

Il risultato era "pulito" a livello di singola riga:

- nessuna chiave duplicata;
- nessun campo critico nullo;
- tipi corretti;
- query completata con successo.

Era la **popolazione** a essere sbagliata.

Un semplice controllo sul volume ha impedito di pubblicare un dataset semanticamente incompleto.

### Un test che passa non dimostra che il dato sia vero

Questo limite va reso esplicito.

Possiamo verificare che:

```text
0 <= discount_pct <= 100
```

ma non sapere se `discount_pct = 35` descrive davvero lo sconto applicato al cliente.

Possiamo verificare che tutti gli ordini abbiano un `customer_id`, ma non sapere se l'identity resolution abbia associato ogni ordine alla persona corretta.

I test automatici dimostrano soprattutto che il dato **non viola alcune aspettative note**.

Sono potenti, ma non sostituiscono riconciliazione, domain knowledge e review metodologica.

### Soglie che derivano dal processo

`row_count > 0` è quasi sempre troppo debole.

Se una tabella passa da 2,4 milioni di righe a 12.000, il test passa comunque.

Le soglie devono riflettere:

- volatilità normale;
- stagionalità;
- giorno della settimana;
- crescita attesa;
- latenze;
- eventi di business noti.

In alcuni casi una soglia fissa è sufficiente. In altri serve una baseline dinamica.

### Severità e blocco

Non ogni anomalia deve interrompere la pubblicazione.

Una classificazione utile è:

- **info/warning**: variazione da investigare, ma dato ancora utilizzabile;
- **failure**: proprietà importante violata, analisi da sospendere o limitare;
- **critical/blocking**: il data product non deve essere pubblicato.

La severità dovrebbe dipendere dall'impatto sulla decisione, non dalla stranezza tecnica dell'errore.

### Alert senza owner = rumore

Un controllo ha valore solo se esiste un circuito operativo:

**regola → rilevazione → owner → investigazione → decisione → correzione → apprendimento**

Se nessuno sa chi deve reagire o che cosa fare, cinquanta alert non aumentano l'affidabilità. Creano alert fatigue.

### La domanda dell'analista

Dopo una buona Data Readiness Review, chiediti:

> **Quali tre o cinque proprietà, se cambieranno domani, potrebbero rendere silenziosamente falsa la stessa analisi?**

Quelle proprietà sono ottime candidate per i primi controlli automatici.

[^gov-dq-plan]: UK Government Data Quality Hub, *Data quality action plan implementation guide*. https://www.gov.uk/government/publications/implement-a-data-quality-action-plan/data-quality-action-plan-implementation-guide