## 4.12 Caso studio — La correlazione che quasi spostò 600.000 euro di budget

> **Caso simulato/composito.** Azienda, numeri e circostanze sono costruiti a fini didattici.

**Northstar Home**, e-commerce di arredamento, chiude il trimestre con un risultato apparentemente molto interessante.

Il team marketing mostra una correlazione di **0,76** tra:

- spesa social settimanale;
- average order value settimanale.

Inoltre i clienti attribuiti al social hanno un AOV aggregato superiore a quelli provenienti dalla search.

La proposta è spostare **600.000 euro di budget annuale** da search a social.

L'analisi sembra quantitativa. La domanda è se il pattern sia abbastanza robusto da sostenere la storia che gli stiamo attribuendo.

### 1. Guardare i punti

Lo scatter plot conferma una relazione positiva, ma mostra quattro settimane molto distanti dal resto:

- Black Friday;
- pre-Natale;
- due lanci della nuova linea premium.

Con tutte le settimane:

```text
r = 0,76
```

In una sensitivity analysis che mostra separatamente le quattro settimane eccezionali:

```text
r sulle altre settimane = 0,31
```

Le quattro osservazioni non sono errori e non vanno cancellate dal business.

Ma la frase "esiste una forte relazione generale" è molto più fragile di quanto suggerisse `0,76`.

### 2. Inserire il tempo

La spesa social e l'AOV sono entrambi elevati nelle settimane in cui:

- cresce la domanda stagionale;
- il catalogo spinge prodotti premium;
- aumentano bundle e gift set;
- sale il traffico complessivo.

Lo stesso calendario può quindi contribuire a entrambe le variabili.

La correlazione iniziale non separa questi meccanismi.

### 3. Guardare la composizione

L'analista confronta AOV per canale e fascia prodotto:

| Canale | AOV aggregato | Prodotti standard | Prodotti premium |
|---|---:|---:|---:|
| Social | €184 | €121 | €296 |
| Search | €169 | €128 | €301 |
| Direct | €176 | €126 | €299 |

Nell'aggregato Social sembra migliore.

Dentro le stesse fasce prodotto non emerge invece un vantaggio sistematico di AOV.

La differenza totale dipende molto dal fatto che il social porta una quota maggiore di traffico alle creatività premium.

Questo non rende il canale social meno interessante.

Cambia la domanda.

### 4. Aggiungere metriche che rappresentano la decisione

Il business non guadagna perché aumenta l'AOV in astratto.

La riallocazione dovrebbe migliorare valore economico dopo aver considerato almeno:

- conversion rate;
- CAC;
- contribution margin;
- return rate;
- volume incrementale ottenibile;
- capacità di scalare la spesa.

L'EDA mostra quindi che `AOV` è un pezzo della decisione, non il suo obiettivo completo.

### 5. Separare fatti e ipotesi

**Fatti osservati**

- social spend e AOV settimanale hanno `r = 0,76` nel trimestre;
- quattro settimane eccezionali influenzano fortemente la relazione;
- social ha un mix di traffico più orientato ai prodotti premium;
- dentro le fasce prodotto l'AOV non mostra un vantaggio uniforme.

**Ipotesi candidate**

- il social è particolarmente efficace nel portare utenti verso linee premium;
- le creatività premium spiegano parte dell'AOV maggiore;
- la stagionalità spiega parte del movimento congiunto di spend e AOV.

**Non dimostrato**

- che aumentare la spesa social causi un AOV maggiore;
- che spostare €600.000 aumenti il margine incrementale.

### 6. La domanda migliore

La domanda iniziale era:

> Più social spend aumenta l'AOV?

Dopo l'EDA diventa:

> **A parità di offerta e mix creativo, aumentare l'investimento social produce abbastanza conversioni e contribution margin incrementali da superare le alternative di allocazione del budget?**

Adesso sappiamo quale tipo di evidenza serve.

### 7. La decisione

L'azienda non sposta immediatamente l'intero budget.

Progetta invece un test limitato nel tempo e nel perimetro, mantenendo più stabile il mix creativo e definendo in anticipo:

- metrica primaria economica;
- CAC;
- conversion;
- AOV;
- contribution margin;
- guardrail su resi e saturazione.

La sperimentazione verrà trattata nel Capitolo 9.

Qui la lezione è diversa:

> **l'EDA non ha dimostrato quale canale fosse causalmente migliore. Ha impedito che un coefficiente aggregato diventasse una decisione da 600.000 euro senza averne stressato la struttura.**

Questo è un buon criterio per valutare l'analisi esplorativa: non quante correlazioni ha trovato, ma quante conclusioni premature ha reso più difficili da sostenere.