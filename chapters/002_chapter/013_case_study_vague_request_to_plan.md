## 2.12 Caso end-to-end: da “facci una dashboard clienti” a un piano analitico

**Caso simulato/composito.** Velora Home è un retailer omnicanale di prodotti per la casa. Il CRM contiene circa **1,8 milioni di profili cliente** e l'e-commerce rappresenta una quota crescente dei ricavi.

Il responsabile commerciale apre una richiesta apparentemente semplice:

> **“Ci serve una dashboard clienti perché ultimamente ci sembra che stiano andando peggio.”**

Se il team accettasse il deliverable come specifica, potrebbe iniziare immediatamente a scegliere KPI, filtri e visualizzazioni. Il brief costringe invece a fermarsi sulla parte meno precisa della frase: che cosa significa che i clienti “stanno andando peggio” e quale decisione dovrebbe migliorare grazie alla dashboard?

### La dashboard nasconde una decisione da €600.000

Durante una breve intervista emerge che il management non è genericamente preoccupato per la clientela. Ha osservato una metrica interna secondo cui la percentuale di nuovi clienti che effettua un secondo acquisto entro 90 giorni sarebbe scesa dal **33,8% al 27,1%** nell'arco di circa sei mesi.

La preoccupazione reale è quindi la capacità di trasformare il primo ordine in una relazione ripetuta. Il numero conta perché il team deve decidere dove concentrare circa **€600.000 di budget** del trimestre successivo: onboarding e CRM post-primo ordine, campagne di riattivazione, revisione delle promozioni di acquisizione, interventi sull'esperienza di consegna oppure nessun investimento specifico finché il fenomeno non sia stato confermato. Il Commercial Director e il CRM Lead sono i decision owner.

Questa informazione cambia già il progetto. Non serve una panoramica generica sui clienti; serve capire se il deterioramento della repeat purchase sia reale, dove si concentri e quale tipo di intervento meriti un approfondimento successivo.

La metrica viene quindi formalizzata prima di guardare i segmenti:

> **Repeat Purchase Rate 90d = clienti con almeno un secondo ordine valido entro 90 giorni / nuovi clienti pienamente osservabili per almeno 90 giorni.**

Un ordine valido esclude test, cancellazioni integrali e ordini fraudolenti annullati. I clienti troppo recenti per aver maturato novanta giorni di osservazione non entrano nel denominatore. Senza questa condizione, la freschezza apparente della metrica introdurrebbe un bias meccanico verso il basso.

Il brief dichiara inoltre che la prima fase è **diagnostica**. Il team vuole verificare il trend, localizzarlo e restringere le spiegazioni plausibili; eventuali associazioni con promozioni o delivery experience non verranno automaticamente interpretate come effetti causali.

### Prima di spiegare il calo, il team verifica che il calo esista

La baseline primaria utilizza coorti mensili comparabili degli ultimi 18 mesi, con attenzione allo stesso periodo dell'anno precedente. Le segmentazioni iniziali vengono scelte perché corrispondono a ipotesi o leve reali: canale di acquisizione, primo prodotto o categoria, sconto sul primo ordine, paese, valore del primo ordine, ritardo rispetto alla promessa di consegna e contatti con il supporto.

Anche il registro delle ipotesi include spiegazioni di business diverse — mix di acquisizione, promozioni una tantum, mix prodotto, delivery, problemi post-acquisto, prezzi e stagionalità — ma contiene deliberatamente anche un'ipotesi di **misurazione**: sei mesi prima il sistema di identificazione cliente potrebbe essere cambiato.

Questa pista viene verificata presto perché costa poco e, se vera, compromette l'intero outcome. Il sanity check scopre infatti che Velora Home ha migrato parte dell'e-commerce a un nuovo identity provider. Per alcuni clienti che acquistano una seconda volta da un dispositivo diverso, il nuovo ordine viene collegato a un nuovo `customer_id` invece che al profilo originale.

La repeat purchase grezza stava quindi mescolando due fenomeni:

- clienti che non avevano realmente riacquistato;
- clienti che avevano riacquistato ma che il sistema non riconosceva più come la stessa persona.

