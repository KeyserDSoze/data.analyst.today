## 10.5 Train, validation e test: simulare il deployment, non dividere righe a caso

Un modello predittivo viene giudicato su ciò che non ha ancora visto.

Il problema della validation non è quindi scegliere una percentuale come `80/20`. È costruire una simulazione credibile del futuro in cui il modello verrà usato.

Possiamo distinguere tre ruoli:

- **training set**: stima parametri e pattern;
- **validation set / cross-validation**: supporta scelte di feature, modello, iperparametri e talvolta soglie;
- **test set**: resta il più possibile isolato fino alla valutazione finale.

Questa separazione protegge una cosa preziosa: una misura di generalizzazione non continuamente ottimizzata durante lo sviluppo.

### La domanda prima dello split

Prima di dividere i dati chiediamo:

> **a che cosa deve generalizzare il modello?**

Possibili risposte:

- nuovi eventi degli stessi clienti;
- clienti mai visti;
- nuovi negozi;
- nuove città;
- periodi futuri;
- device o mercati non presenti nel training;
- una combinazione di questi casi.

La risposta determina il design della validation.

### Caso simulato/composito — FinSure e lo split che mescola due mondi

FinSure eroga finanziamenti a PMI. Costruisce un modello di default con dati 2021–2025.

Uno split casuale produce ottime metriche.

Nel 2026 la performance scende nettamente.

Nel 2025 erano cambiati:

- criteri di acquisizione;
- pricing;
- underwriting;
- mix settoriale;
- canali commerciali.

Lo split casuale aveva distribuito righe appartenenti allo stesso regime sia nel train sia nel test. Il test rispondeva quindi a:

> "quanto funzioniamo su altri esempi mescolati dello stesso archivio?"

La domanda di produzione era invece:

> "quanto funzioniamo sul prossimo periodo operativo?"

Un test temporale più onesto può essere:

- train: 2021–2024;
- validation: gennaio–giugno 2025;
- test: luglio–dicembre 2025.

La metrica può peggiorare. La qualità della valutazione migliora.

Google raccomanda esplicitamente di testare modelli destinati al futuro su dati raccolti **dopo** quelli usati per il training, perché questo riflette meglio il comportamento in produzione.

Fonte: https://developers.google.com/machine-learning/guides/rules-of-ml/

### Group split: quando la riga non è indipendente

Immaginiamo un modello di churn con uno snapshot mensile per cliente.

Se gennaio–maggio dello stesso account finiscono nel training e giugno nel test, il modello può sfruttare segnali quasi identici dello stesso soggetto.

Questo può essere corretto se in produzione vogliamo prevedere mesi futuri di clienti già conosciuti.

Può essere sbagliato se la domanda è:

> "quanto generalizziamo su un nuovo cliente?"

In quel caso lo split dovrebbe preservare i gruppi.

Lo stesso problema compare con:

- pazienti con più visite;
- device con più eventi;
- negozi con più giorni;
- aziende con più dipendenti;
- prodotti con più transazioni.

### Caso simulato/composito — MoveNow e due domande entrambe valide

MoveNow costruisce un ETA model su 12 milioni di consegne.

Ottiene:

- split casuale tra consegne in città note: MAE 5,8 minuti;
- holdout su città non viste: MAE 11,4 minuti.

Non esiste un unico numero "vero" di performance.

I due test rispondono a domande diverse:

1. **new event, known context** — nuove consegne in città già presenti;
2. **new context** — generalizzazione all'apertura di una città nuova.

Se il business vuole entrambi gli use case, la Predictive Decision Card deve riportare entrambi gli scope.

### Validation set contaminato dal processo di sviluppo

Anche un validation set può diventare, di fatto, parte del training mentale del team.

Se proviamo 300 combinazioni di feature e scegliamo quella che performa meglio sullo stesso validation set, stiamo adattando decisioni di sviluppo anche a quel campione.

Per questo nei progetti con molte iterazioni può essere utile mantenere un test finale realmente untouched.

Il test set non è sacro per motivi rituali. Serve a ridurre il rischio che il processo di ricerca ottimizzi inconsapevolmente anche la valutazione.

### Il test deve rispettare la frontiera informativa

Uno split corretto non basta se le feature sono costruite usando informazioni future.

Train/test design e leakage sono due controlli complementari:

- lo split decide **quali osservazioni** il modello può usare;
- la frontiera informativa decide **quali informazioni dentro ogni osservazione** erano disponibili al prediction time.

La sezione successiva affronta proprio questo secondo problema.

### Regola operativa

La strategia di validation deve essere scritta in una frase business, non solo in codice.

Esempio:

> **"Valutiamo il modello su account non usati nel training e su un periodo successivo, perché in produzione lo applicheremo ogni mese anche a nuovi clienti in un mercato che cambia nel tempo."**

> **Il miglior split non è quello che usa meglio il dataset. È quello che simula meglio il fallimento che ci aspetta dopo il deployment.**
