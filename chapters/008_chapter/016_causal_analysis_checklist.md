## 8.16 Checklist operativa per un'analisi causale

Prima di presentare una conclusione causale, l'analista dovrebbe riuscire a rispondere con chiarezza a queste domande.

### 1. Qual è il trattamento?

Definisci esattamente l'intervento:

- cosa riceve l'unità trattata;
- quando lo riceve;
- per quanto tempo;
- con quale intensità;
- se esistono versioni diverse del trattamento.

### 2. Qual è l'outcome?

Specificare:

- metrica;
- finestra temporale;
- unità di analisi;
- eventuali competing outcomes;
- guardrail metrics.

### 3. Qual è il controfattuale?

La domanda fondamentale è:

> cosa sarebbe successo alle stesse unità, nello stesso periodo, senza il trattamento?

Non possiamo osservare direttamente quel mondo. Dobbiamo costruire un confronto credibile.

### 4. Come viene assegnato il trattamento?

Documentare il processo reale:

- randomizzazione;
- regola di soglia;
- decisione umana;
- auto-selezione;
- disponibilità operativa;
- policy territoriale;
- timing.

Spesso la fonte del bias è qui.

### 5. Quali confondenti esistono?

Creare un elenco esplicito delle variabili che possono influenzare sia trattamento sia outcome.

Non limitarsi a ciò che è già nel dataset.

Chiedere ai domain expert quali variabili importanti potrebbero non essere registrate.

### 6. Quali variabili sono pre-treatment?

Separare:

- confondenti preesistenti;
- mediatori;
- conseguenze del trattamento;
- collider potenziali.

### 7. Quale disegno è disponibile?

Ordine di preferenza pragmatico, non assoluto:

- esperimento randomizzato quando fattibile;
- natural experiment credibile;
- RDD quando esiste una soglia valida;
- Difference-in-Differences quando esistono gruppi e trend comparabili;
- instrumental variables quando esiste uno strumento difendibile;
- matching/weighting quando selection on observables è plausibile;
- modelli osservazionali con assunzioni esplicite quando non esiste di meglio.

### 8. Le assunzioni sono plausibili?

Ogni metodo ha assunzioni diverse.

Non basta applicare una funzione statistica. Bisogna verificare e discutere:

- parallel trends;
- common support;
- continuity al cutoff;
- exclusion restriction;
- assenza di manipolazione;
- assenza di interference rilevante;
- stabilità delle definizioni.

### 9. Esistono placebo o falsification test?

Esempi:

- verificare effetti prima dell'intervento;
- usare outcome che teoricamente non dovrebbero cambiare;
- spostare artificialmente il cutoff;
- testare segmenti non esposti;
- verificare covariate balance.

### 10. L'effetto è economicamente importante?

Tradurre sempre:

- punti percentuali;
- clienti salvati;
- revenue incrementale;
- costo dell'intervento;
- ROI;
- rischio operativo;
- intervallo di incertezza.

### 11. L'effetto è generalizzabile?

Chiedere:

- vale solo vicino a una soglia?
- riguarda solo i trattati?
- riguarda solo un mercato?
- cambia per segmenti?
- il periodo analizzato è anomalo?

### 12. Cosa non sappiamo ancora?

Una buona conclusione causale contiene anche le sue limitazioni.

Formato consigliato:

> **Evidenza disponibile → assunzioni → effetto stimato → incertezza → decisione → prossimo test.**

### La frase da evitare

> "Abbiamo controllato per tutte le variabili, quindi l'effetto è causale."

Quasi mai possiamo dimostrare di aver controllato per tutte le cause rilevanti.

### La frase migliore

> "Sotto queste assunzioni, supportate da questi controlli e da questo disegno, la stima è compatibile con un effetto causale di questa dimensione."

Può sembrare meno spettacolare. È molto più utile per una decisione seria.
