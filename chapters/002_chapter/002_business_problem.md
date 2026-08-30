## 2.1 Un problema di business non è ancora una domanda analitica

Una delle competenze più importanti di un analista è riconoscere la differenza tra **problema di business** e **problema analitico**.

Il problema di business riguarda un risultato, un rischio, un'opportunità o una decisione. Il problema analitico definisce invece ciò che possiamo osservare, misurare e confrontare per ridurre l'incertezza su quel problema.

Esempio:

> "Stiamo perdendo clienti."

È un problema di business.

Una possibile traduzione analitica è:

> "Il tasso di churn a 90 giorni dei clienti acquisiti negli ultimi sei mesi è aumentato rispetto alle coorti precedenti? In quali segmenti si concentra l'aumento e quali cambiamenti osservabili precedono maggiormente l'abbandono?"

La seconda formulazione contiene elementi che la prima non aveva:

- una definizione operativa di churn;
- un orizzonte temporale;
- una popolazione;
- un confronto;
- una segmentazione;
- una direzione d'indagine.

### Il rischio della falsa precisione

Trasformare una richiesta vaga in una domanda precisa non significa inventare precisione. Se l'organizzazione non ha ancora deciso cosa significhi "cliente perso", l'analista non dovrebbe scegliere una definizione di nascosto.

Per esempio, un cliente è churned quando:

- cancella formalmente l'abbonamento?
- non acquista da 30 giorni?
- non acquista da 90 giorni?
- passa sotto una soglia minima di utilizzo?
- smette di generare margine positivo?

Queste definizioni possono produrre numeri molto diversi.

Il compito dell'analista è rendere visibili queste scelte.

### La regola della riscrittura

Prima di iniziare un'analisi, prova a riscrivere la richiesta in questo formato:

> **Dobbiamo capire [fenomeno] per decidere [azione o scelta], osservando [popolazione] nel periodo [tempo], usando [metriche] e confrontando [baseline o alternative].**

Esempio:

> Dobbiamo capire perché il margine del canale e-commerce è sceso per decidere se intervenire su prezzi, promozioni o costi logistici, osservando ordini e clienti degli ultimi dodici mesi e confrontandoli con lo stesso periodo precedente.

Questa semplice riscrittura obbliga a esplicitare ciò che spesso rimane implicito.

### Le domande che smontano un problema vago

Quando ricevi una richiesta generica, chiedi:

1. **Che cosa sta succedendo?**
2. **Perché è importante?**
3. **Quale decisione potrebbe cambiare in base all'analisi?**
4. **Chi deve prendere quella decisione?**
5. **Qual è la definizione esatta del fenomeno?**
6. **Rispetto a quale baseline diremo che il fenomeno è migliorato o peggiorato?**
7. **Quale livello di dettaglio serve?**
8. **Quanto rapidamente serve una risposta?**
9. **Quale errore sarebbe più costoso: un falso allarme o non vedere un problema reale?**

L'ultima domanda è particolarmente importante: analisi diverse possono richiedere soglie e livelli di evidenza diversi a seconda del costo degli errori.

## Un principio da ricordare

**Non analizzare una frase. Analizza una decisione.**

La frase iniziale è solo il punto di partenza.