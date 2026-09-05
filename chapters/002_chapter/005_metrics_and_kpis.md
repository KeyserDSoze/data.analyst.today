## 2.4 Metriche nel brief: outcome, driver, guardrail e soglia

Il Capitolo 1 ha stabilito che una metrica è una definizione, non un oggetto naturale che aspetta di essere trovato nel database. Nel brief dobbiamo fare un passo ulteriore: decidere **perché** ogni metrica entra nel piano.

Un elenco di venti KPI non rende un'analisi più completa. Spesso rende soltanto meno chiaro quale numero dovrebbe cambiare la nostra comprensione del problema. Conviene invece assegnare alle metriche ruoli diversi, perché ciascun ruolo risponde a una domanda differente.

L'**outcome metric** rappresenta il risultato principale che vogliamo comprendere, prevedere o modificare. Può essere retention a 90 giorni, margine per ordine, tempo di consegna, conversion rate o forecast error. Quando è possibile, il brief dovrebbe identificare un outcome primario: non perché esista sempre una sola metrica importante, ma perché senza un risultato centrale diventa difficile sapere quali analisi siano decisive e quali accessorie.

I **driver** aiutano invece a scomporre quell'outcome. Se il margine per ordine è diminuito, prezzo medio, sconto, costo prodotto, fulfillment, mix categorie e tasso di reso possono spiegare matematicamente o operativamente parti del cambiamento. Chiamarli driver non significa aver dimostrato che siano cause: indica che sono componenti o segnali che aiutano a restringere la diagnosi.

I **guardrail** proteggono la decisione da miglioramenti locali ottenuti a spese di qualcos'altro. Una promozione può far crescere la conversione e contemporaneamente distruggere margine, aumentare i resi o peggiorare la qualità del mix clienti. Se osserviamo soltanto la metrica che stiamo ottimizzando, il sistema può apparire migliore mentre il business nel complesso peggiora.

Infine, target e soglie collegano la misura a un giudizio operativo. La documentazione Microsoft sui KPI usa proprio questa idea: una misura viene valutata rispetto a un target e a soglie di stato.[^ms-kpi-tabular][^ms-kpi-powerbi] È una convenzione implementativa specifica, ma rende evidente una distinzione generale: una metrica descrive un fenomeno; un KPI viene utilizzato per giudicare una performance rispetto a un riferimento.

## Le metriche formano un sistema, non un catalogo

Supponiamo di voler aumentare la conversione e-commerce attraverso una promozione. Il conversion rate è l'outcome immediato, ma il margine per ordine può diventare un guardrail. Il tasso di reso potrebbe essere un secondo guardrail se la promozione modifica il mix dei prodotti acquistati. Il valore medio dell'ordine e la quota di clienti nuovi possono essere driver utili per capire *come* è cambiato il risultato.

Questa struttura obbliga a formulare meglio la decisione. Non chiediamo più genericamente “la promozione funziona?”, ma se produce un miglioramento della conversione abbastanza grande da giustificare il costo senza violare i vincoli economici che il business considera importanti.

La definizione deve poi essere sufficientemente concreta da evitare implementazioni incompatibili. Consideriamo:

> **Conversion rate:** percentuale di sessioni e-commerce valide che generano almeno un ordine confermato nella stessa sessione, escludendo traffico interno, bot e ordini di test.

La frase sembra precisa, ma rende immediatamente visibili nuove scelte: una sessione con due ordini conta una o due volte? “Confermato” significa creato, pagato o non cancellato? Come identifichiamo bot e traffico interno? Che cosa succede se la sessione attraversa la mezzanotte?

Il valore del brief non è risolvere da solo ogni dettaglio del semantic layer. È far emergere queste domande **prima** che due persone implementino la stessa metrica in modi diversi.

Per questo la metric contract rimane un artefatto strutturato:

```text
Nome:
Ruolo: outcome / driver / guardrail
Definizione business:
Formula:
Unità/grain:
Popolazione eleggibile:
Numeratore/denominatore, se applicabili:
Finestra temporale:
Esclusioni principali:
Fonte/metric owner:
Baseline o target:
Soglia decisionale, se nota:
```

Una domanda finale aiuta a distinguere un KPI operativo da una misura soltanto informativa:

> **“Se questa metrica supera o scende sotto una certa condizione, chi dovrebbe fare che cosa?”**

Se nessuno sa rispondere, il numero può essere comunque utile alla diagnosi. Ma forse non merita il ruolo di KPI nel processo decisionale.

> **Le metriche del brief non devono essere quelle che possiamo calcolare facilmente. Devono essere quelle che spiegano l'outcome o impediscono alla decisione di ottimizzare la cosa sbagliata.**

---

### Fonti

[^ms-kpi-tabular]: Microsoft Learn, *Create and manage KPIs in Analysis Services tabular models*. https://learn.microsoft.com/en-us/analysis-services/tabular-models/kpis-ssas-tabular
[^ms-kpi-powerbi]: Microsoft Learn, *Create key performance indicator (KPI) visualizations*. https://learn.microsoft.com/en-us/power-bi/visuals/power-bi-visualization-kpi
