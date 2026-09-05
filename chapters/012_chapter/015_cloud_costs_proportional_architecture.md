## 12.14 Architettura proporzionata: comprare affidabilità dove cambia la decisione

Ogni garanzia architetturale ha un costo. Ridurre latenza, aumentare retention, duplicare regioni, mantenere replay più lungo, aggiungere observability o servire workload sempre disponibili può essere perfettamente giustificato. Ma non è gratis.

La domanda finale del capitolo è quindi:

> **Quale livello di affidabilità, latenza e recovery è economicamente proporzionato alla decisione che il sistema supporta?**

### Caso simulato/composito — BrightMart e il real time indiscriminato

BrightMart vuole modernizzare vendite, margine, stock, resi e promozioni. La prima proposta prevede streaming a bassissima latenza per tutto. Il discovery mostra invece:

| Use case | Quando serve agire |
|---|---|
| stock-out prodotti critici | entro 10 minuti |
| vendite negozio | ogni 30–60 minuti |
| replenishment standard | una volta al giorno |
| Finance | giornaliero / close |
| board | settimanale |

La soluzione diventa differenziata:

```text
critical stock events → near real time
sales operations      → micro-batch
finance               → reconciled daily batch
board                  → certified weekly serving
```

Non stiamo degradando il servizio per risparmiare. Stiamo evitando di comprare millisecondi dove nessun consumer può trasformarli in un'azione migliore.

### Il valore marginale della freshness

Passare da T+24h a T+1h può cambiare radicalmente un processo Operations. Passare da un minuto a un secondo può non cambiare nulla. Lo stesso vale per l'affidabilità: un SLO del 99% e uno del 99,999% possono richiedere architetture molto diverse.

Google SRE ricorda che il 100% è spesso indesiderabile perché può imporre soluzioni eccessivamente conservative e costose.

Fonte: https://sre.google/sre-book/service-level-objectives/

### Il costo è più largo del compute

Nel caso VMO2, Google Cloud riporta per il percorso mobile migrato a BigQuery/Dataflow **+400% di capacità** e **-30% di TCO**. La lezione non è che il cloud sia sempre più economico; è che il TCO comprende infrastruttura duplicata, licenze, skill specialistiche, manutenzione, delivery time e gestione operativa.

Fonte: https://cloud.google.com/customers/virgin-media-o2-data-platform-migration

Un modello utile è:

```text
TCO =
infrastructure
+ managed services / licenses
+ storage and network
+ engineering time
+ on-call / incident response
+ maintenance
+ duplicated pipelines
+ change cost
+ failure cost
```

Non dobbiamo stimare ogni voce al centesimo. Dobbiamo evitare confronti che guardano soltanto la tariffa per CPU e ignorano costo della complessità e costo del failure.

### Semplice non significa sottodimensionato

Una soluzione manuale può essere adeguata finché utenti, frequenza, rischio e audit restano limitati. Quando questi requisiti cambiano, il costo nascosto della soluzione “semplice” può superare quello di una piattaforma più strutturata.

Allo stesso tempo, una pipeline da 20.000 righe al giorno non diventa più matura perché usa un cluster distribuito multi-region. Ogni nuovo componente introduce configurazione, access control, monitoring, upgrade, failure mode e skill da mantenere.

Quando l'incertezza è alta preferiamo inoltre scelte reversibili. Un batch orario può essere sufficiente oggi se preserviamo il raw event stream e lasciamo aperta la possibilità di aggiungere domani un consumer near-real-time senza ridisegnare la sorgente.

Nella Data Flow Architecture Map annotiamo:

```text
business requirement it satisfies:
cost driver:
utilization:
reliability/freshness gained:
failure cost mitigated:
operational skill required:
scale trigger for redesign:
can simplify? sì/no
can evolve? sì/no
```

> **La maturità architetturale consiste nel pagare per la complessità che riduce davvero rischio o time-to-decision, mantenendo il resto il più semplice e reversibile possibile.**
