## 0.6 Livelli di fiducia: non tutti gli output AI meritano lo stesso trattamento

Uno degli errori più comuni nell'uso dell'AI è applicare lo stesso livello di fiducia e di review a qualsiasi output. Una bozza di email interna e una raccomandazione che modifica un prezzo possono essere prodotte dallo stesso modello, ma non hanno lo stesso profilo di rischio. Lo stesso vale per una query esplorativa rispetto a una query che alimenta il reporting finanziario, o per un brainstorming di ipotesi rispetto a una conclusione causale.

La domanda corretta, quindi, non è «quanto mi fido dell'AI?». È **quanta fiducia devo richiedere a questo output, dato l'uso che ne farò?**

La risposta dipende prima di tutto da quattro dimensioni. L'**impatto** misura quanto costa sbagliare; la **reversibilità** quanto sia semplice annullare l'azione; l'**incertezza** quanto sia fragile l'evidenza; l'**osservabilità** quanto rapidamente ci accorgeremmo dell'errore. A queste si aggiungono, quando rilevanti, il contesto normativo, la sensibilità dei dati e la portata dell'azione. Il punto è che lo stesso sistema può essere perfettamente accettabile in un contesto e inadeguato in un altro.

### Un modello operativo a quattro livelli

I livelli seguenti non sono una certificazione formale. Servono a collegare l'uso dell'output al tipo di controllo che dovrebbe precederlo.

| Livello | Uso tipico | Profilo di rischio | Controllo atteso |
|---|---|---|---|
| **1 — Draft** | riassunti, prime versioni di query, ipotesi, documentazione iniziale | errore poco costoso e facilmente reversibile | review leggera |
| **2 — Assisted execution** | SQL su metriche certificate, data profiling, test di qualità, grafici, classificazione preliminare di anomalie | attività operative entro confini chiari | controlli automatici, tracciabilità, campionamento |
| **3 — Decision support** | forecast per budgeting, ranking clienti, analisi pricing, driver di churn, prioritizzazione operativa | l'output influenza decisioni importanti | review umana, validazione, alternative, incertezza, owner chiaro |
| **4 — Consequential action** | modificare prezzi, allocare budget, bloccare transazioni, cancellare account, cambiare configurazioni di produzione | azione diretta su persone, denaro o sistemi critici | limiti di autorità, logging, approval, rollback, stop condition, controlli indipendenti |

Il passaggio da un livello al successivo non descrive un modello «più intelligente». Descrive una conseguenza più importante collegata al suo output. Per questo una demo convincente non è sufficiente a giustificare autonomia: ciò che dobbiamo validare non è soltanto la qualità della risposta, ma il sistema di decisione nel quale quella risposta verrà inserita.

### Caso simulato/composito: stesso score, tre rischi diversi

Un modello stima la probabilità che un cliente abbandoni. Nel primo uso lo score serve soltanto a ordinare una lista che un account manager esamina manualmente. Un falso positivo costa soprattutto tempo: il modello aiuta a prioritizzare, ma non decide che cosa accadrà al cliente.

Nel secondo uso lo stesso score concede automaticamente uno sconto del 30%. La previsione non è cambiata, ma la conseguenza sì. Un errore produce ora un costo economico diretto e può anche insegnare ai clienti comportamenti indesiderati se il meccanismo di incentivo diventa prevedibile.

Nel terzo uso lo score viene impiegato per negare automaticamente un servizio. Il profilo di rischio cambia ancora: entrano in gioco impatto sulle persone, policy, possibili discriminazioni e requisiti di governance molto più forti. La tecnologia sottostante è la stessa; è la decisione collegata all'output a determinare quanta fiducia e quanta supervisione dobbiamo richiedere.

> **Non esiste un livello di fiducia “del modello” separato dal contesto in cui quel modello viene usato.**

### L'autonomia si guadagna gradualmente

Per la stessa ragione, un sistema AI non dovrebbe passare direttamente da prototipo a piena autonomia soltanto perché una demo funziona. La fiducia operativa si costruisce attraverso una progressione nella quale ogni fase produce nuova evidenza.

1. **Offline evaluation.** Il sistema viene testato su casi storici e scenari noti, dove possiamo confrontare l'output con un riferimento.
2. **Shadow mode.** Produce risultati nel contesto reale ma non agisce, permettendoci di osservare errori e distribuzioni senza conseguenze operative.
3. **Confronto con decisioni umane.** Misuriamo accordi, disaccordi e failure mode invece di trattare l'umano o il modello come gold standard automatico.
4. **Autonomia su casi semplici.** Il sistema agisce entro un perimetro limitato, ben osservabile e reversibile.
5. **Escalation sui casi ambigui.** L'autonomia include la capacità di riconoscere quando non è appropriato procedere.
6. **Espansione graduale.** L'autorità cresce soltanto dopo evidenza operativa sufficiente e controlli adeguati al nuovo impatto.

Questa sequenza si guadagna il diritto di essere numerata perché descrive una progressione: saltare un passaggio significa rinunciare a una parte dell'evidenza che serve per giustificare il successivo. Microsoft propone esplicitamente una governance degli agenti proporzionata al rischio e all'impatto delle azioni che possono compiere.

Fonte:
- https://learn.microsoft.com/en-us/agents/center-of-excellence/govern-agents-risk

Anche un sistema molto ben validato può comunque sbagliare. La fiducia professionale non coincide con la promessa di rischio zero. Consiste nel sapere quale rischio stiamo accettando, perché è compatibile con l'uso previsto, quali segnali ci avviseranno che il sistema sta uscendo dal comportamento atteso, chi dovrà intervenire e come potremo recuperare o limitare il danno.

> **La fiducia professionale non è credere che il sistema non sbaglierà. È sapere come ci accorgeremo che sta sbagliando e cosa faremo dopo.**