Dopo una ricostruzione controllata dell'identità, il quadro cambia in modo materiale:

| Misura | Inizio periodo | Fine periodo |
|---|---:|---:|
| metrica originaria | 33,8% | 27,1% |
| metrica corretta | 33,6% | 30,4% |

Circa metà del deterioramento apparente era un artefatto di misurazione. Se il team avesse iniziato dalla dashboard, avrebbe potuto rendere più visibile e più autorevole un trend parzialmente falso.

Ma il sanity check non chiude il problema. La metrica corretta mostra ancora un calo reale di circa **3,2 punti percentuali**. Ora, però, il team sa qual è il fenomeno che deve spiegare.

### Il delta residuo restringe la decisione

L'analisi diagnostica mostra che la maggior parte del deterioramento residuo si concentra nei clienti acquisiti tramite paid social, entrati con uno sconto iniziale superiore al 25% e con il primo ordine in poche categorie fortemente promosse. Questa combinazione spiega circa **il 60% del delta residuo** rispetto alle coorti di riferimento.

I clienti che subiscono consegne in ritardo mostrano anch'essi una repeat purchase inferiore. Tuttavia, i ritardi sono aumentati soprattutto nelle stesse categorie promozionate. La delivery experience e il mix promozionale sono quindi ancora confusi: i dati osservazionali disponibili non permettono di attribuire il calo a una sola delle due spiegazioni.

Questo è il punto in cui il tipo di domanda dichiarato nel brief protegge la qualità della conclusione. Il team può dire che i clienti provenienti da campagne paid-social ad alto sconto mostrano risultati peggiori; non può ancora dire che **lo sconto causa bassa retention**. Le promozioni potrebbero attirare clienti con propensione al riacquisto già diversa, e il problema logistico potrebbe contribuire nello stesso segmento.

La decisione cambia una seconda volta. All'inizio il management immaginava una dashboard clienti e una possibile spesa in campagne CRM. Alla fine della prima fase il piano è diverso:

1. correggere e monitorare permanentemente l'identity stitching;
2. non utilizzare la vecchia serie storica senza ricostruzione;
3. riesaminare gli economics delle campagne paid-social ad alto sconto;
4. separare in un'analisi successiva il contributo del mix promozionale da quello della delivery experience;
5. progettare un test su incentivi o onboarding invece di trasformare una correlazione osservata in causalità.

Il team **non** investe immediatamente i €600.000 in riattivazione. Prima corregge la misurazione e decide quale nuova evidenza valga la pena raccogliere.

### Il brief che resta dopo l'indagine

Il documento finale conserva in forma compatta ciò che il caso ha reso esplicito:

```text
Problema di business:
repeat purchase dei nuovi clienti potenzialmente in deterioramento.

Decisione:
dove allocare il budget retention/acquisition del prossimo trimestre.

Domanda primaria:
il calo della Repeat Purchase Rate 90d è reale e, se sì,
quali segmenti e cambiamenti osservabili spiegano maggiormente il delta?

Tipo di domanda:
diagnostica; nessuna attribuzione causale automatica.

Outcome:
Repeat Purchase Rate 90d su clienti pienamente maturi.

Baseline:
coorti mensili storiche e year-over-year comparabile.

Segmentazioni:
canale, sconto, primo prodotto, paese, delivery, support.

Dati required:
identità storica + ordini validi.

Rischio principale noto:
migrazione identity provider.

Output:
memo decisionale + dataset/cohort view validata;
dashboard soltanto per metriche che meritano monitoraggio ricorrente.

Stop rule prima fase:
validare la metrica, spiegare la parte materialmente rilevante del delta
e identificare quali ipotesi richiedono un test successivo.
```

La richiesta iniziale era “facci una dashboard clienti”. Il brief ha rivelato una domanda molto diversa: **possiamo fidarci del deterioramento osservato, dove si concentra e quale informazione ci serve prima di spendere il budget?**

Questa differenza è il lavoro analitico che avviene prima dell'analisi — e, in questo caso, è ciò che impedisce alla velocità di trasformare un errore di identity stitching in una decisione da €600.000.
