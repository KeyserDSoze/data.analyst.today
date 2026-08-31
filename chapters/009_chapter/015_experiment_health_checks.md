## 9.15 Experiment health checks: prima di interpretare l'effetto, verifica che l'esperimento sia sano

Uno degli errori più costosi nell'A/B testing è analizzare subito la metrica primaria senza verificare la salute dell'esperimento.

Un risultato può sembrare convincente ma essere invalido perché il sistema non ha randomizzato correttamente, alcuni utenti non sono stati tracciati, la treatment exposure non è coerente o una pipeline si è rotta.

### Caso simulato — RideFlow

RideFlow, piattaforma di mobilità urbana, testa un nuovo algoritmo di ranking per suggerire punti di pickup più efficienti.

Il dashboard mostra:

- tempo medio di attesa: -6,4%
- cancellazioni: -2,1%
- p-value sulla metrica primaria: 0,012

Il risultato sembra ottimo.

Prima di approvare il rollout, l'analista esegue gli health checks.

Scopre che:

- allocazione attesa: 50/50;
- allocazione osservata: 53,8/46,2;
- una versione Android non riceve correttamente la treatment;
- gli utenti Android hanno tempi di attesa storicamente peggiori;
- il gruppo treatment contiene quindi meno utenti Android del previsto.

Il miglioramento apparente non può essere interpretato causalmente.

### Health check essenziali

#### 1. Sample Ratio Mismatch

Il numero di utenti nelle varianti è compatibile con l'allocazione prevista?

#### 2. Assignment stability

Lo stesso utente rimane nella stessa variante per tutta la durata del test?

#### 3. Exposure

Gli utenti assegnati alla treatment hanno effettivamente visto o ricevuto il trattamento?

#### 4. Logging completeness

Gli eventi necessari sono registrati allo stesso modo nei gruppi?

#### 5. Pre-experiment balance

Le variabili pre-trattamento sono ragionevolmente bilanciate?

#### 6. Triggering

La popolazione analizzata corrisponde realmente agli utenti che potevano essere influenzati dal cambiamento?

#### 7. Metric integrity

Numeratori, denominatori, timestamp e join sono coerenti?

#### 8. Concurrent experiments

Esistono altri test che possono interagire con quello in corso?

### Il principio dei tre livelli

Un buon processo di experimentation separa tre domande:

1. **Il sistema funziona?**
2. **L'esperimento è valido?**
3. **Il trattamento produce un effetto utile?**

Saltare i primi due livelli e discutere direttamente il terzo significa costruire una decisione sopra fondamenta non verificate.

### Caso pubblico documentato — Microsoft ExP

Microsoft ha documentato esperimenti su modifiche infrastrutturali nei quali metriche apparentemente semplici non erano sufficienti. Il team ha sottolineato la necessità di validare telemetria e definizioni metriche anche in piattaforme mature e di accompagnare metriche tecniche locali con guardrail di prodotto più ampie.

Il punto è particolarmente utile per un Data Analyst: la qualità dell'esperimento non dipende soltanto dalla statistica, ma dall'intera catena dati.

### Fonte pubblica

Microsoft Research, *A/B Testing Infrastructure Changes at Microsoft ExP*:
https://www.microsoft.com/en-us/research/articles/a-b-testing-infrastructure-changes-at-microsoft-exp/
