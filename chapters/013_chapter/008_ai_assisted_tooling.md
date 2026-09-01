## 13.7 AI-assisted tooling: quando costruire costa meno, scegliere bene conta di più

Il Capitolo 14 sarà dedicato al lavoro analitico assistito dall'AI: errori semantici, eval, privacy, auditability, agenti e verifica.

Qui ci interessa un solo effetto sul tool selection:

> **l'AI riduce il costo marginale di costruire soluzioni in strumenti che prima richiedevano più specializzazione.**

Oggi un analyst può ottenere rapidamente:

- formule spreadsheet;
- SQL;
- Python/R;
- DAX;
- trasformazioni;
- documentazione;
- test iniziali;
- spiegazioni di codice legacy.

Questo rende i confini tra strumenti più permeabili.

Non rende irrilevante scegliere il contesto di esecuzione.

### La falsa conclusione: “ora posso usare qualsiasi tool”

Se un assistente può scrivere Python per noi, potremmo pensare che Python sia sempre una scelta praticabile.

Ma restano domande che non riguardano la sintassi:

- dove vive il dato?
- dove verrà eseguito il codice?
- chi lo revisiona?
- come gestiamo le dipendenze?
- chi mantiene il processo tra sei mesi?
- cosa succede se l'output alimenta un sistema downstream?
- possiamo verificare ciò che è stato generato?

L'AI può abbassare il **build cost** senza abbassare il **ownership cost**.

### Caso simulato/composito — modello churn in venti minuti

Un analyst chiede a un assistente di:

1. generare la query;
2. costruire il training set;
3. addestrare un classificatore;
4. mostrare feature importance;
5. produrre una lista clienti.

In pochi minuti ottiene un modello con AUC 0,96.

Poi scopre che `cancel_reason` è valorizzato soltanto dopo la cancellazione.

La velocità ha ridotto il costo dell'implementazione.

Non ha ridotto il costo della comprensione del problema.

Anzi: ha reso possibile arrivare molto più velocemente a un sistema plausibile ma inutilizzabile.

### AI come acceleratore di migrazione

C'è anche un effetto positivo importante.

Un team può avere un workbook cresciuto troppo, ma rimandare la migrazione perché riscrivere:

- formule;
- macro;
- SQL;
- documentazione;

è costoso.

L'AI può ridurre questo switching cost aiutando a:

- spiegare logica legacy;
- tradurre formule in SQL/Python;
- generare test di equivalenza;
- documentare casi limite;
- produrre una prima versione della migrazione.

Questo non rende la migrazione automatica.

Ma cambia l'economia della decisione “restiamo qui perché riscrivere costa troppo”.

### Tool convergence

Python in Excel è un esempio concreto di convergenza: Microsoft permette di usare Python e librerie analitiche all'interno del workbook.[^python-excel-13]

Altri ambienti incorporano assistenti per query, dashboard o codice.

Di conseguenza, una tassonomia basata soltanto sui nomi degli strumenti diventa meno utile.

Conta di più chiedere:

- dove gira il calcolo;
- quali dati può vedere;
- quale semantica eredita;
- come viene versionato;
- chi può approvarlo;
- come viene distribuito l'output.

### “Can build” non significa “should build”

Prima dell'AI un piccolo costo tecnico poteva funzionare come freno naturale:

> non costruiamo questa automazione perché richiede tre giorni.

Ora può richiedere trenta minuti.

Quel freno è più debole.

Serve sostituirlo con un criterio esplicito:

> **quale requisito concreto rende questa automazione o questo tool migliore dell'alternativa più semplice?**

### Campo del Tooling Decision Record

Quando l'AI influenza la scelta annotiamo:

```text
AI-assisted step:
human owner:
required context / schema:
verification method:
change in build cost:
change in maintenance cost:
security / data boundary:
can output execute or only propose?:
rollback / review for write actions:
exit condition:
```

### Regola operativa

> **Usa l'AI per ridurre il costo di costruzione, comprensione e migrazione. Non lasciare che il costo basso della costruzione diventi una ragione sufficiente per costruire.**

[^python-excel-13]: Microsoft Support, *Introduction to Python in Excel*, https://support.microsoft.com/en-us/excel/python/introduction-to-python-in-excel
