## 10.14 Drift e monitoring: un modello non resta valido per sempre

La validazione non finisce quando il modello entra in produzione.

Un modello può essere eccellente al momento del deployment e deteriorarsi mesi dopo perché cambia il mondo su cui opera.

Questo fenomeno viene spesso riassunto con il termine **drift**.

### Data drift e concept drift

È utile distinguere due idee.

**Data drift**: cambia la distribuzione delle feature in ingresso.

Esempio:

- età media dei clienti diversa;
- nuovi mercati;
- nuovi device;
- diversa composizione del traffico;
- comportamento di acquisto mutato.

**Concept drift**: cambia la relazione tra feature e target.

Una variabile che prima prevedeva bene il churn può perdere valore perché il comportamento del cliente o il prodotto sono cambiati.

### Caso simulato: Horizon Travel e il modello che invecchia in sei mesi

Horizon Travel usa un modello per prevedere cancellazioni di prenotazioni alberghiere.

Al momento del lancio:

- AUC: 0,84;
- precision sul top 10% di rischio: 42%;
- calibration buona.

Sei mesi dopo:

- AUC: 0,75;
- precision top 10%: 27%;
- probabilità sovrastimate.

Che cosa è successo?

Nel frattempo l'azienda ha:

- introdotto una nuova politica di cancellazione gratuita;
- aumentato il traffico mobile;
- aperto due nuovi mercati;
- cambiato la composizione dei canali paid;
- modificato il programma loyalty.

Il modello non è “rotto” in senso tecnico.

È diventato meno rappresentativo del processo reale.

### Monitorare soltanto le feature non basta

Puoi osservare drift nelle feature senza sapere subito se la performance è peggiorata.

Viceversa, la performance può deteriorarsi anche con feature apparentemente stabili se cambia il rapporto tra feature e target.

Un sistema di monitoring dovrebbe quindi distinguere almeno:

1. qualità dei dati;
2. distribuzione delle feature;
3. distribuzione degli score;
4. calibration;
5. performance predittiva quando il target diventa disponibile;
6. metriche business downstream.

### Il ritardo del target

In molti casi non conosci subito la verità.

Per esempio, se prevedi churn a 90 giorni, devi aspettare prima di poter misurare la performance reale del modello sui nuovi clienti.

Nel frattempo puoi monitorare segnali anticipatori:

- score distribution;
- missing rate;
- nuove categorie;
- PSI o altre misure di shift;
- volumi per segmento;
- tassi di intervento.

Ma questi indicatori sono proxy.

Non sostituiscono la verifica finale sulla performance.

### Caso simulato: SecureNet e il falso allarme di drift

SecureNet monitora un modello antifrode.

Dopo una campagna marketing, il valore medio delle transazioni aumenta del 18% e il monitor segnala forte data drift.

Il team pensa che il modello stia degradando.

Quando arrivano le label, però:

- recall stabile;
- precision stabile;
- calibration quasi invariata.

Il drift nelle feature era reale, ma non aveva ancora compromesso la capacità predittiva.

Questo mostra perché drift non significa automaticamente failure.

### Monitoring della decisione, non solo del modello

Se il modello alimenta un processo operativo, bisogna monitorare anche ciò che succede dopo.

Per esempio:

```text
score di churn
→ lista clienti a rischio
→ contatto del customer success
→ offerta retention
→ costo dell'intervento
→ churn evitato
```

Anche con performance statistica stabile, il valore può peggiorare se:

- il team non riesce a contattare i clienti;
- il trattamento perde efficacia;
- il costo dell'incentivo sale;
- la capacità operativa diminuisce.

### Metodo operativo

Un modello in produzione dovrebbe avere almeno:

- owner chiaro;
- frequenza di monitoraggio;
- metriche statistiche;
- metriche operative;
- soglie di attenzione;
- procedura di retraining;
- possibilità di rollback;
- documentazione delle modifiche.

Il deployment non è la fine del progetto.

È l'inizio della fase in cui il modello deve dimostrare di sopravvivere alla realtà.