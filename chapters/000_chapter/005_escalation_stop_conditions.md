## 0.4 Escalation e stop condition: sapere quando l'AI deve fermarsi

Un sistema maturo non è quello che riesce sempre a continuare. È quello che sa anche quando **non deve continuare**.

Gli agenti sono potenti proprio perché possono concatenare azioni: leggere dati, generare codice, eseguire query, modificare file, chiamare API, aprire ticket, inviare messaggi e, in alcuni casi, intervenire direttamente su processi operativi. Questa capacità riduce il costo del passaggio dall'analisi all'azione, ma rende più importante stabilire in anticipo il confine fra ciò che il sistema può fare autonomamente e ciò che richiede review.

La domanda non va posta dopo l'incidente. Va incorporata nel mandato: **in quali condizioni l'agente può procedere da solo, e in quali deve fermarsi o chiedere review?**

### Le stop condition si progettano prima

Una stop condition inventata mentre il sistema sta già fallendo è un rimedio tardivo. I limiti utili vengono definiti quando il workflow viene progettato, insieme agli accessi, ai controlli e alla definition of done.

Una checklist operativa può includere condizioni come queste:

- se il costo stimato supera una soglia, fermati;
- se una query modifica dati di produzione, richiedi approvazione;
- se due analisi producono conclusioni incompatibili, fai escalation;
- se mancano i dati minimi richiesti, non completare la raccomandazione;
- se manca una metrica certificata, non sostituirla con una definizione improvvisata;
- se freshness o completeness non rispettano lo SLA, blocca il processo;
- se un'azione coinvolge clienti, denaro o sistemi critici, richiedi approvazione umana;
- se il loop supera un numero massimo di iterazioni senza convergere, termina;
- se un controllo obbligatorio fallisce, non tentare di aggirarlo con una nuova spiegazione.

Questa lista resta intenzionalmente strutturata perché è un artefatto operativo: può essere trasformata in policy, test, guardrail o criteri di escalation. Il principio che la tiene insieme è uno solo. Un agente non deve essere valutato soltanto per la capacità di raggiungere un obiettivo, ma anche per la capacità di riconoscere quando le condizioni minime per perseguirlo non sono più soddisfatte.

Le linee guida Microsoft sul rischio agentico raccomandano meccanismi affidabili di pausa e interruzione, limiti all'autonomia, least privilege e approvazione umana per azioni ad alto impatto.

Fonti:
- https://learn.microsoft.com/en-us/security/zero-trust/sfi/manage-agentic-risk
- https://learn.microsoft.com/en-us/azure/security/fundamentals/shared-responsibility-ai-agent

### Caso simulato/composito: l'agente che continua a ottimizzare

Un team growth costruisce un agente che rialloca automaticamente il budget pubblicitario. Ogni ora il sistema legge conversioni e CAC, individua campagne inefficienti, sposta budget verso quelle apparentemente migliori e rivaluta il risultato nell'ora successiva. Finché la misurazione è sana, il loop sembra ragionevole: osserva, agisce, misura di nuovo.

Una mattina, però, il tracking iOS perde parte degli eventi di conversione. L'agente interpreta il calo osservato come un peggioramento reale e riduce il budget iOS. Un'ora dopo vede ancora meno conversioni. In parte perché il tracking continua a essere incompleto, in parte perché ora c'è anche meno traffico. Il sistema non distingue le due cause: tratta il nuovo dato come conferma dell'ipotesi iniziale e riduce ancora il budget.

Si forma così un circuito auto-rinforzante:

**errore di misurazione → azione → nuovo dato → conferma apparente → azione più forte**

Dopo sei iterazioni, il budget iOS è sceso del 70%. Il problema non è che l'agente non sapesse ottimizzare. Il problema è che l'ottimizzazione non aveva un concetto esplicito di «dato troppo inaffidabile per continuare».

Un sistema più robusto avrebbe verificato freshness e completeness del tracking prima di modificare il budget, confrontato il segnale con una fonte indipendente e limitato la variazione massima consentita in un'ora. Superata una soglia di budget avrebbe richiesto approval; davanti a drift anomalo o telemetria incompleta avrebbe interrotto automaticamente il loop. Questi controlli non rendono l'agente meno utile. Impediscono che la sua capacità di agire trasformi un errore di osservazione in un errore operativo crescente.

### Escalation non significa fallimento

Un sistema professionale non deve essere costretto a produrre sempre una risposta assertiva. Può avere almeno tre esiti legittimi:

1. **proceed** — l'evidenza è sufficiente e l'azione rientra nel mandato;
2. **review** — serve giudizio umano o un controllo aggiuntivo;
3. **stop** — le condizioni minime non sono soddisfatte.

Questa triade è una sequenza decisionale, non un catalogo. Prima chiediamo se le condizioni minime sono soddisfatte; se non lo sono, ci fermiamo. Se lo sono ma l'incertezza o l'impatto superano l'autorità concessa, facciamo escalation. Solo quando evidenza e mandato sono entrambi adeguati il sistema procede.

Per questo una frase come «non posso concludere in modo affidabile con le informazioni disponibili» può rappresentare l'esecuzione corretta del mandato. L'errore di design è costruire un sistema nel quale l'unico output ammesso sia una risposta netta.

### Una matrice di autorità

La quantità di autonomia dovrebbe cambiare con il tipo di attività. Non esiste una policy universale, ma una matrice rende visibile il principio meglio di una serie di eccezioni sparse.

| Tipo di attività | Autonomia indicativa | Review |
|---|---|---|
| generare una bozza SQL | alta | campionamento e test |
| leggere metriche certificate | alta | controlli automatici |
| pubblicare un dashboard interno | media | review dell'owner |
| cambiare definizione di un KPI | bassa | approvazione di governance |
| modificare prezzi | molto bassa | approvazione business |
| bloccare clienti o servizi | molto bassa | review umana obbligatoria |
| trasferire denaro | minima | controlli forti e segregazione dei compiti |

La regola che emerge è semplice: **l'autonomia deve essere proporzionata all'impatto, alla reversibilità e alla capacità di rilevare rapidamente un errore**. Un'azione facilmente annullabile e ben osservabile può tollerare più autonomia di un'azione irreversibile i cui effetti diventano visibili soltanto dopo giorni.

Essere al timone significa quindi mantenere non soltanto la capacità di autorizzare, ma anche quella di interrompere. Dobbiamo poter vedere che cosa sta facendo l'agente, con quali strumenti e permessi, fermarlo, revocare accessi e ricostruire ciò che è successo. Quando possibile dobbiamo anche poter annullare o compensare le azioni già eseguite.

Se un sistema autonomo non può essere osservato, fermato o auditato, il suo comportamento non è realmente sotto controllo. Da qui nasce un paradosso solo apparente:

> **Più autonomia concediamo, più dobbiamo investire nei meccanismi che rendono quell'autonomia governabile.**

L'autonomia non elimina la governance. La rende più importante.
