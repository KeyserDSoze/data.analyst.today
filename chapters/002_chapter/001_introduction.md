# Capitolo 2 - Dal problema di business al problema analitico

> Una buona analisi non comincia dai dati. Comincia da una decisione che deve essere presa e dall'incertezza che impedisce di prenderla bene.

Nel capitolo precedente abbiamo stabilito una tesi fondamentale: gli strumenti cambiano, ma il nucleo del lavoro analitico rimane sorprendentemente stabile. In questo capitolo trasformiamo quella tesi in un metodo operativo.

Un Data Analyst riceve raramente domande perfette. Più spesso riceve richieste come:

- "Le vendite stanno andando male, capiamo perché."
- "Ci serve una dashboard clienti."
- "Vorremmo capire se il marketing funziona."
- "Perché gli utenti abbandonano?"
- "Quali prodotti dovremmo spingere?"
- "Possiamo prevedere il prossimo trimestre?"

Queste frasi sono importanti, ma non sono ancora problemi analitici ben definiti. Sono segnali di un bisogno decisionale.

Il compito dell'analista è trasformarle in qualcosa che possa essere investigato con dati, misure e metodi appropriati.

Una formulazione utile del processo è:

**Contesto -> Decisione -> Domanda -> Definizioni -> Dati -> Metodo -> Evidenza -> Raccomandazione -> Azione -> Verifica**

L'ordine conta. Se saltiamo direttamente ai dati rischiamo di ottimizzare la parte sbagliata del problema.

## Business Understanding prima della tecnica

La logica non è nuova. Il framework CRISP-DM colloca il *Business Understanding* prima del *Data Understanding*: prima si chiariscono obiettivi e requisiti, poi si entra nei dati. Questo principio resta valido anche quando SQL, Python e persino parte dell'esplorazione possono essere assistiti dall'AI.

L'AI accelera la produzione di query e analisi. Non può però sapere automaticamente quale decisione aziendale conta davvero, quale compromesso sia accettabile o quale definizione di successo sia corretta per l'organizzazione.

## Obiettivo del capitolo

Alla fine di questo capitolo dovresti essere in grado di prendere una richiesta vaga e produrre un vero **analytical brief** contenente almeno:

1. problema di business;
2. decisione da supportare;
3. stakeholder e destinatari;
4. domanda analitica principale;
5. sotto-domande;
6. metriche e definizioni;
7. popolazione e granularità;
8. periodo temporale;
9. ipotesi iniziali;
10. dati necessari;
11. limiti e rischi;
12. criterio con cui l'analisi verrà considerata utile.

Questo documento, anche se breve, è spesso più importante della prima query SQL.

## Riferimenti

- IBM, *CRISP-DM / Business Understanding*: https://www.ibm.com/docs/en/spss-modeler/saas?topic=understanding-business-overview
