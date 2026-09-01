## 4.1 Media e mediana: due idee diverse di "valore tipico"

Quando dobbiamo riassumere una variabile numerica, la prima tentazione è cercare un singolo numero che la rappresenti.

Il problema è che non esiste un unico concetto di "centro".

La **media aritmetica** divide il totale per il numero di osservazioni. È il punto di equilibrio della distribuzione ed è fondamentale quando ci interessa il totale economico sottostante.

La **mediana** è invece il valore centrale una volta ordinate le osservazioni: metà dei casi si trova sotto e metà sopra. È molto meno sensibile ai valori estremi.

Nessuna delle due è universalmente migliore.

Rispondono a domande differenti.

### Caso simulato/composito — Lo stipendio medio dell'azienda

Una startup tecnologica con 41 dipendenti comunica che lo stipendio medio annuo è **62.400 euro**.

La cifra è corretta.

La distribuzione, però, è fortemente asimmetrica:

- 18 persone tra 32.000 e 40.000 euro;
- 13 tra 40.000 e 55.000;
- 6 tra 55.000 e 75.000;
- 3 dirigenti oltre 140.000;
- CEO a 260.000 euro.

La mediana è **46.800 euro**.

Se la domanda è:

> Quanto spende mediamente l'azienda per dipendente?

la media è molto utile.

Se la domanda è:

> Quale retribuzione descrive meglio l'esperienza del dipendente centrale?

la mediana è più informativa.

Il conflitto nasce quando chiamiamo entrambe semplicemente "stipendio tipico".

### La media è sensibile alla coda per una ragione

Supponiamo che cinque ordini valgano:

```text
€20, €25, €30, €35, €390
```

Media:

```text
€100
```

Mediana:

```text
€30
```

La media sembra poco rappresentativa del singolo ordine, ma incorpora correttamente il fatto che un ordine da 390 euro pesa molto sul fatturato totale.

Quindi la sua sensibilità agli estremi non è sempre un difetto. Dipende da ciò che vogliamo misurare.

### Una domanda importante: qual è l'unità su cui stiamo facendo la media?

"Ricavo medio" può significare:

- ricavo medio per ordine;
- ricavo medio per cliente;
- ricavo medio per giorno;
- ricavo medio per prodotto;
- ricavo medio per sessione.

Sono statistiche diverse anche quando provengono dallo stesso dataset.

Prima di interpretare una media dobbiamo quindi dichiarare:

> **media di che cosa, calcolata su quale unità di analisi?**

Il grain è già stato verificato nel Capitolo 3; qui ne vediamo la conseguenza statistica.

### Quando media e mediana divergono, la divergenza è informazione

Se media e mediana sono molto distanti, può esserci:

- forte asimmetria;
- una coda lunga;
- concentrazione economica;
- più popolazioni mescolate;
- valori estremi influenti.

Non dobbiamo scegliere subito quale delle due "sia quella giusta".

Dobbiamo guardare la distribuzione.

### Oltre al centro

Per descrivere seriamente una variabile numerica, il centro dovrebbe essere accompagnato da almeno una misura di dispersione e, quando rilevante, da quantili o una visualizzazione della forma.

Un report del tipo:

> tempo medio di risposta: 3,2 ore

è molto più povero di:

> mediana 1,1 ore; media 3,2; P90 8,7; distribuzione fortemente asimmetrica a destra.

Il secondo non contiene soltanto più numeri. Contiene una rappresentazione più fedele dell'esperienza.

### Regola operativa

Prima di usare una misura centrale chiediti:

1. Qual è l'unità di analisi?
2. Mi interessa il totale/equilibrio oppure il caso centrale?
3. La distribuzione è asimmetrica?
4. Pochi valori influenzano fortemente la media?
5. Media e mediana portano alla stessa decisione?

> **Una media non è "il dato". È una particolare compressione della distribuzione.**