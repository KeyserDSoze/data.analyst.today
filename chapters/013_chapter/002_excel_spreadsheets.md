## 13.1 Excel e fogli di calcolo: il coltellino svizzero dell'analista
Excel è contemporaneamente uno degli strumenti più sottovalutati e più abusati dell'analytics.

È sottovalutato quando viene liquidato come «strumento da non tecnici». È abusato quando diventa database, sistema di versionamento, motore ETL, applicazione operativa e repository unico per processi critici.

La domanda utile non è «Excel sì o no?». È: **per quale parte del problema Excel è lo strumento giusto?**

## 13.1.1 Dove Excel è fortissimo

Excel è particolarmente efficace quando servono:

- esplorazione rapida;
- calcoli trasparenti;
- scenari what-if;
- analisi finanziarie;
- pivot table;
- confronto manuale con stakeholder;
- prototipazione di metriche;
- piccoli dataset;
- output che devono essere modificabili da utenti business.

La sua forza è l'immediatezza. Un manager può vedere la formula, cambiare un'ipotesi e osservare il risultato.

## 13.1.2 Caso realistico: pricing in 90 minuti

Una catena retail deve decidere se aumentare del 3% il prezzo di 240 SKU prima di una riunione con il procurement.

I dati sono già estratti:

- prezzo attuale;
- costo unitario;
- volumi degli ultimi 12 mesi;
- margine;
- elasticità stimata per categoria;
- prezzo medio dei competitor.

Il problema richiede scenari, non una pipeline produttiva.

Un foglio con tre scenari di elasticità, una tabella dati e controlli di margine può essere costruito e verificato molto più rapidamente di una soluzione più sofisticata.

L'errore sarebbe trasformare un problema decisionale urgente in un progetto ingegneristico.

## 13.1.3 Dove Excel inizia a diventare pericoloso

I segnali di allarme sono:

- file da centinaia di MB;
- decine di copie via email;
- macro non documentate;
- formule diverse tra fogli simili;
- lookup su tabelle esterne non controllate;
- aggiornamenti manuali ricorrenti;
- dati sensibili scaricati localmente;
- KPI aziendali calcolati in file personali;
- dipendenza da una singola persona.

### Caso realistico: il margine che cambia quando cambia il proprietario del file

Finance e Sales usano due copie dello stesso workbook.

Il file Finance tratta i resi nel mese della restituzione. Il file Sales li attribuisce al mese originale dell'ordine. Entrambi calcolano «gross margin».

Il risultato del Q2 differisce di 1,7 milioni di euro.

Non è un errore di Excel. È un problema di definizione, governance e duplicazione della logica.

## 13.1.4 Power Query cambia il confine

Con Power Query, Excel può collegarsi a sorgenti, applicare trasformazioni ripetibili e aggiornare un processo senza ricostruirlo manualmente.

Questo sposta il foglio da semplice calcolatore verso un ambiente di preparazione dati leggero.

Ma non elimina la domanda di fondo: quando le trasformazioni diventano condivise, critiche e ricorrenti, la logica dovrebbe probabilmente spostarsi più vicino alla piattaforma dati centrale.

## 13.1.5 Python dentro Excel: i confini si stanno fondendo

Microsoft oggi permette di eseguire Python direttamente in Excel. Il codice viene scritto nelle celle, l'esecuzione avviene nel cloud Microsoft e il risultato viene restituito al workbook. Sono disponibili librerie come pandas, NumPy, Matplotlib e statsmodels.

Questo è un esempio importante dell'evoluzione degli strumenti: le categorie stanno convergendo. Il futuro non è necessariamente «Excel oppure Python», ma ambienti che combinano interfacce familiari con capacità analitiche più avanzate.

La disponibilità di Python in Excel non cambia però la regola: mettere Python in un workbook non rende automaticamente il processo riproducibile, governato o adatto alla produzione.

## 13.1.6 Quando scegliere Excel

Excel è una buona scelta quando:

- la scala è moderata;
- il problema richiede forte interazione umana;
- il risultato deve essere spiegabile a stakeholder non tecnici;
- il ciclo è esplorativo o prototipale;
- l'automazione completa non ha ancora un ritorno economico chiaro.

## 13.1.7 Quando uscire da Excel

È tempo di migrare quando il file diventa:

- un processo aziendale critico;
- una fonte ufficiale di KPI;
- un collo di bottiglia operativo;
- un rischio di sicurezza;
- un sistema di integrazione tra molte sorgenti;
- un oggetto troppo complesso da testare e versionare.

> **Un foglio di calcolo è eccellente per pensare. Diventa rischioso quando gli chiediamo di comportarsi come un sistema informativo.**

### Fonti

- Microsoft Support, *Introduction to Python in Excel*: https://support.microsoft.com/en-us/excel/python/introduction-to-python-in-excel
- Microsoft Support, *Open-source libraries and Python in Excel*: https://support.microsoft.com/en-us/excel/python/open-source-libraries-and-python-in-excel
