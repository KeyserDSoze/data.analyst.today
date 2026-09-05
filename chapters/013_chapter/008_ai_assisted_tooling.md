## 13.7 AI-assisted tooling: quando costruire costa meno, scegliere bene conta di più

Il Capitolo 14 sarà dedicato al lavoro analitico assistito dall'AI. Qui ci interessa una conseguenza più limitata ma decisiva per il tool selection: **l'AI riduce il costo marginale di costruire formule, query, codice, automazioni e documentazione**.

Questa riduzione cambia l'economia delle alternative. Non cambia però le responsabilità del processo.

Se un assistente può scrivere Python per noi, Python diventa più accessibile; non diventa automaticamente il posto giusto in cui far vivere il workload. Restano le domande su data location, execution environment, dipendenze, review, manutenzione, sicurezza, downstream e rollback. In altre parole, l'AI può abbassare il **build cost** senza abbassare il **ownership cost**.

### La velocità può comprimere il tempo prima dell'errore

Un analyst può chiedere a un assistente di generare una query, costruire un training set, addestrare un classificatore, mostrare feature importance e produrre una lista clienti. Nel nostro caso simulato, in pochi minuti compare un modello con **AUC 0,96**. Solo dopo emerge che `cancel_reason` è valorizzato dopo la cancellazione e introduce leakage.

L'AI non ha reso il processo meno rigoroso per definizione. Ha semplicemente permesso di arrivare molto più rapidamente a un artefatto plausibile. **Il costo della comprensione del problema non è diminuito quanto il costo dell'implementazione.** Questo squilibrio rende ancora più importante mantenere frontiere informative, contract e validation gate.

### L'AI può anche ridurre il costo di uscita

Lo stesso abbassamento del build cost può essere utile quando una soluzione ha superato il proprio contesto. Un workbook con formule e macro può restare troppo a lungo in produzione perché riscriverlo sembra costoso. Un assistente può accelerare la lettura della logica legacy, la traduzione in SQL/Python, la generazione di test di equivalenza e la documentazione dei casi limite.

Questo non rende la migrazione automatica, ma cambia il TCO della scelta “restiamo qui perché spostarci costa troppo”. Il sunk cost diventa un argomento un po' meno forte, mentre la verifica di parity e semantic continuity resta indispensabile.

Python in Excel è un esempio concreto della convergenza tra superfici che un tempo sembravano separate: Microsoft permette oggi di eseguire Python nell'ambiente del workbook.[^python-excel-13] Altri prodotti incorporano assistenti per query, dashboard e codice. Di conseguenza, una tassonomia basata soltanto sul nome del tool perde valore. Diventa più utile chiedere **dove gira il calcolo, quali dati può vedere, quale semantica eredita, come viene versionato e chi può approvarne l'output**.

### “Can build” non significa “should build”

Prima dell'AI un costo tecnico di tre giorni poteva funzionare come freno naturale a un'automazione marginale. Se oggi la prima versione richiede trenta minuti, quel freno scompare. Dobbiamo sostituirlo con una domanda esplicita:

> **Quale requisito concreto rende questa soluzione migliore dell'alternativa più semplice?**

Nel Tooling Decision Record conviene quindi separare ciò che l'AI riduce — tempo di costruzione, spiegazione, migrazione — da ciò che può lasciare invariato o perfino aumentare: manutenzione, dipendenze, superficie di security, review, rischio di output plausibili e costo di ownership.

> **Usa l'AI per ridurre il costo di costruzione, comprensione e migrazione. Non lasciare che il costo basso della costruzione diventi una ragione sufficiente per costruire.**

[^python-excel-13]: Microsoft Support, *Introduction to Python in Excel*, https://support.microsoft.com/en-us/excel/python/introduction-to-python-in-excel
