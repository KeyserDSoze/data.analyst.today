## 3.3 Chiavi e identità: unico nel database non significa unico nel mondo reale

Una chiave distingue record o entità all'interno di un sistema. Ma il fatto che una colonna si chiami `id`, o che sia formalmente unica, non garantisce che rappresenti l'identità di business necessaria alla nostra domanda.

Possiamo avere chiavi tecniche generate dal sistema, chiavi di business, chiavi composte, identificatori validi soltanto dentro una sorgente, ID che cambiano nel tempo oppure più ID per la stessa entità. Il problema non è la varietà delle implementazioni. È l'errore che nasce quando trattiamo una convenzione tecnica come se definisse automaticamente “cliente”, “ordine” o “persona”.

Supponiamo che una tabella sia dichiarata a livello cliente. Se `customer_id` non è unico, la reazione corretta non è cancellare tutte le righe ripetute. Dobbiamo capire quale assunzione è falsa: forse esistono versioni della stessa anagrafica, forse l'ID identifica un account e non una persona, oppure la stessa entità è stata ricreata dopo una migrazione.

Il Government Data Quality Framework definisce la **uniqueness** come l'assenza di duplicazioni rispetto alle entità che dovrebbero essere rappresentate una sola volta. La definizione è utile proprio perché sposta il problema dal confronto byte-per-byte al significato dell'entità.[^gov-dq-uniqueness]

## L'identità dipende dal fenomeno che vogliamo misurare

Un `customer_id` può identificare una persona, un account, un contratto, un'azienda, un profilo CRM o persino un dispositivo. Queste interpretazioni possono essere tutte corrette nel sistema che le ha generate e produrre metriche molto diverse.

Se una persona possiede due account, una metrica “per customer_id” può contarla due volte. Se più persone condividono un account familiare, un singolo ID può rappresentare più individui. Se una migrazione assegna un nuovo identificatore alla stessa persona, un cliente esistente può sembrare improvvisamente acquisito da zero.

Prima di calcolare clienti unici, retention o lifetime value dobbiamo quindi completare una frase più impegnativa di “la chiave è customer_id”:

> **Nel contesto di questa analisi, consideriamo la stessa entità quando...**

È qui che la definizione tecnica incontra quella di business.

## False split e false merge

L'identity resolution può sbagliare in due direzioni opposte. Un **false split** tratta la stessa entità come due soggetti diversi: per esempio, un acquisto guest e un acquisto successivo dopo registrazione non vengono collegati. In quel caso il secondo ordine può sembrare un nuovo cliente.

Un **false merge** fa l'opposto: fonde entità diverse. Due dipendenti che utilizzano lo stesso indirizzo amministrativo di un'azienda potrebbero diventare artificialmente un unico cliente se deduplichiamo soltanto per email.

Ridurre il numero di record non è quindi l'obiettivo. L'obiettivo è rappresentare correttamente l'identità rilevante per la domanda. Una regola troppo aggressiva abbassa artificialmente il numero di entità; una troppo prudente lo gonfia. Entrambe distorcono metriche di frequenza, retention e valore.

## Anche i collegamenti raccontano il processo

L'identità emerge anche nelle relazioni tra dataset. Se `orders.customer_id` non trova corrispondenza nell'anagrafica, possiamo avere guest checkout legittimi, latenze tra sistemi, dati storici incompleti, anonimizzazioni, chiavi provenienti da sorgenti differenti oppure veri errori di pipeline.

Un record orfano non è quindi automaticamente “sporco”. È un'informazione sul modo in cui il processo collega — o non collega — le entità.

Nei warehouse incontreremo inoltre chiavi surrogate che separano l'identità tecnica del modello analitico da quella operativa e possono supportare la storia delle dimensioni. La progettazione verrà approfondita nel Capitolo 11; qui basta conservare il principio fondamentale:

> **Una chiave identifica una rappresentazione. Prima di usarla in una metrica dobbiamo sapere che cosa rappresenta, dove è unica, quanto è stabile e quali regole collegano identità provenienti da sistemi diversi.**

Questa conoscenza è ciò che impedisce a un conteggio perfettamente eseguito di diventare una stima sbagliata del mondo reale.

---

### Fonte

[^gov-dq-uniqueness]: UK Government Data Quality Hub, *The Government Data Quality Framework*. https://www.gov.uk/government/publications/the-government-data-quality-framework/the-government-data-quality-framework
