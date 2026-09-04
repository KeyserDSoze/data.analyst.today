## 1.9 Una metrica non è un numero: è una scelta

Una delle idee più importanti dell'analisi dati è anche una delle più facili da dimenticare quando il numero compare già pronto in un dashboard:

> **Una metrica non viene semplicemente trovata nei dati. Viene definita.**

Il database contiene eventi, importi, date, stati, identificativi e relazioni. Concetti come `cliente attivo`, `fatturato`, `conversione`, `retention`, `churn`, `margine` o `engagement` richiedono invece una definizione che colleghi quegli elementi a un fenomeno di business.

Questa è la ragione per cui molte discussioni apparentemente tecniche non si risolvono controllando una formula. Sono discussioni sul significato.

### La definizione corretta dipende dalla decisione

Prendiamo **cliente attivo**. In un prodotto digitale usato ogni giorno potremmo considerare attivo chi ha svolto una certa azione negli ultimi 30 giorni. In un e-commerce stagionale la stessa finestra potrebbe classificare come inattivi clienti perfettamente normali. In un servizio in abbonamento potrebbe contare soprattutto lo stato contrattuale; in un business con acquisti annuali potremmo aver bisogno di una finestra molto più lunga.

Nessuna di queste definizioni è vera in assoluto. Ognuna costruisce una popolazione diversa e quindi rende possibili decisioni diverse.

La metrica è, in questo senso, una **formalizzazione del modello mentale con cui interpretiamo il business**. Se il modello mentale è sbagliato per la decisione, una formula implementata alla perfezione produrrà un numero preciso ma poco utile.

### “Fatturato” diventa ambiguo non appena proviamo a calcolarlo

Un concetto apparentemente semplice come il fatturato costringe subito a scegliere. Dobbiamo decidere se contano ordini creati, pagati o completati; quale data assegna l'evento al periodo; se l'importo è lordo o netto; come trattare IVA, sconti, resi, cancellazioni e costi di spedizione; quale tasso usare per le valute e in quale momento applicarlo.

Due dashboard possono quindi partire dallo stesso ecosistema dati e mostrare numeri diversi perché rappresentano due momenti diversi del processo economico. Una può essere adatta a monitorare domanda commerciale, l'altra alla riconciliazione finanziaria.

Quando i numeri divergono la prima domanda non dovrebbe essere soltanto:

> “Quale query è sbagliata?”

Dovrebbe essere anche:

> **“Quale fenomeno stanno cercando di rappresentare le due query?”**

Questo evita di risolvere come bug tecnico ciò che in realtà è un conflitto di definizione.

### Nei rapporti, il denominatore decide chi stiamo descrivendo

Le metriche percentuali sono particolarmente insidiose perché una formula molto semplice può nascondere scelte profonde sulla popolazione.

Prendiamo una conversion rate espressa come:

**conversion rate = acquisti / visite**

Il significato cambia a seconda di ciò che chiamiamo visita: sessione, utente unico, visita a una pagina prodotto o arrivo al checkout. Cambia ancora se “acquisto” significa ordine creato, pagamento autorizzato, pagamento completato o ordine non successivamente cancellato.

Il denominatore è spesso il punto in cui una metrica apparentemente stabile cambia identità. Se diciamo che il 20% dei clienti ha effettuato un secondo acquisto, dobbiamo decidere chi abbia avuto una reale opportunità di riacquistare. Inserire nel denominatore clienti acquisiti ieri non è una piccola imperfezione statistica: significa attribuire a una popolazione un comportamento che non ha ancora avuto il tempo di manifestare.

Questo è il motivo per cui numeratore, denominatore e popolazione non sono dettagli di implementazione. **Definiscono a chi stiamo attribuendo il risultato.**

### Valori assoluti e relativi rispondono a domande diverse

Supponiamo che un prodotto guadagni €10.000 di ricavi, pari a una crescita del 2%, mentre un altro guadagna €5.000 ma cresce del 40%.

Quale sta andando meglio?

La domanda non ha risposta finché non sappiamo quale decisione dobbiamo prendere. Se ci interessa il contributo economico assoluto, il primo movimento può essere più importante. Se cerchiamo un segnale di accelerazione, il secondo può meritare più attenzione. Se il margine è diverso, entrambe le letture possono cambiare ancora.

