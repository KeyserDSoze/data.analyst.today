# Capitolo 8 - Causalità, confondenti e ragionamento controfattuale

> Sapere che due fenomeni si muovono insieme è utile. Sapere che intervenire su uno cambierà davvero l'altro è un problema molto più difficile.

Nei capitoli precedenti abbiamo imparato a descrivere dati, stimare incertezza, confrontare gruppi, analizzare retention e prevedere il futuro. Ma molte delle decisioni più importanti richiedono una domanda diversa:

**che cosa succederebbe se facessimo qualcosa?**

Aumentare il budget advertising aumenterebbe davvero le vendite? Ridurre il prezzo aumenterebbe il margine complessivo? Un nuovo onboarding ridurrebbe il churn? Un programma di sconti farebbe crescere la frequenza d'acquisto oppure attirerebbe semplicemente clienti che avrebbero comprato comunque?

Queste non sono semplici domande descrittive. Sono domande causali.

Il punto centrale è il controfattuale: per stimare l'effetto di un intervento vorremmo confrontare lo stesso soggetto, nello stesso momento e nelle stesse condizioni, sia con l'intervento sia senza. Questo confronto perfetto non è osservabile. Ogni cliente riceve o non riceve una promozione; ogni negozio applica o non applica un nuovo layout; ogni utente vede una versione del prodotto e non contemporaneamente l'altra.

Il lavoro causale consiste quindi nel costruire un confronto credibile con ciò che sarebbe successo in assenza dell'intervento.

In questo capitolo useremo casi aziendali realistici per affrontare:

- correlazione e causalità;
- controfattuali e potential outcomes;
- confondenti;
- causalità inversa;
- selection bias e collider bias;
- DAG come strumento di ragionamento;
- esperimenti randomizzati;
- natural experiment e quasi-esperimenti;
- difference-in-differences;
- limiti delle conclusioni causali.

La regola di fondo sarà sempre la stessa:

> **Prima di chiedere quale modello usare, bisogna chiedere quale confronto renderebbe credibile la conclusione causale.**

## Una distinzione che cambia il lavoro dell'analista

Consideriamo tre frasi:

1. I clienti che usano la nuova funzionalità hanno retention più alta.
2. La nuova funzionalità aumenta la retention.
3. Se rendessimo obbligatoria la nuova funzionalità, la retention aumenterebbe di 4 punti percentuali.

La prima è un'osservazione descrittiva. La seconda è una conclusione causale. La terza aggiunge una stima quantitativa dell'effetto di un intervento.

Passare dalla prima alla seconda frase non è una questione di SQL più sofisticato. È una questione di identificazione causale.

## Caso introduttivo - Il programma VIP che sembrava funzionare perfettamente

Una piattaforma e-commerce introduce un programma VIP. Dopo sei mesi il team presenta questi numeri:

| Gruppo | Spesa media annua | Ordini medi | Retention 12 mesi |
|---|---:|---:|---:|
| VIP | 1.420 € | 9,8 | 88% |
| Non VIP | 510 € | 3,4 | 61% |

Il CEO conclude:

> "Il programma VIP aumenta enormemente la fedeltà. Estendiamolo a tutti."

Ma l'iscrizione VIP è disponibile solo ai clienti che hanno già superato 800 € di spesa negli ultimi dodici mesi.

Il programma potrebbe avere un effetto positivo. Tuttavia i gruppi erano diversi già prima dell'intervento. I clienti VIP sono selezionati proprio perché erano più attivi, più fedeli e con maggior valore economico.

Il confronto VIP vs non VIP mescola almeno due effetti:

- il possibile effetto del programma;
- le differenze preesistenti tra i clienti.

Questa è la porta d'ingresso alla causalità: capire che una differenza osservata tra gruppi non coincide automaticamente con l'effetto di un intervento.

## Riferimenti

- Stanford University, *Potential Outcomes Model*, STATS 60/160.
- World Bank e Inter-American Development Bank, *Impact Evaluation in Practice*, capitolo su causal inference e counterfactuals.
