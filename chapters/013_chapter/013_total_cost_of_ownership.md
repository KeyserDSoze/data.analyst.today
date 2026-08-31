## 13.12 Total Cost of Ownership: il prezzo dello strumento è solo una parte del costo

Quando si confrontano strumenti, è facile guardare soltanto alla licenza o al costo cloud.

Ma il **Total Cost of Ownership (TCO)** comprende molto di più:

- costo di licenza o consumo;
- tempo di sviluppo;
- manutenzione;
- supporto;
- formazione;
- gestione degli accessi;
- infrastruttura;
- osservabilità;
- costi di migrazione;
- dipendenza da competenze rare;
- costo degli errori;
- costo dell'attesa.

Un tool apparentemente economico può diventare molto costoso se richiede manutenzione continua.

### Caso realistico: la pipeline da €180 al mese che costa €70.000 l'anno

Un team marketing costruisce un processo no-code per importare dati advertising da sei piattaforme.

Costo licenza: circa €180 al mese.

Sembra estremamente conveniente.

Dopo un anno però:

- il workflow ha 93 step;
- si rompe mediamente quattro volte al mese;
- due analyst dedicano circa 20 ore mensili al troubleshooting;
- il processo non ha test automatici;
- solo una persona conosce la logica completa.

Se il costo orario interno effettivo è €60, la sola manutenzione vale circa:

```text
20 ore × 12 mesi × 2 persone × €60 = €28.800/anno
```

Aggiungendo ritardi, errori nei report e rischio operativo, il costo reale è enormemente superiore alla licenza.

### Il contrario è altrettanto possibile

Un team può spendere molto per una piattaforma enterprise che automatizza problemi che non esistono.

Esempio:

una società produce un report trimestrale da 40.000 righe.

Una soluzione proposta include cluster distribuito, orchestratore, catalogo dati e streaming ingestion.

Il problema reale potrebbe essere risolto in modo affidabile con:

- una query SQL;
- una trasformazione schedulata;
- un semantic model;
- una dashboard.

La piattaforma più potente non è necessariamente quella con il TCO migliore.

### Caso pubblico: cost optimization non significa solo ridurre la fattura

Il Google Cloud Well-Architected Framework sottolinea che la valutazione dei costi dovrebbe considerare il **business value** e il TCO, non soltanto il prezzo di provisioning. La documentazione osserva, per esempio, che una VM può sembrare economica ma richiedere overhead per manutenzione, patching e scaling; un servizio gestito può avere un prezzo unitario diverso ma ridurre il costo operativo complessivo.

Fonte: Google Cloud, *Align cloud spending with business value* e *Optimize resource usage*.

- https://docs.cloud.google.com/architecture/framework/cost-optimization/align-cloud-spending-business-value
- https://docs.cloud.google.com/architecture/framework/cost-optimization/optimize-resource-usage

Questo principio si trasferisce direttamente al lavoro analitico.

### Un modello semplice di TCO analitico

Possiamo pensare:

```text
TCO = tecnologia
    + persone
    + manutenzione
    + coordinamento
    + rischio
    + costo del cambiamento
```

Non è una formula contabile precisa. È una checklist mentale.

### Caso realistico: SQL vs Python vs BI

Un'azienda deve calcolare settimanalmente il churn per 3 milioni di clienti.

Tre opzioni:

1. estrarre tutto in Python sul laptop dell'analyst;
2. calcolarlo nel warehouse con SQL;
3. ricostruire la logica direttamente nel BI tool.

Tutte e tre possono produrre lo stesso numero.

Ma il TCO cambia:

- Python locale: flessibile, ma trasferimento dati e dipendenza dalla macchina;
- SQL warehouse: logica centralizzata e scalabile;
- BI: rapido, ma rischio di duplicare logica e aumentare costi di refresh o manutenzione semantica.

Il costo migliore dipende da riuso, scala, ownership e frequenza.

### Costo dell'attesa

C'è infine un costo spesso ignorato: **time-to-insight**.

Se un'azienda perde €30.000 al giorno per un problema di conversione, spendere due settimane per costruire l'architettura perfetta prima di fare un'analisi preliminare può essere economicamente irrazionale.

Il tool più economico tecnicamente può essere il più costoso per il business se rallenta la decisione.

### Regola operativa

> **Non confrontare strumenti per il loro prezzo. Confrontali per il costo totale necessario a produrre e mantenere una decisione affidabile.**
