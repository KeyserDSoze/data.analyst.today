## 5.13 Margine di errore e sample size: comprare precisione dove serve davvero

Una delle domande più frequenti rivolte a un analyst è:

> **Quante osservazioni ci servono?**

Non esiste un numero universale.

La numerosità necessaria dipende da ciò che vogliamo stimare, dalla variabilità del fenomeno, dal livello di precisione desiderato, dal disegno di campionamento e — soprattutto — dalla decisione che quella precisione deve supportare.

Per molte stime semplici, l'incertezza campionaria si riduce approssimativamente come `1 / √n`.

Questo ha una conseguenza economica importante:

> **la precisione ha rendimenti decrescenti.**

Per dimezzare lo standard error o il margine di campionamento servono, in prima approssimazione, circa quattro volte le osservazioni.

### Caso simulato/composito — La survey da quasi 200.000 euro

Una telco vuole stimare una proporzione di soddisfazione nella customer base consumer. Supponiamo, per rendere confrontabili i numeri, un campionamento casuale semplice, un livello di confidenza del 95% e il caso prudenziale in cui la proporzione è vicina al 50%.

L'agenzia propone:

| Risposte utili | Margine di campionamento indicativo | Costo |
|---|---:|---:|
| 400 | circa ±4,9 punti percentuali | 28.000 € |
| 1.600 | circa ±2,5 punti | 71.000 € |
| 6.400 | circa ±1,2 punti | 198.000 € |

Il direttore marketing chiede il campione più grande:

> “Voglio il dato più preciso possibile.”

L'analista riformula:

> **“Quale decisione cambierebbe grazie alla precisione aggiuntiva?”**

Se dobbiamo soltanto capire se la soddisfazione è chiaramente sopra un target del 60%, passare da ±2,5 a ±1,2 punti può valere molto meno dei 127.000 € aggiuntivi.

Se invece una differenza di un punto decide l'estensione di un programma da decine di milioni di euro, quella precisione può avere un valore informativo molto maggiore.

La sample size è quindi anche una **decisione sul valore dell'informazione**.

### Il margine di errore non è “l'errore totale”

Nelle survey, espressioni come “margine di errore ±3%” vengono facilmente interpretate come:

> “il dato può essere sbagliato al massimo di tre punti”.

Non è così.

AAPOR sottolinea che il margin of sampling error riguarda l'incertezza dovuta al campionamento secondo il disegno adottato; non incorpora automaticamente errori di copertura, nonresponse, formulazione delle domande, modalità di raccolta o altri bias.[^aapor-accuracy]

Una survey può quindi avere:

- margine di campionamento piccolo;
- errore totale molto più grande perché il campione o la misura sono distorti.

Questo è lo stesso principio visto nel caso Literary Digest.

### Più risposte non correggono chi non può rispondere

Supponiamo che la telco raccolga feedback solo via email.

I clienti che usano poco i canali digitali rispondono meno e, contemporaneamente, possono avere un'esperienza diversa col contact center.

Passare da 400 a 40.000 risposte può restringere drasticamente l'incertezza **all'interno del meccanismo osservato** senza correggere quella sottorappresentazione.

> **Precisione e rappresentatività sono problemi distinti.**

### La sample size deve essere pianificata sul parametro decisionale

Un dataset può contenere 100.000 righe e avere comunque pochissima informazione per la domanda realmente importante.

Se vogliamo stimare il comportamento di:

> “nuovi clienti enterprise in Francia acquisiti negli ultimi 90 giorni”

e quel segmento contiene 37 aziende, `n = 100.000` non descrive la precisione della stima che ci interessa.

Lo stesso avviene nei funnel. Possiamo avere:

- 250.000 visite;
- 18.000 trial;
- 2.100 opportunità qualificate;
- 612 contratti firmati.

Se l'outcome decisionale è il contratto annuale, il volume in cima al funnel può creare un'impressione ingannevole di abbondanza informativa.

### Sample size per stima e sample size per confronto

Ci sono almeno due domande diverse:

1. **Quanto precisamente voglio stimare un parametro?**
2. **Quanto piccolo è l'effetto che voglio riuscire a distinguere in un confronto?**

Per la prima ragioniamo soprattutto in termini di precisione e ampiezza dell'intervallo.

Per la seconda entrano anche:

- effetto minimo rilevante;
- variabilità;
- livello di falso positivo accettato;
- power.

La sezione 5.16 collegherà questi elementi. Il Capitolo 9 mostrerà come usarli nella pianificazione di un esperimento.

### Fermarsi quando la precisione è sufficiente

Più precisione è quasi sempre possibile, ma non è gratuita.

Un criterio maturo è:

> **raccogliere abbastanza informazione da distinguere le alternative decisionali che contano, non abbastanza da eliminare ogni incertezza possibile.**

In termini pratici, prima di chiedere “quante osservazioni?” scrivi:

```text
Parametro / effetto da stimare:
Popolazione:
Precisione necessaria o effetto minimo rilevante:
Decisione che cambia a quella soglia:
Principali bias non risolti aumentando n:
Costo marginale dell'informazione aggiuntiva:
```

La sample size non è una proprietà del dataset. È una proprietà del **problema inferenziale**.

[^aapor-accuracy]: AAPOR, *Polling Accuracy*: https://aapor.org/polling-accuracy/
