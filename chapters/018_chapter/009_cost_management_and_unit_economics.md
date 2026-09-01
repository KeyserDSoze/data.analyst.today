## 18.8 Cost-to-serve: un prodotto analitico deve avere anche un'economia

Una piattaforma analitica può diventare tecnicamente più sofisticata e contemporaneamente economicamente peggiore.

I costi crescono attraverso migliaia di decisioni apparentemente piccole:

- refresh più frequenti;
- copie regionali;
- query senza pruning;
- retention eccessiva;
- ambienti dimenticati;
- notebook sempre accesi;
- modello più grande del necessario;
- streaming per decisioni giornaliere;
- agenti che ripetono query costose;
- dashboard che nessuno usa più.

Il problema non è semplicemente:

> “Spendiamo troppo.”

È:

> **“Quale prodotto, consumer o decisione genera questo costo, e il valore ottenuto giustifica il livello di servizio che stiamo pagando?”**

## Cost visibility prima dell'optimization

Non possiamo governare un costo che vive soltanto nella fattura aggregata della piattaforma.

Per un portfolio analitico servono livelli di allocazione coerenti con il modo in cui prendiamo decisioni.

Possibili dimensioni:

- team;
- domain;
- data product;
- workload;
- environment;
- consumer class;
- region;
- model/agent;
- criticality tier.

Non tutto deve essere allocato al centesimo.

Serve abbastanza trasparenza da cambiare comportamento.

## Caso reale documentato: FinOps e cost allocation

La FinOps Foundation definisce l'**Allocation** come la capacità di assegnare costi e utilizzo a team, progetti o altre unità responsabili, includendo una strategia esplicita per costi condivisi e metadata.

Fonte: https://www.finops.org/framework/capabilities/allocation/

La stessa guida osserva che non tutti i shared cost devono necessariamente essere distribuiti con un modello estremamente sofisticato. In alcuni casi è legittimo decidere consapevolmente di mantenerli centrali: ciò che conta è che la scelta sia esplicita e utile al livello di maturità dell'organizzazione.

Questa idea evita un anti-pattern frequente:

> spendere più per calcolare un'allocazione perfetta di quanto l'allocazione possa far risparmiare.

## Cost allocation strategy

Possiamo distinguere:

### Direct cost

Attribuibile chiaramente a un prodotto.

Esempi:

- warehouse compute di una pipeline dedicata;
- API usage di un modello;
- licenza specifica.

### Shared cost allocabile

Piattaforma condivisa il cui consumo può essere stimato con:

- query time;
- bytes processed;
- storage;
- request count;
- active users;
- workload unit.

### Shared central cost

Capability comune che decidiamo di finanziare centralmente:

- catalogo;
- governance;
- base observability;
- support platform.

La strategia deve essere documentata, non nascosta nei report Finance.

## Dal costo totale alla unit economics analitica

La FinOps Foundation definisce la **Unit Economics** come la pratica di collegare uso/costo tecnologico al valore dei prodotti, servizi o attività organizzative, distinguendo metriche di efficienza tecnica e metriche di business.

Fonte: https://www.finops.org/framework/capabilities/unit-economics/

Per analytics, unit metric possibili sono:

- costo per 1.000 query;
- costo per refresh;
- costo per milione di eventi processati;
- costo per forecast prodotto;
- costo per account scored;
- costo per decision feed servito;
- costo per consumer attivo;
- costo per workload business unit.

Ma attenzione.

La metrica:

> costo per query

può incentivare meno query anche quando una query crea valore.

La unit metric deve rappresentare l'economia della capability, non soltanto ciò che il cloud provider fattura.

## Caso simulato/composito: la dashboard “gratuita” da €31.000 al mese

Un marketplace costruisce una executive dashboard.

All'inizio costa poco.

Nel tempo vengono aggiunti:

- refresh ogni 10 minuti;
- 34 visualizzazioni;
- due anni di eventi raw letti ripetutamente;
- copie per cinque regioni;
- cinque semantic model quasi identici;
- export automatici;
- caching disallineato;
- un agente che ricalcola ogni ora summary e anomalie.

Il costo attribuito al prodotto arriva a circa **€31.000/mese**.

La prima reazione è:

> “Serve più capacità.”

Il team ricostruisce il demand profile.

Scopre che:

