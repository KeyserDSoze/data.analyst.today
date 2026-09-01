## 17.1 “Le vendite stanno scendendo”: prima capire quale numero sta cambiando

### Caso simulato/composito: Orion Living

Una catena retail multicanale, **Orion Living**, chiude il mese con un alert: `-11,2% YoY`.

Il CEO chiede:

> “È un problema di domanda, prezzo o execution?”

Questa è una domanda realistica perché contiene già tre spiegazioni concorrenti. Il rischio è trasformarle troppo presto in tre dashboard.

Il primo compito non è scegliere una tecnica. È capire **quale decisione dipende dalla risposta**.

Il management sta considerando tre azioni molto diverse:

- aumentare promozioni per recuperare domanda;
- intervenire su prodotto e pricing;
- correggere problemi operativi che stanno distruggendo valore dopo l'ordine.

Agire sulla spiegazione sbagliata può costare milioni e peggiorare il fenomeno.

## Routing iniziale

Il Capstone Routing Canvas parte così:

| Elemento | Domanda |
|---|---|
| Decisione | serve stimolare domanda o correggere execution? |
| Failure cost | scontare inutilmente, erodere margine, ignorare un problema operativo |
| Claim necessario | diagnostico prima che causale |
| Tempo disponibile | 72 ore per la prima decisione |
| Reversibilità | alta per analisi e test; media per campagne e rollback prodotto |
| Primo gate | verificare che il `-11,2%` significhi davvero ciò che il board pensa |

Questa classificazione evita un errore frequente: chiedere una prova causale perfetta quando per la prima decisione basta localizzare con affidabilità il meccanismo dominante.

## 1. “Vendite” non è una metrica

“Vendite” può significare:

- ordini;
- pezzi;
- gross sales;
- net sales;
- revenue riconosciuta;
- contribution margin.

Il primo controllo mostra che il `-11,2%` riguarda **net sales**, non ordini né gross sales.

Questa distinzione cambia completamente il routing.

Se gross sales e ordini fossero crollati, la priorità sarebbe domanda/conversione.

Se gli ordini fossero stabili ma net sales crollasse, dovremmo guardare cosa succede tra ordine e valore netto riconosciuto.

### Deliverable attivato

Serve subito un **Analytical Brief** minimale:

- metrica decisionale: net sales;
- baseline: stesso mese anno precedente, con verifica di comparabilità;
- popolazione: ordini consumer completati;
- decisione: promozione generalizzata sì/no nelle prossime due settimane;
- stop rule iniziale: non proporre azioni commerciali finché gross e net sales non sono riconciliati.

Non serve ancora un modello predittivo, un esperimento o un Causal Identification Brief.

## 2. Decomporre prima di spiegare

L'analista costruisce una bridge decomposition tra domanda e valore netto:

- sessioni;
- conversione;
- unità per ordine;
- prezzo medio;
- mix prodotto;
- cancellazioni;
- resi;
- valore netto finale.

I risultati principali sono:

- sessioni: `-2,1%`;
- conversione: `-0,4 pp`;
- unità per ordine: quasi stabile;
- prezzo medio: `+3,8%`;
- return rate osservato: `7,4% → 10,9%`.

Il dato non sostiene più la storia semplice “la domanda è crollata”.

La parte più anomala si trova dopo l'acquisto.

### Evidence promotion

In questa fase vengono prodotti molti breakdown. Solo una visualizzazione viene promossa a decision artifact: una bridge che mostra quanto del gap net sales arriva da traffico/conversione e quanto da cancellazioni/resi.

Il suo ruolo è `orient`.

Non prova ancora la causa. Riduce lo spazio delle ipotesi.

## 3. Cercare concentrazione, non soltanto correlazione

Per canale:

| Canale | Net sales YoY |
|---|---:|
| Store | -3,1% |
| Web desktop | -5,4% |
| Mobile app | -24,8% |

Il calo è inoltre concentrato:

- nell'arredo voluminoso;
- su iOS;
- in tre mercati che spiegano circa il 64% del delta.

A questo punto il team potrebbe dire:

> “È la nuova release iOS.”

Sarebbe prematuro.

Abbiamo localizzato **dove** il fenomeno è forte, non ancora **perché**.

## 4. Data Readiness Review: prima di costruire una storia

Il team controlla:

- completeness degli eventi;
- definizione del return rate;
- date ordine, consegna e reso;
- versioni app realmente esposte;
- policy di reso;
- modalità di contabilizzazione dei refund;
- eventuali cambiamenti di mix.

Emerge un fatto importante: nello stesso periodo la finestra di reso è stata estesa da 30 a 45 giorni in due mercati.

Il confronto YoY del return rate non è quindi semanticamente omogeneo.

Il `+3,5 pp` osservato non può essere trattato come deterioramento operativo puro.

### Stop rule

La prima stop rule scatta:

> **non attribuire il deterioramento alla release né alla logistica finché non abbiamo reso comparabili esposizione al reso, mix e finestre temporali.**

