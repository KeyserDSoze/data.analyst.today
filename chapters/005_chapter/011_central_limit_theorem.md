## 5.11 Teorema del Limite Centrale: perché tante medie diventano quasi normali

Il Teorema del Limite Centrale è uno dei motivi per cui la statistica inferenziale funziona così bene in problemi molto diversi.

In forma intuitiva, dice che se prendiamo campioni sufficientemente grandi da una popolazione e calcoliamo la media di ciascun campione, la distribuzione di quelle medie tende ad avvicinarsi a una distribuzione normale, anche quando i dati originali non sono normali.

Inoltre, la distribuzione delle medie è centrata sulla media della popolazione e la sua deviazione standard si riduce approssimativamente come:

\[
\frac{\sigma}{\sqrt{n}}
\]

### Caso realistico: gli importi degli ordini non sono per niente normali

Un e-commerce di arredamento analizza l'importo degli ordini.

La distribuzione è fortemente asimmetrica:

- moltissimi ordini tra 40 e 180 euro;
- alcuni ordini da 600-1.500 euro;
- pochi progetti completi da 8.000-20.000 euro.

La distribuzione individuale è quindi lontana dalla classica campana.

Il CFO però non deve prevedere il valore del singolo ordine. Vuole stimare l'average order value mensile.

Il team simula campioni casuali di 500 ordini e calcola la media di ciascun campione. Le medie risultanti sono molto più regolari della distribuzione originale.

Questo è esattamente il tipo di fenomeno spiegato dal Teorema del Limite Centrale.

### Attenzione: non significa che “n = 30” risolve tutto

Una scorciatoia spesso insegnata è che con 30 osservazioni possiamo assumere normalità.

È una regola troppo meccanica.

La velocità con cui la distribuzione campionaria della media si avvicina alla normalità dipende dalla forma della popolazione, dalla presenza di code pesanti, di outlier e dalla dipendenza tra osservazioni.

Se analizziamo importi finanziari con eventi rarissimi ma enormi, 30 osservazioni possono essere pochissime.

Se analizziamo una distribuzione relativamente simmetrica e ben comportata, possono invece essere già informative.

### Il problema della dipendenza

Il Teorema del Limite Centrale viene spesso applicato come se ogni riga fosse indipendente.

Ma immaginiamo 10.000 click provenienti da soli 120 utenti.

Abbiamo davvero 10.000 osservazioni indipendenti?

No.

Lo stesso utente può produrre molti eventi correlati. Trattare ogni click come unità indipendente può far sembrare la stima molto più precisa di quanto sia realmente.

Lo stesso problema compare con:

- transazioni ripetute dello stesso cliente;
- misure multiple dello stesso macchinario;
- ordini dello stesso negozio;
- osservazioni giornaliere consecutive;
- utenti appartenenti alla stessa azienda.

La numerosità nominale del dataset non coincide necessariamente con la numerosità informativa.

### Perché l'analista deve capirlo

Il Teorema del Limite Centrale non è una licenza per applicare formule automaticamente.

È un ponte tra dati individuali rumorosi e stime aggregate più regolari.

Ma quel ponte regge solo se comprendiamo come il campione è stato generato.

### Fonti

[^nist-clt]: NIST/SEMATECH e-Handbook of Statistical Methods, *Normal Distribution*, sezione “Theoretical Justification - Central Limit Theorem”, https://www.itl.nist.gov/div898/handbook/eda/section3/eda3661.htm
