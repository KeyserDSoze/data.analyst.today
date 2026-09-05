## 10.3 Coefficienti e interazioni: capire come il modello usa il segnale senza trasformarlo in causalità

I modelli lineari sono attraenti perché i coefficienti sembrano raccontare una storia. Proprio questa leggibilità crea il rischio di confondere una proprietà del modello con una teoria del mondo.

In termini operativi, un coefficiente descrive come cambia la previsione quando una feature cambia di un'unità, mantenendo fisse le altre feature rappresentate nel modello. La frase contiene già i suoi limiti: “mantenendo fisse” riguarda soltanto ciò che abbiamo misurato, la scala della feature cambia l'interpretazione numerica e la relazione vale nel dominio su cui il modello è stato appreso.

### Caso simulato/composito — BluePeak SaaS

BluePeak vuole prevedere l'espansione annuale dei contratti usando utenti attivi, integrazioni configurate, ticket di supporto, piano commerciale e utilizzo delle automazioni. Nel primo modello `ticket_support` riceve un coefficiente positivo molto forte.

La lettura ingenua sarebbe:

> “Aprire ticket aumenta l'espansione.”

L'EDA mostra invece che gli account enterprise hanno contemporaneamente implementazioni più complesse, più ticket, più business unit e più spazio di espansione. Aggiungendo proxy migliori della dimensione e complessità dell'account, il coefficiente dei ticket si riduce molto.

Non abbiamo trovato il “coefficiente vero”. Abbiamo visto che il coefficiente dipende dalla rappresentazione che il modello riceve del problema. Questo è perfettamente compatibile con un uso predittivo e insufficiente per una conclusione causale.

Per passare da:

> “gli account con più integrazioni hanno espansione prevista maggiore”

A:

> “aggiungere un'integrazione farà aumentare l'espansione”

serve l'identification strategy del Capitolo 8. Una regressione predittiva, anche stabile e ben validata, non chiude quel passaggio.

### Categorie: il riferimento fa parte della frase

Una variabile `Basic / Pro / Enterprise` non dovrebbe diventare automaticamente `1 / 2 / 3` se quei numeri non rappresentano una scala quantitativa reale. Con una codifica a indicatori possiamo usare, per esempio, `Basic` come riferimento: i coefficienti di `Pro` ed `Enterprise` descrivono differenze rispetto a Basic. Cambiare riferimento modifica la parametrizzazione visibile, non le previsioni di un modello specificato in modo equivalente.

Per questo la categoria di riferimento deve comparire nella comunicazione quando interpretiamo coefficienti.

### Interazioni: lo stesso segnale può valere diversamente in contesti diversi

Un modello additivo assegna a una feature lo stesso contributo marginale indipendentemente dalle altre, salvo trasformazioni esplicite. Un termine come:

`usage × integrations`

permette invece al contributo di `usage` di dipendere dal numero di integrazioni.

Nel caso BluePeak l'interazione migliora la performance perché l'utilizzo delle automazioni discrimina maggiormente tra account con ecosistemi complessi che tra piccoli clienti appena attivati. Questa osservazione ci dice **dove il modello trova segnale**. Non dimostra che un training sulle automazioni causerà espansione.

Lo stesso vale per spline, polinomi e altre non linearità. Un ticket può avere significato predittivo diverso tra 1 e 20 eventi; stock e tempi di attesa possono mostrare soglie o saturazioni. Aggiungere complessità ha senso soltanto quando il pattern sopravvive fuori campione, è supportato da abbastanza osservazioni e migliora la prediction task.

### Il dominio osservato mette un confine alle previsioni

Supponiamo che BrightFoods abbia osservato saturazione del magazzino tra `0,35` e `0,92`. Un modello lineare può produrre senza protestare una previsione per `1,40`. Il fatto che la formula restituisca un numero non significa che i dati sostengano quella extrapolation.

La Predictive Decision Card dovrà quindi dichiarare non soltanto il modello ma anche lo **scope**: popolazioni, periodi e regioni delle feature in cui la generalizzazione è stata verificata.

### Come comunicare senza creare una leva immaginaria

Una formulazione professionale è:

> “Nel modello, questa feature contribuisce positivamente alla previsione, condizionatamente alle altre informazioni incluse.”

Oppure:

> “Questa interazione migliora la performance fuori campione e mostra che il segnale cambia in questo contesto.”

La frase da evitare, senza un disegno causale, è:

> “Questa variabile fa aumentare l'outcome.”

> **L'interpretabilità predittiva spiega come il modello costruisce una previsione. La causalità spiega che cosa accadrebbe se intervenissimo sul mondo. Sono domande diverse anche quando usano le stesse variabili.**