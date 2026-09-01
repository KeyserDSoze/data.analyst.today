## 13.1 Spreadsheet: eccellenti per pensare, pericolosi come infrastruttura invisibile

Un foglio di calcolo è uno degli strumenti più potenti dell'analista perché combina in un'unica superficie:

- dati;
- formule;
- scenari;
- controlli manuali;
- tabelle pivot;
- grafici;
- annotazioni;
- interazione immediata con stakeholder.

Questa stessa flessibilità è anche il suo rischio.

Un workbook può passare gradualmente da:

> strumento per capire un problema

ad

> sistema operativo critico che nessuno ha progettato come sistema.

La domanda non è quindi “Excel sì o no?”.

È:

> **Quale responsabilità stiamo affidando al foglio?**

### Dove un foglio è difficile da battere

È particolarmente efficace quando il lavoro è:

- esplorativo;
- piccolo o moderato per scala;
- fortemente interattivo;
- dominato da scenari e assunzioni;
- facilmente verificabile visivamente;
- destinato a stakeholder che devono modificare input;
- temporaneo o prototipale.

### Caso simulato/composito — pricing in 90 minuti

Una catena retail deve decidere se aumentare il prezzo di 240 SKU prima di un incontro con procurement.

Ha già un dataset curato con:

- prezzo;
- costo;
- volume;
- margine;
- elasticità stimata;
- prezzo competitor.

Il problema è confrontare rapidamente tre scenari e discutere le ipotesi con persone business.

Un foglio controllato, con celle input separate, formule protette e reconciliation sul margine totale, può essere la scelta più trasparente.

Costruire una pipeline produttiva prima del meeting non aumenterebbe il rigore della decisione. Ritarderebbe soltanto l'apprendimento.

### Il problema non è il limite di righe: è non sapere di avere superato il contesto ideale

Ogni strumento ha limiti tecnici e operativi.

Microsoft documenta per un worksheet Excel un massimo di **1.048.576 righe e 16.384 colonne**.[^excel-limits]

Ma un processo può diventare inadeguato molto prima di arrivare al limite tecnico.

Segnali più importanti sono:

- copie del file non controllate;
- formule sovrascritte manualmente;
- passaggi copy-paste ricorrenti;
- macro conosciute da una sola persona;
- dati sensibili locali;
- più fonti collegate con logica fragile;
- impossibilità di rieseguire il processo da zero;
- KPI ufficiali che dipendono dal workbook;
- utenti downstream che trattano l'output come servizio.

### Caso reale documentato — Public Health England, 2020

Nell'ottobre 2020 Public Health England comunicò che un problema tecnico nel processo di caricamento aveva escluso **15.841 casi positivi COVID-19** dalle statistiche giornaliere e ritardato il loro trasferimento al contact tracing.[^phe-statement]

La dichiarazione ufficiale parla di un problema tecnico nel data-load process. La stampa tecnica e generalista dell'epoca ricondusse il failure mode all'uso di template Excel e ai limiti del formato impiegato.[^guardian-phe-excel]

Il punto didattico non è “Excel è pericoloso”.

È l'opposto:

> **un componente adatto a un certo volume e a un certo rischio può diventare un single point of failure quando il processo cresce senza una nuova design review.**

Il problema professionale è riconoscere il momento in cui una soluzione locale è diventata infrastruttura.

### Power Query sposta il confine, non lo elimina

Power Query rende trasformazioni e connessioni più ripetibili rispetto al copy-paste.

Può essere ottimo per:

- acquisire file ricorrenti;
- applicare trasformazioni leggibili;
- ridurre passaggi manuali;
- aggiornare scenari e reporting leggero.

Ma se la stessa logica deve alimentare 30 report e viene considerata una definizione aziendale, il problema non è più soltanto aggiornare bene il workbook.

Probabilmente quella logica merita un layer condiviso.

### Python in Excel: le categorie si stanno fondendo

Microsoft supporta oggi l'esecuzione di Python in Excel e l'uso di librerie analitiche nell'ambiente del workbook.[^python-excel]

Questa convergenza è utile perché mostra una cosa importante:

**il nome del tool dice sempre meno sul livello di maturità del processo.**

Un workbook può usare Python e restare un prototipo fragile.

Un semplice foglio può invece essere ben controllato, documentato e proporzionato a una decisione una tantum.

### Spreadsheet risk ladder

Possiamo pensare a quattro livelli.

**Livello 1 — scratchpad**  
Calcoli temporanei, esplorazione, nessun consumer downstream.

**Livello 2 — decision workbook**  
Scenario o analisi condivisa, input controllati, reconciliation e owner chiaro.

**Livello 3 — recurring analytical process**  
Refresh ricorrente, più fonti, output distribuito. Servono automazione, QA e maggiore tracciabilità.

**Livello 4 — hidden production system**  
Altri processi dipendono dal file, impatto economico elevato, failure operativi. A questo punto serve una design review esplicita.

### Campo del Tooling Decision Record

Se scegliamo uno spreadsheet, il TDR dovrebbe dichiarare:

```text
purpose:
source data:
expected max scale:
manual steps:
critical formulas / controls:
owners:
consumers:
versioning / storage:
sensitive data policy:
reconciliation:
exit condition:
```

Esempio di exit condition:

> Migrare la trasformazione in SQL quando il report diventa settimanale, supera tre sorgenti o viene utilizzato come input automatico da altri processi.

### Regola operativa

> **Un foglio di calcolo è eccellente come superficie di ragionamento. Quando diventa un'infrastruttura, deve essere gestito come tale oppure sostituito da qualcosa progettato per quella responsabilità.**

[^excel-limits]: Microsoft Support, *Excel specifications and limits*, https://support.microsoft.com/en-us/excel/excel-specifications-and-limits
[^phe-statement]: Public Health England, *PHE statement on delayed reporting of COVID-19 cases*, https://www.gov.uk/government/news/phe-statement-on-delayed-reporting-of-covid-19-cases
[^guardian-phe-excel]: The Guardian, *Covid: how Excel may have caused loss of 16,000 test results in England*, https://www.theguardian.com/politics/2020/oct/05/how-excel-may-have-caused-loss-of-16000-covid-tests-in-england
[^python-excel]: Microsoft Support, *Introduction to Python in Excel*, https://support.microsoft.com/en-us/excel/python/introduction-to-python-in-excel
