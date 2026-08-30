## 1.15 Una checklist operativa per qualsiasi analisi

Davanti a una nuova richiesta, l'analista può usare una sequenza semplice per evitare di saltare direttamente all'esecuzione.

### 1.15.1 Decisione

- Quale decisione deve supportare questa analisi?
- Chi prenderà la decisione?
- Entro quando?
- Quale errore sarebbe più costoso: un falso allarme o un problema non rilevato?

### 1.15.2 Domanda

- Qual è la domanda analitica esatta?
- È descrittiva, diagnostica, predittiva o causale?
- Quali ipotesi stiamo implicitamente facendo?

### 1.15.3 Metrica

- Come definiamo il fenomeno?
- Qual è il numeratore?
- Qual è il denominatore?
- Qual è la granularità temporale?
- Quali eventi sono inclusi o esclusi?

### 1.15.4 Dati

- Quali sorgenti servono?
- Chi le produce?
- Quanto sono aggiornate?
- Quali trasformazioni hanno subito?
- Esistono missing value, duplicati, ritardi, cambi di schema o cambi di definizione?

### 1.15.5 Confronto

- Qual è la baseline corretta?
- Dobbiamo controllare stagionalità o trend?
- Quali segmenti devono essere confrontati?
- La popolazione è comparabile tra i periodi?

### 1.15.6 Metodo

- È sufficiente una tabella o serve statistica inferenziale?
- Serve un modello?
- Serve un esperimento?
- Stiamo cercando associazioni o effetti causali?

### 1.15.7 Verifica

- Il risultato è robusto rispetto a definizioni alternative?
- Esistono spiegazioni concorrenti?
- I numeri tornano con altre fonti?
- Possiamo riprodurre l'analisi?

### 1.15.8 Comunicazione

- Qual è il messaggio principale?
- Cosa sappiamo?
- Cosa non sappiamo?
- Quali assunzioni influenzano la conclusione?
- Quale azione suggerisce l'evidenza?

### 1.15.9 Misurazione dopo l'azione

- Come sapremo se la decisione ha funzionato?
- Quale metrica controlleremo?
- Per quanto tempo?
- Quale risultato ci farebbe cambiare strategia?

Questa checklist non è una procedura rigida. È un dispositivo mentale. Alcune analisi richiederanno pochi minuti, altre settimane. Ma la struttura rimane utile perché costringe l'analista a rendere esplicite decisioni che altrimenti resterebbero implicite.

### Formula del capitolo

**Decisione → Domanda → Definizione → Dati → Metodo → Evidenza → Interpretazione → Azione → Misurazione**
