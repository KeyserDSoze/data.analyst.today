## 8.1 Il controfattuale: definire l'alternativa prima di misurare l'effetto

Per una stessa unità vorremmo osservare due mondi:

- risultato se riceve il trattamento;
- risultato se non lo riceve.

Nel linguaggio dei *potential outcomes*:

- `Y(1)` = outcome sotto trattamento;
- `Y(0)` = outcome sotto controllo.

L'effetto individuale sarebbe:

`Y(1) - Y(0)`

Ma per una stessa unità e nello stesso momento ne osserviamo soltanto uno.

Questo è il **fundamental problem of causal inference**: il controfattuale individuale manca per definizione.

### Caso simulato/composito — Il coupon da 20 euro

Un retailer invia un coupon a 50.000 clienti. Entro trenta giorni:

- conversione tra i destinatari: 24%;
- conversione tra i non destinatari: 15%.

Il `+9 pp` è una differenza osservata.

Non possiamo ancora chiamarla effetto causale.

Il marketing ha scelto i destinatari tra clienti con almeno tre visite recenti. Quindi il gruppo trattato aveva già un intento di acquisto maggiore.

La domanda causale non è:

> “Quanto acquistano i destinatari rispetto agli altri?”

È:

> **“Quanto avrebbero acquistato quei clienti se, a parità del resto, non avessero ricevuto il coupon?”**

### Anche il prima/dopo ha un controfattuale implicito

Supponiamo che la conversione dei clienti target fosse 17% prima e 24% dopo.

Un'analisi `24% - 17% = +7 pp` assume implicitamente che, senza coupon, la conversione sarebbe rimasta al 17%.

Ma nel frattempo può essere iniziato Natale, può essere cambiato il catalogo, può essere aumentato il traffico o il prezzo può essere sceso.

Il “prima” non è automaticamente il controfattuale del “dopo”.

### L'estimand decide quale controfattuale serve

Non esiste un unico “effetto del trattamento”.

Possiamo voler stimare:

- **ATE — Average Treatment Effect:** effetto medio nella popolazione target;
- **ATT — Average Treatment Effect on the Treated:** effetto medio sulle unità che hanno effettivamente ricevuto il trattamento;
- **CATE — Conditional Average Treatment Effect:** effetto medio in un sottogruppo definito;
- un effetto locale, per esempio vicino a una soglia;
- un effetto su una specifica versione del trattamento.

Queste quantità rispondono a decisioni diverse.

Se un programma di retention è oggi offerto solo ad account recuperabili, l'ATT può essere molto diverso dall'ATE che otterremmo estendendolo a tutti.

### Trattamento e alternativa devono essere ben definiti

“Customer Success” non è un trattamento abbastanza preciso.

Potrebbe significare:

- una telefonata di 15 minuti;
- tre sessioni tecniche;
- un account manager dedicato;
- un voucher;
- una combinazione di interventi.

Se unità diverse ricevono versioni molto diverse, la causal claim diventa ambigua.

Una specifica più utile è:

```text
Unità: account SMB
Trattamento: sessione tecnica di 45 minuti entro 7 giorni
Alternativa: onboarding standard senza sessione extra
Outcome: rinnovo entro 90 giorni
Popolazione: account che non hanno completato ERP integration entro D30
```

### Consistency: il trattamento osservato deve corrispondere a quello definito

Una causal claim presume che quando diciamo `trattamento = 1` sappiamo che cosa è stato realmente ricevuto.

Se nel gruppo “training” alcuni ricevono un video automatico e altri un workshop con consulente senior, stiamo mescolando versioni diverse.

Prima di stimare l'effetto bisogna verificare:

- assignment;
- exposure effettiva;
- intensità;
- timing;
- eventuale cross-over.

Il Capitolo 9 entrerà nel dettaglio operativo degli esperimenti. Qui fissiamo il principio causale: **non possiamo interpretare un trattamento che non sappiamo definire**.

### Interference: il controfattuale di uno può dipendere dagli altri

Molti esempi semplici assumono che il trattamento di un'unità non modifichi l'outcome di un'altra.

Ma nel mondo reale può esserci interferenza:

- una promozione a un seller sottrae domanda ad altri seller;
- un nuovo algoritmo cambia il marketplace per tutti;
- un training a un manager influenza il suo team;
- un aumento prezzi in una regione sposta clienti nella regione confinante.

Quando esistono spillover, la domanda causale deve includerli oppure scegliere un'unità di trattamento coerente.

### Il controfattuale è una costruzione, non una colonna mancante

Un buon comparison group non è “il gruppo che abbiamo trovato nel database”.

È un gruppo per cui possiamo argomentare:

> **in assenza del trattamento avrebbe riprodotto, abbastanza bene, l'outcome che i trattati avrebbero avuto senza intervento.**

Metodi diversi costruiscono questo argomento in modi differenti.

Randomizzazione, DiD, matching, RDD e IV non sono varianti della stessa formula. Sono strategie diverse per rendere plausibile un controfattuale non osservato.

> **Prima di calcolare l'effetto, scrivi il mondo alternativo che vuoi rappresentare. Se non sai descriverlo, non hai ancora una causal question sufficientemente definita.**

### Riferimenti

- World Bank e Inter-American Development Bank, *Impact Evaluation in Practice*, capitolo 3, causal inference e counterfactuals: https://www.worldbank.org/en/programs/sief-trust-fund/publication/impact-evaluation-in-practice
- Stanford University, STATS 209, *Introduction to Causal Inference*: https://bulletin.stanford.edu/courses/2235031
