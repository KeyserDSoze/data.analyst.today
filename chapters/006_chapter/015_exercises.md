## 6.14 Esercizi: costruire diagnosi di lifecycle, non soltanto KPI

Questi esercizi restano volutamente strutturati: sono il laboratorio operativo del capitolo. L'obiettivo non è soltanto calcolare una percentuale, ma allenare la distinzione fra **presenza, valore, tempo, rischio, actionability e causalità**.

Per ogni caso separa sempre tre livelli: ciò che i dati mostrano direttamente, l'interpretazione che consideri plausibile e ciò che richiede altra evidenza prima di diventare una conclusione.

### Esercizio 1 — Activation ambigua

Una piattaforma di videoconferenza considera “attivato” qualsiasi utente che abbia creato un account e avviato almeno una call.

I dati mostrano:

- signup mensili: 80.000;
- utenti con almeno una call: 62.000;
- utenti con almeno una call con partecipante esterno: 41.000;
- utenti con almeno tre call in sette giorni: 19.000;
- retention D60 tra chi ha fatto una sola call: 18%;
- retention D60 tra chi ha fatto almeno tre call: 57%.

Domande:

1. Quali eventi considereresti candidati di activation e perché?
2. Quale evento sembra più vicino al valore del prodotto?
3. Quali segmentazioni controlleresti prima di adottarlo come metrica?
4. Perché la forte correlazione con retention non dimostra che forzare tre call aumenterà causalmente la retention?
5. Come misureresti il time-to-value?

### Esercizio 2 — Funnel che migliora, economics che peggiora

Un e-commerce modifica il checkout. Dopo il redesign:

- add-to-cart → checkout: 54% → 61%;
- checkout → pagamento: 71% → 76%;
- conversion rate complessivo: +9%;
- average order value: -13%;
- return rate: 8% → 12%;
- contribution margin per visitatore: -3%.

Prepara una nota al Product Manager di massimo 120 parole che distingua miglioramento locale del funnel, effetto economico complessivo ed evidenza mancante prima di dichiarare il redesign “vincente”.

### Esercizio 3 — Due coorti, stessa D30

Due coorti hanno entrambe retention D30 del 52%.

| Giorno | Coorte A | Coorte B |
| --- | ---: | ---: |
| D1 | 86% | 63% |
| D7 | 68% | 56% |
| D14 | 58% | 54% |
| D30 | 52% | 52% |

Domande:

1. Come descriveresti la forma delle due curve?
2. In quale coorte il problema sembra concentrato nell'activation iniziale?
3. In quale potrebbe esserci un decadimento più progressivo?
4. Quali eventi di prodotto sovrapporresti alla timeline?
5. Perché il solo D30 elimina informazione importante?

### Esercizio 4 — Logo churn stabile, revenue a rischio

Una società SaaS inizia il trimestre con 1.000 clienti e 10 milioni di euro di ARR.

Nel trimestre:

- 40 clienti cancellano completamente, per 620.000 € di ARR;
- 85 clienti riducono il contratto, per 410.000 € di contraction;
- 30 clienti espandono il contratto, per 540.000 € di expansion.

Calcola o descrivi logo churn, Gross Revenue Retention e Net Revenue Retention, poi spiega perché i tre indicatori raccontano storie differenti. Indica quale useresti per una riunione Customer Success e quale per valutare la salute economica della base.

### Esercizio 5 — Churn involontario

Un servizio subscription registra 2.400 cancellazioni nel mese.

L'indagine mostra:

- 1.650 cancellazioni volontarie;
- 520 pagamenti falliti mai recuperati;
- 230 account chiusi per altri motivi amministrativi.

Il CRM team propone uno sconto del 20% a tutti i clienti persi. Spiega perché l'intervento è mal disegnato. Costruisci almeno tre segmenti di uscita e associa a ciascuno un possibile tipo di intervento.

### Esercizio 6 — Reactivation o semplice apertura?

Una campagna contatta 100.000 utenti inattivi.

Dopo trenta giorni:

- 15.000 riaprono l'app;
- 8.000 compiono almeno un evento core;
- 4.200 ripetono l'evento core tre volte;
- 2.600 risultano ancora attivi dopo sessanta giorni.

In una popolazione comparabile non contattata, il 6% torna spontaneamente nell'app.

Domande:

1. Quale reactivation rate presenteresti?
2. Come distingueresti ritorno e durable reactivation?
3. Perché non puoi attribuire tutti i 15.000 ritorni alla campagna?
4. Quale esperimento progetteresti per misurare il lift incrementale?

### Esercizio 7 — LTV osservato o previsto?

Tre coorti hanno questi dati:

| Coorte | Età | CAC | Contribution margin cumulato |
| --- | ---: | ---: | ---: |
| Gennaio | 12 mesi | 75 € | 164 € |
| Giugno | 7 mesi | 68 € | 121 € |
| Novembre | 2 mesi | 54 € | 61 € |

Un manager conclude che novembre è la coorte migliore perché ha già quasi recuperato il CAC. Quali controlli faresti prima di accettare la conclusione? Distingui valore osservato, payback e LTV futuro previsto.

### Esercizio 8 — Il churn model trova clienti impossibili da salvare

Un modello assegna score di rischio elevatissimi a clienti che hanno già comunicato la disdetta. Il Customer Success può contattare soltanto 200 account.

Progetta una tabella di prioritizzazione con almeno queste colonne:

- risk score;
- ARR a rischio;
- giorni al rinnovo;
- motivo/problema osservato;
- actionability;
- stato della disdetta.

Spiega perché il ranking finale può essere molto diverso dal ranking del modello.

### Esercizio finale — Il board vuole sapere perché la retention è scesa

Sei Data Analyst di una subscription company. La retention M6 è scesa dal 67% al 59%.

Sai che:

- il calo è concentrato in due coorti recenti;
- entrambe provengono soprattutto da un nuovo canale di acquisition;
- il time-to-value è passato da 2,8 a 6,4 giorni;
- il pricing è aumentato nello stesso periodo;
- il tracking di una parte dell'onboarding è cambiato;
- i clienti con TTV sotto tre giorni mostrano retention molto più alta;
- non esiste ancora evidenza causale sull'onboarding o sul pricing.

Costruisci una **Lifecycle Diagnostic Map**:

| Campo | La tua risposta |
| --- | --- |
| KPI iniziale |  |
| Chi |  |
| Quando |  |
| Dove |  |
| Activation/TTV |  |
| Persistenza |  |
| Valore economico da verificare |  |
| Cosa sappiamo |  |
| Cosa è plausibile |  |
| Cosa non è dimostrato |  |
| Problema di data quality/tracking |  |
| Prossimo metodo |  |

Chiudi con una risposta al board di massimo 180 parole. La qualità della risposta non dipende dal “trovare una causa” a tutti i costi, ma dal mostrare quanto il problema sia stato ristretto e quale evidenza serva per restringerlo ancora.

## Dal lifecycle al tempo come processo

Il capitolo ha trasformato una base clienti in una traiettoria: ingresso, activation, persistenza, rischio, uscita, ritorno e valore. Nel prossimo capitolo il tempo smetterà di essere soltanto l'età del cliente e diventerà una proprietà del processo stesso.

Vendite, domanda, ticket, ordini e capacità operativa hanno memoria, calendario, stagionalità e cambi di regime. Il **Capitolo 7** userà queste strutture per distinguere una normale oscillazione temporale da un'anomalia e una descrizione del passato da un forecast credibile.

> **Nel lifecycle abbiamo chiesto come cambia una relazione mentre invecchia. Nelle serie temporali chiederemo come cambia il processo mentre scorre il calendario.**