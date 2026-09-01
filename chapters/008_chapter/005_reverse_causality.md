## 8.4 Causalità inversa e treatment response: quando l'intervento è una conseguenza del rischio

Una delle fonti più comuni di interpretazione sbagliata nasce quando l'azienda interviene **in risposta** a un deterioramento già iniziato.

Il trattamento precede l'outcome finale, ma non precede necessariamente il processo che lo ha generato.

### Caso simulato/composito — Più sconti, più churn

Un SaaS osserva:

| Clienti | Churn 90 giorni |
|---|---:|
| ricevono retention discount | 27% |
| non ricevono discount | 9% |

La lettura ingenua è:

> “Gli sconti aumentano il churn.”

Ma gli sconti vengono concessi dopo segnali come:

- calo d'uso;
- ticket critici;
- richiesta di cancellazione;
- pressione del procurement;
- downgrade pianificato.

Il processo assomiglia a:

```text
rischio latente -> sconto
rischio latente -> churn
sconto ---------> possibile riduzione del churn
```

Il trattamento può essere utile e apparire comunque associato a risultati peggiori.

### Il problema non è solo “Y causa X”

Nella pratica è spesso più utile parlare di **treatment by indication** o **intervento reattivo**.

La dinamica può essere:

```text
stato deteriorato_t-1 -> trattamento_t -> outcome_t+1
          |
          +---------------------------> outcome_t+1
```

Il trattamento arriva dopo che una parte della traiettoria causale è già iniziata.

### Il tempo va modellato come processo

Per ogni analisi causale dovremmo distinguere almeno:

1. finestra pre-trattamento;
2. momento di eleggibilità;
3. assignment;
4. exposure effettiva;
5. periodo in cui il trattamento può agire;
6. finestra di outcome.

Esempio:

```text
D-60 ... D-1   comportamento pre-treatment
D0             account diventa eleggibile
D1             chiamata assegnata
D3             chiamata effettivamente ricevuta
D4 ... D90     outcome window
```

Senza questa timeline è facile usare segnali prodotti dopo l'inizio del trattamento oppure trattare come baseline un comportamento già modificato dall'intervento.

### Immortal time e finestre costruite male

Supponiamo di confrontare clienti che “hanno ricevuto almeno una sessione di training nei primi 60 giorni” con quelli che non l'hanno ricevuta.

Per entrare nel gruppo trattato un cliente deve **sopravvivere abbastanza a lungo** da ricevere il training.

Se alcuni clienti churnano al giorno 10 non potranno mai entrare nel gruppo trattato.

Il confronto può quindi favorire artificialmente il training.

La definizione del tempo zero deve essere coerente tra gruppi.

### Caso simulato/composito — Manutenzione predittiva

Un impianto industriale mostra più guasti tra macchine che ricevono manutenzione straordinaria.

Non significa che la manutenzione causi i guasti.

I sensori rilevano vibrazioni anomale, il team pianifica manutenzione e alcune macchine falliscono comunque.

La vera domanda è:

> “Tra macchine con segnali di rischio comparabili, quale sarebbe stato il failure rate senza manutenzione?”

### Lag non significa automaticamente pre-treatment

Creare `feature_lag_7d` non rende automaticamente una variabile causalmente sicura.

Se il processo decisionale è iniziato due settimane prima, il valore a `t-7` può già riflettere il trattamento o la decisione di trattare.

Serve conoscere il **momento in cui l'intervento diventa possibile e inizia a influenzare il sistema**.

### Regola operativa

Prima di confrontare trattati e non trattati, costruisci una timeline e chiedi:

- quando è comparso il primo segnale di rischio?
- quando l'operatore ha deciso il trattamento?
- quando l'unità lo ha ricevuto davvero?
- quali covariate erano già influenzate dalla decisione?
- tutti i gruppi hanno lo stesso time zero?

> **La precedenza temporale è necessaria, ma la causalità richiede di ricostruire il processo che ha portato al trattamento, non soltanto l'ordine dei timestamp.**
