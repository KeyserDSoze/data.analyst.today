## 9.9 CUPED e variance reduction: ottenere più informazione dallo stesso traffico

Quando il traffico è costoso, raro o lento da accumulare, una domanda naturale è: possiamo rendere il test più sensibile senza aumentare il numero di utenti?

Una delle tecniche più note è CUPED, acronimo di *Controlled-experiment Using Pre-Experiment Data*. L'idea, a livello intuitivo, è semplice: se conosciamo il comportamento dell'utente prima dell'esperimento e quel comportamento è correlato con la metrica durante il test, possiamo usare questa informazione per spiegare parte della variabilità che non dipende dal trattamento.

Non stiamo modificando artificialmente i dati per ottenere significatività. Stiamo costruendo uno stimatore meno rumoroso dell'effetto causale.

### Caso simulato/composito - Due gruppi uguali, ma uno parte con utenti più pesanti

Una piattaforma video testa una nuova home page. La metrica primaria è minuti visti per utente.

La randomizzazione è corretta, ma per puro caso il trattamento contiene leggermente più heavy users. Prima del test:

- controllo: 312 minuti medi settimanali;
- trattamento: 327 minuti.

Durante il test:

- controllo: 319 minuti;
- trattamento: 338 minuti.

Il confronto grezzo suggerisce +19 minuti, circa +6%.

Ma parte della differenza esisteva già prima del test. Utilizzando i minuti visti nel periodo pre-esperimento come covariata, l'effetto aggiustato scende a +5,4 minuti con un errore standard molto più piccolo.

La storia corretta non è più "la nuova home aumenta il watch time del 6%". È: "dopo aver rimosso la componente prevedibile dal comportamento precedente, stimiamo un incremento di circa 5 minuti per utente".

### Un caso pubblico: Microsoft Experimentation Platform

Microsoft descrive CUPED come una tecnica di variance reduction utilizzata nella propria piattaforma di sperimentazione. In una simulazione documentata, un R² di 0,4 corrispondeva a un effective traffic multiplier mediano di circa 1,66: in termini intuitivi, la precisione ottenuta era simile a quella che si sarebbe avuta con circa il 66% di traffico in più usando il confronto semplice.

Microsoft sottolinea però che il beneficio varia molto per superficie di prodotto e metrica: in alcuni contesti il guadagno è quasi nullo, in altri è sostanziale. Questo è importante perché CUPED non è magia: funziona bene quando il dato pre-esperimento predice davvero il comportamento nel periodo sperimentale.

### Quando CUPED aiuta poco

La tecnica può essere poco efficace quando:

- molti utenti sono nuovi e non hanno storico;
- il comportamento pregresso è poco correlato con la metrica futura;
- la randomization unit cambia frequentemente;
- il periodo pre-esperimento non è rappresentativo;
- la metrica è già molto stabile.

### Principio operativo

> **Variance reduction non sostituisce un buon disegno sperimentale. Lo rende più efficiente quando il disegno è già corretto.**

### Fonte

- Microsoft Experimentation Platform, *Deep Dive Into Variance Reduction*, 2022.
