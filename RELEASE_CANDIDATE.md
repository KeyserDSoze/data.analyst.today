# Release Candidate — v1.0.0-rc3

Data candidate: **5 settembre 2026**.

Stato: **release candidate editoriale selezionata per la pubblicazione come prerelease**.

RC1 e RC2 restano candidate storiche già pubblicate. RC3 è la prima candidate successiva alla revisione prose-first sostantiva completata su tutto il manoscritto, front matter e reference layer.

## Perché RC3

### v1.0.0-rc1

Prima release candidate pubblica. La relativa nota resta in `release-notes/v1.0.0-rc1.md`.

### v1.0.0-rc2

Seconda release candidate pubblica, focalizzata principalmente su identità editoriale, frontespizio, impaginazione e formati distributivi. La relativa nota resta in `release-notes/v1.0.0-rc2.md`.

RC2 dichiarava esplicitamente che quell'intervento non modificava il contenuto sostantivo. Il pass completato il **5 settembre 2026** è invece sostantivo e coinvolge tutti i Capitoli 0–19. Per questo non viene riutilizzato un tag precedente: la nuova candidate è **`v1.0.0-rc3`**.

Le note pubbliche della candidate sono in:

`release-notes/v1.0.0-rc3.md`

## Baseline di contenuto validata

La baseline di contenuto e apparati validata prima dei soli commit di metadata RC3 è:

`470ad51bd762c912a15addbce40619f03e42c415`

Book CI run `33980921004`: **SUCCESS**.

La run conferma:

| Indicatore | Valore |
|---|---:|
| Capitoli | 20 |
| File Markdown corpo | 321 |
| Parole stimate corpo | 247.697 |
| Caratteri corpo | 1.772.827 |
| URL esterni distinti | 189 |
| File con LaTeX residuo | 0 |
| Grafie ASCII legacy | 0 |
| PDF | 723 pagine |
| PDF outline | 344 voci |
| Tabelle DOCX con repeating header | 232 |
| EPUB | 30 documenti XHTML |
| Metadata autore PDF/DOCX/EPUB | Alessandro Rapiti |

La CI ha inoltre confermato assenza di footnote Markdown irrisolte negli output, outline PDF valido, repeating header su tutte le tabelle DOCX, frontespizio DOCX con first-page footer separato e vuoto e struttura EPUB valida.

I commit successivi a questa baseline, fino al commit che modifica `release.json`, riguardano esclusivamente note e metadata della candidate. Il corpo dei Capitoli 0–19 non viene modificato.

## Gate RC3

| Gate | Stato |
|---|---|
| Capitoli 0–19 revisionati | **PASS** |
| Front matter allineato | **PASS** |
| Reference layer allineato | **PASS** |
| Source/factual audit corrente | **PASS** |
| Freshness recheck finale | **PASS** |
| Caso NXP ritirato e audit riallineato | **PASS** |
| Normalized sources | **PASS** |
| Lint strict | **PASS** |
| Markdown/DOCX/PDF/EPUB build | **PASS** |
| Output guardrails | **PASS** |
| Release identifier | **v1.0.0-rc3** |
| Prerelease | **SÌ** |
| Copyright/licenza definitiva | **OPEN — publishing decision per release stabile** |

## Meccanismo di pubblicazione

La pipeline pubblica una GitHub Release soltanto quando cambia `release.json` su `main`. Per RC3 il manifest deve indicare:

```json
{
  "tag": "v1.0.0-rc3",
  "name": "Data Analyst Today v1.0.0-rc3",
  "prerelease": true,
  "notes_file": "release-notes/v1.0.0-rc3.md"
}
```

La stessa run deve prima completare con successo `validate-and-build`; solo dopo usa gli artifact prodotti da quella build per creare la prerelease.

## Tesi da preservare

Definizione finale:

> **Il Data Analyst è la persona che trasforma domande ambigue e dati imperfetti in evidenza sufficientemente affidabile da migliorare una decisione.**

Ultima riga del corpo:

> **Gli strumenti cambieranno. Il timone resta una responsabilità.**

## Freeze RC3

Una volta pubblicata `v1.0.0-rc3`, nuove modifiche al contenuto dovrebbero essere motivate da errori fattuali o tipografici dimostrati, source decay, regressioni di build/rendering, problemi di accessibilità/navigazione o metadata di pubblicazione.

Preferenze stilistiche marginali o nuovi esempi non necessari non riaprono automaticamente il manoscritto.