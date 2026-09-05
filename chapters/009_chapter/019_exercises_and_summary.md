## 9.18 Sintesi ed esercizi: progettare esperimenti che sopravvivono al mondo reale

Un A/B test non è **split → p-value → winner**. È una catena di affidabilità in cui la causalità creata dalla randomizzazione deve sopravvivere a identity, assignment, exposure, telemetria, metriche, durata, inferenza e rollout.

Il Capitolo 5 ci ha dato il linguaggio dell'incertezza. Il Capitolo 8 ci ha spiegato perché un assignment randomizzato può costruire un controfattuale. Questo capitolo ha aggiunto la parte che domina il lavoro reale: **verificare che il confronto progettato sulla carta sia ancora quello che abbiamo misurato in produzione e che la decisione finale rispetti le regole fissate prima di conoscere il risultato**.

La sequenza professionale è diventata:

**decisione → trattamento → popolazione → randomizzazione → exposure → telemetria → Metric Contract → Experiment Health Gate → inferenza → decision matrix → rollout → rollback/monitoring**.

Un SRM può sospendere la lettura dell'effetto. Una primary positiva può essere bloccata da un guardrail. Il sample size può essere sufficiente mentre il comportamento non è ancora maturo. CUPED può ridurre il rumore senza riparare un confronto selettivamente rotto. Una scorecard può contenere centinaia di metriche senza trasformarle tutte in prove confermative. Un test valido può produrre una ship candidate e scoprire soltanto durante il ramp un problema raro di scala o coverage.

Il deliverable del capitolo è l'**Experiment Contract**, che nasce prima del run e diventa il suo record storico. Insieme al **Health Gate** rende visibile una distinzione fondamentale: un risultato può essere favorevole, sfavorevole, inconclusivo oppure semplicemente **non interpretabile**. Questa quarta possibilità è una delle competenze più importanti di una cultura sperimentale matura.

> **Un esperimento affidabile non è quello che produce sempre una risposta netta. È quello in cui sappiamo distinguere una risposta netta da un sistema di misura che si è rotto, e sappiamo aumentare l'esposizione senza trasformare una vittoria locale in un rischio globale.**

Gli esercizi restano volutamente strutturati: qui la forma serve ad allenare l'applicazione del contract, non a esporre nuova teoria.

---

### Esercizio 1 — Conversione positiva, guardrail negativa

Un e-commerce testa un checkout semplificato.

| Metrica | Control | Treatment |
|---|---:|---:|
| conversione | 5,40% | 5,71% |
| contribution margin / eligible user | €1,82 | €1,86 |
| refund rate | 4,2% | 5,6% |
| contatti supporto / 1.000 ordini | 18 | 29 |

L'intervallo sulla conversione esclude zero. Nel contract, però, il refund rate non doveva peggiorare di oltre 0,5 pp.

Costruisci il verdetto finale separando risultato della primary, guardrail, decisione `SHIP CANDIDATE / REDESIGN / NO-SHIP`, informazione aggiuntiva necessaria e modifica da testare nella variante successiva. Non cercare una nuova metrica che faccia vincere B: applica la funzione decisionale definita prima.

---

### Esercizio 2 — SRM e missing selettivo

Un test configurato 50/50 produce 128.400 utenti control e 119.600 treatment. Il treatment sembra avere conversione inferiore del 4% relativo e la differenza di volumi è concentrata su Safari iOS.

Prepara un piano diagnostico distinguendo assignment, exposure, telemetry, filtering e analysis join. Poi assegna uno dei tre verdetti del Health Gate — **VALIDO / VALIDO CON CAVEAT / INVALIDO PER DECISIONE** — e spiega quali evidenze potrebbero cambiarlo.

---

### Esercizio 3 — Assignment, exposure ed estimand

Una nuova feature viene assegnata al 50% degli account B2B. Per un bug di configurazione solo il 62% degli account trattati la vede realmente; i mancati exposed sono soprattutto tenant legacy.

Spiega quale effetto misura una intention-to-treat sull'assignment, perché confrontare soltanto `exposed` vs `not exposed` può reintrodurre selection bias, quando l'eventuale esclusione dei tenant legacy dovrebbe essere definita e se ripeteresti il test dopo la correzione.

---

### Esercizio 4 — Marketplace e interferenza

Una piattaforma mette il 50% dei seller nel treatment con un nuovo algoritmo di pricing, ma tutti i buyer acquistano dagli stessi seller. Il trattamento modifica prezzi, disponibilità e capacità.

Progetta due alternative al semplice seller-level A/B: una basata su cluster geografici/mercati e una su switchback temporali. Per ognuna specifica unità di randomizzazione, rischio residuo di spillover, durata minima plausibile ed estimand business.

---

### Esercizio 5 — Sample size raggiunto in 30 ore

Una piattaforma ad altissimo traffico raggiunge il sample size pianificato in 30 ore e la primary è positiva. Il traffico weekend è però molto diverso, il nuovo flusso richiede apprendimento e refund/chargeback maturano in 7–14 giorni.

Spiega perché `sample size reached` non equivale a `experiment complete` e proponi un duration plan coerente con cicli temporali, learning/novelty e metric maturity.

