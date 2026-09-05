## 1.4 I dati non sono la realtà

Uno degli errori più pericolosi nell'analisi è confondere il dato con il fenomeno che il dato cerca di rappresentare.

Un database non contiene il mondo reale. Contiene una rappresentazione costruita da applicazioni, processi, definizioni, regole operative e decisioni prese spesso molto prima che l'analista formulasse la propria domanda.

Quando leggiamo una colonna chiamata `customer`, `revenue`, `active_user` o `conversion`, il nome può dare l'impressione che il significato sia già risolto. In realtà siamo arrivati alla fine di una catena di scelte. Qualcuno ha deciso quando una persona diventa cliente, quale evento conta come vendita, in quale momento registrare l'importo, quale stato rende un utente attivo e che cosa succede a ordini annullati, rimborsi o eventi che il tracking non riesce a osservare.

I nomi familiari rendono naturali decisioni che naturali non sono.

### Un evento reale, molte rappresentazioni valide

Immaginiamo un e-commerce. Un cliente effettua un ordine alle 23:58 del 31 gennaio. Il pagamento viene autorizzato alle 00:01 del 1° febbraio. Il magazzino prepara il pacco il 2 febbraio, la spedizione parte il 3, il cliente restituisce metà dell'ordine il 10 e riceve il rimborso il 15.

A quale mese appartiene quella vendita?

La domanda non ha una risposta universale perché “la vendita” non è un singolo evento tecnico. Se stiamo studiando la domanda commerciale può interessarci la data dell'ordine. Se analizziamo il cash flow contano pagamento e rimborso. Per la logistica conta l'evasione; per la contabilità può valere una regola diversa ancora.

Lo stesso fatto economico genera quindi più timestamp, stati e importi, tutti potenzialmente corretti rispetto a domande diverse. **La scelta analitica non consiste nel trovare la data vera in assoluto, ma nel collegare la rappresentazione adatta al fenomeno che vogliamo comprendere.**

### Misurare significa costruire un modello del fenomeno

Una metrica comprime una parte della realtà in una forma utilizzabile. Nel farlo sceglie che cosa includere, quale unità osservare, quale finestra temporale adottare, come aggregare gli eventi, come trattare eccezioni e missing value e quale popolazione considerare eleggibile.

Queste decisioni possono essere scritte in una specifica oppure rimanere implicite nella query. Ma esistono comunque.

Per questo due dashboard possono partire dallo stesso ecosistema dati e mostrare numeri diversi senza che una delle due contenga necessariamente un bug. Potrebbero usare due rappresentazioni diverse dello stesso processo. La sezione 1.9 entrerà nel dettaglio delle metriche; qui ci basta fissare un principio più generale:

> **prima del calcolo esiste sempre un modello della realtà, esplicito o implicito.**

Il problema nasce quando quel modello rimane invisibile e il numero viene trattato come se fosse il fenomeno stesso.

### Spesso osserviamo proxy, non ciò che ci interessa davvero

Molti concetti importanti non sono direttamente registrabili. Vogliamo conoscere la soddisfazione del cliente, ma osserviamo survey, recensioni, reclami, utilizzo e retention. Vogliamo capire la produttività, ma misuriamo ticket chiusi, output, ore lavorate o tempi di ciclo. Vogliamo parlare di qualità e disponiamo di difetti, resi, errori o reclami.

Queste variabili sono **proxy**: segnali osservabili che rappresentano fenomeni più complessi.

Un proxy può essere molto utile proprio perché rende misurabile ciò che altrimenti rimarrebbe astratto. Diventa pericoloso quando dimentichiamo il pezzo di realtà che non cattura. Un aumento dei ticket chiusi può indicare maggiore produttività, ma può anche riflettere ticket più semplici, una diversa classificazione o un incentivo a chiudere troppo presto. Se il proxy diventa un KPI, può persino cambiare il comportamento che pretendeva soltanto di osservare.

La domanda corretta non è quindi soltanto *quanto è correlato al fenomeno?*, ma anche *in quali condizioni smette di rappresentarlo bene?*

### Anche l'assenza di dato è prodotta da un processo

Ciò che non compare in tabella può essere importante quanto ciò che compare.

Un sistema di supporto registra i problemi segnalati, non tutti i problemi vissuti dai clienti. Una survey osserva chi ha risposto, non automaticamente l'intera popolazione. Un funnel digitale contiene gli eventi che il tracking è riuscito a catturare; un sensore rotto può far sparire un comportamento invece di modificarlo.

Per questo una domanda accompagnerà tutto il libro:

> **Quale meccanismo ha determinato che questa osservazione entrasse — o non entrasse — nel dataset?**

È una domanda di qualità del dato, ma anche di selezione. Se la probabilità di essere osservati dipende dal fenomeno che stiamo studiando, l'assenza non è rumore neutrale: può deformare l'interpretazione.

### Perché l'AI rende il problema ancora più evidente

Un sistema generativo può costruire una query sintatticamente perfetta usando la colonna sbagliata, una relazione non adatta o una definizione incoerente con la domanda. La documentazione Microsoft per Copilot in Power BI insiste proprio sulla dipendenza degli output dal modello semantico e dal contesto con cui viene preparato.[^ms-semantic][^ms-prepare]

La tecnologia cambia la velocità con cui possiamo interrogare la rappresentazione. Non cambia il fatto che dobbiamo sapere che cosa quella rappresentazione significa.

> **Prima di chiedere che cosa dicono i dati, dobbiamo capire che cosa rappresentano, come sono stati prodotti e che cosa non riescono a vedere.**

---

### Fonti

[^ms-semantic]: Microsoft Learn, *Use Copilot with semantic models in Power BI*. https://learn.microsoft.com/en-us/power-bi/create-reports/copilot-semantic-models
[^ms-prepare]: Microsoft Learn, *Prepare your data for AI*. https://learn.microsoft.com/en-us/power-bi/create-reports/copilot-prepare-data-ai
