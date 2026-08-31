## 9.12 Case study - Dal test al rollout: il checkout che migliorava la conversione ma aumentava i problemi a valle

Una piattaforma e-commerce internazionale, che chiameremo **Northstar Retail**, gestisce circa 28 milioni di sessioni al mese in Europa. Il team Checkout propone di rendere preselezionata l'opzione di consegna più veloce quando disponibile.

L'ipotesi di prodotto è semplice: meno scelta visibile e una proposta più chiara dovrebbero ridurre l'attrito e aumentare la conversione.

### Disegno iniziale

La randomizzazione avviene a livello utente. Il test coinvolge il 20% del traffico eleggibile.

Metrica primaria:

- completed orders per eligible user.

Guardrail:

- cancellation rate entro 24 ore;
- customer support contacts per order;
- refund rate;
- delivery complaint rate;
- margine netto per ordine.

Prima del lancio viene fissato un MDE di +0,20 punti percentuali sulla conversione, perché effetti più piccoli non giustificherebbero costi di implementazione, customer support aggiuntivo e rischio reputazionale.

### Prima settimana

I primi dati sembrano eccellenti:

| metrica | controllo | trattamento | differenza |
|---|---:|---:|---:|
| conversion rate | 4,91% | 5,18% | +0,27 pp |
| AOV | 73,40 € | 74,10 € | +0,95% |
| margine/order | 18,60 € | 18,94 € | +1,8% |

Il product manager propone il rollout al 100%.

L'analista rifiuta di chiudere il test dopo sette giorni per tre motivi:

1. il piano prevedeva almeno due cicli settimanali completi;
2. i reclami di consegna maturano con ritardo;
3. il controllo del Sample Ratio Mismatch deve essere completato prima dell'interpretazione.

### Seconda settimana: il quadro cambia

Dopo quattordici giorni:

- conversion: +0,23 pp;
- margine per order: +1,2%;
- cancellation rate: +0,34 pp;
- contatti al supporto per ordine: +7,6%;
- complaint rate legato alla consegna: +11,8%.

Il problema emerge dalle interviste al supporto: parte degli utenti non si rende conto di avere selezionato una consegna premium con sovrapprezzo. La conversione aumenta perché il checkout è più fluido, ma una parte del valore viene recuperata a valle sotto forma di cancellazioni, rimborsi e assistenza.

### Segmentazione predefinita

Il team aveva predefinito due segmenti:

- clienti abituali;
- nuovi clienti.

Tra i clienti abituali l'effetto è molto positivo e i guardrail restano stabili. Tra i nuovi clienti, invece, la conversion migliora di più ma aumentano nettamente cancellazioni e reclami.

La soluzione non è scegliere il segmento migliore dopo aver visto i dati. Il segmento era stato definito prima proprio perché il team sospettava differenze nella comprensione del checkout.

### Iterazione 2

Viene progettata una nuova variante:

- consegna veloce preselezionata solo per utenti ritornanti;
- per i nuovi utenti viene aggiunto un testo esplicito sul sovrapprezzo;
- il prezzo viene reso più prominente.

Il test riparte.

Dopo tre settimane:

- conversion complessiva: +0,19 pp;
- margine netto per eligible user: +3,4%;
- cancellation rate: differenza trascurabile;
- support contacts: +0,6%, non significativo;
- complaint rate: stabile.

### Rollout progressivo

Il team non passa direttamente dal 20% al 100%.

Il rollout viene articolato in:

- 20%;
- 50%;
- 80%;
- 100%.

A ogni fase vengono monitorati i guardrail e le metriche operative per verificare che l'effetto non cambi quando il sistema raggiunge scala maggiore.

Questa cautela è importante perché alcune regressioni emergono solo con più carico, più varietà di utenti o più casi limite.

### Un caso pubblico analogo: infrastruttura Microsoft

Microsoft Experimentation Platform ha documentato l'uso di A/B test per modifiche infrastrutturali e backend. Nei test reali, il team ha rilevato effetti inattesi che metriche tecniche locali non avrebbero mostrato; per questo ha affiancato alle metriche backend anche guardrail di prodotto più ampi. Quando comparivano regressioni, l'esposizione poteva essere fermata rapidamente, correggendo e ripetendo il test prima del rollout.

La lezione è la stessa del caso Northstar Retail:

> **Un esperimento non termina quando troviamo un p-value favorevole. Termina quando abbiamo abbastanza evidenza per decidere come distribuire il cambiamento senza compromettere il sistema.**

### Checklist della decisione finale

Prima del rollout l'analista deve poter rispondere a queste domande:

- l'assegnazione è rimasta valida?
- esiste SRM?
- la metrica primaria ha superato la soglia business rilevante?
- i guardrail sono sani?
- l'effetto è stabile nel tempo?
- gli effetti per segmenti erano predefiniti o post-hoc?
- esistono ritardi nella maturazione delle metriche?
- l'effetto può cambiare a rollout completo?
- abbiamo un piano di rollback?
- sappiamo quali metriche monitorare dopo il lancio?

### Fonte pubblica

- Microsoft Experimentation Platform, *A/B Testing Infrastructure Changes at Microsoft ExP*, 2024.
