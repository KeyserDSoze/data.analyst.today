## 6.5 Churn: distinguere perdita di relazione, perdita di valore e perdita evitabile

Il churn viene spesso trattato come l'opposto della retention. La scorciatoia funziona solo quando popolazione, contratto e valore sono semplici. Nel lavoro reale perdere il 3% dei clienti può significare cose molto diverse a seconda di **chi** esce, **quanto valore** porta con sé e **per quale meccanismo** la relazione si interrompe.

### CloudLedger: stessi loghi persi, molto più valore che esce

**CloudLedger**, software contabile per PMI e mid-market, vede il customer churn mensile restare quasi stabile:

| Metrica | Trimestre precedente | Trimestre attuale |
| --- | ---: | ---: |
| Customer churn mensile | 3,1% | 3,2% |
| Gross revenue churn mensile | 2,8% | 5,4% |
| ARR medio cliente perso | 8.400 € | 19.700 € |

Guardando i loghi il deterioramento sembra minimo. Guardando la revenue, la storia cambia: l'azienda non sta perdendo molti più clienti, sta perdendo **clienti mediamente più grandi**. La priorità operativa cambia immediatamente.

È il motivo per cui in un business ricorrente conviene distinguere logo/customer churn, gross revenue churn, Gross Revenue Retention e Net Revenue Retention. La NRR può essere espressa come:

`NRR = (revenue iniziale - churn - contraction + expansion) / revenue iniziale`

Una NRR sopra il 100% significa che l'espansione dei clienti rimasti compensa più che completamente churn e contraction sulla base considerata. Ma anche questo aggregato può nascondere traiettorie opposte. CloudLedger ha NRR complessiva del **104%**, mentre i segmenti mostrano **SMB 111%**, **mid-market 102%** ed **enterprise 91%**. L'espansione degli account piccoli può quindi convivere con una perdita strutturale di valore nell'enterprise.

### Non tutto il churn è una scelta del cliente

Un abbonamento può interrompersi perché il cliente decide di andarsene, ma anche perché un pagamento fallisce. Stripe tratta esplicitamente questo secondo caso come **involuntary churn** e documenta strumenti di revenue recovery, notifiche e retry automatici per pagamenti ricorrenti falliti.[^stripe-recovery]

Carta scaduta, fondi insufficienti, rifiuto temporaneo dell'emittente, autenticazione non completata o metodo di pagamento non più valido non sono lo stesso problema di un cliente che ha deciso di lasciare il prodotto. La distinzione conta perché cambia l'intervento: a un cliente che vuole restare ma ha una carta scaduta non serve una campagna sul valore del prodotto; serve un processo di recovery del pagamento.

Per lo stesso motivo lo stato del cliente non dovrebbe essere ridotto a un booleano `churned`. Un account può essere contrattualmente attivo ma comportamentalmente inattivo, molto attivo ma vicino a un mancato rinnovo, temporaneamente `past_due`, oppure cancellato ma ancora autorizzato all'uso fino alla fine del periodo pagato. In un business subscription conviene spesso mantenere distinti **uso del prodotto, stato della subscription, stato del pagamento e stato contrattuale/commerciale**.

### Evento osservato, stato di rischio e previsione non sono la stessa cosa

“Il cliente ha cancellato”, “non usa il prodotto da trenta giorni” e “ha il 72% di probabilità di churn” appartengono a tre livelli differenti. Il primo è un evento osservato, il secondo uno stato comportamentale, il terzo una previsione. Mescolarli porta a dashboard e interventi incoerenti.

Anche il denominatore deve seguire il contratto. In un prodotto cancellabile in qualunque momento può avere senso usare la base attiva all'inizio del periodo. In un business con rinnovi annuali concentrati, la popolazione davvero esposta al rischio di churn in un mese può essere soprattutto quella eleggibile al rinnovo. La frequenza va quindi costruita sul processo reale, non su una formula copiata da un altro modello di business.

Una diagnosi utile dovrebbe permettere di completare questa frase:

> **Stiamo perdendo ______, per un valore di ______, soprattutto nella popolazione ______, nel momento ______, attraverso il meccanismo osservabile ______.**

Segmenti, coorti e lifecycle analysis possono spesso riempire le prime parti. L'ultima domanda — *perché accade e quale intervento lo riduce* — richiede spesso evidenza causale o sperimentale.

È qui che churn smette di essere una percentuale di dashboard e diventa un problema di relazione, economics e meccanismo.

[^stripe-recovery]: Stripe Documentation, *Revenue recovery* e *Automate payment retries*: https://docs.stripe.com/billing/revenue-recovery ; https://docs.stripe.com/billing/revenue-recovery/smart-retries
