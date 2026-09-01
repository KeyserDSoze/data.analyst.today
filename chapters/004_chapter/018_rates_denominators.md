## 4.17 Conteggi, proporzioni e tassi: il denominatore è parte della metrica

Un conteggio dice **quanto** è successo. Un tasso o una proporzione prova a dire **quanto è successo rispetto alla popolazione o all'esposizione rilevante**.

Questa distinzione sembra elementare, ma cambia continuamente le conclusioni.

### Caso simulato/composito — Lo stabilimento con più incidenti

La società industriale immaginaria **IronPeak Components** gestisce tre stabilimenti.

| Stabilimento | Incidenti |
|---|---:|
| Torino | 18 |
| Verona | 11 |
| Bari | 9 |

Il primo report mette Torino in rosso: registra il doppio degli incidenti di Bari.

Poi l'analista aggiunge l'esposizione:

| Stabilimento | Incidenti | Ore lavorate | Incidenti per 100.000 ore |
|---|---:|---:|---:|
| Torino | 18 | 610.000 | 2,95 |
| Verona | 11 | 280.000 | 3,93 |
| Bari | 9 | 170.000 | 5,29 |

La graduatoria si ribalta.

Torino genera più incidenti assoluti perché è il sito più grande. Bari mostra invece il tasso più alto rispetto alle ore lavorate.

Per una decisione sulla **frequenza del rischio** guarderemmo soprattutto il tasso. Per una decisione sul **numero totale di persone o casi coinvolti** potrebbe continuare a contare anche il volume assoluto.

Nessuno dei due numeri sostituisce automaticamente l'altro.

### Quattro domande sul denominatore

Prima di fidarci di una percentuale conviene chiedere:

1. **Elegibilità** — chi avrebbe potuto produrre l'evento del numeratore?
2. **Esposizione** — quanto è stata esposta ogni unità all'opportunità o al rischio?
3. **Tempo** — numeratore e denominatore coprono davvero lo stesso intervallo?
4. **Unità** — stiamo contando persone, ordini, articoli, sessioni o ore?

Il CDC, nel suo materiale di epidemiologia applicata, sottolinea proprio la necessità di mettere gli eventi in relazione alla popolazione o all'esposizione appropriata quando si confrontano gruppi di dimensione diversa.[^cdc-rates]

In business analytics il principio è identico.

### Lo stesso nome può nascondere denominatori diversi

Prendiamo un `return_rate`.

Può significare:

- ordini con almeno un reso / ordini consegnati;
- unità restituite / unità vendute;
- valore economico restituito / valore venduto.

Sono tre metriche legittime e tre domande differenti.

Un ordine con dieci articoli, di cui uno restituito, produce:

- un ordine con reso;
- una unit return rate del 10%;
- una value return rate che dipende dal prezzo dell'articolo restituito.

Scrivere semplicemente `return_rate = 8%` senza definire il denominatore lascia aperta una parte essenziale del significato.

### Il denominatore può cambiare la direzione del trend

Una piattaforma registra:

- gennaio: 900 cancellazioni su 25.000 abbonati attivi;
- giugno: 1.100 cancellazioni su 40.000 abbonati attivi.

Il numero di cancellazioni cresce del 22,2%.

Il tasso passa invece dal 3,6% al 2,75%.

Il volume peggiora, il rischio relativo migliora.

La domanda di business decide quale prospettiva è rilevante. Il team customer success può preoccuparsi del carico assoluto di 1.100 cancellazioni; chi valuta la salute della base clienti può essere interessato soprattutto al tasso.

### Attenzione al denominatore “quasi giusto”

Un marketplace confronta due seller:

- seller A: 240 reclami su 120.000 ordini → 2,0 per 1.000 ordini;
- seller B: 90 reclami su 18.000 ordini → 5,0 per 1.000 ordini.

B sembra peggiore dopo la normalizzazione.

Ma se B vende quasi esclusivamente prodotti complessi con un rischio di reclamo molto più alto, anche `reclami / ordini` può essere un confronto incompleto. Il denominatore è corretto aritmeticamente, ma la **popolazione esposta non è necessariamente comparabile**.

Questo è il ponte verso la sezione successiva: scegliere un denominatore è necessario, ma non sempre sufficiente.

### La frase di controllo

Prima di interpretare una percentuale, completa:

> **Il numeratore conta ________; il denominatore rappresenta ________; entrambi coprono il periodo ________ e la popolazione eleggibile ________.**

Se non riusciamo a riempire questi spazi senza ambiguità, non abbiamo ancora una metrica sufficientemente definita.

[^cdc-rates]: CDC, *Describing Epidemiologic Data*, Field Epidemiology Manual: https://www.cdc.gov/field-epi-manual/php/chapters/describing-epi-data.html
