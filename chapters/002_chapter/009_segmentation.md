## 2.8 Segmentazioni previste: cercare eterogeneità che può cambiare la decisione

Le medie aggregate possono nascondere differenze decisive, ma questo non significa che ogni dimensione disponibile meriti una segmentazione. Nel brief non stiamo ancora facendo EDA completa; stiamo decidendo **quali differenze tra gruppi sarebbe utile rendere osservabili fin dall'inizio perché potrebbero cambiare la spiegazione o l'azione**.

Una dimensione entra nel piano quando esiste una ragione per aspettarsi eterogeneità rilevante. Se un nuovo checkout è stato rilasciato soltanto su mobile, `device` non è un taglio casuale: separa popolazioni con esposizioni diverse e può distinguere un problema generale da uno collegato alla release. Se pricing e policy cambiano per paese, la geografia può determinare sia il meccanismo sia l'intervento disponibile. Se il mix di acquisizione varia molto tra canali, il canale può spiegare perché un outcome aggregato cambia anche quando il comportamento dentro ogni segmento resta stabile.

La regola è semplice: **una segmentazione è prioritaria quando una differenza tra gruppi potrebbe cambiare ciò che crediamo o ciò che facciamo**.

### Caso simulato/composito: retention in calo, comportamento stabile

Supponiamo che la retention complessiva scenda dall'82% al 77%. Una lettura aggregata suggerisce che l'esperienza dei clienti sia peggiorata. Segmentando per canale di acquisizione scopriamo però che la retention dentro ciascun canale è quasi stabile; ciò che è cambiato è il mix, perché una quota molto maggiore di nuovi clienti arriva da paid social, un canale che storicamente presenta retention inferiore.

Questa osservazione cambia la diagnosi. Non abbiamo necessariamente un deterioramento dell'esperienza all'interno dei segmenti. Potremmo avere soprattutto una composizione diversa della popolazione. La decisione, di conseguenza, può spostarsi dal prodotto alla strategia di acquisizione.

È esattamente il tipo di situazione in cui il livello aggregato produce una storia plausibile ma incompleta, anticipando fenomeni come il paradosso di Simpson che approfondiremo nel Capitolo 4.

## Pre-specificare non significa vietare l'esplorazione

Conviene distinguere le segmentazioni motivate **prima** di osservare il risultato da quelle che emergono durante l'EDA. Le prime sono collegate a ipotesi, rollout, policy o conoscenza del dominio. Le seconde sono scoperte esplorative e possono essere molto preziose, ma vanno interpretate sapendo che sono emerse dopo aver cercato tra molte combinazioni.

Questa distinzione protegge da una forma di data fishing: esplorare centinaia di tagli finché appare un pattern spettacolare e poi raccontarlo come se fosse stato previsto. Non rende il pattern falso; cambia il livello di fiducia con cui dovremmo trattarlo e la necessità di confermarlo.

Perciò il brief mantiene una piccola mappa delle segmentazioni realmente motivate:

| Segmentazione | Perché potrebbe contare | Decisione che potrebbe cambiare | Priorità |
|---|---|---|---|
| device | rollout differente mobile/desktop | rollback mirato | alta |
| acquisition channel | mix clienti differente | riallocazione budget | alta |
| paese | policy e pricing diversi | intervento locale | media |

Le segmentazioni esplorative potranno essere aggiunte dopo. Il punto non è limitare la curiosità, ma distinguere ciò che stavamo cercando da ciò che abbiamo scoperto mentre cercavamo altro.

> **Segmentare non significa dividere il dataset in tutti i modi possibili. Significa cercare differenze che possono cambiare il modello del problema o la leva su cui decidiamo di intervenire.**
