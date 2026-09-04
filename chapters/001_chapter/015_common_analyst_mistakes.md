## 1.14 Gli errori tipici dell'analista

Molti errori analitici non nascono da una formula sbagliata. Nascono prima, quando il problema viene rappresentato male, oppure dopo, quando l'evidenza viene trasformata in una conclusione più forte di quanto meriti.

Per questo è più utile raggruppare gli errori non per strumento, ma per il punto della catena analitica in cui si rompe il significato.

### Errore 1 — Partire da ciò che possiamo fare invece che da ciò che dobbiamo capire

Aprire Power BI, Excel, SQL o un notebook prima di chiarire la domanda crea un bias molto semplice: iniziamo a vedere il problema attraverso le funzioni dello strumento che abbiamo davanti.

Lo stesso accade con i dati. Se una colonna esiste, diventa facile usarla come rappresentazione del fenomeno anche quando è soltanto un proxy debole. Al contrario, possiamo ignorare variabili importanti perché non sono immediatamente disponibili.

I due errori hanno la stessa radice: **confondere disponibilità con rilevanza**.

La correzione è partire dal concetto e dalla decisione. Prima chiediamo che cosa dobbiamo capire e quale evidenza cambierebbe la scelta; soltanto dopo cerchiamo dati e strumenti adeguati. Se il fenomeno non è osservabile direttamente, dichiariamo il proxy e i suoi limiti invece di lasciare che il nome di una colonna risolva implicitamente la definizione.

### Errore 2 — Trattare definizioni e popolazioni come se fossero naturali

“Cliente attivo”, “revenue”, “retention” e “conversione” sembrano concetti stabili finché due team non li calcolano in modo diverso.

Il problema diventa ancora più insidioso nelle metriche di rapporto. Una percentuale può cambiare perché è cambiato il comportamento del numeratore, ma anche perché è cambiata la popolazione nel denominatore. Confrontare periodi o segmenti senza controllare l'eleggibilità può quindi creare un movimento che non corrisponde a nessun cambiamento individuale.

La stessa fragilità compare quando ignoriamo lineage e trasformazioni. Una tabella “pronta” può aver applicato filtri, deduplicazioni, join, mapping e regole di business che hanno già definito la popolazione prima che iniziassimo l'analisi.

La correzione è rendere espliciti almeno popolazione, numeratore, denominatore, data di riferimento, grain e trasformazioni critiche. Per una metrica importante dobbiamo essere in grado di ricostruire non soltanto la formula, ma il contratto semantico che la rende interpretabile.

### Errore 3 — Costruire una storia prima di avere localizzato il fenomeno

Davanti a un calo o a un aumento sorprendente, il cervello cerca subito una causa. È il momento in cui confondenti, selezione e causalità inversa diventano più pericolosi, perché una spiegazione plausibile può iniziare a guidare quali dati guardiamo dopo.

Prima della storia viene la decomposizione.

Una media stabile può nascondere segmenti che si muovono in direzioni opposte. Un valore aggregato può cambiare soltanto perché è cambiato il mix della popolazione. Un problema attribuito all'intero prodotto può essere concentrato in un dispositivo, una coorte o una fase del funnel.

Il caso della sezione precedente mostrava proprio questo passaggio: “vendite in calo” è diventato “conversione dei nuovi visitatori mobile in calo” prima di diventare una discussione sulle possibili cause.

La correzione è separare tre momenti: **osservazione, localizzazione, spiegazione**. Solo dopo chiediamo quale meccanismo potrebbe produrre il pattern e quale evidenza distinguerebbe le ipotesi concorrenti.

### Errore 4 — Fermarsi quando il grafico racconta una storia convincente

Un pattern interessante non è automaticamente un insight e un insight non è automaticamente una raccomandazione.

Possiamo fermarci troppo presto in due modi opposti. Nel primo consegniamo un grafico senza chiedere quale incertezza riduca o quale decisione possa influenzare. Nel secondo facciamo il salto inverso: trasformiamo rapidamente il pattern in una raccomandazione, nascondendo l'incertezza per rendere il messaggio più netto.

Entrambi gli errori spezzano la catena tra evidenza e uso.

La correzione consiste nel rendere esplicita la distanza fra ciò che osserviamo e ciò che inferiamo. Dobbiamo sapere quale ipotesi il risultato rafforza o indebolisce, quali alternative rimangono credibili, quale livello di fiducia è giustificato e quale decisione è davvero sensibile a quell'informazione.

Questo vale anche per l'AI. Un output generato può essere chiaro, coerente e tecnicamente elegante, ma la qualità della forma non certifica intento, semantica o metodo. Il Capitolo 0 ha definito l'ownership necessaria e il Capitolo 14 entrerà nei controlli tecnici; qui ci basta una disciplina: usare l'AI per ampliare esplorazione ed execution, non come autorità che chiude il ragionamento.

### Il pattern comune dietro molti errori

Gli errori descritti sembrano diversi — tool-first, metrica sbagliata, media ingannevole, causalità prematura, lineage ignorata, incertezza nascosta — ma condividono una struttura.

In tutti i casi una scelta importante viene lasciata implicita. Il tool decide la forma della domanda. La colonna decide la definizione. L'aggregato decide la popolazione. La correlazione decide la storia. Il tono della presentazione decide quanta certezza attribuiamo alla conclusione.

Il lavoro dell'analista consiste in gran parte nel rendere visibili queste scelte prima che diventino errori difficili da riconoscere.

> **L'errore più pericoloso non è quello evidentemente assurdo. È quello plausibile, ben presentato e perfettamente coerente con una domanda formulata male.**