Una percentuale non è più “vera” di un valore assoluto. È una lente diversa. Il problema nasce quando la lente viene scelta dopo avere visto quale storia rende più convincente.

### Una metrica può cambiare il sistema che osserva

Finché una metrica descrive soltanto un fenomeno, possiamo valutarla soprattutto per la sua capacità di rappresentarlo. Quando diventa un obiettivo, entra nel sistema degli incentivi e può modificarlo.

Un call center valutato soltanto sulla durata media delle chiamate può imparare a chiudere più rapidamente invece di risolvere meglio i problemi. Un team commerciale premiato soltanto sul fatturato può privilegiare vendite a basso margine. Un prodotto digitale ottimizzato esclusivamente per il tempo trascorso nell'app può aumentare engagement senza aumentare soddisfazione o valore per l'utente.

L'analista deve quindi porsi due domande diverse: *questa metrica rappresenta bene il fenomeno?* e *quale comportamento rende conveniente se l'organizzazione la trasforma in un target?*

Una buona metrica descrittiva può diventare una pessima metrica di performance.

### Dalla query personale al contratto semantico

Quando una metrica è critica e viene usata da più team, la sua definizione non dovrebbe dipendere dalla memoria di chi ha scritto la prima query. Serve un artefatto condiviso che trasformi le scelte implicite in un contratto verificabile.

Una scheda minima può essere organizzata così:

| Elemento | Che cosa deve rendere esplicito |
|---|---|
| **Definizione** | che cosa significa la metrica in linguaggio di business |
| **Formula** | come viene calcolata e quali sono numeratore e denominatore |
| **Popolazione** | chi è incluso, chi è escluso e perché |
| **Grain e tempo** | unità di analisi, granularità e data che determina il periodo |
| **Sorgenti** | dati di origine e trasformazioni critiche |
| **Eccezioni** | resi, cancellazioni, missing value, casi limite |
| **Ownership** | chi può approvare o modificare la definizione |
| **Versione** | quando la definizione è cambiata e se il confronto storico resta valido |
| **Limiti d'uso** | decisioni o contesti nei quali la metrica non dovrebbe essere usata |

In un'organizzazione matura questa documentazione diventa un vero **contratto semantico**: non dice soltanto come calcolare un numero, ma che cosa l'organizzazione promette che quel numero significhi.

Questo contratto è utile anche quando l'esecuzione diventa più automatica. Un agente può generare in pochi secondi una query chiamata `customer_retention_rate`; se però nessuno ha definito retention, il nome della variabile nasconde una scelta che non è ancora stata presa.

### Semantic layer: quando il significato diventa infrastruttura

Le moderne piattaforme analytics formalizzano questo problema attraverso modelli e layer semantici: definizioni condivise di metriche, relazioni, descrizioni e logica di business riutilizzabili da report, strumenti e applicazioni differenti.

La documentazione Microsoft sui semantic model di Power BI e sulla preparazione dei modelli per Copilot è un esempio concreto di questa direzione. La qualità dell'interazione in linguaggio naturale dipende da un modello curato, con nomi, relazioni, descrizioni e contesto sufficientemente chiari da ridurre l'ambiguità.[^ms-semantic][^ms-copilot]

Il **Capitolo 11** entrerà nell'implementazione delle metriche nel data modeling e nel semantic layer; i **Capitoli 12 e 18** affronteranno architettura, ownership e governance. Qui ci interessa la conseguenza analitica:

> **se il significato di una metrica non è condiviso, automatizzare le query non risolve il problema. Automatizza l'incoerenza.**

Prima di fidarci di una metrica critica dovremmo quindi riuscire a ricostruire il suo contratto: quale fenomeno rappresenta, chi entra nella popolazione, quale data determina il periodo, se la definizione è cambiata, chi la possiede e soprattutto per quali decisioni è abbastanza buona.

Il numero è l'ultima riga di questo processo, non la prima.

---

### Fonti e approfondimenti

[^ms-semantic]: Microsoft Learn, *Power BI semantic models*. https://learn.microsoft.com/en-us/power-bi/connect-data/semantic-models-third-party
[^ms-copilot]: Microsoft Learn, *Optimize your semantic model for Copilot in Power BI*. https://learn.microsoft.com/en-us/power-bi/create-reports/copilot-evaluate-data
