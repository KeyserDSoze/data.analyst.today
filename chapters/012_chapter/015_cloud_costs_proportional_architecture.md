## 12.14 Architettura proporzionata: comprare affidabilità dove cambia la decisione

Ogni garanzia architetturale ha un costo.

Ridurre la latenza, aumentare retention, duplicare regioni, mantenere più copie, aggiungere observability o servire workload sempre disponibili può essere perfettamente giustificato.

Ma non gratis.

La domanda quindi non è:

> qual è l'architettura più robusta che possiamo costruire?

È:

> **quale livello di affidabilità, latenza e recovery è economicamente proporzionato alla decisione che il sistema supporta?**

### Caso simulato/composito — BrightMart e il real time indiscriminato

BrightMart vuole modernizzare il reporting di:

- vendite;
- margine;
- stock;
- resi;
- promozioni.

La prima proposta usa un percorso streaming a bassissima latenza per tutto.

Il discovery mostra però:

| Use case | Quando serve agire |
|---|---|
| stock-out prodotti critici | entro 10 minuti |
| vendite negozio | ogni 30–60 minuti |
| replenishment standard | una volta al giorno |
| finance | giornaliero / close |
| board | settimanale |

La soluzione diventa differenziata:

```text
critical stock events → near real time
sales operations      → micro-batch
finance               → reconciled daily batch
board                  → certified weekly serving
```

Non stiamo “risparmiando” degradando il servizio.

Stiamo evitando di comprare millisecondi dove nessuno può usarli.

### Freshness curve: il valore marginale non è lineare

Passare da:

```text
T+24h → T+1h
```

può cambiare radicalmente un processo operations.

Passare da:

```text
1 min → 1 sec
```

può non cambiare nulla.

Per ogni use case possiamo immaginare una curva:

```text
business value gained by lower latency
vs
engineering + infrastructure cost
```

Il punto ottimale non coincide necessariamente con la minima latenza tecnicamente raggiungibile.

### Affidabilità ha una curva simile

Un SLO del 99% e uno del 99,999% possono richiedere architetture molto diverse.

Google SRE sottolinea che obiettivi del 100% sono spesso indesiderabili perché possono imporre soluzioni eccessivamente conservative e costose.

Fonte:
https://sre.google/sre-book/service-level-objectives/

Questa idea vale anche per i data products.

Un report di planning mensile non richiede lo stesso recovery design di un sistema che blocca frodi in tempo reale.

### Caso reale documentato — VMO2 e TCO

Nel caso Virgin Media O2 discusso in 12.8, Google Cloud riporta una riduzione del TCO di circa il 30% rispetto a piattaforme on-premises equivalenti nel percorso di consolidamento e modernizzazione.

Fonte:
https://cloud.google.com/customers/virgin-media-o2-data-platform-migration

La lezione non è che cloud o serverless siano sempre più economici.

È che il TCO comprende anche:

- infrastruttura duplicata;
- capacity limits;
- licenze;
- manutenzione;
- skill specialistiche;
- tempo di delivery;
- gestione operativa.

### TCO: il prezzo del compute è soltanto una riga

Un modello utile è:

```text
TCO =
infrastructure
+ managed service / licenses
+ storage and network
+ engineering time
+ on-call / incident response
+ maintenance
+ duplicated pipelines
+ change cost
+ failure cost
```

Non serve stimare ogni voce al centesimo per migliorare una decisione architetturale.

Serve evitare di confrontare due soluzioni soltanto sulla tariffa per CPU.

### Cost of failure

La complessità aggiuntiva può essere giustificata da ciò che evita.

Esempio:

```text
pipeline A
costa meno ma fallisce 3 volte/mese durante una decisione critica

pipeline B
costa di più ma riduce fortemente quel rischio
```

Il confronto deve includere:

- decisioni ritardate;
- ore di analisti bloccati;
- incident response;
- eventuali decisioni prese su dati incompleti.

### Cost of complexity

Ogni nuovo componente introduce anche:

- configurazione;
- access control;
- monitoring;
- upgrade;
- failure mode;
- competenza necessaria.

Una pipeline con 20.000 righe al giorno e un report mattutino non diventa più matura perché usa una piattaforma distribuita multi-cluster.

### Underengineering esiste

La regola “parti semplice” non significa “resta manuale per sempre”.

Un foglio condiviso può essere adeguato finché:

- utenti sono pochi;
- dato non è sensibile;
- refresh può essere manuale;
- audit non è critico.

Quando cambiano scala e rischio, il costo nascosto della soluzione semplice può superare quello di una piattaforma più strutturata.

### Reversibilità architetturale

Quando l'incertezza è alta, preferiamo spesso scelte che permettano di evolvere.

Esempio:

```text
batch hourly oggi
```

può essere una buona scelta se:

- soddisfa il requisito;
- il raw event stream è conservato;
- domani possiamo aggiungere un consumer near-real-time senza rifare la sorgente.

Semplice non deve significare irreversibile.

### Campo della Data Flow Architecture Map

Per ogni componente rilevante annotiamo:

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

### Architecture review in otto domande

1. quale decisione giustifica questo componente?
2. quale SLO deve sostenere?
3. cosa succede se lo eliminiamo?
4. quanta capacità viene realmente usata?
5. qual è il costo di gestione, non solo di compute?
6. quale failure mode nuovo introduce?
7. possiamo soddisfare il requisito con meno accoppiamento?
8. quale segnale ci dirà che la soluzione è diventata troppo piccola?

> **La maturità architetturale non consiste nel comprare la massima scalabilità. Consiste nel pagare per la complessità che riduce davvero rischio o time-to-decision, mantenendo il resto il più semplice possibile.**
