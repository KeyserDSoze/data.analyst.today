## 19.8 Seniority nell'era AI: l'esecuzione accelera, l'esperienza no

L'AI non elimina la differenza tra junior e senior. Rende meno affidabile uno dei vecchi segnali con cui la osservavamo: **la quantità di esecuzione tecnica che una persona riesce a produrre senza assistenza**.

Query, codice, grafici, modelli baseline, documentazione e presentazioni possono essere generati molto più rapidamente di prima. Questo comprime una parte dell'attrito operativo, ma non comprime automaticamente l'esposizione a metriche ambigue, incidenti, stakeholder in conflitto, esperimenti falliti, dati incompleti, causal claim eccessivi, forecast sbagliati o rollout con effetti collaterali. La produzione può sembrare senior prima che lo sia il giudizio.

È più utile descrivere la seniority attraverso quattro **span di responsabilità**.

| Span | Domanda | Come cresce |
|---|---|---|
| Ambiguity span | quanto poco definito può essere il problema che riesco a strutturare? | da task con criteri chiari a decisioni come “la crescita è sana?” |
| Failure span | quanto costoso o nascosto è il failure mode che so anticipare? | da errori tecnici a semantic drift, leakage, causal overclaim, metric gaming e rollout irreversibili |
| Coordination span | quante dipendenze so orchestrare senza perdere accountability? | stakeholder, team, specialisti, owner semantici, agenti e decision owner |
| Decision span | quanto vicino so accompagnare l'evidenza alla scelta? | da output a alternative, policy, rollout e feedback loop |

Questi span spiegano meglio anche una progressione di carriera. Un junior dovrebbe costruire **task reliability**: eseguire problemi abbastanza definiti, controllare grain e denominatori, spiegare i propri controlli e sapere quando non è sicuro. Un mid-level cresce verso **problem ownership**, scegliendo metodi, formulando ipotesi, progettando verification e coordinando stakeholder. Un senior si sposta verso **decision e system ownership**: calibra claim e rischio, anticipa failure mode, decide che cosa non analizzare, orchestra persone e agenti, collega economics e rollout e rende il processo riusabile quando serve. A livello lead/principal il focus può diventare **organizational capability**: standard, operating model, metric governance, experimentation culture, agent governance e sviluppo delle persone.

Il punto non è trasformare questi livelli in una job ladder universale. È osservare che la seniority aumenta quando cresce la quantità di ambiguità e rischio che possiamo governare senza perdere rigore.

Immaginiamo un junior e un senior davanti alla stessa richiesta: “perché la conversion è scesa del 12%?”. Entrambi hanno accesso allo stesso agente, che produce SQL, breakdown geografico, segmentazione per device, grafici e cinque spiegazioni plausibili. Il junior sceglie l'ipotesi con correlazione più forte. Il senior controlla prima definizione e denominator, readiness, traffic mix, release/change log, timing e spiegazioni concorrenti.

L'indagine scopre che la definizione di conversion è cambiata due settimane prima, il paid traffic ha modificato il mix e una release è sovrarappresentata nel segmento residuo. Il vantaggio senior non è aver scritto più SQL. È aver riconosciuto **in quale ordine il sistema poteva ingannarlo**.

Questo crea un problema importante per l'apprendistato. Storicamente molte intuizioni venivano costruite attraversando pulizia, query semplici, debugging, reconciliation, reporting e code review. Se l'AI assorbe tutta questa superficie immediatamente, un junior può produrre output senior-looking senza avere ancora incontrato abbastanza failure mode. È una **experience compression apparente**: l'output accelera, l'esperienza no.

La risposta non è conservare lavoro inutile. Obbligare qualcuno a copiare CSV per mesi non crea automaticamente judgment. Serve invece progettare esposizione deliberata ai punti in cui il lavoro rompe: query AI con bug nascosti, metric-definition exercise, shadowing di data incident, causal claim critique, experiment review, forecast stress test, postmortem, Decision Record e agent-eval failure analysis. Meno ripetizione senza feedback; più contatto intenzionale con errori che richiedono un modello mentale.

Anche la review deve evolvere in questo modo. All'inizio può essere profonda: leggere SQL completo, ricostruire il denominator, spiegare il join, verificare il sample, replicare un risultato. Con l'esperienza può diventare più risk-based. Ma quella riduzione della review dovrebbe essere una **compressione conquistata**, non fiducia concessa perché il sistema produce output plausibili da molto tempo.

Infine, seniority non significa sapere tutto. Sapere dire “qui non ho sufficiente profondità” e coinvolgere statistica, Security, Legal/Privacy, ML Engineering, Finance o un domain expert è parte del failure span. L'escalation corretta protegge il sistema proprio dove la nostra competence boundary finisce.

> **Nell'era AI la seniority si misura sempre meno da quanto lavoro sappiamo eseguire da soli e sempre più da quanta ambiguità, rischio e responsabilità sappiamo governare senza perdere il controllo su significato ed evidenza.**