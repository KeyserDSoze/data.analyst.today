## 6.13 Checklist operativa: prima di parlare di retention o churn

Prima di costruire una dashboard o lanciare un modello, l'analista dovrebbe poter rispondere a queste domande.

### Definizione

- Cosa significa “attivo” nel nostro prodotto?
- Qual è l'evento di activation e perché rappresenta valore?
- Come definiamo churn?
- Qual è la finestra temporale coerente con il ciclo naturale del prodotto?
- La reactivation cambia lo stato di churn o viene trattata separatamente?

### Coorti

- Qual è la dimensione di coorte più utile: signup, primo acquisto, primo pagamento, contratto, mese di activation?
- Le coorti confrontate hanno la stessa maturità?
- Stiamo mescolando utenti con lifecycle diversi?

### Funnel

- Gli step sono realmente ordinati?
- Il denominatore è corretto a ogni passaggio?
- Gli eventi possono ripetersi?
- Una stessa persona può apparire più volte nello stesso step?
- Esistono problemi di tracking o cambi di definizione nel tempo?

### Retention

- Misuriamo ritorno generico o ritorno al comportamento che genera valore?
- Usiamo N-day, rolling o unbounded retention? La scelta è coerente con il prodotto?
- La curva viene letta nel suo insieme o solo tramite pochi punti?
- Esistono momenti del lifecycle in cui l'hazard aumenta?

### Churn

- Parliamo di customer churn, logo churn, revenue churn, gross revenue retention o net revenue retention?
- Il churn è volontario o involontario?
- Stiamo distinguendo cancellazione da mancato rinnovo?
- Le contrazioni di revenue vengono trattate separatamente dalle cancellazioni complete?

### Prediction

- Il modello serve a prioritizzare o a spiegare?
- Le feature predittive sono disponibili prima dell'evento di churn?
- Esiste data leakage?
- Il team ha capacità operativa per agire sui clienti identificati?
- Rischio e actionability vengono confusi?

### Decisione

La domanda finale è sempre la stessa:

> Se questa analisi cambia, quale decisione cambierà con essa?

Se nessuno sa rispondere, probabilmente il problema non è ancora stato formulato abbastanza bene.
