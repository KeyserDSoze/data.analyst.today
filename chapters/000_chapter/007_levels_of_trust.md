## 0.6 Livelli di fiducia: non tutti gli output AI meritano lo stesso trattamento
Uno degli errori più comuni nell'uso dell'AI è trattare tutti gli output come se avessero lo stesso grado di affidabilità.

Non è così.

Una bozza di email interna e una raccomandazione che modifica un prezzo non hanno lo stesso profilo di rischio.

Una query esplorativa e una query che alimenta il reporting finanziario non richiedono lo stesso livello di verifica.

Un brainstorming di ipotesi e una decisione causale non sono equivalenti.

## Fiducia come funzione del contesto

Possiamo pensare la fiducia richiesta come funzione di almeno quattro dimensioni:

- **impatto** dell'errore;
- **reversibilità** dell'azione;
- **incertezza** dell'output;
- **osservabilità** degli effetti.

Più cresce l'impatto e diminuisce la reversibilità, più dobbiamo alzare il livello di controllo.

## Un modello operativo a quattro livelli

### Livello 1 — Draft

L'AI produce una bozza o un supporto creativo.

Esempi:

- riassunto;
- prima versione di una query;
- elenco di ipotesi;
- documentazione iniziale.

Qui la review può essere leggera.

### Livello 2 — Assisted execution

L'AI esegue attività operative ma entro confini chiari.

Esempi:

- generazione di SQL su metriche certificate;
- data profiling;
- test di qualità;
- produzione di grafici.

Servono controlli automatici e campionamento.

### Livello 3 — Decision support

L'AI influenza decisioni importanti ma non agisce direttamente.

Esempi:

- forecast per budgeting;
- ranking clienti per retention;
- analisi pricing;
- identificazione dei driver di churn.

Qui servono review umana, alternative explanation, validazione e accountability chiara.

### Livello 4 — Consequential action

L'AI può agire direttamente su sistemi, persone o denaro.

Esempi:

- modificare prezzi;
- bloccare transazioni;
- allocare budget;
- cancellare account;
- modificare configurazioni di produzione.

Qui l'autonomia deve essere molto più controllata, con approval, logging, rollback e stop conditions.

## Caso realistico: stesso modello, uso diverso

Un modello stima la probabilità che un cliente abbandoni.

Se viene usato per ordinare una lista che un account manager esamina manualmente, il rischio è relativamente limitato.

Se lo stesso score viene usato per concedere automaticamente uno sconto del 30%, il rischio economico aumenta.

Se viene usato per negare automaticamente un servizio, il profilo cambia ancora.

Lo stesso output tecnico può richiedere livelli di governance completamente diversi in base all'uso.

## La fiducia deve essere guadagnata

Un sistema AI non dovrebbe passare direttamente da demo a piena autonomia.

Possiamo costruire una progressione:

1. shadow mode;
2. confronto con decisioni umane;
3. autonomia su casi semplici;
4. escalation sui casi ambigui;
5. espansione graduale del perimetro.

Questa logica permette di osservare failure mode prima di concedere autorità maggiore.

Microsoft propone esplicitamente di governare gli agenti per livelli di rischio, con controlli più intensi per agenti che possono incidere su persone, denaro o processi critici.

Fonte:
- https://learn.microsoft.com/en-us/agents/center-of-excellence/govern-agents-risk

## Fiducia non significa certezza

Anche un sistema molto ben validato può sbagliare.

Il punto non è eliminare ogni rischio.

È sapere:

- quale rischio stiamo accettando;
- perché;
- con quali controlli;
- con quale piano di recovery.

> **La fiducia professionale non è credere che il sistema non sbaglierà. È sapere come ci accorgeremo che sta sbagliando e cosa faremo dopo.**