## 8.3 Confondenti: capire perché i gruppi erano diversi prima del trattamento

Il confounding nasce quando lo stesso processo che rende più probabile il trattamento influenza anche l'outcome. In forma minima:

```text
Z -> trattamento
Z -> outcome
```

Il confronto grezzo tra trattati e non trattati mescola allora due cose: il possibile effetto del trattamento e differenze che esistevano già prima. Il problema non è nel coefficiente finale; nasce nel modo in cui il mondo ha prodotto i gruppi.

### Caso simulato/composito — La campagna display che sembrava triplicare la conversione

Un e-commerce osserva:

| Gruppo | Conversion rate |
|---|---:|
| Esposti agli annunci | 5,8% |
| Non esposti | 2,1% |

La differenza è **+3,7 pp**, ma la piattaforma mostra più annunci proprio agli utenti che hanno visitato siti della categoria, cercato prodotti simili o manifestato recente intento d'acquisto. Una storia plausibile è quindi:

```text
intento preesistente -> probabilità di esposizione
intento preesistente -> probabilità di acquisto
esposizione ----------> possibile effetto sull'acquisto
```

La differenza osservata contiene insieme selezione e possibile effetto advertising. Una regressione può aggiustare parte del problema solo se misura adeguatamente le cause comuni rilevanti e se le tratta nel ruolo causale corretto.

Questo è il punto in cui la regola “controlliamo per tutte le colonne” smette di essere prudente e diventa pericolosa. Una variabile correlata sia al trattamento sia all'outcome può essere una causa comune pre-treatment, un semplice predittore, un mediatore generato dal trattamento, un collider, un proxy imperfetto o perfino una conseguenza dell'outcome. Il ruolo nel processo, non la correlazione, determina se l'adjustment aiuta.

### Il prezzo del gelato e la temperatura

Una catena di gelaterie trova una correlazione positiva tra prezzo medio e quantità venduta. Se nei giorni più caldi aumenta la domanda e alcuni store attivano pricing dinamico, la struttura può essere:

```text
temperatura -> prezzo
     |
     +-------> domanda
```

Confrontare giornate climaticamente diverse attribuisce al prezzo una parte dell'effetto della temperatura. Aggiungere “più feature” non risolve il problema se non abbiamo prima ricostruito quali variabili appartengono al percorso causale.

Hernán e Robins descrivono proprio questo passaggio come una scelta strutturale: l'adjustment deve essere guidato da conoscenza causale a priori e da un modello delle cause comuni, non da una procedura che aggiunge automaticamente covariate perché migliorano il fit.[^whatif-confounding]

Alcune cause comuni sono facilmente misurabili — storico acquisti, dimensione account, tenure, geografia, utilizzo pre-trattamento, calendario — mentre altre possono rimanere quasi invisibili nel warehouse: motivazione, intento reale, qualità del management, urgenza, forza della relazione commerciale, severità di un problema non registrata. Matching, weighting e regressione possono bilanciare **ciò che osserviamo**. Non eliminano per definizione il confounding non osservato.

Per questo una delle domande più utili viene prima del notebook:

> **Perché questa unità ha ricevuto il trattamento?**

Intervistare chi prende la decisione operativa può far emergere informazioni che il dataset non possiede. Se Customer Success dice “offriamo lo sconto solo quando il procurement minaccia esplicitamente di andarsene” e quella minaccia non è registrata, nessuna regressione sul CRM può controllarla direttamente.

Questa dinamica è frequente nei processi aziendali perché gli interventi sono spesso **reattivi al rischio**: più supporto ai clienti in difficoltà, più sconti a chi minaccia churn, più manutenzione agli impianti fragili, più visite manageriali ai negozi peggiori. Il trattamento può quindi apparire associato a outcome peggiori anche quando sta riducendo il danno rispetto al controfattuale.

Prima di aggiustare un confronto osservazionale conviene fissare in una piccola scheda le assunzioni che stiamo facendo:

```text
Trattamento:
Outcome:
Cause plausibili del trattamento:
Cause plausibili dell'outcome:
Cause comuni plausibili:
Quali sono pre-trattamento?
Quali sono misurate?
Quali importanti non sono misurate?
Quali variabili NON dobbiamo controllare e perché?
```

La sezione successiva rende questa dinamica ancora più concreta: quando l'azienda interviene proprio perché il rischio è già salito, il trattamento arriva dopo che una parte della traiettoria causale è iniziata.

[^whatif-confounding]: Hernán, M.A. & Robins, J.M., *Causal Inference: What If*, capitolo sul confounding e causal DAG: https://www.hsph.harvard.edu/miguel-hernan/wp-content/uploads/sites/1268/2024/04/hernanrobins_WhatIf_26apr24.pdf
