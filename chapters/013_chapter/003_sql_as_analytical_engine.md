## 13.2 SQL: scegliere il luogo del calcolo, non soltanto il linguaggio

Il Capitolo 11 ha già trattato grain, join, trasformazioni e semantica SQL. Qui la domanda è diversa: **quando conviene che il lavoro analitico avvenga vicino al dato, dentro il motore che lo gestisce già?**

SQL è spesso la scelta naturale non perché sia “più professionale” di uno spreadsheet o di Python, ma perché filtri, join, aggregazioni e window calculation possono essere eseguiti senza trasferire inutilmente grandi quantità di dati. Se **800 milioni di righe** sono già nel warehouse e il risultato finale è una tabella di 20.000 righe, portare tutto sul laptop per poi ridurlo localmente è spesso una complicazione, non un vantaggio.

Consideriamo un analyst che deve calcolare clienti attivi, ordini per cliente, net revenue e repeat rate su **180 milioni di righe** già disponibili nel warehouse. Possiamo esportare gli eventi e aggregarli in pandas, oppure costruire nel motore dati il dataset alla granularità necessaria e portare fuori soltanto il risultato. Se il lavoro è prevalentemente relazionale, la seconda strada riduce trasferimento, memoria locale, copie sensibili e dipendenza dalla macchina personale.

> **Compute near data è spesso una scelta di semplicità.**

Il principio opposto è altrettanto importante: non tutto ciò che *può* essere espresso in SQL dovrebbe esserlo. Simulazioni iterative, ottimizzazione numerica, statistica specializzata, processing di testo o immagini e diagnostica scientifica possono diventare molto più leggibili e verificabili in un ambiente con librerie dedicate. In questi casi una divisione del lavoro è spesso più naturale:

```text
SQL
→ costruisce la popolazione e il dataset analitico
→ Python/R esegue il metodo specialistico
→ il risultato riusabile torna in una tabella o serving layer
```

Non esiste alcun premio per trasformare un'analisi in una query di 1.500 righe se così diventa più difficile da verificare.

### Pushdown e pull-out sono una decisione sul confine

La domanda operativa è: **quale parte del lavoro beneficia dal restare vicino al dato e quale beneficia da un ambiente analitico più flessibile?** Filtri, join, deduplicazione, aggregazioni e feature tabellari sono spesso buoni candidati al pushdown. Un dataset già ridotto può invece essere portato fuori per simulazione, librerie scientifiche, visual diagnostics o algoritmi non disponibili nel motore.

Questo confine non sostituisce la correttezza semantica. Un team può riscrivere in SQL un processo che passa da **18 minuti a 40 secondi** e scoprire poi che un `INNER JOIN` con la loyalty table ha escluso tutti i clienti non iscritti. La tecnologia ha migliorato il runtime e peggiorato la risposta. Il Capitolo 13 ci chiede se SQL fosse il posto giusto per quel workload; il Capitolo 11 ci obbliga ancora a dimostrare che la trasformazione preserva popolazione, grain e metriche.

### Quando una trasformazione smette di essere personale

Il confine cambia anche con il riuso. Se cinque analyst ricostruiscono ogni settimana la stessa logica `net_orders`, non abbiamo più soltanto un problema di preferenza individuale. Può essere più economico creare una trasformazione condivisa e testata:

```text
source
   ↓
shared SQL transformation
   ↓
certified analytical model
   ↓
consumer diversi
```

La scelta di SQL diventa allora anche una scelta di ownership e di interfaccia condivisa.

Nel Tooling Decision Record conviene rendere espliciti il luogo del dato, la scala in ingresso e in uscita, la quota di lavoro relazionale, la frequenza, il costo di scansione e soprattutto il motivo per cui quella logica deve essere locale o condivisa. Anche qui serve un'uscita: se la metodologia cresce fino a richiedere simulazioni o diagnostiche che rendono la query opaca, una parte del lavoro può meritare un ambiente Python/R.

> **Usa SQL quando il problema beneficia dal calcolo vicino al dato e da trasformazioni tabellari condivise. Non usarlo per dimostrare che tutto può essere scritto in SQL.**
