## 5.20 Uncertainty Brief: consegnare una stima senza nascondere ciò che non sappiamo

Il Capitolo 5 non dovrebbe lasciarci con una collezione di formule. Dovrebbe aggiungere un artefatto alla catena professionale costruita fin qui:

**Analytical Brief → Data Readiness Review → EDA Evidence Map → Uncertainty Brief**.

L'Analytical Brief stabilisce che cosa vogliamo sapere e perché. La Data Readiness Review verifica se il dato rappresenta abbastanza bene quel fenomeno. La EDA Evidence Map descrive la struttura osservata senza trasformarla prematuramente in spiegazione. L'**Uncertainty Brief** aggiunge l'ultimo livello: rende esplicito quanto bene conosciamo la stima, fino a quale popolazione possiamo generalizzarla, quali assunzioni rendono valido il metodo, quali bias rimangono fuori dall'intervallo e quale dimensione dell'effetto cambierebbe davvero la decisione.

Non è un nuovo documento da compilare per burocrazia. È il modo per impedire che, nella consegna finale, tutta la disciplina costruita durante l'analisi venga compressa in un numero e una cella verde.

## Il template operativo

```text
DOMANDA INFERENZIALE
Quale parametro, differenza o rischio stiamo cercando di stimare?

POPOLAZIONE TARGET
Su chi o su che cosa vogliamo generalizzare?

DATI / DISEGNO
Come sono entrate le osservazioni nel campione?
Qual è la numerosità informativa reale?

STIMA
Qual è il valore o effect size osservato?

PRECISIONE
Standard error / confidence interval appropriato.

MODELLO E ASSUNZIONI
Indipendenza? Distribuzione? Unità di analisi? Sampling design?

BIAS NON CONTENUTI NELL'INTERVALLO
Selection, nonresponse, measurement, drift, definizioni, confounding...

TEST, SE UTILE
H0, p-value e criterio pre-specificato.

POWER / INFORMATIVITÀ
Il disegno era capace di distinguere l'effetto che ci interessa?

MOLTEPLICITÀ
Quante metriche, segmenti o specificazioni sono state esplorate?

SOGLIA BUSINESS
Qual è il più piccolo effetto che cambierebbe davvero la decisione?

CONCLUSIONE CALIBRATA
Che cosa sostengono i dati? Che cosa non sostengono?

PROSSIMO PASSO
Agire, raccogliere altri dati, confermare, sperimentare o fermarsi?
```

Per un'analisi semplice questa struttura può occupare mezza pagina. Per una decisione ad alto rischio può diventare una review più profonda. La quantità di documentazione deve seguire la stessa logica della quantità di evidenza: **più forte è la decisione che vogliamo sostenere, più chiaramente dobbiamo rendere visibili le condizioni che rendono forte o fragile la conclusione**.

## Un 74% che non può essere consegnato da solo

Immaginiamo una survey customer success sui clienti enterprise attivati nel trimestre. La survey viene inviata a 4.800 clienti e ottiene 1.120 risposte. Il 74% dei rispondenti esprime un CSAT positivo; sotto assunzioni semplici il confidence interval di campionamento è circa 71%–77%. Il rollout richiede evidenza ragionevole che il CSAT sia almeno 70%.

Fermarsi qui produrrebbe una frase molto rassicurante: “CSAT 74%, circa ±3 punti, quindi siamo sopra target”.

Ma il disegno contiene un'informazione che l'intervallo non incorpora: i clienti con onboarding fallito rispondono meno frequentemente. Il 74% può quindi essere una stima abbastanza precisa tra i rispondenti e, nello stesso tempo, sovrastimare la soddisfazione della popolazione target.

L'Uncertainty Brief renderebbe la conclusione più calibrata:

```text
DOMANDA
Qual è la quota di clienti enterprise soddisfatti del nuovo onboarding?

POPOLAZIONE TARGET
Clienti enterprise attivati nel trimestre.

DISEGNO
Survey inviata a 4.800 clienti; 1.120 risposte.
Risposta volontaria, quindi possibile nonresponse bias.

STIMA
CSAT positivo: 74%.

PRECISIONE
CI 95% da campionamento, sotto assunzioni semplici: circa 71%–77%.

BIAS NON NEL CI
I clienti con onboarding fallito rispondono meno frequentemente.

SOGLIA BUSINESS
Il rollout richiede evidenza ragionevole che il CSAT sia almeno 70%.

CONCLUSIONE
La stima osservata supera il target e il CI di campionamento è prevalentemente sopra 70%,
ma la sottorappresentazione dei clienti con onboarding problematico può produrre bias positivo.
Non presentiamo quindi il 74% come stima definitiva dell'intera popolazione.

PROSSIMO PASSO
Collegare survey e dati operativi, aumentare follow-up dei nonrespondent e fare sensitivity analysis.
```

La differenza non è soltanto più cautela. È **più informazione sulla decisione**: sappiamo quale incertezza è piccola e quale rimane invece il vero limite dell'evidenza.

