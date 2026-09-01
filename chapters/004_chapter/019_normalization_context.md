## 4.18 Rendere confrontabili i confronti: esposizione, mix e base di riferimento

Aver scelto un buon denominatore non garantisce ancora che due gruppi siano confrontabili.

Due team possono avere lo stesso win rate ma ricevere opportunità molto diverse. Due ospedali possono avere lo stesso tasso di complicanze ma trattare pazienti con profili di rischio differenti. Due negozi possono avere ricavi per metro quadrato simili ma operare in mercati con stagionalità e prezzi completamente diversi.

Dopo la domanda:

> **Qual è il denominatore corretto?**

arriva quindi una seconda domanda:

> **Le basi che sto confrontando rappresentano davvero condizioni abbastanza simili da rendere il confronto utile?**

### Caso simulato/composito — Qual è il team commerciale migliore?

La società B2B immaginaria **VectorCore Systems** confronta tre team.

| Team | Contratti chiusi |
|---|---:|
| Enterprise | 42 |
| Mid-Market | 67 |
| SMB | 118 |

Se il criterio è il volume, SMB è primo.

Aggiungiamo le opportunità qualificate:

| Team | Contratti | Opportunità | Win rate |
|---|---:|---:|---:|
| Enterprise | 42 | 105 | 40,0% |
| Mid-Market | 67 | 215 | 31,2% |
| SMB | 118 | 590 | 20,0% |

Ora Enterprise sembra il più efficace.

Aggiungiamo il valore medio dei contratti:

| Team | Contratti | ACV medio | Nuovo ARR |
|---|---:|---:|---:|
| Enterprise | 42 | 148.000 € | 6,22 M€ |
| Mid-Market | 67 | 46.000 € | 3,08 M€ |
| SMB | 118 | 9.500 € | 1,12 M€ |

La classifica cambia ancora.

Ma nemmeno il win rate rende automaticamente i team confrontabili. Le opportunità enterprise possono essere molto più selezionate prima di entrare nel pipeline; SMB può ricevere un volume enorme di lead meno qualificati; i cicli di vendita e i territori possono essere diversi.

Il problema non è trovare **la metrica che incorona un vincitore**. È capire quale dimensione di performance corrisponde alla decisione.

### Volume, efficienza e valore non sono sinonimi

Tre domande producono tre metriche diverse:

- **Quanto produciamo?** → contratti, ordini, revenue, casi risolti;
- **Quanto convertiamo l'opportunità disponibile?** → win rate, conversion rate, output per ora;
- **Quanto valore generiamo?** → ARR, margine, contribution margin, valore atteso.

Una dashboard che usa una sola metrica per classificare processi complessi rischia di confondere questi livelli.

### Il mix può creare performance apparente

Supponiamo che due call center abbiano entrambi un first-contact resolution rate dell'82%.

Il primo gestisce soprattutto richieste semplici di password reset. Il secondo gestisce principalmente problemi di fatturazione e integrazioni tecniche.

Il tasso è identico. Il compito no.

Prima di concludere che i team abbiano la stessa efficacia, potremmo dover stratificare per tipo di ticket o costruire un confronto su popolazioni più omogenee.

È lo stesso principio incontrato con Simpson's paradox: **la composizione della popolazione può generare, attenuare o invertire un confronto aggregato**.

### La base di riferimento conta anche per lo z-score

Nella sezione 4.14 abbiamo standardizzato osservazioni rispetto a media e deviazione standard. Anche lì il risultato dipende dalla popolazione scelta.

Uno store aeroportuale confrontato con tutta la rete può sembrare estremo. Confrontato soltanto con altri store aeroportuali può risultare normale.

La standardizzazione matematica non sostituisce quindi la scelta analitica della **reference population**.

### Mostrare sia intensità sia volume

Un tasso alto su una base piccola e un tasso moderato su una base enorme possono suggerire priorità differenti.

Per esempio:

- segmento A: 20% di reclami su 200 ordini → 40 reclami;
- segmento B: 6% su 50.000 ordini → 3.000 reclami.

A ha il rischio relativo peggiore. B genera quasi tutto l'impatto assoluto.

Se dobbiamo capire dove il processo è più fragile, guardiamo A. Se dobbiamo ridurre rapidamente il numero totale di reclami, B può avere più leva.

Una buona EDA tiene insieme entrambe le prospettive.

### Una matrice mentale per i confronti

Prima di dichiarare che A è “migliore” o “peggiore” di B, chiediti:

| Dimensione | Domanda |
|---|---|
| Volume | Quanti eventi osserviamo? |
| Esposizione | Su quante opportunità o unità a rischio? |
| Mix | Le popolazioni hanno composizione simile? |
| Tempo | Il periodo e la stagionalità sono comparabili? |
| Valore | Gli eventi hanno lo stesso peso economico? |
| Base | La popolazione di riferimento è appropriata? |

> **Normalizzare non significa rendere magicamente uguali gruppi diversi. Significa rendere esplicito rispetto a che cosa li stiamo confrontando.**
