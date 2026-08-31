## 1.15 Una checklist operativa per qualsiasi analisi

Davanti a una nuova richiesta, l'analista può usare una sequenza semplice per evitare di saltare direttamente all'esecuzione.

Non è una procedura burocratica. È un controllo contro le omissioni più costose.

### 1.15.1 Decisione

- Quale decisione o incertezza deve supportare questa analisi?
- Chi userà il risultato?
- Entro quando?
- Quanto è reversibile la decisione?
- Quale errore sarebbe più costoso: agire inutilmente o non agire quando serviva?

### 1.15.2 Domanda

- Qual è la domanda analitica esatta?
- È descrittiva, diagnostica, predittiva, causale o decisionale?
- Quali ipotesi stiamo facendo già nella formulazione?
- Quale risultato potrebbe smentire la nostra prima intuizione?

### 1.15.3 Metrica

- Come definiamo il fenomeno?
- Quali sono numeratore e denominatore, se esistono?
- Qual è la popolazione?
- Qual è la granularità temporale?
- Quali eventi sono inclusi o esclusi?
- La definizione è stabile nel tempo?

### 1.15.4 Dati

- Quali sorgenti servono?
- Chi le produce?
- Quanto sono aggiornate e complete?
- Quali trasformazioni hanno subito?
- Esistono missing value, duplicati, ritardi, cambi di schema o cambi di definizione?
- Quale parte del fenomeno non è osservata direttamente?

### 1.15.5 Confronto

- Qual è la baseline corretta?
- Dobbiamo controllare stagionalità o trend?
- Quali segmenti devono essere confrontati?
- La popolazione è comparabile tra periodi o gruppi?
- Un cambiamento di mix può spiegare il risultato aggregato?

### 1.15.6 Metodo

- Basta una decomposizione o serve inferenza statistica?
- Serve un modello predittivo?
- Serve un esperimento o un disegno causale?
- Quali assunzioni introduce il metodo?
- Esiste un approccio più semplice che risponde già alla domanda?

### 1.15.7 Verifica

- I numeri riconciliano con fonti indipendenti?
- Il risultato è robusto rispetto a segmentazioni o definizioni ragionevoli?
- Esistono spiegazioni concorrenti?
- Possiamo riprodurre l'analisi?
- Quali controlli cercherebbero un errore da un'angolazione diversa?

### 1.15.8 Comunicazione

- Qual è il messaggio principale?
- Che cosa osserviamo direttamente?
- Che cosa stiamo interpretando?
- Che cosa non sappiamo?
- Quali assunzioni influenzano la conclusione?
- Quale decisione suggerisce l'evidenza, e con quale livello di fiducia?

### 1.15.9 Misurazione dopo l'azione

- Come sapremo se la decisione ha funzionato?
- Quale metrica controlleremo?
- Per quanto tempo?
- Quali guardrail servono?
- Quale risultato ci farebbe cambiare strategia?

La checklist può richiedere due minuti o diventare un documento di progetto. La sua funzione è sempre la stessa: rendere esplicite le scelte che, se lasciate implicite, possono produrre analisi tecnicamente impeccabili e decisionalmente inutili.

### Formula del capitolo

**Problema → Domanda → Dati → Metodo → Evidenza → Interpretazione → Decisione → Azione → Misurazione**
