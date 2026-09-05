## 16.1 Dalla visualizzazione esplorativa all'evidenza decisionale

Non tutti i grafici che aiutano l'analista a capire meritano di arrivare davanti a chi decide. Durante l'EDA produciamo **discovery artifacts**: servono a cercare pattern, cambiare grain, confrontare definizioni, smentire ipotesi e capire dove investigare. Nella comunicazione costruiamo invece **decision artifacts**: servono a sostenere un passaggio preciso del Decision Record.

La differenza non è estetica. È epistemica.

Un discovery artifact può essere utile anche quando porta a una strada morta. Un decision artifact deve invece aver guadagnato il diritto di rappresentare un claim. Prima della promozione chiediamo quindi se la metrica è definita, il grain è coerente, il denominatore è stabile, il pattern resiste ai controlli rilevanti, l'incertezza ne modifica l'interpretazione e il linguaggio resta dentro il livello di evidenza disponibile.

Possiamo pensare alla promozione così:

```text
pattern trovato
→ semantic/readiness check
→ alternative explanation check
→ materiality
→ claim level
→ decision relevance
→ decision artifact
```

Il punto finale è decisivo: un pattern può essere vero, robusto e comunque non meritare la pagina executive se non cambia nessuna alternativa, soglia o azione.

### Caso simulato/composito — 27 grafici, tre prove

Un e-commerce vede la conversion scendere dal **3,8% al 3,4%**. Durante l'indagine il team produce 27 grafici su device, browser, paese, canale, landing, ora, new/returning, payment method, app version, basket size e categoria. Quella ricchezza è utile nella ricerca, ma il lavoro converge su quattro fatti robusti: circa il **78% del delta** è su iOS; il peggioramento è quasi interamente nella versione **6.12**; il drop si concentra tra `payment_started` e `payment_authorized`; Android e le versioni iOS precedenti restano sostanzialmente stabili.

La Decision Communication Pack non deve mostrare i 27 grafici in ordine cronologico. Deve selezionare le prove che ricostruiscono la logica della decisione: una decomposition per piattaforma localizza il delta; il confronto tra versioni mostra la concentrazione; il funnel identifica il boundary in cui il comportamento cambia. I controlli sugli altri segmenti restano disponibili nell'evidence/provenance layer per dimostrare che le spiegazioni alternative principali sono state esaminate.

Questo non elimina il lavoro esplorativo. Lo trasforma in **provenance della selezione**.

## Dalla cronologia alla logica

Una presentazione analyst-first racconta spesso il percorso seguito: “prima abbiamo guardato il traffico, poi i paesi, poi i device...”. È una struttura utile in una peer review o in un post-mortem, ma raramente è quella che riduce meglio il costo cognitivo di chi deve scegliere.

La comunicazione decisionale usa un ordine diverso:

```text
decision question
→ headline
→ evidence che discrimina le alternative
→ caveat / uncertainty
→ alternative
→ ask
```

L'analisi rimane auditabile, ma il pubblico non deve ricostruire da solo quale dei ventisette passaggi sia diventato materialmente importante.

## Ogni visual deve sostenere una frase verificabile

Per ogni elemento chiediamo:

> **“Questo visual serve a mostrare che...”**

“Conversion per paese” descrive soltanto il contenuto. “La Germania spiega circa due terzi del gap europeo, mentre gli altri mercati restano vicini alla baseline” dichiara invece il claim che il visual deve poter sostenere o smentire.

Questa frase ci costringe anche a controllare se la forma scelta rappresenta davvero la relazione richiesta. Se il claim riguarda la contribution al delta, un semplice ranking del livello corrente può essere il grafico sbagliato pur contenendo numeri corretti.

## I cinque ruoli dell'evidenza

Nella Pack un elemento dovrebbe avere un compito riconoscibile. Può **orientare** mostrando che cosa sta accadendo, **confrontare** alternative o segmenti, **diagnosticare** dove si concentra il fenomeno, **rendere visibile una decision boundary** oppure **permettere verifica** di un claim. Queste categorie non sono una checklist da riempire: servono a evitare visual senza funzione.

Togliere un grafico dalla pagina principale non deve però rendere opaco il ragionamento. Ogni decision artifact importante deve poter rimandare a definizione metrica, periodo, fonte, dataset/query, controlli principali e appendix pertinente.

> **La visualizzazione esplicativa non è il riassunto del lavoro fatto dall'analista. È la selezione minima di evidenze necessarie per valutare la decisione senza perdere la possibilità di risalire alla prova.**
