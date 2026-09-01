## 8.5 Selection bias e collider: quando il campione costruisce una relazione

Un dataset può essere perfettamente pulito e comunque rappresentare male la relazione causale che ci interessa.

Il problema può nascere **prima** dell'analisi, nel meccanismo che decide chi entra nel campione.

### Caso simulato/composito — I migliori venditori sembrano usare meno il CRM

Un'azienda B2B analizza soltanto le opportunità arrivate alla fase finale della pipeline.

Tra queste, i commerciali con meno attività registrate nel CRM hanno win rate più alto.

La conclusione superficiale è:

> “Documentare troppe attività riduce la performance.”

Ma l'arrivo alla fase finale è favorito sia da:

- qualità iniziale del lead;
- intensità commerciale.

Possiamo rappresentarlo così:

```text
qualità lead --------> fase finale <-------- intensità commerciale
```

`fase finale` è un **collider**: riceve frecce da entrambe le variabili.

Condizionando sull'essere arrivati in quella fase, possiamo creare un'associazione artificiale tra qualità del lead e intensità commerciale.

### Un collider non va “controllato perché importante”

Una regola di regressione puramente predittiva potrebbe suggerire di aggiungere una variabile molto informativa come `reached_final_stage`.

Ma causalmente il controllo può aprire un percorso che prima era chiuso.

È uno dei motivi per cui:

> **“controllare più variabili” non equivale a “controllare meglio il bias”.**

### Caso simulato/composito — NPS dei soli rispondenti

Un servizio digitale invia una survey a tutti i clienti. Risponde il 18%.

Tra i rispondenti, gli utenti più intensivi sembrano meno soddisfatti.

Ma la probabilità di rispondere aumenta sia per:

- utenti molto coinvolti;
- utenti estremamente insoddisfatti.

Studiando solo i rispondenti, analizziamo una popolazione selezionata da un meccanismo collegato alle variabili di interesse.

Il problema non è soltanto il basso response rate. È **come la probabilità di risposta dipende dal fenomeno studiato**.

### Survivorship bias

Una forma frequente di selection bias consiste nell'analizzare solo chi è rimasto abbastanza a lungo da essere osservato.

Esempi:

- retention dei clienti ancora attivi;
- produttività dei dipendenti rimasti in azienda;
- qualità dei seller che non sono stati sospesi;
- performance degli SKU sopravvissuti a una razionalizzazione;
- tempi di consegna dei soli ordini effettivamente consegnati.

### Caso simulato/composito — Il corriere “più veloce”

Un marketplace confronta i tempi medi dei soli ordini consegnati entro 30 giorni:

- corriere nuovo: 2,8 giorni;
- corriere storico: 3,4 giorni.

Il nuovo corriere sembra migliore.

Poi emerge che ha una quota molto più alta di ordini non consegnati entro 30 giorni, esclusi dalla tabella.

Il filtro rimuove proprio parte della coda negativa che dovrebbe entrare nella decisione.

### Selezione causata dal trattamento

La selezione è particolarmente pericolosa quando il trattamento influenza la probabilità di essere osservati.

Esempio:

```text
trattamento -> sopravvivenza nel campione <- severità iniziale
```

Analizzare soltanto i sopravvissuti può rompere la comparabilità creata inizialmente, perfino in un esperimento randomizzato.

Questa è una delle ragioni per cui le esclusioni post-randomizzazione devono essere trattate con estrema cautela.

### Domanda diagnostica fondamentale

Prima di aprire il notebook chiedi:

> **“Quale processo deve attraversare un'unità per comparire in questa tabella?”**

Scrivilo come funnel di selezione:

```text
popolazione target
    ↓
eleggibile
    ↓
registrata nel sistema
    ↓
ha outcome osservabile
    ↓
passa i filtri analitici
    ↓
campione finale
```

A ogni passaggio chiedi se la selezione dipende da:

- trattamento;
- outcome;
- cause del trattamento;
- cause dell'outcome.

### Regola operativa

La scheda minima dovrebbe includere:

```text
Popolazione target:
Popolazione realmente osservabile:
Filtri prima dell'analisi:
Filtri dopo il trattamento:
Chi manca?
Perché manca?
La probabilità di essere osservato dipende da trattamento/outcome?
Quale conclusione cambierebbe includendo gli esclusi?
```

> **La tabella finale non è la popolazione. È il risultato di un processo di selezione che deve entrare nel ragionamento causale.**
