## 0.5 Evitare il deskilling: usare l'AI senza perdere la capacità di pensare

L'AI può renderci più capaci.

Può anche renderci più fragili.

Se deleghiamo progressivamente ogni passaggio senza mantenere comprensione dei principi, rischiamo il **deskilling**: perdere proprio le competenze che ci servono per riconoscere, correggere e governare gli errori del sistema che utilizziamo.

Non è nostalgia per il lavoro manuale.

È un problema di resilienza professionale.

### Produttività apparente, dipendenza reale

Immaginiamo un analyst junior che usa l'AI per quasi tutto:

- scrivere SQL;
- interpretare errori;
- scegliere statistiche;
- selezionare grafici;
- costruire modelli;
- formulare conclusioni.

Può produrre molto più output di un analyst di qualche anno prima.

Ma la domanda decisiva è che cosa succede quando l'output è plausibile e sbagliato.

Riconosce un join many-to-many che duplica la revenue?

Si accorge che un modello usa una variabile disponibile soltanto dopo l'evento che dovrebbe prevedere?

Capisce che un intervallo di confidenza è stato interpretato male?

Nota che una spiegazione causale nasce soltanto da una correlazione?

Se non possiede un modello mentale sufficiente per porre queste domande, la velocità nasconde dipendenza.

### Non tutte le competenze devono restare uguali

Evitare il deskilling non significa continuare a fare tutto manualmente.

Alcune abilità possono perdere valore relativo:

- ricordare la sintassi esatta di ogni funzione;
- memorizzare tutti i parametri di una libreria;
- scrivere boilerplate da zero;
- ricostruire a mano attività meccaniche che un sistema svolge bene e in modo verificabile.

Altre diventano più importanti proprio perché l'esecuzione è più facile:

- grain e cardinalità;
- semantica delle metriche;
- probabilità e incertezza;
- causalità;
- temporalità;
- design sperimentale;
- validazione;
- business understanding;
- capacità di leggere query e codice;
- capacità di diagnosticare un risultato assurdo o semplicemente sospetto.

L'obiettivo non è sapere tutto a memoria.

È **possedere abbastanza fondamenta da poter giudicare ciò che viene delegato**.

### Caso simulato/composito: la senior che non scrive più SQL

Una responsabile analytics coordina un team e usa agenti per generare quasi tutte le query operative.

Non scrive SQL da mesi.

Durante un'analisi pricing, un agente produce una tabella che mostra il margine medio per categoria. Il risultato indica che una categoria a basso prezzo ha il margine percentuale più alto.

La manager nota però che il margine assoluto non riconcilia con Finance.

Apre la query e individua rapidamente il problema: il join con una tabella di promozioni è many-to-many e duplica alcune righe.

Non aveva scritto la query.

Ma aveva mantenuto la capacità di:

- leggere SQL;
- ragionare sul grain;
- riconoscere una reconciliation impossibile;
- formulare un test;
- spiegare perché il risultato non era affidabile.

Questa è la differenza tra delega e deskilling.

### “Manual enough to understand”

Per una competenza importante non è necessario eseguire ogni volta tutto a mano. Dovremmo però conservare almeno la capacità di:

1. spiegare il principio;
2. riconoscere errori tipici;
3. formulare un controllo;
4. leggere l'implementazione generata;
5. intervenire quando il sistema fallisce.

Non serve diventare i migliori programmatori, statistici o data engineer del team.

Serve evitare di diventare incapaci di distinguere un sistema sano da uno rotto.

### Usare l'AI anche per allenare il giudizio

L'AI non deve essere soltanto un esecutore. Può diventare uno sparring partner.

Possiamo chiederle, per esempio:

- “Fammi domande per verificare se ho capito questo modello.”
- “Non darmi la soluzione: indicami dove il mio ragionamento è debole.”
- “Proponi un controesempio alla mia conclusione.”
- “Fai code review, ma lascia a me la correzione.”
- “Quale assunzione sto dando per scontata?”
- “Quale risultato dovrei aspettarmi prima di eseguire il calcolo?”

La stessa tecnologia che può sostituire passivamente un'attività può anche rendere l'apprendimento più attivo.

### Mantenere una quota di pratica deliberata

Per le competenze fondamentali è utile conservare momenti in cui l'AI non fornisce immediatamente la soluzione.

Per esempio:

- formulare ipotesi prima di chiederne altre all'agente;
- stimare un ordine di grandezza prima di vedere il risultato;
- ricostruire periodicamente una metrica critica;
- fare una prima code review senza assistenza;
- spiegare un concetto statistico con parole proprie.

Non perché il lavoro quotidiano debba tornare manuale, ma perché una competenza mai esercitata tende a deteriorarsi.

Il Capitolo 19 tornerà sul tema dal punto di vista della carriera e dell'apprendimento nel lungo periodo. Qui ci basta fissare il principio operativo:

> **possiamo delegare la produzione, ma dobbiamo preservare le competenze che ci permettono di accorgerci quando la produzione sta andando nella direzione sbagliata.**

Il test più semplice resta una domanda:

> “Perché pensi che questo risultato sia corretto?”

Se l'unica risposta disponibile è:

> “Perché l'AI lo ha prodotto.”

abbiamo ceduto il timone.
