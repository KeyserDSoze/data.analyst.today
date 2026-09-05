## 3.17 Sintesi ed esercizi

Il Capitolo 2 ci ha insegnato a non iniziare dall'output. Questo capitolo aggiunge una seconda disciplina: **non iniziare nemmeno dal presupposto che il dataset rappresenti già correttamente ciò che vogliamo analizzare**.

Prima della statistica viene una ricostruzione. Dobbiamo capire che cosa rappresenta una riga, quale grain rende distinti i record, che cosa identifica davvero una chiave, quale tempo descrive il dataset, perché alcuni valori mancano, quando più record rappresentano la stessa realtà, quali estremi sono errori e quali eventi reali, quali trasformazioni separano la sorgente dal report e se il risultato si riconcilia con una fonte indipendente.

Il percorso può essere sintetizzato così:

**Riga → grain → identità → tempo → qualità → anomalie → lineage → riconciliazione → data readiness**

Ma il valore non sta nella sequenza come checklist. Sta nel fatto che ogni passaggio restringe il confine delle conclusioni che possiamo sostenere. Un grain ambiguo rende sospetti i conteggi; un'identità instabile altera retention e clienti unici; un timestamp che cambia significato rompe la comparabilità; un missing concentrato in un segmento può selezionare la popolazione; una riconciliazione incompleta può impedire di usare il dato per un consuntivo pur lasciandolo utile per un monitoraggio preliminare.

Per questo il verdetto finale non è “dataset pulito”. È **PRONTO / PRONTO CON CAVEAT / NON PRONTO** rispetto a una domanda specifica. La maturità consiste nel sapere abbastanza del dato da spiegare dove può essere usato, dove richiede limiti e dove una conclusione sarebbe prematura.

Gli artefatti introdotti nel capitolo — schede di variabile, reconciliation bridge, data contract, controlli automatici e Data Readiness Review — servono proprio a rendere riutilizzabile questa conoscenza, così che l'organizzazione non debba riscoprire ogni volta gli stessi problemi.

---

### Esercizio 1 — Qual è davvero il grain?

Hai una tabella:

```text
order_id
customer_id
order_date
product_id
quantity
unit_price
```

`order_id` compare più volte.

Elenca almeno cinque spiegazioni compatibili con questo comportamento.

Poi specifica quali controlli useresti per distinguere tra:

- riga d'ordine legittima;
- duplicato tecnico;
- versione successiva dell'ordine;
- rettifica;
- errore nella chiave attesa.

Non deduplicare prima di avere una teoria del record.

---

### Esercizio 2 — Il cliente unico che non è unico

Un e-commerce usa `customer_id` come chiave cliente.

Scopri che:

- il 7% delle email compare su più `customer_id`;
- il 3% dei clienti ha cambiato email;
- esistono account familiari condivisi;
- il guest checkout genera nuovi ID.

Disegna una strategia di identity resolution e indica almeno due possibili **false merge** e due **false split**.

Poi spiega come gli errori di identità influenzerebbero:

- nuovi clienti;
- repeat purchase;
- retention;
- customer lifetime value.

---

### Esercizio 3 — Missing che cambia la conclusione

Un servizio di delivery ha `delivered_at` mancante nel 6% degli ordini.

Segmentando scopri:

```text
App courier v5:  1,2%
App courier v4: 23,8%
```

La versione v4 è utilizzata soprattutto in aree rurali.

Spiega perché calcolare il tempo medio di consegna soltanto sui record completi può essere fuorviante.

Proponi:

- controlli aggiuntivi;
- possibili fonti alternative;
- una comunicazione corretta del caveat;
- una condizione che renderebbe il dato non pronto.

---

### Esercizio 4 — Outlier: errore o informazione?

Una distribuzione degli importi contiene questi ordini:

```text
€14
€27
€83
€410
€48.000
€999.999
```

Non sai ancora se gli ultimi due siano errori.

Costruisci un piano di investigazione senza utilizzare una soglia automatica di esclusione.

Per ciascun record indica quali campi, sorgenti e domain expert consulteresti.

---

### Esercizio 5 — Il numero senza unità

Un file contiene:

```text
weight = 180
speed = 65
temperature = 70
rate = 0.12
```

Per ogni variabile elenca almeno due interpretazioni possibili.

Poi spiega perché il caso reale del **Mars Climate Orbiter** è un esempio estremo dello stesso principio: un valore numerico può essere formalmente disponibile ma inutilizzabile se l'unità interpretata dai sistemi non coincide.

Riferimento: NASA Lessons Learned, *Mars Climate Orbiter Mishap Investigation Board — Phase I Report, Lesson 641*. https://llis.nasa.gov/lesson/641

---

