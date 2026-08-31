## 13.9 Reproducibility e version control: se non puoi rifarlo, non puoi davvero fidarti

Un'analisi utile non dovrebbe esistere solo nella testa dell'analista o in un file chiamato `final_v7_vera_finale.xlsx`.

La riproducibilità significa poter ricostruire il risultato partendo dagli stessi input, applicando le stesse trasformazioni e ottenendo lo stesso output o, almeno, comprendendo esattamente perché l'output è cambiato.

Questo non è un ideale accademico. È un requisito operativo.

### Caso realistico: il margine che cambia tra venerdì e lunedì

Un team finance prepara il venerdì una tabella con margine lordo per categoria. Il lunedì il CFO chiede di aggiornare i numeri con le vendite del weekend.

L'analista apre il file precedente ma non ricorda:

- quali righe erano state escluse manualmente;
- se i resi erano stati sottratti prima o dopo l'aggregazione;
- quale versione del tasso di cambio era stata usata;
- se la tabella prodotti proveniva dal file ERP o dal catalogo commerciale;
- quali celle contenevano formule e quali valori incollati.

Il problema non è che Excel sia sbagliato. Il problema è che il processo non è più ricostruibile.

### Reproducibility non significa necessariamente codice

Un processo può essere riproducibile anche con strumenti visuali o spreadsheet, se:

1. le fonti sono note;
2. le trasformazioni sono documentate;
3. le modifiche sono tracciabili;
4. l'ordine dei passaggi è stabile;
5. gli output possono essere rigenerati senza interpretazione arbitraria.

Il codice rende spesso più semplice soddisfare questi requisiti, ma non li garantisce automaticamente.

Uno script Python non versionato, pieno di path locali e passaggi manuali, può essere meno riproducibile di un modello Power Query ben strutturato.

### Cosa versionare

Quando un'analisi diventa importante o ricorrente, dovrebbero essere versionati almeno:

- query SQL;
- script Python/R;
- definizioni metriche;
- file di configurazione;
- documentazione delle assunzioni;
- logica di trasformazione;
- test;
- eventualmente notebook e dashboard source files, quando il formato lo consente.

I dati grezzi non devono necessariamente essere inseriti in Git. Spesso è meglio versionare il **modo con cui vengono ottenuti e trasformati**, non copie enormi del dato stesso.

### Caso realistico: due analisti, due churn rate

Due analisti lavorano sullo stesso problema SaaS.

Il primo usa:

```sql
WHERE subscription_status = 'cancelled'
```

Il secondo considera churn anche gli account scaduti da oltre 30 giorni.

Entrambi producono query corrette. Ottengono churn rate del 4,8% e del 6,1%.

Senza version control e definizione condivisa, il team discute per ore sul risultato.

Con una metrica versionata, la discussione cambia:

> "Quale definizione di churn vogliamo governare?"

È una discussione molto più utile.

### Git come memoria del ragionamento

Version control non serve solo per recuperare una query cancellata. Permette di rispondere a domande come:

- quando è cambiata questa definizione?
- chi l'ha modificata?
- perché?
- quale dashboard usa ancora la versione precedente?
- quale commit ha introdotto la regressione?

Un buon commit non dovrebbe dire solo `fix query`.

Meglio:

```text
Exclude refunded orders from net revenue metric
```

oppure:

```text
Use customer_id instead of email for retention cohort identity
```

Il commit diventa parte della documentazione analitica.

### Notebook: potenti ma non automaticamente riproducibili

I notebook sono ottimi per esplorazione e storytelling tecnico, ma introducono rischi specifici:

- celle eseguite fuori ordine;
- variabili rimaste in memoria;
- output non aggiornati;
- dipendenze non dichiarate;
- dataset locali non più disponibili.

Una pratica utile è verificare periodicamente che il notebook funzioni con un'esecuzione completa dall'inizio alla fine in un ambiente pulito.

### Regola operativa

> **Se un'analisi è importante abbastanza da influenzare una decisione ricorrente, deve essere importante abbastanza da poter essere ricostruita.**
