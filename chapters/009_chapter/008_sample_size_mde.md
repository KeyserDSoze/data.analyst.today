## 9.7 MDE e feasibility: progettare il test attorno all'effetto che cambia la decisione

Il Capitolo 5 ha già spiegato la relazione tra sample size, effect size, alpha e power. Nell'experimentation il punto operativo è più concreto: **il sistema ha abbastanza traffico per distinguere un effetto che sarebbe abbastanza importante da cambiare la decisione?**

Questa domanda evita un errore comune: progettare il test attorno alla durata desiderata e poi chiamare “MDE” il numero che la rende possibile.

### QuickPay: dal +2% relativo alla soglia economica

Supponiamo:

- conversion baseline: 3,80%;
- utenti eleggibili/mese: 4,2 milioni;
- contribution margin per ordine: 17,40 €.

Il PM propone un MDE relativo di `+2%`, circa `+0,076 pp` assoluti. Su 4,2 milioni di utenti:

```text
4.200.000 × 0,00076 ≈ 3.192 ordini incrementali/mese
3.192 × 17,40 € ≈ 55.500 €/mese
```

Il numero sembra interessante finché non entra nella decisione completa. Il redesign richiede manutenzione su quattro codebase, modifica due integration path di pagamento, aumenta fraud review e ha costo opportunità rispetto ad altri progetti. Se `+0,076 pp` non giustifica questi costi, non è la soglia business che il test deve riuscire a distinguere.

Il team può allora definire: “Ship solo se il beneficio plausibile è almeno +0,15 pp senza violare i guardrail.” A quel punto materialità, MDE, traffic plan e decision matrix parlano la stessa lingua.

### Minimum effect of interest, MDE e observed effect

Sono tre oggetti diversi. Il **minimum effect of interest (MEI)** è il più piccolo effetto che cambierebbe la decisione business. L'**MDE del design** descrive la sensibilità del test sotto le proprietà statistiche scelte. L'**observed effect** è ciò che i dati stimano.

Un effetto più piccolo dell'MDE può esistere. Il test può semplicemente non essere abbastanza informativo per distinguerlo con la precisione desiderata. Per questo un risultato inconcludente non è sinonimo di “effetto zero”.

Idealmente il design dovrebbe essere sensibile nella zona del MEI. Se non può esserlo, il problema va dichiarato **prima** del lancio.

### Feasibility: quando il traffico non basta

Se servono 900.000 utenti per variante ma soltanto 80.000 utenti al mese sono realmente eleggibili, la durata teorica supera undici mesi per arm, senza contare maturity e stagionalità. “Facciamolo comunque e vediamo” non migliora l'informazione.

Possiamo cambiare domanda, scegliere un outcome più sensibile ma ancora decision-relevant, allargare la popolazione solo se semanticamente corretto, usare variance reduction, testare un trattamento più forte, scegliere un design diverso o accettare che l'esperimento non sia praticabile.

La non-feasibility è un risultato di design, non una sconfitta dell'analista.

### Primary facile, guardrail raro

Un test può avere enorme power sulla conversione e pochissima informazione su fraud, severe crash, churn D90 o chargeback. Se uno di questi outcome può bloccare lo ship, dobbiamo dichiarare quanto bene il test potrà **escludere un danno materialmente importante**. Dimensionare soltanto la primary crea una decision matrix che il test non è capace di completare.

Lo stesso vale nei cluster experiments. Se randomizziamo 80 negozi, milioni di transazioni non trasformano automaticamente 80 cluster in milioni di unità indipendenti. La feasibility deve usare la randomization unit reale e la dipendenza introdotta dal design.

### Exposure rate e durata

Un milione di utenti randomizzati di cui soltanto il 35% raggiunge la feature può produrre un intent-to-treat molto diluito. Se è quello l'estimand decisionale, il traffic plan deve incorporarlo invece di dimensionarsi sui soli exposed users.

E anche quando il sample requirement arriva presto, la fine del test resta governata dal massimo tra informazione statistica, minimum calendar duration e outcome maturity:

```text
experiment end = max(
    sample requirement,
    minimum calendar duration,
    outcome maturity requirement
)
```

È un principio operativo, non una formula universale.

### Feasibility card

```text
Baseline metric:
Minimum effect of business interest:
MDE planned:
Alpha / desired power:
Randomization unit:
Eligible units/day:
Expected exposure rate:
Variance / baseline rate:
Cluster design effect if any:
Rare guardrail feasibility:
Expected time to sample requirement:
Minimum calendar duration:
Outcome maturity:
Is the experiment decision-useful at this sensitivity?
```

> **La domanda non è quante settimane servono per ottenere un p-value. È se il test può distinguere gli effetti che separano davvero le decisioni disponibili.**
