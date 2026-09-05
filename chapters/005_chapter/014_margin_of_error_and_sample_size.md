## 5.13 Margine di errore e sample size: comprare precisione soltanto quando serve

Quando un analyst riceve la domanda “quante osservazioni ci servono?”, la tentazione è rispondere con una formula. Ma la formula arriva troppo presto se non sappiamo **quanto precisamente dobbiamo distinguere le alternative che contano per la decisione**.

La numerosità necessaria dipende dal parametro che stiamo stimando, dalla variabilità del fenomeno, dal disegno di raccolta e dalla precisione desiderata. Per molte stime semplici, la variabilità campionaria si riduce approssimativamente come `1 / √n`. Questo significa che la precisione ha **rendimenti decrescenti**: per dimezzare lo standard error o il margin of sampling error servono, in prima approssimazione, circa quattro volte le osservazioni.

Questa relazione trasforma la sample size da esercizio tecnico in decisione economica.

## La survey da quasi 200.000 euro

Una telco vuole stimare la soddisfazione nella customer base consumer. Per rendere confrontabili i numeri assumiamo un campionamento casuale semplice, livello di confidenza 95% e proporzione vicina al 50%, cioè il caso prudenziale per il margine di campionamento.

| Risposte utili | Margine di campionamento indicativo | Costo |
|---|---:|---:|
| 400 | circa ±4,9 punti percentuali | 28.000 € |
| 1.600 | circa ±2,5 punti | 71.000 € |
| 6.400 | circa ±1,2 punti | 198.000 € |

Il direttore marketing chiede il campione più grande perché vuole “il dato più preciso possibile”. La domanda migliore dell'analista è un'altra:

> **Quale decisione cambierebbe grazie alla precisione aggiuntiva?**

Se il problema è capire se la soddisfazione sia chiaramente sopra un target del 60%, spendere 127.000 € in più per passare da circa ±2,5 a ±1,2 punti può aggiungere pochissimo valore decisionale. Se invece un punto percentuale decide un programma da decine di milioni, la stessa precisione aggiuntiva può essere economicamente razionale.

La sample size diventa quindi una forma di **Value of Information**: compriamo osservazioni finché il valore atteso della riduzione di incertezza giustifica costo e tempo necessari.

## Il margine di campionamento non è l'errore totale

La frase “margine di errore ±3%” viene spesso letta come se il risultato non potesse essere sbagliato di più di tre punti. Non è ciò che il numero promette.

AAPOR chiarisce che il margin of sampling error riguarda l'incertezza dovuta al campionamento e non include automaticamente nonresponse bias, coverage error, measurement error o altri problemi del processo di raccolta.[^aapor-accuracy][^aapor-definitions]

Una survey può quindi avere un margine di campionamento piccolissimo e un errore totale molto più grande. Se la telco raccoglie feedback soltanto via email e i clienti meno digitali rispondono molto meno, passare da 400 a 40.000 risposte restringe l'incertezza all'interno del gruppo osservato senza necessariamente correggere la sua sottorappresentazione.

È la stessa distinzione che attraversa tutto il capitolo:

> **precisione e rappresentatività sono problemi diversi.**

## La numerosità deve essere quella del parametro che conta

Un dataset con 100.000 righe può contenere pochissima informazione per la domanda effettiva. Se vogliamo stimare il comportamento dei “nuovi clienti enterprise in Francia acquisiti negli ultimi 90 giorni” e quel segmento contiene 37 aziende, la dimensione totale del warehouse non ci aiuta.

Lo stesso accade nei funnel. Possiamo osservare 250.000 visite, 18.000 trial, 2.100 opportunità qualificate e 612 contratti firmati. Se la decisione riguarda la probabilità di chiudere un contratto annuale, il volume in cima al funnel non può essere usato per fingere una precisione che l'outcome finale non possiede.

La domanda “quante osservazioni abbiamo?” deve quindi diventare:

> **Quante unità informative abbiamo per il parametro, il segmento e l'effetto su cui vogliamo decidere?**

## Stimare con precisione e rilevare un effetto sono problemi diversi

La sample size può essere progettata per almeno due scopi. Possiamo voler stimare un parametro con una certa ampiezza di intervallo, oppure voler distinguere un effetto minimo in un confronto. Nel secondo caso entrano anche la variabilità, il livello di falso positivo accettato e la potenza statistica.

Questo è il motivo per cui il **Minimum Effect of Interest** deve precedere la power analysis. Se il business non cambierebbe mai decisione per un uplift sotto +0,5 punti percentuali, progettare un test gigantesco per rilevare +0,03 punti con alta precisione può essere un uso inefficiente di traffico e tempo.

Il template seguente merita di restare strutturato perché funziona come specifica decisionale prima di raccogliere dati:

```text
Parametro / effetto da stimare:
Popolazione:
Precisione necessaria o effetto minimo rilevante:
Decisione che cambia a quella soglia:
Principali bias non risolti aumentando n:
Costo marginale dell'informazione aggiuntiva:
```

Il criterio di stop non è “abbiamo eliminato l'incertezza”. È **abbiamo abbastanza informazione per distinguere le alternative decisionali che contano**.

> **La sample size non è una proprietà del dataset. È una proprietà del problema inferenziale e del valore economico della precisione.**

---

### Fonti

[^aapor-accuracy]: AAPOR, *Polling Accuracy*. https://aapor.org/polling-accuracy/
[^aapor-definitions]: AAPOR, *Standard Definitions*, 10th edition. https://aapor.org/standards-and-ethics/standard-definitions/
