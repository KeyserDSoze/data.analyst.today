## 3.2 Granularità: il livello a cui il mondo è stato registrato

La granularità, o *grain*, descrive il livello di dettaglio rappresentato da una tabella.

È uno dei concetti più importanti dell'intero mestiere analitico perché determina quali domande possiamo porre senza introdurre errori.

Una tabella vendite può avere granularità:

- una riga per ordine;
- una riga per riga d'ordine;
- una riga per prodotto e giorno;
- una riga per negozio, prodotto e giorno;
- una riga per cliente e mese.

Tutte possono essere chiamate informalmente "tabella vendite", ma non sono intercambiabili.

Microsoft, nella documentazione sul dimensional modeling per workload analitici, descrive le fact table come tabelle che registrano misure associate a osservazioni o eventi e sottolinea che esse conservano valori a uno specifico livello granulare insieme alle chiavi delle dimensioni. Questa idea è alla base del corretto disegno dei modelli analitici.  
Fonte: Microsoft Learn, *Dimensional modeling in Microsoft Fabric*: https://learn.microsoft.com/en-us/fabric/data-warehouse/dimensional-modeling-overview

### Dichiarare il grain prima delle metriche

Una buona pratica è scrivere esplicitamente:

> Una riga rappresenta un prodotto presente in un singolo ordine.

oppure:

> Una riga rappresenta il saldo di un prodotto in un magazzino alla fine di ogni giornata.

Questa frase rende immediatamente visibili molti rischi.

Se la tabella è a livello di riga d'ordine e contiene anche `order_total`, quel valore potrebbe essere ripetuto su tutte le righe dell'ordine. Sommarlo produrrebbe un fatturato gonfiato.

Esempio:

| order_id | product | line_amount | order_total |
|---|---|---:|---:|
| 1 | A | 40 | 100 |
| 1 | B | 60 | 100 |

La somma corretta di `line_amount` è 100. La somma ingenua di `order_total` è 200.

Il database non segnala alcun errore. SQL esegue perfettamente il calcolo richiesto. L'errore è concettuale.

### Il problema delle join che cambiano il grain

La granularità può anche cambiare durante una join.

Supponiamo di avere:

- `customers`: una riga per cliente;
- `orders`: molte righe per cliente.

Dopo una join tra clienti e ordini, i dati del cliente vengono replicati per ogni ordine. Questo è corretto dal punto di vista relazionale, ma significa che il risultato non è più a livello cliente: è a livello ordine.

Se poi sommiamo un attributo del cliente, come `annual_income`, otteniamo valori privi di significato.

### Domande da porre sempre

Prima di lavorare con una tabella chiediamoci:

- Qual è il grain dichiarato?
- Quali colonne identificano una riga?
- Il grain è stabile nel tempo?
- Una join può moltiplicare le righe?
- Le metriche presenti sono additive a questo livello?
- Esistono valori già aggregati che rischiamo di aggregare una seconda volta?

Comprendere il grain significa capire **a quale risoluzione il sistema informativo ha osservato il fenomeno**.
