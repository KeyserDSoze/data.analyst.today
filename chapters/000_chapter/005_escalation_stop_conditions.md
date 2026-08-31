# 0.4 Escalation e stop conditions: sapere quando l'AI deve fermarsi

Un sistema maturo non è quello che riesce sempre a continuare.

È quello che sa anche quando **non deve continuare**.

Gli agenti sono potenti proprio perché possono concatenare azioni: leggere dati, generare codice, eseguire query, modificare file, chiamare API, aprire ticket, inviare messaggi, proporre decisioni.

Ma ogni catena autonoma introduce una domanda di governance:

> **In quali condizioni l'agente può procedere da solo, e in quali deve fermarsi?**

## Stop condition prima del problema

La stop condition non dovrebbe essere inventata durante l'incidente.

Va definita prima.

Esempi:

- se il costo stimato supera una soglia, fermati;
- se una query modifica dati di produzione, richiedi approvazione;
- se due agenti producono conclusioni incompatibili, escalation;
- se il confidence score scende sotto una soglia, non emettere raccomandazioni;
- se manca una metrica certificata, non sostituirla con una definizione improvvisata;
- se il dato è stale oltre lo SLA, blocca la decisione;
- se un'azione coinvolge clienti o denaro, human approval obbligatoria;
- se l'agente supera N iterazioni senza convergere, termina il loop.

Microsoft, nelle linee guida recenti sul rischio agentico, raccomanda esplicitamente meccanismi affidabili per mettere in pausa o interrompere gli agenti, limiti su loop, step e costi, approvazione umana per azioni ad alto impatto e least privilege sugli strumenti disponibili.

Fonti:
- https://learn.microsoft.com/en-us/security/zero-trust/sfi/manage-agentic-risk
- https://learn.microsoft.com/en-us/azure/security/fundamentals/shared-responsibility-ai-agent

## Caso realistico: l'agente che continua a ottimizzare

Un team growth costruisce un agente che ottimizza automaticamente il budget pubblicitario.

Ogni ora:

1. legge conversioni e CAC;
2. identifica campagne inefficienti;
3. sposta budget verso le campagne migliori;
4. rivaluta dopo un'ora.

Durante una mattina, il tracking iOS perde parte degli eventi di conversione.

L'agente interpreta il calo come peggioramento reale.

Riduce il budget iOS.

L'ora successiva vede ancora meno conversioni, perché ora c'è anche meno traffico.

Riduce ancora.

Il sistema ha creato un feedback loop:

**measurement error → action → nuovo dato → conferma apparente → azione più forte**

Dopo sei iterazioni, il budget iOS è sceso del 70%.

Non mancava intelligenza.

Mancava una stop condition.

Un sistema migliore avrebbe richiesto:

- freshness e completeness del tracking;
- confronto con fonti indipendenti;
- limite massimo alla variazione oraria;
- approval sopra una soglia di budget;
- stop automatico in caso di drift anomalo.

## Escalation non significa fallimento

Quando un agente dice:

> “Non posso concludere in modo affidabile con le informazioni disponibili.”

non sta fallendo.

Sta eseguendo correttamente il proprio mandato.

Un sistema pericoloso è quello che deve sempre dare una risposta.

Un sistema professionale può produrre tre esiti:

1. **proceed** — evidenza sufficiente, azione entro autorità;
2. **review** — serve giudizio umano;
3. **stop** — condizioni minime non soddisfatte.

## Authority matrix

Per ogni agente possiamo definire una matrice semplice.

| Tipo di attività | Autonomia | Review |
|---|---|---|
| generare una bozza SQL | alta | campionamento |
| leggere metriche certificate | alta | controlli automatici |
| pubblicare un dashboard interno | media | review owner |
| cambiare definizione KPI | bassa | approvazione governance |
| modificare prezzi | molto bassa | approvazione business |
| bloccare clienti | molto bassa | review umana obbligatoria |
| trasferire denaro | minima | controlli forti e segregazione |

Questa matrice rende concreta una regola fondamentale:

> **L'autonomia deve essere proporzionata alla reversibilità e all'impatto dell'azione.**

## Il diritto di interrompere

Essere al timone significa anche mantenere la capacità di:

- vedere cosa sta facendo l'agente;
- interromperlo;
- revocare accessi;
- annullare o compensare azioni;
- ricostruire ciò che è successo.

Se un sistema autonomo non può essere osservato, fermato o auditato, non è realmente sotto controllo.

## Il paradosso dell'autonomia

Più autonomia concediamo, più dobbiamo investire in:

- confini;
- audit;
- rollback;
- escalation;
- osservabilità;
- controlli indipendenti.

L'autonomia non elimina la governance.

La rende più importante.