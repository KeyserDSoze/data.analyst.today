## 1.9 Una metrica non è un numero: è una scelta

Una delle idee più importanti dell'analisi dati è anche una delle più facili da sottovalutare:

> **Una metrica non viene semplicemente trovata nei dati. Viene definita.**

Il database contiene eventi, importi, date, stati, identificativi e relazioni. Concetti come `cliente attivo`, `fatturato`, `conversione`, `retention`, `churn`, `margine` o `engagement` richiedono invece una definizione che colleghi quegli elementi a un fenomeno di business.

Molte discussioni apparentemente tecniche sono quindi discussioni sul significato.

### Lo stesso concetto può avere più definizioni ragionevoli

Prendiamo **cliente attivo**.

Potremmo definirlo come:

- un cliente che ha effettuato almeno un acquisto negli ultimi 30 giorni;
- un cliente che ha acquistato negli ultimi 90 giorni;
- un cliente con almeno due acquisti nell'ultimo anno;
- un cliente che ha effettuato il login nell'ultimo mese;
- un cliente con un abbonamento non scaduto;
- un cliente che continua a generare ricavi.

Qual è la definizione corretta?

Dipende dal fenomeno e dalla decisione.

Per un servizio in abbonamento lo stato contrattuale può essere centrale. Per un e-commerce stagionale una finestra di 30 giorni può classificare come inattivi clienti perfettamente normali. Per un prodotto acquistato una volta l'anno sarebbe assurdo applicare la stessa soglia di un servizio utilizzato ogni giorno.

La metrica è quindi una **formalizzazione del modello mentale con cui interpretiamo il business**.

### “Fatturato” diventa ambiguo appena proviamo a implementarlo

Anche un concetto apparentemente semplice richiede scelte:

- ordini creati, pagati o completati?
- data dell'ordine, del pagamento, della spedizione o della contabilizzazione?
- importo lordo o netto?
- IVA inclusa o esclusa?
- sconti incorporati?
- resi e cancellazioni sottratti?
- costi di spedizione inclusi?
- valute convertite con quale tasso e in quale data?

Due dashboard possono partire dallo stesso ecosistema dati e mostrare numeri diversi perché implementano definizioni diverse.

Quando accade, non dobbiamo chiedere soltanto:

> “Quale query è sbagliata?”

ma anche:

> **“Quale fenomeno stanno cercando di rappresentare le due query?”**

### Numeratore, denominatore e popolazione

Le metriche basate su rapporti meritano particolare attenzione.

Supponiamo di voler misurare:

**conversion rate = acquisti / visite**

Che cosa conta come visita?

- sessione?
- utente unico?
- visita a una pagina prodotto?
- utente arrivato al checkout?

E che cosa conta come acquisto?

- ordine creato?
- pagamento autorizzato?
- pagamento completato?
- ordine non successivamente cancellato?

La formula può rimanere identica mentre il significato cambia radicalmente.

Il denominatore è spesso la parte più trascurata. Se diciamo che il 20% dei clienti ha effettuato un secondo acquisto, chi entra nel 100% iniziale?

Tutti i clienti storici? Solo quelli acquisiti abbastanza tempo fa da avere avuto una reale opportunità di riacquisto? Una coorte specifica?

Includere clienti acquisiti ieri in una metrica di repeat purchase non è un piccolo dettaglio tecnico. Cambia la popolazione a cui stiamo attribuendo un comportamento.

### Valori assoluti e relativi raccontano domande diverse

Un prodotto può mostrare:

- +€10.000 di ricavi;
- +2% di crescita.

Un altro:

- +€5.000 di ricavi;
- +40% di crescita.

Quale sta andando meglio?

Dipende dalla decisione. Potremmo voler massimizzare contributo assoluto, crescita, margine, quota di mercato o riduzione del rischio.

Una percentuale non è più “vera” di un valore assoluto. Risponde a una domanda diversa.

### Le metriche non osservano soltanto il comportamento: possono modificarlo

Quando una metrica diventa un obiettivo, influenza incentivi e comportamenti.

Se un call center viene valutato soltanto sulla durata media delle chiamate, gli operatori possono avere un incentivo a chiudere rapidamente anche quando il problema non è risolto.

Se una squadra commerciale viene premiata soltanto sul fatturato, può privilegiare vendite a basso margine o clienti costosi da servire.

Se un prodotto digitale ottimizza soltanto il tempo trascorso nell'app, può aumentare engagement senza aumentare soddisfazione o valore per l'utente.

Per questo l'analista deve chiedersi non soltanto:

> “Come calcolo questa metrica?”

ma anche:

> **“Che comportamento rende conveniente quando diventa un obiettivo?”**

Una buona metrica descrittiva può diventare una cattiva metrica di performance se crea incentivi distorti.

### Dalla definizione individuale al contratto organizzativo

Quando una metrica è critica e viene riutilizzata da molte persone, non dovrebbe dipendere dalla memoria di un singolo analista.

Una scheda minima dovrebbe contenere almeno:

1. nome e definizione in linguaggio naturale;
2. formula;
3. numeratore e denominatore;
4. popolazione inclusa ed esclusa;
5. grain e granularità temporale;
6. fonte dati;
7. regole per resi, cancellazioni, missing value ed eccezioni;
8. owner della definizione;
9. eventuali cambiamenti di versione;
10. casi in cui la metrica non dovrebbe essere usata.

In un'organizzazione matura questa documentazione può diventare un vero **contratto semantico**: non soltanto “come calcoliamo il numero”, ma “che cosa promettiamo che quel numero significhi”.

### Semantic layer e coerenza organizzativa

Le moderne piattaforme analytics cercano di formalizzare questo problema attraverso modelli e layer semantici: definizioni centralizzate di metriche, relazioni e logica di business riutilizzabili in report e applicazioni differenti.

La documentazione Microsoft sui semantic model di Power BI e sulla preparazione dei modelli per Copilot è un esempio reale documentato di questa direzione: terminologia, relazioni e metriche curate diventano parte dell'infrastruttura con cui utenti e sistemi AI interpretano i dati.

Il **Capitolo 11** entrerà nell'implementazione delle metriche nel data modeling e nel semantic layer; i **Capitoli 12 e 18** affronteranno architettura, ownership e governance.

Qui ci basta la conseguenza analitica:

> **se il significato di una metrica non è condiviso, automatizzare le query non risolve il problema. Automatizza l'incoerenza.**

### Domande da fare prima di fidarsi di una metrica

- Che cosa misura realmente?
- Quale fenomeno vuole rappresentare?
- Qual è l'unità di analisi?
- Qual è la popolazione eleggibile?
- Chi entra nel denominatore?
- Quali eventi sono esclusi?
- Quale data determina il periodo?
- È confrontabile tra periodi e segmenti?
- La definizione è cambiata nel tempo?
- Quale comportamento incentiva?
- Chi possiede la definizione?
- In quali decisioni non dovrebbe essere usata?

Un agente AI può generare in pochi secondi una query chiamata `customer_retention_rate`.

Ma se nessuno ha definito che cosa significhi retention per quell'azienda, il nome della query sta soltanto rendendo invisibile una decisione concettuale non ancora presa.

### Fonti e approfondimenti

- Microsoft Learn, *Power BI semantic models*: https://learn.microsoft.com/en-us/power-bi/connect-data/semantic-models-third-party
- Microsoft Learn, *Get started with metric sets*: https://learn.microsoft.com/en-gb/power-bi/create-reports/get-started-metrics
- Microsoft Learn, *Optimize your semantic model for Copilot in Power BI*: https://learn.microsoft.com/en-us/power-bi/create-reports/copilot-evaluate-data
