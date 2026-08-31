## 9.6 Stopping rules, peeking e sequential testing

Uno dei modi più comuni per falsare inconsapevolmente un A/B test è guardare continuamente il p-value e fermarsi appena diventa favorevole.

È umano: il team aspetta il risultato, apre la dashboard dieci volte al giorno e appena compare `p < 0.05` vuole dichiarare la vittoria.

Il problema è che, se ripetiamo abbastanza controlli nel tempo usando una procedura pensata per una sola analisi finale, aumentiamo la probabilità di fermarci su una fluttuazione casuale.

### Caso: il bottone verde che vince alle 11:40

Un sito travel testa un nuovo pulsante di prenotazione.

La variante B viene osservata ogni due ore.

| Ora dal lancio | Lift conversione | p-value |
|---|---:|---:|
| 12 | +1,1% | 0,31 |
| 24 | +1,7% | 0,12 |
| 36 | +2,2% | 0,048 |
| 48 | +1,4% | 0,11 |
| 72 | +0,8% | 0,29 |

Se il team avesse fermato il test a 36 ore, avrebbe dichiarato una vittoria. Continuando, l'effetto rientra nel rumore.

### Perché il peeking è pericoloso

Ogni nuova lettura è una nuova opportunità di trovare casualmente un risultato estremo.

La soluzione non è vietare di guardare i dati operativi. È distinguere tra:

- monitoraggio di sicurezza;
- controllo qualità;
- decisione statistica finale.

Possiamo guardare crash rate, latency, SRM o bug ogni ora. Non dobbiamo però usare una procedura frequentista fissa come se non avessimo mai guardato prima.

### Fixed horizon

Il metodo più semplice è stabilire in anticipo:

- sample size;
- durata minima;
- data di analisi;
- metriche;
- soglie di decisione.

Poi si evita di prendere la decisione finale prima del punto stabilito, salvo motivi di sicurezza o danno evidente.

### Sequential testing

Esistono approcci statistici progettati per analisi sequenziali, nei quali possiamo effettuare controlli intermedi mantenendo sotto controllo il tasso di errore.

Il punto concettuale importante per un Data Analyst non è memorizzare ogni variante matematica, ma capire che:

> se vogliamo prendere decisioni sequenziali, dobbiamo usare una procedura sequenziale.

Non possiamo semplicemente applicare la stessa soglia `0.05` infinite volte.

### Stop per danno

Un test può e deve essere interrotto prima quando emergono problemi seri:

- crash;
- perdita di pagamenti;
- aumento frodi;
- violazioni di sicurezza;
- danno economico oltre una soglia prestabilita.

Questo è diverso dal fermare il test perché la primary metric ha appena superato la soglia desiderata.

### La regola scritta prima del test

Nel pre-analysis plan possiamo definire:

- durata minima: 14 giorni;
- sample size minimo: 900.000 utenti per variante;
- un'analisi finale;
- eventuali checkpoint intermedi usando procedura sequenziale;
- stopping rule di sicurezza: error rate checkout > +20% rispetto al controllo.

### Errore tipico

Il problema del peeking non si risolve nascondendo la dashboard. Si risolve costruendo governance e regole decisionali coerenti.

> La domanda non è “quando il risultato sembra abbastanza bello?”. È “quale procedura avevamo deciso di usare per stabilire quando l'evidenza è sufficiente?”.