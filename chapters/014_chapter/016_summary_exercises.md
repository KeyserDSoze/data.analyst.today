# 14.15 Sintesi ed esercizi: dall'assistente al sistema sotto responsabilità

L'AI-assisted analytics non è un singolo strumento. È un nuovo modo di organizzare il lavoro analitico.

Possiamo usare l'AI per:

- tradurre linguaggio naturale in SQL;
- scrivere e spiegare codice;
- generare ipotesi;
- esplorare dataset;
- costruire grafici;
- proporre modelli;
- cercare anomalie;
- documentare pipeline;
- revisionare query;
- orchestrare agenti specializzati.

Ma ogni aumento di capacità introduce una domanda di governance:

> chi controlla ciò che viene prodotto, con quali standard e con quale responsabilità?

Il principio finale del capitolo è semplice:

**non dobbiamo dimostrare di aver eseguito personalmente ogni passaggio; dobbiamo essere in grado di spiegare, verificare e difendere il sistema che ha prodotto il risultato.**

## Esercizio 1 — SQL plausibile ma semanticamente errato

Un agente riceve la richiesta:

> “Calcola il revenue per cliente nel 2026.”

Genera una query che unisce `orders`, `order_items` e `payments`, somma `payment_amount` e raggruppa per cliente.

La query gira e produce risultati plausibili.

Domande:

1. quali rischi di grain e cardinalità controlleresti?
2. quali confronti useresti per verificare il totale?
3. quali definizioni di revenue potrebbero essere implicite?
4. come modificheresti il prompt per ridurre il rischio?
5. quali controlli automatizzeresti?

## Esercizio 2 — L'AI trova una “causa”

Un agente osserva che i clienti che usano una nuova funzione hanno retention D90 del 64%, contro il 41% degli altri utenti.

Conclude:

> “La nuova funzione aumenta la retention di 23 punti percentuali.”

Costruisci una risposta professionale che:

- distingua associazione ed effetto causale;
- proponga almeno quattro confondenti plausibili;
- descriva un esperimento o quasi-esperimento credibile;
- spieghi cosa può fare l'AI e cosa deve decidere l'analista.

## Esercizio 3 — Cinque agenti e un'unica conclusione

Un team usa cinque agenti:

1. data quality agent;
2. SQL agent;
3. anomaly agent;
4. causal-reasoning agent;
5. executive-summary agent.

I primi quattro producono risultati parzialmente in conflitto. L'executive agent sintetizza comunque una raccomandazione netta.

Progetta:

- gerarchia degli agenti;
- criteri di escalation;
- evidenze minime richieste;
- stop condition;
- punti di approvazione umana;
- audit trail necessario.

## Esercizio 4 — Dati sensibili

Un responsabile HR vuole analizzare testo libero delle exit interview con un LLM esterno.

Definisci un processo che minimizzi il rischio prima dell'analisi. Indica:

- quali dati non invieresti;
- quali trasformeresti;
- quale livello di accesso daresti all'agente;
- quali output richiederebbero revisione umana;
- come documenteresti il workflow.

## Esercizio 5 — Eval set per un agente analitico

Devi validare un agente che risponde a domande commerciali interrogando il warehouse.

Crea almeno 15 casi di test distribuiti tra:

- metriche semplici;
- join difficili;
- finestre temporali;
- dati mancanti;
- metriche ambigue;
- richieste non autorizzate;
- causal language;
- richieste che dovrebbero generare una domanda di chiarimento.

Per ogni caso definisci il criterio di successo.

## Esercizio 6 — Il forecast perfetto che non puoi usare

Un agente costruisce un modello con performance eccellente usando una feature derivata da un dato disponibile solo 48 ore dopo il momento della previsione.

Spiega:

- perché è leakage;
- perché il modello può sembrare ottimo offline;
- come ricostruire correttamente il dataset;
- quale baseline useresti;
- come impedirai che l'errore ricompaia.

## Esercizio 7 — “L'ha fatto l'AI”

Durante un meeting, il CFO scopre che una previsione inviata la settimana precedente era errata del 18%.

L'analista risponde:

> “Il file è stato generato automaticamente dall'agente.”

Riscrivi la gestione dell'incidente come dovrebbe avvenire in un'organizzazione matura. Includi:

- ownership;
- diagnosi;
- contenimento;
- rollback;
- root cause;
- modifica dei controlli;
- comunicazione al management.

## Esercizio 8 — Caso finale: DeltaHome

DeltaHome è un retailer europeo da €620 milioni di revenue. Il lunedì mattina un sistema agentico segnala:

- revenue settimanale: -7,6%;
- conversion: -9,2%;
- mobile checkout: principale driver;
- causa proposta: nuova UI introdotta venerdì.

Il sistema ha automaticamente:

- interrogato il warehouse;
- segmentato per paese e device;
- controllato anomaly history;
- letto le release note;
- generato una raccomandazione di rollback.

Prima di autorizzare il rollback scopri che:

- il feed pagamenti di un provider è in ritardo di 11 ore;
- la nuova UI è attiva solo sul 25% degli utenti;
- un altro provider di pagamento mostra conversion stabile;
- il calo apparente è concentrato esattamente dove manca il feed.

Prepara il memo che invieresti al VP Product.

Il memo deve separare:

1. fatti osservati;
2. problemi di qualità del dato;
3. ipotesi ancora plausibili;
4. decisioni da non prendere ancora;
5. controlli necessari;
6. condizioni che giustificherebbero davvero il rollback.

## Conclusione

L'AI sposta il baricentro del lavoro.

Prima gran parte del tempo era speso nell'esecuzione. Sempre più spesso l'esecuzione sarà prodotta da sistemi automatici.

Il valore dell'analista si sposta verso:

**framing → semantica → supervisione → verifica → giudizio → responsabilità.**

Questa trasformazione merita una discussione più ampia della sola tecnica. Per questo torneremo sul tema in un capitolo dedicato alla mentalità dell'analista che lavora con molti agenti: non come passeggero dell'automazione, ma come persona che resta al timone.
