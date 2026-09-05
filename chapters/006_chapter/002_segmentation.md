## 6.1 Segmentazione: dividere la popolazione solo quando cambia la decisione

Nel Capitolo 4 la segmentazione serviva soprattutto a rompere un aggregato e vedere se nascondeva strutture differenti. Nel lifecycle analysis deve fare qualcosa di più: **trasformare differenze osservate in unità decisionali**.

Un segmento è utile quando clienti che entrano, si attivano, restano, espandono o abbandonano in modo diverso richiedono una diagnosi, una priorità o un intervento differente. Se dividere la popolazione non cambia nulla di ciò che faremmo, abbiamo creato un filtro, non ancora un segmento strategico.

### Northstar Home: dal “mobile converte peggio” a un punto preciso del sistema

L'e-commerce immaginario **Northstar Home** vede il conversion rate scendere dal **3,9% al 3,5%**. La prima apertura per device mostra che il deterioramento è quasi interamente mobile:

| Device | Q1 | Q2 |
|---|---:|---:|
| Desktop | 5,8% | 5,9% |
| Mobile | 3,1% | 2,5% |
| Tablet | 3,4% | 3,3% |

“Il mobile converte peggio” è però ancora troppo ampio per essere una diagnosi. Sul mobile, il confronto per canale restringe ulteriormente il problema:

| Canale | Q1 | Q2 |
|---|---:|---:|
| Organic | 3,4% | 3,3% |
| Email | 4,6% | 4,5% |
| Paid search | 2,9% | 2,8% |
| Paid social | 2,7% | 1,6% |

Il calo vive soprattutto in `mobile + paid social`. Incrociando il paese emerge poi che il gap è concentrato in Italia e Spagna, dove è stata introdotta una nuova landing page. La frase utile diventa quindi:

> **Il calo aggregato è concentrato nel traffico paid social mobile di Italia e Spagna dopo il cambio di landing.**

La landing non è ancora una causa dimostrata. Ma la segmentazione ha già cambiato la decisione: non serve aprire un progetto generico sulla conversione mobile globale; serve indagare una popolazione e un punto del percorso molto più circoscritti.

Questa è la soglia che un buon segmento deve superare. Può cambiare **dove** crediamo si trovi il problema, **quanto** valore o rischio attribuiamo a un gruppo, **quale** intervento è plausibile, **quale** metrica è adatta o **chi** possiede la leva operativa.

Nel lifecycle i segmenti possono nascere da acquisizione, profilo, comportamento, stato del percorso o economics. Un canale o una campagna ci aiutano a capire quale popolazione stiamo portando dentro; mercato, use case, piano o dimensione account descrivono differenze strutturali; feature adottate e frequenza d'uso descrivono ciò che il cliente fa; stati come onboarding, activated, at-risk o reactivated localizzano il punto del percorso; ARR, margine, cost-to-serve ed LTV distinguono infine frequenza e impatto economico. Queste famiglie sono utili soltanto se restano collegate alla decisione. Un churn del 10% su clienti da 20 € al mese e lo stesso 10% su account enterprise sono la stessa frequenza, non lo stesso problema economico.

### Un comportamento interessante non è ancora una leva causale

Un case study pubblicato da **Amplitude** descrive come Canal+ abbia confrontato gruppi con pattern di utilizzo differenti. Gli utenti che guardavano sia contenuti live sia on-demand mostravano retention più alta rispetto a chi usava soltanto uno dei due formati; il team usò questa osservazione per orientare cambiamenti di prodotto.[^canal-amplitude]

Il claim va letto per ciò che è: **un'associazione comportamentale utile alla diagnosi e alla progettazione del prodotto**. Non dimostra, da solo, che indurre un utente a consumare entrambi i formati provochi causalmente maggiore retention. La segmentazione ci aiuta a trovare comportamenti che meritano attenzione; il metodo successivo deve stabilire se quei comportamenti sono anche leve.

Lo stesso principio protegge da due errori molto comuni. Il primo è la frammentazione eccessiva. Incrociare 8 paesi, 4 device, 6 canali, 5 piani e 3 fasce di tenure genera già **2.880 combinazioni** potenziali. Molte avranno basi minuscole, e un uplift del 40% su 17 utenti può essere una pista esplorativa senza essere una priorità aziendale. Per questo denominatore e distinzione tra segmenti pre-specificati ed esplorativi devono restare visibili.

Il secondo errore è definire il segmento usando informazione futura. Se al giorno 30 vogliamo distinguere clienti promettenti e creiamo il gruppo “chi farà almeno 10 ordini nei primi 12 mesi”, abbiamo usato il futuro per costruire la categoria e poi celebrato una relazione quasi tautologica con la retention annuale. Un segmento operativo al giorno 30 deve essere costruito con ciò che era conoscibile entro quel giorno. È lo stesso principio di leakage che tornerà nei modelli predittivi.

Per i segmenti che entrano stabilmente in una dashboard lifecycle conviene conservare una piccola scheda operativa:

```text
Segmento:
Regola di appartenenza:
Momento in cui l'appartenenza è conoscibile:
Dimensione / denominatore:
Differenza osservata nel lifecycle:
Decisione che cambia:
Owner dell'eventuale intervento:
Ipotesi o meccanismo plausibile:
Confermativo o esplorativo?
```

La domanda che chiude la sezione non è “quanti modi abbiamo per dividere gli utenti?”. È:

> **quale divisione della popolazione rende più precisa la diagnosi e cambia concretamente ciò che il team dovrebbe fare?**

[^canal-amplitude]: Amplitude, *How Canal+ used Product Intelligence to increase conversion by 3x*: https://amplitude.com/case-studies/canal
