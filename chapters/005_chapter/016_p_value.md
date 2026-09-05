## 5.15 Il p-value: una domanda stretta che non va trasformata in una sentenza

Il p-value è utile proprio perché risponde a una domanda ben delimitata. Diventa pericoloso quando gli attribuiamo significati che non contiene.

In termini operativi:

> **assumendo il modello statistico specificato, incluso lo scenario di `H0`, qual è la probabilità di ottenere una statistica almeno altrettanto estrema di quella osservata?**

Il p-value è quindi **condizionato al modello**. Non è la probabilità che il mondo funzioni in un certo modo, né la probabilità che l'ipotesi nulla sia vera.

L'American Statistical Association ha pubblicato una dichiarazione specifica sul tema proprio perché soglie e interpretazioni meccaniche avevano trasformato questo numero in qualcosa che la teoria non promette.[^asa-p]

## Quattro traduzioni che sembrano intuitive e sono sbagliate

Se leggiamo `p = 0,03`, non possiamo dire che esista il 97% di probabilità che l'ipotesi alternativa sia vera. Il p-value non è `P(H1 | dati)` e non è il complemento di `P(H0 | dati)`.

Non possiamo nemmeno dire che “c'è solo il 3% di probabilità che il risultato sia dovuto al caso”. Il test non divide il mondo in “caso” e “causa reale”: valuta quanto i dati siano estremi sotto un particolare modello nullo.

Allo stesso modo, `p = 0,18` non dimostra che l'effetto sia assente. Un risultato non piccolo può emergere perché l'effetto è realmente modesto, perché il campione contiene poca informazione, perché la variabilità è alta o perché il disegno è inefficiente.

Infine, `p < 0,05` non contiene alcuna istruzione del tipo “implementa”. Il p-value non conosce costo, margine, dimensione dell'effetto, guardrail o reversibilità. Il software statistico non ha accesso al business case.

Questi quattro errori hanno una radice comune: **si chiede al p-value di rispondere a domande che appartengono ad altri pezzi dell'evidenza**.

## `p = 0,03` e un progetto che distrugge valore

Un retailer testa un nuovo sistema di raccomandazione su circa 1,4 milioni di sessioni. L'AOV passa da 63,84 € a 63,97 €, quindi il delta è **+0,13 €**. Il confronto produce `p = 0,03`.

La frase “il nuovo algoritmo migliora significativamente l'AOV” è formalmente compatibile con il test, ma insufficiente per decidere.

L'implementazione costa 2 milioni di euro l'anno tra infrastruttura, licenze e manutenzione. Dopo resi, costi di serving e margine, il beneficio economico atteso è circa 480.000 €. Il segnale può essere statisticamente incompatibile con un effetto esattamente nullo e, contemporaneamente, essere un pessimo investimento.

La statistica ha risposto a una domanda sull'evidenza. L'economia deve ancora rispondere alla domanda sulla decisione.

## `0,049` e `0,051` non sono due universi opposti

La soglia `0,05` può essere parte di un piano di analisi predefinito, ma non è un confine naturale tra vero e falso. Due risultati con `p = 0,049` e `p = 0,051` sono quasi indistinguibili nella forza del segnale e non dovrebbero generare due storie epistemiche opposte.

L'ASA afferma esplicitamente che conclusioni scientifiche, di policy o di business non dovrebbero dipendere soltanto dal superamento di una soglia convenzionale.[^asa-p] Il punto non è abolire ogni criterio predefinito; è impedire la trasformazione automatica:

**numero continuo → etichetta vero/falso → decisione**.

## La numerosità può rendere “significativo” ciò che non conta

Il p-value dipende anche da quanta informazione possediamo. Consideriamo due confronti ipotetici sul churn:

| Confronto | n | Controllo | Variante | Delta assoluto |
|---|---:|---:|---:|---:|
| A | 2.000.000 | 8,000% | 7,950% | -0,05 pp |
| B | 1.200 | 8,0% | 6,4% | -1,6 pp |

Il confronto A può produrre un p-value più piccolo del B pur mostrando un effetto molto meno interessante per il business. Con milioni di osservazioni possiamo distinguere dallo zero differenze minuscole; con pochi casi possiamo osservare effetti grandi senza stimarli ancora con precisione.

Per questo **p-value, effect size e confidence interval devono viaggiare insieme**.

La dichiarazione ASA del 2016 può essere conservata come una checklist concettuale perché i suoi sei principi rispondono esattamente ai fraintendimenti più comuni:[^asa-p]

1. il p-value può indicare quanto i dati siano incompatibili con un modello statistico specificato;
2. non misura la probabilità che l'ipotesi studiata sia vera;
3. una decisione non dovrebbe dipendere soltanto da una soglia;
4. inferenza e reporting richiedono trasparenza;
5. il p-value non misura dimensione o importanza dell'effetto;
6. da solo non è una misura completa dell'evidenza.

Nel 2021 una task force dell'ASA ha ribadito un principio complementare: diverse misure di incertezza possono completarsi e nessuna singola misura serve a tutti gli scopi.[^asa-taskforce]

Un risultato inferenziale dovrebbe quindi assomigliare più a questo:

> **Effetto stimato:** +0,24 punti percentuali  
> **CI 95%:** +0,07 / +0,41 pp  
> **p-value:** 0,012  
> **Baseline:** 4,2%  
> **Soglia business rilevante:** +0,18 pp  
> **Principali caveat:** ...

che a una cella verde con scritto **SIGNIFICANT**.

La prima struttura permette di vedere dimensione del segnale, precisione, soglia economica e limiti non rappresentati dal test. Il p-value resta presente, ma torna alla dimensione corretta.

> **Il p-value è una coordinata dell'evidenza, non la destinazione.**

---

### Fonti

[^asa-p]: American Statistical Association, *Statement on Statistical Significance and P-Values*. https://www.amstat.org/asa/files/pdfs/p-valuestatement.pdf
[^asa-taskforce]: ASA President's Task Force, *Statement on Statistical Significance and Replicability*. https://magazine.amstat.org/blog/2021/08/01/task-force-statement-p-value/
