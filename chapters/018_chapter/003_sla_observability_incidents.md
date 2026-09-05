## 18.2 Reliability: il servizio deve sapere quando non è fit for decision

Una pipeline può essere verde e il prodotto analitico rosso. Se il report arriva alle 10:15 ma il capacity meeting è alle 09:00, il servizio ha fallito. Se arriva puntuale con il 92% delle transazioni e nessuno sa quale sorgente manchi, ha fallito in un altro modo. Se è fresco e completo ma una definizione è cambiata senza preavviso, il rischio può essere persino maggiore.

Per questo la reliability dell'analytics deve partire dal **consumer della decisione**, non dal job scheduler. Infrastructure health e pipeline health restano importanti, ma non bastano. La domanda più alta è: il dato è disponibile entro la deadline, con copertura, significato e reconciliation sufficienti per sostenere la decisione che promette di supportare?

## SLI, SLO e SLA: trasformare “affidabile” in una promessa misurabile

Google SRE distingue **SLI**, la misura osservata di un comportamento rilevante; **SLO**, il target desiderato; e **SLA**, l'accordo che associa conseguenze esplicite al mancato rispetto di un livello di servizio. Il valore della distinzione, per l'analytics, è costringerci a specificare ciò che conta per l'utente invece di dichiarare genericamente che una dashboard “deve essere affidabile”.

Fonte: https://sre.google/sre-book/service-level-objectives/

Per un executive revenue pack possiamo avere un SLI di freshness — percentuale di business day in cui `executive_revenue` è certificato entro le 07:00 CET — con SLO `≥99%`. Possiamo avere un SLI di completeness — quota di ordini del giorno precedente presenti rispetto alla fonte operativa riconciliata — con SLO `≥99,8%` prima della pubblicazione. E possiamo avere gate di semantic correctness per i quali il target è semplicemente `100%` perché fallire quel controllo significa non pubblicare.

Gli indicatori utili dipendono dal prodotto. In analytics contano spesso freshness, completeness, correctness, semantic stability, availability, event-to-data latency, recoverability e traceability. Non dobbiamo copiare gli SLO software alla lettera: dobbiamo scegliere le proprietà che, se degradano, cambiano il diritto del consumer a usare il numero.

Anche il target deve seguire il criticality tier. Un notebook T0 è best effort. Una dashboard T1 può promettere refresh entro le 09:00 nel 95% dei business day. Un executive pack T2 può richiedere certification entro le 07:00 nel 99% dei giorni più blocking reconciliation. Un feed T3 può richiedere recovery e auditability concordati con il processo finanziario o regolatorio che alimenta.

Google SRE sottolinea inoltre che 100% di reliability è spesso indesiderabile: può imporre costi e conservatorismo sproporzionati. Il punto è scegliere un SLO coerente con ciò che gli utenti realmente richiedono, non con il desiderio astratto di perfezione.

## Error budget: quando la reliability deve battere le feature

Uno SLO sotto il 100% implica un margine di fallimento accettato, l'**error budget**. Nell'analytics non serve trasformarlo in rituale matematico. Serve a rendere esplicita una decisione di priorità.

Se un prodotto T2 con readiness SLO del 99% consuma troppo rapidamente il proprio budget, può diventare ragionevole congelare nuove feature, ridurre dipendenze fragili o investire in root-cause e recovery. La policy di error budget di Google SRE usa esattamente questo principio: affidabilità e velocità del cambiamento competono per capacità, e il budget fornisce un meccanismo per decidere quando spostare attenzione verso la stabilità.

Fonte: https://sre.google/workbook/error-budget-policy/

## La dashboard verde con 63 store mancanti

Una catena retail usa ogni mattina una dashboard per allocare stock. Alle 08:00 la pipeline è `SUCCESS`, il report è disponibile e i KPI sembrano normali. Alle 10:30 Operations scopre che **63 store** non hanno inviato dati POS.

Il sistema monitorava job success, runtime e presenza della tabella. Non monitorava il numero di store attesi, coverage per sorgente, scostamento del volume dalla baseline o reconciliation con POS. La pipeline aveva processato correttamente ciò che aveva ricevuto; il prodotto aveva violato la propria promessa.

Questo caso definisce meglio l'osservabilità di qualsiasi catalogo di metriche. Non dobbiamo monitorare tutto: dobbiamo osservare i segnali che permettono di scoprire un fallimento **prima che produca una decisione sbagliata**. In questo esempio il source coverage è un segnale decision-critical; CPU e runtime non lo sono, almeno non da soli.

