## 5.15 Il p-value: un numero utile che risponde a una domanda molto più stretta di quanto sembri

Il p-value è uno dei numeri più usati e più fraintesi dell'analisi quantitativa.

Una formulazione operativa corretta è:

> **assumendo il modello statistico specificato, incluso lo scenario di `H0`, qual è la probabilità di ottenere una statistica almeno altrettanto estrema di quella osservata?**

Questa definizione contiene già un avvertimento: il p-value è **condizionato al modello**. Non è una probabilità generale sulla verità del mondo.

L'American Statistical Association ha pubblicato una dichiarazione specifica proprio perché l'uso meccanico del p-value aveva generato interpretazioni scorrette in molti campi.[^asa-p]

### Quattro frasi da non dire

#### 1. “`p = 0,03`, quindi c'è il 97% di probabilità che l'ipotesi alternativa sia vera”

No.

Il p-value non è `P(H1 | dati)` e non è `1 - P(H0 | dati)`.

Per ottenere probabilità sulle ipotesi servirebbe un'impostazione diversa, per esempio bayesiana, con prior e modello espliciti.

#### 2. “`p = 0,03`, quindi c'è solo il 3% di probabilità che il risultato sia dovuto al caso”

Anche questa frase è sbagliata.

Il p-value non divide il mondo in “caso” e “causa reale”. Quantifica quanto il risultato sia estremo **sotto uno specifico modello nullo**.

#### 3. “`p = 0,18`, quindi non c'è effetto”

No.

Un p-value non piccolo può derivare da:

- effetto piccolo;
- campione insufficiente;
- rumore elevato;
- disegno inefficiente;
- dati compatibili con un intervallo molto ampio di effetti.

“Non abbiamo evidenza sufficiente per distinguere l'effetto dal rumore alle condizioni del test” è una frase molto diversa da “abbiamo dimostrato che l'effetto è zero”.

#### 4. “`p < 0,05`, quindi dobbiamo implementare”

No.

Il p-value non contiene:

- costo di implementazione;
- dimensione dell'effetto;
- margine;
- rischio operativo;
- guardrail;
- reversibilità della decisione.

Il software statistico non conosce il business case.

### Caso simulato/composito — `p = 0,03` e un progetto che distrugge valore

Un retailer testa un nuovo sistema di raccomandazione su circa 1,4 milioni di sessioni.

L'AOV passa:

- controllo: 63,84 €;
- nuovo sistema: 63,97 €;
- differenza: **+0,13 €**.

Il p-value sul confronto è `0,03`.

La prima slide dice:

> **“Il nuovo algoritmo migliora significativamente l'AOV.”**

La frase è incompleta.

L'implementazione costa 2 milioni di euro l'anno tra infrastruttura, licenze e manutenzione. Dopo resi, costi di serving e margine, il beneficio economico atteso è circa 480.000 €.

Il risultato può essere statisticamente incompatibile con un effetto esattamente nullo e contemporaneamente essere una pessima decisione economica.

### `0,05` non è un confine naturale tra vero e falso

Un risultato con:

- `p = 0,049`;
- `p = 0,051`;

non rappresenta due universi epistemici opposti.

L'ASA afferma esplicitamente che decisioni scientifiche, di policy o di business non dovrebbero essere basate soltanto sul superamento di una soglia convenzionale.[^asa-p]

La soglia può essere parte di un piano di analisi predefinito. Non deve diventare una trasformazione automatica:

**numero continuo → etichetta vero/falso**.

### La sample size modifica il p-value

Con campioni enormi possiamo ottenere p-value molto piccoli per differenze minuscole.

Con campioni piccoli possiamo osservare effetti materialmente grandi e non avere abbastanza informazione per distinguerli con precisione.

Consideriamo due confronti ipotetici sul churn:

| Confronto | n | Controllo | Variante | Delta assoluto |
|---|---:|---:|---:|---:|
| A | 2.000.000 | 8,000% | 7,950% | -0,05 pp |
| B | 1.200 | 8,0% | 6,4% | -1,6 pp |

Il confronto A può avere un p-value più piccolo del B pur mostrando un effetto molto meno interessante.

Per questo p-value e **effect size** devono essere letti insieme.

### Le sei idee dell'ASA tradotte per un Data Analyst

La dichiarazione ASA può essere condensata in sei regole operative:[^asa-p]

1. il p-value può indicare quanto i dati siano incompatibili con un modello statistico specificato;
2. non misura la probabilità che l'ipotesi studiata sia vera;
3. una decisione non dovrebbe dipendere soltanto da una soglia;
4. analisi e reporting devono essere trasparenti;
5. il p-value non misura dimensione o importanza dell'effetto;
6. da solo non è una misura completa dell'evidenza.

Per il nostro libro queste sei regole confluiscono in una sola:

> **Il p-value è una coordinata dell'evidenza, non la destinazione.**

### Cosa presentare invece di un p-value isolato

Un risultato inferenziale dovrebbe mostrare almeno:

> **Effetto stimato:** +0,24 punti percentuali  
> **CI 95%:** +0,07 / +0,41 pp  
> **p-value:** 0,012  
> **Baseline:** 4,2%  
> **Soglia business rilevante:** +0,18 pp  
> **Principali caveat:** ...

Questa struttura consente al lettore di capire:

- quanto è grande il segnale;
- quanto è preciso;
- come si confronta con ciò che conta economicamente;
- quale parte dell'incertezza non è rappresentata dal test.

È molto più informativa di una cella verde con scritto **SIGNIFICANT**.

[^asa-p]: American Statistical Association, *Statement on Statistical Significance and P-Values*: https://www.amstat.org/asa/files/pdfs/p-valuestatement.pdf
