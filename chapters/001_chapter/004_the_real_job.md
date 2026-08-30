## 1.3 Il vero lavoro dell'analista

La parte visibile del lavoro di un Data Analyst è spesso la meno importante.

Una dashboard è visibile. Una query SQL è visibile. Un notebook è visibile. Una presentazione con grafici è visibile. Ma prima di ciascuno di questi output esiste una serie di decisioni che determinano se l'analisi sarà utile oppure no.

Un analista deve decidere quali domande meritano una risposta, quali metriche rappresentano davvero il fenomeno, quali confronti sono legittimi, quali dati sono affidabili, quali assunzioni sono implicite e quale livello di incertezza è accettabile.

Il lavoro reale può essere descritto come una catena:

**Problema di business -> domanda analitica -> dati -> metodo -> evidenza -> interpretazione -> decisione -> azione -> misurazione dell'effetto**

Questa catena è più importante dello strumento utilizzato in ogni singolo passaggio.

### Dalla richiesta alla decisione

Consideriamo una richiesta comune:

> "Voglio capire perché le vendite sono scese."

La risposta ingenua è aprire i dati e cercare un grafico che mostri la diminuzione.

La risposta analitica è scomporre la richiesta.

Prima domanda: **che cosa significa vendite?**

Potrebbe significare:

- fatturato lordo;
- fatturato netto;
- numero di ordini;
- quantità vendute;
- margine;
- valore medio dell'ordine;
- ricavi ricorrenti;
- vendite contabilizzate o semplicemente ordinate.

Seconda domanda: **rispetto a cosa stanno scendendo?**

Confrontare luglio con giugno può essere fuorviante se il business è stagionale. Confrontare luglio con luglio dell'anno precedente può essere migliore, ma potrebbe essere distorto da una promozione eccezionale avvenuta l'anno prima.

Terza domanda: **dove avviene la diminuzione?**

Per prodotto? Area geografica? Canale? Tipologia di cliente? Cohort? Fascia di prezzo?

Quarta domanda: **quale decisione deve essere presa?**

Se il management non può agire sul fattore identificato, quell'analisi potrebbe avere un valore descrittivo ma poco valore operativo.

L'obiettivo dell'analista non è quindi "trovare qualcosa di interessante". È ridurre l'incertezza attorno a una decisione.

### Il Business Understanding viene prima del dato

Questa idea non nasce con l'AI. È presente nei framework di analytics da decenni. Nel processo CRISP-DM, ad esempio, la fase iniziale è il *Business Understanding*: comprendere gli obiettivi dell'organizzazione, chiarire cosa si vuole ottenere e tradurre il problema in un piano analitico prima di investire risorse nelle fasi successive.

La documentazione IBM dedicata a CRISP-DM sottolinea esplicitamente che comprendere le ragioni di business del progetto aiuta ad allineare le persone coinvolte prima di utilizzare tempo e risorse sull'analisi.

Fonte: https://www.ibm.com/docs/en/spss-modeler/saas?topic=understanding-business-overview

Subito dopo arriva il *Data Understanding*: raccogliere i dati, esplorarli, valutarne la qualità e identificare problemi che potrebbero compromettere le fasi successive.

Fonte: https://www.ibm.com/docs/en/spss-modeler/saas?topic=understanding-data-overview

Queste due fasi sono ancora più importanti oggi. L'AI può accelerare enormemente il lavoro successivo, ma se l'obiettivo o i dati sono sbagliati accelera nella direzione sbagliata.

### L'analista come riduttore di incertezza

Una definizione utile per tutto il libro sarà questa:

> **Un Data Analyst è una persona che utilizza dati, metodi quantitativi, conoscenza del dominio e strumenti tecnologici per ridurre l'incertezza attorno a una decisione.**

Questa definizione è volutamente indipendente da Excel, SQL, Python, Power BI o qualunque altro prodotto.

Gli strumenti cambiano. Il problema professionale resta.
