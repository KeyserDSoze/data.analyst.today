## 5.18 Multiple testing: più occasioni abbiamo di trovare un segnale, più dobbiamo ricordarcelo

L'analisi moderna rende facilissimo provare molte metriche, segmenti, finestre temporali e specificazioni.

Questo è utile per esplorare.

Diventa pericoloso quando il risultato più interessante trovato dopo decine di tentativi viene presentato come se fosse l'unico test pianificato dall'inizio.

Il problema non è soltanto il **multiple testing esplicito**. È anche la molteplicità nascosta nelle scelte analitiche.

### Caso simulato/composito — Il segmento perfetto trovato al centododicesimo tentativo

Una piattaforma subscription introduce una nuova offerta annuale.

Nel totale:

- controllo: conversione 6,21%;
- offerta: 6,28%.

Il risultato globale è poco interessante.

Il team growth esplora quindi:

- 8 paesi;
- 5 fasce d'età;
- 4 canali;
- 4 device/platform;
- nuovi vs returning;
- 6 fasce di spesa storica;
- varie combinazioni tra questi attributi.

Dopo oltre cento confronti trova:

> **iOS, 25–34 anni, paid social, Spagna: +11,8% conversione relativa, `p < 0,05`.**

Il segmento può davvero contenere un effetto interessante.

Ma il p-value di quel confronto non porta con sé una nota automatica che dice:

> “prima di arrivare qui abbiamo avuto più di cento opportunità di trovare qualcosa di estremo”.

Questa informazione deve aggiungerla l'analista.

### Perché il rischio cresce

Supponiamo, per intuizione, che:

- tutti e 20 i null siano veri;
- i test siano indipendenti;
- ciascuno usi `α = 0,05`.

La probabilità di ottenere **almeno un falso positivo** è:

`1 - (1 - 0,05)^20 ≈ 64%`.

Questa non è una formula universale per qualsiasi analisi reale — i test possono essere correlati — ma rende visibile il principio:

> **quando aumentano le opportunità di vedere un risultato raro, vedere almeno un risultato raro diventa meno sorprendente.**

### Esplorazione e conferma hanno ruoli diversi

Nel Capitolo 4 abbiamo difeso l'EDA come strumento per generare ipotesi.

La stessa regola vale qui.

Se scopriamo a posteriori che un segmento sembra reagire molto bene, possiamo scrivere:

> **“Segnale esplorativo: il segmento X mostra un effetto maggiore; da verificare su nuovi dati o in un'analisi pianificata.”**

Non dobbiamo scrivere:

> “Abbiamo dimostrato che la variante funziona per X.”

La distinzione non riduce il valore della scoperta. Evita di confondere **generazione di ipotesi** con **evidenza confermativa**.

### La molteplicità non riguarda soltanto i segmenti

Possiamo creare molte opportunità di trovare un risultato favorevole cambiando:

- metrica primaria dopo aver visto i risultati;
- finestra temporale;
- criterio di esclusione;
- trasformazione del dato;
- modello statistico;
- soglia;
- subset della popolazione;
- momento in cui fermiamo l'analisi.

Anche se ogni singola scelta sembra difendibile, selezionare a posteriori la combinazione che produce il risultato più forte aumenta il rischio di overfitting analitico.

Per questo l'ASA include **trasparenza e reporting completo** tra i principi essenziali per interpretare correttamente i p-value.[^asa-multiple]

### Strategie di controllo

Non esiste una sola soluzione.

#### Pre-specificare ciò che conta

Definire prima:

- metrica primaria;
- confronti principali;
- segmenti confermativi;
- eventuali guardrail;
- criterio di analisi.

È spesso la misura più efficace contro il risultato “scelto dopo”.

#### Correggere la molteplicità quando serve

Metodi comuni includono:

- **Bonferroni:** semplice e spesso conservativo;
- **Holm:** controllo del family-wise error rate con maggiore flessibilità;
- **Benjamini–Hochberg:** controllo del False Discovery Rate, utile quando l'obiettivo è gestire molte potenziali scoperte.

La scelta dipende dal problema. Cercare un singolo claim altamente affidabile non è la stessa cosa che fare screening di centinaia di segnali per priorità successive.

#### Usare nuovi dati per confermare

Un pattern scoperto esplorativamente può essere validato su:

- periodo futuro;
- holdout non usato nella scoperta;
- nuovo esperimento;
- popolazione indipendente.

È uno dei modi più intuitivi per separare scoperta e conferma.

### Caso simulato/composito — Sessanta metriche e tre verdi

Un dashboard mostra 60 metriche di un confronto prodotto.

La metrica primaria non cambia in modo materialmente rilevante. Tre metriche secondarie mostrano `p < 0,05`.

Se scegliamo proprio quelle tre e ignoriamo le altre 57, creiamo un racconto molto più ottimista dell'insieme dell'evidenza.

La conclusione corretta non è necessariamente “sono tutti falsi positivi”.

È:

> **“Questi tre segnali sono emersi in una famiglia ampia di confronti; devono essere interpretati tenendo conto della molteplicità e, se importanti, confermati.”**

### La domanda che deve accompagnare ogni scoperta

Quando un risultato sembra sorprendente, chiedi:

> **Quante occasioni avevamo di essere sorpresi?**

Poi documenta:

```text
Ipotesi pre-specificata o esplorativa?
Numero/famiglia dei confronti:
Correzione applicata, se necessaria:
Scelte analitiche effettuate dopo aver visto i dati:
Nuovi dati disponibili per conferma:
```

> **La trasparenza sulla ricerca del segnale è parte dell'evidenza sul segnale.**

[^asa-multiple]: American Statistical Association, *Statement on Statistical Significance and P-Values*: https://www.amstat.org/asa/files/pdfs/p-valuestatement.pdf
