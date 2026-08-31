## 0.4 Escalation e stop condition: sapere quando l'AI deve fermarsi

Un sistema maturo non è quello che riesce sempre a continuare.

È quello che sa anche quando **non deve continuare**.

Gli agenti sono potenti perché possono concatenare azioni: leggere dati, generare codice, eseguire query, modificare file, chiamare API, aprire ticket, inviare messaggi e, in alcuni casi, intervenire direttamente su processi operativi.

Ogni passo aggiuntivo rende però più importante una domanda:

> **In quali condizioni l'agente può procedere da solo, e in quali deve fermarsi o chiedere review?**

### La stop condition si decide prima dell'incidente

Una stop condition inventata mentre il sistema sta già fallendo è un rimedio tardivo.

I limiti utili vengono definiti prima.

Per esempio:

- se il costo stimato supera una soglia, fermati;
- se una query modifica dati di produzione, richiedi approvazione;
- se due analisi producono conclusioni incompatibili, fai escalation;
- se mancano i dati minimi richiesti, non completare la raccomandazione;
- se manca una metrica certificata, non sostituirla con una definizione improvvisata;
- se freshness o completeness non rispettano lo SLA, blocca il processo;
- se un'azione coinvolge clienti, denaro o sistemi critici, richiedi approvazione umana;
- se il loop supera un numero massimo di iterazioni senza convergere, termina;
- se un controllo obbligatorio fallisce, non tentare di “aggirarlo” con una nuova spiegazione.

Le linee guida Microsoft sul rischio agentico raccomandano meccanismi di pausa e interruzione, limiti su loop e costi, least privilege e approvazione umana per azioni ad alto impatto.

Fonti:
- https://learn.microsoft.com/en-us/security/zero-trust/sfi/manage-agentic-risk
- https://learn.microsoft.com/en-us/azure/security/fundamentals/shared-responsibility-ai-agent

### Caso simulato/composito: l'agente che continua a ottimizzare

Un team growth costruisce un agente che rialloca automaticamente il budget pubblicitario.

Ogni ora il sistema:

1. legge conversioni e CAC;
2. identifica campagne inefficienti;
3. sposta budget verso quelle apparentemente migliori;
4. rivaluta il risultato un'ora dopo.

Una mattina il tracking iOS perde parte degli eventi di conversione.

L'agente interpreta il calo come peggioramento reale e riduce il budget iOS.

L'ora successiva osserva ancora meno conversioni. In parte perché il tracking continua a essere incompleto, in parte perché ora c'è anche meno traffico.

Il sistema legge il nuovo dato come conferma e riduce ancora il budget.

Si crea un feedback loop:

**errore di misurazione → azione → nuovo dato → conferma apparente → azione più forte**

Dopo sei iterazioni, il budget iOS è sceso del 70%.

Il problema non è che l'agente non sapesse ottimizzare.

Il problema è che nessuno aveva definito quando l'ottimizzazione doveva diventare sospetta.

Un sistema più robusto avrebbe richiesto:

- freshness e completeness del tracking;
- confronto con una fonte indipendente;
- limite massimo alla variazione oraria;
- approval sopra una soglia di budget;
- stop automatico in presenza di drift anomalo o telemetria incompleta.

### Escalation non significa fallimento

Un sistema professionale non deve essere costretto a produrre sempre una risposta.

Può avere almeno tre esiti legittimi:

1. **proceed** — evidenza sufficiente e azione entro il mandato;
2. **review** — serve giudizio umano o un controllo aggiuntivo;
3. **stop** — le condizioni minime non sono soddisfatte.

Quando un agente dice:

> “Non posso concludere in modo affidabile con le informazioni disponibili.”

può stare eseguendo correttamente il proprio mandato.

L'errore è progettare sistemi nei quali l'unico output ammesso sia una risposta assertiva.

### Una matrice di autorità

La quantità di autonomia dovrebbe cambiare con il tipo di attività.

| Tipo di attività | Autonomia indicativa | Review |
|---|---|---|
| generare una bozza SQL | alta | campionamento e test |
| leggere metriche certificate | alta | controlli automatici |
| pubblicare un dashboard interno | media | review dell'owner |
| cambiare definizione di un KPI | bassa | approvazione di governance |
| modificare prezzi | molto bassa | approvazione business |
| bloccare clienti o servizi | molto bassa | review umana obbligatoria |
| trasferire denaro | minima | controlli forti e segregazione dei compiti |

La tabella non è una policy universale. Serve a rendere concreta la regola:

> **L'autonomia deve essere proporzionata all'impatto, alla reversibilità e alla capacità di rilevare rapidamente un errore.**

### Essere al timone significa poter interrompere

Governare un agente significa mantenere la capacità di:

- vedere che cosa sta facendo;
- sapere con quali strumenti e permessi;
- interromperlo;
- revocare accessi;
- annullare o compensare azioni quando possibile;
- ricostruire ciò che è successo.

Se un sistema autonomo non può essere osservato, fermato o auditato, il suo comportamento non è realmente sotto controllo.

Da qui un paradosso importante:

> **più autonomia concediamo, più dobbiamo investire nei meccanismi che rendono quell'autonomia governabile.**

L'autonomia non elimina la governance. La rende più importante.
