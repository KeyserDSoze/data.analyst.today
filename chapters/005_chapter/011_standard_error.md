## 5.10 Standard error: misurare quanto oscilla la stima, non quanto varia il fenomeno

La sampling distribution ci ha mostrato che una statistica cambia da campione a campione. Lo **standard error** riassume la dispersione di quella distribuzione: misura, in altre parole, quanto tende a oscillare la stima quando ripetiamo lo stesso processo di campionamento.

Per la media, in condizioni semplici di osservazioni indipendenti, una stima comune è:

`SE(x̄) ≈ s / √n`.

La formula rende visibile una relazione fondamentale: a parità di variabilità del fenomeno, aumentando il campione la media diventa più precisa. Ma la precisione migliora con la **radice quadrata** di `n`, non linearmente. Raddoppiare il campione non dimezza lo standard error; per dimezzarlo servono, in prima approssimazione, quattro volte le osservazioni.

## Deviazione standard e standard error parlano di oggetti diversi

Questa distinzione è facile da perdere perché entrambe le quantità descrivono dispersione.

La **deviazione standard** riguarda le osservazioni: quanto differiscono tra loro consegne, ordini, clienti o ticket.

Lo **standard error** riguarda una statistica: quanto differirebbe, per esempio, la media se ripetessimo il campionamento.

Un processo può avere consegne molto eterogenee e una media conosciuta con grande precisione grazie a milioni di ordini. Oppure può avere consegne abbastanza omogenee e una media poco precisa perché osserviamo pochi casi. Confondere i due livelli significa confondere **variabilità del mondo** e **incertezza della nostra conoscenza del suo centro**.

## Milano e Parma: stessa dispersione, diversa precisione

Una piattaforma di food delivery confronta i tempi medi mensili.

**Milano** osserva 48.200 ordini, media 31,4 minuti e deviazione standard 9,8 minuti. **Parma** osserva 620 ordini, media 29,9 minuti e deviazione standard 10,1 minuti.

La variabilità delle singole consegne è quasi identica. La precisione delle due medie no. Parma ha una base molto più piccola, quindi il suo valore medio può muoversi sensibilmente da un periodo all'altro anche senza un cambiamento strutturale. Se la settimana successiva passa a 33,1 minuti e poi torna a 30,4, il management non dovrebbe cercare automaticamente una nuova spiegazione operativa per ogni oscillazione. Una parte può essere semplice **sampling variability**.

Questo è anche il motivo per cui le classifiche di molti store, seller o team tendono a spingere le unità con denominatori piccoli verso gli estremi: non necessariamente perché siano sistematicamente migliori o peggiori, ma perché la loro stima è più rumorosa.

## Diecimila righe non sono necessariamente diecimila osservazioni indipendenti

La formula `s / √n` è utile proprio perché mostra il ruolo di `n`; diventa pericolosa quando interpretiamo `n` come il numero di righe senza verificare l'unità informativa.

Diecimila eventi possono provenire da diecimila utenti oppure da cento utenti con cento eventi ciascuno. Ordini dello stesso store, clienti della stessa azienda, osservazioni serialmente correlate o unità campionate in cluster condividono struttura. In questi casi la quantità di informazione indipendente può essere molto inferiore al numero fisico di record.

Lo stesso vale per survey con pesi e disegni complessi. L'errore standard corretto dipende dal processo di raccolta, dall'unità di analisi e dalle dipendenze presenti. Trattare ogni riga come indipendente può produrre un'incertezza artificialmente piccola e una sicurezza che il dataset non possiede.

Per questo un ranking professionale, quando la precisione conta, dovrebbe rendere visibile almeno la stima, il denominatore, il periodo e una misura coerente dell'incertezza. Ordinare soltanto per il punto centrale trasforma facilmente rumore in reputazione.

Lo standard error ci dà quindi l'ingrediente che mancava alla stima puntuale. Il passaggio successivo sarà usarlo per costruire intervalli; prima dobbiamo capire perché, in molti problemi, la sampling distribution della media diventa abbastanza regolare da permettere approssimazioni utili.

> **La dimensione del dataset non è la stessa cosa della quantità di informazione indipendente contenuta nel dataset.**
