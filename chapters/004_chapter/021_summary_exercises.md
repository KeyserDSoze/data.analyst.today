## 4.20 Sintesi ed esercizi: descrivere prima di spiegare

L'Exploratory Data Analysis non è una fase decorativa. È il momento in cui impariamo come si comportano realmente i dati prima di imporre loro una spiegazione.

In questo capitolo abbiamo visto che:

- media e mediana raccontano aspetti diversi della distribuzione;
- la dispersione può essere più importante del valore medio;
- percentili e code descrivono problemi che le medie nascondono;
- istogrammi e box plot aiutano a vedere struttura, asimmetria e anomalie;
- correlazione non significa causalità;
- trend, stagionalità e mix possono creare associazioni ingannevoli;
- una percentuale senza denominatore è spesso una metrica incompleta;
- normalizzare può rendere confrontabili processi diversi, ma solo se il denominatore è coerente con la domanda;
- gli outlier non sono automaticamente errori;
- segmentare può trasformare una storia aggregata in una spiegazione molto diversa.

NIST descrive l'EDA come un insieme di tecniche, soprattutto grafiche, finalizzate a massimizzare la comprensione dei dati, scoprire strutture, individuare anomalie e verificare assunzioni.[^nist-eda]

### Esercizio 1 — Il tempo medio di risposta migliora

Un servizio clienti mostra:

- gennaio: tempo medio 9,2 minuti;
- febbraio: 8,7;
- marzo: 8,1;
- aprile: 7,6.

Il management conclude che il servizio sta migliorando.

Hai anche queste informazioni:

- mediana aprile: 4,1 minuti;
- P90 aprile: 19 minuti;
- P99 aprile: 84 minuti;
- quota ticket premium: dal 9% al 22%;
- i ticket premium ricevono priorità.

Costruisci un piano EDA che stabilisca se il miglioramento è generalizzato oppure dovuto al mix e alla priorità.

### Esercizio 2 — Lo store con più resi

Store A:

- 1.400 resi;
- 42.000 ordini;
- 78.000 unità vendute.

Store B:

- 950 resi;
- 19.000 ordini;
- 24.000 unità vendute.

Definisci almeno due return rate diversi. Spiega quale useresti per valutare esperienza cliente e quale per valutare qualità prodotto.

### Esercizio 3 — Il commerciale migliore

Tre account executive chiudono rispettivamente 31, 28 e 24 contratti.

Ricevono però 210, 90 e 55 opportunità qualificate e operano su segmenti con ACV medio di 8.000 €, 22.000 € e 70.000 €.

Costruisci almeno tre classifiche differenti e spiega quale decisione supporta ciascuna.

### Esercizio 4 — Outlier o informazione?

Una piattaforma di pagamenti registra normalmente transazioni tra 5 € e 4.000 €. Compaiono 17 transazioni superiori a 100.000 €.

Scrivi le verifiche che faresti prima di eliminarle. Considera almeno:

- identità cliente;
- valuta;
- duplicazioni;
- categoria merchant;
- migrazioni o cambi di sistema;
- possibile nuovo segmento enterprise.

### Esercizio 5 — Correlazione pericolosa

Un'azienda trova correlazione `r = 0,81` tra numero di demo commerciali settimanali e nuovo ARR.

Il CRO propone di imporre un target di demo +40%.

Elenca almeno cinque spiegazioni alternative alla causalità diretta e indica quali segmentazioni o analisi esplorative useresti.

### Esercizio finale — Scrivere una conclusione che resista alle domande

Immagina di aver trovato:

- revenue +14%;
- clienti +3%;
- AOV +10%;
- P50 AOV +1%;
- top 5% clienti +38%;
- return rate aggregato in calo;
- return rate del segmento che cresce maggiormente in aumento.

Scrivi una conclusione esecutiva di massimo 150 parole che distingua:

1. fatti osservati;
2. interpretazioni;
3. rischi o limiti;
4. decisioni suggerite;
5. analisi successive.

### Domande di autovalutazione

Prima di passare al capitolo successivo, dovresti riuscire a rispondere senza formule davanti:

- Quando preferiresti la mediana alla media?
- Cosa aggiunge una misura di dispersione?
- Perché P95 può essere più utile della media in un SLA?
- Quando un outlier non va rimosso?
- Qual è il rischio di confrontare conteggi con basi diverse?
- Qual è la differenza tra correlazione e causalità?
- Perché segmentare può invertire una conclusione aggregata?
- Qual è il numeratore e qual è il denominatore della metrica che stai usando?

Se queste domande diventano automatiche, l'EDA smette di essere una lista di grafici e diventa un modo di ragionare.

[^nist-eda]: NIST, “NIST/SEMATECH e-Handbook of Statistical Methods; Chapter 1: Exploratory Data Analysis”, https://www.nist.gov/publications/nistsematech-e-handbook-statistical-methods-chapter-1-exploratory-data-analysis
