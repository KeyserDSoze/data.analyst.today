## 5.18 Multiple testing: quando cercare abbastanza a lungo garantisce una falsa scoperta

Se esegui un solo test con livello di significatività del 5%, accetti un certo rischio di falso positivo. Se esegui decine o centinaia di test indipendenti e poi mostri soltanto quelli con p-value più piccolo, il rischio di trovare almeno una "scoperta" casuale cresce rapidamente.

Questo è il problema del multiple testing.

### Caso realistico: il team growth trova 14 segmenti "vincenti"

Una piattaforma subscription lancia una nuova offerta annuale. Il risultato globale non è particolarmente interessante. La conversione passa dal 6,21% al 6,28%.

Il team growth decide allora di esplorare i risultati per:

- 8 paesi;
- 5 fasce d'età;
- 4 canali di acquisizione;
- 3 device;
- nuovi vs clienti di ritorno;
- 6 fasce di spesa storica.

In poche ore vengono prodotti più di cento confronti.

Quattordici segmenti mostrano p < 0,05. Il più spettacolare è "utenti iOS, 25-34 anni, acquisiti da paid social in Spagna": +11,8% di conversione relativa.

Il team propone una campagna dedicata.

L'analyst chiede una cosa semplice: quanti segmenti sono stati testati prima di trovare quello?

La risposta cambia completamente il significato della scoperta.

Se si eseguono molti test, alcuni risultati estremi emergeranno per puro caso anche quando non esiste alcun effetto specifico nei segmenti.

### Fishing expedition e p-hacking

Il problema non è esplorare. L'esplorazione è fondamentale.

Il problema nasce quando un'analisi esplorativa viene presentata come se fosse stata una verifica confermativa pianificata in anticipo.

Cercare pattern nei dati è legittimo. Ma un pattern trovato dopo aver provato molte combinazioni dovrebbe essere trattato come ipotesi da verificare su nuovi dati, non come prova definitiva.

### Family-Wise Error Rate

Se facciamo \(m\) test indipendenti ciascuno con α = 0,05, la probabilità di ottenere almeno un falso positivo cresce con \(m\).

Con 20 test indipendenti, la probabilità di almeno un falso positivo sotto null tutte vere è approssimativamente:

\[
1 - (1 - 0.05)^{20} \approx 64\%
\]

Quindi non è sorprendente trovare "qualcosa" quando si guarda abbastanza a lungo.

### Correzioni

Esistono diversi approcci. Bonferroni riduce la soglia per ogni singolo test dividendo α per il numero di confronti. È semplice e conservativo.

Altri metodi, come Holm, controllano anch'essi il family-wise error rate in modo meno rigido. Quando il problema è gestire una grande quantità di scoperte, può essere più appropriato controllare il False Discovery Rate con procedure come Benjamini-Hochberg.

La scelta dipende dal costo dei falsi positivi e dal tipo di analisi.

### Caso realistico: 60 metriche in un A/B test

Una marketplace company testa un nuovo layout. Il documento iniziale definisce una metrica primaria: purchase conversion rate. Ma nel dashboard dell'esperimento compaiono anche 59 metriche secondarie.

La metrica primaria non cambia. Tre metriche secondarie hanno p < 0,05:

- click sulla wishlist +4,2%;
- tempo sulla pagina +2,1%;
- apertura FAQ +7,8%.

Il product manager propone di dichiarare il test positivo perché "tre KPI sono significativamente migliori".

Questa interpretazione ignora il fatto che 60 metriche sono state osservate. Se nessun effetto fosse reale, aspettarsi alcuni p-value piccoli non sarebbe affatto sorprendente.

Una pratica migliore è definire prima:

- metrica primaria;
- metriche secondarie;
- guardrail metrics;
- piano di analisi;
- eventuale strategia di correzione per confronti multipli.

### Regola editoriale per l'analyst

Quando presenti un risultato statisticamente interessante, aggiungi sempre una domanda mentale:

**Quante opportunità avevamo di trovare qualcosa di interessante?**

Un p-value non porta con sé la memoria di tutti i test che hai eseguito prima di arrivare a quello che stai mostrando.

La trasparenza su numero di confronti, analisi esplorative e ipotesi definite a posteriori è quindi parte integrante della qualità analitica.
