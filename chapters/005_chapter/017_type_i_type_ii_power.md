## 5.16 Errori di tipo I, tipo II e power: decidere quanta evidenza comprare prima di agire

Un test di ipotesi può sbagliare in due direzioni. Nel linguaggio classico, commettiamo un **errore di tipo I** quando rifiutiamo `H0` mentre lo scenario nullo è vero; commettiamo un **errore di tipo II** quando non rifiutiamo `H0` pur essendo presente l'effetto specificato nell'alternativa.

Queste definizioni diventano davvero utili quando smettiamo di trattarle come caselle di una tabella scolastica e le traduciamo in **costi decisionali**.

## Un rollout da 4 milioni e due modi diversi di sbagliare

Una rete logistica valuta un nuovo processo di picking che richiede scanner, formazione e modifiche operative per circa **4 milioni di euro**.

Un falso positivo significa concludere che il nuovo processo produce il beneficio richiesto quando il segnale osservato era compatibile con il rumore sotto il modello: investiamo milioni senza ottenere il miglioramento atteso.

Un falso negativo significa invece non avere evidenza sufficiente quando il nuovo processo riduce davvero gli errori abbastanza da creare valore: perdiamo un'opportunità reale.

I due errori non hanno necessariamente lo stesso costo. Per questo `α = 0,05` e `power = 80%` non dovrebbero essere numeri rituali scelti perché “si usa così”. NIST definisce `α` come probabilità di errore di tipo I sotto `H0` e il power come probabilità di rifiutare `H0` quando l'alternativa specificata è vera; ricorda inoltre che l'errore di tipo II dipende dalla dimensione della discrepanza reale e aumenta, a parità di altre condizioni, quando rendiamo più severo `α`.[^nist-tests][^nist-type2]

La domanda progettuale diventa quindi:

> **Quanto costerebbe un falso positivo, quanto costerebbe un falso negativo e quale quantità di evidenza rende questi rischi accettabili?**

## Power rispetto a quale effetto?

La potenza statistica non è un'etichetta generica del tipo “questo esperimento ha power 80%”. Il power ha senso **rispetto a un effetto specificato**, oltre che a numerosità, variabilità, livello `α` e struttura del disegno.

Più piccolo è l'effetto che vogliamo distinguere, più informazione serve in genere. Questo è il motivo per cui la power analysis dovrebbe partire dal **Minimum Effect of Interest**: il più piccolo effetto che cambierebbe davvero la decisione.

Immaginiamo un prodotto digitale con conversione baseline del 3,0%. Il business considera interessante almeno **+0,15 punti percentuali**, fino a 3,15%. Dopo pochi giorni osserva 3,01% nel controllo e 3,19% nella variante, con 8.000 utenti per gruppo. Il risultato non supera il criterio inferenziale predefinito e il product manager conclude che “la variante non funziona”.

Questa conclusione sarebbe eccessiva se il test fosse stato avviato senza pianificazione della potenza e 8.000 utenti per gruppo fossero insufficienti per distinguere con affidabilità un delta dell'ordine di +0,15 pp.

La frase corretta è:

> **Il test corrente non contiene abbastanza informazione per discriminare bene l'effetto business-rilevante che avevamo in mente.**

“Non abbiamo rilevato” e “abbiamo dimostrato l'assenza” sono due stati epistemici diversi.

## Il Minimum Effect of Interest viene prima della sample size

Se il business non implementerebbe mai per un miglioramento inferiore a +0,5 pp, progettare un test enorme per trovare con precisione +0,05 pp può essere uno spreco di traffico e tempo. Se invece un delta di +0,05 pp vale milioni su una base enorme e i costi marginali sono bassi, lo stesso effetto può meritare un disegno molto più sensibile.

Il Capitolo 9 userà questa logica per MDE, durata, unità di randomizzazione, guardrail e stopping rules. Qui il punto è più generale: **la forza del test deve essere progettata rispetto alla decisione, non rispetto a una convenzione astratta**.

## Un risultato non significativo può raccontare storie diverse

La combinazione di effect size e precisione è spesso più informativa dell'etichetta `significant / not significant`.

| Evidenza | Effetto business-rilevante plausibile? | Lettura |
|---|---|---|
| Precisa e vicino a zero | No | Evidenza utile di effetto trascurabile |
| Imprecisa e vicino a zero | Sì | Inconclusivo: serve più informazione |
| Precisa e materialmente positivo | Sì | Evidenza forte da portare alla decisione |
| Imprecisa ma molto positivo | Sì | Segnale interessante, ancora incerto |

Questa matrice merita di restare strutturata perché impedisce una semplificazione frequente: trattare ogni `p > 0,05` come la stessa conclusione. Un intervallo stretto attorno a zero e un intervallo larghissimo che include effetti molto interessanti non hanno lo stesso significato decisionale.

> **Power non serve a garantire che troveremo un risultato significativo. Serve a evitare di fare una domanda importante con uno strumento troppo debole per risponderle.**

---

### Fonti

[^nist-tests]: NIST/SEMATECH, *Quantitative Techniques — Hypothesis Tests*. https://itl.nist.gov/div898/handbook/eda/section3/eda35.htm
[^nist-type2]: NIST/SEMATECH, *What are statistical tests?*. https://www.itl.nist.gov/div898/handbook/prc/section1/prc13.htm
