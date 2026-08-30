## 3.16 Checklist prima di fidarsi di un dataset

Prima di iniziare un'analisi, fermati abbastanza a lungo da rispondere a queste domande.

### Identità del dato

- Qual è l'unità di analisi?
- Una riga rappresenta cosa?
- Qual è la granularità?
- Esiste una chiave univoca?
- La chiave è veramente stabile nel tempo?

### Completezza

- Qual è il periodo coperto?
- Mancano giorni, clienti, prodotti, regioni o canali?
- Esistono buchi nella serie temporale?
- I null sono concentrati in specifici segmenti?

### Duplicati

- La chiave attesa è davvero unica?
- Esistono duplicati perfetti?
- Esistono duplicati logici con ID diversi?
- Un join potrebbe moltiplicare righe?

### Tempo

- Quale timestamp rappresenta l'evento?
- In quale timezone?
- Gli aggiornamenti tardivi sono possibili?
- I dati storici possono essere riscritti?

### Semantica

- Chi ha definito le colonne?
- Esiste un glossario?
- I valori hanno lo stesso significato in tutti i periodi?
- Sono cambiate le regole di business?

### Plausibilità

- Minimi e massimi sono plausibili?
- Le distribuzioni hanno senso?
- I volumi sono coerenti con il business?
- Le metriche aggregate si riconciliano con fonti affidabili?

### Provenance

- Da quale sistema arriva il dato?
- Quali trasformazioni ha subito?
- Chi è l'owner?
- Quando è stato aggiornato?

### Decisione

Infine, chiediti:

> Se questo dato fosse sbagliato del 5%, cambierebbe la decisione che sto per supportare?

Se la risposta è sì, la validazione deve essere proporzionalmente più rigorosa.

### Caso simulato: una dashboard perfetta costruita sul mese sbagliato

Un analyst prepara un report per confrontare il Black Friday con l'anno precedente. I grafici sono corretti, le query testate e gli importi riconciliati.

Durante la review qualcuno nota però che l'anno precedente il Black Friday cadeva il 24 novembre, mentre il confronto era stato fatto usando semplicemente gli stessi giorni del mese corrente.

Il dataset era corretto.

Il codice era corretto.

Il confronto era sbagliato.

La checklist non serve quindi solo a trovare dati corrotti. Serve anche a verificare che il dato sia **adatto alla domanda**.
