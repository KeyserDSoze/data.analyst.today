## 2.9 Il tipo di domanda è una promessa metodologica

Il Capitolo 1 ha già distinto domande descrittive, diagnostiche, predittive, causali e decisionali. Nel brief non serve ripetere quella tassonomia come teoria. Serve usarla per dichiarare **quale tipo di pretesa l'analisi avrà il diritto di sostenere**.

La distinzione conta perché lo stesso tema può generare domande molto diverse. Sul churn possiamo misurare quanto sia aumentato negli ultimi tre mesi, localizzare il peggioramento per coorte e piano, prevedere quali clienti abbiano maggiore probabilità di cancellare, stimare se un contatto proattivo ridurrebbe le cancellazioni oppure decidere su quali clienti valga economicamente la pena intervenire.

Parte dei dati può essere la stessa, ma l'evidenza richiesta cambia radicalmente. Una segmentazione può essere sufficiente per una domanda diagnostica. Un modello predittivo può ordinare clienti per rischio senza spiegare che cosa accadrebbe se li contattassimo. Una domanda causale richiede un confronto controfattuale credibile. Una domanda decisionale aggiunge costi, capacità, alternative e valore degli esiti.

Per questo una frase apparentemente innocua come:

> “Voglio capire perché gli utenti abbandonano.”

può nascondere aspettative incompatibili. Lo stakeholder può aspettarsi un'analisi dei segmenti associati al churn oppure una raccomandazione su quale intervento lo ridurrà. Se questa differenza emerge soltanto alla presentazione finale, possiamo avere svolto un lavoro corretto e consegnato la risposta alla domanda sbagliata.

## Delimitare in anticipo ciò che potremo dire

Nel brief basta spesso una riga molto esplicita:

```text
Tipo di domanda: diagnostica con obiettivo di generare ipotesi per un successivo test causale.
```

oppure:

```text
Tipo di domanda: predittiva; il modello servirà a prioritizzare review umana, non a stimare l'effetto di un intervento.
```

Queste specifiche non limitano inutilmente il lavoro. Proteggono il linguaggio finale. Se abbiamo concordato una diagnosi osservazionale, non possiamo trasformare una correlazione interessante in “questa leva causa churn” soltanto perché il management desidera una raccomandazione più netta.

Nella letteratura analytics è comune parlare di descriptive, diagnostic, predictive e prescriptive analytics. IBM descrive la prescriptive analytics come l'uso di dati e previsioni per raccomandare corsi d'azione.[^ibm-prescriptive] In questo libro useremo più spesso il termine **decisionale**, perché vogliamo includere anche situazioni in cui non esiste un ottimizzatore formale: la scelta può dipendere da expected value, vincoli operativi, reversibilità e giudizio umano.

## Il metodo segue la promessa, non la moda

Dichiarare il tipo di domanda impedisce anche un errore molto comune: scegliere il metodo perché è disponibile o prestigioso. Un modello predittivo non risponde automaticamente a una domanda causale; un before/after non dimostra automaticamente l'effetto di una policy; una dashboard diagnostica non seleziona l'intervento migliore; un algoritmo di ottimizzazione non rende vere le assunzioni con cui lo alimentiamo.

Il metodo appropriato è quello capace di sostenere la pretesa concordata, con il livello di affidabilità richiesto dalla decisione.

Il campo del brief resta quindi breve:

```text
Tipo di domanda primaria:
Pretesa massima che l'analisi dovrà sostenere:
Metodo iniziale previsto:
Metodo/evidenza necessario per una conclusione più forte:
```

> **Specificare il tipo di domanda significa decidere prima quale salto inferenziale siamo autorizzati a fare, invece di negoziarlo dopo aver visto i dati.**

---

### Fonte

[^ibm-prescriptive]: IBM, *What is prescriptive analytics?*. https://www.ibm.com/think/topics/prescriptive-analytics
