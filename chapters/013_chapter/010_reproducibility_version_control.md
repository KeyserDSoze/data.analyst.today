## 13.9 Reproducibility e version control: il tool giusto deve lasciare una traccia ricostruibile

Una scelta di tooling non riguarda soltanto ciò che possiamo fare oggi. Riguarda anche ciò che un'altra persona potrà capire, rieseguire e verificare domani.

> **Se un risultato importante non può essere ricostruito, una parte della conoscenza è rimasta nella memoria delle persone invece di diventare un asset dell'organizzazione.**

La riproducibilità non è binaria. Un calcolo scratch può non promettere nulla; un'analisi una tantum può limitarsi a documentare input e assunzioni; un processo ricorrente deve essere almeno rieseguibile; un prodotto critico può richiedere versionamento, test, automation e audit trail.

Possiamo rappresentare questa progressione così:

| Livello | Promessa |
|---|---|
| R0 — scratch | nessuna promessa di riproduzione |
| R1 — documented | input, passaggi e assunzioni comprensibili |
| R2 — rerunnable | riesecuzione con gli stessi input senza ricostruzione arbitraria |
| R3 — versioned | logica, configurazione e dipendenze tracciate |
| R4 — automated and tested | esecuzione automatizzata, controllata e revisionabile |

Il livello giusto dipende dalla responsabilità del lavoro. Una statistica pubblicata mensilmente o un processo che influenza milioni di euro non dovrebbe dipendere da una sequenza di passaggi che esiste solo nella memoria di chi l'ha costruita.

Consideriamo Finance che produce venerdì il margine per categoria. Lunedì nessuno ricorda quali righe erano state escluse manualmente, quale FX table era stata usata, quali formule erano diventate valori o quale versione del product mapping era corretta. Il problema non è l'estensione `.xlsx`: è **lo stato non registrato**.

### RAP: la riproducibilità cresce con frequenza e pressione

La Government Analysis Function del Regno Unito promuove le **Reproducible Analytical Pipelines (RAP)** come processi analitici automatizzati che incorporano pratiche di software engineering per aumentare riproducibilità, auditabilità, efficienza e qualità.[^rap-overview] Tra i requisiti minimi compaiono la riduzione dei passaggi manuali, peer review e un audit trail tramite version control; la strategia collega queste pratiche anche a business continuity e knowledge management.[^rap-strategy]

Il punto per il nostro capitolo è importante: **riproducibilità non è decorazione da sviluppatori. Diventa più preziosa proprio quando un processo aumenta in frequenza, pressione o importanza**.

Il codice da solo non basta. Uno script con path personali, package non versionati, query non salvate e step manuali nascosti può essere meno riproducibile di un workflow visuale ben controllato. Allo stesso modo, Power Query o un processo low-code possono essere abbastanza riproducibili se input, trasformazioni, change history e controlli sono dichiarati.

Codice e riproducibilità sono correlati, non sinonimi.

### Version control come memoria della logica

La Government Analysis Function raccomanda esplicitamente Git per registrare la versione del codice usata in una specifica esecuzione, osservando che nomi come `v1` e `v2` non offrono la stessa garanzia.[^rap-sophisticated] Questo ci permette di rispondere a domande operative: quando è cambiata la metrica? quale commit ha modificato il filtro? quale logica ha prodotto il report di marzo? possiamo tornare alla versione precedente?

Per un processo critico non serve mettere ogni dato grezzo in Git. Serve poter identificare **quali dati, quale logica, quale configurazione e quale ambiente hanno prodotto l'output**.

### Ogni tool paga una reproducibility tax

La riproducibilità ha un costo diverso per ogni superficie:

| Ambiente | Tax tipica |
|---|---|
| Spreadsheet | input, formule, versioni e modifiche manuali |
| SQL | query/model versionati, sorgenti e temporalità |
| Notebook | environment, clean run, input/output dichiarati |
| Python/R | dipendenze, config, package/code version |
| BI | semantic definitions e source artifacts |
| Low-code | change history, export/config, test e audit trail |

Se rendere un processo sufficientemente riproducibile dentro il tool corrente diventa sempre più difficile, questo è un segnale che il contesto è cambiato. Il Tooling Decision Record dovrebbe quindi includere il livello R0–R4 richiesto e il costo necessario per raggiungerlo.

> **Scegli un tool non soltanto perché permette di produrre il risultato, ma anche perché permette di ricostruirlo con un costo proporzionato alla sua importanza.**

[^rap-overview]: UK Government Analysis Function, *Reproducible Analytical Pipelines (RAP)*, https://analysisfunction.civilservice.gov.uk/reproducible-analytical-pipelines/
[^rap-strategy]: UK Government Analysis Function, *Reproducible Analytical Pipelines (RAP) strategy*, https://analysisfunction.civilservice.gov.uk/policy-store/reproducible-analytical-pipelines-strategy/
[^rap-sophisticated]: UK Government Analysis Function, *Why take a more sophisticated approach to building your pipeline*, https://analysisfunction.civilservice.gov.uk/support/reproducible-analytical-pipelines/why-take-a-more-sophisticated-approach-to-building-your-pipeline/
