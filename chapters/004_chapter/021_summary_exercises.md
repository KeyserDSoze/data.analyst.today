## 4.20 Sintesi ed esercizi: descrivere prima di spiegare

L'Exploratory Data Analysis non è una fase decorativa e non è una gara a chi produce più grafici.

È il lavoro con cui trasformiamo un dataset già sufficientemente affidabile in una **mappa della struttura osservata**:

- dove si trova il centro;
- quanto varia il fenomeno;
- come sono fatte le code;
- quali gruppi differiscono;
- quanto il risultato dipende dal mix;
- quali relazioni appaiono nei dati;
- quali osservazioni o periodi guidano il pattern;
- quanto la conclusione resiste a letture alternative.

NIST descrive l'EDA come un approccio orientato a massimizzare la comprensione dei dati, scoprire strutture, individuare anomalie e verificare assunzioni, con un ruolo centrale delle tecniche grafiche.[^nist-eda]

Il principio che vogliamo portarci dietro è però ancora più operativo:

> **L'EDA restringe lo spazio delle spiegazioni plausibili. Non certifica automaticamente una spiegazione.**

### Il deliverable del capitolo: EDA Evidence Map

Alla fine di un'esplorazione seria dovremmo poter produrre una sintesi simile:

```text
DOMANDA
Che cosa stiamo cercando di capire?

OSSERVATO
Quali pattern sono direttamente visibili nei dati?

CONCENTRAZIONE / MIX
In quali segmenti, code, periodi o categorie si concentra il fenomeno?

ROBUSTEZZA
La conclusione cambia con mediana vs media, diversa baseline,
esclusione di punti influenti o segmentazione?

IPOTESI
Quali spiegazioni sono diventate plausibili?

NON DIMOSTRATO
Quali interpretazioni non possiamo ancora sostenere?

PROSSIMO METODO
Serve altra descrizione, inferenza, coorti, causalità,
esperimento, forecasting o modellazione?
```

Questo è il ponte verso il resto del libro. L'EDA non termina necessariamente con una decisione: spesso termina dicendoci **quale domanda vale la pena studiare con un metodo più forte**.

### Dieci abitudini da rendere automatiche

Prima di chiudere un'EDA, verifica di aver considerato almeno:

1. **media e mediana**, quando entrambe aggiungono informazione;
2. **dispersione e quantili**, non soltanto un valore centrale;
3. **forma della distribuzione**, soprattutto asimmetria e multimodalità;
4. **dimensione dei gruppi**, insieme alle percentuali;
5. **numeratore e denominatore** delle metriche;
6. **mix e popolazione di riferimento** nei confronti;
7. **tempo e baseline** quando i dati hanno struttura temporale;
8. **osservazioni influenti**, con sensitivity analysis quando necessario;
9. **grafico prima del coefficiente** nelle relazioni quantitative;
10. **linguaggio non causale** finché la causalità non è stata identificata.

### Esercizio 1 — Il tempo medio di risposta migliora

Un servizio clienti mostra:

- gennaio: media 9,2 minuti;
- febbraio: 8,7;
- marzo: 8,1;
- aprile: 7,6.

Il management conclude che il servizio sta migliorando.

Sai inoltre che ad aprile:

- mediana: 4,1 minuti;
- P90: 19 minuti;
- P99: 84 minuti;
- quota ticket premium: dal 9% al 22%;
- i ticket premium ricevono priorità.

Costruisci una **EDA Evidence Map**. Specifica quali distribuzioni e segmentazioni useresti per capire se il miglioramento è generalizzato oppure prodotto dal mix dei ticket.

Non cercare ancora una causa definitiva.

### Esercizio 2 — Due return rate, due domande

Store A:

- 1.400 ordini con almeno un reso;
- 42.000 ordini consegnati;
- 78.000 unità vendute;
- 2.100 unità restituite.

Store B:

- 950 ordini con almeno un reso;
- 19.000 ordini consegnati;
- 24.000 unità vendute;
- 1.250 unità restituite.

Calcola almeno:

- order return rate;
- unit return rate.

