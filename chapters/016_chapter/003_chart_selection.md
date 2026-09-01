## 16.2 Scegliere la forma in base al compito cognitivo

La domanda corretta non è:

> “Quale grafico è più bello?”

né:

> “Quale visual offre il tool?”

È:

> **“Quale confronto deve diventare facile da percepire, e quale errore di lettura dobbiamo evitare?”**

La forma viene dopo la decision question, il grain e il tipo di relazione.

## Un Visual Encoding Contract

Per ogni visual importante possiamo dichiarare quattro cose:

1. **task** — che cosa deve fare il lettore con gli occhi;
2. **encoding** — posizione, lunghezza, area, colore, linea, testo;
3. **reference** — baseline, target, zero, periodo o gruppo di confronto;
4. **failure mode** — quale interpretazione sbagliata è più probabile.

| Domanda | Forma spesso utile | Facilita | Failure mode tipico |
|---|---|---|---|
| Quale gruppo è più grande? | barre ordinate | confronto di magnitudine | asse troncato |
| Come cambia nel tempo? | linea | trend, turning point | finestra cherry-picked |
| Come è distribuito? | istogramma / boxplot / percentile | forma e code | media usata come sintesi totale |
| Due variabili si muovono insieme? | scatter | relazione e dispersione | correlazione letta come causalità |
| Come cambia la composizione? | stacked / 100% stacked / small multiples | quota o mix | confondere quota e volume |
| Dove si perde una popolazione? | funnel / step conversion | drop-off | denominatori incompatibili |
| Quanto siamo lontani da un target? | valore + delta + trend | distanza dalla soglia | gauge senza scala utile |
| Devo leggere valori precisi? | tabella | lookup | heatmap decorativa |

## Confrontare grandezze: lunghezze allineate prima di angoli e aree

Se dobbiamo confrontare categorie, barre ordinate su una scala comune sono spesso più leggibili di una torta.

Esempio:

| Categoria | Revenue |
|---|---:|
| Home | €12,4M |
| Beauty | €10,9M |
| Sports | €9,8M |
| Electronics | €9,6M |

Il compito è distinguere valori relativamente vicini. La lunghezza su una baseline comune rende quel confronto diretto.

## Tempo: chart type corretto, grain sbagliato

### Caso simulato/composito — Il mese stabile che nasconde il weekend

Una piattaforma food delivery mostra ordini mensili quasi invariati.

Il line chart è tecnicamente corretto.

Passando al dato giornaliero emerge però che:

- lunedì–giovedì gli ordini crescono;
- venerdì–domenica diminuiscono;
- i due movimenti si compensano nell'aggregato mensile.

Il failure mode non era il grafico.

Era il **grain temporale**.

> **Una forma visiva corretta non salva una domanda rappresentata alla granularità sbagliata.**

## Distribuzioni: quando il centro nasconde la coda

Delivery time medio: 2,4 giorni.

Se il 90° percentile è 6,8 giorni, il problema può vivere nella coda e non nel cliente medio.

La Decision Communication Pack deve quindi scegliere la forma in base alla decisione:

- media + percentile se conta il service level;
- boxplot se dobbiamo confrontare gruppi;
- distribuzione se la forma stessa è il messaggio.

## Relazione: visivamente forte non significa causalmente forte

Uno scatter plot può rendere una correlazione estremamente convincente.

Proprio per questo titolo e annotazioni devono rispettare il claim level.

Meglio:

> “Gli account con maggiore adoption mostrano NRR più alta”

che:

> “L'adoption aumenta la NRR”

se non abbiamo un disegno causale adeguato.

## Composizione: quota e volume non sono intercambiabili

Un 100% stacked bar risponde bene a:

> “Come cambia il mix?”

ma può nascondere che il totale si è dimezzato.

Se volume e composizione sono entrambi decision-critical, mostriamoli separatamente o con due livelli coordinati.

## Funnel: una sequenza richiede una popolazione coerente

Un funnel ha senso soltanto se gli step appartengono a una sequenza definita e i denominatori sono compatibili.

Se `checkout_started` conta sessioni e `payment_success` conta ordini, la forma può sembrare perfetta mentre la conversione non ha un significato stabile.

Il visual contract eredita quindi il semantic contract dei capitoli precedenti.

## Target: spesso basta meno

Per mostrare performance rispetto a una soglia spesso sono sufficienti:

- valore corrente;
- target;
- delta;
- trend;
- eventuale uncertainty band.

Un gauge occupa molto spazio e spesso aggiunge poco.

## La domanda finale

Prima di disegnare chiediamoci:

> **“Se il destinatario avesse cinque secondi, quale relazione deve percepire correttamente?”**

Poi controlliamo che scala, denominatore, baseline e titolo non gli facciano percepire una relazione diversa.

> **Il chart type non è una preferenza estetica. È una scelta sul compito cognitivo che rendiamo facile e sull'errore che dobbiamo rendere difficile.**

### Fonti

- Office for National Statistics, *Data visualisation guidance — Axes and gridlines*: https://service-manual.ons.gov.uk/data-visualisation/guidance/axes-and-gridlines
- Government Analysis Function, *Accessible charts: a checklist of the basics*: https://analysisfunction.civilservice.gov.uk/policy-store/accessible-charts-a-checklist-of-the-basics/
