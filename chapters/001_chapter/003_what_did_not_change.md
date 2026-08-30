## 1.2 Cosa non è cambiato

Se cambiano gli strumenti ma resta stabile il nucleo del lavoro, qual è esattamente questo nucleo?

Possiamo partire da una frase molto comune:

> "Le vendite stanno diminuendo."

Sembra una richiesta semplice. In realtà non è ancora un problema analitico completo.

Prima di aprire Excel, scrivere una query SQL, avviare un notebook Python, costruire una pagina Power BI o interrogare un assistente AI, dobbiamo chiarire il significato della frase.

Che cosa intendiamo per "vendite"?

Fatturato lordo? Fatturato netto? Numero di ordini? Unità vendute? Margine? Ricavi contabilizzati?

Che cosa significa "stanno diminuendo"?

Rispetto alla settimana precedente? Al mese precedente? Allo stesso periodo dell'anno scorso? Al budget? Alla previsione? A un gruppo di controllo? A una tendenza storica?

E soprattutto: **quale decisione deve essere presa dopo l'analisi?**

Se la risposta deve servire al direttore commerciale, potremmo voler capire quali territori o clienti stanno contribuendo al calo. Se deve servire al marketing, potremmo concentrarci sul traffico, sulla conversione o sul costo di acquisizione. Se deve servire alla supply chain, potremmo verificare stock-out, ritardi o disponibilità dei prodotti. Se deve servire al management, potrebbe essere necessario distinguere tra diminuzione dei volumi, variazioni di prezzo, mix di prodotto e marginalità.

La stessa frase iniziale può quindi generare analisi molto diverse.

### L'analisi comincia dalla definizione del problema

Questa è una delle idee più importanti dell'intero libro:

> **L'analisi dei dati non comincia dai dati. Comincia dal problema.**

I dati diventano utili soltanto rispetto a una domanda.

Un dataset può contenere milioni di righe e centinaia di colonne, ma senza una domanda non esiste ancora una direzione analitica. Possiamo esplorarlo, visualizzarlo e descriverlo, ma non sappiamo ancora quale evidenza sia rilevante.

È per questo che framework sviluppati molto prima degli attuali sistemi generativi iniziano dalla comprensione del business. Nella metodologia CRISP-DM la prima fase è esplicitamente la **Business Understanding**: chiarire obiettivi, situazione, vincoli e criteri di successo prima di investire risorse nell'analisi.[^ibm-business]

Questo principio non è diventato meno importante con l'AI. È diventato più importante, perché oggi possiamo produrre risposte molto più rapidamente.

Una risposta veloce a una domanda mal formulata rimane una cattiva risposta.

### Dalla frase vaga alla domanda analitica

Prendiamo ancora il caso delle vendite.

La frase:

> "Le vendite stanno diminuendo."

può essere trasformata progressivamente in una domanda analitica più precisa:

> "Il fatturato netto mensile dell'ultimo trimestre è inferiore rispetto allo stesso trimestre dell'anno precedente?"

Poi possiamo renderla ancora più utile:

> "Quali categorie di prodotto, aree geografiche e segmenti di clientela spiegano maggiormente la variazione del fatturato netto rispetto allo stesso periodo dell'anno precedente?"

E poi collegarla a una decisione:

> "Quali componenti del calo sono abbastanza grandi e controllabili da giustificare un intervento commerciale nel prossimo trimestre?"

Notiamo il cambiamento.

La prima formulazione descrive un'impressione.

La seconda introduce una metrica e un confronto.

La terza cerca i driver.

La quarta collega l'analisi all'azione.

Il lavoro dell'analista è spesso proprio questo: **trasformare una richiesta vaga in una sequenza di domande verificabili**.

### Le definizioni vengono prima dei calcoli

Supponiamo che ci venga chiesto di calcolare il fatturato.

Potrebbe sembrare sufficiente una query come:

```sql
SELECT SUM(price * quantity) AS revenue
FROM order_lines;
```

Tecnicamente la query è plausibile.

Ma prima di considerarla corretta dobbiamo sapere:

- `price` include o esclude l'IVA?
- Lo sconto è già incorporato?
- Gli ordini annullati sono presenti nella tabella?
- I resi vengono sottratti?
- La spedizione fa parte del fatturato?
- Quale valuta viene utilizzata?
- La data dell'ordine coincide con la data di competenza?
- Una riga rappresenta sempre un prodotto acquistato oppure può rappresentare anche un omaggio?

Questi non sono problemi di sintassi SQL.

Sono problemi di **semantica**.

