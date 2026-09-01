# Capitolo 13 — Scegliere lo strumento giusto senza diventarne dipendenti

Un Data Analyst moderno può lavorare con spreadsheet, SQL, Python, R, notebook, BI, piattaforme cloud, workflow visuali, automazioni e assistenti AI.

Questa abbondanza crea un paradosso: **più strumenti conosciamo, più diventa facile introdurre tecnologia che il problema non richiede**.

Un'analisi una tantum può diventare una pipeline. Un prototipo può essere trattato come prodotto prima di sapere se produce valore. Una dashboard può cristallizzare una domanda ancora instabile. Uno script può sostituire una pivot table senza aggiungere alcuna affidabilità. E un foglio di calcolo può restare in produzione anni dopo aver superato i limiti del problema per cui era nato.

Il problema professionale non è quindi:

> Qual è il tool migliore?

È:

> **Qual è il livello minimo di complessità che permette di ottenere una risposta affidabile nel contesto reale in cui dovrà vivere?**

Questa domanda cambia completamente il capitolo.

Non confronteremo Excel, SQL, Python, BI e cloud come prodotti concorrenti. Li considereremo **superfici di lavoro con proprietà differenti**.

## 13.0 Il tool non è il punto di partenza

Prima di scegliere uno strumento servono almeno otto informazioni.

| Vincolo | Domanda |
|---|---|
| Decisione | Che cosa deve diventare possibile fare? |
| Frequenza | Una volta, ogni mese o continuamente? |
| Scala | Quanti dati, utenti, sorgenti e operazioni? |
| Metodo | Aggregazione, statistica, simulazione, ML, scenario? |
| Interazione | Serve forte manipolazione umana o esecuzione automatica? |
| Riproducibilità | Quanto deve essere ricostruibile e verificabile? |
| Rischio | Cosa succede se il processo è sbagliato o non disponibile? |
| Ownership | Chi lo userà, revisionerà e manterrà? |

Solo dopo entrano in gioco familiarità, costo, stack aziendale e disponibilità degli strumenti.

### Caso simulato/composito — il forecast del board tra due giorni

Una società B2B deve preparare una stima dei ricavi del trimestre successivo per un board meeting tra 48 ore.

Ha 4.800 opportunità commerciali già estratte dal CRM e deve discutere con Sales tre scenari su probabilità di chiusura, slittamenti e concentrazione del pipeline.

È possibile costruire:

- una pipeline Python;
- un database intermedio;
- un notebook parametrico;
- un piccolo data product.

Ma il bisogno immediato è **interattivo, esplorativo e una tantum**.

Un workbook controllato può essere una scelta migliore per il primo ciclo perché rende ipotesi e scenari modificabili davanti agli stakeholder.

Se tre mesi dopo il processo è diventato ricorrente, integra CRM, ERP e billing e produce numeri ufficiali, il requisito è cambiato.

La stessa soluzione che era adeguata al prototipo può diventare fragile in produzione.

> **La scelta di uno strumento ha una scadenza implicita: dura finché restano vere le condizioni che l'hanno resa sensata.**

## 13.0.1 Separare le funzioni

Una grande fonte di confusione nasce dal voler fare tutto nello stesso ambiente.

Un workflow può invece separare:

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

Esempio:

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

Excel può essere l'interfaccia di scenario senza essere il database.

Python può stimare il modello senza diventare il dashboard.

BI può distribuire il KPI senza essere il luogo in cui reinventiamo la business logic.

## 13.0.2 Tooling Decision Record

Il deliverable operativo del capitolo sarà il **Tooling Decision Record (TDR)**.

Non è un documento burocratico. Può essere una pagina.

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

L'ultima riga è fondamentale.

Una scelta matura non dice soltanto:

> usiamo un foglio.

Dice:

> usiamo un foglio **finché** il processo resta mensile, sotto questa scala, con due owner e senza diventare fonte ufficiale downstream.

Oppure:

> usiamo Python locale **finché** il modello rimane esplorativo e non alimenta automaticamente una decisione.

## 13.0.3 Ottimizzare il costo totale della decisione

Il costo di uno strumento non è solo licenza o compute.

Include:

- tempo per ottenere la prima evidenza;
- tempo per modificarla;
- probabilità di errore;
- effort di verifica;
- skill necessarie;
- manutenzione;
- collaborazione;
- costi cloud;
- governance;
- migrazione futura;
- costo di un incidente;
- costo dell'attesa.

Per questo la soluzione più economica da acquistare può essere la più costosa da possedere.

E quella tecnicamente più sofisticata può essere la più lenta nel generare apprendimento.

## 13.0.4 L'AI rende ancora più importante la scelta

L'AI abbassa drasticamente il costo della sintassi.

Possiamo generare formule, SQL, Python e configurazioni molto più rapidamente.

Questo non elimina il problema della scelta. Lo amplifica.

Se costruire diventa economico, diventa più facile costruire **la cosa sbagliata**.

Il Capitolo 14 entrerà nel governo degli output AI. Qui ci basta una conseguenza:

> **meno costa implementare una soluzione, più dobbiamo essere disciplinati nel verificare che serva davvero quella soluzione.**

## 13.0.5 Principio guida

La maturità tecnica non si misura dal numero di tecnologie presenti nel diagramma.

Si misura dalla capacità di rispondere:

1. perché questa soluzione è sufficiente oggi;
2. quali rischi accettiamo;
3. chi la mantiene;
4. quale requisito ci obbligherebbe a cambiarla.

> **Lo strumento giusto è quello che minimizza il costo totale di ottenere, verificare, distribuire e mantenere una risposta affidabile — senza acquistare complessità prima che serva.**
