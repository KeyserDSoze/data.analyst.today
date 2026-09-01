## 9.18 Sintesi ed esercizi: progettare esperimenti che sopravvivono al mondo reale

Un A/B test non è:

**split → p-value → winner.**

È una catena di affidabilità:

**decisione → trattamento → popolazione → randomizzazione → exposure → telemetria → metrica → health gate → inferenza → decisione → rollout.**

Ogni anello può modificare la conclusione.

Il Capitolo 5 ci ha insegnato a leggere effect size, intervalli, Type I/II error, power e multiple testing. Il Capitolo 8 ci ha insegnato perché un confronto randomizzato può identificare un effetto causale. Questo capitolo aggiunge il problema che domina la pratica: **far sì che il confronto progettato sulla carta sia ancora quello che abbiamo davvero misurato in produzione**.

### Le cinque domande finali

Prima di approvare un esperimento importante dovremmo riuscire a rispondere, nell'ordine:

1. **Il contract era sensato?** — treatment, popolazione, metrica e soglie rappresentavano davvero la decisione?
2. **L'esperimento è sano?** — assignment, exposure e telemetria hanno conservato il confronto?
3. **Che cosa abbiamo stimato?** — effect size, uncertainty e scope sono coerenti con il piano?
4. **L'effetto vale abbastanza e non costa troppo altrove?** — primary/OEC e guardrail producono una decisione economicamente sensata?
5. **Possiamo aumentare l'esposizione in sicurezza?** — rollout, coverage e rollback gestiscono il rischio residuo?

Il deliverable operativo del capitolo è l'**Experiment Contract**, che nasce prima del test e diventa il record finale dell'esperimento.

> **Un esperimento affidabile non è quello che produce una risposta netta. È quello in cui sappiamo distinguere una risposta netta da un sistema di misura che si è rotto.**

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

Costruisci il verdetto finale separando:

- risultato della primary;
- guardrail;
- decisione `SHIP CANDIDATE / REDESIGN / NO-SHIP`;
- informazione aggiuntiva necessaria;
- modifica che testeresti nella variante successiva.

L'obiettivo non è trovare una nuova metrica che faccia vincere B. È rispettare la funzione decisionale definita prima.

---

### Esercizio 2 — SRM e missing selettivo

Un test configurato 50/50 produce:

- control: 128.400 utenti;
- treatment: 119.600 utenti.

Il treatment sembra anche avere conversione inferiore del 4% relativo.

L'indagine preliminare mostra che la differenza di volumi è concentrata su Safari iOS.

Prepara un piano diagnostico distinguendo:

1. assignment;
2. exposure;
3. telemetry;
4. filtering;
5. analysis join.

Poi assegna uno dei tre verdetti del Health Gate:

**VALIDO / VALIDO CON CAVEAT / INVALIDO PER DECISIONE**.

Spiega quali evidenze servirebbero per cambiare verdetto.

---

### Esercizio 3 — Assignment, exposure e estimand

Una nuova feature viene assegnata al 50% degli account B2B. Per un bug di configurazione solo il 62% degli account trattati la vede realmente.

Gli utenti che non la vedono sono soprattutto tenant con una versione legacy del prodotto.

Rispondi:

- quale effetto misura un'analisi intention-to-treat sull'assignment?
- perché confrontare soltanto `exposed` vs `not exposed` può reintrodurre selection bias?
- la popolazione legacy dovrebbe essere esclusa, e se sì in quale momento della definizione?
- ripeteresti il test dopo la correzione?

L'obiettivo è separare **problema di prodotto**, **problema di delivery del trattamento** e **problema di analisi**.

---

### Esercizio 4 — Marketplace e interferenza

Una piattaforma mette il 50% dei seller nel treatment con un nuovo algoritmo di pricing, ma tutti i buyer acquistano dagli stessi seller.

Il trattamento modifica prezzi, disponibilità e capacità dei seller.

Progetta due alternative al semplice seller-level A/B:

- una basata su cluster geografici/mercati;
- una basata su switchback temporali.

Per ognuna specifica:

- unità di randomizzazione;
- principale rischio residuo di spillover;
- durata minima plausibile;
- quale effetto business stai cercando di stimare.

---

### Esercizio 5 — Il test che raggiunge il sample size in 30 ore

Una piattaforma ad altissimo traffico raggiunge il sample size pianificato in 30 ore. Il risultato sulla primary è positivo.

Sappiamo però che:

- il traffico weekend è molto diverso;
- il nuovo flusso richiede apprendimento;
- refund e chargeback maturano in 7–14 giorni.

Spiega perché `sample size reached` non equivale a `experiment complete` e proponi una durata minima coerente con:

- cicli temporali;
- learning/novelty;
- metric maturity.

---

### Esercizio 6 — Peeking o sequential design?

Il PM vuole controllare formalmente il test ogni giorno e fermarlo appena l'evidenza è sufficiente.

Costruisci due Experiment Contract alternativi:

