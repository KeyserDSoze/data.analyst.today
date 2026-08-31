## 12.14 Costi cloud e architettura proporzionata: non tutto deve essere real time

Una buona architettura non e' quella con piu' componenti. E' quella che soddisfa il requisito decisionale con il livello di complessita' e costo appropriato.

### Caso realistico: BrightMart

BrightMart e' un retailer regionale con 180 punti vendita.

Il management chiede una piattaforma "real time" per monitorare:

- vendite;
- margine;
- stock;
- resi;
- performance promozionale.

La prima proposta tecnica include streaming continuo, code di eventi, cluster always-on, serving layer a bassa latenza e dashboard aggiornate ogni pochi secondi.

Costo stimato: circa 1,1 milioni di euro l'anno.

Durante il discovery emerge pero' che:

- i direttori di negozio controllano le vendite ogni ora;
- il pricing cambia una volta al giorno;
- il finance usa dati giornalieri consolidati;
- solo gli stock-out di alcuni prodotti critici richiedono alert entro 10 minuti.

La soluzione viene ridisegnata.

```text
vendite e margine -> micro-batch ogni 30 minuti
finance -> batch giornaliero
stock critico -> near real time
archivio storico -> object storage
semantic model -> refresh differenziato per dominio
```

Il costo scende drasticamente senza ridurre la qualita' delle decisioni.

### Freshness ha un prezzo

In generale, ridurre la latenza richiede piu' infrastruttura, piu' osservabilita' e piu' complessita' operativa.

Passare da:

```text
24 ore -> 1 ora
```

puo' essere relativamente semplice.

Passare da:

```text
1 ora -> 1 secondo
```

puo' cambiare completamente l'architettura.

La domanda corretta non e':

> possiamo farlo in real time?

ma:

> quale valore decisionale otteniamo riducendo la latenza?

### Costi invisibili

Il costo cloud non e' solo compute.

Comprende anche:

- storage;
- scansione dei dati;
- egress;
- orchestrazione;
- cluster inattivi;
- log e osservabilita';
- ambienti duplicati;
- copie ridondanti;
- query ad hoc inefficienti;
- costo umano di gestione.

### Un esempio analitico

Un team crea una dashboard che esegue 40 query su una fact table da 12 TB a ogni refresh.

Refresh ogni 5 minuti.

La dashboard viene consultata in media da 14 persone al giorno.

Il problema non e' soltanto tecnico. E' economico.

Una possibile riprogettazione:

- pre-aggregazioni;
- partition pruning;
- semantic cache;
- refresh meno frequente;
- separazione tra dashboard operative e analisi esplorativa.

### Build vs buy vs managed service

Un altro asse di costo riguarda la gestione.

Una tecnologia open source puo' avere costo di licenza molto basso ma richiedere:

- infrastruttura;
- patching;
- competenze specialistiche;
- on-call;
- capacity planning.

Un servizio gestito puo' costare di piu' per unita' di compute ma ridurre molto il costo operativo.

Non esiste una risposta universale.

### Total Cost of Ownership

Per confrontare architetture conviene pensare al **TCO**:

```text
TCO = infrastruttura + licenze + persone + manutenzione + incidenti + inefficienza + switching cost
```

La formula non deve essere perfetta. Serve a ricordare che il prezzo del servizio cloud e' solo una parte della decisione.

### Overengineering

Un sintomo tipico di overengineering e' quando la soluzione e' piu sofisticata del problema.

Esempio:

- 20.000 righe al giorno;
- report aggiornato una volta ogni mattina;
- 5 utenti;
- pipeline streaming distribuita multi-cluster.

La tecnologia puo' essere eccellente e la scelta comunque sbagliata.

### Underengineering

Esiste anche l'errore opposto.

Un foglio Excel condiviso manualmente puo' funzionare per 5 persone e fallire quando:

- gli utenti diventano 200;
- serve audit;
- arrivano dati sensibili;
- la logica deve essere riutilizzata;
- gli aggiornamenti devono essere affidabili.

### Framework di scelta

Prima di introdurre un nuovo componente chiedere:

1. qual e' il volume?
2. qual e' la latenza necessaria?
3. quante persone lo useranno?
4. qual e' il costo di un dato in ritardo?
5. qual e' il costo di un sistema piu' complesso?
6. quali competenze abbiamo davvero?
7. quanto deve scalare nei prossimi 12-24 mesi?
8. possiamo partire piu' semplici?

**La maturita' architetturale non si misura dal numero di tecnologie. Si misura dalla capacita' di scegliere la complessita' minima sufficiente.**
