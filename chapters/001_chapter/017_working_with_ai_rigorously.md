## 1.16 Dove entra l'AI nel metodo analitico

Dopo il Capitolo 0 non serve un secondo manifesto sull'uso responsabile dell'AI. Serve collocarla nel processo che abbiamo appena costruito.

La catena del capitolo è:

**Problema → Domanda → Dati → Metodo → Evidenza → Interpretazione → Decisione → Azione → Misurazione**

L'AI può contribuire quasi ovunque, ma il suo ruolo non è identico in tutti i passaggi. Capire questa differenza evita due estremi: relegarla alla sola generazione di codice oppure trattarla come un analista completo a cui consegnare una domanda vaga e dal quale aspettarsi una decisione pronta.

### All'inizio amplia lo spazio delle possibilità

Nelle fasi di framing ed esplorazione l'AI è utile soprattutto perché genera alternative a basso costo.

Davanti a una richiesta vaga può proporre più formulazioni analitiche, suggerire metriche possibili, far emergere dati che potrebbero mancare e costruire ipotesi concorrenti. Può anche interrogare documentazione o schemi e aiutarci a capire quali parti di un sistema meritino una prima ispezione.

Il valore qui sta nella **divergenza**: vedere più possibilità di quelle che avremmo prodotto da soli nello stesso tempo.

Il rischio nasce se confondiamo la prima formulazione convincente con quella corretta. Un modello non conosce automaticamente la decisione implicita, la politica aziendale, le eccezioni semantiche o ciò che il dataset non registra. Per questo il framing assistito deve terminare con una scelta umana esplicita su domanda, popolazione, metrica e livello di evidenza necessario.

### Nel mezzo riduce il costo dell'esecuzione e della critica

Durante data preparation, query, analisi e modellazione l'AI può generare SQL e Python, spiegare codice esistente, proporre controlli, costruire segmentazioni, suggerire visualizzazioni e aiutare a diagnosticare anomalie.

È il punto in cui il guadagno di produttività può essere più visibile, ma anche quello in cui una semantica sbagliata può essere implementata con grande efficienza. Una query corretta sulla tabella sbagliata rimane sbagliata per la decisione. Un test statistico eseguito bene non salva un confronto non comparabile.

Per questo l'AI non dovrebbe servire soltanto a produrre. Può anche essere usata come critico: cercare spiegazioni rivali, formulare failure mode, proporre test ortogonali o chiedersi quali dati renderebbero falsa la conclusione corrente. La stessa capacità che aumenta il volume dell'execution può quindi aumentare anche la pressione a cui sottoponiamo l'analisi.

### Alla fine aiuta a comunicare, ma non aumenta da sola la forza dell'evidenza

Nella fase di sintesi un sistema generativo può trasformare risultati tecnici in una prima bozza leggibile, confrontare scenari, preparare un memo o suggerire come spiegare un limite.

Qui il rischio cambia forma. Il testo può diventare più fluido della nostra evidenza. Una relazione osservazionale può essere riscritta come causa, un'incertezza può sparire per rendere il messaggio più netto e una raccomandazione può sembrare inevitabile soltanto perché è espressa bene.

La revisione finale deve quindi verificare non solo che il testo sia chiaro, ma che ogni affermazione conservi il livello di certezza consentito dal metodo. L'AI può migliorare la comunicazione di una conclusione; non può trasformare un'evidenza debole in un'evidenza forte.

### Una regola unica per tutto il processo

Possiamo riassumere il rapporto fra AI e metodo analitico così:

> **Usa l'AI per ampliare ciò che puoi esplorare e produrre. Usa evidenza, controlli e giudizio per restringere ciò che sei disposto a credere e consegnare.**

Il **Capitolo 0 — Al timone** descrive ownership, verifica, stop condition e livelli di autonomia. Il **Capitolo 14 — AI-assisted analytics** entrerà nei workflow operativi e tecnici.

Nel resto del libro l'AI comparirà invece dove modifica concretamente il lavoro, senza diventare ogni volta il centro del discorso. È una scelta editoriale ma anche metodologica: **questo libro parla di analisi nell'era dell'AI, non di AI al posto dell'analisi.**
