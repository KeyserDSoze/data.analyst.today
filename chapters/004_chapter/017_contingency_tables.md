## 4.16 Tabelle di contingenza: rendere visibili le relazioni tra categorie

Non tutte le domande riguardano variabili numeriche. Molte decisioni di business mettono in relazione categorie:

- cliente nuovo o esistente;
- piano mensile o annuale;
- churn sì o no;
- canale organico, paid o referral;
- ticket risolto al primo contatto oppure no.

Una **tabella di contingenza** incrocia due variabili categoriche e rende visibile come i casi si distribuiscono tra le loro combinazioni.

Il punto non è soltanto contare. È scegliere **rispetto a quale popolazione** vogliamo leggere quelle frequenze.

### Caso simulato/composito — “I clienti annuali abbandonano meno”

La società SaaS immaginaria **CloudDesk** osserva 24.000 clienti.

| Piano | Clienti | Churn | Churn rate |
|---|---:|---:|---:|
| Mensile | 14.000 | 2.240 | 16,0% |
| Annuale | 10.000 | 700 | 7,0% |

La differenza è grande. Il team commerciale propone di spingere aggressivamente il passaggio all'annuale.

Prima di interpretare il piano come spiegazione, l'analista aggiunge una seconda dimensione: **customer tenure**.

Clienti con meno di sei mesi:

| Piano | Clienti | Churn rate |
|---|---:|---:|
| Mensile | 8.500 | 18,1% |
| Annuale | 2.000 | 16,4% |

Clienti con almeno sei mesi:

| Piano | Clienti | Churn rate |
|---|---:|---:|
| Mensile | 5.500 | 12,8% |
| Annuale | 8.000 | 4,7% |

L'associazione non scompare, ma cambia forma. Tra i clienti nuovi la differenza è piccola; tra quelli maturi è molto più ampia. Inoltre il piano annuale contiene una quota molto maggiore di clienti con tenure elevata.

L'aggregato iniziale stava quindi mescolando almeno due fenomeni:

1. differenze tra piano mensile e annuale;
2. diversa composizione dei due gruppi per anzianità.

L'EDA non deve ancora stabilire quale dei due sia causale. Deve **rendere visibile la struttura che il totale nasconde**.

### Percentuale per riga o per colonna?

Una tabella di contingenza può mostrare conteggi, percentuali per riga, percentuali per colonna o percentuali sul totale. Non sono presentazioni intercambiabili.

Se chiediamo:

> Tra i clienti mensili, quale quota fa churn?

il denominatore è il totale dei clienti mensili: ci serve una percentuale **per riga**.

Se chiediamo:

> Tra tutti i clienti che hanno fatto churn, quale quota aveva un piano mensile?

il denominatore è il totale dei churner: può servirci una percentuale **per colonna**.

La stessa matrice risponde quindi a domande differenti a seconda di come viene normalizzata.

### Conteggi e percentuali vanno letti insieme

Supponiamo di trovare un segmento con churn del 30%.

- 3 churn su 10 clienti: 30%;
- 3.000 churn su 10.000 clienti: 30%.

La percentuale è identica, ma il peso dell'evidenza e l'impatto operativo non lo sono.

In EDA è buona pratica conservare entrambi:

> **frequenza relativa + numerosità della base**.

Questo evita di trasformare segmenti minuscoli in priorità solo perché mostrano percentuali estreme.

### La tabella descrive associazioni, non interventi

Dal caso CloudDesk possiamo dire che piano, tenure e churn sono associati nei dati osservati.

Non possiamo ancora concludere:

> “se convertiamo un cliente mensile all'annuale, ridurremo il suo churn”.

Chi sceglie un annuale può essere già più convinto del prodotto, più maturo, più grande o diverso per altre caratteristiche.

I test statistici del Capitolo 5 ci aiuteranno a ragionare sull'incertezza dell'associazione. Il Capitolo 8 affronterà invece la domanda causale.

Qui il compito è più fondamentale:

> **mostrare come una relazione aggregata cambia quando condizioniamo sui gruppi che compongono la popolazione.**
