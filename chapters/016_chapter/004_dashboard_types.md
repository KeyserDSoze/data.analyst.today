## 16.3 Una dashboard deve sapere quale responsabilità sta assumendo

Una dashboard diventa confusa quando prova a essere contemporaneamente monitor operativo, ambiente diagnostico e superficie di decisione strategica. Le tre funzioni possono condividere dati e semantic layer, ma hanno cadenze, audience e failure mode differenti.

Una vista **operativa** deve rispondere a “che cosa richiede attenzione adesso?”. Qui contano freshness, soglie, owner dell'alert, runbook e tempi di risposta. Payment failure rate, backlog, stockout risk o pipeline freshness hanno valore soltanto se il segnale è abbastanza tempestivo e qualcuno sa che cosa fare quando supera la soglia. Per questo metriche come time-to-detect, time-to-acknowledge e time-to-action possono essere importanti quanto il KPI business stesso.

Una vista **diagnostica** risponde invece a “dove si concentra il problema e quale ipotesi dobbiamo verificare?”. Ha bisogno di più libertà esplorativa: segmentazioni, decomposition, funnel, cohort, distribuzioni, filtri e drill-through. Il suo obiettivo non è decidere da sola, ma ridurre il percorso da segnale a spiegazione verificabile.

Una vista **decisionale** parte dal Decision Record. Deve rendere facile vedere la scelta aperta, la baseline, i driver materiali, le alternative, il downside, l'incertezza che può cambiare ranking, lo switching value, i guardrail e l'ask. Non è “tutto il business in una schermata”: è una **superficie di scelta**.

### Caso simulato/composito — 54 visual, quattro domande

Una catena retail costruisce una “Executive Sales Dashboard” con **54 visualizzazioni su sei pagine**. Dopo due mesi il CEO usa quasi sempre la dashboard per quattro domande: siamo sopra o sotto piano? dove si concentra il delta? il fenomeno è transitorio o persiste? quale decisione richiede attenzione questa settimana?

Il redesign smette di cercare una sola pagina universale. La home decisionale mostra revenue e contribution margin vs plan, decomposition del gap, forecast di fine mese con range e tre exception con owner e decision requested. Una pagina diagnostica conserva categorie, regioni, canali, funnel, promozioni e mix. Un evidence layer espone tabelle dettagliate, definizioni, freshness, lineage e controlli.

La home contiene meno elementi, ma il sistema offre **più accesso alla complessità** perché il percorso dal segnale alla prova è esplicito.

## One screen come disciplina, non come dogma

Microsoft Learn raccomanda di pensare all'audience, mettere in evidenza le informazioni più importanti e, quando possibile, evitare che la dashboard richieda scroll per capire lo stato principale.[^ms-dashboard] Questo non significa che l'intero sistema analitico debba vivere su una sola pagina. Significa che la prima vista dovrebbe rispondere rapidamente a una domanda: **c'è qualcosa che richiede una decisione o un'azione?**

La Government Analysis Function 2026 usa una logica simile: headline content prima, dettaglio in altri layer, minimizzazione di scroll e click, user testing e attenzione ai diversi dispositivi.[^gaf-test]

## Testare il task, non il gusto

“Ti piace?” è una domanda debole per validare una dashboard. Un test migliore chiede a un utente reale di trovare l'anomalia più importante, indicare rispetto a quale baseline è anomala, capire se il dato è maturo, localizzare il driver, dire quale azione sembra richiesta e trovare definizione e fonte.

Misuriamo così **task success, errori di interpretazione e tempo di comprensione**. Se l'informazione esiste ma il compito fallisce, la dashboard non sta facendo bene il proprio lavoro.

## Anche una dashboard deve avere un lifecycle

Una dashboard non merita di esistere per sempre solo perché è stata costruita. Va riesaminata quando le metriche sono duplicate, l'owner scompare, il processo business cambia, gli alert vengono ignorati, le definizioni non sono più mantenute o gli utenti esportano sistematicamente i dati per ricostruire altrove la vista che serve davvero.

La Government Analysis Function raccomanda infatti di costruire dashboard soltanto quando esiste un user need chiaro, gli aggiornamenti sono frequenti, l'interattività aggiunge valore e l'organizzazione ha risorse per mantenerle.[^gaf-lifecycle]

> **Una buona dashboard non mostra tutto. Assume una responsabilità precisa e collega quella responsabilità alla profondità giusta di evidenza, con un percorso chiaro da segnale ad azione e una condizione per essere ridisegnata o ritirata.**

[^ms-dashboard]: Microsoft Learn, *Tips for designing a great Power BI dashboard*, https://learn.microsoft.com/en-us/power-bi/create-reports/service-dashboards-design-tips
[^gaf-test]: Government Analysis Function, *Data visualisation: testing dashboards for design and accessibility*, https://analysisfunction.civilservice.gov.uk/policy-store/data-visualisation-testing-dashboards-for-design-and-accessibility/
[^gaf-lifecycle]: Government Analysis Function, *Data visualisation: building and managing dashboards*, https://analysisfunction.civilservice.gov.uk/policy-store/data-visualisation-building-and-managing-dashboards/
