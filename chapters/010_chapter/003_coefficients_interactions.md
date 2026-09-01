## 10.3 Coefficienti, categorie e interazioni: interpretare il modello senza trasformarlo in una teoria causale

I modelli lineari sono attraenti perché producono coefficienti leggibili. Proprio questa leggibilità crea un rischio: scambiare una descrizione del comportamento predittivo del modello per una spiegazione del mondo.

Un coefficiente risponde, in modo semplificato, a una domanda del tipo:

> **come cambia la previsione quando questa feature cambia di un'unità, mantenendo fisse le altre feature rappresentate nel modello?**

Questa frase contiene già tre limiti:

- "mantenendo fisse" riguarda solo ciò che il modello contiene;
- l'unità e la scala della feature cambiano l'interpretazione numerica;
- la relazione stimata vale nella popolazione e nel dominio in cui il modello è stato appreso.

### Caso simulato/composito — BluePeak SaaS

BluePeak vende software B2B e vuole prevedere l'espansione annuale del contratto.

Il primo modello usa:

- utenti attivi;
- integrazioni configurate;
- ticket di supporto;
- piano commerciale;
- utilizzo delle automazioni.

`ticket_support` riceve un coefficiente positivo molto forte.

La lettura sbagliata è:

> "Aprire ticket fa aumentare l'espansione."

L'EDA mostra invece che gli account enterprise hanno contemporaneamente:

- implementazioni più complesse;
- più ticket;
- più business unit;
- maggiore spazio di espansione.

Aggiungendo proxy migliori della dimensione e complessità dell'account, il coefficiente dei ticket si riduce molto.

Il punto non è cercare il "coefficiente vero" finché il numero ci piace. È ricordare che il coefficiente dipende dalla rappresentazione del problema fornita al modello.

### Coefficiente predittivo vs effetto causale

Questa distinzione deve essere esplicita in ogni presentazione.

Un coefficiente può essere molto stabile e utile per predire senza rappresentare l'effetto di una leva modificabile.

Per trasformare:

> "gli account con più integrazioni hanno espansione prevista maggiore"

in:

> "aggiungere un'integrazione farà aumentare l'espansione"

serve una strategia causale come quelle discusse nel Capitolo 8.

La regressione predittiva da sola non chiude quel passaggio.

### Variabili categoriche: il riferimento cambia la lettura

Una variabile come piano `Basic / Pro / Enterprise` non dovrebbe essere trattata come la scala numerica arbitraria `1 / 2 / 3` se non esiste davvero quella struttura quantitativa.

Una codifica con indicatori può usare, per esempio, `Basic` come riferimento.

A quel punto:

- il coefficiente `Pro` descrive una differenza rispetto a Basic;
- il coefficiente `Enterprise` descrive una differenza rispetto a Basic;
- cambiare categoria di riferimento cambia i coefficienti visualizzati, non le previsioni del modello correttamente specificato.

Quando si comunica il modello, la categoria di riferimento va quindi dichiarata.

### Interazioni: il contributo di una feature può dipendere dal contesto

I modelli additivi assumono che il contributo di una feature non cambi a seconda del valore di un'altra, salvo trasformazioni esplicite.

Un termine come:

`usage × integrations`

permette invece al contributo di `usage` di dipendere dal numero di integrazioni.

Nel caso BluePeak, un'interazione migliora la previsione perché l'utilizzo delle automazioni discrimina molto di più tra account con ecosistemi complessi che tra piccoli clienti appena attivati.

Questo è utile per capire **dove il modello trova segnale**.

Non basta, da solo, a concludere che un intervento di training sulle automazioni produrrà espansione.

### Non linearità e domain of validity

Molti fenomeni business non cambiano in modo costante.

Esempi:

- 1 ticket può essere normale, 20 ticket in una settimana no;
- aumentare stock riduce stock-out fino a un certo punto, poi immobilizza capitale;
- il rapporto tra tempo di attesa e abbandono può accelerare oltre una soglia;
- una variazione di prezzo può avere risposta diversa per fasce diverse.

Possiamo rappresentare queste strutture con:

- trasformazioni;
- spline;
- termini polinomiali;
- interazioni;
- modelli non lineari.

Prima di farlo, però, dobbiamo verificare che il pattern sia:

1. presente fuori dal training set;
2. supportato da abbastanza osservazioni;
3. rilevante per la prediction task.

### Extrapolation: il coefficiente non autorizza a uscire dai dati

Supponiamo che BrightFoods abbia osservato saturazione del magazzino tra 0,35 e 0,92.

Usare il modello per stimare che cosa accadrebbe a saturazione `1,40` non è una semplice previsione più estrema. È extrapolation fuori dal dominio osservato.

La forma lineare continuerà a produrre un numero anche quando l'evidenza per sostenerlo è molto debole.

Per questo nella Predictive Decision Card indicheremo anche lo **scope** della popolazione e dei valori su cui il modello è stato validato.

### Regola di comunicazione

Preferisci:

> "Nel modello, questa feature contribuisce positivamente alla previsione, condizionatamente alle altre variabili incluse."

oppure:

> "Il modello usa questa interazione per migliorare la performance fuori campione."

Evita, senza identificazione causale:

> "Questa variabile fa aumentare l'outcome."

> **L'interpretabilità predittiva spiega come il modello costruisce una previsione. Non dimostra automaticamente come il mondo reagirà a un intervento.**
