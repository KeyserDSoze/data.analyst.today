## 5.7 Intuizione bayesiana: l'evidenza deve poterci far cambiare idea

Il ragionamento bayesiano formalizza qualcosa che un buon analista dovrebbe fare anche prima di conoscere la formula: **partire da ciò che è plausibile, osservare nuova evidenza e aggiornare la propria valutazione in proporzione a quanto quell'evidenza discrimina tra le ipotesi**.

La formula di Bayes è:

`P(A|B) = P(B|A) × P(A) / P(B)`.

Nel linguaggio bayesiano, ciò che consideriamo plausibile prima dell'evidenza viene espresso attraverso un **prior**; la compatibilità dei dati con l'ipotesi passa attraverso la **likelihood**; dopo l'osservazione otteniamo una valutazione aggiornata, il **posterior**. NIST descrive proprio Bayes come il meccanismo che combina conoscenza precedente e dati correnti per produrre una distribuzione posterior.[^nist-bayes]

La sezione sulla probabilità condizionata ci ha già mostrato perché il base rate conta. Qui facciamo un passo in più: invece di trattare ogni nuovo dato come se arrivasse in un vuoto informativo, chiediamo **quanto deve modificare ciò che ritenevamo plausibile prima**.

## Un crollo di conversione e quattro spiegazioni concorrenti

Una piattaforma e-commerce vede il checkout conversion rate scendere dal 4,1% al 3,2% in meno di un'ora. Il team considera quattro ipotesi: problema di tracking, cambiamento nel mix di traffico, bug della nuova release oppure problema del payment provider.

Negli ultimi 40 incidenti con un pattern iniziale simile, le cause erano state approssimativamente:

| Causa | Frequenza storica |
|---|---:|
| Tracking / telemetry | 40% |
| Traffic mix / campagne | 25% |
| Product bug | 20% |
| Payment provider | 15% |

Queste frequenze non sono una legge del mondo. Possono però funzionare come **prior operativo**: prima di ulteriori evidenze, un problema di telemetry merita più attenzione di una causa storicamente molto più rara.

Poi arriva la prima informazione nuova. Finance e il database transazionale confermano che sono scesi anche gli ordini reali. L'ipotesi “solo tracking” perde molto peso.

La seconda evidenza mostra che web e Android sono stabili mentre il problema è quasi esclusivamente su iOS. Un semplice cambiamento generale di traffic mix diventa meno plausibile e l'ipotesi di product bug guadagna terreno.

Infine il calo viene localizzato sulla versione 8.42: iOS 8.41 mantiene una conversione normale, mentre la 8.42 perde utenti nel passaggio payment → confirmation. I log mostrano un errore nella gestione delle carte salvate introdotto proprio da quella release.

La storia importante non è che l'ipotesi corretta “ha vinto”. È che il team ha permesso a ipotesi inizialmente plausibili di **perdere peso** man mano che l'evidenza diventava meno compatibile con esse.

## Bayesian thinking anche senza un modello bayesiano completo

Nel caso non abbiamo calcolato numericamente ogni posterior. Eppure la sequenza è già bayesiana:

**prior → evidenza → aggiornamento relativo delle ipotesi → nuova evidenza → nuovo aggiornamento**.

È l'opposto del confirmation bias. Una prima intuizione non diventa il tema da difendere; diventa una posizione provvisoria che deve essere aggiornata anche quando i dati la indeboliscono.

Il prior, a sua volta, non è una preferenza personale resa matematica. Può derivare dallo storico dello stesso processo, da popolazioni comparabili, da studi precedenti, da conoscenza di dominio formalizzata o, quando sappiamo poco, da una distribuzione volutamente ampia. Deve essere **difendibile e aggiornabile**. Se viene scelto soltanto perché spinge il risultato verso la conclusione desiderata, non sta aiutando l'apprendimento.

## La stessa percentuale può contenere quantità di informazione molto diverse

Supponiamo che un nuovo piano abbia conversione storica attesa attorno al 12%. Nei primi 20 visitatori osserviamo 8 acquisti: 40%. È un segnale interessante, ma venti osservazioni contengono poca informazione e possono provenire da early adopter molto selezionati.

Se osservassimo invece 8.000 acquisti su 20.000 visitatori comparabili, lo stesso 40% dovrebbe produrre un aggiornamento enormemente più forte. La percentuale è identica; cambia **quanto il nuovo dato è capace di spostare razionalmente ciò che credevamo prima**.

Questa idea collega Bayes al resto del capitolo. Standard error, confidence interval e power parleranno con un linguaggio diverso della stessa questione: quanta informazione contiene realmente ciò che abbiamo osservato?

## AI: generare ipotesi non significa pesarle

Un sistema AI può proporre in pochi secondi venti spiegazioni per un'anomalia. Questo amplia lo spazio di ricerca, ma non assegna alle ipotesi la stessa plausibilità. Frequenza storica, coerenza con il dominio, capacità di spiegare i dettagli osservati, costo della verifica e nuova evidenza devono ancora stabilire quali ipotesi meritino priorità e quali debbano essere abbandonate.

È un'altra applicazione del principio di **Al timone**: l'AI può moltiplicare le alternative; la responsabilità di aggiornare le convinzioni in funzione dell'evidenza resta parte del lavoro analitico.

> **La domanda bayesiana non è “avevo ragione?”. È “dato ciò che sapevo prima e ciò che ho osservato adesso, quanto deve cambiare ciò che considero plausibile?”.**

---

### Fonte

[^nist-bayes]: NIST/SEMATECH, *How can Bayesian methodology be used for reliability evaluation?*. https://www.itl.nist.gov/div898/handbook/apr/section2/apr1a.htm
