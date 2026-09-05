## 8.1 Il controfattuale: definire l'alternativa prima di misurare l'effetto

Ogni causal question contiene due mondi. Per una stessa unità vorremmo conoscere il risultato sotto trattamento e quello che avrebbe prodotto la stessa unità senza trattamento. Nel linguaggio dei *potential outcomes* li indichiamo come `Y(1)` e `Y(0)`; l'effetto individuale sarebbe `Y(1) - Y(0)`. Il problema è che, per la stessa unità nello stesso momento, ne osserviamo soltanto uno. Il controfattuale individuale manca per definizione.

Questa assenza non è un inconveniente tecnico da correggere con più dati. È il motivo per cui la causal inference ha bisogno di un design. Un gruppo di confronto serve a rappresentare il risultato non osservato, e la qualità della causal claim dipende dalla credibilità di quella rappresentazione.

### Caso simulato/composito — Il coupon da 20 euro

Un retailer invia un coupon a **50.000 clienti**. Entro trenta giorni la conversione è **24%** tra i destinatari e **15%** tra i non destinatari. Il `+9 pp` è una differenza osservata, ma il marketing ha scelto i destinatari tra clienti con almeno tre visite recenti. Il gruppo trattato partiva quindi con un intento d'acquisto maggiore.

La domanda causale non è “quanto acquistano i destinatari rispetto agli altri?”, ma:

> **Quanto avrebbero acquistato quei clienti se, a parità del resto, non avessero ricevuto il coupon?**

Anche il confronto prima/dopo nasconde un controfattuale. Se la conversione dei clienti target passa dal **17% prima** al **24% dopo**, il calcolo `24% - 17% = +7 pp` assume implicitamente che, senza coupon, il 17% sarebbe rimasto una baseline adeguata. Ma Natale, catalogo, traffico, prezzi o campagne possono essere cambiati nello stesso periodo. Il “prima” non è automaticamente il mondo senza trattamento del “dopo”.

### L'estimand decide quale mondo alternativo serve

Non esiste un unico “effetto del trattamento”. Possiamo voler conoscere l'**ATE**, cioè l'effetto medio nella popolazione target; l'**ATT**, l'effetto medio sulle unità effettivamente trattate; un **CATE**, l'effetto medio in un sottogruppo definito; oppure un effetto locale, per esempio vicino a una soglia. La quantità corretta dipende dalla decisione.

Se oggi un programma di retention viene offerto solo ad account considerati recuperabili, l'ATT sui clienti trattati può essere molto diverso dall'ATE che avremmo estendendo la policy a tutta la customer base. Cambiare estimand significa cambiare domanda, non soltanto formula.

Per la stessa ragione, trattamento e alternativa devono essere definiti abbastanza bene da poter essere immaginati come due condizioni realmente diverse. “Customer Success” è troppo vago se può significare una telefonata, tre sessioni tecniche, un account manager dedicato o un voucher. Una specifica operativa è molto più utile:

```text
Unità: account SMB
Trattamento: sessione tecnica di 45 minuti entro 7 giorni
Alternativa: onboarding standard senza sessione extra
Outcome: rinnovo entro 90 giorni
Popolazione: account che non hanno completato ERP integration entro D30
```

Questa precisione introduce il principio di **consistency**: quando classifichiamo un'unità come trattata dobbiamo sapere quale versione del trattamento ha effettivamente ricevuto. Se alcuni account vedono un video automatico e altri un workshop con un consulente senior, una sola colonna `training = 1` può nascondere interventi abbastanza diversi da rendere ambiguo l'effetto.

Prima della stima dobbiamo quindi ricostruire assignment, exposure effettiva, intensità, timing e possibili cross-over. Il Capitolo 9 entrerà nei dettagli operativi degli esperimenti; qui il principio è più generale: **non possiamo interpretare causalmente un trattamento che non sappiamo definire**.

### Quando il controfattuale dipende dagli altri

Molti esempi introduttivi assumono che il trattamento di un'unità non influenzi l'outcome di un'altra. Nei sistemi reali, però, può esserci **interference**: una promozione a un seller può sottrarre domanda ad altri seller; un algoritmo può modificare l'esperienza di tutto il marketplace; un training a un manager può influenzare il team; un aumento prezzi in una regione può spostare clienti in quella confinante.

In questi casi non basta aggiungere una covariata. Bisogna ridefinire l'unità di trattamento o formulare una domanda che includa gli spillover. Il controfattuale di un individuo può dipendere da come sono trattati gli altri.

La World Bank tratta il controfattuale come il passaggio centrale dell'impact evaluation e mostra che randomizzazione, IV, RDD, DiD e matching costruiscono la comparabilità in modi differenti.[^worldbank-counterfactual] Il testo di Hernán e Robins *Causal Inference: What If* insiste analogamente sulla necessità di specificare l'intervento e le condizioni sotto cui l'outcome controfattuale può essere confrontato.[^whatif]

Il punto operativo è semplice: un comparison group non è “il gruppo che il database ci offre”. È una popolazione per cui possiamo sostenere che, senza trattamento, avrebbe riprodotto abbastanza bene l'outcome controfattuale dei trattati. I metodi che incontreremo dopo non sono varianti della stessa formula; sono argomenti differenti per rendere plausibile quella frase.

> **Prima di calcolare l'effetto, descrivi il mondo alternativo che vuoi rappresentare. Se non sai farlo, la causal question non è ancora sufficientemente definita.**

[^worldbank-counterfactual]: World Bank e Inter-American Development Bank, *Impact Evaluation in Practice, Second Edition*, capitolo 3 e parte II: https://www.worldbank.org/en/programs/sief-trust-fund/publication/impact-evaluation-in-practice
[^whatif]: Hernán, M.A. & Robins, J.M., *Causal Inference: What If*, Harvard T.H. Chan School of Public Health: https://www.hsph.harvard.edu/miguel-hernan/wp-content/uploads/sites/1268/2024/04/hernanrobins_WhatIf_26apr24.pdf
