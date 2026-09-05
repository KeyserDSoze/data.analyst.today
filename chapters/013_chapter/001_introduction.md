# Capitolo 13 — Scegliere lo strumento giusto senza diventarne dipendenti

Un Data Analyst moderno può lavorare con spreadsheet, SQL, Python, R, notebook, BI, piattaforme cloud, workflow visuali, automazioni e assistenti AI. Questa abbondanza è utile, ma crea un paradosso: **più strumenti conosciamo, più diventa facile introdurre tecnologia che il problema non richiede**.

Un'analisi una tantum può diventare una pipeline prima di aver dimostrato valore. Un prototipo può essere trattato come prodotto. Una dashboard può cristallizzare una domanda ancora instabile. Uno script può sostituire una pivot table senza aggiungere affidabilità. Un foglio può invece restare in produzione per anni, molto dopo aver superato il contesto per cui era nato.

Il problema professionale non è quindi scegliere *il tool migliore*. È scegliere **il livello minimo di complessità che permette di ottenere una risposta affidabile nel contesto reale in cui dovrà vivere**.

Questa è la stella polare del capitolo. Non useremo Excel, SQL, Python, BI o cloud come identità professionali o come tappe di una scala di maturità. Li tratteremo come superfici di lavoro con proprietà differenti. Una soluzione è matura quando è proporzionata alla decisione, al rischio e al lifecycle del lavoro, non quando contiene più tecnologia.

## 13.0 Prima del tool viene la responsabilità

Prima di scegliere uno strumento dobbiamo capire che cosa il lavoro deve diventare. Le domande fondamentali sono abbastanza stabili:

| Vincolo | Domanda |
|---|---|
| Decisione | Che cosa deve diventare possibile fare? |
| Frequenza | Una volta, ogni mese o continuamente? |
| Scala | Quanti dati, utenti, sorgenti e operazioni? |
| Metodo | Aggregazione, statistica, simulazione, ML, scenario? |
| Interazione | Serve manipolazione umana o esecuzione automatica? |
| Riproducibilità | Quanto deve essere ricostruibile e verificabile? |
| Rischio | Cosa succede se il processo è sbagliato o indisponibile? |
| Ownership | Chi lo userà, revisionerà e manterrà? |

Solo dopo ha senso discutere familiarità, costo, stack aziendale e disponibilità dei prodotti.

Consideriamo un forecast per un board meeting tra 48 ore. Una società B2B ha già estratto **4.800 opportunità** dal CRM e deve discutere con Sales tre scenari su probabilità di chiusura, slittamenti e concentrazione della pipeline. Possiamo costruire un notebook parametrico, una pipeline Python o un piccolo data product. Ma il bisogno immediato è esplorativo, interattivo e una tantum: un workbook controllato può essere la scelta migliore perché rende le ipotesi modificabili davanti agli stakeholder e permette di arrivare rapidamente a evidenza verificabile.

Tre mesi dopo lo stesso processo potrebbe essere ricorrente, integrare CRM, ERP e billing e alimentare numeri ufficiali. A quel punto il requisito è cambiato. Non significa che il workbook fosse una scelta sbagliata all'inizio; significa che **la scelta di uno strumento ha una scadenza implicita: dura finché restano vere le condizioni che l'hanno resa sensata**.

## Separare le responsabilità evita il falso problema del tool unico

Un workflow analitico può distribuire responsabilità diverse su ambienti diversi:

```text
storage / source of truth
        ↓
transformation
        ↓
analysis / modeling
        ↓
serving
        ↓
decision interface
```

Per esempio:

```text
warehouse
   ↓ SQL
analytical dataset
   ↓ Python
simulation
   ↓ certified table
BI
   ↓
manager
```

Excel può essere l'interfaccia di scenario senza diventare il database. Python può stimare un modello senza diventare il dashboard. BI può distribuire un KPI senza essere il luogo in cui reinventiamo la business logic. La domanda non è quindi “quale tool vince?”, ma **quale responsabilità assegniamo a ciascun componente e perché**.

## Il deliverable: Tooling Decision Record

Per rendere questa scelta verificabile useremo un **Tooling Decision Record (TDR)**. Può stare in una pagina; il suo valore non è burocratico, ma storico: tra sei mesi deve permettere di capire perché una decisione era sensata e se le condizioni sono cambiate.

```text
Decision / use case:
Current stage: explore | prototype | recurring | production
Data location and scale:
Frequency / freshness:
Users / consumers:
Method required:
Risk if wrong / unavailable:
Reproducibility requirement:
Candidate tools:
Chosen tool / combination:
Why this is sufficient:
Why alternatives were rejected:
Known limitations:
Owner:
Exit condition / migration trigger:
Review date:
```

La voce più importante è l'**exit condition**. Una scelta matura non dice soltanto “usiamo un foglio”; dice “usiamo un foglio finché il processo resta mensile, sotto questa scala, con questi owner e senza diventare fonte ufficiale downstream”. Allo stesso modo, un notebook può rimanere l'ambiente giusto finché il lavoro è esplorativo; quando alimenta automaticamente Operations, è comparsa una responsabilità nuova e serve una nuova design review.

## Il costo da ottimizzare è quello della decisione

Il costo di uno strumento non coincide con licenza o compute. Include il tempo per ottenere la prima evidenza, modificarla e verificarla; la probabilità di errore; la manutenzione; le skill necessarie; la collaborazione; la governance; il costo di un incidente; il costo di migrare in futuro e, soprattutto, il costo dell'attesa.

Per questo la soluzione più economica da acquistare può essere la più costosa da possedere, mentre quella tecnicamente più sofisticata può essere la più lenta nel generare apprendimento. La domanda economica del capitolo sarà sempre: **quanto costa ottenere, verificare, distribuire e mantenere una risposta affidabile?**

L'AI rende questo criterio ancora più importante. Generare formule, SQL, Python o configurazioni costa meno di prima. Ma abbassare il **build cost** non abbassa automaticamente ownership, manutenzione, rischio o costi di failure. Se costruire diventa economico, diventa anche più facile costruire rapidamente la cosa sbagliata.

Il Capitolo 14 entrerà nel governo degli output AI. Qui ci basta fissare la conseguenza sul tooling:

> **“Can build” non significa “should build”. Più è economico implementare una soluzione, più dobbiamo essere disciplinati nel dimostrare che quella complessità serve davvero.**

La maturità tecnica non si misura dal numero di tecnologie nel diagramma. Si misura dalla capacità di spiegare perché una soluzione è sufficiente oggi, quali rischi accettiamo, chi la possiede e quale requisito ci obbligherebbe a cambiarla.

> **Lo strumento giusto è quello che minimizza il costo totale di ottenere una risposta affidabile senza acquistare complessità prima che serva.**
