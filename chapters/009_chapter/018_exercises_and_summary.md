## 9.18 Sintesi ed esercizi: progettare esperimenti che sopravvivono al mondo reale

L'A/B testing viene spesso presentato come una procedura semplice:

1. dividi gli utenti;
2. mostra due versioni;
3. confronta una metrica;
4. guarda il p-value;
5. scegli il vincitore.

Questa versione è utile per imparare il meccanismo di base, ma è insufficiente per lavorare bene.

Nel mondo reale bisogna gestire:

- randomizzazione;
- unità di assegnazione;
- esposizione;
- identità utente;
- sample size;
- power;
- MDE;
- guardrail;
- multiple metrics;
- multiple variants;
- Sample Ratio Mismatch;
- peeking;
- novelty effect;
- learning effect;
- spillover;
- network effects;
- rollout progressivo;
- rollback;
- qualità della telemetria.

La statistica è solo una parte del sistema.

### Una formula mentale utile

Prima di fidarti di un risultato, chiedi:

**Esperimento sano → confronto valido → effetto credibile → effetto utile → rollout sicuro**

Se uno di questi passaggi fallisce, il fatto che una metrica abbia `p < 0.05` non salva la decisione.

---

## Esercizio 1 — Il nuovo checkout vince davvero?

Un e-commerce testa un checkout semplificato.

| metrica | control | treatment |
|---|---:|---:|
| conversione | 5,40% | 5,71% |
| AOV | €82,10 | €80,90 |
| refund rate | 4,2% | 5,6% |
| contatti supporto / 1.000 ordini | 18 | 29 |

La conversione è statisticamente significativa con `p = 0,018`.

Domande:

1. dichiareresti il test vinto?
2. quale metrica primaria avresti preferito definire prima?
3. quali guardrail cambiano la decisione?
4. calcoleresti revenue lorda o revenue netta?
5. quale rollout proporresti?

---

## Esercizio 2 — SRM dopo cinque giorni

Un test 50/50 produce:

- control: 128.400 utenti;
- treatment: 119.600 utenti.

Domande:

1. perché non dovresti analizzare subito il risultato business?
2. quali possibili cause tecniche indagheresti?
3. cosa controlleresti per device, browser e versione app?
4. cosa succede se gli utenti mancanti appartengono soprattutto a un segmento ad alta conversione?

---

## Esercizio 3 — Marketplace e network effect

Una piattaforma mette il 50% dei seller nel treatment con un nuovo algoritmo di pricing, ma buyer control e treatment acquistano dagli stessi seller.

Domande:

1. qual è il rischio di contaminazione?
2. l'unità seller è davvero appropriata?
3. come ridisegneresti l'esperimento?
4. useresti cluster geografici, mercati o finestre temporali?
5. quali effetti indiretti vorresti misurare?

---

## Esercizio 4 — Peeking

Dopo quattro giorni un test mostra `p = 0,032`. Il PM vuole interromperlo. Il piano originale prevedeva 21 giorni.

Dopo 10 giorni il p-value sale a 0,11.

Domande:

1. quale errore di processo è stato commesso?
2. perché il p-value può oscillare?
3. quali alternative corrette esistono?
4. quando sarebbe comunque legittimo fermare il test prima?

---

## Esercizio 5 — A/A test che fallisce

Un A/A test su due esperienze identiche mostra movimenti statisticamente significativi su 28% delle metriche, molte con `p < 0,001`.

Domande:

1. è plausibile attribuire tutto al caso?
2. quali layer del sistema controlleresti?
3. cosa significa per gli esperimenti già eseguiti sulla stessa piattaforma?
4. bloccheresti temporaneamente le decisioni di rollout?

---

## Esercizio 6 — Rollout progressivo

Un nuovo motore di raccomandazione supera il test su 15% del traffico:

- CTR +4,3%;
- revenue/session +1,8%;
- latency P95 +22 ms;
- nessuna guardrail critica.

Al 70% di rollout, la latency P99 cresce di 310 ms su utenti di una regione specifica.

Domande:

1. perché il test iniziale non necessariamente era sbagliato?
2. quale rischio si è materializzato?
3. rollback totale o parziale?
4. quali segmenti dovevano essere analizzati prima?
5. come documenteresti la decisione?

---

## Esercizio 7 — Caso da leadership meeting

Il CEO vede una slide:

> "Variant B +3,2% engagement — significativa al 95%. Raccomandazione: rollout globale."

Hai venti minuti prima della riunione.

Le informazioni aggiuntive sono:

- engagement +3,2%;
- retention D30 -0,6 pp;
- notifiche inviate +19%;
- opt-out notifiche +24%;
- session duration +7%;
- customer satisfaction non ancora disponibile;
- test durato 9 giorni;
- la metrica engagement è stata scelta tra 17 metriche dopo aver visto i risultati.

Scrivi una nuova conclusione executive separando:

1. ciò che sappiamo;
2. ciò che non possiamo concludere;
3. i rischi metodologici;
4. la decisione consigliata;
5. il prossimo esperimento.

---

## Autovalutazione

Dovresti essere in grado di rispondere senza formule complesse:

- Perché l'unità di randomizzazione è una scelta causale e non tecnica?
- Che differenza c'è tra assignment ed exposure?
- Perché un SRM può invalidare un test?
- Perché una metrica significativa può essere economicamente irrilevante?
- Perché multiple metrics aumentano il rischio di false discovery?
- Quando CUPED può aumentare la sensibilità?
- Perché marketplace e social product richiedono attenzione agli spillover?
- Perché un A/A test è utile?
- Che differenza c'è tra un test vinto e un rollout sicuro?
- Cosa dovrebbe contenere il documento finale di un esperimento?

Se queste risposte sono chiare, l'A/B testing non è più una ricetta statistica: è diventato un sistema per prendere decisioni causali in condizioni di incertezza.
