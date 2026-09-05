## 13.6 No-code e low-code: comprare automazione senza nascondere il software

Gli strumenti no-code e low-code abbassano il costo iniziale dell'automazione. Possono essere una scelta eccellente quando il workflow è semplice, stabile e leggibile: collegare alcune sorgenti, applicare regole deterministiche, pubblicare un output e notificare qualcuno non richiede sempre software custom.

Il vantaggio non è “non scrivere codice”. È **rendere economica un'automazione che rimane comprensibile e governabile**.

Immaginiamo un report del lunedì in cui un analyst scarica dati dal CRM, aggiorna un estratto billing, applica una tabella di mapping, produce un report e lo distribuisce a **18 manager**. Il processo richiede circa **90 minuti**. Se le sorgenti hanno connettori stabili, le regole sono semplici e gli errori sono facili da osservare, un workflow visuale può ridurre copy-paste, dimenticanze e dipendenza dalla presenza dell'analista con un costo di costruzione molto basso.

Il confine cambia quando la soluzione cresce. Un flusso lineare come:

```text
trigger
→ read
→ transform
→ publish
→ notify
```

è facile da revisionare. Ma se nel tempo compaiono decine di branch, loop, retry custom, chiamate API, mapping dinamici, stato persistente ed eccezioni accumulate, **stiamo costruendo software anche se lo rappresentiamo con blocchi**.

Nel caso simulato del team Operations, il workflow arriva a **146 blocchi, 11 branch, 8 retry e 4 API**. Quando cambia il payment provider, nessuno riesce a prevedere con sicurezza quali percorsi vengono impattati. Il problema non è che lo strumento visuale abbia “fallito”. È che il processo ha superato il livello di complessità per cui era stato scelto senza una nuova review.

### Un complexity budget rende visibile il confine

Per evitare questa crescita accidentale possiamo dichiarare nel Tooling Decision Record alcune condizioni di riesame. Per esempio:

```text
critical integrations: max 4
manual exception classes: max 3
workflow owners: almeno 2
execution log: obbligatorio
alert on failure: obbligatorio
version/change history: obbligatoria
```

I numeri non sono universali. Il loro valore è costringere il team a decidere **quando il workflow smette di essere automazione semplice e diventa un prodotto software con obblighi diversi**.

Con l'aumentare di branching, stato persistente, volume, criticità, recovery, gestione di segreti e riuso di logica comune, la migrazione può essere progressiva:

```text
workflow visuale
→ estrazione della logica critica in SQL/code
→ dataset condivisi centralizzati
→ workflow resta come orchestrazione leggera
```

Non serve una big rewrite per dimostrare maturità. Serve ridurre la parte di complessità che lo strumento corrente rende difficile da testare e possedere.

Automazione e validazione restano due cose distinte. Un processo automatizzato può eseguire ogni lunedì una definizione sbagliata con precisione perfetta. Prima di automatizzare dobbiamo ancora sapere quale input è authoritative, quali eccezioni sono legittime, che cosa succede se una sorgente manca, quali controlli validano l'output e chi riceve l'allarme.

> **No-code riduce il costo dell'automazione semplice. Quando la complessità cresce, non fingere che il processo non sia software soltanto perché il software è disegnato invece che scritto.**
