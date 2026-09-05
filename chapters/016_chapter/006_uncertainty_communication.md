## 16.5 Comunicare l'incertezza: mostrare ciò che può cambiare la decisione

Una stima centrale è facile da ricordare e quindi facile da trasformare in una promessa. Dire “prevediamo **€12,4 milioni** il prossimo mese” può essere tecnicamente corretto e, nello stesso tempo, occultare proprio l'informazione che il decision maker dovrebbe usare per scegliere.

Il primo passo è distinguere famiglie diverse di incertezza. Quella **statistica** riguarda variabilità della stima; la **data maturity** riguarda freshness, completezza e revisioni attese; la **scenario uncertainty** riguarda futuri o regimi differenti; l'incertezza **semantica o di identificazione** riguarda definizione, comparabilità e forza del claim. Non tutte queste cose possono essere compresse in un confidence interval.

La domanda utile, ereditata dal Capitolo 15, è:

> **L'incertezza attraversa il valore al quale cambieremmo scelta?**

Se un progetto produce beneficio plausibile tra **€4,8M e €6,1M** contro un costo di **€1,2M**, il range è ampio ma non necessariamente decision-critical. Se il beneficio centrale è **€1,2M**, il range è **€0,4M–€1,9M** e il costo è **€1,0M**, l'incertezza attraversa il break-even. In quel caso deve entrare nella headline o accanto alla recommendation.

### Caso simulato/composito — Il forecast venduto come promessa

Un produttore industriale porta al board un forecast Q4 di **€84,2M**. Il modello aveva in realtà un prediction interval all'80% di **€76M–€92M**, ma il range rimane nel notebook tecnico. Il board usa €84,2M come input puntuale per cash planning e acquisti; il trimestre chiude a **€78,5M** e il forecast viene giudicato “sbagliato”.

Il failure non è soltanto statistico. È di traduzione: un oggetto probabilistico è stato comunicato come commitment.

Una comunicazione decisionale rende il range operativo:

> **La stima centrale Q4 è €84,2M; l'80% prediction interval è €76M–€92M. Il cash plan resta robusto sopra €79M, quindi il downside inferiore richiede una contingency sugli acquisti.**

Ora l'incertezza non è una nota metodologica: modifica il piano.

## Provisional è una proprietà del numero

Se la revenue giornaliera è D+1 ma i refund arrivano fino a D+5, “Net revenue ieri: €4,1M” non è un numero finale. La Pack deve poter mostrare `data as-of`, stato `PROVISIONAL / RECONCILED / FINAL`, expected revision e prossimo refresh. Una misura può essere computazionalmente corretta e ancora troppo immatura per l'azione richiesta.

Lo stesso vale per un KPI costruito con feed a latenze differenti: il lettore deve sapere se la decisione sta usando uno stato finalizzato o una fotografia destinata a cambiare.

## Il verbo fa parte del metodo

“La release ha ridotto la conversione” e “il calo è concentrato sugli utenti esposti alla release” non sono due stili equivalenti. La prima frase contiene un claim causale, la seconda un finding localizzato. La grammatica deve preservare il livello di evidenza costruito nei Capitoli 8 e 14.

Per questo una executive rewrite non può rimuovere un caveat causale semplicemente per rendere il messaggio più netto.

## Visualizzare l'incertezza in funzione della scelta

Error bar, confidence band, prediction interval, fan chart, distribuzione e scenario table sono strumenti diversi. Se il compito è confrontare alternative, spesso **range + switching value** è più utile di una distribuzione completa. Se il compito è capire come cresce l'incertezza con l'orizzonte, una fan chart può essere appropriata. Se conta la maturity del dato, uno status testuale può essere più informativo di qualsiasi banda.

La Government Analysis Function raccomanda di comunicare qualità, uncertainty e cambiamenti in modo che il lettore possa capire il loro impatto sull'uso dei dati.[^gaf-uncertainty] Una nota generica come “risultati soggetti a incertezza” è formalmente prudente ma operativamente debole. Molto più utile è dire:

> “Il ranking tra A e B si inverte se l'uplift reale di A è sotto il 2,8%; il range corrente include valori inferiori a questa soglia.”

Questo collega uncertainty e decision boundary.

> **Comunicare bene l'incertezza non significa mostrare ogni dubbio possibile. Significa rendere visibile l'incertezza che limita il claim, modifica il downside o può cambiare l'azione.**

[^gaf-uncertainty]: Government Analysis Function, *Communicating quality, uncertainty and change*, https://analysisfunction.civilservice.gov.uk/policy-store/communicating-quality-uncertainty-and-change/
