# Indice degli artefatti operativi

Gli artefatti del libro non sono moduli burocratici da compilare sempre. Sono strutture di controllo che rendono esplicito un rischio specifico prima che venga nascosto dentro codice, dashboard o presentazioni.

| Artefatto | Capitolo | Domanda che protegge |
|---|---:|---|
| **Analytical Brief** | 2 | Quale decisione stiamo realmente supportando, con quale popolazione, metrica, scope e criterio di successo? |
| **Data Readiness Review** | 3 | Il dato è abbastanza affidabile e comparabile per sostenere il lavoro che vogliamo fare? |
| **EDA Evidence Map** | 4 | Quali pattern osserviamo, dove si concentrano e quali spiegazioni alternative restano aperte? |
| **Uncertainty Brief** | 5 | Quale incertezza stiamo quantificando e quale potrebbe cambiare la decisione? |
| **Lifecycle Diagnostic Map** | 6 | In quale punto del percorso utente/cliente/prodotto si concentra il fenomeno e come cambia tra coorti o stati? |
| **Temporal Decision Brief** | 7 | Quale orizzonte, frequenza e loss function rendono un forecast utile alla decisione reale? |
| **Causal Identification Brief** | 8 | Qual è il controfattuale e quale strategia rende credibile il claim causale sotto assunzioni esplicite? |
| **Experiment Contract** | 9 | Quale trattamento, popolazione, randomization unit, metrica, guardrail, durata e stopping rule proteggono il confronto? |
| **Predictive Decision Card** | 10 | Come passa un modello da score offline a policy operativa, con threshold, capacità, costi e monitoring? |
| **Analytical Data Contract** | 11 | Che cosa deve significare il dataset: grain, chiavi, metriche, tempo, inclusioni, esclusioni e invarianti? |
| **Data Flow Architecture Map** | 12 | Da dove arriva il dato, quali trasformazioni attraversa e con quali garanzie arriva al consumer? |
| **Tooling Decision Record** | 13 | Quale ambiente è proporzionato a volume, latenza, governance, costo, skill e failure cost? |
| **AI Analysis Control Sheet** | 14 | Che cosa deleghiamo all'AI, come verifichiamo l'output e quale claim può uscire dal workflow? |
| **Decision Record** | 15 | Quali alternative abbiamo considerato, perché ne preferiamo una e quali condizioni ci farebbero cambiare scelta? |
| **Decision Communication Pack** | 16 | Come comprimiamo la decisione senza rafforzare il claim, nascondere l'incertezza o perdere i trade-off? |
| **Capstone Routing Canvas** | 17 | Quali artefatti servono davvero per questo problema end-to-end e quali sarebbero complessità non giustificata? |
| **Analytics Operating Contract** | 18 | Quando una capacità ricorrente deve diventare un servizio con ownership, SLO, change management, incident e retirement? |
| **Personal Career Operating Plan** | 19 | Quali capacità mantenere, delegare, ricostruire o approfondire quando cambia il costo dei task e aumenta l'automazione? |

## Catena canonica

Il percorso base è:

```text
Analytical Brief
→ Data Readiness Review
→ EDA Evidence Map
→ Uncertainty Brief
→ Lifecycle Diagnostic Map
→ Temporal Decision Brief
→ Causal Identification Brief
→ Experiment Contract
→ Predictive Decision Card
→ Analytical Data Contract
→ Data Flow Architecture Map
→ Tooling Decision Record
→ AI Analysis Control Sheet
→ Decision Record
→ Decision Communication Pack
```

Questa sequenza descrive un **vocabolario di rischi**, non una pipeline obbligatoria.

Un analyst maturo sa anche saltare un artefatto quando non chiude nessun rischio materiale.

## Routing rapido

### Problema ancora ambiguo

Partire da **Analytical Brief**.

### Dato sospetto o non comparabile

Attivare **Data Readiness Review** prima di aumentare la sofisticazione statistica.

### Pattern interessante ma spiegazione incerta

Usare **EDA Evidence Map** e, se la decisione richiede un effetto, passare a **Causal Identification Brief**.

### Esperimento possibile

Tradurre il design in **Experiment Contract**, non soltanto in una query di analisi.

### Modello predittivo

Usare **Predictive Decision Card** per collegare score, threshold, capacità, azione e outcome.

### Definizione contestata

Prima di ottimizzare query o dashboard, formalizzare un **Analytical Data Contract**.

### Sistema ricorrente

Promuovere la capacità a **Analytics Operating Contract** soltanto quando esiste una promessa stabile da mantenere nel tempo.

### Workflow AI-assisted

Usare **AI Analysis Control Sheet** quando la delega può cambiare claim, dati, codice o azioni; escalation e verifica devono crescere con il failure cost.

### Decisione pronta per stakeholder

Separare **Decision Record** — ragionamento completo — da **Decision Communication Pack** — superficie compressa per il pubblico.

> **La maturità non consiste nell'usare tutti gli artefatti. Consiste nel sapere quale rischio merita di essere reso esplicito prima che diventi una decisione invisibile.**
