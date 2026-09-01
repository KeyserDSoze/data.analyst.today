## 13.12 Total Cost of Ownership: quanto costa davvero possedere una scelta

Il prezzo di uno strumento è una delle parti più visibili del costo e spesso una delle meno importanti.

Per un workflow analitico il **Total Cost of Ownership** comprende almeno:

```text
build
+ run
+ maintenance
+ coordination
+ skills
+ reliability
+ governance
+ migration
+ error cost
+ delay cost
```

Non serve trasformare ogni scelta in un business case finanziario completo.

Serve evitare confronti del tipo:

> questo tool costa €200 al mese, quindi è più economico.

La domanda corretta è:

> **quanto ci costa ottenere e continuare a ottenere una decisione affidabile attraverso questa soluzione?**

### 1. Build cost

Comprende:

- discovery;
- implementazione;
- integrazione;
- test;
- documentazione;
- migrazione iniziale;
- formazione.

L'AI può ridurre molto questa voce.

Non necessariamente riduce le successive.

### 2. Run cost

È il costo per eseguire e distribuire il processo:

- licenza;
- compute;
- storage;
- scansione;
- API;
- egress;
- scheduling;
- ambienti.

È spesso la voce più facile da misurare.

### 3. Maintenance cost

Include:

- failure investigation;
- schema change;
- aggiornamenti delle dipendenze;
- modifiche alla business logic;
- richieste degli utenti;
- manual exception handling.

È qui che molte soluzioni apparentemente economiche cambiano profilo.

### Caso simulato/composito — la licenza da €180 al mese

Un team Marketing usa un workflow no-code per integrare sei piattaforme advertising.

Costi diretti:

```text
licenza: €180/mese
= €2.160/anno
```

Dopo un anno il team misura anche:

```text
manutenzione: 40 ore/mese complessive
costo interno: €60/ora

40 × 12 × €60 = €28.800/anno
```

Inoltre stima:

```text
incidenti con report ritardato:
8 episodi/anno × €750 di effort/opportunity cost
= €6.000

formazione/handover:
60 ore/anno × €60
= €3.600
```

Il TCO osservabile diventa quindi almeno:

```text
€2.160 + €28.800 + €6.000 + €3.600
= €40.560/anno
```

Non stiamo affermando che una soluzione custom costerebbe meno.

Stiamo dicendo che confrontarla con **€2.160** sarebbe un confronto falso.

### 4. Coordination cost

Una soluzione può richiedere molto coordinamento anche con poco compute.

Esempi:

- tre team devono approvare ogni modifica;
- una persona deve inviare file ogni lunedì;
- Finance e Analytics devono riconciliare manualmente due output;
- cinque dashboard devono essere aggiornati separatamente.

Questa frizione ha un costo reale, anche se non compare nella fattura del vendor.

### 5. Skill cost e bus factor

Uno stack può richiedere competenze rare o molto specifiche.

Domande:

- quante persone possono mantenerlo?
- quanto costa formarle?
- quanto tempo richiede l'onboarding?
- esiste supporto interno?
- quanto siamo dipendenti da una singola persona?

Una tecnologia ottima con `bus factor = 1` può avere un ownership cost elevato.

### 6. Reliability cost

Quanto costa quando il processo:

- fallisce;
- produce dati incompleti;
- arriva tardi;
- deve essere rifatto;
- genera una decisione errata?

Questo costo dipende dal contesto.

Un report interno mensile e un sistema antifrode non devono avere lo stesso investimento in reliability.

### 7. Migration e switching cost

Ogni scelta accumula dipendenze:

- query;
- macro;
- file;
- dashboard;
- skill;
- training;
- processi downstream.

Cambiare più tardi può costare molto.

Questo non significa scegliere sempre il tool più “future proof”.

Significa documentare **quanto siamo disposti a investire prima di sapere se il problema merita permanenza**.

L'exit condition del Tooling Decision Record serve proprio a evitare che lo switching cost cresca in modo invisibile.

### 8. Error cost

Una soluzione più rapida ma meno verificabile può costare poco da eseguire e molto quando sbaglia.

Esempio:

```text
risparmio operativo: €15.000/anno

un errore plausibile sul pricing:
€120.000 di margine a rischio
```

A quel punto spendere qualcosa in più per review, test o governance può avere senso.

Il TCO deve quindi includere anche **expected risk**, non solo costi certi.

### 9. Delay cost: il costo di aspettare la soluzione perfetta

Esiste infine il problema opposto.

Supponiamo che un checkout bug faccia perdere circa €30.000 al giorno.

Possiamo:

**A.** produrre in quattro ore un'analisi sufficientemente affidabile per isolare il problema;

**B.** aspettare due settimane per costruire il data product definitivo prima di iniziare la diagnosi.

Anche se B fosse più elegante, il costo dell'attesa potrebbe dominare il confronto.

Per questo **time-to-first-reliable-evidence** è una vera dimensione economica del tooling.

### Caso reale documentato — cost optimization come business value

Il Google Cloud Well-Architected Framework definisce il cost optimization pillar in termini di massimizzazione del **business value** dell'investimento, non come semplice minimizzazione della spesa.[^gcp-waf]

La documentazione e i materiali FinOps di Google insistono inoltre sul collegamento tra consumo tecnologico, accountability e valore prodotto.[^gcp-finops]

Il principio è trasferibile al nostro contesto:

> **ottimizzare un tool analitico significa migliorare il rapporto tra costo totale e valore decisionale, non ridurre ogni voce di spesa.**

### TCO worksheet dentro il Tooling Decision Record

Non serve precisione falsa. Basta una stima ordinata.

| Voce | Opzione A | Opzione B | Evidenza/confidenza |
|---|---:|---:|---|
| Build | | | |
| Run annuale | | | |
| Maintenance | | | |
| Coordination | | | |
| Training/skills | | | |
| Reliability / incident | | | |
| Migration/switching | | | |
| Expected error cost | | | |
| Delay / time-to-value | | | |

Dopo la tabella aggiungiamo:

```text
largest uncertainty:
most expensive failure mode:
cheapest reversible option:
what must be true for the extra cost to be justified:
```

Quest'ultima domanda evita un errore frequente:

> scegliere l'opzione costosa perché “scala meglio” senza sapere quale crescita dovrebbe realmente materializzarsi.

### Confine con il Capitolo 12

Nel Capitolo 12 abbiamo discusso il TCO dell'**architettura**.

Qui valutiamo il costo di ownership della **scelta di tooling per un workflow o prodotto analitico**.

Le due prospettive si toccano, ma non sono identiche.

### Regola operativa

> **Non confrontare strumenti per il loro prezzo. Confrontali per il costo totale di costruire, verificare, operare, cambiare e — quando serve — abbandonare la soluzione che produce la decisione.**

[^gcp-waf]: Google Cloud Documentation, *About the Well-Architected Framework*, https://docs.cloud.google.com/docs/get-started/well-architected-framework
[^gcp-finops]: Google Cloud, *What is Cloud FinOps?*, https://cloud.google.com/learn/what-is-finops