### Esercizio 6 — Revenue A contro Revenue B

Due dashboard mostrano per marzo:

```text
Finance: €6,42 milioni
Sales:   €6,81 milioni
```

Costruisci una reconciliation bridge ipotetica considerando almeno:

- data di riconoscimento;
- ordini cancellati;
- resi;
- IVA;
- spedizione;
- cambio valuta;
- freshness;
- grain;
- filtri di canale.

Concludi indicando se le due metriche dovrebbero convergere oppure mantenere nomi e usi differenti.

---

### Esercizio 7 — Progetta controlli che valgano qualcosa

Per una tabella `orders_daily` definisci cinque test automatici.

Per ciascuno specifica:

| Campo | Cosa definire |
|---|---|
| Regola | proprietà attesa |
| Razionale | perché conta per il business |
| Soglia | quando considerarla violata |
| Severità | warning / failure / blocking |
| Owner | chi deve reagire |
| Azione | cosa succede dopo il fallimento |

Evita test deboli come `row_count > 0` se non sono sufficienti a proteggere l'uso reale del dato.

---

### Esercizio 8 — Data Readiness Review

Riprendi un dataset che conosci oppure un dataset pubblico e produci una review di una pagina con queste sezioni:

```text
Domanda analitica:
Grain:
Chiavi e identità:
Tempo:
Completezza:
Validità e outlier:
Lineage/provenance:
Riconciliazioni disponibili:
Issue critiche:
Caveat:
Verdetto: PRONTO / PRONTO CON CAVEAT / NON PRONTO
```

La parte più importante è motivare il verdetto rispetto alla **domanda**, non assegnare un voto astratto alla qualità del dataset.

---

### Caso finale — Quattro ore prima del board

Sei responsabile del report mensile di una società subscription.

Il board è domani mattina.

La prima build mostra:

- MRR +7,4%;
- nuovi clienti +12,1%;
- churn dal 4,8% al 3,1%;
- ARPU invariato.

Durante il profiling emergono tre segnali:

1. la tabella subscription contiene il 6% di righe in più del mese precedente;
2. circa 18.000 subscription hanno `cancelled_at = NULL` ma risultano chiuse nel billing;
3. una nuova pipeline è entrata in produzione undici giorni fa.

Hai quattro ore.

Prepara un piano operativo che specifichi:

1. quali KPI consideri immediatamente a rischio;
2. quale grain e quali chiavi verifichi per primi;
3. come distingui crescita reale da duplicazione;
4. come riconcili lo stato delle subscription con il billing;
5. quali controlli fai prima e dopo il deploy della nuova pipeline;
6. quali stakeholder coinvolgi;
7. quale verdetto di data readiness assegni a ogni KPI;
8. che cosa comunichi al board se il problema non viene risolto entro la scadenza.

Il punto non è riuscire a “salvare” il report a tutti i costi. È mostrare che sai proteggere una decisione dalla falsa precisione.

### Domande di autovalutazione

Alla fine del capitolo dovresti saper rispondere con sicurezza:

- Che differenza c'è tra record, entità e unità di analisi?
- Come dichiaro e verifico il grain?
- Perché una chiave unica non garantisce una corretta identity resolution?
- Quando una misura è un evento, uno stock o uno snapshot?
- Come distinguo missing strutturale, da processo e introdotto da una join?
- Perché `SELECT DISTINCT *` non risolve necessariamente i duplicati?
- Come distinguo un valore impossibile da uno raro ma reale?
- Perché unità e dominio fanno parte della semantica?
- Che cosa cerco nei primi minuti di data profiling?
- Come ricostruisco il lineage minimo di una metrica?
- Che cosa significa riconciliare due numeri?
- Quando una scoperta dovrebbe diventare un data contract o un test automatico?
- Come giustifico un verdetto **pronto / pronto con caveat / non pronto**?

## Chiusura

Il Capitolo 3 completa il lavoro preparatorio iniziato nel Capitolo 2. L'Analytical Brief definisce che cosa vorremmo sapere; la Data Readiness Review verifica se le fonti disponibili possono davvero sostenere quella pretesa. Soltanto quando questi due livelli sono coerenti ha senso passare alla descrizione statistica del fenomeno.

Nel prossimo capitolo inizieremo quindi a osservare distribuzioni, confronti e pattern. Ma entreremo in quella fase con una distinzione già acquisita: **un riepilogo numerico descrive ciò che il dataset contiene; non dimostra da solo perché il fenomeno esista né che la rappresentazione sia perfetta**.

Prima di fare statistica sui dati, dobbiamo sapere che cosa stiamo contando. Dopo questo capitolo, quella frase non è più un avvertimento generico: è un metodo operativo.
