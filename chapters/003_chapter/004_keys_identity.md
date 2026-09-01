## 3.3 Chiavi e identità: unico nel database non significa unico nel mondo reale

Una chiave serve a distinguere record o entità. Ma una colonna chiamata `id` non garantisce automaticamente che l'identità rappresentata sia quella di cui abbiamo bisogno.

Possiamo incontrare:

- una chiave tecnica generata dal sistema;
- una chiave di business, come un numero ordine;
- una chiave composta da più colonne;
- un identificatore valido solo dentro una sorgente;
- un identificatore che cambia nel tempo;
- più identificatori per la stessa entità;
- lo stesso identificatore riutilizzato impropriamente per entità diverse.

### Unicità attesa e unicità osservata

Se una tabella dichiara una riga per cliente, `customer_id` dovrebbe normalmente essere unico a quel grain.

La prima verifica è semplice: il numero di record e il numero di identificatori distinti coincidono?

Se non coincidono, non dobbiamo dedurre immediatamente che "ci sono duplicati da cancellare". Dobbiamo capire quale assunzione è falsa.

Il Government Data Quality Framework britannico definisce la **uniqueness** come il grado con cui il dataset contiene una sola rappresentazione per ciascuna entità che dovrebbe essere unica. Sottolinea inoltre che due record possono rappresentare un duplicato anche se alcuni campi differiscono.[^gov-dq-uniqueness]

### Identità tecnica e identità di business

Un `customer_id` potrebbe identificare:

- una persona;
- un account;
- un contratto;
- un'azienda;
- una relazione persona-azienda;
- un profilo CRM;
- un dispositivo;
- un indirizzo email.

Queste non sono distinzioni accademiche.

Se un cliente possiede due account, una metrica "per customer_id" può contarlo due volte. Se due persone condividono un account familiare, un singolo ID può rappresentare più persone. Se l'identificatore cambia dopo una migrazione, la stessa persona può sembrare un nuovo cliente.

Per questo, prima di calcolare retention, frequenza o lifetime value, dobbiamo completare una seconda frase:

> **Nel nostro sistema, un cliente è identificato come...**

### Due errori opposti: split e merge

Nell'identity resolution esistono almeno due errori concettuali opposti.

**False split:** la stessa entità viene trattata come due entità diverse.

Esempio: un cliente acquista una volta come guest e una volta dopo essersi registrato. Se i due record non vengono collegati, il secondo acquisto può sembrare un nuovo cliente.

**False merge:** due entità diverse vengono fuse in una sola.

Esempio: due dipendenti utilizzano lo stesso indirizzo email amministrativo di un'azienda. Deduplicare soltanto per email potrebbe trasformarli artificialmente in un unico cliente.

Il punto non è ottenere il minor numero possibile di record. È rappresentare correttamente l'identità rilevante per la domanda.

### Referential integrity: i collegamenti che ci aspettiamo esistono davvero?

Se una tabella ordini contiene `customer_id`, possiamo aspettarci che l'identificatore sia presente nell'anagrafica clienti, salvo eccezioni deliberate.

Quando non accade, le possibili cause includono:

- guest checkout legittimo;
- latenze tra sistemi;
- dati storici incompleti;
- cancellazioni o anonimizzazioni;
- chiavi provenienti da sorgenti differenti;
- errori di pipeline.

Un record orfano non è automaticamente un errore. È una domanda sul processo.

### Chiavi surrogate: ciò che l'analista deve sapere

Nei warehouse è comune incontrare chiavi surrogate create dal modello analitico. Sono utili, tra le altre cose, per separare l'identità tecnica del warehouse dalle chiavi operative e per gestire la storia delle dimensioni.

La progettazione approfondita arriverà nel Capitolo 11. Qui basta fissare una regola:

> **Una chiave identifica una rappresentazione. Non assumere che quella rappresentazione coincida automaticamente con la persona, l'ordine o il fenomeno che hai in mente.**

Prima di usare un identificatore in una metrica, verifica quindi:

- che cosa identifica;
- dove è unico;
- se è stabile nel tempo;
- se può essere condiviso;
- se può cambiare;
- quali regole collegano identità provenienti da sistemi diversi.

[^gov-dq-uniqueness]: UK Government Data Quality Hub, *The Government Data Quality Framework*. https://www.gov.uk/government/publications/the-government-data-quality-framework/the-government-data-quality-framework