## 5.4 Distribuzioni di probabilità: descrivere non solo il centro, ma gli esiti possibili

Una probabilità singola risponde bene a domande del tipo “quanto spesso accade questo evento?”. Molte decisioni richiedono però qualcosa di più: sapere **quali esiti sono possibili, come si distribuisce il loro peso e quanto è plausibile arrivare nelle code**.

Una distribuzione di probabilità serve a questo. Non è una curva con un nome da riconoscere a memoria; è un modello compatto del processo incerto. Ci permette di chiedere quanto sia probabile superare una soglia, quanto possa oscillare un conteggio attorno al valore atteso o quale downside dobbiamo essere in grado di assorbire.

NIST ricorda che le distribuzioni sono usate sia per modellare dati sia come base di intervalli e test, e che le assunzioni distributive devono essere abbastanza adeguate da rendere valide le conclusioni della procedura.[^nist-distributions]

## “Ci aspettiamo 250 conversioni” non significa che ne avremo 250

Un marketplace invia una campagna a 10.000 clienti. Per una popolazione comparabile il conversion rate storico è 2,5%, quindi il valore atteso è:

`10.000 × 2,5% = 250 conversioni`.

Per capire quanto possa oscillare il risultato dobbiamo dichiarare un modello. Se assumiamo che ogni cliente produca due esiti rilevanti, conversione o non conversione, che la probabilità sia approssimativamente costante e che le prove siano sufficientemente indipendenti, il numero di conversioni può essere rappresentato con una **binomiale**:

`X ~ Binomiale(n = 10.000, p = 0,025)`.

NIST definisce la binomiale proprio come il modello del numero di successi in `n` prove con due esiti e probabilità `p` costante.[^nist-binomial]

Nel nostro caso il valore atteso è 250 e la deviazione standard è circa 15,6 conversioni. Osservarne 236 significa essere sotto l'atteso, ma non autorizza ancora a dire che la campagna sia “rotta”. Prima dobbiamo confrontare lo scarto con la variabilità che il modello considera normale.

La frase professionale non è quindi “abbiamo mancato il target di 14 conversioni”, ma:

> **Quanto è insolito 236 rispetto alla distribuzione degli esiti che ci aspetteremmo se il processo fosse rimasto quello modellato?**

## Il nome della distribuzione è un contratto di assunzioni

Nella campagna reale, naturalmente, le condizioni binomiali possono essere soltanto approssimative. I clienti possono avere propensioni molto diverse, appartenere alla stessa azienda o influenzarsi tra loro; l'invio può avvenire in momenti differenti; segmenti diversi possono reagire diversamente all'offerta.

Questo non rende automaticamente inutile il modello. Significa che dobbiamo sapere **quale semplificazione stiamo comprando** quando scegliamo quella distribuzione.

La stessa disciplina vale per altri modelli comuni. Una Bernoulli rappresenta un singolo esito sì/no; una binomiale conta successi su un numero di prove; una Poisson può essere utile per conteggi di eventi su una certa esposizione sotto condizioni appropriate. La tabella seguente vale quindi come mappa, non come motore di scelta automatica:

| Processo | Modello possibile | Domanda |
|---|---|---|
| singolo esito sì/no | Bernoulli | accade oppure no? |
| successi su `n` prove | Binomiale | quanti successi? |
| eventi su tempo/spazio/esposizione | Poisson, se le assunzioni reggono | quanti eventi? |
| sampling distribution / errori | Normale, in molte condizioni | quanto oscilla una stima? |

## La normale è importante soprattutto dove serve davvero

La distribuzione normale occupa un posto centrale nella statistica, ma viene spesso cercata nel posto sbagliato. Importi di ordine, lifetime value, tempi di attesa e revenue per cliente possono essere fortemente asimmetrici o avere code pesanti e non c'è alcun motivo di “normalizzarli” soltanto perché molte formule classiche usano la normale.

Il punto che ci servirà tra poco è diverso: **la distribuzione dei dati originali e la distribuzione di una statistica campionaria non sono la stessa cosa**. NIST collega l'importanza della normale anche al Central Limit Theorem: in molte condizioni, al crescere del campione la distribuzione della media campionaria diventa approssimativamente normale anche quando la variabile di partenza non lo è.[^nist-normal]

Quindi un AOV individuale può essere fortemente asimmetrico mentre la distribuzione delle medie su campioni abbastanza grandi diventa molto più regolare. Questa distinzione ci permetterà di costruire intervalli senza fingere che ogni ordine del mondo segua una campana.

## Quando la coda vale più della media

Consideriamo una compagnia assicurativa con moltissimi sinistri da poche centinaia di euro e pochi sinistri estremamente costosi. La perdita media può essere 1.850 €, ma la decisione su riserve e capitale dipende soprattutto dalla probabilità della **coda destra**.

Un modello che riproduce bene la media e sottostima drasticamente gli eventi estremi può essere peggiore, per quella decisione, di un modello meno elegante ma più realistico sulle code. La bontà del modello è quindi sempre **fit for purpose**, come la data quality del Capitolo 3.

> **Una distribuzione non è un'etichetta da assegnare ai dati. È una dichiarazione sugli esiti possibili e sul meccanismo che li rende più o meno plausibili.**

---

### Fonti

[^nist-distributions]: NIST/SEMATECH, *Probability Distributions*. https://www.itl.nist.gov/div898/handbook/eda/section3/eda36.htm
[^nist-binomial]: NIST/SEMATECH, *Binomial Distribution*. https://itl.nist.gov/div898/handbook/eda/section3/eda366i.htm
[^nist-normal]: NIST/SEMATECH, *Normal Distribution*. https://www.itl.nist.gov/div898/handbook/eda/section3/eda3661.htm
