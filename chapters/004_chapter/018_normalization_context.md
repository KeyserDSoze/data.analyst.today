## 4.18 Normalizzare per il contesto: quando i numeri grezzi ingannano

Normalizzare significa riportare una misura a una base comparabile. Non è soltanto una tecnica statistica: è un atto di interpretazione.

A seconda del problema possiamo normalizzare per:

- popolazione;
- tempo;
- superficie;
- numero di clienti;
- ordini;
- dipendenti;
- esposizione al rischio;
- capitale investito;
- traffico;
- opportunità commerciali.

### Caso: quale team commerciale è davvero più efficace?

La società B2B **VectorCore Systems** confronta tre team commerciali nel trimestre.

| Team | Contratti chiusi |
|---|---:|
| Enterprise | 42 |
| Mid-Market | 67 |
| SMB | 118 |

SMB sembra dominare.

Poi vengono aggiunte le opportunità qualificate ricevute:

| Team | Contratti | Opportunità | Win rate |
|---|---:|---:|---:|
| Enterprise | 42 | 105 | 40,0% |
| Mid-Market | 67 | 215 | 31,2% |
| SMB | 118 | 590 | 20,0% |

Il quadro cambia. Enterprise chiude meno contratti in valore assoluto ma converte una quota molto più alta delle opportunità.

Poi entra una terza variabile: il valore medio dei contratti.

| Team | Contratti | ACV medio | Nuovo ARR |
|---|---:|---:|---:|
| Enterprise | 42 | 148.000 € | 6,22 M€ |
| Mid-Market | 67 | 46.000 € | 3,08 M€ |
| SMB | 118 | 9.500 € | 1,12 M€ |

Tre metriche producono tre classifiche diverse.

Qual è quella corretta?

Dipende dalla decisione.

Se vogliamo misurare volume, guardiamo i contratti. Se vogliamo valutare efficacia del processo commerciale, il win rate è più informativo. Se vogliamo capire contributo economico, nuovo ARR o margine possono essere più appropriati.

### Normalizzare non significa scegliere la metrica che ci piace

Il rischio opposto consiste nel continuare a cambiare denominatore finché emerge la storia desiderata.

Una buona normalizzazione deve essere definita **prima** di guardare il risultato, sulla base del processo che vogliamo rappresentare.

### Metriche per unità

Molte metriche utili sono rapporti:

- revenue per employee;
- revenue per square meter;
- cost per acquisition;
- tickets per 1.000 customers;
- defects per million opportunities;
- orders per active customer;
- incidents per 100.000 hours worked.

Il vantaggio è che rendono confrontabili entità di dimensione diversa.

Lo svantaggio è che possono nascondere il volume assoluto.

Un piccolo stabilimento può avere il tasso di difetti peggiore ma produrre soltanto il 2% dei pezzi. Un grande stabilimento può avere un tasso migliore ma generare più difetti assoluti.

Per decidere dove intervenire potrebbero servirci entrambi.

### Mostrare numeratore e denominatore

Una buona pratica è non mostrare mai un tasso isolato quando la dimensione della base è rilevante.

Scrivere:

> Conversion rate: 18,4%

è meno informativo di:

> 184 conversioni su 1.000 sessioni eleggibili: 18,4%.

Questo diventa essenziale con segmenti piccoli. Un segmento con conversion rate del 50% su quattro visite non dovrebbe ricevere lo stesso peso decisionale di un segmento al 22% su 80.000 visite.

Prima di confrontare performance, chiediamo quindi:

**Stiamo confrontando numeri, o stiamo confrontando processi equivalenti su basi equivalenti?**
