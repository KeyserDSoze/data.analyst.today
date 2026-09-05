# Release Candidate — stato corrente

Ultimo aggiornamento: **5 settembre 2026**.

Il repository contiene release candidate storiche già pubblicate, ma il manoscritto corrente ha ricevuto successivamente una revisione prose-first sostantiva dell'intero corpo. Questo file non riutilizza quindi RC1 o RC2 come se descrivessero ancora la baseline editoriale corrente.

## Candidate storiche

### v1.0.0-rc1

Prima release candidate pubblica. La relativa nota resta in `release-notes/v1.0.0-rc1.md`.

### v1.0.0-rc2

Seconda release candidate pubblica, focalizzata principalmente su identità editoriale, frontespizio, impaginazione e formati distributivi. La relativa nota resta in `release-notes/v1.0.0-rc2.md`.

RC2 dichiarava esplicitamente che quell'intervento non modificava il contenuto sostantivo. Il pass editoriale completato il **5 settembre 2026** è invece sostantivo e coinvolge tutti i Capitoli 0–19, front matter e reference layer. Per questo RC1/RC2 restano artefatti storici e non vengono sovrascritti.

## Stato del manoscritto post-revisione

La baseline di contenuto e apparati validata dopo il pass finale è:

`470ad51bd762c912a15addbce40619f03e42c415`

Book CI run `33980921004`: **SUCCESS**.

La run conferma:

- **20 capitoli**;
- **321 file Markdown** nel corpo;
- **247.697 parole stimate**;
- **1.772.827 caratteri**;
- **189 URL esterni distinti**;
- **0 file con LaTeX residuo**;
- **0 file con grafie ASCII legacy**;
- **723 pagine PDF**;
- **344 voci outline PDF**;
- **232 tabelle DOCX** con repeating header;
- **30 documenti XHTML EPUB**;
- metadata autore `Alessandro Rapiti` verificati nei formati distributivi;
- nessuna footnote Markdown irrisolta negli output.

Il source/factual audit è stato riallineato alla revisione finale. In particolare il precedente customer case NXP del Capitolo 17 e i claim `75% / 90%` sono stati rimossi e sostituiti con documentazione AWS corrente su cost allocation e unit metrics.

Dettagli:

- `EDITORIAL_AUDIT.md`;
- `SOURCE_FACTUAL_AUDIT.md`.

## Nessuna nuova candidate pubblicata automaticamente

Questo pass non modifica il release manifest e non pubblica una nuova GitHub Release. Gli step release-specific della CI risultano infatti correttamente `skipped`.

La prossima candidate pubblica dovrà usare **un nuovo identificatore** invece di riutilizzare RC1 o RC2. Il numero/tag esatto resta una decisione di pubblicazione separata.

## Gate per la prossima candidate

Prima di creare una nuova candidate pubblica devono essere veri contemporaneamente:

| Gate | Stato corrente |
|---|---|
| Capitoli 0–19 revisionati | **PASS** |
| Front matter allineato | **PASS** |
| Reference layer allineato | **PASS** |
| Source/factual audit corrente | **PASS** |
| Freshness recheck finale | **PASS** |
| Normalized sources | **PASS** |
| Lint strict | **PASS** |
| Markdown/DOCX/PDF/EPUB build | **PASS** |
| Output guardrails | **PASS** |
| Nuovo tag / release identifier scelto | **OPEN — publishing decision** |
| Copyright/licenza definitiva | **OPEN — publishing decision** |

## Tesi da preservare

Definizione finale:

> **Il Data Analyst è la persona che trasforma domande ambigue e dati imperfetti in evidenza sufficientemente affidabile da migliorare una decisione.**

Ultima riga del corpo:

> **Gli strumenti cambieranno. Il timone resta una responsabilità.**

## Criterio di freeze

Il pass editoriale descritto in questa conversazione è chiuso. Nuove modifiche alla futura candidate dovrebbero essere motivate da errori fattuali o tipografici, source decay, regressioni di build/rendering, accessibilità/navigazione, metadata di pubblicazione oppure da una nuova revisione sostantiva esplicitamente aperta.

Non è necessario riaprire l'intero manoscritto per preferenze stilistiche marginali o per aggiungere esempi non richiesti da una lacuna dimostrata.