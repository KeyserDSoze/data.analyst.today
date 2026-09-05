## 5.11 Teorema del Limite Centrale: la normalità riguarda spesso la stima, non il dato grezzo

La sezione precedente ha introdotto lo standard error, cioè la dispersione della nostra stima tra possibili campioni. Il **Teorema del Limite Centrale** spiega perché, in molte condizioni, quella distribuzione delle stime assume una forma abbastanza regolare da rendere pratici intervalli e test.

In forma intuitiva: se prendiamo ripetutamente campioni della stessa dimensione e calcoliamo ogni volta la media, la distribuzione di quelle medie tende ad avvicinarsi a una forma normale al crescere di `n`, anche quando la distribuzione delle osservazioni originali non è normale. NIST riassume due proprietà centrali: la sampling distribution della media tende verso la normale e la sua deviazione standard si riduce come `σ / √n`.[^nist-clt]

La parola da proteggere è **sampling distribution**.

Il CLT non dice che i dati grezzi “diventano normali”. Dice che, in condizioni appropriate, una statistica aggregata come la media può avere una distribuzione campionaria molto più regolare dei valori individuali da cui è costruita.

## Ordini asimmetrici, medie più regolari

Un e-commerce di arredamento ha una distribuzione degli importi fortemente asimmetrica: moltissimi ordini tra 40 e 180 €, alcuni tra 600 e 1.500 €, pochi progetti completi tra 8.000 e 20.000 €.

Il singolo ordine è lontanissimo da una campana normale. Il CFO vuole però stimare l'AOV della popolazione attraverso campioni casuali. Se il team estrae ripetutamente campioni di 500 ordini e calcola ogni volta la media, quelle medie tendono a essere molto meno asimmetriche dei singoli importi.

Questo è il motivo per cui alcune procedure inferenziali sulla media possono funzionare anche quando il dato grezzo è irregolare. La giustificazione non è “i ricavi sono normali”; è che **la media campionaria ha una propria distribuzione**, diversa da quella dei ricavi individuali.

## Perché `n = 30` non è una legge naturale

La scorciatoia didattica “con 30 osservazioni possiamo assumere normalità” è troppo meccanica per il lavoro reale. La velocità con cui l'approssimazione diventa buona dipende dalla forma della popolazione, dall'asimmetria, dalle code pesanti, dalla presenza di eventi estremi e dalla quantità di dipendenza tra osservazioni.

Con dati relativamente regolari, poche decine di casi possono già produrre una sampling distribution della media abbastanza utilizzabile. Con fenomeni molto heavy-tailed o con una piccola quota di valori enormi, trenta osservazioni possono essere insufficienti. Non serve sostituire la vecchia soglia con un'altra. Serve chiedere **quanto è difficile il processo che stiamo mediando**.

## La dipendenza limita ciò che `n` può comprare

Il CLT classico non è una licenza per ignorare la struttura delle osservazioni. Un dataset con 10.000 click generati da 120 utenti contiene 10.000 righe, ma i click dello stesso utente possono essere fortemente correlati. Lo stesso accade con transazioni ripetute dello stesso cliente, misure dello stesso sensore, ordini dello stesso store o osservazioni consecutive nel tempo.

Se una procedura tratta ogni record come osservazione indipendente, può produrre standard error troppo piccoli e intervalli troppo ottimisti. La normalità della sampling distribution non corregge una definizione sbagliata dell'unità informativa.

È utile vedere il CLT per ciò che realmente offre: un ponte tra dati e distribuzione delle stime. Ci aiuta a costruire intervalli per una media, approssimazioni normali di statistiche aggregate e molti test inferenziali. Non corregge selection bias, non rende casuale un campione osservazionale e non elimina la dipendenza.

Questa formulazione è più utile della domanda scolastica “i miei dati sono normali?”. La domanda professionale diventa:

> **Quale statistica sto stimando, quale sampling distribution mi serve e le proprietà del campione rendono ragionevole l'approssimazione che sto usando?**

---

### Fonte

[^nist-clt]: NIST/SEMATECH, *Normal Distribution — Theoretical Justification: Central Limit Theorem*. https://www.itl.nist.gov/div898/handbook/eda/section3/eda3661.htm
