## 8.15 Caso studio completo: quale intervento riduce davvero il churn?

Una società SaaS B2B da 42 milioni di euro di ARR osserva un aumento del churn annualizzato dal 9,6% all'11,8%.

Il management vuole investire 1,2 milioni di euro in Customer Success e chiede al team analytics:

> **Quale intervento riduce davvero il churn e su quali clienti dobbiamo concentrarlo?**

Il team parte da quattro azioni già in uso:

1. chiamata proattiva del Customer Success;
2. sessione di training aggiuntiva;
3. sconto temporaneo del 15%;
4. revisione tecnica dell'integrazione.

### Primo errore: guardare i risultati osservati

Dai dati storici emerge:

| Intervento | Churn a 90 giorni |
|---|---:|
| nessun intervento | 8,1% |
| chiamata CS | 19,4% |
| training | 14,8% |
| sconto | 22,1% |
| revisione tecnica | 17,3% |

Se prendessimo questi numeri alla lettera, concluderemmo che tutti gli interventi peggiorano il churn.

È chiaramente plausibile un problema di **confounding by indication**: gli interventi vengono assegnati proprio ai clienti già a rischio.

### Ricostruire il processo decisionale

Il team intervista Customer Success e scopre che:

- la chiamata viene fatta soprattutto quando l'health score scende sotto 65;
- lo sconto è proposto ai clienti che hanno già espresso intenzione di cancellare;
- la revisione tecnica viene attivata quando esistono errori di integrazione;
- il training viene offerto più spesso ai clienti con bassa adoption ma relazione commerciale ancora buona.

Il dataset quindi incorpora il comportamento degli operatori.

### Disegno 1: soglia quasi-sperimentale

Per la chiamata CS esiste una regola abbastanza rigida: health score < 65.

Il team usa una regression discontinuity locale confrontando clienti con score 62-64 e 65-67.

Risultato:

- churn senza chiamata vicino alla soglia: 16,2%;
- churn con chiamata vicino alla soglia: 12,7%;
- effetto locale stimato: **-3,5 punti percentuali**.

La chiamata sembra utile almeno vicino alla soglia.

### Disegno 2: matching per il training

Il training non segue una soglia. Il team costruisce un propensity score usando caratteristiche pre-treatment:

- ARR;
- industry;
- numero di utenti;
- activation iniziale;
- tenure;
- health score precedente;
- numero ticket nei 60 giorni precedenti;
- adozione delle feature core.

Dopo matching e verifica del common support:

- churn trattati: 14,8%;
- churn controlli comparabili: 17,1%;
- differenza stimata: **-2,3 punti**.

Risultato promettente, ma meno robusto di un esperimento perché dipende dall'assenza di confondenti non osservati rilevanti.

### Disegno 3: lo sconto

Per lo sconto emerge un problema più grave.

La decisione dipende spesso da conversazioni qualitative non registrate nel CRM: intenzione di cancellare, pressione sul budget, relazione con il procurement.

Il matching non può catturare queste informazioni.

Il team decide quindi di non presentare un effetto causale dello sconto dai dati storici.

Propone invece un esperimento controllato su clienti eleggibili e realmente contendibili.

Questa è una conclusione analitica valida: **non sempre il dato esistente permette una risposta causale credibile**.

### Disegno 4: revisione tecnica

La revisione tecnica sembra particolarmente utile per clienti con integrazioni complesse.

L'effetto medio stimato con un pilot randomizzato è:

- controllo: churn 18,0%;
- trattamento: churn 14,9%;
- differenza: -3,1 pp.

Ma l'effetto eterogeneo mostra:

| Segmento | Effetto stimato |
|---|---:|
| integrazione semplice | -0,6 pp |
| integrazione media | -2,7 pp |
| integrazione complessa | -7,9 pp |

L'effetto medio nasconde quindi un segmento ad altissimo valore.

### Dalla causalità alla decisione

Il team costruisce una matrice operativa:

| Intervento | Evidenza causale | Effetto stimato | Costo medio | Target consigliato |
|---|---|---:|---:|---|
| chiamata CS | RDD locale | -3,5 pp | €45 | health score vicino a 65 |
| training | matching | -2,3 pp | €120 | bassa adoption, buon fit |
| sconto | insufficiente | non stimabile | €600+ | da testare |
| revisione tecnica | RCT pilot | -7,9 pp nel segmento complesso | €280 | integrazioni complesse |

La raccomandazione non è più "aumentiamo il Customer Success".

Diventa:

1. automatizzare l'identificazione dei clienti appena sotto la soglia health score;
2. dare priorità alle revisioni tecniche nei clienti ad alta complessità;
3. usare training solo sui segmenti con evidenza plausibile;
4. sperimentare gli sconti invece di dedurne l'effetto dai dati storici;
5. misurare incremental churn saved e valore economico netto.

### Il risultato economico

Il piano precedente prevedeva 1,2 milioni distribuiti uniformemente sui clienti ad alto rischio.

Il nuovo piano concentra circa 760.000 euro sugli interventi e segmenti con maggiore effetto atteso, riservando 140.000 euro alla sperimentazione e lasciando il resto come capacità adattiva.

La previsione interna passa da circa 720 churn evitati a **1.050 churn evitati equivalenti**, con forte incertezza dichiarata sui segmenti non ancora sperimentati.

Il numero non viene presentato come certezza. Viene accompagnato da intervalli e da una roadmap di validazione.

### Cosa rende questo un buon lavoro analitico

Il valore non è stato scegliere una tecnica sofisticata.

Il valore è stato:

- riconoscere il bias di selezione;
- ricostruire il processo operativo che genera il trattamento;
- scegliere un metodo diverso per ogni intervento;
- dichiarare dove l'identificazione causale non era credibile;
- tradurre gli effetti in priorità operative ed economiche.

### Regola finale

> **La causalità non serve a produrre un coefficiente più elegante. Serve a evitare di investire denaro su interventi che sembrano efficaci solo perché sono stati applicati a persone diverse.**
