# Indice degli artefatti operativi

Gli artefatti del libro non sono moduli burocratici da compilare sempre. Sono strutture di controllo che rendono esplicito un rischio specifico prima che venga nascosto dentro codice, dashboard, automazioni o presentazioni.

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
| **Tooling Decision Record** | 13 | Quale ambiente è proporzionato a problema, lifecycle, collaborazione, riproducibilità, TCO e failure cost? |
| **AI Analysis Control Sheet** | 14 | Che cosa deleghiamo all'AI, come verifichiamo l'output e quale claim può uscire dal workflow? |
| **Decision Record** | 15 | Quali alternative abbiamo considerato, perché ne preferiamo una e quali condizioni ci farebbero cambiare scelta? |
| **Decision Communication Pack** | 16 | Come comprimiamo la decisione senza rafforzare il claim, nascondere l'incertezza o perdere i trade-off? |
| **Capstone Routing Canvas** | 17 | Quali artefatti e metodi servono davvero per questo problema e quali sarebbero complessità non giustificata? |
| **Analytics Operating Contract** | 18 | Una capacità ricorrente merita di diventare un servizio e, se sì, chi possiede promessa, failure, change, costo e retirement? |
| **Personal Career Operating Plan** | 19 | Quale responsabilità vogliamo possedere, che cosa possiamo delegare e quale verification reserve deve restare viva? |

## Progressione del libro, non pipeline del caso

L'ordine dei capitoli costruisce progressivamente un vocabolario di rischi:

```text
framing
→ readiness
→ evidence
→ uncertainty
→ lifecycle / time
→ causalità / experimentation
→ prediction
→ semantic data
→ architecture / tooling
→ AI control
→ decisione / comunicazione
→ routing end-to-end
→ operating lifecycle
→ career lifecycle
```

Questo ordine **non** prescrive la sequenza da usare in una singola analisi. Il Capitolo 17 rende esplicito il principio attraverso il Method Budget: ogni artefatto deve poter rispondere alla domanda “quale rischio decisionale resterebbe aperto se lo saltassimo?”. Se non abbiamo una risposta materiale, l'artefatto è candidato a essere eliminato.

Alcuni casi si fermano quindi dopo Data Readiness Review ed EDA Evidence Map; altri richiedono causalità o experimentation; altri ancora diventano prodotti ricorrenti e attivano l'Analytics Operating Contract. Il Personal Career Operating Plan applica la stessa logica alla professione: non accumulare capability per completezza, ma perché sostengono responsabilità che vogliamo poter possedere.

## Routing rapido

| Situazione | Artefatto da considerare per primo |
|---|---|
| problema o decisione ancora ambigui | **Analytical Brief** |
| dato sospetto, incompleto o non comparabile | **Data Readiness Review** |
| pattern osservato ma spiegazioni ancora concorrenti | **EDA Evidence Map** |
| incertezza capace di cambiare scelta | **Uncertainty Brief** |
| comportamento che dipende da coorti/stati/lifecycle | **Lifecycle Diagnostic Map** |
| decisione che dipende dal futuro e dalla loss operativa | **Temporal Decision Brief** |
| claim su cosa accadrebbe intervenendo | **Causal Identification Brief** |
| variation controllabile e decisione sperimentabile | **Experiment Contract** |
| score che deve diventare azione sotto capacità/costo | **Predictive Decision Card** |
| definizione, grain o tempo contestati | **Analytical Data Contract** |
| problema di percorso, recovery o serving del dato | **Data Flow Architecture Map** |
| dubbio su quale ambiente/tool giustificare | **Tooling Decision Record** |
| delega AI che può cambiare dato, codice, claim o azione | **AI Analysis Control Sheet** |
| alternative da confrontare e scegliere | **Decision Record** |
| decisione da comprimere per uno stakeholder | **Decision Communication Pack** |
| caso complesso in cui serve scegliere il metodo minimo sufficiente | **Capstone Routing Canvas** |
| workflow stabile e ricorrente che deve sopravvivere all'autore | **Analytics Operating Contract** |
| crescita professionale da rendere intenzionale | **Personal Career Operating Plan** |

> **La maturità non consiste nell'usare tutti gli artefatti. Consiste nel sapere quale rischio merita di essere reso esplicito prima che diventi una decisione invisibile.**