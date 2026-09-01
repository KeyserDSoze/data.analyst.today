## 3.13 Riconciliazione: spiegare la differenza prima di scegliere il numero

Una delle situazioni più comuni nel lavoro reale è questa:

> due sistemi mostrano valori diversi per una metrica che porta lo stesso nome.

La reazione sbagliata è decidere immediatamente quale dashboard "ha ragione".

La domanda corretta è:

> **Quali regole fanno sì che i due sistemi producano numeri diversi?**

La **riconciliazione** serve a costruire quella spiegazione.

### Caso simulato/composito — Il fatturato che non coincide

Una società retail riceve due report mensili:

```text
ERP / Finance:        €1.842.310
Dashboard Sales:      €1.917.480
Differenza:              €75.170
```

Circa il **4,1%**.

L'analista confronta prima le definizioni, non il codice.

Emergono differenze precise:

- Finance riconosce il ricavo alla data di spedizione;
- Sales lo attribuisce alla data dell'ordine;
- Finance esclude ordini annullati prima della spedizione;
- Sales li rimuove quando riceve l'aggiornamento di stato;
- Sales include un contributo di spedizione che Finance classifica separatamente;
- alcune note di credito del mese precedente vengono registrate contabilmente nel mese corrente.

I due numeri non sono semplicemente due implementazioni concorrenti della stessa metrica.

Rappresentano **due viste differenti del fenomeno**.

### La reconciliation bridge

Un modo efficace di lavorare è partire da un totale e costruire un ponte verso l'altro.

| Voce | Impatto |
|---|---:|
| Totale Sales | €1.917.480 |
| Ordini non ancora spediti | -€31.800 |
| Contributi di spedizione | -€19.420 |
| Cancellazioni non ancora recepite | -€8.650 |
| Note di credito / resi | -€15.300 |
| Totale Finance | €1.842.310 |

La tabella trasforma una discussione generica — "i dati non tornano" — in un insieme di differenze verificabili.

Nella pratica le componenti possono interagire e il ponte deve essere costruito record per record o con regole più precise. Il principio resta lo stesso: **spiegare il delta**.

### Otto livelli da controllare

Quando due numeri non coincidono, procedi in quest'ordine:

1. **Definizione** — le metriche significano davvero la stessa cosa?
2. **Popolazione** — includono gli stessi record?
3. **Tempo** — usano lo stesso timestamp e la stessa finestra?
4. **Grain** — aggregano allo stesso livello?
5. **Stati** — cancellazioni, resi e rettifiche sono trattati allo stesso modo?
6. **Unità** — valuta, tasse, scala e unità di misura coincidono?
7. **Freshness** — i sistemi fotografano lo stesso momento?
8. **Trasformazioni** — filtri, join o mapping modificano la popolazione?

Questo ordine evita di passare ore su una query quando la differenza nasce da una definizione.

### Riconciliare non significa obbligare i sistemi a coincidere

A volte il risultato corretto della riconciliazione è mantenere **due metriche diverse**, purché siano nominate e usate correttamente.

Per esempio:

- `ordered_revenue` per il monitoraggio commerciale;
- `recognized_revenue` per la contabilità.

Forzare un'unica definizione può peggiorare entrambi gli usi.

L'obiettivo non è l'uniformità a tutti i costi. È evitare che numeri diversi vengano presentati come se misurassero la stessa cosa.

### Tolleranza e materialità

Non ogni differenza richiede la stessa investigazione.

Una discrepanza di 0,02% dovuta a arrotondamenti può essere irrilevante per un'analisi strategica. La stessa discrepanza può essere importante in un processo regolato o in una riconciliazione contabile.

Per questo dovremmo definire:

- quale fonte è autorevole per quale uso;
- quale tolleranza è accettabile;
- quali differenze richiedono escalation;
- quali differenze sono attese e documentate.

### Un buon output della riconciliazione

Alla fine dovremmo poter scrivere una frase come:

> La dashboard Sales supera Finance di €75.170. La differenza è interamente spiegata da timing di riconoscimento, shipping fees, cancellazioni e note di credito; non emerge una perdita di record non spiegata.

oppure:

> Rimangono €18.400 non riconciliati, concentrati su ordini del canale marketplace. Finché il delta non viene spiegato, il dato non è pronto per il consuntivo.

Queste sono conclusioni operative.

> **Se due sistemi mostrano numeri diversi, la prima responsabilità dell'analista non è scegliere un vincitore. È rendere la differenza intelligibile.**