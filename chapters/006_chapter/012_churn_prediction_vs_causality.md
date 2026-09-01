## 6.11 Churn prediction: rischio, diagnosi e persuadibilità sono problemi diversi

Dopo aver descritto segmenti, coorti, activation, retention e valore, arriva spesso una richiesta naturale:

> Possiamo prevedere chi se ne andrà?

Sì, spesso possiamo costruire un modello utile. Ma il lifecycle analysis deve fissare una distinzione prima ancora di parlare di algoritmo.

Esistono almeno tre domande diverse:

1. **Prediction** — chi ha maggiore probabilità di churnare?
2. **Diagnosis** — quali condizioni e pattern sono associati al churn?
3. **Intervention** — su quali clienti una certa azione riduce realmente il churn?

Un modello predittivo risponde soprattutto alla prima.

### Caso simulato/composito: Northstar CRM

**Northstar CRM** serve circa 18.000 aziende. Il team Data Science assegna settimanalmente a ogni account un risk score.

Tra i segnali più predittivi emergono:

- riduzione dei login;
- meno utenti attivi nel workspace;
- mancato utilizzo delle automazioni;
- aumento dei ticket al supporto;
- assenza dell'integrazione contabile.

Gli account nel decile di rischio più alto churnano molto più frequentemente della media.

Il modello è utile per il **ranking** del rischio.

Il Customer Success team propone però:

> i clienti con pochi login sono a rischio, quindi dobbiamo farli usare di più.

Il salto logico è troppo grande.

### Un segnale predittivo non è automaticamente una leva

Pochi login possono significare che:

- il prodotto è diventato meno utile;
- il champion interno ha lasciato l'azienda;
- il cliente ha acquistato un concorrente;
- il team si è ridimensionato;
- l'account ha già deciso di non rinnovare;
- il workflow è diventato più efficiente e richiede meno accessi.

Aumentare artificialmente il numero di login non risolve necessariamente nessuno di questi problemi.

Il segnale aiuta a localizzare il rischio. Non ci dice ancora quale trattamento funzioni.

### Il caso dei ticket di supporto

Nel modello Northstar, molti ticket sono associati a churn elevato.

Sarebbe assurdo concludere che bisogna impedire ai clienti di contattare il supporto.

È più plausibile che:

`problema del cliente → più ticket`

e contemporaneamente:

`problema del cliente → maggiore rischio di churn`

Il ticket è in parte un proxy del problema sottostante.

Questo esempio è utile perché rende evidente la differenza tra **predittore** e **causa**, anche senza un modello causale formale.

### Rischio elevato non significa cliente salvabile

Supponiamo che il Customer Success possa intervenire su 300 account al mese.

Se seleziona semplicemente i 300 risk score più alti, può finire per contattare soprattutto clienti che:

- hanno già comunicato la disdetta;
- stanno cessando l'attività;
- hanno completato una migrazione verso un concorrente;
- non hanno più il bisogno che il prodotto soddisfaceva.

Sono clienti facili da prevedere e difficili da influenzare.

La lista operativa dovrebbe quindi considerare almeno:

- rischio di churn;
- valore economico;
- tempo prima del momento decisionale;
- tipo di problema osservato;
- possibilità concreta di intervento.

### Risk score, value score, actionability

Un modo semplice per evitare che il modello domini la decisione è separare tre colonne:

| Dimensione | Domanda |
| --- | --- |
| Risk | Quanto è probabile l'uscita? |
| Value | Quanto valore è a rischio? |
| Actionability | Abbiamo ancora una leva plausibile e il tempo per usarla? |

Non devono necessariamente essere fuse subito in un unico punteggio.

Vederle separatamente aiuta il team a capire perché un account viene prioritizzato.

### E la persuadibilità?

Esiste una quarta domanda ancora più difficile:

> quale cliente cambierebbe comportamento **proprio grazie** al nostro intervento?

Un cliente ad alto rischio potrebbe churnare comunque. Un cliente a basso rischio sarebbe rimasto anche senza intervento. Il segmento più interessante può essere quello intermedio: clienti per i quali il trattamento produce un effetto incrementale.

Questa idea porta a uplift modeling, heterogeneous treatment effects e sperimentazione mirata.

La incontreremo nei capitoli dedicati a causalità, sperimentazione e modelli.

### Confine con i capitoli successivi

Questo capitolo non deve diventare un tutorial di machine learning.

Qui il punto è capire **dove entra la prediction nel lifecycle**.

- Nel **Capitolo 8** approfondiremo il ragionamento causale e i treatment effect.
- Nel **Capitolo 9** vedremo come progettare esperimenti e interventi controllati.
- Nel **Capitolo 10** costruiremo e valuteremo modelli predittivi, compresi leakage, calibration, threshold e monitoring.

La regola da portare avanti è semplice:

**Un modello che predice bene chi churnerà non dimostra perché churnerà e non identifica automaticamente chi possiamo salvare.**

### La domanda operativa

Prima di costruire un churn model chiediamo:

> Quale decisione prenderemo con il ranking, quanta capacità operativa abbiamo e quale evidenza useremo per scegliere l'intervento?

Se nessuno conosce la risposta, il rischio è costruire un modello tecnicamente corretto per una decisione ancora indefinita.
