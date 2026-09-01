## 16.1 Dalla visualizzazione esplorativa all'evidenza decisionale

Non tutti i grafici che ci aiutano a capire devono arrivare davanti a chi decide.

Durante l'EDA produciamo **discovery artifacts**: servono a cercare pattern, smentire ipotesi, cambiare grain, verificare segmenti, confrontare definizioni e capire dove investigare.

Durante la comunicazione costruiamo invece **decision artifacts**: servono a sostenere un passaggio preciso del Decision Record.

La differenza non è estetica. È epistemica.

## Discovery artifacts: spazio di ricerca

Nell'esplorazione è normale produrre:

- distribuzioni;
- segmentazioni;
- scatter plot;
- decine di breakdown;
- versioni alternative di un KPI;
- grafici che alla fine si rivelano inutili;
- controlli che servono soprattutto a escludere spiegazioni.

Questa abbondanza è spesso necessaria.

Il problema nasce quando confondiamo **quanto lavoro abbiamo fatto** con **quanto materiale il pubblico deve vedere**.

## Decision artifacts: spazio di prova

Un elemento entra nella Decision Communication Pack solo se svolge almeno una funzione esplicita:

| Ruolo | Domanda |
|---|---|
| Orient | Che cosa sta succedendo? |
| Compare | Quale alternativa/segmento differisce? |
| Diagnose | Dove si concentra il fenomeno? |
| Decide | Quale trade-off o soglia cambia la scelta? |
| Verify | Quale dettaglio consente di controllare il claim? |

Un grafico che non riesce a completare una di queste frasi è probabilmente ancora un discovery artifact.

## Evidence promotion: non tutto ciò che troviamo merita la slide

Tra discovery e decision serve un passaggio di **promozione dell'evidenza**.

Prima di portare un pattern nella comunicazione chiediamo:

1. la metrica è certificata o almeno definita?
2. il grain è coerente con il claim?
3. il pattern resiste a segmentazioni e controlli ragionevoli?
4. esiste un problema di composizione o denominatore?
5. l'incertezza può cambiarne il significato?
6. il linguaggio proposto supera la forza del metodo?
7. questa evidenza cambia davvero una decisione?

Solo dopo il pattern entra nel pack.

## Caso simulato/composito — 27 grafici, tre prove

Un e-commerce vede la conversione scendere dal 3,8% al 3,4%.

Durante l'indagine il team produce 27 grafici: device, browser, paese, canale, landing, ora, new/returning, payment method, app version, basket size, categoria e altri breakdown.

Alla fine emergono quattro fatti robusti:

- circa il 78% del delta è su iOS;
- il peggioramento è quasi interamente nella versione 6.12;
- il drop si concentra tra `payment_started` e `payment_authorized`;
- Android e le versioni iOS precedenti sono sostanzialmente stabili.

La Decision Communication Pack non contiene i 27 grafici.

Contiene:

1. **decomposition del delta per piattaforma** — localizza il problema;
2. **conversion per app version** — identifica la concentrazione del segnale;
3. **funnel del payment step** — mostra dove si rompe il percorso;
4. in appendix, i controlli che dimostrano che i principali segmenti alternativi non spiegano il fenomeno.

Il lavoro esplorativo non è stato buttato via. È diventato **provenance della selezione**.

## Non presentare la cronologia dell'indagine

Una presentazione analyst-first spesso dice:

> “Prima abbiamo guardato il traffico, poi i paesi, poi i device, poi abbiamo provato...”

Il decision maker raramente ha bisogno della cronologia.

Ha bisogno della logica:

**decision question → headline → evidence → caveat → alternative → ask**.

La cronologia investigativa può essere utile in un post-mortem o in una peer review, non necessariamente nella pagina executive.

## Ogni visual deve avere una frase verificabile

Per ogni elemento importante completiamo:

> **“Questo visual serve a mostrare che...”**

Debole:

> “Questo mostra la conversion per paese.”

Forte:

> “Questo mostra che la Germania spiega circa due terzi del gap europeo, mentre gli altri mercati restano vicini alla baseline.”

La seconda frase definisce un claim che il visual può sostenere o smentire.

## La regola della provenance

Togliere grafici dalla pagina principale non deve rendere il ragionamento opaco.

Per questo ogni decision artifact dovrebbe poter rimandare a:

- definizione metrica;
- query/dataset;
- periodo;
- controlli principali;
- eventuale appendix;
- owner o documento analitico sorgente.

La sintesi è affidabile quando possiamo risalire dalla headline alla prova.

> **La visualizzazione esplicativa non è il riassunto del percorso fatto dall'analista. È la selezione minima di evidenze necessarie per valutare una decisione.**
