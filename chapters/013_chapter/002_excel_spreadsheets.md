## 13.1 Spreadsheet: eccellenti per pensare, pericolosi come infrastruttura invisibile

Un foglio di calcolo combina dati, formule, scenari, controlli manuali, pivot, grafici e annotazioni nella stessa superficie. È difficile da battere quando il lavoro richiede interazione immediata con stakeholder e modifica rapida delle ipotesi. La stessa flessibilità, però, permette a un workbook di attraversare senza rumore un confine importante: da strumento per capire un problema a **sistema operativo critico che nessuno ha progettato come sistema**.

La domanda quindi non è “Excel sì o no?”. È: **quale responsabilità stiamo affidando al foglio e per quanto tempo quella responsabilità resta proporzionata?**

Immaginiamo una catena retail che, prima di un incontro con procurement, deve decidere in 90 minuti se modificare il prezzo di **240 SKU**. Esiste già un dataset curato con prezzo, costo, volume, margine, elasticità stimata e prezzo competitor. Il lavoro consiste nel confrontare tre scenari e discuterne le assunzioni con persone business. Un workbook controllato, con celle input separate, formule protette e reconciliation sul margine totale, è una soluzione trasparente e veloce. Costruire una pipeline produttiva prima del meeting non aumenterebbe il rigore: aumenterebbe soltanto il tempo prima dell'apprendimento.

Il limite tecnico non è il criterio principale. Microsoft documenta ancora un massimo di **1.048.576 righe e 16.384 colonne** per worksheet.[^excel-limits] Ma molti processi diventano inadatti al foglio molto prima. Il segnale non è “abbiamo finito le righe”: è che compaiono copie non controllate, formule sovrascritte, copy-paste ricorrenti, macro note a una sola persona, dati sensibili locali, più sorgenti collegate con logica fragile, KPI ufficiali e consumer downstream che trattano il file come un servizio.

### Quando un tool locale diventa infrastruttura

Il caso Public Health England del 2020 è utile proprio perché evita la morale semplicistica “Excel è pericoloso”. PHE comunicò ufficialmente che un problema tecnico nel processo di caricamento aveva escluso **15.841 casi positivi COVID-19** dalle statistiche giornaliere e ne aveva ritardato il trasferimento al contact tracing.[^phe-statement] Il reporting dell'epoca collegò il failure mode all'uso di file/template Excel e ai limiti del formato impiegato.[^guardian-phe-excel]

La lezione è più generale: **un componente può essere perfettamente adeguato in una fase e diventare un single point of failure quando scala, frequenza e impatto aumentano senza una nuova design review**.

Power Query può spostare questo confine perché rende acquisizione e trasformazioni più ripetibili rispetto al copy-paste. Anche Python in Excel, oggi disponibile nell'ecosistema Microsoft 365, amplia enormemente ciò che un workbook può eseguire.[^python-excel] Ma queste capacità non cambiano la domanda fondamentale. Un file con Python può restare un prototipo fragile; un foglio semplice può invece essere ben controllato e perfettamente proporzionato a una decisione una tantum. **Il nome del tool dice meno della responsabilità che gli abbiamo assegnato.**

### Una scala di rischio, non di prestigio

Per rendere visibile il passaggio di responsabilità possiamo usare una piccola ladder:

| Livello | Ruolo del workbook | Obblighi crescenti |
|---|---|---|
| 1 — scratchpad | esplorazione temporanea | nessun consumer downstream |
| 2 — decision workbook | scenario condiviso | input controllati, reconciliation, owner |
| 3 — recurring analytical process | refresh ricorrente | QA, automazione, tracciabilità |
| 4 — hidden production system | altri processi dipendono dal file | design review, recovery, ownership esplicita |

Questa non è una scala in cui il livello 4 sia “migliore”. È una scala che indica quanto il costo di failure e di coordinamento sta crescendo. Un workbook dovrebbe poter restare al livello 2 per anni se il problema resta davvero quello. Il rischio nasce quando siamo al livello 4 e continuiamo a gestirlo mentalmente come se fosse ancora uno scratchpad.

Nel Tooling Decision Record, quindi, uno spreadsheet dovrebbe avere almeno una **exit condition**. Per esempio:

```text
purpose: scenario pricing mensile
source data: dataset certificato
owners: Finance + Pricing
reconciliation: margine totale vs source
exit condition:
- refresh diventa settimanale
- sorgenti > 3
- output alimenta automaticamente altri processi
```

A quel punto non abbiamo decretato che “Excel non va più bene”. Abbiamo dichiarato in anticipo **quale cambio di responsabilità ci obbliga a riesaminare la soluzione**.

> **Un foglio di calcolo è eccellente come superficie di ragionamento. Quando diventa infrastruttura, deve essere gestito come tale oppure sostituito da qualcosa progettato per quella responsabilità.**

[^excel-limits]: Microsoft Support, *Excel specifications and limits*, https://support.microsoft.com/en-us/excel/excel-specifications-and-limits
[^phe-statement]: Public Health England, *PHE statement on delayed reporting of COVID-19 cases*, https://www.gov.uk/government/news/phe-statement-on-delayed-reporting-of-covid-19-cases
[^guardian-phe-excel]: The Guardian, *Covid: how Excel may have caused loss of 16,000 test results in England*, https://www.theguardian.com/politics/2020/oct/05/how-excel-may-have-caused-loss-of-16000-covid-tests-in-england
[^python-excel]: Microsoft Support, *Introduction to Python in Excel*, https://support.microsoft.com/en-us/excel/python/introduction-to-python-in-excel
