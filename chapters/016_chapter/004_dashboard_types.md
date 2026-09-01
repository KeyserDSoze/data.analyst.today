## 16.3 Dashboard operative, diagnostiche e decisionali: tre prodotti diversi

Una dashboard diventa confusa quando prova a servire contemporaneamente monitoraggio, diagnosi e decisione strategica.

Questi tre usi hanno cadenze, audience e requisiti differenti.

## 1. Dashboard operativa — rilevare e agire

Domanda:

> **“Cosa richiede attenzione adesso?”**

Caratteristiche:

- refresh coerente con la velocità del processo;
- pochi segnali critici;
- baseline e soglie operative;
- stato del dato/freshness visibile;
- owner dell'alert;
- azione o runbook associato;
- drill-down rapido.

Esempi:

- payment failure rate;
- backlog di ordini;
- stockout risk;
- call-center queue;
- pipeline freshness.

Metriche utili non sono soltanto i KPI business. Possiamo misurare anche:

- **time to detect**;
- **time to acknowledge**;
- **time to action**.

Un alert che nessuno possiede è decorazione operativa.

## 2. Dashboard diagnostica — localizzare e spiegare

Domanda:

> **“Dove si concentra il problema e quali ipotesi dobbiamo verificare?”**

Qui servono più libertà esplorativa:

- segmentazioni;
- decomposizioni;
- funnel;
- coorti;
- distribuzioni;
- filtri;
- drill-through;
- confronto con baseline e periodi alternativi.

È normale che questa dashboard sia più ricca della vista executive.

Il suo obiettivo non è decidere da sola, ma ridurre il tempo necessario per passare da segnale a diagnosi.

## 3. Dashboard decisionale — confrontare alternative

Domanda:

> **“Quale scelta è aperta e quali evidenze possono cambiarla?”**

Una vista decisionale dovrebbe derivare dal Decision Record e rendere visibili soprattutto:

- decision question;
- stato corrente e baseline;
- driver materiali;
- alternative;
- valore/upside e downside;
- incertezza decision-critical;
- switching value o soglia;
- guardrail;
- decision requested.

Non è un report di tutto il business. È una **superficie di scelta**.

## Caso simulato/composito — La executive dashboard da 54 visual

Una catena retail costruisce una “Executive Sales Dashboard” con 54 visualizzazioni su sei pagine.

Dopo due mesi il CEO usa quasi sempre soltanto quattro domande:

1. siamo sopra o sotto piano?
2. dove si concentra il delta?
3. il fenomeno è transitorio o persiste?
4. quale decisione richiede attenzione questa settimana?

Il redesign separa i prodotti.

### Home decisionale

- revenue e contribution margin vs plan;
- decomposition del gap;
- forecast di fine mese con range;
- tre exception con owner e decision requested.

### Pagina diagnostica

- categorie, regioni, canali, funnel, promozioni e mix.

### Evidence layer

- tabelle dettagliate;
- definizioni;
- freshness;
- lineage e controlli.

La dashboard contiene meno elementi nella home ma offre **più accesso alla complessità** perché la gerarchia è esplicita.

## One screen: disciplina, non dogma

Microsoft suggerisce di rendere visibile la storia principale senza costringere il lettore a scorrere o cercare tra troppi elementi, quando possibile.

Questo non significa che un sistema analitico debba avere una sola pagina.

Significa che la prima vista deve rispondere:

> **“C'è qualcosa che richiede una decisione?”**

prima di chiedere all'utente di esplorare.

## Dashboard testing: non basta chiedere “ti piace?”

La Government Analysis Function britannica raccomanda di testare i dashboard rispetto ai bisogni reali degli utenti e su dispositivi e modalità di accesso differenti.

Un test utile può chiedere a un utente reale di:

1. trovare l'anomalia più importante;
2. spiegare quale confronto la rende anomala;
3. individuare il dettaglio necessario a diagnosticarla;
4. dire quale azione ritiene richiesta;
5. trovare fonte, definizione e data di aggiornamento.

Misuriamo così **task success e tempo di comprensione**, non soltanto preferenza estetica.

## Dashboard lifecycle

Una dashboard deve poter anche morire.

Segnali di retirement o redesign:

- non supporta più una decisione reale;
- metriche duplicate altrove;
- definizioni non mantenute;
- owner assente;
- utenti esportano sistematicamente i dati per ricostruire la vera vista;
- alert ignorati;
- il processo business è cambiato.

Mantenere per sempre dashboard obsolete aumenta il costo di trovare la fonte autorevole.

> **Una buona dashboard non mostra tutto. Collega un bisogno decisionale alla profondità giusta di evidenza, con un percorso chiaro da segnale ad azione.**

### Fonti

- Microsoft Learn, *Tips for designing a great Power BI dashboard*: https://learn.microsoft.com/en-us/power-bi/create-reports/service-dashboards-design-tips
- Government Analysis Function, *Data visualisation: testing dashboards for design and accessibility*: https://analysisfunction.civilservice.gov.uk/policy-store/data-visualisation-testing-dashboards-for-design-and-accessibility/