## La tesi del capitolo

Abbiamo iniziato distinguendo la variabilità del processo dall'incertezza della stima. Da lì il percorso ha seguito una sola domanda: **quanto deve essere forte la conclusione rispetto all'informazione che possediamo?**

La probabilità ci ha obbligato a definire l'evento e a modellare gli esiti possibili. La probabilità condizionata ha mostrato che il rischio cambia quando cambia il denominatore; l'indipendenza che molte formule incorporano assunzioni sul processo; le distribuzioni e il valore atteso che una media nasconde code e rischio. La legge dei grandi numeri ha poi separato la riduzione del rumore dalla correzione del bias, aprendo il problema del campionamento.

Da quel punto la stima è diventata una delle molte realizzazioni possibili del processo di raccolta. Sampling distribution, standard error e Central Limit Theorem hanno spiegato perché possiamo quantificare la precisione; il confidence interval ha reso quella precisione visibile; la sample size l'ha trasformata in una decisione sul valore dell'informazione.

Infine abbiamo visto perché il test non deve diventare una sentenza. Il p-value risponde a una domanda stretta dentro un modello; power e errori di tipo I e II rendono esplicito il costo di non avere abbastanza evidenza o di agire su un falso segnale; effect size e soglia business separano precisione e materialità; multiple testing ricorda che anche **il modo in cui abbiamo cercato il risultato** fa parte della sua evidenza.

Questa progressione porta a poche distinzioni che devono diventare automatiche. Più dati non significa automaticamente dati migliori. Deviazione standard e standard error descrivono due livelli diversi di variabilità. Un intervallo di confidenza non contiene tutti gli errori possibili. Un p-value non è la probabilità che `H0` sia vera. “Non significativo” non equivale a “nessun effetto”, così come “significativo” non equivale a “effetto importante”. E una scoperta trovata dopo cento tentativi non possiede la stessa forza confermativa di un'ipotesi specificata prima di guardare i dati.

> **Una buona analisi non elimina l'incertezza. La misura abbastanza bene da impedire alla conclusione di essere più sicura dei dati.**

Il Capitolo 6 applicherà questa disciplina a segmentazione, coorti, funnel e retention. Lì i denominatori si assottigliano rapidamente: una cella di cohort table può passare da migliaia a poche decine di utenti, e una curva apparentemente diversa può essere sostenuta da pochissima informazione. L'Uncertainty Brief non resterà quindi alle nostre spalle; diventerà il modo in cui leggiamo ogni differenza di lifecycle senza trasformare il colore di una heatmap in certezza.

## Esercizi

### Esercizio 1 — Il milione di risposte

Una piattaforma raccoglie un milione di rating volontari e ottiene soddisfazione del 92,4% con un intervallo di campionamento strettissimo.

Sai però che solo gli utenti che completano almeno cinque sessioni vedono la survey.

Costruisci un Uncertainty Brief. Spiega perché aumentare ancora il numero di risposte non risolve il problema principale.

### Esercizio 2 — Stima precisa ma irrilevante

Un cambiamento riduce il churn da 6,000% a 5,970% su 8 milioni di clienti.

La stima è molto precisa e il p-value è minuscolo.

Quali numeri economici servono prima di decidere? Scrivi una conclusione che non usi le parole “vince” o “funziona”.

### Esercizio 3 — Effetto importante ma test debole

Un prodotto B2B osserva:

- controllo: churn 7,2%;
- trattamento: 5,9%;
- 430 clienti per gruppo;
- intervallo molto ampio;
- `p = 0,19`.

Scrivi tre conclusioni:

1. una sbagliata che confonde non-significativo con effetto zero;
2. una tecnicamente corretta;
3. una conclusione decisionale che consideri anche il valore potenziale dell'effetto e il costo di raccogliere nuovi dati.

### Esercizio 4 — Il segmento trovato dopo 120 tentativi

Un team prova 120 segmentazioni e trova un gruppo con `p = 0,009` e uplift del 14%.

Come cambia la tua interpretazione sapendo quante analisi sono state fatte? Quali dati useresti per confermare il segnale?

### Esercizio 5 — Type I e Type II come euro

Per un nuovo controllo antifrode, definisci:

- falso positivo;
- falso negativo;
- costo medio dei due errori;
- prevalenza della frode;
- volume mensile;
- quale errore vorresti ridurre maggiormente e perché.

Poi spiega perché questa decisione non può essere presa guardando soltanto accuracy o p-value.

### Esercizio 6 — Costruire il proprio Uncertainty Brief

Scegli una metrica del tuo dominio — conversion, churn, difetti, delivery SLA, NPS, forecast error o altro — e compila l'intero template del capitolo.

L'esercizio è riuscito se, alla fine, sai dire non soltanto:

> **“qual è il numero?”**

ma anche:

> **“quanto lo conosco bene, che cosa non è dentro quell'incertezza e quanto dovrebbe essere diverso per cambiare una decisione?”**