Un sistema AI può scrivere perfettamente la query sbagliata se riceve una definizione incompleta della metrica.

La qualità di un'analisi dipende quindi dalla qualità delle definizioni che stanno sotto ai numeri.

### La granularità non è cambiata

Un altro problema fondamentale rimane la granularità, cioè il livello al quale ogni riga rappresenta il fenomeno osservato.

Una tabella può avere una riga per ordine, una riga per articolo dell'ordine, una riga per cliente al mese o una riga per evento sul sito.

Confondere questi livelli può produrre errori enormi.

Immaginiamo una tabella `orders` con una riga per ordine e una tabella `order_lines` con più righe per ogni ordine. Se uniamo le due tabelle e poi sommiamo una colonna di valore già presente a livello di ordine, potremmo duplicare il fatturato tante volte quante sono le righe dell'ordine.

Il codice può essere sintatticamente perfetto.

Il risultato può essere numericamente preciso.

Eppure la risposta può essere completamente sbagliata.

Capire il **grain** del dato rimane quindi una competenza essenziale indipendentemente dallo strumento utilizzato.

### Correlazione, causalità e spiegazione

Anche un altro problema classico rimane intatto: osservare una relazione non significa averne spiegato la causa.

Supponiamo di scoprire che i clienti che contattano più spesso l'assistenza hanno un tasso di abbandono superiore.

Potremmo concludere:

> "Contattare l'assistenza aumenta il churn."

Ma potrebbe essere vero l'opposto: i clienti con problemi sono più propensi a contattare l'assistenza **e** più propensi ad abbandonare.

Il contatto con il supporto potrebbe essere semplicemente un indicatore di un problema sottostante.

La distinzione tra associazione e causalità non viene risolta da un grafico più bello, da un modello più sofisticato o da un LLM più grande.

Richiede ragionamento, disegno dell'analisi, conoscenza del processo reale e, in alcuni casi, sperimentazione.

### La qualità del dato rimane una responsabilità analitica

Una delle tentazioni dell'automazione è considerare il dataset come una rappresentazione neutrale della realtà.

Non lo è.

I dati sono il risultato di processi.

Qualcuno ha deciso cosa registrare. Un sistema ha scelto quando registrarlo. Un'applicazione ha imposto determinate categorie. Una pipeline ha trasformato i valori. Alcune osservazioni possono mancare. Alcune possono essere duplicate. Alcune definizioni possono essere cambiate nel tempo.

Per questo la fase di Data Understanding di CRISP-DM include esplicitamente l'esame dei dati disponibili e della loro qualità prima della preparazione e della modellazione.[^ibm-data-understanding]

La domanda corretta non è soltanto:

> "Che cosa dice il dataset?"

ma anche:

> "Come è stato prodotto questo dataset e quali parti della realtà non riesce a rappresentare?"

### La decisione rimane il punto di arrivo

Un'analisi tecnicamente impeccabile può comunque avere poco valore se non influenza alcuna decisione.

Questo non significa che ogni analisi debba produrre immediatamente un'azione. Alcune analisi hanno funzione esplorativa, descrittiva o conoscitiva. Ma anche in quei casi dovrebbe essere chiaro quale incertezza stiamo cercando di ridurre.

Possiamo rappresentare il lavoro analitico con una catena:

**Problema -> Domanda -> Dati -> Metodo -> Evidenza -> Interpretazione -> Decisione -> Azione -> Misurazione**

Ogni anello può fallire.

Un problema può essere definito male.
Una domanda può essere troppo vaga.
I dati possono essere incompleti.
Il metodo può essere inappropriato.
L'evidenza può essere interpretata in modo eccessivo.
La decisione può ignorare costi e vincoli.
L'azione può essere eseguita male.
La misurazione successiva può non dirci se l'intervento ha funzionato.

Questa catena sarà il filo conduttore del libro.

### Il principio fondamentale

Alla fine, ciò che non è cambiato può essere espresso in una frase:

> **Un analista non viene pagato per produrre numeri. Viene pagato per ridurre l'incertezza in modo sufficientemente affidabile da migliorare una decisione.**

Gli strumenti possono cambiare radicalmente.

La responsabilità analitica rimane.

---

### Fonti

[^ibm-business]: IBM, *Business Understanding Overview*, metodologia CRISP-DM / SPSS Modeler. https://www.ibm.com/docs/it/spss-modeler/19.0.0?topic=understanding-business-overview
[^ibm-data-understanding]: IBM, *Data Understanding Overview*, metodologia CRISP-DM / SPSS Modeler. https://www.ibm.com/docs/en/spss-modeler/saas?topic=understanding-data-overview
