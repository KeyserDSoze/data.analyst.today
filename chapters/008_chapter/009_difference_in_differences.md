## 8.8 Difference-in-Differences: usare un'altra traiettoria come controfattuale

La **Difference-in-Differences (DiD)** non confronta semplicemente due gruppi.

Confronta **come cambiano** due gruppi nel tempo.

L'idea è:

```text
DiD = (Trattati_dopo - Trattati_prima)
    - (Confronto_dopo - Confronto_prima)
```

Il gruppo di confronto serve a stimare quale cambiamento avrebbero avuto i trattati **senza** l'intervento.

### Caso simulato/composito — Nuovo layout in 25 negozi

Revenue medio settimanale:

| Gruppo | Prima | Dopo | Variazione |
|---|---:|---:|---:|
| Nuovo layout | 118.000 € | 129.000 € | +11.000 € |
| Confronto | 121.000 € | 126.000 € | +5.000 € |

Il prima/dopo dei trattati suggerisce `+11.000 €`.

Ma anche i negozi non trattati crescono di `+5.000 €`, forse per domanda generale o calendario.

La DiD è:

`+11.000 - +5.000 = +6.000 €`

La causal claim non deriva però dalla sottrazione.

Deriva dall'assunzione che, senza nuovo layout, i negozi trattati avrebbero seguito una variazione comparabile a quella dei negozi di confronto.

### Parallel trends è il cuore del design

L'assunzione fondamentale è spesso chiamata **parallel trends**.

Non richiede che i gruppi partano dallo stesso livello.

Richiede che la traiettoria del gruppo di confronto sia un proxy credibile per la traiettoria controfattuale dei trattati.

La World Bank descrive proprio la DiD come confronto tra il cambiamento del gruppo trattato e quello del gruppo di confronto e sottolinea la centralità di questa assunzione.[^worldbank-did]

### I pre-trend sono diagnostica, non prova

Se abbiamo più periodi prima dell'intervento, possiamo verificare se le traiettorie storiche erano simili.

Questo è molto utile.

Ma:

> **trend pre-trattamento paralleli non dimostrano che i trend controfattuali sarebbero rimasti paralleli dopo.**

Sono evidenza a favore del design, non certificazione automatica.

### Caso simulato/composito — Il pricing UK vs Francia

MRR medio per account:

| Mese | UK | Francia |
|---|---:|---:|
| Gen | 186 € | 181 € |
| Feb | 191 € | 182 € |
| Mar | 198 € | 183 € |
| Apr — pricing | 211 € | 184 € |
| Mag | 222 € | 185 € |

L'UK cresceva molto più rapidamente **già prima** del pricing.

La Francia è quindi un controfattuale debole per la dinamica UK.

Un coefficiente DiD può essere calcolato. Il design resta fragile.

### Shock differenziali contemporanei

La DiD non protegge da eventi che cambiano nello stesso periodo **solo** per il gruppo trattato.

Esempi:

- campagna locale;
- nuova concorrenza;
- differenze di stock;
- modifica del tracking;
- cambio di sales team;
- shock normativo aggiuntivo.

Se un'altra causa cambia insieme al trattamento, la stima può attribuire al trattamento anche quell'effetto.

### Composizione del gruppo

Un'altra minaccia sottovalutata è che la popolazione osservata cambi.

Supponiamo che dopo il pricing escano molti clienti piccoli dal gruppo UK. L'MRR medio per account può crescere anche perché la composizione si sposta verso account più grandi.

Quindi bisogna verificare:

- unità che entrano/escono;
- definizione della popolazione;
- attrition differenziale;
- eventuali cambi di mix.

### Announcement e anticipation

Il “momento del trattamento” non è sempre la data formale.

Se una policy viene annunciata tre mesi prima, clienti e manager possono reagire prima dell'entrata in vigore.

Un event study può mostrare effetti anticipati. In quel caso dobbiamo ripensare la timeline, non semplicemente dichiarare che DiD “ha fallito”.

### Event study: vedere la dinamica dell'effetto

Con più periodi possiamo rappresentare coefficienti relativi al momento dell'intervento.

Serve a investigare:

- pre-trend;
- anticipazione;
- effetto immediato o graduale;
- persistenza;
- decadimento.

Ma anche qui il grafico non sostituisce l'identification argument.

### Staggered adoption: attenzione alle DiD meccaniche

Nel mondo reale unità diverse possono ricevere il trattamento in momenti differenti.

Per esempio un nuovo processo viene introdotto regione per regione.

In questi casi una semplice regressione `unit fixed effects + time fixed effects` può diventare difficile da interpretare quando gli effetti cambiano nel tempo o tra coorti di trattamento.

Per un Data Analyst il principio operativo è:

> **se il rollout è staggered, non assumere che la DiD più semplice abbia automaticamente lo stesso significato della formula a due gruppi e due periodi.**

Serve una strategia coerente con il timing del rollout e con l'estimand desiderato.

### Causal checklist DiD

```text
Trattamento e data effettiva:
Gruppo di confronto:
Perché è un controfattuale plausibile?
Periodi pre disponibili:
Pre-trend compatibili?
Anticipazione possibile?
Shock differenziali?
Composizione stabile?
Treatment timing uguale o staggered?
Outcome definito allo stesso modo nel tempo?
Qual è l'estimand?
```

### Claim calibrato

Debole:

> “Dopo il rollout le vendite sono salite, quindi il rollout ha funzionato.”

Più forte:

> **“Rispetto a un gruppo con traiettoria pre-intervento comparabile, il gruppo trattato mostra un incremento differenziale di circa 6.000 € a settimana; l'interpretazione causale dipende da parallel trends e dall'assenza di shock differenziali rilevanti.”**

> **Difference-in-Differences non trasforma il tempo in causalità. Usa una traiettoria osservata per rappresentare una traiettoria controfattuale, sotto assunzioni che devono essere difese.**

[^worldbank-did]: World Bank e Inter-American Development Bank, *Impact Evaluation in Practice*, capitolo su Difference-in-Differences: https://www.worldbank.org/en/programs/sief-trust-fund/publication/impact-evaluation-in-practice
