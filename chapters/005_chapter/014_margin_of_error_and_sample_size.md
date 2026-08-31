## 5.13 Margine d'errore e dimensione del campione: quanto costa la precisione

Una domanda molto comune è:

> Quante osservazioni servono?

La risposta corretta non è un numero universale.

Dipende da quanta precisione vogliamo, da quanto è variabile il fenomeno e da quanto rischio siamo disposti ad accettare.

Per molte stime, il margine d'errore si riduce approssimativamente con la radice quadrata della dimensione del campione.

Questo significa che la precisione costa sempre di più.

Per dimezzare il margine d'errore servono, in prima approssimazione, quattro volte le osservazioni.

### Caso realistico: la survey da 200.000 euro

Una società telco vuole stimare la soddisfazione dei clienti consumer dopo una modifica al servizio di assistenza.

L'agenzia di ricerca propone tre opzioni:

| Risposte utili | Margine d'errore indicativo | Costo |
|---|---:|---:|
| 400 | circa ±5 punti percentuali | 28.000 € |
| 1.600 | circa ±2,5 punti | 71.000 € |
| 6.400 | circa ±1,25 punti | 198.000 € |

Il direttore marketing chiede immediatamente il campione più grande: “Voglio il dato più preciso possibile.”

Ma l'analista pone una domanda diversa:

> quale decisione cambierebbe tra una stima del 72% con ±2,5 punti e una con ±1,25 punti?

Se la decisione è semplicemente capire se la soddisfazione è rimasta sopra un target del 60%, spendere altri 127.000 € per raddoppiare la precisione potrebbe avere poco valore.

Se invece una differenza di un punto percentuale decide l'estensione nazionale di un programma da 40 milioni di euro, il campione più grande può essere giustificato.

La dimensione del campione è quindi anche una decisione economica.

### Più dati non correggono una cattiva misura

Supponiamo che la survey venga inviata solo tramite email.

I clienti più anziani, che usano poco l'email e chiamano più spesso il contact center, rispondono molto meno.

Passare da 400 a 40.000 risposte non risolve questo problema.

Rende molto precisa la stima di un campione potenzialmente sbilanciato.

Ancora una volta:

**la precisione non corregge il bias.**

### Il campione deve essere proporzionato alla decisione

Non sempre serve stimare con grande precisione un parametro medio complessivo.

Se il vero obiettivo è confrontare sei segmenti, la numerosità rilevante è quella *dentro ciascun segmento*.

Un dataset da 100.000 osservazioni può sembrare enorme. Ma se il segmento strategico “nuovi clienti enterprise in Francia” contiene soltanto 37 casi, l'analisi di quel segmento rimane fragile.

### Caso realistico: l'A/B test che sembrava enorme

Una piattaforma B2B esegue un test su 250.000 visite. Il numero impressiona il management.

Ma il KPI finale è la sottoscrizione di un contratto annuale.

Solo 612 visite arrivano alla firma.

La metrica realmente decisionale ha quindi un denominatore molto più piccolo di quello dichiarato nel titolo del test.

Questo è frequente nei funnel: il campione iniziale può essere enorme mentre il numero di eventi finali è limitato.

### La domanda giusta

Non chiedere soltanto:

> quante righe abbiamo?

Chiedi:

> quante osservazioni informative abbiamo per la stima e per il confronto che ci interessa?

È una differenza che può cambiare completamente l'affidabilità di un'analisi.

### Fonti

[^nist-ci-width]: NIST/SEMATECH e-Handbook of Statistical Methods, *Confidence Limits for the Mean*, https://www.itl.nist.gov/div898/handbook/eda/section3/eda352.htm
