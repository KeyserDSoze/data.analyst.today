## 9.4 Contaminazione e interferenza: quando A influenza B

L'idea classica dell'A/B test presume che l'esperienza assegnata a un'unità non cambi direttamente l'outcome di un'altra unità. Nei prodotti digitali reali questa assunzione può rompersi.

Succede quando utenti, venditori, team o mercati interagiscono tra loro.

### Caso: marketplace e seller che reagiscono al trattamento

Un marketplace testa una nuova logica di ranking che aumenta la visibilità dei venditori con consegne più rapide.

L'unità di randomizzazione iniziale è il buyer. Metà dei buyer vede il ranking nuovo, metà quello vecchio.

Dopo due settimane:

- conversione buyer B: +1,7%;
- GMV buyer B: +2,4%;
- delivery time medio: -4,1%.

Sembra una vittoria netta.

Ma i seller vedono crescere la domanda su alcuni prodotti e reagiscono:

- aumentano stock;
- cambiano prezzo;
- modificano promozioni;
- danno priorità operativa agli SKU più esposti.

Queste azioni influenzano anche i buyer nel gruppo A.

Il controllo non è più veramente "non trattato".

### Spillover

Questo fenomeno è spesso chiamato spillover o interference.

L'effetto del trattamento può propagarsi attraverso:

- rete sociale;
- mercato condiviso;
- inventario comune;
- capacità logistica condivisa;
- team operativi;
- sistemi di raccomandazione che apprendono globalmente.

### Caso B2B: esperimento sul team commerciale

Un'azienda assegna a metà dei Sales Representative un nuovo lead scoring model.

Gli account, però, non sono totalmente separati: alcuni appartengono allo stesso gruppo societario e i commerciali condividono informazioni nel CRM.

Dopo pochi giorni i commerciali di controllo iniziano a copiare informalmente le priorità dei colleghi trattati.

L'effetto osservato del modello si attenua. Non perché il modello non funzioni, ma perché il controllo viene contaminato.

### Strategie possibili

A seconda del sistema possiamo:

- randomizzare cluster invece di individui;
- usare regioni geografiche separate;
- creare holdout più isolati;
- limitare il test a mercati indipendenti;
- modellare esplicitamente gli spillover;
- accettare che la stima sia un effetto diluito e documentarlo.

Non esiste una soluzione universale.

### Quando l'interferenza è parte del prodotto

Nei marketplace, social network e piattaforme collaborative l'interferenza non è un'eccezione: è spesso il meccanismo di valore.

Se una feature rende più attivi alcuni seller e questo migliora l'esperienza di altri buyer, il network effect è parte dell'effetto business. Il problema non è eliminarlo, ma progettare un esperimento che lo misuri correttamente.

### Principio operativo

Prima del test chiediti:

> Se tratto questa unità, può cambiare il comportamento o l'ambiente di un'unità di controllo?

Se la risposta è sì, un semplice A/B individuale può non essere sufficiente.
