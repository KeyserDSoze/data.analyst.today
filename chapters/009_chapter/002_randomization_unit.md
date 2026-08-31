## 9.1 L'unità di randomizzazione: chi stiamo davvero assegnando?

Una delle decisioni più sottovalutate in un esperimento è scegliere l'unità di randomizzazione. Molti team partono dalla metrica e arrivano troppo tardi alla domanda fondamentale: **chi o che cosa viene assegnato al trattamento?**

Le opzioni più comuni sono:

- sessione;
- utente;
- account;
- device;
- negozio;
- area geografica;
- venditore;
- team;
- giorno o fascia temporale.

La scelta non è puramente tecnica. Determina indipendenza, contaminazione, potenza e interpretabilità.

### Caso: il checkout che cambia a ogni sessione

Torniamo alla piattaforma e-commerce del capitolo. Il team implementa inizialmente la randomizzazione per sessione perché è semplice: ogni nuova sessione riceve A oppure B.

Dopo tre giorni i dati mostrano:

| Variante | Sessioni | Conversion rate |
|---|---:|---:|
| A | 512.420 | 3,89% |
| B | 510.976 | 4,11% |

Il risultato sembra eccellente. Ma l'analista controlla l'identità degli utenti e scopre che circa il 27% degli utenti eleggibili ha avuto più di una sessione durante il test e che il 14% ha visto entrambe le esperienze.

Un utente può quindi:

1. vedere il checkout tradizionale al mattino;
2. tornare la sera;
3. vedere il checkout rapido;
4. imparare dal primo percorso qualcosa che influenza il secondo.

Il trattamento non è più isolato.

La metrica di conversione è session-level, ma la decisione di acquisto appartiene spesso allo stesso utente nel tempo.

### Randomizzare al livello della decisione

Una buona regola pratica è:

> Randomizza al livello più stabile che rappresenta l'unità decisionale rilevante, salvo forti motivi contrari.

Se il prodotto è individuale, l'utente è spesso preferibile alla sessione. In un SaaS B2B può essere l'account. In un marketplace con pricing lato seller può essere il venditore. In un test di layout di un negozio fisico può essere il punto vendita.

### Cluster randomization

A volte non possiamo randomizzare individui senza creare contaminazione.

Immagina una catena di 180 supermercati che vuole testare una nuova procedura di picking per gli ordini online. Se randomizzassimo singoli picker nello stesso negozio, i dipendenti potrebbero copiarsi procedure e organizzazione. La soluzione può essere randomizzare interi negozi.

Questo però riduce il numero effettivo di unità sperimentali: 180 negozi, non magari 4.000 dipendenti. La potenza statistica cambia drasticamente.

### Il principio operativo

Prima di avviare un test, documenta sempre:

- unità di randomizzazione;
- unità di analisi;
- unità di esposizione;
- possibilità di contaminazione tra varianti;
- eventuale clustering.

Questi quattro livelli non devono necessariamente coincidere, ma devono essere coerenti.

### Errore tipico

Un errore frequente è scegliere la randomizzazione in base a ciò che è più facile implementare e solo dopo adattare l'analisi. È l'ordine sbagliato.

L'ordine corretto è:

**decisione -> meccanismo causale -> unità di trattamento -> randomizzazione -> metrica.**