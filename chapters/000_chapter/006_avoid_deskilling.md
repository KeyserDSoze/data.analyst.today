# 0.5 Evitare il deskilling: usare l'AI senza perdere la capacità di pensare

L'AI può farci diventare più capaci.

Può anche farci diventare più fragili.

Se deleghiamo progressivamente ogni passaggio senza mantenere comprensione dei principi, rischiamo il **deskilling**: perdita delle competenze necessarie per capire, correggere e governare il sistema che utilizziamo.

Non è un argomento nostalgico.

È un problema operativo.

## Il rischio invisibile

Immaginiamo un analyst junior che usa l'AI per ogni attività:

- scrive SQL;
- interpreta errori;
- sceglie statistiche;
- seleziona grafici;
- costruisce modelli;
- scrive conclusioni.

Dopo un anno può produrre molto più output di un analyst di generazioni precedenti.

Ma cosa succede quando:

- il join è semanticamente sbagliato?
- la query ritorna un risultato plausibile ma duplicato?
- il modello ha leakage?
- l'intervallo di confidenza è interpretato male?
- un agente confonde correlazione e causalità?
- la documentazione generata contiene una definizione KPI inventata?

Se la persona non possiede abbastanza modello mentale per riconoscere l'errore, la produttività apparente nasconde dipendenza.

## Non dobbiamo conservare tutte le abilità allo stesso livello

Non significa che dobbiamo continuare a fare tutto manualmente.

Alcune competenze possono diventare meno centrali.

Memorizzare la sintassi esatta di ogni funzione SQL può valere meno.

Ricordare ogni parametro di una libreria può valere meno.

Scrivere boilerplate da zero può valere meno.

Ma altre competenze diventano ancora più importanti:

- grain;
- cardinalità;
- semantica delle metriche;
- probabilità;
- causalità;
- validazione;
- design sperimentale;
- temporalità;
- business understanding;
- capacità di leggere codice e query;
- capacità di diagnosticare un risultato assurdo.

L'obiettivo non è sapere tutto a memoria.

È **possedere abbastanza fondamenta da poter giudicare ciò che viene delegato**.

## Caso realistico: il senior che non scrive più SQL

Una responsabile analytics coordina un team e usa agenti per generare quasi tutte le query.

Non scrive SQL da mesi.

Durante un'analisi pricing, un agente produce una tabella che mostra margine medio per categoria.

Il risultato indica che una categoria a basso prezzo ha il margine percentuale più alto.

La manager nota però che il margine assoluto non riconcilia con Finance.

Apre la query e individua rapidamente il problema: il join con una tabella di promozioni è many-to-many e duplica alcune righe.

Non aveva scritto la query.

Ma aveva mantenuto la capacità di:

- leggere SQL;
- ragionare sul grain;
- riconoscere una reconciliation impossibile;
- formulare un test.

Questa è la differenza tra delega e deskilling.

## Il modello “manual enough to understand”

Per ogni competenza importante dovremmo arrivare almeno al punto in cui possiamo:

1. spiegare il principio;
2. riconoscere un output plausibile ma sbagliato;
3. formulare un controllo;
4. leggere l'implementazione generata;
5. intervenire quando il sistema fallisce.

Non serve essere i migliori programmatori del team.

Serve evitare di diventare incapaci di distinguere un sistema sano da uno rotto.

## Pratica deliberata

Un modo concreto per evitare deskilling è mantenere esercizi senza AI.

Per esempio:

- una volta a settimana scrivere una query complessa manualmente;
- spiegare una regressione senza assistente;
- ricostruire a mano una metrica critica;
- fare code review senza chiedere prima all'AI;
- stimare un ordine di grandezza prima di vedere il risultato;
- formulare tre ipotesi prima di chiedere all'agente di generarne altre.

Non perché il lavoro debba essere sempre eseguito così.

Ma perché una competenza non esercitata tende a deteriorarsi.

## L'AI come sparring partner, non soltanto come esecutore

L'AI può anche ridurre il deskilling se viene usata bene.

Possiamo chiederle:

- “fammi domande per verificare che abbia capito questo modello”;
- “non darmi la soluzione: indicami dove il mio ragionamento è debole”;
- “proponi un controesempio”;
- “fammi una code review ma lascia a me la correzione”;
- “quale assunzione sto dando per scontata?”

In questo modo l'AI non sostituisce il pensiero.

Lo stressa.

## Il test definitivo

Dovremmo preoccuparci quando non siamo più in grado di rispondere a una domanda semplice:

> “Perché pensi che questo risultato sia corretto?”

Se la risposta è:

> “Perché l'AI lo ha prodotto.”

abbiamo ceduto il timone.

Se invece possiamo spiegare dati, metodo, controlli, limiti e alternative, l'AI ci sta amplificando senza renderci dipendenti.

> **Non dobbiamo competere con l'AI sulla velocità di esecuzione. Dobbiamo mantenere le competenze che ci permettono di riconoscere quando l'esecuzione sta andando nella direzione sbagliata.**