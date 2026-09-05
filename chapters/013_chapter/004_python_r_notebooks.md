## 13.3 Python, R e notebook: scegliere programmabilità quando serve libertà metodologica

Python e R diventano particolarmente utili quando il problema richiede una libertà che SQL o un foglio esprimono male. La proprietà importante non è semplicemente “scrivere codice”, ma poter rappresentare in modo esplicito una sequenza di lavoro:

```text
input
→ trasformazione
→ metodo
→ diagnostica
→ output
```

con funzioni, librerie, iterazioni e test riusabili.

La domanda quindi non è “posso farlo in Python?”. Quasi sempre la risposta è sì. La domanda è: **la programmabilità riduce davvero la complessità del metodo o stiamo spostando in codice un lavoro tabellare che il motore dati eseguirebbe meglio?**

Immaginiamo un marketplace che deve analizzare **600 viste del lifecycle**, combinando paese, categoria, acquisition channel e tenure. Per ogni combinazione servono numerosità, retention, intervalli, delta dalla baseline, grafico e ranking dei deterioramenti. Costruire manualmente centinaia di pivot e chart sarebbe fragile; una funzione applicata sistematicamente alle stesse regole riduce variazioni e rende più visibile ciò che è stato eseguito. Qui il valore del codice non è prestigio tecnico: è **sistematicità**.

Programmazione e notebook diventano ancora più naturali quando servono statistica avanzata, machine learning, bootstrap, simulazione, ottimizzazione, API custom o diagnostica grafica. Ma la stessa libertà aumenta il numero dei failure mode: dipendenze, file locali, credenziali personali, chiamate di rete, stato mutabile e ambienti differenti diventano parte del processo.

### Il notebook è un laboratorio, non una garanzia

Il notebook è eccellente per EDA, prototipazione, confronto di modelli e documentazione tecnica perché mantiene testo, codice, output e grafici nello stesso spazio. Ma il suo vantaggio interattivo può introdurre **hidden state**.

Un notebook di forecasting può funzionare perfettamente il venerdì e non essere riproducibile il lunedì da una collega se `forecast_input.csv` era stato modificato a mano, alcune celle erano state eseguite fuori ordine, una variabile proveniva da un tentativo precedente o la libreria aveva una versione differente. In quel caso il problema non è “Jupyter è inaffidabile”: è che il risultato dipende da stato che non fa parte dell'artefatto verificabile.

La prova utile è più concreta:

```text
nuovo ambiente
+ input dichiarati
+ esecuzione dall'inizio
= stesso processo
```

Quando una parte del lavoro diventa stabile e riusata, può meritare una casa più testabile dello stato interattivo:

```text
notebook
├─ narrativa / exploration
├─ chiamate a funzioni stabili
└─ diagnostica

src/
├─ preparation
├─ metrics
├─ models
└─ tests
```

Non ogni notebook deve diventare software di produzione. Il punto è riconoscere **quando la logica stabile ha acquisito obblighi diversi dall'esplorazione che l'ha generata**.

### Python o R: scegliere per il sistema, non per identità

Entrambi coprono un'enorme parte del lavoro analitico. La scelta dovrebbe considerare librerie necessarie, ecosistema del team, deployment, standard interni, facilità di review e interoperabilità con la piattaforma dati. Un linguaggio leggermente meno comodo per il singolo analyst può avere un costo totale minore se altre otto persone possono revisionarlo e mantenerlo.

Con l'aumentare della criticità diventano progressivamente importanti dependency management, test, version control, logging, secret management e separazione tra configurazione e logica. Non perché “il codice richiede sempre DevOps”, ma perché **la libertà general purpose deve essere accompagnata dai controlli proporzionati alla responsabilità che il processo assume**.

Nel Tooling Decision Record, quindi, non basta scrivere `Python`. Dobbiamo dichiarare quale metodo richiede codice, quanto dato resta dopo il pushdown, se il lavoro è interattivo o ricorrente, dove gira, chi lo revisiona, dove finisce l'output e quale evento obbliga a promuovere notebook o script in un processo più governato.

> **Scegli la programmabilità quando riduce la complessità del metodo o rende il processo sistematico. Non scegliere il codice perché rende tecnicamente possibile fare tutto nello stesso posto.**

### Riferimenti

- pandas documentation: https://pandas.pydata.org/docs/
- Project Jupyter: https://jupyter.org/
