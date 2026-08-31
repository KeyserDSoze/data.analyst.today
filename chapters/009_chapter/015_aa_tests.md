## 9.14 A/A test: testare il sistema prima di testare il prodotto

Un A/A test assegna gli utenti a due gruppi che ricevono **la stessa esperienza**.

A prima vista sembra inutile. In realtà è uno dei modi migliori per verificare se la piattaforma di experimentation è affidabile.

Se A e A sono identici, non dovremmo osservare differenze sistematiche nelle metriche. Se le vediamo, il problema può essere nel sistema di assegnazione, nella telemetria, nel filtering o nella pipeline di analisi.

### Caso pubblico documentato — Microsoft Teams

Microsoft ha descritto un problema reale durante il confronto tra build di Teams. Un A/A test apparentemente semplice mostrava differenze statisticamente significative tra gruppi che avrebbero dovuto essere equivalenti. L'indagine ha mostrato che effetti legati all'aggiornamento della build e differenze di penetrazione introducevano bias nel confronto.

Il team ha sviluppato un framework A/A'/B per separare meglio gli effetti del processo di update da quelli della build in test. In produzione, questo approccio ha permesso di rilevare regressioni reali e bloccare release prima di procedere.

Questo esempio è importante perché dimostra una cosa spesso trascurata:

> **un esperimento può essere statisticamente sofisticato e comunque sbagliato se l'infrastruttura di assegnazione o misurazione non è affidabile.**

### Cosa può rivelare un A/A test

Un buon A/A test può aiutare a individuare:

- Sample Ratio Mismatch;
- assegnazioni non stabili;
- metriche calcolate in modo diverso tra gruppi;
- problemi di logging;
- filtri che rimuovono utenti in modo asimmetrico;
- differenze di esposizione;
- errori nella randomizzazione;
- problemi nella gestione dei cookie o degli identifier;
- regressioni della piattaforma di experimentation.

### Ma un A/A test può produrre falsi positivi

Se analizziamo 100 metriche indipendenti con soglia 0,05, ci aspettiamo comunque alcune differenze significative per puro caso.

Per questo un A/A test non dovrebbe essere giudicato con la domanda:

> "Esiste almeno una metrica con p < 0,05?"

Meglio chiedere:

- quante metriche si muovono?
- la quota è compatibile con il false positive rate atteso?
- esistono pattern sistematici?
- le differenze persistono nel tempo?
- si concentrano su una famiglia di metriche?

### Quando usare A/A test

Sono particolarmente utili:

- quando si introduce una nuova piattaforma di experimentation;
- dopo modifiche importanti alla telemetria;
- quando cambiano identifier o sistemi di identity resolution;
- prima di grandi campagne sperimentali;
- dopo migrazioni infrastrutturali;
- quando i risultati di molti test diventano improvvisamente sospetti.

### Fonte pubblica

Microsoft Research, *A/A'/B Testing: Evaluating Microsoft Teams across Build Releases*:
https://www.microsoft.com/en-us/research/articles/a-a-b-testing-evaluating-microsoft-teams-across-build-releases/