**A. Fixed horizon**  
Definisci durata, momento di analisi finale e safety monitoring consentito durante il test.

**B. Sequential design**  
Definisci checkpoint, procedura compatibile con analisi ripetute e regola di stop.

Spiega perché "guardiamo ogni giorno `p < 0,05`" non è equivalente alla seconda strategia.

---

### Esercizio 7 — A/A che mette in discussione la piattaforma

Un A/A test su esperienze identiche mostra:

- SRM su due browser;
- differenze persistenti su metriche revenue;
- 28% delle metriche con segnali incompatibili con il false-positive rate atteso;
- un cambio recente nel sistema di identity resolution.

Scrivi un incident brief di experimentation:

- quali decisioni sospenderesti?
- quali layer indagheresti per primi?
- come valuteresti gli esperimenti già conclusi dopo il cambio di identity?
- quale criterio useresti per riaprire la piattaforma a decisioni di rollout?

---

### Esercizio 8 — CUPED non ripara un test rotto

Un team ottiene una riduzione di varianza del 45% usando dati pre-esperimento. Il risultato aggiustato è molto preciso e positivo.

Contemporaneamente il test mostra SRM e un bug di exposure su Android.

Il PM sostiene:

> "CUPED ha corretto le differenze iniziali, quindi possiamo fidarci del risultato."

Spiega perché questa conclusione è sbagliata distinguendo:

- variance reduction;
- confounding/selection introdotta dal bug;
- health gate;
- precisione vs validità.

---

### Esercizio 9 — Multiple metrics e scoperta post-hoc

Un test ha:

- 1 primary;
- 4 guardrail;
- 28 diagnostic metrics;
- 12 segmenti esplorati;
- 3 varianti treatment.

La primary è neutra. Un segmento non predefinito mostra +9% su una diagnostic metric con p-value piccolo.

Classifica il risultato come:

- confermativo;
- esplorativo;
- irrilevante.

Poi descrivi il test successivo necessario per trasformare quel pattern in evidenza più forte.

---

### Esercizio 10 — Dal test al rollout

Un motore di raccomandazione supera il test sul 15% del traffico:

- contribution margin/session +1,8%;
- CTR +4,3%;
- latency P95 +22 ms;
- nessuna guardrail critica;
- Health Gate: valido.

Al 70% di rollout la latency P99 cresce di 310 ms in una regione e il customer support load aumenta del 18%.

Decidi tra:

- freeze;
- partial rollback;
- global rollback;
- continuazione al 100%.

Motiva la scelta usando **scale risk, coverage risk e rollback criteria**, senza dichiarare retroattivamente che l'esperimento iniziale fosse necessariamente invalido.

---

### Esercizio 11 — Leadership meeting

Il CEO vede una slide:

> "Variant B +3,2% engagement — significativa al 95%. Raccomandazione: rollout globale."

Hai venti minuti per correggerla. Scopri che:

- engagement +3,2%;
- retention D30 -0,6 pp;
- notifiche inviate +19%;
- opt-out notifiche +24%;
- customer satisfaction non ancora matura;
- test durato 9 giorni;
- engagement è stato scelto tra 17 metriche dopo aver visto i risultati;
- il contract originale indicava retention D30 come guardrail.

Scrivi un executive summary in sei righe contenente:

1. finding;
2. stato del Health Gate;
3. problema di multiplicity/post-hoc selection;
4. guardrail;
5. decisione;
6. prossimo test.

---

### Esercizio 12 — Costruisci l'Experiment Contract

Il team vuole testare una nuova politica di free shipping per utenti ad alto valore.

Costruisci da zero il contract specificando almeno:

- decisione;
- treatment;
- mechanism;
- eligibility;
- randomization/exposure/analysis unit;
- primary/OEC;
- guardrail;
- MDE business-relevant;
- durata;
- inference plan;
- segmenti confermativi;
- interference risks;
- Health Gate;
- decision matrix;
- rollout e rollback.

Poi prova a immaginare tre risultati possibili e applica la decision matrix senza modificarla.

### Autovalutazione

Alla fine del capitolo dovresti riuscire a spiegare con parole semplici:

- perché randomization unit, exposure unit e analysis unit possono differire;
- perché un SRM è un problema di fiducia prima che di significatività;
- perché una primary positiva può portare a NO-SHIP;
- perché raggiungere il sample size non garantisce durata sufficiente;
- perché un fixed-horizon test e un sequential test richiedono regole diverse;
- che cosa CUPED migliora e che cosa non può riparare;
- perché multiple metrics richiedono gerarchia e controllo della molteplicità;
- quando cluster o switchback sono preferibili alla randomizzazione individuale;
- a cosa serve un A/A test;
- perché il rollout è una fase di measurement e risk management;
- quali elementi devono essere congelati nell'Experiment Contract.

Se queste risposte sono chiare, l'A/B testing ha smesso di essere una procedura statistica isolata. È diventato una capacità organizzativa per produrre **evidenza causale verificabile e decisioni reversibili**.
