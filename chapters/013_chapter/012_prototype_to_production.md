## 13.11 Dal prototipo alla produzione: cambiare tool quando cambia la responsabilità

Un prototipo e un sistema di produzione possono usare lo stesso linguaggio e avere obblighi completamente diversi. Il prototipo deve rispondere soprattutto a una domanda: **questa idea merita di essere usata?** La produzione deve rispondere anche a un'altra: **possiamo continuare a fidarci del processo quando aumentano volume, utenti, frequenza, errori e dipendenze?**

Per questo il passaggio a produzione non è un semplice deploy. È una **nuova decisione di design**.

Un analyst costruisce un notebook per suggerire condizioni commerciali a **120 clienti enterprise**. Legge tre estratti, applica regole, calcola scenari e produce un workbook per Sales. Per due trimestri funziona bene. Poi il business decide di usarlo per **18.000 clienti in 14 paesi**, con esecuzione notturna, caricamento automatico nel CRM e audit delle raccomandazioni.

Il metodo può essere rimasto identico. Sono cambiate invece scala, frequenza, consumer, rischio, accesso ai dati, recovery e ownership. Il notebook non è diventato “cattivo”: ha **superato l'exit condition del prototipo**.

### Il promotion gate nasce dai nuovi obblighi

Una progressione utile è:

| Livello | Responsabilità |
|---|---|
| P0 — scratch | lavoro personale, nessun consumer |
| P1 — validated prototype | metodo e baseline verificati, valore da dimostrare |
| P2 — recurring analytical process | riesecuzione, version control, test e owner |
| P3 — production analytical product | scheduling, monitoring, access control, recovery e change management |

Non tutti i progetti devono arrivare a P3. Molti non dovrebbero farlo.

Il passaggio di livello viene giustificato da segnali concreti: l'analisi passa da ad hoc a settimanale o continua; nuovi processi dipendono dall'output; crescono righe, paesi, utenti o runtime; aumentano privacy e rischio economico; la stessa logica viene riusata da più consumer. Questi sono **promotion trigger**, non prove che serva automaticamente una piattaforma più sofisticata.

### Il costo della premature productionization

Un team può costruire streaming, feature store, microservizi, orchestration, CI/CD e monitoring completo prima di sapere se un recommendation system crea valore. Dopo quattro mesi scopre che una semplice regola recency-frequency produce quasi lo stesso risultato economico.

La tecnologia può essere impeccabile e il processo di apprendimento inefficiente. Una sequenza più sana è spesso:

```text
problema
→ soluzione minima verificabile
→ evidenza di valore
→ failure modes reali
→ industrializzazione proporzionata
```

Questo non significa ignorare rischi gravi durante il prototipo. Significa non comprare obblighi di produzione che non servono ancora all'esperimento che stiamo facendo.

### Migrare senza cambiare silenziosamente il prodotto

Quando un prototipo viene riscritto, la nuova pipeline deve preservare — quando devono restare invariati — popolazione, grain, date, identity logic, filtri, metriche, missing handling e fallback. Una pipeline può diventare più robusta e contemporaneamente implementare un concetto diverso, per esempio sostituendo inconsapevolmente `revenue netto dopo refund` con `gross_amount`.

L'Analytical Data Contract del Capitolo 11 diventa quindi anche uno strumento di migrazione. Per processi importanti può essere utile uno **shadow run**:

```text
old output
vs
new output
```

Le differenze non devono essere necessariamente zero, perché una migrazione può correggere bug o cambiare regole deliberate. Devono però essere **attese, spiegate e approvate**.

Nel Tooling Decision Record registriamo il maturity level attuale, consumer, frequenza, rischio, promotion trigger, requisiti mancanti per il livello successivo, parity plan, nuovo owner e rollback.

> **Non chiedere “possiamo mettere in produzione questo notebook?”. Chiedi quali nuovi obblighi sono comparsi perché il lavoro è diventato importante, ricorrente o operativo. Lo strumento deve cambiare solo quanto serve per soddisfarli.**
