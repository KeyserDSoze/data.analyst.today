## 1.12 Il Data Analyst come orchestratore di persone, dati, strumenti e AI

L'immagine tradizionale del Data Analyst è spesso troppo stretta.

Lo si immagina davanti a un foglio Excel, a una query SQL o a una dashboard.

Ma in un'organizzazione reale l'analista opera all'interno di un sistema molto più ampio. Deve comprendere persone, processi, definizioni, fonti dati, vincoli tecnologici, priorità economiche e modalità con cui una decisione verrà effettivamente presa.

Nell'era dell'AI questo ruolo si avvicina sempre di più a quello di un **orchestratore**.

### Orchestrare non significa sapere tutto

Un buon analista non deve essere necessariamente il miglior database administrator, il miglior data engineer, il miglior statistico, il miglior designer e il miglior esperto di machine learning contemporaneamente.

Deve però sapere abbastanza di ciascuna area da riconoscere:

- quale problema sta affrontando;
- quale competenza è necessaria;
- quale strumento è adeguato;
- quando può procedere in autonomia;
- quando deve coinvolgere uno specialista;
- come verificare che il risultato sia coerente con il problema.

Questa è una competenza diversa dal semplice possesso di un elenco di tool.

### Il percorso di un dato reale

Immaginiamo una metrica mostrata in una dashboard executive: `Monthly Recurring Revenue`.

Dietro quel singolo numero potrebbe esserci una catena composta da:

1. un utente che sottoscrive un piano;
2. un sistema applicativo che registra l'evento;
3. un database transazionale;
4. una pipeline che copia o trasforma i dati;
5. un data warehouse;
6. tabelle intermedie;
7. regole per upgrade, downgrade, cancellazioni e rimborsi;
8. un modello semantico;
9. una misura definita in SQL, DAX o un semantic layer;
10. una dashboard;
11. una presentazione al management;
12. una decisione commerciale.

Un errore in qualsiasi punto può modificare il numero finale.

Per questo un analista senior deve sviluppare una sorta di **visione end-to-end del dato**.

Non significa che debba gestire personalmente ogni componente. Significa che deve sapere che esiste.

### Dal tool-first al problem-first

Un analista inesperto tende a ragionare così:

> Ho Power BI. Come posso risolvere questo problema con Power BI?

Oppure:

> Sto studiando Python. Devo usare Python per questa analisi.

L'approccio maturo è l'opposto:

> Qual è il problema? Qual è il modo più semplice, affidabile e sostenibile di risolverlo?

Se dobbiamo analizzare una tabella di 2.000 righe una sola volta, Excel potrebbe essere perfettamente adeguato.

Se dobbiamo aggregare miliardi di righe già presenti nel warehouse, estrarle tutte in Python sul laptop potrebbe essere una pessima decisione.

Se dieci dirigenti devono consultare quotidianamente le stesse metriche, una dashboard governata può essere migliore di dieci notebook.

Se dobbiamo esplorare rapidamente una domanda nuova e non ripetitiva, un notebook può essere migliore di una dashboard formalizzata.

Se una trasformazione deve essere eseguita ogni giorno e alimentare molti sistemi, probabilmente stiamo entrando nel territorio delle pipeline e dell'analytics engineering.

Lo strumento corretto dipende dal contesto.

### Cinque dimensioni per scegliere uno strumento

Nel corso del libro costruiremo un vero Tool Decision Framework. Per ora possiamo introdurre cinque dimensioni fondamentali.

**1. Volume**

Quanti dati dobbiamo elaborare?

**2. Frequenza**

È un'analisi una tantum o deve essere ripetuta ogni ora, giorno o mese?

**3. Complessità**

Serve una semplice aggregazione o una pipeline con molte trasformazioni e modelli statistici?

**4. Audience**

Il risultato serve all'analista, a cinque manager o a migliaia di utenti?

**5. Governance**

Quanto è importante che definizioni, accessi, lineage e riproducibilità siano controllati?

A queste dimensioni se ne aggiungeranno altre: costo, latenza, sicurezza, competenze del team, mantenibilità e lock-in tecnologico.

### Il ruolo dell'AI nell'orchestrazione

L'AI diventa un nuovo livello della toolchain.

Può aiutare l'analista a:

