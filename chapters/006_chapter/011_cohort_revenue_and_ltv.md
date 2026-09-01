## 6.10 Cohort value e LTV: seguire il valore, non solo la presenza

Retention e churn descrivono persistenza e perdita. Ma due coorti con la stessa retention possono avere valore economico molto diverso.

Per questo il lifecycle dovrebbe essere letto anche in termini di **valore cumulato**.

Una vista semplice e potente consiste nel seguire, per coorte di acquisizione, quanto revenue, margine o contribution profit viene generato dopo 30, 60, 90, 180 giorni.

Prima di costruire un modello sofisticato di LTV, spesso conviene guardare ciò che le coorti hanno realmente prodotto.

### Caso simulato/composito: ModaLab e il canale che sembrava troppo costoso

**ModaLab** è un e-commerce fashion. Il team performance confronta paid social e referral.

| Canale | CAC medio | Primo ordine medio |
| --- | ---: | ---: |
| Paid social | 41 € | 72 € |
| Referral | 23 € | 69 € |

Guardando soltanto CAC e primo ordine, referral sembra nettamente migliore.

L'analista costruisce però le coorti e segue la revenue cumulata per cliente:

| Canale | Revenue D30 | Revenue D90 | Revenue D180 |
| --- | ---: | ---: | ---: |
| Paid social | 78 € | 146 € | 238 € |
| Referral | 73 € | 112 € | 151 € |

Paid social costa di più all'inizio, ma le sue coorti acquistano più frequentemente nei mesi successivi.

Quando il team passa dalla revenue al margine lordo cumulato, la differenza resta:

- paid social: 91 € a 180 giorni;
- referral: 63 €.

La domanda cambia da:

> quale canale ha il CAC più basso?

A:

> quanto capitale siamo disposti a spendere oggi per acquisire una coorte che produce più margine nei mesi successivi?

### Valore osservato e LTV previsto non sono la stessa cosa

È utile distinguere due concetti.

**Observed cohort value** — valore realmente prodotto fino a un certo orizzonte.

**Predicted LTV** — stima del valore futuro che la coorte dovrebbe produrre oltre ciò che abbiamo già osservato.

Il primo è descrittivo. Il secondo richiede un modello e quindi assunzioni.

Confonderli rende un forecast simile a un fatto già avvenuto.

### Revenue, gross margin e contribution margin

La parola “LTV” viene spesso usata per quantità economicamente diverse.

Una coorte può produrre 300 € di revenue ma avere:

- molti resi;
- costi di fulfilment elevati;
- incentivi;
- fee di pagamento;
- supporto costoso;
- forti sconti.

Per ModaLab due coorti generano entrambe 220 € di revenue a 180 giorni.

La prima ha return rate 9% e margine lordo 48%. La seconda ha return rate 24%, margine 36% e forte uso di coupon.

Chiamare entrambe “LTV 220 €” nasconde la differenza che conta per la decisione.

### Cohort maturity: non confrontare futuro con passato

Una coorte acquisita un mese fa ha avuto un solo mese per generare valore. Una coorte di un anno fa ne ha avuti dodici.

Confrontare il valore cumulato “fino a oggi” senza allineare l'età produce quasi sempre un risultato inutile.

Le coorti devono essere confrontate alla stessa maturità:

- D30 contro D30;
- M3 contro M3;
- M12 contro M12.

Questo sembra elementare, ma diventa meno ovvio quando le dashboard mostrano una sola colonna di `lifetime_revenue`.

### Il problema delle coorti non mature nei modelli LTV

Se il business è nuovo o il comportamento è cambiato, le coorti recenti non hanno ancora mostrato il loro intero lifecycle.

Per prevederne il valore futuro possiamo usare:

- pattern di coorti più mature;
- modelli di retention/survival;
- frequenza d'acquisto;
- margine atteso;
- scenario analysis.

Ma la qualità del LTV previsto dipende dalla stabilità di queste relazioni.

Un cambio di pricing, prodotto, acquisition mix o retention può rendere poco trasferibile il passato.

### Payback period: una domanda spesso più operativa del LTV

In molti business la domanda decisiva non è soltanto quanto vale un cliente “in tutta la vita”, ma **quando recuperiamo il costo di acquisizione**.

Se una coorte ha CAC di 80 € e genera contribution margin cumulato:

- D30: 22 €;
- D90: 51 €;
- D180: 86 €;

il payback avviene tra tre e sei mesi.

Una seconda coorte può avere LTV finale maggiore ma richiedere diciotto mesi per recuperare il CAC. Per un'azienda con vincoli di cassa, la differenza è enorme.

### LTV/CAC non è una legge universale

Rapporti come `LTV/CAC` possono essere utili, ma diventano pericolosi quando numeratore e denominatore non sono costruiti con definizioni compatibili.

Prima di usare il rapporto bisogna sapere:

- LTV su revenue o margine?
- CAC include sales e marketing allocati oppure solo media spend?
- quale orizzonte temporale?
- il LTV è osservato o previsto?
- il CAC è medio o marginale?
- le due quantità appartengono alla stessa coorte?

Un rapporto elegante non corregge due definizioni incoerenti.

### Dalla retention al valore

Una Lifecycle Diagnostic Map dovrebbe quindi tenere insieme almeno tre dimensioni:

- **presenza** — il cliente rimane?
- **comportamento** — continua a ottenere/creare valore?
- **economics** — quanto valore economico genera nel tempo?

Questa è la differenza tra seguire utenti e seguire un business.

### La domanda operativa

Prima di presentare un LTV, completa questa frase:

> Stiamo stimando ______ per la coorte ______, su un orizzonte di ______, usando ______ come misura economica; la parte fino a ______ è osservata, la parte successiva è prevista.

Se non riusciamo a distinguerlo, il numero è probabilmente troppo ambiguo per sostenere una decisione.
