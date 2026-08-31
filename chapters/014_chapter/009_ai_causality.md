## 14.8 AI e causalità: velocità di ipotesi, non scorciatoia verso la verità
L'AI è molto brava a trovare pattern, proporre spiegazioni e suggerire variabili da controllare. Questo la rende potentissima nell'analisi causale, ma anche pericolosa: può produrre una storia causale perfettamente plausibile partendo da dati che supportano solo un'associazione.

Immaginiamo che un'azienda SaaS osservi:

- clienti che partecipano ai webinar: churn 5,8%;
- clienti che non partecipano: churn 12,4%.

Un assistente AI potrebbe concludere rapidamente:

> “I webinar riducono il churn di circa 6,6 punti percentuali.”

La frase è elegante, numerica e probabilmente sbagliata.

Chi partecipa ai webinar potrebbe essere già più coinvolto, avere account più grandi, CSM più attivi o una maggiore maturità digitale. L'AI può aiutare a costruire il DAG, suggerire confondenti, cercare possibili bias e scrivere il codice per matching, regression adjustment o Difference-in-Differences. Ma non può trasformare automaticamente un dataset osservazionale in un esperimento.

## Cosa delegare all'AI

Possiamo chiederle di:

- elencare spiegazioni alternative;
- costruire un DAG preliminare;
- identificare potenziali confondenti e mediatori;
- verificare precedenza temporale;
- proporre disegni sperimentali o quasi-sperimentali;
- generare controlli di robustness;
- simulare scenari controfattuali;
- cercare variabili post-treatment finite erroneamente nel modello.

Ma il punto finale resta umano:

**Quale confronto sarebbe credibile se volessimo sostenere una conclusione causale?**

## Caso realistico: il coupon “miracoloso”

Un retailer usa un agente AI per analizzare 2,4 milioni di clienti. Il sistema trova che i clienti che hanno ricevuto un coupon mostrano un aumento del 19% nel valore speso nei successivi 30 giorni.

Il management propone immediatamente di estendere il programma.

Un analista verifica il processo di assegnazione del coupon e scopre che il marketing lo invia soprattutto a clienti che:

- hanno visitato il sito negli ultimi 72 ore;
- hanno almeno un articolo in wishlist;
- hanno aperto almeno due email recenti.

Il coupon non è assegnato casualmente: viene dato a clienti già vicini all'acquisto.

L'AI aveva trovato un pattern vero. L'interpretazione era sbagliata.

L'analista propone quindi un holdout randomizzato del 10% tra i clienti eleggibili. Il test mostra un incremento reale di conversione del 3,1%, non del 19%.

L'AI ha accelerato l'indagine. Il design causale ha prodotto la risposta.

## Regola operativa

Quando l'AI usa parole come:

- causa;
- impatto;
- effetto;
- driver;
- influenza;
- ha generato;

chiediamoci immediatamente:

1. il trattamento è stato assegnato in modo credibile?
2. quali confondenti possono spiegare il pattern?
3. stiamo controllando variabili post-treatment?
4. l'effetto è locale o generalizzabile?
5. quale counterfactual stiamo implicitamente assumendo?

**L'AI può moltiplicare le ipotesi causali. Non moltiplica automaticamente la credibilità causale.**

### Fonti

- World Bank, *Impact Evaluation in Practice*: https://www.worldbank.org/en/programs/sief-trust-fund/publication/impact-evaluation-in-practice
- NIST AI RMF: https://www.nist.gov/itl/ai-risk-management-framework
