## 4.12 Caso studio — La correlazione che quasi spostò 600.000 euro di budget

> **Caso simulato/composito.** Azienda, numeri e circostanze sono costruiti a fini didattici.

**Northstar Home**, e-commerce di arredamento, chiude il trimestre con un risultato che sembra abbastanza forte da diventare immediatamente una decisione. La spesa social settimanale e l'average order value settimanale hanno correlazione **`r = 0,76`**; inoltre i clienti attribuiti al social mostrano un AOV aggregato superiore a quelli provenienti dalla search.

Il team marketing propone quindi di spostare **600.000 euro di budget annuale** da search a social. Il ragionamento sembra quantitativo: più social spend coincide con ordini di valore maggiore, quindi aumentare il primo dovrebbe migliorare il secondo.

L'EDA non deve ancora stabilire se la proposta sia giusta o sbagliata. Deve chiedere **quanto la storia sopravviva alla struttura che il coefficiente ha compresso**.

Lo scatter plot è il primo attrito. La relazione positiva esiste, ma quattro settimane sono molto lontane dal resto: Black Friday, pre-Natale e due lanci della nuova linea premium. Con tutte le settimane `r = 0,76`; se separiamo quelle quattro osservazioni in una sensitivity analysis, sulle altre settimane il coefficiente scende a **`0,31`**.

Le settimane eccezionali sono reali e non vanno cancellate dal business. Ma la frase “esiste una forte relazione generale tra social spend e AOV” ha appena perso molta solidità. Una parte consistente del movimento congiunto appartiene a periodi in cui accadono contemporaneamente altre cose importanti.

## Il tempo introduce spiegazioni concorrenti

Nelle stesse quattro settimane aumentano domanda stagionale, bundle e gift set, visibilità dei prodotti premium e traffico complessivo. Social spend e AOV possono quindi muoversi insieme perché entrambi reagiscono allo stesso calendario commerciale. Il coefficiente iniziale non distingue tra un effetto del canale e un contesto che rende elevate entrambe le variabili.

La segmentazione per fascia prodotto restringe ulteriormente la storia:

| Canale | AOV aggregato | Prodotti standard | Prodotti premium |
|---|---:|---:|---:|
| Social | €184 | €121 | €296 |
| Search | €169 | €128 | €301 |
| Direct | €176 | €126 | €299 |

Nell'aggregato Social sembra avere clienti di valore maggiore. Dentro le stesse fasce prodotto, però, non emerge un vantaggio uniforme: sui prodotti standard Search è persino sopra, mentre sulle linee premium i tre canali sono molto vicini. Il social porta semplicemente una quota maggiore di traffico verso le creatività premium.

Questo non rende il canale meno interessante. Cambia ciò che possiamo dire. La differenza di AOV aggregato contiene molto **product mix**, e product mix è a sua volta collegato a creatività, calendario e strategia commerciale.

## L'AOV non è ancora la decisione economica

Anche se riuscissimo a stabilire che il social produce AOV più alto, il business non guadagna automaticamente perché cresce il valore medio dell'ordine. Una riallocazione di 600.000 euro deve essere valutata anche attraverso conversion rate, CAC, contribution margin, return rate, volume incrementale ottenibile e capacità di scalare la spesa.

Il problema analitico cambia quindi forma. Non stiamo più chiedendo soltanto se social spend e AOV siano associati. Stiamo chiedendo se aumentare l'investimento social generi **valore economico incrementale sufficiente rispetto alle alternative**, mantenendo sotto controllo i guardrail.

A questo punto l'EDA può separare ciò che ha realmente guadagnato il diritto di sostenere.

**Osservato:** social spend e AOV settimanale hanno `r = 0,76` nel trimestre; quattro settimane eccezionali influenzano fortemente la relazione; il social ha un mix più orientato ai prodotti premium; dentro le fasce prodotto l'AOV non mostra un vantaggio sistematico.

**Ipotesi candidate:** il social può essere particolarmente efficace nel portare utenti verso linee premium; le creatività premium possono spiegare parte dell'AOV aggregato; stagionalità e lanci possono spiegare parte del movimento congiunto.

**Non dimostrato:** che aumentare la spesa social causi un AOV maggiore e, soprattutto, che spostare 600.000 euro aumenti il contribution margin incrementale.

La domanda che rimane è quindi molto più vicina a una decisione reale:

> **A parità di offerta e mix creativo, aumentare l'investimento social produce abbastanza conversioni e contribution margin incrementali da superare le alternative di allocazione del budget?**

Per rispondere serve un metodo più forte dell'EDA. Northstar non sposta immediatamente l'intero budget: progetta un test limitato nel tempo e nel perimetro, mantiene più stabile il mix creativo e definisce in anticipo metrica economica primaria, CAC, conversion, AOV, contribution margin e guardrail su resi e saturazione. La sperimentazione arriverà nel Capitolo 9.

Il risultato dell'EDA, quindi, non è “social non funziona”. È molto più utile: **una correlazione aggregata non è più sufficiente per giustificare una riallocazione da 600.000 euro, e ora sappiamo quale evidenza dovrebbe sostituirla**.

> **Il valore dell'EDA non si misura dal numero di correlazioni trovate, ma dalla quantità di decisioni premature che rende più difficili da sostenere.**