Google SRE distingue monitoring utile per trend, debugging, dashboard e alerting e ricorda che un alert dovrebbe richiedere un'azione umana significativa, non generare rumore permanente.

Fonte: https://sre.google/sre-book/monitoring-distributed-systems/

Per un data product questo porta a quattro famiglie di segnali: source signals come arrival, partition coverage e schema version; transformation signals come join match rate, duplicate e row expansion; semantic signals come invariant, reconciliation e denominator shift; consumer signals come data age, query failure, consumer impact e missed decision deadline. La gerarchia conta più del numero di monitor.

## Page, ticket o monitor soltanto

Non ogni deviazione deve svegliare qualcuno. Un problema T2/T3 fuori SLO, vicino alla decision deadline e con un'azione immediata possibile può meritare una page. Un degrado di qualità senza impatto immediato può diventare ticket. Un segnale utile soltanto a trend e capacity planning può restare monitoring. Se tutto pagina, nessun alert resta credibile.

Questa distinzione prepara il concetto più importante della sezione: un prodotto analitico non vive soltanto negli stati `verde` e `rotto`.

## Serving states: degradare senza fingere

Lo stato del servizio deve essere leggibile dal consumer e progettato prima dell'incidente.

| Stato | Significato operativo |
|---|---|
| `READY` | tutti i blocking gate passano |
| `READY WITH CAVEATS` | il dato è utilizzabile per la decisione dichiarata, con caveat visibile |
| `STALE BUT SERVABLE` | il nuovo refresh non è pronto, ma l'ultima snapshot certificata è ancora valida entro limiti espliciti |
| `PARTIAL / DEGRADED` | parte della copertura manca e l'ambito escluso è dichiarato |
| `BLOCKED` | il rischio di correttezza o significato rende il prodotto non fit for decision |

Supponiamo che manchi un mercato che vale il 2% delle vendite. Pubblicare come se nulla fosse è scorretto; bloccare l'intero prodotto può essere inutile. `PARTIAL` con coverage label può essere la risposta giusta se il decision owner accetta quel rischio residuo. Se invece manca una reconciliation finanziaria materiale, lo stesso prodotto può dover passare a `BLOCKED`.

Un fallback segue la stessa logica: last-known-good, stima `PROVISIONAL`, dataset parziale, manual reconciliation o superficie disabilitata non sono strategie per massimizzare availability. Sono modi per **preservare il significato mentre la promessa piena non è disponibile**.

## Incident severity e runbook

La severity dovrebbe combinare decisione impattata, valore economico, deadline, consumer, rischio regolatorio/privacy, reversibilità e durata. Una possibile tassonomia è: `SEV-1` per un dato T3 errato già usato o imminente in una high-consequence decision; `SEV-2` per un prodotto T2 bloccato o materialmente sbagliato prima della deadline; `SEV-3` per un problema circoscritto con workaround; `SEV-4` per difetti non decision-critical.

Il runbook deve ridurre il tempo necessario per capire cosa fare, non documentare tutto ciò che sappiamo:

```text
symptom
→ affected product / tier
→ decision deadline
→ serving state
→ likely failure domains
→ checks
→ fallback
→ communication path
→ recovery / backfill
→ verification before re-certification
```

Questo è il contrario della memoria eroica. Un incidente non dovrebbe richiedere la persona che “sa dove guardare” perché l'ha risolto tre volte l'anno scorso.

## Postmortem e reliability review

Google SRE promuove postmortem blameless: lo scopo è capire quali condizioni del sistema hanno permesso il failure e trasformare l'incidente in miglioramento, non trovare il colpevole.

Fonte: https://sre.google/workbook/postmortem-culture/

Per un prodotto analitico chiediamo quando sia iniziato il problema, quando sia stato rilevato, se l'ha scoperto il sistema o l'utente, perché i gate non lo abbiano fermato, quale decisione fosse a rischio, se il degraded mode abbia funzionato, quanto sia durata la recovery e quale test, monitor o runbook debba cambiare.

A cadenza mensile o trimestrale, SLO attainment, error budget, incident severity, time-to-detect, time-to-recover, repeat incident e quota di problemi scoperti dagli utenti chiudono il ciclo **promessa → misura → deviazione → risposta → apprendimento**.

> **Un prodotto analitico affidabile non è quello che non fallisce mai. È quello che sa quale fallimento può tollerare, lo rende visibile prima che diventi una decisione sbagliata e degrada senza fingere che il dato sia più affidabile di quanto sia.**

Una volta che il prodotto sa dichiarare la propria affidabilità, possiamo affrontare il problema successivo: come permettere a più persone di usarlo senza costringerle a ricostruire da sole semantica, qualità e ownership.