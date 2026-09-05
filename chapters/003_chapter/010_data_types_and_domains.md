## 3.9 Tipi, domini e unità: una colonna non è soltanto un contenitore

Una variabile possiede almeno quattro livelli di significato: **tipo tecnico**, **dominio ammesso**, **unità di misura** e **significato di business**. Un dataset può essere perfettamente valido per il motore che lo legge e diventare pericoloso quando uno di questi livelli rimane implicito.

Il tipo tecnico stabilisce come il valore viene memorizzato. Il dominio stabilisce quali valori hanno senso. L'unità rende interpretabile la quantità. Il significato di business collega infine il campo al fenomeno che vogliamo rappresentare. Nessuno di questi livelli sostituisce gli altri.

### Caso simulato/composito — Il CAP che perse gli zeri

Mercurio Express importa ogni notte un CSV con gli indirizzi dei clienti. `postal_code` viene interpretato automaticamente come intero, così `00144` diventa `144`.

La pipeline non fallisce e il valore rimane un numero perfettamente valido. Il problema è che un CAP non è una quantità: è un codice. Non ha senso sommarlo, calcolarne una media o perdere zeri iniziali.

La correzione tecnica è semplice, ma il principio è generale:

> **La rappresentazione tecnica deve seguire il significato del dato, non il contrario.**

Un identificatore composto soltanto da cifre può dover essere una stringa; un importo richiede una valuta; una durata richiede un'unità; `0.12` non può essere interpretato senza sapere se rappresenta una frazione, dodici punti percentuali o un valore già scalato.

### Caso reale documentato — Mars Climate Orbiter

Il Mars Climate Orbiter fu perso il 23 settembre 1999. NASA identifica la causa radice nella mancata applicazione delle unità metriche in un file software di terra usato nei modelli di traiettoria: dati di impulso erano prodotti in unità inglesi mentre l'interfaccia richiedeva unità metriche.[^nasa-mco][^nasa-mco-report]

Il caso è diventato un esempio estremo di un principio quotidiano nell'analytics. Il valore numerico può esistere, il file può essere prodotto e il software può leggerlo senza eccezioni, mentre il significato attribuito al numero è sbagliato.

La stessa ambiguità, in scala molto meno drammatica, compare in campi come:

```text
weight = 80
revenue = 1200
duration = 90
temperature = 70
rate = 0.15
```

Senza unità e convenzione non sappiamo se `weight` è in chilogrammi o libbre, `revenue` in euro o centesimi, `duration` in secondi o minuti, `temperature` in Celsius o Fahrenheit, `rate` come frazione o punti percentuali.

## Il dominio rende verificabile la semantica

Le regole di dominio trasformano conoscenza tacita in condizioni controllabili. `discount_pct` può dover stare tra 0 e 100, `currency` appartenere all'insieme supportato, `order_status` all'enum del workflow, `birth_date` non essere futura e `quantity` rispettare la semantica con cui vendite e resi vengono registrati.

Queste regole sono potenti perché possono essere automatizzate, ma non dimostrano che il valore sia accurato. `country_code = IT` è valido se `IT` appartiene al dominio; può comunque descrivere il Paese sbagliato. Una data può avere formato corretto e riferirsi all'evento sbagliato.

Validità e accuratezza devono quindi restare separate. La prima controlla la compatibilità con la rappresentazione attesa; la seconda richiede un confronto con la realtà o con una fonte indipendente.

Per i campi critici conviene conservare una piccola scheda operativa:

```text
Campo:
Significato:
Tipo tecnico:
Unità:
Dominio:
Null ammesso:
Momento di validità:
Sistema sorgente:
Casi speciali:
```

Non è documentazione fine a se stessa. È il contratto minimo che permette a una query, a un modello o a un agente di sapere che cosa sta manipolando.

> **Un numero senza unità, dominio e significato non è ancora una misura. È soltanto un valore memorizzato.**

---

### Fonti

[^nasa-mco]: NASA Lessons Learned, *Mars Climate Orbiter Mishap Investigation Board — Phase I Report, Lesson 641*. https://llis.nasa.gov/lesson/641
[^nasa-mco-report]: NASA, *Mars Climate Orbiter Mishap Investigation Board — Phase I Report*. https://discovery.larc.nasa.gov/pdf_files/MCO_report_2.pdf
