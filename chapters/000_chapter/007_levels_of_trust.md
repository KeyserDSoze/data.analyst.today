## 0.6 Livelli di fiducia: non tutti gli output AI meritano lo stesso trattamento

Uno degli errori più comuni nell'uso dell'AI è applicare lo stesso livello di fiducia e di review a qualsiasi output.

Una bozza di email interna e una raccomandazione che modifica un prezzo non hanno lo stesso profilo di rischio.

Una query esplorativa e una query che alimenta il reporting finanziario non richiedono lo stesso livello di verifica.

Un brainstorming di ipotesi e una conclusione causale non sono equivalenti.

La domanda corretta non è quindi:

> “Quanto mi fido dell'AI?”

È:

> **“Quanta fiducia devo richiedere a questo output, dato l'uso che ne farò?”**

### La fiducia dipende dall'uso, non soltanto dal modello

Possiamo ragionare almeno su quattro dimensioni:

- **impatto** — quanto costa sbagliare?
- **reversibilità** — quanto è semplice annullare l'azione?
- **incertezza** — quanto è fragile l'evidenza?
- **osservabilità** — quanto rapidamente ci accorgeremmo dell'errore?

A queste si possono aggiungere contesto normativo, sensibilità dei dati e portata dell'azione.

Il punto è che lo stesso sistema può essere perfettamente accettabile in un contesto e inadeguato in un altro.

### Un modello operativo a quattro livelli

#### Livello 1 — Draft

L'AI produce una bozza che una persona può correggere facilmente.

Esempi:

- riassunto;
- prima versione di una query;
- elenco di ipotesi;
- documentazione iniziale.

Il costo dell'errore è basso e la reversibilità alta. La review può essere leggera.

#### Livello 2 — Assisted execution

L'AI esegue attività operative entro confini chiari.

Esempi:

- generazione SQL su metriche certificate;
- data profiling;
- test di qualità;
- produzione di grafici;
- classificazione preliminare di anomalie.

Qui servono controlli automatici, tracciabilità e campionamento.

#### Livello 3 — Decision support

L'output influenza decisioni importanti, anche se una persona mantiene l'ultima parola.

Esempi:

- forecast per budgeting;
- ranking clienti per retention;
- analisi pricing;
- identificazione dei driver di churn;
- prioritizzazione di interventi operativi.

Qui diventano centrali review umana, validazione, spiegazioni alternative, analisi dell'incertezza e accountability chiara.

#### Livello 4 — Consequential action

Il sistema può agire direttamente su persone, denaro o sistemi critici.

Esempi:

- modificare prezzi;
- allocare budget;
- bloccare transazioni;
- cancellare account;
- cambiare configurazioni di produzione.

Qui servono limiti di autorità, logging, approval, rollback, stop condition e controlli indipendenti molto più forti.

Questi livelli non sono una certificazione formale. Sono un modo semplice per impedire che una demo convincente venga trattata come un sistema pronto per qualsiasi conseguenza.

### Caso simulato/composito: stesso score, tre rischi diversi

Un modello stima la probabilità che un cliente abbandoni.

**Uso A.** Lo score ordina una lista che un account manager esamina manualmente.

Un falso positivo costa principalmente tempo. Il modello è un supporto alla prioritizzazione.

**Uso B.** Lo stesso score concede automaticamente uno sconto del 30%.

Ora un errore produce un costo economico diretto e può insegnare ai clienti comportamenti indesiderati.

**Uso C.** Lo score viene usato per negare automaticamente un servizio.

Il profilo di rischio cambia ancora: entrano in gioco impatto sulle persone, policy, possibili discriminazioni e requisiti di governance molto più forti.

La tecnologia è la stessa. Cambia la decisione collegata all'output.

> **Non esiste un livello di fiducia “del modello” separato dal contesto in cui quel modello viene usato.**

### L'autonomia si guadagna gradualmente

Un sistema AI non dovrebbe passare direttamente da prototipo a piena autonomia soltanto perché una demo funziona.

Una progressione più prudente può essere:

1. **offline evaluation** — test su casi storici e scenari noti;
2. **shadow mode** — il sistema produce output senza agire;
3. **confronto con decisioni umane** — misuriamo accordi, disaccordi e failure mode;
4. **autonomia su casi semplici** — perimetro limitato e reversibile;
5. **escalation sui casi ambigui** — il sistema sa quando non procedere;
6. **espansione graduale** — l'autorità cresce soltanto dopo evidenza operativa sufficiente.

Questa progressione crea una storia di affidabilità osservata, invece di sostituirla con una promessa.

Microsoft propone esplicitamente una governance degli agenti proporzionata al rischio e all'impatto delle azioni che possono compiere.

Fonte:
- https://learn.microsoft.com/en-us/agents/center-of-excellence/govern-agents-risk

### Fiducia non significa certezza

Anche un sistema molto ben validato può sbagliare.

Il punto non è promettere rischio zero. È sapere:

- quale rischio stiamo accettando;
- perché è accettabile;
- quali segnali ci avviseranno di un problema;
- chi interviene;
- come recuperiamo o limitiamo il danno.

> **La fiducia professionale non è credere che il sistema non sbaglierà. È sapere come ci accorgeremo che sta sbagliando e cosa faremo dopo.**
