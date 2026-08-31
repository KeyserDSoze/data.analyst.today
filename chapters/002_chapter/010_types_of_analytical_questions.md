## 2.9 Il tipo di domanda come impegno metodologico

Il Capitolo 1 ha già distinto cinque famiglie operative di domanda:

1. **descrittiva** — che cosa è successo?
2. **diagnostica** — dove e in quali condizioni è successo?
3. **predittiva** — che cosa è probabile che succeda?
4. **causale** — che cosa cambierebbe se intervenissimo?
5. **decisionale** — quale azione conviene intraprendere date evidenza, costi e vincoli?

Non serve ripetere qui la tassonomia. Nel brief dobbiamo fare qualcosa di più concreto: **dichiarare quale tipo di pretesa dovrà sostenere l'analisi**, perché questo vincola metodo e dati.

### Lo stesso tema può contenere domande diverse

Tema: churn.

**Descrittiva**

> “Quanto è aumentato il churn negli ultimi tre mesi?”

**Diagnostica**

> “In quali coorti, piani e fasi del customer journey si concentra l'aumento?”

**Predittiva**

> “Quali clienti hanno maggiore probabilità di cancellare nei prossimi 30 giorni?”

**Causale**

> “Un contatto proattivo del customer success ridurrebbe le cancellazioni?”

**Decisionale**

> “Su quali clienti conviene usare il contatto proattivo, considerando capacità del team, valore del cliente e probabile effetto incrementale?”

Le cinque domande possono utilizzare parte degli stessi dati, ma non richiedono la stessa evidenza.

### Perché dichiararlo nel brief

Se il requester dice:

> “Voglio capire perché gli utenti abbandonano.”

potrebbe aspettarsi una lista di correlazioni diagnostiche. Oppure potrebbe aspettarsi una raccomandazione causale su quale intervento ridurrà il churn.

Se questa differenza emerge soltanto alla presentazione finale, l'analisi può essere metodologicamente corretta e comunque deludere lo stakeholder.

Il brief dovrebbe quindi contenere una riga come:

```text
Tipo di domanda: diagnostica con obiettivo di generare ipotesi per un successivo test causale.
```

oppure:

```text
Tipo di domanda: predittiva; il modello servirà a prioritizzare review umana, non a stimare l'effetto di un intervento.
```

Queste frasi delimitano ciò che l'output potrà sostenere.

### “Prescrittivo” e “decisionale”

Nella letteratura analytics è comune la distinzione tra descriptive, diagnostic, predictive e prescriptive analytics. IBM, per esempio, descrive la prescriptive analytics come il livello che usa dati, previsioni, obiettivi e vincoli per raccomandare azioni.

Fonte:
- IBM, *What is prescriptive analytics?*: https://www.ibm.com/think/topics/prescriptive-analytics

In questo libro useremo più spesso **decisionale** perché vogliamo includere anche casi in cui non esiste un ottimizzatore formale: la scelta può richiedere expected value, trade-off, capacità operativa e giudizio umano. Il Capitolo 15 approfondirà questo livello.

### Il metodo deve seguire la pretesa

Un errore frequente è scegliere il metodo perché disponibile:

- un modello predittivo non risponde automaticamente a una domanda causale;
- un confronto before/after non dimostra automaticamente l'effetto di una policy;
- una dashboard diagnostica non sceglie automaticamente l'intervento migliore;
- un algoritmo di ottimizzazione non rende corrette le assunzioni su cui è costruito.

### Campo del brief

```text
Tipo di domanda primaria:
Pretesa massima che l'analisi dovrà sostenere:
Metodo iniziale previsto:
Metodo/evidenza che sarebbe necessario per una conclusione più forte:
```

> **Dichiarare il tipo di domanda significa impegnarsi a non promettere con il linguaggio più di quanto il disegno dell'analisi possa sostenere.**
