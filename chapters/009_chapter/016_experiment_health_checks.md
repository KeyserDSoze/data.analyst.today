## 9.15 Experiment Health Gate: certificare il confronto prima di stimare l'effetto

A questo punto abbiamo già incontrato quasi tutti i modi in cui un esperimento può smettere di rappresentare il design: identity instabile, randomization unit sbagliata, SRM, exposure asimmetrica, logging differenziale, contamination, filtri post-treatment, metriche cambiate o incidenti operativi.

Serve quindi un passaggio esplicito tra raccolta dati e interpretazione causale. Lo chiameremo **Experiment Health Gate**.

La sua domanda non è “B sta vincendo?”, ma:

> **questo run ha prodotto un confronto abbastanza affidabile da meritare una lettura dell'effetto?**

Finché la risposta non è sì, effect size, confidence interval e p-value sono secondari.

### Caso simulato/composito — RideFlow

RideFlow testa un algoritmo per suggerire punti di pickup più efficienti. La dashboard mostra tempo medio di attesa -6,4%, cancellazioni -2,1% e un intervallo interamente favorevole sulla primary.

Il gate trova però:

| Controllo | Esito |
|---|---|
| allocazione attesa 50/50 | fallisce: 53,8/46,2 |
| assignment stabile | ok |
| exposure per versione app | fallisce su una versione Android |
| logging dei pickup | ok |
| distribuzione OS pre-treatment | sbilanciata tra gruppi osservati |
| concurrent experiments | nessun conflitto noto |

La versione Android che riceve meno spesso il trattamento ha storicamente tempi di attesa peggiori. La composizione osservata di B è quindi diversa proprio su una caratteristica legata all'outcome. Il risultato non viene classificato “positivo” o “negativo”, ma:

**INVALIDO PER DECISIONE — correggere exposure/telemetria e ripetere.**

È una conclusione più forte di un intervallo stretto costruito su un confronto compromesso.

### Le famiglie del gate

Il gate deve coprire l'intera catena, non soltanto l'SRM. Per renderlo scansionabile conviene mantenerlo come artefatto operativo:

| Area | Domanda |
|---|---|
| Assignment integrity | l'unità prevista è stata assegnata una volta, con rapporto coerente e senza auto-selezione? |
| Identity stability | la stessa unità resta nella stessa variante attraverso sessioni, device e periodi rilevanti? |
| Exposure integrity | assignment e trattamento ricevuto sono compatibili con l'estimand? |
| Telemetry completeness | eventi, filtri e join sono simmetrici tra arm? |
| Population integrity | eligibility e filtri rappresentano ancora la popolazione predefinita? |
| Metric integrity | numeratore, denominatore, timestamp, join e maturity sono quelli congelati? |
| Interference / concurrent changes | altri test, campagne o shared resources modificano il confronto? |
| Operational incidents | outage, migrazioni o capacity constraints rendono il run non rappresentativo? |

Il valore della tabella non è trasformare la review in una checklist cieca. È impedire che un risultato business molto favorevole faccia dimenticare le condizioni che lo rendono interpretabile.

### Pre-treatment balance: usare il pattern per diagnosticare il processo

Con randomizzazione corretta qualche squilibrio pre-treatment emergerà per caso, soprattutto se guardiamo molte covariate. Per questo “una covariata ha `p < 0,05`” non deve diventare automaticamente prova di test rotto.

Sono più informativi differenze materialmente grandi, pattern sistematici, squilibri concentrati su platform/version o deviazioni coerenti con un problema già osservato in assignment o exposure. Il balance check deve aiutare a capire **come sono stati prodotti i gruppi osservati**, non creare un nuovo torneo di p-value.

### Tre verdetti, non una spunta generica

**VALIDO** significa che non emergono problemi materialmente rilevanti e l'effetto può essere interpretato secondo il piano.

**VALIDO CON CAVEAT** significa che esiste una deviazione compresa e circoscritta che non distrugge il confronto ma restringe lo scope. Una versione legacy pari all'1,5% della popolazione, esclusa simmetricamente dall'estimand dichiarato, può essere un esempio.

**INVALIDO PER DECISIONE** significa che esiste un problema capace di alterare gruppi, outcome o telemetria in modo selettivo e non siamo in grado di quantificarne credibilmente l'impatto. In quel caso non si “aggiusta finché torna il risultato”: si ripara e, quando necessario, si ripete.

Microsoft ExP ha documentato ripetutamente che la trustworthiness dipende dall'intera catena assignment → execution → telemetry → metric computation e che modifiche infrastrutturali apparentemente locali possono produrre regressioni visibili soltanto quando si osservano metriche di prodotto più ampie.[^ms-infra]

L'ordine operativo resta quindi:

**Experiment Contract → run → Experiment Health Gate → stima dell'effetto → decisione → rollout.**

> **Un esperimento non è affidabile perché produce un intervallo stretto. È affidabile quando possiamo spiegare perché treatment e control rappresentano ancora il confronto che avevamo deciso di costruire.**

[^ms-infra]: Microsoft Research, *A/B Testing Infrastructure Changes at Microsoft ExP*: https://www.microsoft.com/en-us/research/articles/a-b-testing-infrastructure-changes-at-microsoft-exp/