Spiega quale useresti per parlare di esperienza a livello ordine e quale per indagare qualità o compatibilità dei prodotti. Poi indica quale informazione manca ancora per confrontare correttamente i due store.

### Esercizio 3 — Il commerciale “migliore”

Tre account executive chiudono rispettivamente 31, 28 e 24 contratti.

Ricevono 210, 90 e 55 opportunità qualificate e operano su segmenti con ACV medio di 8.000 €, 22.000 € e 70.000 €.

Costruisci almeno tre classifiche:

- volume;
- win rate;
- valore economico approssimativo.

Poi rispondi:

> Quale delle tre classifiche misura davvero “bravura commerciale”?

La risposta corretta può essere: **nessuna, senza conoscere come vengono assegnate e qualificate le opportunità**. Spiega perché.

### Esercizio 4 — L'osservazione influente

Un'azienda trova correlazione `r = 0,74` tra advertising settimanale e nuovi ordini.

Nel grafico quattro settimane promozionali sono molto distanti dal resto. Senza quelle quattro settimane `r` scende a `0,29`.

Costruisci una breve analisi che distingua:

- dato valido vs dato influente;
- risultato completo vs sensitivity analysis;
- associazione osservata vs spiegazione causale.

Che cosa comunicheresti al marketing team?

### Esercizio 5 — Simpson's paradox operativo

Due canali di acquisizione hanno conversion rate aggregati:

- canale A: 14%;
- canale B: 11%.

Dopo aver segmentato tra desktop e mobile, B converte meglio di A su entrambi i device.

Costruisci una possibile tabella di volumi che renda questo risultato matematicamente plausibile. Poi spiega in parole semplici come il mix dei device produce l'inversione.

### Esercizio 6 — La crescita è ampia o concentrata?

Un marketplace riporta:

- revenue +14%;
- clienti +3%;
- AOV +10%;
- P50 AOV +1%;
- P90 AOV +24%;
- top 5% clienti +38%;
- una categoria produce il 52% della crescita assoluta.

Scrivi almeno cinque osservazioni che appartengono all'EDA e tre spiegazioni che **non** puoi ancora dichiarare dimostrate.

### Caso finale — Una conclusione che deve resistere alle domande

Immagina di aver completato un'EDA e di avere queste evidenze:

- ordini +11%;
- acquirenti unici +4%;
- revenue +15%;
- mediana ordine +2%;
- P90 ordine +21%;
- il 48% della crescita viene da una nuova categoria;
- il tasso di reclami aggregato è stabile;
- nella nuova categoria il tasso è quasi doppio;
- escludendo cinque giornate promozionali la revenue resta +9%.

Produci tre output:

1. una **EDA Evidence Map** completa;
2. una conclusione esecutiva di massimo 150 parole;
3. una lista delle tre analisi successive con il metodo che useresti.

La qualità dell'esercizio non dipende dal trovare la storia più interessante. Dipende dal non dire più di ciò che l'evidenza consente.

### Domande di autovalutazione

Prima di passare al Capitolo 5 dovresti riuscire a rispondere senza formule davanti:

- Quando la mediana racconta meglio l'esperienza tipica rispetto alla media?
- Che cosa aggiunge la dispersione a un valore centrale?
- Perché P95 può essere più utile della media in un livello di servizio?
- Perché un punto oltre `1,5 × IQR` non è automaticamente un errore?
- Come distingui un denominatore aritmeticamente corretto da una popolazione realmente comparabile?
- Perché bisogna guardare uno scatter plot prima di fidarsi di una correlazione?
- Come può il mix invertire un confronto aggregato?
- Che cosa deve contenere una sensitivity analysis?
- Qual è la differenza tra **pattern**, **ipotesi** e **causa dimostrata**?
- Qual è il prossimo metodo quando l'EDA non basta?

Se queste domande diventano automatiche, l'EDA smette di essere una lista di statistiche e diventa una disciplina di **controllo dell'interpretazione**.

[^nist-eda]: NIST, *NIST/SEMATECH e-Handbook of Statistical Methods — Exploratory Data Analysis*: https://www.nist.gov/publications/nistsematech-e-handbook-statistical-methods-chapter-1-exploratory-data-analysis
