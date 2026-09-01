## 3.2 Granularità: a quale risoluzione il sistema ha osservato il fenomeno

La **granularità**, o *grain*, descrive che cosa rende distinta una riga.

È uno dei concetti più importanti del lavoro analitico perché stabilisce quali aggregazioni hanno senso e quali invece possono creare doppio conteggio o perdita di informazione.

Una generica "tabella vendite" potrebbe avere:

- una riga per ordine;
- una riga per prodotto nell'ordine;
- una riga per prodotto e giorno;
- una riga per negozio, prodotto e giorno;
- una riga per cliente e mese.

Il nome della tabella non basta. Dobbiamo riuscire a dichiararne il grain in una frase:

> **Una riga rappresenta un prodotto presente in un singolo ordine.**

oppure:

> **Una riga rappresenta lo stock di un prodotto in un magazzino alla fine di una giornata.**

Microsoft, nella documentazione sul dimensional modeling per Microsoft Fabric, sottolinea lo stesso principio: una fact table registra misure a uno specifico livello di granularità insieme alle chiavi che ne descrivono il contesto.[^ms-grain]

### Una colonna può essere corretta ma non additiva al grain corrente

Consideriamo:

| order_id | product | line_amount | order_total |
|---|---|---:|---:|
| 1 | A | 40 | 100 |
| 1 | B | 60 | 100 |

La tabella è a livello di riga d'ordine.

`line_amount` è additivo a quel livello: `40 + 60 = 100`.

`order_total`, invece, è un attributo dell'ordine replicato su ogni linea. La somma `100 + 100 = 200` è sintatticamente possibile ma semanticamente priva di senso.

Questo tipo di errore è insidioso perché non genera eccezioni. Produce un numero plausibile con una query perfettamente valida.

### Una join può cambiare il grain

Supponiamo di partire da:

- `customers`: una riga per cliente;
- `orders`: molte righe per cliente.

Dopo aver collegato le due tabelle, ogni attributo del cliente può essere replicato su più ordini. Il dataset risultante non è più a livello cliente.

Il punto non è imparare qui tutte le tecniche di join — lo faremo nel Capitolo 11 — ma sviluppare un riflesso:

> **Dopo ogni trasformazione importante, chiediti se è cambiato ciò che rappresenta una riga.**

### Grain dichiarato e grain osservato

Anche la documentazione può essere sbagliata o superata.

Se ci viene detto che una tabella contiene una riga per ordine, dovremmo verificare almeno che la chiave attesa sia unica. Se troviamo più righe per `order_id`, le spiegazioni possibili sono diverse:

- la documentazione è sbagliata;
- esistono versioni successive dell'ordine;
- il caricamento ha duplicato record;
- la chiave è composta anche da un'altra colonna;
- il concetto di "ordine" nel sistema è diverso da quello che pensavamo.

Non basta quindi conoscere il grain dichiarato. Serve confrontarlo con il grain osservato.

### Domande operative

Prima di usare una tabella, rispondi a queste domande:

- Che cosa rende unica una riga?
- Quali colonne dovrebbero identificare il grain?
- Quel vincolo è rispettato nei dati?
- Quali misure sono additive a questo livello?
- Quali valori sono già aggregati?
- Una trasformazione o una join può moltiplicare righe?
- Il grain è rimasto stabile nel tempo?

Comprendere la granularità significa capire **la risoluzione con cui il processo reale è diventato dato**.

[^ms-grain]: Microsoft Learn, *Dimensional modeling in Microsoft Fabric*. https://learn.microsoft.com/en-us/fabric/data-warehouse/dimensional-modeling-overview