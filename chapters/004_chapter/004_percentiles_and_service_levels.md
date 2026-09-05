## 4.3 Percentili e code: quando il costo del problema vive lontano dalla media

In molti processi operativi la domanda più importante non è quale esperienza viva il caso centrale, ma **quanto peggiora l'esperienza per la parte più sfortunata della popolazione**. Tempi di risposta, latenza, consegne, attese, perdite e carichi di lavoro hanno spesso code che una media comprime troppo aggressivamente.

I **percentili** rendono quella coda leggibile. Dire che il `P95` del tempo di risposta è 15 ore significa che circa il 95% delle osservazioni si trova a 15 ore o meno e il restante 5% supera quella soglia. Non stiamo descrivendo un caso “tipico”: stiamo collocando un confine nella distribuzione.

Consideriamo un'azienda SaaS che dichiara un tempo medio di prima risposta di **2 ore e 14 minuti**. La cifra sembra rassicurante finché non osserviamo la distribuzione:

```text
P50 = 47 minuti
P75 = 2h 05m
P90 = 7h 42m
P95 = 15h 18m
P99 = 41h
```

La maggioranza dei clienti riceve risposta rapidamente, ma una quota relativamente piccola aspetta molto più a lungo. Quando l'analista scompone il `P95` per piano e giorno della settimana, la coda si concentra nel piano Basic durante il weekend. L'EDA ha così trasformato una generica “coda lunga” in una popolazione operativa precisa su cui indagare capacità, prioritizzazione o processo.

## Percentile e soglia di servizio rispondono a domande diverse

Un servizio può essere descritto dicendo `P95 = 4,8 ore` oppure `92% dei ticket entro 4 ore`. Le due statistiche sono complementari, non intercambiabili. La prima chiede sotto quale valore cade una quota definita della popolazione; la seconda parte da una soglia già importante per il business e chiede quale quota la rispetti.

Quando esiste uno SLA, la percentuale entro soglia può essere direttamente collegata a un impegno operativo o contrattuale. Il percentile aiuta invece a vedere quanto lontano si spinge la coda e se essa sta cambiando anche quando lo SLA aggregato resta stabile.

Per questo una metrica di servizio è spesso più leggibile quando tiene insieme posizione, coda, soglia e volume:

| Elemento | Esempio |
|---|---|
| Popolazione | ticket validi ricevuti nel mese |
| P50 | 47 min |
| P90 | 7h 42m |
| P95 | 15h 18m |
| Soglia SLA | 4h |
| % entro SLA | 81% |
| Volume | 28.420 ticket |

La numerosità è essenziale soprattutto quando ci spingiamo verso percentili estremi. `P99` non significa automaticamente “più rigoroso” di `P95`. Su milioni di richieste l'1% può rappresentare una popolazione enorme e operativamente rilevante; su 120 casi al mese il P99 può dipendere da una o due osservazioni e oscillare violentemente.

## La coda va attribuita a una popolazione, non soltanto misurata

Quando un percentile peggiora, la prossima domanda non è quale altro percentile calcolare. È capire **chi compone quella coda e in quali condizioni vi entra**. Può concentrarsi in particolari segmenti, ore, giorni, tipi di richiesta, livelli di carico o regioni. La mediana può rimanere stabile mentre il P95 peggiora, indicando che il processo centrale non è cambiato ma una minoranza sta vivendo un deterioramento sostanziale.

Questa attenzione protegge anche da un uso opportunistico dei percentili. Se il P90 migliora e il P99 peggiora, non dovremmo scegliere dopo aver visto i dati quale mostrare in base alla storia che preferiamo. Dobbiamo tornare alla decisione: **quale parte della distribuzione produce un costo abbastanza importante da meritare attenzione?**

La risposta ci porta naturalmente alla forma complessiva della distribuzione. I percentili ne descrivono alcuni punti; un istogramma può mostrarci come quei punti sono collegati tra loro.

> **Quando il costo del problema vive nella coda, la media è spesso il posto sbagliato in cui guardare.**