- il CEO la usa una volta al giorno;
- il weekly review usa snapshot giornaliero;
- soltanto due metriche operative richiedono freshness < 1 ora;
- l'80% delle query ripete aggregazioni già calcolabili a monte;
- i cinque modelli regionali possono condividere core semantics;
- l'agente produce 24 summary al giorno, ma ne vengono letti in media 1,7.

La soluzione non è una micro-ottimizzazione tecnica.

È un **service-level redesign**.

## Reliability ha un prezzo

Più reliability può richiedere:

- replica;
- monitoring;
- on-call;
- test;
- più frequenza;
- recovery capability;
- retention;
- parallel run.

Quindi il cost review deve leggere insieme:

- criticality tier;
- SLO;
- consumer value;
- cost-to-serve.

Un T1 sovra-ingegnerizzato può costare quanto un T3 senza creare valore equivalente.

## Freshness economics

Una delle domande più potenti è:

> **“Quanto vale davvero un dato più fresco?”**

Esempio:

### Dashboard executive

Decisione una volta al giorno.

Refresh ogni 10 minuti probabilmente non crea valore proporzionale.

### Fraud decision

Ogni secondo può cambiare l'esito.

Ridurre latency può avere valore elevato.

### Inventory planning

Una parte del dato può richiedere near-real-time, altre dimensioni possono essere daily.

Non dobbiamo assegnare la freshness dell'elemento più urgente a tutto il prodotto.

## Storage e history economics

Anche la retention deve dipendere dall'uso.

Conservare raw event per sempre può essere utile per:

- audit;
- backfill;
- ricerca;
- regolazione.

Ma può essere inutile per altre sorgenti.

L'Operating Contract può definire:

- hot window;
- cold/archive;
- replay requirement;
- legal retention;
- delete policy;
- cost owner.

Il valore della recoverability deve essere confrontato con il costo della history.

## Agent cost-to-serve

Con gli agenti AI emerge una nuova categoria di costo:

- token/model usage;
- tool calls;
- repeated query;
- retry loop;
- duplicate agents;
- evaluation;
- human review.

Un agente può sembrare economico per task e diventare costoso quando:

- viene chiamato troppo spesso;
- usa sempre il modello più potente;
- interroga dati non aggregati;
- produce output che nessuno consuma.

L'Operating Contract dell'agente deve quindi avere anche:

- usage budget;
- escalation per cost anomaly;
- model routing;
- cache/reuse strategy;
- consumer/adoption metric.

## Cost anomaly management

Come per data quality, una variazione di costo può essere:

- errore;
- nuovo consumer;
- crescita reale;
- query regressiva;
- mancato pruning;
- runaway agent;
- change di pricing provider.

Gli alert devono portare a un owner e a un playbook.

Esempio:

> cost-to-serve del prodotto +45% WoW con usage +3%.

Questo è un segnale molto più azionabile di:

> cloud bill +8%.

## Cost per unit of value

La metrica ideale sarebbe:

> **costo per decisione migliorata**.

Spesso non possiamo misurarla direttamente.

Possiamo però avvicinarci con una gerarchia:

### Cost

Quanto costa il prodotto?

### Output

Quante query/forecast/decision feed serve?

### Adoption

Quanti processi reali lo usano?

### Outcome

Quale tempo, rischio o valore economico cambia?

Questa gerarchia evita di chiamare efficienza il semplice taglio di spesa.

## Non ottimizzare il prodotto utile fino a renderlo inutile

Un forecast costa €2.000/mese e riduce stock-out attesi per centinaia di migliaia di euro.

Ridurre la frequenza per risparmiare €700 può essere una falsa economia.

Viceversa, un dashboard costa €15.000 e non entra più in alcuna decisione.

Qui l'optimization corretta può essere **retirement**, non tuning.

## Cost review nel lifecycle

Ogni prodotto T2/T3 può avere review periodica:

```text
monthly/quarterly cost
→ key drivers
→ allocated vs shared cost
→ SLO cost
→ cost per unit
→ adoption
→ value evidence
→ optimize / resize / redesign / retire
```

La FinOps Foundation sottolinea che unit metric e target devono essere rivisti nel tempo e collegati agli obiettivi organizzativi.

Fonte: https://www.finops.org/framework/capabilities/unit-economics/

## La regola economica

> **Un sistema analitico sostenibile non è quello che costa poco. È quello in cui il livello di servizio, il costo e il valore sono leggibili nello stesso Operating Contract, così possiamo capire se stiamo pagando per reliability utile o per complessità ereditata.**