Questo è un esempio di valore creato senza modello sofisticato: impedire una decisione anticipata.

## 5. Ipotesi concorrenti

Dopo il controllo semantico restano cinque ipotesi:

1. peggioramento dell'esperienza iOS;
2. politica di reso più permissiva;
3. mix verso categorie ad alto return rate;
4. deterioramento logistico sugli articoli bulky;
5. combinazione di più meccanismi.

L'analista costruisce una **EDA Evidence Map** che registra, per ogni ipotesi:

- evidenza a favore;
- evidenza contro;
- dati mancanti;
- test discriminante successivo.

Questo evita che il team selezioni soltanto i grafici compatibili con la spiegazione preferita.

## 6. Separare composizione e performance

Standardizzando il mix prodotto e confrontando finestre di reso omogenee, il deterioramento comparabile del return rate scende da `+3,5 pp` a circa `+1,4 pp`.

La decomposizione del residuo mostra:

- circa `0,8 pp` concentrati sugli ordini bulky;
- circa `0,4 pp` associati agli utenti esposti alla nuova esperienza iOS;
- una quota residua diffusa.

Nel segmento bulky:

- lead time medio `+1,7 giorni`;
- resi per “prodotto danneggiato” in forte aumento;
- tre carrier spiegano gran parte del deterioramento;
- i mercati più colpiti coincidono con quelli in cui è cambiato il network di consegna.

Ora l'evidenza diagnostica è molto più forte.

Ma “associato alla release” non equivale ancora a “causato dalla release”.

## 7. Quanto claim ci serve davvero?

Per la decisione immediata non serve stimare con precisione l'effetto causale di ogni driver.

Serve decidere se lanciare uno sconto generalizzato.

L'evidenza disponibile è già sufficiente per dire:

- la domanda aggregata non spiega la maggioranza del gap;
- una quota importante del problema nasce dopo l'ordine;
- il deterioramento è fortemente concentrato in specifici flussi operativi;
- uno sconto generalizzato agirebbe poco sui driver dominanti e comprimerebbe ulteriormente il margine.

Quindi il **claim gate** per la decisione commerciale può essere superato anche senza un'identificazione causale completa.

Per il rollback iOS, invece, il claim richiesto è più forte. Qui serve una verifica specifica sull'esposizione al rollout e, se possibile, un confronto controllato.

## 8. Decision Record

Il Decision Record confronta:

### A — Sconto generalizzato

Upside: possibile recupero conversione.

Downside: margine inferiore, scarso impatto sui resi bulky, rischio di mascherare il problema.

### B — Nessuna azione

Upside: nessun costo immediato.

Downside: continuano danni, resi e deterioramento net sales.

### C — Intervento mirato

- audit carrier bulky nei tre mercati critici;
- rollback controllato della componente iOS sospetta;
- confronto con finestre di reso omogenee;
- test packaging/carrier sugli SKU più danneggiati;
- monitoraggio separato di gross sales, returns e net sales.

La scelta è **C**.

Il motivo non è che conosciamo perfettamente ogni causa. È che C è la scelta più robusta all'evidenza disponibile e mantiene alto il valore informativo delle azioni successive.

## 9. Decision Communication Pack

La headline executive non è:

> “Le vendite sono -11,2%.”

E neppure:

> “La logistica ha causato il calo.”

È:

> **“Il gap di net sales non è principalmente un calo generalizzato della domanda: dopo aver reso comparabili policy e mix, il deterioramento residuo è concentrato negli ordini bulky e in una parte del rollout iOS. Non raccomandiamo sconti generalizzati; proponiamo interventi mirati su carrier, packaging e rollout.”**

Sotto la headline compaiono:

- il bridge gross-to-net;
- il breakdown per categoria/mercato;
- il principale caveat causale;
- decisione richiesta;
- metriche da monitorare.

## 10. Outcome review

Il piano misura:

- return rate bulky;
- damage-related return rate;
- delivery lead time;
- net sales per session;
- conversion iOS;
- customer complaints;
- contribution margin.

L'outcome review non chiederà soltanto se net sales sono risalite.

Chiederà se il meccanismo su cui abbiamo agito si è mosso nella direzione prevista.

## Cosa abbiamo scelto di non fare

In questo caso non servono, almeno nella prima fase:

- churn model;
- forecast complesso;
- MMM;
- architettura streaming nuova;
- modello causale globale di tutte le determinanti delle vendite.

Questa rinuncia è parte della soluzione.

La catena effettiva è:

**Analytical Brief → Data Readiness Review → EDA Evidence Map → Decision Record → Decision Communication Pack**

con un eventuale Causal Identification Brief solo sul sotto-problema iOS se il rollback ha un costo sufficientemente alto.

> **Un capstone non dimostra maturità usando tutto. La dimostra scegliendo il minimo percorso di evidenza che rende difendibile la decisione.**
