## 8.4 Interventi reattivi: quando il trattamento arriva perché il rischio è già iniziato

Una delle interpretazioni causali più insidiose nasce quando l'azienda interviene **in risposta** a un deterioramento già in corso. Il trattamento precede l'outcome finale, ma non precede necessariamente il processo che lo ha generato.

### Caso simulato/composito — Più sconti, più churn

Un SaaS osserva:

| Clienti | Churn 90 giorni |
|---|---:|
| ricevono retention discount | 27% |
| non ricevono discount | 9% |

La lettura superficiale è che gli sconti aumentino il churn. Il processo operativo racconta però una storia diversa: lo sconto viene concesso dopo segnali come calo d'uso, ticket critici, richiesta di cancellazione, pressione del procurement o downgrade pianificato. La struttura plausibile è:

```text
rischio latente -> sconto
rischio latente -> churn
sconto ---------> possibile riduzione del churn
```

Il trattamento può quindi essere utile e apparire comunque associato a risultati peggiori. Più che una semplice “causalità inversa”, nel lavoro aziendale è spesso un problema di **treatment by indication**: l'intervento viene attivato proprio perché il rischio è già elevato.

Per questo il tempo va ricostruito come processo, non come una sola colonna timestamp. Una causal analysis dovrebbe distinguere finestra pre-treatment, momento di eleggibilità, assignment, exposure effettiva, periodo in cui il trattamento può agire e finestra di outcome. Una timeline minima può essere:

```text
D-60 ... D-1   comportamento pre-treatment
D0             account diventa eleggibile
D1             chiamata assegnata
D3             chiamata effettivamente ricevuta
D4 ... D90     outcome window
```

Questa sequenza impedisce di usare come “baseline” un comportamento già modificato dalla decisione di trattare e rende visibile quando una covariata smette di essere davvero pre-treatment.

### Quando il time zero crea il bias

Supponiamo di confrontare clienti che “hanno ricevuto almeno una sessione di training nei primi 60 giorni” con quelli che non l'hanno ricevuta. Per entrare nel gruppo trattato un cliente deve rimanere nel sistema abbastanza a lungo da ricevere il training. Chi churna al giorno 10 non potrà mai essere classificato come trattato. Una parte della migliore sopravvivenza del gruppo può quindi essere incorporata nella definizione stessa del trattamento: è un esempio di **immortal time bias**.

Il rimedio non è aggiungere una feature. Serve un time zero coerente tra gruppi e una definizione di eleggibilità che permetta a tutte le unità comparate di avere la stessa opportunità di ricevere il trattamento.

La stessa logica vale in manutenzione predittiva. Se le macchine che ricevono manutenzione straordinaria hanno più guasti, non possiamo concludere che la manutenzione li provochi: i sensori hanno rilevato vibrazioni anomale, il team è intervenuto e alcune macchine hanno fallito comunque. La domanda causale è “tra macchine con segnali di rischio comparabili, quale sarebbe stato il failure rate senza manutenzione?”.

Un lag non rende automaticamente una variabile causalmente sicura. `feature_lag_7d` può essere cronologicamente precedente all'outcome e tuttavia già successiva alla decisione operativa che ha iniziato a modificare il sistema. Bisogna conoscere il momento in cui l'intervento diventa possibile e può iniziare a influenzare comportamento e misure.

Prima di confrontare trattati e non trattati, quindi, conviene poter rispondere a cinque domande: quando è comparso il primo segnale di rischio, quando l'operatore ha deciso il trattamento, quando l'unità lo ha ricevuto davvero, quali covariate erano già influenzate dalla decisione e se tutti i gruppi condividono lo stesso time zero.

> **La precedenza temporale è necessaria, ma la causalità richiede di ricostruire il processo che ha portato al trattamento, non soltanto l'ordine dei timestamp.**

Questa ricostruzione porta al problema successivo: perfino con un timing corretto possiamo introdurre bias scegliendo **chi entra nel campione finale**.
