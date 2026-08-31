# 20.1 Diventare manager di N agenti

Il salto più importante non è passare da Excel a Python, da SQL a un LLM o da un notebook a un agente.

Il salto è passare da **esecutore di task** a **orchestratore di capacità**.

Un analista AI-native potrebbe avere agenti diversi per:

- data discovery;
- SQL generation;
- data quality;
- metric verification;
- forecasting;
- causal reasoning;
- visualization;
- documentation;
- code review;
- executive communication.

Questi agenti possono lavorare in parallelo. Ma parallelizzare il lavoro non significa parallelizzare automaticamente il giudizio.

## Caso realistico: dieci agenti, una sola decisione

Un marketplace vede il Gross Merchandise Value scendere del 9% in Spagna.

Il responsabile analytics lancia una squadra di agenti.

### Agent 1 — Data health

Segnala che il feed ordini è completo al 99,8%.

### Agent 2 — Funnel

Trova un calo nella conversione checkout.

### Agent 3 — Payments

Individua un aumento dei payment failures.

### Agent 4 — Releases

Trova una release mobile avvenuta due giorni prima.

### Agent 5 — Segmentation

Mostra che il calo è concentrato su iOS.

### Agent 6 — Geography

Mostra che Madrid e Barcellona spiegano il 71% del delta.

### Agent 7 — Causal reasoning

Propone la release iOS come principale ipotesi causale.

### Agent 8 — SQL reviewer

Conferma che le query sono coerenti con la definizione certificata di GMV.

### Agent 9 — Counter-hypothesis

Nota che un provider di pagamento ha avuto un incidente nello stesso intervallo.

### Agent 10 — Executive writer

Produce una raccomandazione:

> “Rollback immediato della release iOS.”

A prima vista il sistema sembra straordinario.

Il problema è che due spiegazioni competono:

- release iOS;
- outage del provider di pagamento.

Se l'executive agent ha il compito di “produrre una raccomandazione”, potrebbe trasformare un conflitto non risolto in una conclusione troppo netta.

Qui serve il manager.

L'analista deve chiedere:

- quali utenti hanno davvero ricevuto la release?
- quale provider usavano?
- il problema esiste anche su iOS con provider alternativi?
- il timing coincide con deploy o incidente?
- quali segmenti costituiscono un controllo naturale?

Gli agenti hanno moltiplicato la capacità investigativa. L'analista deve trasformarla in una gerarchia di evidenze.

## Non tutti gli agenti hanno la stessa autorità

Un sistema maturo distingue tra agenti:

### Esplorativi

Possono generare ipotesi e cercare pattern.

Il loro output non è una decisione.

### Operativi

Possono generare query, report o trasformazioni entro confini definiti.

Richiedono controlli automatici.

### Critici

Possono autorizzare o proporre azioni che incidono su clienti, denaro, compliance o sistemi di produzione.

Qui la soglia di supervisione deve essere molto più alta.

## Una possibile gerarchia

Un workflow potrebbe essere progettato così:

1. **worker agents** producono analisi;
2. **review agents** cercano errori e controesempi;
3. **control layer** esegue test deterministici;
4. **human owner** valuta conflitti, incertezza e decisione.

L'errore è costruire una catena in cui ogni agente prende per vero l'output del precedente.

Se il primo agente interpreta male una metrica, dieci agenti successivi possono produrre una montagna di lavoro coerente con un'assunzione sbagliata.

## Manager non significa micromanager

Essere al timone non significa leggere ogni token prodotto.

Un manager di agenti deve progettare:

- **scope**: cosa può fare ciascun agente;
- **input**: a quali dati può accedere;
- **definition of done**: quando un task è concluso;
- **checks**: quali verifiche sono obbligatorie;
- **escalation**: quando deve fermarsi e chiedere aiuto;
- **budget**: quante iterazioni e quanto costo può consumare;
- **authority**: quali azioni può eseguire senza approvazione.

È una logica molto simile alla gestione di un team.

## Il collo di bottiglia cambia

Quando N agenti possono lavorare contemporaneamente, il collo di bottiglia non è più la produzione.

Diventa:

- priorità;
- coordinamento;
- risoluzione dei conflitti;
- qualità degli obiettivi;
- capacità di verifica;
- decisione.

Questo è uno dei motivi per cui analytical thinking, business understanding e semantica acquistano valore proprio mentre la capacità tecnica diventa più accessibile.

**Il futuro dell'analista non è competere con dieci agenti. È saper dirigere dieci agenti verso una risposta che meriti fiducia.**
