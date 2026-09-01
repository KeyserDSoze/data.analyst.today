## 16.7 Annotazioni e Context Contract: rendere visibile ciò che i segni non contengono

Un punto, una barra o una linea non contengono da soli tutto ciò che serve per interpretarli.

Mancano spesso informazioni come:

- baseline;
- target;
- denominatore;
- definizione della metrica;
- data di aggiornamento;
- cambio metodologico;
- rollout;
- shock esterno;
- regime operativo.

Se una di queste informazioni può cambiare l'interpretazione, deve entrare nel **Context Contract** della visualizzazione.

## Il Context Contract

Per un visual decision-critical chiediamo:

| Campo | Domanda |
|---|---|
| Metric definition | Che cosa misura esattamente? |
| Population / denominator | Su chi o su cosa è calcolata? |
| Time window | Quale periodo rappresenta? |
| Baseline | Rispetto a cosa giudichiamo il valore? |
| Target / threshold | Quale soglia ha significato operativo? |
| Freshness | Fino a quando il dato è aggiornato? |
| Maturity | È provisional, reconciled o final? |
| Method break | È cambiata definizione, tracking o sistema? |
| Event annotation | Quali eventi osservabili aiutano a leggere il pattern? |

Non tutti i campi devono essere stampati in grande. Devono però essere disponibili al livello appropriato della Decision Communication Pack.

## Annotare eventi, non inventare spiegazioni

È corretto annotare:

> “14 aprile — release 6.12 distribuita al 65% degli utenti.”

È diverso da:

> “14 aprile — la release causa il calo.”

La prima frase documenta un evento.

La seconda promuove una coincidenza a spiegazione causale.

L'annotazione deve rispettare lo stesso claim level del testo.

## Caso simulato/composito — Il crollo creato da una definizione

Una piattaforma SaaS mostra i daily active users.

Il 14 aprile la serie scende del 16%.

Il titolo iniziale è:

> **Engagement in forte calo**

Ma quel giorno cambia la definizione di `active_user`:

- prima: apertura dell'app;
- dopo: almeno un'azione significativa.

Il dato post-14 aprile è valido.

Quello pre-14 aprile è valido secondo la vecchia definizione.

È la **comparabilità della serie** a essersi rotta.

Una linea verticale e una nota:

> “14 aprile — nuova definizione di active user; i livelli pre/post non sono direttamente comparabili”

impediscono una lettura falsa.

## Baseline: un numero senza riferimento è quasi sempre incompleto

`Conversion = 3,8%` non dice ancora se dobbiamo preoccuparci.

Possibili riferimenti:

- target: 4,2%;
- settimana precedente: 3,7%;
- stesso periodo anno precedente: 4,0%;
- intervallo storico normale: 3,5–4,1%;
- gruppo di controllo: 3,9%.

La baseline deve essere scelta perché risponde alla decision question, non perché produce il contrasto più interessante.

## Denominatore: la nota che può cambiare la storia

> “Il 90% dei clienti è soddisfatto.”

La frase cambia significato se scopriamo che:

- ha risposto il 12% degli invitati;
- il survey è apparso solo dopo un acquisto completato;
- i ticket aperti sono esclusi;
- `satisfied` include il punteggio neutrale.

Se il denominatore o l'eligibility sono materialmente importanti, devono essere leggibili senza scavare in un data dictionary.

## Freshness e provisionalità

Una dashboard alle 08:00 può mostrare:

- ordini completi fino alle 07:45;
- pagamenti fino alle 07:30;
- refund D+2;
- logistics cost D+1.

Un contribution margin “di oggi” costruito con queste latenze non è un numero finalizzato.

Il Context Contract dovrebbe mostrare almeno:

> **Data as of 07:45 — margin provisional; refund e logistics reconciliation D+2.**

Il lettore può così decidere se il dato è abbastanza maturo per l'azione richiesta.

## Titoli: conclusivi ma non speculativi

Titolo debole:

> “DAU 2026”

Titolo utile:

> “I DAU post-14 aprile non sono comparabili con lo storico dopo il cambio di definizione”

Titolo eccessivo:

> “La nuova definizione ha ridotto l'engagement”

La regola è:

> **Il titolo può guidare l'attenzione; non può aggiungere evidenza che il grafico non possiede.**

## Provenance vicino al punto d'uso

Per un elemento decision-critical rendiamo facile trovare:

- fonte;
- metrica/versione;
- timestamp;
- eventuale nota metodologica;
- link all'appendix o al Decision Record.

Non serve trasformare ogni slide in documentazione tecnica. Serve evitare che il contesto necessario venga separato dall'evidenza al punto da non arrivare mai al lettore.

> **Il contesto non è decorazione del grafico. È parte del significato che il grafico pretende di comunicare.**

### Fonte

- Office for National Statistics, *Data visualisation guidance*: https://service-manual.ons.gov.uk/data-visualisation
