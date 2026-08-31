## 4.16 Tabelle di contingenza: quando due variabili categoriche si incontrano

Non tutte le relazioni analitiche riguardano variabili numeriche. Molte domande di business mettono in relazione categorie:

- cliente nuovo o esistente;
- abbonamento mensile o annuale;
- churn sì o no;
- canale organico, paid, referral;
- ticket risolto al primo contatto oppure no.

In questi casi uno strumento fondamentale è la **tabella di contingenza**.

### Caso: “i clienti annuali abbandonano meno”

La società SaaS **CloudDesk** osserva il churn di 24.000 clienti.

Il CFO riceve questa tabella:

| Piano | Clienti | Churn | Churn rate |
|---|---:|---:|---:|
| Mensile | 14.000 | 2.240 | 16,0% |
| Annuale | 10.000 | 700 | 7,0% |

La conclusione sembra immediata: il piano annuale riduce il churn di oltre la metà.

Il team commerciale propone quindi di incentivare aggressivamente il passaggio al piano annuale.

Ma l'analista aggiunge una seconda variabile: **anzianità del cliente**.

Tra i clienti con meno di sei mesi:

| Piano | Clienti | Churn rate |
|---|---:|---:|
| Mensile | 8.500 | 18,1% |
| Annuale | 2.000 | 16,4% |

Tra i clienti con più di sei mesi:

| Piano | Clienti | Churn rate |
|---|---:|---:|
| Mensile | 5.500 | 12,8% |
| Annuale | 8.000 | 4,7% |

La relazione esiste ancora, ma è molto meno uniforme di quanto suggerisse il primo riepilogo.

Il piano annuale contiene molti più clienti maturi, che in generale hanno una probabilità inferiore di churn. Parte della differenza aggregata dipende quindi dalla composizione dei gruppi.

### Frequenze assolute e frequenze relative

Una tabella di contingenza può mostrare conteggi assoluti, percentuali per riga, percentuali per colonna o percentuali sul totale.

La scelta cambia completamente ciò che il lettore vede.

Se vogliamo capire:

> Tra i clienti mensili, quanti fanno churn?

dobbiamo normalizzare per riga.

Se vogliamo capire:

> Tra tutti i clienti che fanno churn, quanti erano mensili?

può essere più utile normalizzare per colonna.

Usare la percentuale sbagliata è uno degli errori più frequenti nelle analisi categoriali.

### Una tabella non dimostra causalità

La tabella può mostrare associazione tra piano e churn. Non dimostra che cambiare piano provochi automaticamente una riduzione del churn.

I clienti che scelgono un annuale potrebbero essere già più convinti del prodotto, più grandi, più maturi o avere processi di acquisto differenti.

La tabella di contingenza serve quindi a rendere visibile una struttura. La spiegazione richiede ulteriori domande.

Questa distinzione prepara il terreno per i test di indipendenza e, più avanti, per il ragionamento causale.
