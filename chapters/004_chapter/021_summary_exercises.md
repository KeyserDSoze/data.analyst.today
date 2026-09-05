## 4.20 Sintesi ed esercizi: descrivere prima di spiegare

Il Capitolo 3 ci ha insegnato a non trattare un dataset come una rappresentazione già affidabile della realtà. Questo capitolo aggiunge una seconda disciplina: **anche quando il dato è pronto, il primo riepilogo non è ancora il fenomeno**.

Media, mediana, percentili, tassi, grafici e correlazioni sono tutti modi di comprimere una struttura molto più ricca. Il lavoro dell'EDA consiste nello scegliere compressioni utili e, soprattutto, nel controllare che non cancellino proprio l'informazione che potrebbe cambiare la decisione.

Per questo il percorso del capitolo non è stato una collezione di tecniche statistiche. Abbiamo iniziato dal centro e aggiunto dispersione, code e forma quando il centro non bastava. Abbiamo confrontato gruppi chiedendoci se il risultato dipendesse dalla composizione, osservato relazioni quantitative prima di ridurle a coefficienti, inserito il tempo quando calendario e trend potevano produrre pattern apparenti e usato sensitivity analysis per misurare quanto un insight dipendesse da punti, periodi o scelte di rappresentazione.

Il principio che tiene insieme tutto è semplice:

> **L'EDA restringe lo spazio delle spiegazioni plausibili. Non certifica automaticamente una spiegazione.**

NIST descrive l'EDA come un approccio orientato a massimizzare la comprensione dei dati, scoprire strutture, individuare anomalie e verificare assunzioni, con un ruolo centrale delle tecniche grafiche.[^nist-eda] Nel nostro workflow questa filosofia diventa un confine professionale tra **pattern**, **ipotesi** e **causa dimostrata**.

## Il deliverable del capitolo: EDA Evidence Map

La struttura operativa rimane deliberatamente compatta perché deve poter essere riutilizzata:

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

Quando questa mappa è completa, sappiamo anche quando l'EDA deve fermarsi. Se un'altra segmentazione non riduce più l'incertezza rilevante e la domanda successiva riguarda generalizzazione, precisione della stima o plausibilità statistica, il metodo deve cambiare. È il ponte verso il Capitolo 5: non chiederemo più soltanto **che cosa mostrano i dati osservati**, ma quanto possiamo fidarci della stima e quanto possiamo generalizzarla oltre quel campione.

---

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

1. Quando la mediana racconta meglio l'esperienza tipica rispetto alla media?
2. Che cosa aggiunge la dispersione a un valore centrale?
3. Perché P95 può essere più utile della media in un livello di servizio?
4. Perché un punto oltre `1,5 × IQR` non è automaticamente un errore?
5. Come distingui un denominatore aritmeticamente corretto da una popolazione realmente comparabile?
6. Perché bisogna guardare uno scatter plot prima di fidarsi di una correlazione?
7. Come può il mix invertire un confronto aggregato?
8. Che cosa deve contenere una sensitivity analysis?
9. Qual è la differenza tra **pattern**, **ipotesi** e **causa dimostrata**?
10. Qual è il prossimo metodo quando l'EDA non basta?

Se queste domande diventano automatiche, la statistica descrittiva smette di essere un inventario di formule e diventa una disciplina di **controllo dell'interpretazione**.

[^nist-eda]: NIST, *NIST/SEMATECH e-Handbook of Statistical Methods — Exploratory Data Analysis*. https://www.nist.gov/publications/nistsematech-e-handbook-statistical-methods-chapter-1-exploratory-data-analysis
