## 2.10 Dai requisiti analitici ai requisiti dati

Una volta chiarita la domanda, dobbiamo tradurla in **evidenza necessaria** e poi in dati.

L'ordine è importante.

Partire da “quali tabelle abbiamo?” favorisce analisi determinate dalla disponibilità del dato. Partire da “che cosa dovremmo osservare per distinguere le ipotesi?” rende invece visibile ciò che manca.

Supponiamo che la domanda sia:

> **Perché la retention dei nuovi clienti è diminuita negli ultimi sei mesi?**

Dire “servono i dati clienti” non è un requisito.

Potrebbero servire:

- identificativo cliente coerente nel tempo;
- data e canale di acquisizione;
- prodotto o piano iniziale;
- eventi di utilizzo;
- transazioni e rinnovi;
- cancellazioni;
- prezzi e promozioni;
- ticket di supporto;
- cambiamenti di prodotto;
- paese o mercato;
- eventuali segnali di esposizione a onboarding differenti.

Ogni elemento dovrebbe essere collegato a una domanda o a un'ipotesi. Se non sappiamo perché ci serve, probabilmente non è un requisito prioritario.

### Required, useful, proxy

Nel brief è utile classificare i dati.

**Required** — senza questa informazione non possiamo rispondere alla domanda primaria.

**Useful** — aumenta la profondità o permette segmentazioni importanti, ma l'analisi può iniziare senza.

**Proxy** — sostituisce imperfettamente un concetto che non osserviamo direttamente.

Questa distinzione aiuta quando una fonte non è disponibile o richiederebbe settimane di engineering.

### Dati necessari e disponibili non coincidono

Una delle conclusioni più professionali che un analyst possa produrre prima dell'analisi è:

> “Con i dati attuali possiamo descrivere il fenomeno, ma non distinguere tra le ipotesi A e B. Per farlo servirebbe misurare X.”

Non è un fallimento. È un **gap informativo identificato prima di promettere una risposta che i dati non possono sostenere**.

### Il grain entra nel requisito, non soltanto nella query

Il Capitolo 3 studierà in profondità grain, chiavi e qualità. Nel brief basta dichiarare a quale livello serve l'informazione.

Per esempio:

| Dato | Significato | Grain richiesto | Perché serve | Priorità |
|---|---|---|---|---|
| customer_id | identità coerente del cliente | cliente | coorti e repeat purchase | required |
| order_date | data dell'ordine valido | ordine | finestre di acquisto | required |
| acquisition_channel | canale iniziale | cliente | test mix acquisizione | useful |
| delivery_delay | giorni oltre promessa | spedizione | ipotesi experience | useful |
| satisfaction | proxy esperienza | survey response | ipotesi CX | proxy |

Se una fonte disponibile ha grain diverso da quello necessario, il problema va identificato prima di costruire aggregazioni fragili.

### Requisiti minimi per una fonte critica

Prima di considerare disponibile un dato importante dovremmo sapere almeno:

- che cosa rappresenta;
- quale grain ha;
- quale chiave lo identifica;
- quale storico copre;
- con quale latenza diventa completo;
- quali trasformazioni principali subisce;
- chi possiede la fonte;
- se definizioni o tracking sono cambiati nel periodo.

Non serve trasformare il brief in un data catalog. Serve sapere abbastanza da valutare **fattibilità e rischi dell'analisi**.

### Dal requisito al piano di acquisizione

Per ogni gap possiamo scegliere:

- usare una fonte esistente;
- costruire una trasformazione;
- usare un proxy dichiarato;
- raccogliere nuovo dato;
- ridurre la domanda;
- rinviare una conclusione più forte a una fase successiva.

Queste sono decisioni di progetto analitico, non soltanto tecniche.

### Campo del brief

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

Il Capitolo 3 riprenderà da qui e insegnerà come capire se le fonti che abbiamo dichiarato “disponibili” meritano davvero fiducia.

> **Non chiedere soltanto quali dati possiedi. Chiedi quali osservazioni servono per distinguere le spiegazioni che contano.**
