## 13.9 Reproducibility e version control: il tool giusto deve lasciare una traccia ricostruibile

La scelta di uno strumento non riguarda soltanto ciò che possiamo fare oggi.

Riguarda anche ciò che un'altra persona potrà capire e rifare domani.

> **Se un risultato importante non può essere ricostruito, il processo contiene conoscenza che non è stata trasformata in un asset dell'organizzazione.**

### Riproducibilità come requisito graduato

Non tutti i lavori richiedono lo stesso livello.

Possiamo distinguere:

**R0 — scratch**  
Calcolo temporaneo. Nessuna promessa di riproduzione.

**R1 — documented**  
Input, passaggi e assunzioni principali sono comprensibili.

**R2 — rerunnable**  
Il processo può essere rieseguito con gli stessi input senza ricostruzione manuale arbitraria.

**R3 — versioned**  
Codice/logica, configurazione e dipendenze sono tracciati.

**R4 — automated and tested**  
L'esecuzione è automatizzata, controllata e revisionabile.

Un'analisi una tantum può fermarsi a R1 o R2.

Una statistica pubblicata mensilmente o un processo che influenza milioni di euro probabilmente richiede molto di più.

### Caso simulato/composito — il margine che cambia tra venerdì e lunedì

Finance produce venerdì il margine per categoria.

Lunedì deve aggiornare il file e nessuno ricorda:

- quali righe erano state escluse manualmente;
- quale FX table era stata usata;
- quali formule erano state convertite in valori;
- se i resi erano stati riallocati al mese originale;
- quale versione del product mapping era corretta.

Il problema non è il formato `.xlsx`.

Il processo dipende da **stato e memoria umana non registrati**.

### Reproducible Analytical Pipelines: un caso pubblico di maturità analitica

La Government Analysis Function del Regno Unito promuove le **Reproducible Analytical Pipelines (RAP)** come processi analitici automatizzati che incorporano pratiche di software engineering per aumentare riproducibilità, auditabilità, efficienza e qualità.[^rap-overview]

Tra i requisiti minimi indicati ci sono la riduzione dei passaggi manuali e un audit trail tramite version control; la strategia RAP sottolinea anche riuso, quality assurance e business continuity.[^rap-strategy]

La strategia cita l'**ONS COVID-19 Infection Survey** come esempio di analisi nazionale realizzata sotto forte pressione in cui pratiche RAP hanno aiutato il team a migliorare efficienza e qualità.[^rap-strategy]

Questo è un punto importante per il nostro capitolo:

> riproducibilità non è “abbellimento da sviluppatori”. Diventa più preziosa proprio quando frequenza, pressione e importanza aumentano.

### Codice aiuta, ma non basta

Uno script può essere non riproducibile se contiene:

```text
/home/mario/Desktop/final_data.csv
```

oppure se dipende da:

- package non versionati;
- credenziali personali;
- query non salvate;
- step manuali non documentati;
- dati modificati in-place;
- notebook eseguiti fuori ordine.

Allo stesso modo un workflow visuale o Power Query può essere sufficientemente riproducibile se:

- input sono noti;
- trasformazioni sono salvate;
- modifiche sono tracciabili;
- il processo può essere rieseguito;
- esistono controlli sull'output.

Quindi **codice e riproducibilità sono correlati, non sinonimi**.

### Version control come memoria della logica

La Government Analysis Function raccomanda esplicitamente Git per bloccare e registrare la versione del codice usata in una specifica esecuzione, osservando che file chiamati `v1`, `v2` non offrono la stessa garanzia.[^rap-sophisticated]

Per l'analytics, versionare significa poter rispondere:

- quando è cambiata la metrica?
- quale commit ha modificato il filtro?
- quale codice ha prodotto il report di marzo?
- perché è cambiata la logica?
- possiamo tornare alla versione precedente?

Un messaggio come:

```text
Exclude full refunds from net revenue
```

ha molto più valore di:

```text
final fix 2
```

### Cosa deve essere ricostruibile

A seconda del rischio, possiamo versionare o identificare:

- SQL;
- Python/R;
- notebook;
- definizioni metriche;
- configurazioni;
- test;
- environment/dependencies;
- schema atteso;
- source snapshot o data version/reference;
- modello e parametri;
- output pubblicato.

Non significa mettere ogni raw dataset in Git.

Significa poter identificare **quali dati** sono stati usati e **quale trasformazione** li ha convertiti nell'output.

### Reproducibility tax

Ogni scelta di tool ha un costo per renderla riproducibile.

| Ambiente | Tax tipica |
|---|---|
| Spreadsheet | tracciare modifiche manuali, input, formule e versioni |
| SQL | versionare query/model, definire sorgenti e temporalità |
| Notebook | environment + clean run + input/output dichiarati |
| Python/R | dipendenze, config, package/code version |
| BI | versionare semantic definitions e source artifacts quando possibile |
| Low-code | change history, export/config, test e audit trail |

Se quel costo diventa molto alto, può essere un segnale che il tool corrente ha superato il suo contesto ideale.

### Campo del Tooling Decision Record

```text
required reproducibility level: R0-R4
input identification:
logic versioning:
environment/dependencies:
manual steps:
QA / review:
execution record:
output version:
business continuity risk:
reproducibility owner:
exit condition:
```

### Regola operativa

> **Scegli un tool non soltanto perché permette di produrre il risultato, ma anche perché permette di ricostruirlo con un costo proporzionato alla sua importanza.**

[^rap-overview]: UK Government Analysis Function, *Reproducible Analytical Pipelines (RAP)*, https://analysisfunction.civilservice.gov.uk/reproducible-analytical-pipelines/
[^rap-strategy]: UK Government Analysis Function, *Reproducible Analytical Pipelines (RAP) strategy*, https://analysisfunction.civilservice.gov.uk/policy-store/reproducible-analytical-pipelines-strategy/
[^rap-sophisticated]: UK Government Analysis Function, *Why take a more sophisticated approach to building your pipeline*, https://analysisfunction.civilservice.gov.uk/support/reproducible-analytical-pipelines/why-take-a-more-sophisticated-approach-to-building-your-pipeline/
