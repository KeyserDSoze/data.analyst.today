## 13.12 Total Cost of Ownership: quanto costa davvero possedere una scelta

Il prezzo di uno strumento è una delle parti più visibili del costo e spesso una delle meno importanti. Per un workflow analitico il **Total Cost of Ownership** comprende costruzione, esecuzione, manutenzione, coordinamento, skill, affidabilità, governance, migrazione e costi di errore o ritardo.

La domanda non è quindi “quanto costa la licenza?”, ma:

> **quanto ci costa ottenere e continuare a ottenere una decisione affidabile attraverso questa soluzione?**

L'AI può abbassare molto il costo di costruzione iniziale. Non necessariamente riduce il resto.

### Il costo che la fattura non mostra

Un team Marketing usa un workflow no-code per integrare sei piattaforme advertising. La licenza costa **€180 al mese**, cioè **€2.160 l'anno**. Se guardassimo solo quella cifra, la soluzione sembrerebbe quasi gratuita.

Poi il team misura **40 ore di manutenzione al mese** a un costo interno medio di €60/ora:

```text
40 × 12 × €60 = €28.800/anno
```

Aggiunge **8 incidenti l'anno** con circa €750 ciascuno di effort/opportunity cost, cioè €6.000, e circa **60 ore di formazione/handover**, altri €3.600. Il TCO osservabile diventa almeno:

```text
€2.160 + €28.800 + €6.000 + €3.600
= €40.560/anno
```

Questo non dimostra che una soluzione custom costerebbe meno. Dimostra che confrontarla con **€2.160** sarebbe un confronto falso.

Il costo totale include anche coordinamento: file da inviare ogni lunedì, riconciliazioni manuali tra Finance e Analytics, dashboard da aggiornare separatamente, approvazioni distribuite tra team. Include il costo delle skill e del bus factor. Include ciò che succede quando il processo fallisce, arriva tardi o produce un output errato.

### Error cost e delay cost cambiano la decisione

Una soluzione può risparmiare **€15.000 l'anno** di effort operativo ma esporre un processo di pricing a un errore plausibile da **€120.000 di margine a rischio**. In quel contesto spendere di più per test, review o governance può essere economicamente razionale.

Esiste anche il problema opposto: aspettare troppo per una soluzione perfetta. Se un checkout bug sta facendo perdere circa **€30.000 al giorno**, produrre in quattro ore un'analisi sufficientemente affidabile può avere molto più valore che attendere due settimane per costruire il data product definitivo prima di iniziare la diagnosi.

Per questo **time-to-first-reliable-evidence** è una dimensione economica reale del tooling.

### Switching cost e reversibilità

Ogni scelta accumula query, macro, dashboard, skill e dipendenze. Migrare più tardi può diventare costoso. La risposta non è comprare subito lo stack più “future proof”, perché potremmo industrializzare un bisogno che non sopravvive. È preferibile rendere esplicita l'exit condition e, quando l'incertezza è alta, privilegiare alternative reversibili.

Il Google Cloud Well-Architected Framework descrive il cost optimization pillar come massimizzazione del **business value** dell'investimento, non come semplice minimizzazione della spesa.[^gcp-waf] È esattamente il criterio che ci serve qui: ottimizzare il tooling significa migliorare il rapporto tra costo totale e valore decisionale.

### Un TCO worksheet leggero è sufficiente

Non serve falsa precisione. Una stima ordinata aiuta già molto:

| Voce | Opzione A | Opzione B | Evidenza/confidenza |
|---|---:|---:|---|
| Build | | | |
| Run annuale | | | |
| Maintenance | | | |
| Coordination | | | |
| Training/skills | | | |
| Reliability / incident | | | |
| Migration/switching | | | |
| Expected error cost | | | |
| Delay / time-to-value | | | |

Dopo la tabella bastano quattro domande: qual è l'incertezza più grande? qual è il failure mode più costoso? qual è l'opzione reversibile più economica? **che cosa deve diventare vero perché la soluzione più costosa sia giustificata?**

Quest'ultima domanda è un antidoto all'overengineering: “scala meglio” non è un beneficio finché non sappiamo quale crescita deve realmente materializzarsi.

> **Non confrontare strumenti per il loro prezzo. Confrontali per il costo totale di costruire, verificare, operare, cambiare e — quando serve — abbandonare la soluzione che produce la decisione.**

[^gcp-waf]: Google Cloud Documentation, *About the Well-Architected Framework*, https://docs.cloud.google.com/docs/get-started/well-architected-framework
[^gcp-finops]: Google Cloud, *What is Cloud FinOps?*, https://cloud.google.com/learn/what-is-finops
