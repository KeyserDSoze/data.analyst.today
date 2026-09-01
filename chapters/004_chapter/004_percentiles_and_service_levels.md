## 4.3 Percentili e code: descrivere l'esperienza che la media non rappresenta

In molti processi operativi non ci interessa soltanto il comportamento centrale.

Ci interessa sapere **quanto è brutta la coda**.

È il caso di:

- tempi di risposta;
- latenza;
- consegne;
- attese;
- tempi di processo;
- importi di perdita;
- carichi di lavoro.

I **percentili** trasformano la distribuzione in soglie interpretabili.

Dire che il `P95` del tempo di risposta è 15 ore significa che circa il 95% delle osservazioni si trova a 15 ore o meno e circa il 5% sopra quella soglia.

### Caso simulato/composito — Il customer care sembra veloce

Un'azienda SaaS dichiara un tempo medio di prima risposta di **2 ore e 14 minuti**.

Il dato è plausibile, ma non ci dice che esperienza vive la coda dei clienti.

L'analista calcola:

```text
P50 = 47 minuti
P75 = 2h 05m
P90 = 7h 42m
P95 = 15h 18m
P99 = 41h
```

La storia cambia.

La maggioranza riceve una risposta rapidamente, ma una piccola quota attende molto più a lungo.

Segmentando il P95 per piano e giorno della settimana, il problema si concentra nel piano Basic durante il weekend.

L'EDA non ha soltanto scoperto "una coda lunga". Ha trasformato un problema medio in una popolazione operativa identificabile.

### Percentile e soglia di servizio non sono la stessa cosa

Possiamo descrivere un servizio in almeno due modi:

**Percentile:**

> P95 = 4,8 ore.

**Quota entro una soglia:**

> 92% dei ticket riceve risposta entro 4 ore.

Sono viste complementari.

La prima chiede:

> sotto quale valore cade il 95% dei casi?

La seconda chiede:

> quale quota dei casi rispetta una soglia già definita?

Nei processi con SLA la seconda può essere direttamente collegata al contratto; la prima aiuta a capire la forma della coda.

### P99 non è automaticamente "più rigoroso"

Scegliere un percentile più estremo non rende sempre migliore la metrica.

Il P99 può essere molto importante per servizi digitali ad alto volume, dove l'1% rappresenta milioni di richieste. Su un processo con 120 casi al mese, invece, il P99 può dipendere da una o due osservazioni e risultare molto instabile.

Quindi dobbiamo sempre mostrare anche la dimensione della popolazione.

### Le code possono avere proprietari diversi

Se il P95 complessivo è alto, chiediamoci:

- riguarda tutti i segmenti o uno solo?
- si concentra in particolari ore o giorni?
- è associato a una tipologia di richiesta?
- emerge soltanto oltre una certa soglia di volume?
- la mediana è stabile mentre la coda peggiora?

Queste domande sono spesso più utili della ricerca di una singola "media migliore".

### Evitare il percentile opportunistico

Un errore comunicativo consiste nel scegliere dopo aver visto i dati il percentile che produce la storia desiderata.

Se il P90 è migliorato ma il P99 è peggiorato, non dobbiamo decidere quale dei due mostrare in base alla convenienza narrativa.

Dobbiamo chiedere quale parte della distribuzione conta per la decisione.

### Tabella minima per una metrica di servizio

| Elemento | Esempio |
|---|---|
| Popolazione | ticket validi ricevuti nel mese |
| P50 | 47 min |
| P90 | 7h 42m |
| P95 | 15h 18m |
| Soglia SLA | 4h |
| % entro SLA | 81% |
| Volume | 28.420 ticket |

Questa struttura evita che una singola statistica nasconda la dimensione e la forma dell'esperienza.

> **Quando il costo del problema vive nella coda, la media è spesso il posto sbagliato in cui guardare.**