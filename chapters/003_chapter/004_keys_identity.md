## 3.3 Chiavi e identità: sapere che cosa è davvero unico

Una chiave serve a identificare un'entità o un'osservazione. In analisi dati è facile trattare una colonna chiamata `id` come se fosse automaticamente affidabile. Non lo è.

Possiamo avere:

- una chiave primaria tecnica generata dal sistema;
- una chiave di business, come numero ordine o codice fiscale;
- una chiave composta, formata da più colonne;
- un identificatore valido solo dentro una specifica sorgente;
- un identificatore che cambia nel tempo;
- record duplicati che violano l'unicità attesa.

### Unicità attesa vs unicità osservata

Se `customer_id` dovrebbe identificare un solo cliente, dobbiamo verificarlo.

```sql
SELECT customer_id, COUNT(*)
FROM customers
GROUP BY customer_id
HAVING COUNT(*) > 1;
```

Questa query non dimostra che l'identità sia corretta, ma verifica almeno che il vincolo di unicità atteso sia rispettato nel dataset.

La qualità "uniqueness" è una delle dimensioni comunemente adottate nei framework di data quality. IBM la definisce come la capacità di assicurare che valori o record distinti non compaiano più volte quando non dovrebbero.  
Fonte: IBM, *Data quality dimensions*: https://www.ibm.com/think/topics/data-quality-dimensions

### Identità non significa persona

Un errore frequente è assumere che `customer_id` corrisponda a una persona fisica.

In realtà potrebbe identificare:

- un account;
- un contratto;
- un indirizzo email;
- un dispositivo;
- una relazione cliente-azienda;
- una persona deduplicata da un sistema MDM;
- una semplice registrazione CRM.

Quindi, prima di calcolare metriche "per cliente", dobbiamo sapere che cosa il sistema considera cliente.

### Chiavi surrogate e chiavi naturali

Nei data warehouse è comune usare chiavi surrogate, cioè identificatori tecnici creati appositamente per il modello analitico. Sono utili perché separano la rappresentazione analitica dagli identificatori operativi e permettono di gestire cambiamenti storici delle dimensioni.

L'analista non deve diventare necessariamente un esperto di modellazione dimensionale in questa fase, ma deve capire che:

> **un identificatore tecnico e un'identità di business non sono la stessa cosa.**

### Referential integrity

Se una tabella ordini contiene `customer_id`, dovremmo aspettarci che quell'identificatore esista nella tabella clienti, salvo eccezioni deliberate.

Gli ordini senza cliente corrispondente sono esempi di violazioni di integrità referenziale. Possono derivare da:

- latenze di caricamento;
- cancellazioni;
- sistemi sorgenti non sincronizzati;
- errori nelle pipeline;
- dati storici incompleti;
- regole di business che consentono clienti anonimi.

Il punto non è semplicemente trovare il record anomalo. È capire **perché esiste** e se modifica il significato dell'analisi.
