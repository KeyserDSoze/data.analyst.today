## 3.14 Data contract: smettere di scoprire i cambiamenti quando è troppo tardi

Molti problemi di qualità del dato non nascono nel team analytics. Nascono a monte, quando un'applicazione cambia il modo in cui produce un evento, rinomina un campo, modifica un enum o smette di valorizzare una proprietà.

Se nessuno comunica il cambiamento, la pipeline può continuare a funzionare tecnicamente e produrre risultati semanticamente sbagliati.

Un **data contract** rende esplicite le aspettative tra chi produce e chi consuma un dato.

Può specificare, per esempio:

- nome dell'evento o della tabella;
- significato dei campi;
- tipo dei dati;
- valori ammessi;
- nullability;
- chiavi;
- granularità;
- frequenza di aggiornamento;
- SLA attesi;
- owner;
- regole per i breaking change.

### Caso simulato: il conversion rate crolla del 22% in una notte

Un marketplace monitora quotidianamente il checkout conversion rate.

Lunedì mattina il valore passa dal **3,8% al 2,9%**.

Marketing pensa a un problema di traffico. Product pensa a un bug nel checkout. Il management chiede un'analisi urgente.

L'analista verifica le vendite assolute: sono normali.

Poi controlla il denominatore della conversione, cioè le sessioni che hanno iniziato il checkout. È aumentato improvvisamente del 31%.

Dopo alcune ore si scopre la causa: durante una release del frontend l'evento `checkout_started` era stato spostato dal click su "Vai al pagamento" all'apertura automatica del drawer del carrello.

Il nome dell'evento non era cambiato.

La pipeline non era rotta.

Il dashboard non era rotto.

Era cambiato **il significato del dato**.

Il team analytics non era stato informato.

### Come avrebbe aiutato un data contract

Il contratto avrebbe potuto definire:

```text
Event: checkout_started
Definition: fired once when the user explicitly enters step 1 of checkout
Grain: one event per checkout attempt
Required fields: session_id, user_id, timestamp, cart_value
Owner: Checkout Product Team
Breaking changes: require analytics review before production
```

Cambiare il punto di emissione dell'evento avrebbe costituito una modifica semantica e quindi richiesto una revisione.

### Data contract non significa burocrazia infinita

Non ogni tabella ha bisogno di un documento di venti pagine.

Il principio è più semplice:

> Le proprietà del dato da cui dipendono decisioni importanti non devono essere implicite.

Più il dato è critico, più devono essere chiare responsabilità, semantica e aspettative.
