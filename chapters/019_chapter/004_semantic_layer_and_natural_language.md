## 19.3 Semantic leverage: quando l'interfaccia diventa più semplice

Una delle promesse più visibili dell'AI applicata ai dati è:

> “Chiunque potrà fare domande ai dati in linguaggio naturale.”

È plausibile che una parte crescente dell'interazione con l'analytics diventi più conversazionale.

Ma una UI più semplice non rende il problema sottostante più semplice.

Spesso accade il contrario.

## Il linguaggio naturale comprime la sintassi, non l'ambiguità

Un manager chiede:

> “Qual è il churn in Francia?”

La generazione SQL può essere quasi istantanea.

Ma `churn` potrebbe significare:

- logo churn;
- revenue churn;
- gross churn;
- cancellation;
- non-renewal;
- churn volontario;
- churn a 30/60/90 giorni;
- mensile o annualizzato.

La difficoltà non è tradurre parole in query.

È collegare la richiesta alla **versione di realtà che l'organizzazione ha deciso di considerare autorevole per quella decisione**.

La catena reale è:

**linguaggio umano → concetto business → entità/metrica → semantic contract → dati → query → evidenza**.

Natural language analytics comprime soprattutto l'ultimo tratto.

## Più accesso, più blast radius semantico

Se due analyst interpretano diversamente una metrica, abbiamo già un problema.

Se diecimila richieste conversazionali possono generare automaticamente query su interpretazioni diverse, il problema scala.

Quindi l'AI aumenta il valore di infrastrutture come:

- metriche certificate;
- business glossary;
- entity definitions;
- time semantics;
- lineage;
- freshness metadata;
- owner;
- deprecation status;
- access policy;
- verified answer per domande critiche.

Il Capitolo 11 le ha trattate come disciplina di data modeling.

Il Capitolo 18 come disciplina operativa.

Qui ci interessa la conseguenza professionale:

> **la capacità di formalizzare il significato diventa una forma di leverage.**

## Il lavoro invisibile dietro una chat semplice

L'utente vede una casella di testo.

Perché quella casella possa rispondere bene, qualcuno deve avere stabilito:

- che cosa sia un customer;
- che cosa sia una transazione valida;
- quale date field governi il periodo;
- quale revenue sia certificata;
- quali metriche non possano essere combinate;
- quali asset siano deprecated;
- cosa fare quando il dato è stale;
- quale definizione usare se il termine è ambiguo.

Questo lavoro è meno spettacolare di un nuovo agente.

Ma spesso è ciò che decide se l'agente può essere affidabile.

## Caso simulato/composito: “top 20 clienti per revenue”

Un commerciale chiede:

> “Mostrami i 20 clienti con revenue più alta negli ultimi 12 mesi.”

Il sistema produce immediatamente una classifica.

L'azienda però ha:

- contratti annuali;
- professional services una tantum;
- crediti;
- invoice multi-entity;
- revenue recognition differita;
- ARR separato dalla recognized revenue.

Il sistema può usare un campo `invoice_amount` perfettamente valido.

La risposta può essere sintatticamente e matematicamente corretta.

Ma se la decisione riguarda account prioritari per il board, Finance potrebbe richiedere `recognized_revenue` o perfino `ARR`, a seconda del contesto.

L'errore non è di codice.

È **ontologico**.

## Semantic fluency come competenza di carriera

Un analyst con forte semantic fluency sa:

- trasformare parole business in entità e metriche verificabili;
- riconoscere quando due stakeholder usano lo stesso termine per concetti diversi;
- distinguere campo disponibile da concetto corretto;
- documentare eccezioni senza nasconderle nella query;
- progettare alternative nominate invece di metriche ambigue;
- collaborare con Finance, Product, Engineering e Governance sul significato;
- valutare se un agente sta usando l'asset autorevole.

Questa competenza attraversa Data Analyst e Analytics Engineer.

E può diventare ancora più importante quando l'accesso tecnico diventa più democratico.

## Da report builder a semantic product thinking

Una possibile evoluzione del ruolo è passare da:

> “costruisco il dashboard che risponde alla domanda”

verso:

> “rendo il dominio interrogabile senza costringere ogni consumer a ricostruirne il significato”.

Questo può includere:

- definire metric contracts;
- mantenere glossari;
- progettare semantic models;
- curare verified/certified answers;
- raccogliere failure query;
- osservare quali parole generano ambiguità;
- decidere quando una domanda richiede chiarimento invece di una risposta automatica.

## L'esempio pubblico già incontrato nel libro

Nel Capitolo 14 abbiamo visto un esempio documentato da Microsoft in cui Copilot per Power BI poteva usare una colonna `Birthday` per rispondere a una domanda temporale sul profitto se il semantic model non guidava sufficientemente il sistema.

Il caso è istruttivo perché mostra il punto centrale: un campo può essere reale, una query può essere valida e la risposta può comunque avere **semantica sbagliata**.

Microsoft oggi offre strumenti come AI instructions, AI data schemas e verified answers proprio per rendere più esplicito il contesto fornito ai sistemi conversazionali.

Fonte pubblica: https://learn.microsoft.com/en-us/power-bi/create-reports/copilot-prepare-data-ai

## Il vantaggio professionale

Nel mondo dei dashboard, un analyst poteva differenziarsi anche attraverso velocità nella costruzione delle viste.

Nel mondo conversazionale parte di quella velocità viene assorbita dal sistema.

Resta però una domanda molto più difficile:

> **“Come facciamo in modo che diecimila domande diverse attraversino un significato coerente?”**

Chi sa rispondere bene a questa domanda non sta soltanto costruendo metriche.

Sta progettando **la grammatica con cui persone e agenti parlano del business**.

> **Quando l'interfaccia diventa naturale, la semantica diventa infrastruttura e competenza strategica.**