---

### Esercizio 6 — Fixed horizon o sequential?

Il PM vuole controllare formalmente il test ogni giorno e fermarlo appena l'evidenza è sufficiente.

Costruisci due Experiment Contract: uno **fixed horizon**, con final read e safety monitoring separato, e uno **sequential**, con checkpoint, procedura compatibile con analisi ripetute e regola di stop. Spiega perché “guardiamo ogni giorno `p < 0,05`” non è equivalente al secondo.

---

### Esercizio 7 — A/A che mette in discussione la piattaforma

Un A/A su esperienze identiche mostra SRM su due browser, differenze persistenti su metriche revenue, il 28% delle metriche con segnali incompatibili con il false-positive rate atteso e un recente cambio di identity resolution.

Scrivi un experimentation incident brief: quali decisioni sospendi, quali layer indaghi per primi, come rivaluti gli esperimenti conclusi dopo il cambio di identity e quale gate usi per riaprire la piattaforma a decisioni di rollout.

---

### Esercizio 8 — CUPED non ripara un test rotto

Un team ottiene riduzione di varianza del 45% usando dati pre-esperimento. Il risultato aggiustato è molto preciso e positivo, ma il test mostra SRM e un bug di exposure su Android.

Spiega perché “CUPED ha corretto le differenze iniziali” è una conclusione sbagliata distinguendo variance reduction, selection introdotta dal bug, Health Gate e differenza tra precisione e validità.

---

### Esercizio 9 — Multiple metrics e discovery post-hoc

Un test ha 1 primary, 4 guardrail, 28 diagnostic metrics, 12 segmenti esplorati e 3 treatment. La primary è neutra; un segmento non predefinito mostra +9% su una diagnostic metric con p-value piccolo.

Classifica il risultato come confermativo, esplorativo o irrilevante e descrivi il test successivo necessario per trasformarlo in evidenza più forte.

---

### Esercizio 10 — Dal test al rollout

Un motore di raccomandazione supera il test sul 15% del traffico: contribution margin/session +1,8%, CTR +4,3%, latency P95 +22 ms, nessuna guardrail critica e Health Gate valido.

Al 70% di rollout la latency P99 cresce di 310 ms in una regione e il customer support load aumenta del 18%.

Decidi tra freeze, partial rollback, global rollback o continuazione al 100%, usando scale risk, coverage risk e rollback criteria senza dichiarare retroattivamente invalido il test iniziale.

---

### Esercizio 11 — Leadership meeting

Il CEO vede una slide: “Variant B +3,2% engagement — significativa al 95%. Raccomandazione: rollout globale.”

Scopri che retention D30 è -0,6 pp, notifiche inviate +19%, opt-out +24%, customer satisfaction non è ancora matura, il test è durato 9 giorni, engagement è stato scelto tra 17 metriche dopo aver visto i risultati e il contract originale indicava retention D30 come guardrail.

Scrivi un executive summary in sei righe con finding, Health Gate, problema di multiplicity/post-hoc selection, guardrail, decisione e prossimo test.

---

### Esercizio 12 — Costruisci l'Experiment Contract

Il team vuole testare una nuova politica di free shipping per utenti ad alto valore.

Costruisci il contract specificando almeno decisione, treatment, mechanism, eligibility, randomization/exposure/analysis unit, primary/OEC, guardrail, MDE business-relevant, durata, inference plan, segmenti confermativi, interference risk, Health Gate, decision matrix, rollout e rollback.

Poi immagina tre risultati possibili e applica la decision matrix **senza modificarla**.

### Autovalutazione

A fine capitolo dovresti riuscire a spiegare senza dashboard perché randomization, exposure e analysis unit possono differire; perché un SRM sospende la fiducia prima della significatività; perché una primary positiva può portare a NO-SHIP; perché sample size e durata rispondono a domande diverse; perché fixed horizon e sequential richiedono procedure diverse; che cosa CUPED migliora e che cosa non ripara; perché una scorecard ampia richiede gerarchia; quando cluster o switchback sono più vicini alla policy reale; a cosa serve un A/A; e perché il rollout resta una fase di measurement e risk management.

## Verso il Capitolo 10

Finora abbiamo costruito evidenza su **che cosa cambia quando assegniamo un trattamento**. Nel prossimo capitolo la domanda cambia di nuovo: non vogliamo più necessariamente intervenire in modo randomizzato, ma **anticipare quali casi futuri richiederanno una decisione**.

Questo cambio di obiettivo riproporrà molte discipline già viste. Anche un modello predittivo avrà una unità, un momento in cui l'informazione deve essere disponibile, un target, una baseline, una validazione fuori campione e una policy operativa. E come in questo capitolo, la complessità del modello non potrà compensare una definizione sbagliata del problema o dati che appartengono al futuro.

Il Capitolo 9 ci ha insegnato a preservare un confronto causale dalla randomizzazione al rollout. Il **Capitolo 10 — Regressione e modelli predittivi per Data Analyst** partirà dalla frontiera complementare: **prediction time → dati disponibili → score → azione**.
