## 19.3 Natural language analytics e semantic layer
Una delle promesse più visibili dell’AI applicata ai dati è semplice:

> “Chiunque potrà fare domande ai dati in linguaggio naturale.”

La promessa è potente.

Ma nasconde un problema.

Il linguaggio naturale è ambiguo.

I dati aziendali lo sono ancora di più.

## La domanda non è il problema

Immaginiamo che un manager chieda:

> “Qual è il churn in Francia?”

Un sistema può generare rapidamente una query.

Ma cosa significa churn?

- cancellazione volontaria?
- account non più pagante?
- logo churn?
- revenue churn?
- gross churn?
- net churn?
- mensile?
- annualizzato?
- su clienti attivi a inizio periodo?
- su tutti i clienti che hanno generato revenue nel periodo?

La difficoltà non è tradurre una frase in SQL.

È collegare la frase alla **semantica ufficiale dell’organizzazione**.

## Perché il semantic layer diventa più importante con l’AI

Quando gli utenti interrogano direttamente i dati tramite linguaggio naturale, ogni ambiguità semantica diventa un rischio di scala.

Se dieci analyst interpretano in modo diverso la stessa metrica, il problema è già serio.

Se diecimila query generate automaticamente usano interpretazioni diverse, il problema diventa sistemico.

Per questo metriche certificate, definizioni, lineage, owner e dimensioni coerenti diventano infrastruttura essenziale per l’AI.

L’AI non elimina il bisogno di modellazione semantica.

Lo amplifica.

## Dal dashboard al conversational analytics

Una parte delle interazioni con i dati potrebbe spostarsi da:

- dashboard statiche;
- report predefiniti;
- filtri manuali;

verso:

- domande conversazionali;
- esplorazione iterativa;
- agenti che attraversano metriche e dimensioni;
- spiegazioni generate dinamicamente.

Questo cambia il ruolo dell’analista.

Meno tempo può essere speso nel costruire decine di viste molto simili.

Più tempo deve essere investito nel rendere il sistema interrogabile in modo sicuro.

## Caso realistico: “revenue per cliente”

Un commerciale chiede a un assistente:

> “Mostrami i 20 clienti con revenue più alta negli ultimi 12 mesi.”

Il sistema produce una classifica.

Il risultato sembra corretto.

Ma l’azienda ha:

- contratti annuali;
- servizi professionali una tantum;
- crediti;
- revenue recognition differita;
- fatture multi-entity.

La domanda “revenue” può significare:

- bookings;
- billed revenue;
- recognized revenue;
- ARR;
- cash collected.

Senza semantic layer, l’assistente non ha un errore sintattico.

Ha un errore ontologico.

Sta rispondendo a una domanda diversa da quella che l’organizzazione pensa di aver posto.

## Il nuovo lavoro invisibile

Paradossalmente, più l’interfaccia diventa semplice, più aumenta il lavoro dietro le quinte necessario per renderla affidabile.

Servono:

- metric definitions;
- entity resolution;
- business glossary;
- data contracts;
- lineage;
- access control;
- freshness metadata;
- quality signals;
- certified dimensions;
- deprecation policies.

L’utente finale vede una casella di testo.

Dietro quella casella deve esistere un sistema semantico robusto.

## Un’opportunità professionale

Questo crea uno spazio interessante per Data Analyst e Analytics Engineer.

Chi conosce bene il business può diventare il ponte tra:

- linguaggio umano;
- metriche;
- modelli dati;
- sistemi AI.

È un lavoro meno visibile della costruzione di una dashboard, ma potenzialmente più strategico.

> **Nel mondo del natural-language analytics, chi controlla la semantica controlla una parte importante della qualità delle decisioni.**
