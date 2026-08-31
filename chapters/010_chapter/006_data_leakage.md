## 10.6 Data leakage: quando il modello conosce il futuro senza dirtelo

Il data leakage è uno dei modi più pericolosi per ottenere un modello apparentemente eccezionale.

Accade quando durante il training entra informazione che, nel momento reale della previsione, non sarebbe disponibile.

La documentazione ufficiale di scikit-learn lo definisce come l'uso di informazione non disponibile al prediction time, con performance troppo ottimistiche in validazione e risultati peggiori su dati realmente nuovi.

Fonte: https://scikit-learn.org/stable/common_pitfalls.html

### Quattro forme comuni di leakage

**1. Leakage temporale**

Usare eventi successivi al momento della previsione.

Esempio: prevedere churn a inizio mese usando il numero di email di cancellazione ricevute durante quel mese.

**2. Leakage dal target**

Una feature è una trasformazione o conseguenza quasi diretta del target.

Esempio: prevedere default usando un campo `account_sent_to_collections` registrato solo dopo il mancato pagamento.

**3. Leakage da preprocessing**

Calcolare normalizzazione, imputazione o feature selection usando anche il test set.

**4. Leakage tra entità correlate**

La stessa entità o entità quasi duplicate compaiono sia nel train sia nel test.

### Caso pubblico documentato: scikit-learn e le feature casuali

La documentazione di scikit-learn mostra un esempio volutamente estremo e molto istruttivo.

Viene costruito un dataset con target casuale e **10.000 feature generate casualmente**. Non dovrebbe esistere alcun segnale predittivo reale.

Se la feature selection viene eseguita sull'intero dataset **prima** dello split, il modello arriva comunque a un'accuracy intorno a **0,76**.

È un risultato impressionante e completamente falso.

Quando invece:

1. si divide prima train e test;
2. si impara la feature selection solo sul train;
3. si applica poi la trasformazione al test;

la performance torna vicino al livello casuale, come dovrebbe.

Questo è un esempio perfetto di una regola fondamentale:

> anche trasformazioni che sembrano innocue possono trasferire informazione dal test al training.

Fonte pubblica documentata: https://scikit-learn.org/stable/common_pitfalls.html#data-leakage

### Caso realistico: HealthFlow e il rischio di mancato appuntamento

HealthFlow vuole prevedere quali pazienti non si presenteranno all'appuntamento, così da inviare reminder più intensivi.

Un modello iniziale raggiunge AUC 0,94.

Tra le feature compare:

`days_since_last_contact`

Sembra innocua.

L'analista scopre però che il campo viene ricalcolato ogni notte usando il CRM corrente. Per gli appuntamenti storici, quindi, contiene anche contatti avvenuti **dopo** la data dell'appuntamento.

Ricostruendo la feature con uno snapshot storico corretto, AUC scende a 0,72.

Il secondo modello è molto meno spettacolare, ma è quello realmente utilizzabile.

### La domanda temporale da fare per ogni feature

Per ogni colonna, chiediti:

> questa informazione sarebbe stata disponibile, esattamente in questa forma, nel momento in cui avrei dovuto produrre la previsione?

Non:

> questa colonna esiste nel database oggi?

Sono domande molto diverse.

### Pipeline e preprocessing

Scikit-learn raccomanda di separare train/test prima del preprocessing e di imparare trasformazioni come scaler, imputazione e selezione delle feature solo sul training set. Le pipeline aiutano a rendere questo comportamento sistematico.

Il principio non dipende da Python.

Vale in SQL, notebook, BI, feature store e pipeline cloud.

### Errore tipico con l'AI

Chiedere a un LLM:

> “Costruiscimi un modello di churn con queste colonne.”

L'LLM può generare codice sintatticamente perfetto senza sapere quali colonne esistessero davvero al prediction time.

L'AI può aiutare a implementare il modello. La responsabilità della **linea temporale informativa** rimane dell'analista.

### Checklist anti-leakage

Prima di fidarti di un risultato molto alto, controlla:

- quando nasce ogni feature;
- quando viene aggiornata;
- se dipende dal target;
- se preprocessing e feature selection sono fit solo sul train;
- se esistono duplicati o entità presenti in entrambi i set;
- se lo split rispetta tempo e unità di generalizzazione;
- se il risultato è plausibile rispetto al problema.

Quando un modello diventa improvvisamente “troppo bravo”, il leakage dovrebbe essere una delle prime ipotesi da verificare.
