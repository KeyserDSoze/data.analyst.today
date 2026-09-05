## 2.10 Dall'evidenza necessaria ai requisiti dati

Una volta chiarita la domanda, il passaggio corretto non è chiedere “quali tabelle abbiamo?”. È chiedere **quali osservazioni ci servirebbero per distinguere le ipotesi che contano** e, soltanto dopo, capire se quelle osservazioni esistono nei sistemi disponibili.

L'ordine cambia il progetto. Se partiamo dalle tabelle, tendiamo a formulare domande compatibili con ciò che è facile interrogare. Se partiamo dall'evidenza necessaria, diventano visibili anche i segnali mancanti, i proxy e i limiti che potrebbero impedire una conclusione forte.

Supponiamo di voler capire perché la retention dei nuovi clienti sia diminuita negli ultimi sei mesi. “Servono i dati clienti” non è un requisito. Per ricostruire il fenomeno potrebbe essere indispensabile un identificativo coerente nel tempo, insieme a data e canale di acquisizione, transazioni, rinnovi e cancellazioni. Per distinguere ipotesi sul prodotto potrebbero servire eventi di utilizzo; per pricing e promozioni, storico delle condizioni commerciali; per l'esperienza post-acquisto, ticket o tempi di consegna. Se sospettiamo onboarding differenti, serve soprattutto sapere **a quale esperienza ogni cliente è stato realmente esposto**.

Ogni dato dovrebbe quindi avere una ragione analitica. Se non sappiamo quale ipotesi, metrica o confronto abilita, probabilmente non è un requisito prioritario.

## Required, useful e proxy

Una classificazione semplice aiuta a progettare il lavoro senza fingere che tutte le fonti abbiano lo stesso valore.

Un dato **required** è necessario per rispondere alla domanda primaria. Se manca, dobbiamo cambiare fonte, raccogliere nuova informazione oppure ridurre la pretesa dell'analisi. Un dato **useful** aumenta profondità o consente segmentazioni importanti, ma la prima fase può procedere senza. Un **proxy** sostituisce invece un concetto che non osserviamo direttamente e deve portarsi dietro la consapevolezza della propria imperfezione.

Questa distinzione diventa concreta quando il costo dei dati è alto. Se una fonte useful richiede settimane di engineering, potremmo iniziare con la parte required e decidere in seguito, usando il Value of Information, se la profondità aggiuntiva giustifica il costo. Se manca un dato required, invece, non possiamo semplicemente riempire il buco con una variabile comoda senza cambiare la domanda.

Una conclusione professionale può quindi arrivare **prima** dell'analisi:

> “Con i dati attuali possiamo descrivere il fenomeno, ma non distinguere tra le ipotesi A e B. Per farlo servirebbe misurare X.”

Non è un fallimento. È un gap informativo identificato prima che venga promesso un livello di evidenza impossibile.

## Anche il grain è un requisito

Il Capitolo 3 approfondirà grain, chiavi, lineage e qualità. Nel brief dobbiamo già dichiarare a quale livello serve l'informazione, perché una fonte al grain sbagliato può rendere impossibile il confronto che abbiamo progettato.

| Dato | Significato | Grain richiesto | Perché serve | Priorità |
|---|---|---|---|---|
| customer_id | identità coerente del cliente | cliente | coorti e repeat purchase | required |
| order_date | data dell'ordine valido | ordine | finestre di acquisto | required |
| acquisition_channel | canale iniziale | cliente | test mix acquisizione | useful |
| delivery_delay | giorni oltre promessa | spedizione | ipotesi experience | useful |
| satisfaction | proxy esperienza | survey response | ipotesi CX | proxy |

Se, per esempio, il delivery delay è disponibile soltanto come media mensile per paese, non possiamo attribuirlo in modo credibile al singolo cliente per spiegare repeat purchase individuale. Il dato esiste, ma non al grain necessario alla pretesa che vorremmo sostenere.

Per una fonte critica dovremmo sapere almeno che cosa rappresenta, quale grain e chiave usa, quanto storico copre, con quale latenza diventa completa, quali trasformazioni principali subisce, chi la possiede e se tracking o definizioni sono cambiati nel periodo. Non serve trasformare il brief in un data catalog; serve valutare fattibilità e rischio prima che il piano dipenda da una fonte che non può sostenere ciò che le chiediamo.

Quando emerge un gap, le opzioni sono diverse: usare una fonte esistente migliore, costruire una trasformazione, accettare un proxy dichiarato, raccogliere nuovo dato, ridurre la domanda oppure rimandare una conclusione più forte a una fase successiva. Sono scelte del progetto analitico, non semplici dettagli di engineering.

Il campo del brief resta riusabile:

```text
Dato / segnale:
Ruolo: required / useful / proxy
Grain richiesto:
Fonte disponibile:
Owner:
Storico/freshness:
Problemi noti:
Gap e piano di mitigazione:
```

Il Capitolo 3 riprenderà da questo punto e ci costringerà a una domanda più dura: le fonti che abbiamo dichiarato disponibili rappresentano davvero ciò che il brief presume, e con quale affidabilità?

> **I requisiti dati non nascono dal catalogo delle tabelle. Nascono dalle osservazioni che servono per mettere alla prova il modello del problema.**
