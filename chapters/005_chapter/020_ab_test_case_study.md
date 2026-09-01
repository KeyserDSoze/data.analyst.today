## 5.19 Caso end-to-end — Quando un risultato “significativo” non basta

> **Caso simulato/composito.** Questo caso usa un confronto A/B perché rende concreti i concetti inferenziali del capitolo. Il disegno e la gestione operativa degli esperimenti — randomizzazione, SRM, contaminazione, durata, stopping, CUPED e rollout — saranno trattati nel Capitolo 9.

Una piattaforma e-commerce confronta una nuova pagina prodotto con la versione corrente per 14 giorni.

Risultati osservati:

| Metrica | Controllo | Variante |
|---|---:|---:|
| Utenti | 246.180 | 245.940 |
| Purchase conversion | 4,82% | 5,01% |
| AOV | 71,40 € | 70,95 € |
| Revenue per visitor | 3,44 € | 3,55 € |
| Return rate | 7,9% | 9,6% |

Sulla conversione:

- delta assoluto: **+0,19 punti percentuali**;
- delta relativo: circa **+3,9%**;
- p-value: **0,028**.

La prima lettura del team è:

> **“La variante vince.”**

Il compito dell'analista è trasformare questa frase in una valutazione completa dell'incertezza.

### Passo 1 — Qual era la domanda pre-specificata?

Prima del test il team aveva dichiarato come metrica primaria **revenue per visitor**, non conversion rate.

La conversione era una metrica diagnostica importante, ma il prodotto doveva aumentare il valore economico per visita.

Questa informazione cambia immediatamente il peso del `p = 0,028`.

Non perché la conversione sia improvvisamente falsa, ma perché selezionare dopo il test la metrica con il risultato più favorevole introduce molteplicità e modifica la domanda rispetto a quella pianificata.

### Passo 2 — Effect size prima dell'etichetta

`+0,19 pp` di conversione è il primo numero da comprendere.

Su una baseline del 4,82% equivale a circa +3,9% relativo.

La domanda successiva non è ancora “è significativo?”. È:

> **Quanto valore economico produrrebbe questo effetto se fosse persistente?**

La variante aumenta leggermente il numero di ordini ma riduce l'AOV e aumenta il return rate.

Per questo conversione e revenue lordo non bastano.

### Passo 3 — L'intervallo deve incontrare la soglia economica

Supponiamo che l'analisi della conversione produca una stima del tipo:

> `+0,19 pp`, CI 95% circa `+0,02 / +0,36 pp`.

Il range è compatibile con un miglioramento quasi nullo oppure con uno più interessante.

Il team stima che, dati costi e margini, serva almeno **+0,15 pp di conversione equivalente a parità di qualità economica** per giustificare il rollout.

L'intervallo attraversa quella soglia.

Quindi il risultato non è semplicemente:

> “positivo”.

È:

> **“La migliore stima supera la soglia, ma l'incertezza include anche scenari che non la raggiungono.”**

### Passo 4 — Il guardrail cambia l'economia

Il return rate passa da 7,9% a 9,6%.

Quando il team calcola il **revenue netto dopo i resi**, gran parte del beneficio apparente scompare.

Questo mostra perché una metrica localmente positiva non deve essere interpretata separatamente dal sistema economico.

Il p-value sulla conversione non incorpora il costo dell'aumento dei resi.

### Passo 5 — I segmenti scoperti dopo sono ipotesi, non verdetti

A posteriori il team esplora:

- desktop;
- mobile web;
- iOS;
- Android;
- nuovi utenti;
- returning;
- organic;
- paid search;
- paid social;
- direct.

Alcuni segmenti mostrano effetti molto positivi.

Il mobile sembra particolarmente promettente.

Ma questi confronti non erano definiti come claim confermativi prima dell'analisi.

La formulazione corretta è:

> **“Abbiamo trovato un possibile effetto eterogeneo su mobile; è un'ipotesi per il prossimo test.”**

Non:

> “La variante funziona sicuramente su mobile.”

### Passo 6 — L'orizzonte osservato fa parte dell'incertezza

Il risultato è particolarmente forte nei primi quattro giorni, che coincidono con una campagna premium.

Questo non è necessariamente un difetto statistico del test. È un problema di **generalizzazione temporale**:

> l'effetto medio dei 14 giorni rappresenta anche periodi futuri senza quella campagna?

La statistica inferenziale può essere precisa rispetto ai dati raccolti e il business può avere ancora incertezza sulla persistenza dell'effetto.

Questa distinzione è essenziale:

- **sampling uncertainty**;
- **external validity / stabilità nel tempo**;

non sono la stessa cosa.

### L'Uncertainty Brief del caso

| Campo | Sintesi |
|---|---|
| **Domanda** | La nuova pagina aumenta valore economico per visita abbastanza da meritare rollout? |
| **Popolazione osservata** | Utenti eleggibili nei 14 giorni del confronto. |
| **Metrica primaria** | Revenue per visitor. |
| **Segnale diagnostico** | Conversion +0,19 pp; `p = 0,028`. |
| **Precisione** | CI conversione include effetti piccoli e materialmente interessanti. |
| **Soglia business** | Circa +0,15 pp equivalente, subordinata a margine/return. |
| **Guardrail** | Return rate +1,7 pp: peggioramento rilevante. |
| **Molteplicità** | Segmenti mobile/channel esplorati a posteriori. |
| **Bias/incertezza non nel CI** | Possibile dipendenza dalla campagna premium e dalla finestra temporale. |
| **Conclusione** | Evidenza di aumento conversione, ma non evidenza sufficiente di aumento del valore netto. |
| **Prossimo passo** | Nuovo test pre-specificato su metrica economica netta e segmenti prioritari. |

Questa tabella contiene più valore decisionale di:

> `p = 0,028`.

### La decisione

Il team non lancia la variante in produzione su tutti gli utenti.

Decide di usare il risultato per progettare il confronto successivo con:

- metrica primaria economica netta;
- return rate come guardrail esplicito;
- segmenti di interesse pre-specificati;
- durata sufficiente a coprire condizioni commerciali normali.

Il Capitolo 9 spiegherà come farlo operativamente.

### Il punto del caso

L'inferenza non serve a produrre un'etichetta `WIN / LOSE`.

Serve a rispondere, nell'ordine:

1. **quanto è grande il segnale?**
2. **quanto è incerto?**
3. **rispetto a quale popolazione e disegno?**
4. **quali bias o fonti di instabilità non sono dentro l'intervallo?**
5. **quante opportunità avevamo di trovare un risultato interessante?**
6. **l'effetto supera una soglia che conta davvero?**

> **Un risultato statisticamente interessante diventa evidenza decisionale solo quando dimensione, incertezza e valore economico vengono letti insieme.**
