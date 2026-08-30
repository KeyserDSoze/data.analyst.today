## 4.12 Caso studio: la correlazione che quasi cambiò la strategia di marketing

Una società e-commerce di arredamento, che chiameremo **Northstar Home**, chiude il trimestre con una sorpresa. I clienti acquisiti tramite campagne social mostrano un valore medio dell'ordine più alto rispetto agli altri canali.

Il team marketing porta in riunione un numero molto forte: correlazione di 0,76 tra spesa social settimanale e average order value.

La proposta è immediata: spostare 600.000 euro di budget annuale da search a social.

A prima vista sembra una decisione data-driven.

L'analista apre però l'analisi prima di approvare la conclusione.

### Passo 1: guardare i punti

Lo scatter plot mostra una relazione positiva, ma anche quattro settimane molto distanti dal resto. Sono le settimane di Black Friday, pre-Natale e due campagne di lancio della nuova linea premium.

Senza quelle quattro settimane, la correlazione scende da 0,76 a 0,31.

Questo non rende i quattro punti "sbagliati". Significa che stanno dominando la relazione.

### Passo 2: aggiungere il tempo

Le settimane con più spesa social coincidono con quelle in cui il catalogo promuove prodotti di fascia alta. Anche il valore medio dell'ordine cresce per tutti i canali.

Il team stava osservando contemporaneamente:

- maggiore investimento social;
- maggiore domanda stagionale;
- mix di prodotto più costoso;
- promozioni bundle;
- incremento generale del traffico.

### Passo 3: segmentare

L'analista confronta l'AOV per canale, categoria prodotto e settimana.

Risultato semplificato:

| Canale | AOV complessivo | AOV standard products | AOV premium products |
| --- | ---: | ---: | ---: |
| Social | €184 | €121 | €296 |
| Search | €169 | €128 | €301 |
| Direct | €176 | €126 | €299 |

Social aveva AOV più alto nel totale soprattutto perché portava una quota maggiore di utenti sulle campagne premium. All'interno delle stesse categorie, non emergeva un vantaggio sistematico.

### Passo 4: riformulare la domanda

La domanda iniziale era:

> La spesa social aumenta il valore medio dell'ordine?

Dopo l'EDA diventa:

> Il canale social è più efficace nel portare clienti verso categorie premium, e questo effetto produce margine incrementale sufficiente a giustificare una riallocazione di budget?

È una domanda molto diversa. Richiede di separare composizione del traffico, causalità, costo di acquisizione e marginalità.

### Passo 5: la decisione

L'azienda non sposta immediatamente 600.000 euro. Decide invece di realizzare un test controllato su sei settimane, mantenendo costante il mix creativo e misurando non solo AOV ma anche conversion rate, CAC e contribution margin.

L'EDA non ha "risposto" definitivamente alla domanda. Ha evitato che una correlazione plausibile diventasse prematuramente una decisione costosa.

Questa è una delle funzioni più importanti dell'analisi esplorativa: **trasformare una storia convincente in una domanda verificabile**.

NIST distingue esplicitamente correlazione e causalità: due variabili possono muoversi insieme senza che una provochi il cambiamento dell'altra.[^nist-correlation]

[^nist-correlation]: NIST, *Correlation*: https://www.nist.gov/glossary-term/21291