- generare SQL;
- spiegare una query complessa;
- costruire uno script Python;
- proporre controlli di qualità;
- documentare una metrica;
- suggerire visualizzazioni;
- generare ipotesi;
- sintetizzare risultati;
- trasformare linguaggio naturale in interrogazioni sui dati;
- accelerare la comprensione di un codebase o di un modello semantico.

Ma il valore più interessante non è semplicemente "fare prima la stessa cosa".

È aumentare il numero di iterazioni analitiche che possiamo permetterci.

Un analista che impiegava due ore per testare un'ipotesi potrebbe ora testarne cinque nello stesso intervallo di tempo.

Questo cambia il processo di esplorazione.

### Più velocità richiede più disciplina

La velocità, però, crea un nuovo rischio.

Se un assistente genera una query in trenta secondi, siamo tentati di eseguirla senza comprenderla completamente.

Se produce una spiegazione convincente di un grafico, siamo tentati di inserirla in una presentazione.

Se suggerisce una metrica, siamo tentati di considerarla standard.

Il nuovo analista deve quindi sviluppare un ciclo di lavoro esplicito:

**Ask → Generate → Inspect → Validate → Compare → Decide**

Non semplicemente:

**Ask → Copy → Paste**

### Semantic model e AI

La relazione tra AI e semantica dei dati è già evidente nei moderni strumenti BI.

La documentazione Microsoft sui semantic model sottolinea che metriche curate, nomi business-friendly, relazioni e logica di calcolo centralizzata rendono più coerenti sia le analisi tradizionali sia le domande poste in linguaggio naturale agli agenti AI.

Questo suggerisce una trasformazione importante.

Più l'interfaccia diventa naturale, più il livello semantico sottostante deve essere rigoroso.

Se l'utente può chiedere semplicemente:

> "Quanto è cresciuta la retention dei clienti enterprise?"

il sistema deve già sapere:

- cosa significa cliente enterprise;
- cosa significa retention;
- quale periodo usare;
- quale popolazione considerare;
- quali relazioni tra tabelle sono corrette.

L'AI elimina parte della sintassi visibile, ma non elimina la necessità di costruire il significato.

### L'analista come ponte

Il Data Analyst moderno si trova spesso tra mondi differenti.

Parla con il business, che ragiona in termini di clienti, ricavi, costi e decisioni.

Parla con i dati, che esistono sotto forma di tabelle, eventi, colonne e timestamp.

Parla con la tecnologia, che impone vincoli di architettura e performance.

Parla con statistica e metodologia, che stabiliscono cosa possiamo inferire.

Parla con l'AI, che accelera la produzione ma richiede contesto e verifica.

Il valore dell'analista sta nella capacità di collegare questi mondi senza confonderli.

### Una definizione operativa del Data Analyst moderno

Possiamo quindi proporre una prima definizione che accompagnerà il resto del libro:

> **Un Data Analyst è una persona che riduce l'incertezza attorno a decisioni reali trasformando problemi in domande, dati in evidenza ed evidenza in azioni verificabili, scegliendo e orchestrando gli strumenti più appropriati.**

Excel, SQL, Python, Power BI, cloud e AI sono parti importanti del mestiere.

Ma nessuno di essi, preso singolarmente, definisce il mestiere.

### La domanda che conclude il capitolo

Davanti a ogni nuovo problema analitico proveremo progressivamente a rispondere a questa sequenza:

> **Quale decisione dobbiamo prendere? Quale domanda ci aiuta a prenderla? Quali dati rappresentano realmente il fenomeno? Quali definizioni stiamo usando? Quanto possiamo fidarci dei dati? Quale metodo è appropriato? Quale strumento è sufficiente? Quale parte può essere delegata all'AI? Come verifichiamo il risultato? Come comunichiamo l'incertezza? Come misuriamo ciò che succede dopo la decisione?**

Se impariamo a rispondere bene a queste domande, i tool diventano ciò che dovrebbero essere:

strumenti al servizio dell'analisi.

Non l'analisi stessa.

### Fonti e approfondimenti

- Microsoft Learn, *Power BI semantic models*: https://learn.microsoft.com/en-us/power-bi/connect-data/semantic-models-third-party
- Microsoft Learn, *Use Copilot with Semantic Models in Power BI*: https://learn.microsoft.com/en-us/power-bi/create-reports/copilot-semantic-models
- Microsoft Learn, *Optimize your semantic model for Copilot in Power BI*: https://learn.microsoft.com/en-us/power-bi/create-reports/copilot-evaluate-data
