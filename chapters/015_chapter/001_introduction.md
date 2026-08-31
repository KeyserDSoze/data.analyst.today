# Capitolo 15 — Dall'analisi all'insight e alla decisione

## 15.0 Un numero interessante non è ancora una decisione

Molte analisi finiscono troppo presto.

Il team trova un pattern, costruisce un grafico, scrive una frase come:

> “La conversione mobile è diminuita del 7%.”

Poi il lavoro viene considerato concluso.

Ma quella frase non è ancora un insight. È un **finding**: un fatto osservato nei dati.

Per diventare utile deve essere collegato a:

- una domanda di business;
- un meccanismo plausibile;
- una stima dell'impatto;
- alternative possibili;
- incertezza;
- una decisione concreta.

Una struttura utile è:

**Finding → Insight → Raccomandazione → Decisione → Azione → Misurazione**

Questa catena sembra semplice, ma contiene alcuni dei passaggi più difficili dell'intero lavoro analitico.

## Finding

Un finding descrive qualcosa che osserviamo.

Esempi:

- il churn è passato dal 4,2% al 5,1%;
- il margine della categoria Home è sceso di 3,4 punti percentuali;
- i clienti acquisiti da paid social hanno retention più bassa;
- il tempo medio di consegna è aumentato di 0,8 giorni.

Sono osservazioni.

Possono essere corrette e allo stesso tempo poco utili.

## Insight

Un insight collega il finding al contesto e alla decisione.

Per esempio:

> “Il peggioramento della retention è concentrato nei clienti acquisiti da paid social dopo il cambio di landing page, soprattutto nei segmenti con activation incompleta. Il problema sembra quindi meno legato al canale in sé e più alla qualità dell'attivazione post-acquisizione.”

Qui il dato inizia a spiegare qualcosa.

## Raccomandazione

La raccomandazione risponde:

> “Che cosa dovremmo fare?”

Ma una buona raccomandazione non è una preferenza personale travestita da analisi.

Deve collegare evidenza, beneficio atteso, costo, rischio e reversibilità.

## Decisione

La decisione appartiene spesso a un responsabile di business, non all'analista.

Il compito dell'analista è però rendere quella decisione migliore.

Questo significa non soltanto fornire informazioni, ma **ridurre l'incertezza rilevante per la scelta**.

È coerente con l'impostazione del NIST AI Risk Management Framework, che sottolinea l'importanza del contesto e della conoscenza dei rischi per supportare decisioni appropriate: senza contesto, la valutazione del rischio e la decisione diventano fragili.

Fonte pubblica: https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf

## Caso realistico: una dashboard perfetta, una decisione inutile

Un'azienda subscription scopre che il churn dei clienti small business è aumentato dal 5,6% al 7,2%.

Il dashboard è corretto.

La prima raccomandazione è:

> “Creiamo una campagna di retention per tutti i clienti small business.”

Il problema è che il segmento contiene circa 180.000 clienti.

L'analisi successiva mostra che:

- l'aumento di churn è concentrato nei clienti con meno di 90 giorni di anzianità;
- il 74% del delta viene da account che non hanno completato l'onboarding;
- i clienti pienamente attivati non mostrano peggioramenti sostanziali;
- una campagna generalizzata avrebbe un costo di circa €1,1 milioni;
- un intervento mirato sull'onboarding avrebbe un costo stimato di €190.000.

Il finding iniziale era corretto.

La raccomandazione iniziale era inefficiente.

L'insight vero non era:

> “Il churn small business è aumentato.”

Era:

> “Il deterioramento è quasi interamente associato alla mancata activation nei primi 90 giorni; trattare tutto il segmento disperderebbe budget su clienti che non mostrano il problema.”

## Il criterio fondamentale

Una buona analisi non si misura dal numero di grafici, query o modelli prodotti.

Si misura da quanto migliora la qualità della decisione.

> **Un insight è utile quando cambia cosa faremmo, quanto lo faremmo, dove lo faremmo o con quale livello di fiducia.**
