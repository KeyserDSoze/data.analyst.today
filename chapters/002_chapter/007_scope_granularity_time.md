## 2.6 Popolazione, granularità e tempo: dove nasce gran parte degli errori

Anche una domanda apparentemente chiara può produrre risultati diversi se cambiamo popolazione, granularità o finestra temporale.

Questi tre elementi dovrebbero essere esplicitati prima di analizzare.

### Popolazione

Chi o che cosa stiamo studiando?

Esempi:

- tutti i clienti;
- solo clienti attivi;
- nuovi clienti acquisiti negli ultimi sei mesi;
- account enterprise;
- ordini completati;
- sessioni web valide;
- prodotti venduti almeno una volta nel periodo.

Una piccola differenza nella popolazione può cambiare completamente una metrica.

### Granularità

Qual è l'unità elementare dell'analisi?

Possibili livelli:

- evento;
- sessione;
- ordine;
- riga d'ordine;
- cliente;
- account;
- prodotto;
- negozio;
- giorno;
- settimana;
- mese.

Mescolare granularità è una fonte classica di errori.

Esempio: una tabella `orders` contiene una riga per ordine, mentre `order_items` contiene più righe per ordine. Fare una join e poi sommare il fatturato dell'ordine senza correggere la duplicazione può moltiplicare artificialmente i ricavi.

Questo non è un problema di SQL in senso stretto. È un problema di modello mentale del dato.

### Tempo

Il tempo non è solo una colonna data.

Dobbiamo decidere:

- quale timestamp rappresenta il fenomeno;
- quale timezone usare;
- se confrontare giorni, settimane, mesi o coorti;
- come trattare stagionalità e festività;
- se il periodo è completo;
- se i dati arrivano con ritardo;
- come gestire eventi che attraversano più periodi.

Un ordine può avere:

- `created_at`;
- `paid_at`;
- `shipped_at`;
- `delivered_at`;
- `returned_at`.

Quale data rappresenta "la vendita" dipende dalla domanda e dalla definizione contabile o operativa.

### Snapshot vs flow

Alcune metriche rappresentano uno **stock** in un momento preciso:

- clienti attivi a fine mese;
- inventario disponibile oggi;
- pipeline commerciale aperta.

Altre rappresentano un **flusso** durante un intervallo:

- nuovi clienti nel mese;
- ordini ricevuti;
- ticket aperti;
- ricavi riconosciuti.

Confondere stock e flow genera confronti ingannevoli.

### Denominatori

Molte metriche sono rapporti. Il denominatore merita la stessa attenzione del numeratore.

Esempio:

`conversion rate = ordini / visite`

Ma visite significa:

- page views?
- sessioni?
- utenti unici?
- sessioni con product view?
- sessioni eleggibili?

Un cambiamento nel denominatore può far muovere il KPI senza alcun cambiamento reale nel comportamento che pensavamo di misurare.

### Measurement before modeling

NIST sottolinea da tempo che ogni misura nasce da un processo di misurazione e che bias, variabilità, stabilità e incertezza determinano quanto il valore sia adatto a supportare decisioni. Nei sistemi digitali il principio è identico: gli strumenti cambiano, ma anche un evento registrato automaticamente può essere incompleto, duplicato, ritardato o definito male.

### Checklist minima di scope

Prima di eseguire l'analisi, completa:

- **Population:**
- **Unit of analysis:**
- **Numerator:**
- **Denominator:**
- **Time field:**
- **Timezone:**
- **Analysis window:**
- **Baseline:**
- **Known exclusions:**
- **Data latency:**

Questa piccola scheda previene una quantità sorprendente di errori.

## Riferimenti

- NIST/SEMATECH, *Measurement Process Characterization*: https://www.nist.gov/publications/nistsematech-engineering-statistics-handbook-chapter-2-measurement-process
- NIST, *Measurement Uncertainty*: https://www.nist.gov/itl/sed/topic-areas/measurement-uncertainty
