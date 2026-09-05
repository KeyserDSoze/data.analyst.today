## 3.15 Controlli automatici: trasformare le aspettative in segnali

Una Data Readiness Review manuale può dirci che il dataset di oggi è plausibile. Non garantisce che lo sarà domani. Quando una fonte alimenta analisi ricorrenti, le proprietà importanti scoperte durante il profiling dovrebbero progressivamente diventare controlli automatici.

L'analista non deve necessariamente costruire tutta l'infrastruttura di observability, ma spesso è la persona che conosce meglio **quali violazioni cambierebbero il significato di una metrica o la popolazione di una decisione**. È questa conoscenza che deve essere trasformata in regole.

Supponiamo di sapere che la tabella clienti contiene normalmente fra 2,3 e 2,5 milioni di account. Se quella popolazione alimenta dashboard e campagne, l'aspettativa può diventare un controllo:

```text
2.300.000 <= row_count(customer_daily) <= 2.550.000
```

Se sappiamo che `order_id` deve essere unico tra gli ordini completati, l'unicità diventa un secondo test. Se una valuta deve appartenere a un insieme ammesso, la regola di dominio può diventare un terzo.

Le linee guida britanniche più recenti sui data quality action plan insistono proprio su questo approccio: definire regole legate allo scopo del dato, fissare target e performance band e concentrarsi sui campi critici invece di misurare indiscriminatamente tutto.[^gov-dq-plan]

## Dalla proprietà locale al circuito operativo

I controlli possono agire su famiglie diverse: struttura dello schema, vincoli e domini, relazioni tra dataset, volume e freshness, distribuzioni e composizione della popolazione. La classificazione è utile, ma la domanda più importante resta sempre la stessa: **che cosa significherebbe per l'uso del dato se questa proprietà venisse violata?**

Un controllo sullo schema segnala che una colonna critica è scomparsa o ha cambiato tipo. Un test di relazione può misurare la quota di `product_id` senza corrispondenza nel catalogo. Un controllo di freshness verifica che la sorgente abbia raggiunto la SLA. Un test di distribuzione può scoprire che una categoria è passata improvvisamente dal 12% al 70%.

Nessuno di questi test vale per la sua sofisticazione tecnica. Vale per la capacità di intercettare una modifica che renderebbe falsa o non comparabile l'analisi.

### Caso simulato/composito — 420.000 account scomparsi

Una società SaaS possiede circa **2,4 milioni di account**. Ogni notte una pipeline aggiorna la tabella utilizzata da CRM e dashboard. Alle 7:20 un controllo sul volume segnala:

```text
row_count(customer_daily) = 1.981.442
expected range = 2.300.000 - 2.550.000
STATUS = FAIL
```

Una modifica alla trasformazione ha introdotto un `INNER JOIN` con la tabella dei consensi marketing. Gli account privi di consenso sono scomparsi dal dataset.

La tabella appare “pulita” se osservata riga per riga: nessuna chiave duplicata, nessun campo critico nullo, tipi corretti, query completata con successo. È la **popolazione** a essere sbagliata. Un controllo estremamente semplice ha quindi protetto il significato del data product meglio di molti test locali.

## Un test che passa non dimostra che il dato sia vero

Questo limite deve restare esplicito. Possiamo verificare che `0 <= discount_pct <= 100` senza sapere se `35` sia davvero lo sconto applicato. Possiamo verificare che ogni ordine possieda un `customer_id` senza sapere se l'identity resolution abbia associato l'ordine alla persona corretta.

I test automatici dimostrano soprattutto che il dato **non viola alcune aspettative note**. Non sostituiscono riconciliazione, domain knowledge e review metodologica.

Anche le soglie devono derivare dal processo. `row_count > 0` è quasi sempre troppo debole: una tabella che passa da 2,4 milioni di righe a 12.000 soddisfa ancora la condizione. Una buona soglia deve riflettere volatilità normale, stagionalità, giorno della settimana, crescita attesa, latenze ed eventi di business noti. In alcuni casi basta un intervallo fisso; in altri serve una baseline dinamica.

## Severità e ownership

Non ogni deviazione deve bloccare la pubblicazione. Alcune sono **warning** da investigare, altre rendono il dato temporaneamente inutilizzabile, altre ancora devono impedire l'uscita del data product. La severità dovrebbe seguire l'impatto sulla decisione, non la stranezza tecnica dell'anomalia.

Soprattutto, un alert senza owner e senza azione prevista è soltanto rumore. Il vero sistema è:

**regola → rilevazione → owner → investigazione → decisione → correzione → apprendimento**

Se nessuno sa chi deve reagire, moltiplicare gli alert aumenta l'alert fatigue invece dell'affidabilità.

Dopo una Data Readiness Review, una domanda pratica aiuta a scegliere da dove iniziare:

> **Quali tre o cinque proprietà, se cambiassero domani, renderebbero silenziosamente falsa la stessa analisi?**

Quelle proprietà sono ottime candidate per i primi controlli automatici.

---

### Fonte

[^gov-dq-plan]: UK Government Data Quality Hub, *Implementing a data quality action plan*. https://www.gov.uk/government/publications/implement-a-data-quality-action-plan/data-quality-action-plan-implementation-guide
