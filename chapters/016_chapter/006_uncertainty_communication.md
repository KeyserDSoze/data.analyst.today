## 16.5 Comunicare l'incertezza: mostrare ciò che può cambiare la decisione

Una stima centrale è facile da ricordare.

> “Prevediamo €12,4 milioni il prossimo mese.”

È anche facile da usare come se fosse una promessa.

Una comunicazione professionale deve distinguere almeno quattro famiglie di incertezza:

1. **statistica** — variabilità della stima;
2. **data maturity** — freshness, completezza, dati ancora provvisori;
3. **scenario / structural** — futuro, regime change, assunzioni economiche;
4. **identification / semantic** — definizione, causalità, comparabilità.

Non tutte possono essere compresse in un confidence interval.

## Il criterio decisionale: attraversa lo switching value?

Dal Capitolo 15 ereditiamo una domanda molto più utile di:

> “Quanto è largo l'intervallo?”

Chiediamo:

> **“L'incertezza attraversa il valore al quale cambieremmo scelta?”**

### Caso A — Incertezza non decision-critical

- beneficio progetto: €4,8M–€6,1M;
- costo: €1,2M;
- nessun downside strategico rilevante.

L'intervallo è ampio, ma l'opzione resta preferibile in tutto il range plausibile.

### Caso B — Incertezza decision-critical

- beneficio centrale: €1,2M;
- range plausibile: €0,4M–€1,9M;
- costo: €1,0M.

Qui l'incertezza attraversa il break-even.

Deve comparire nella headline o accanto alla recommendation, non in una nota finale.

## Caso simulato/composito — Il forecast venduto come promessa

Un produttore industriale presenta al board:

> **Q4 revenue: €84,2M**

Il modello aveva in realtà un prediction interval 80% di €76M–€92M, ma il range rimane nel notebook tecnico.

Il board usa €84,2M come input puntuale per cash planning e acquisti.

Le vendite chiudono a €78,5M.

La previsione viene classificata come “sbagliata”.

Il problema non è soltanto statistico. È un **failure di traduzione**: un oggetto probabilistico è stato comunicato come commitment.

Una versione migliore:

> **La stima centrale Q4 è €84,2M; l'80% prediction interval è €76M–€92M. Il cash plan resta robusto sopra €79M, quindi il downside inferiore richiede una contingency sugli acquisti.**

L'incertezza diventa collegata all'azione.

## Data maturity: “provvisorio” è una proprietà del numero

Supponiamo che la revenue giornaliera sia D+1 ma i refund arrivino fino a D+5.

Scrivere:

> “Net revenue ieri: €4,1M”

senza indicare che il dato è provvisorio comunica una precisione che il sistema non possiede ancora.

Una Decision Communication Pack dovrebbe poter mostrare:

- `fresh as of`;
- stato `provisional / reconciled / final`;
- eventuale expected revision;
- quando verrà aggiornato il dato.

Questo è particolarmente importante nelle dashboard operative.

## Linguaggio calibrato: il verbo è parte del metodo

Confrontiamo:

> “La release ha ridotto la conversione.”

con:

> “Il calo è concentrato sugli utenti esposti alla release; non abbiamo ancora isolato causalmente l'effetto.”

Oppure:

> “Il pricing causa il churn.”

con:

> “Il pricing è compatibile con il pattern osservato, ma i dati storici non separano bene prezzo, mix di coorte e account maturity.”

La forza grammaticale della frase deve essere coerente con il **claim level** costruito nei capitoli 8 e 14.

## Visualizzare l'incertezza

Possibili forme:

- error bars;
- confidence band;
- prediction interval;
- fan chart;
- distribuzione;
- downside/base/upside coerenti;
- range annotato;
- tabella con switching value.

La forma dipende dalla decisione.

Se il pubblico deve confrontare alternative, spesso è più utile mostrare **range + threshold** che una distribuzione completa.

## Qualità e limiti devono essere utilizzabili

La Government Analysis Function britannica raccomanda di comunicare qualità, incertezza e cambiamenti in modo che l'utente possa capire l'impatto sull'interpretazione e sull'uso dei dati.

Una nota come:

> “I risultati sono soggetti a incertezza.”

è formalmente prudente ma operativamente inutile.

Meglio:

> “Il ranking tra A e B si inverte se l'uplift reale di A è sotto il 2,8%; l'intervallo corrente include valori inferiori a questa soglia.”

## Non nascondere il problema con più decimali

Precisione numerica e certezza epistemica sono cose diverse.

`12,417M` può avere tre decimali e dipendere da:

- refund ancora incompleti;
- FX provvisorio;
- forecast altamente instabile;
- definizione contestata.

Il numero più preciso non è necessariamente il messaggio più affidabile.

> **Comunicare l'incertezza bene significa mostrare non tutta l'incertezza possibile, ma quella che limita il claim o può cambiare l'azione.**

### Fonte

- Government Analysis Function, *Communicating quality, uncertainty and change*: https://analysisfunction.civilservice.gov.uk/policy-store/communicating-quality-uncertainty-and-change/
