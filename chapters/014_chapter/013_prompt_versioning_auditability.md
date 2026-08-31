# 14.12 Prompt, versioning e auditability: se cambia l'istruzione, cambia il sistema

Nei workflow AI il prompt non è solo testo. È parte della logica del sistema.

Se cambiamo da:

> “Calcola la revenue mensile.”

a:

> “Calcola la revenue mensile escludendo ordini cancellati e rimborsati, usando `order_paid_at` e la metrica certificata `net_revenue`.”

non abbiamo semplicemente riscritto una frase: abbiamo modificato il comportamento atteso del sistema.

Questo significa che prompt, tool disponibili, modello, versione del semantic layer e criteri di valutazione dovrebbero essere trattati come artefatti versionabili.

## Cosa registrare

Per un workflow analitico serio può essere utile conservare:

- versione del prompt o delle istruzioni;
- modello utilizzato;
- tool disponibili;
- dataset e viste accessibili;
- timestamp;
- versione del semantic model;
- query generate;
- output intermedi;
- eventuali correzioni umane;
- risultato finale consegnato.

Non serve registrare tutto indiscriminatamente. Serve poter ricostruire il percorso quando il rischio o il valore del risultato lo giustificano.

## Caso realistico: il KPI cambia senza che nessuno tocchi la dashboard

Un team finance usa un agente per generare ogni lunedì una sintesi automatica.

Per sei mesi il prompt contiene:

> “Usa la revenue riconosciuta nel periodo.”

Dopo una modifica, qualcuno semplifica:

> “Analizza la revenue della settimana.”

L'agente inizia a usare `invoice_amount`, che include importi emessi ma non ancora riconosciuti secondo le regole finance.

La dashboard non cambia. Il warehouse non cambia. Il codice della pipeline non cambia.

Cambia una frase.

Il CFO vede un miglioramento del 6,4% che non esiste secondo la definizione contabile ufficiale.

Senza versioning del prompt, ricostruire l'origine dell'errore diventa difficile.

## Il prompt come codice morbido

Il prompt è meno deterministico del codice tradizionale, ma proprio per questo richiede disciplina:

1. versionare cambi rilevanti;
2. collegarli a eval regression;
3. testare casi critici prima del rollout;
4. conservare esempi di output atteso;
5. definire rollback;
6. separare prompt di sviluppo e produzione.

## Auditability non significa burocrazia infinita

Un'analisi esplorativa personale non richiede lo stesso livello di tracciamento di un agente che modifica prezzi, manda comunicazioni o produce metriche per il board.

Il principio è proporzionale:

**più il risultato è difficile da correggere, costoso o consequenziale, più dobbiamo essere in grado di ricostruire come è stato prodotto.**

Questo vale per il codice, per i dati e ora anche per le istruzioni date all'AI.

### Fonti

- NIST AI RMF Generative AI Profile: https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence
- Microsoft Learn, Responsible AI for agents: https://learn.microsoft.com/en-us/agents/center-of-excellence/responsible-ai
