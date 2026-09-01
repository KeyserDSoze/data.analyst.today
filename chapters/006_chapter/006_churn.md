## 6.5 Churn: distinguere perdita di relazione, perdita di valore e perdita evitabile

Il churn viene spesso trattato come l'opposto della retention. Questa scorciatoia funziona solo in contesti semplici.

Nel lavoro reale dobbiamo distinguere almeno tre domande:

- quanti clienti perdiamo?
- quanto valore economico perdiamo?
- quanta parte della perdita deriva da una decisione del cliente e quanta da problemi operativi recuperabili?

Queste domande possono produrre diagnosi molto diverse.

### Caso simulato/composito: CloudLedger e il churn apparentemente stabile

**CloudLedger** vende software contabile a PMI e aziende mid-market. Nel trimestre il customer churn mensile rimane quasi invariato.

| Metrica | Trimestre precedente | Trimestre attuale |
| --- | ---: | ---: |
| Customer churn mensile | 3,1% | 3,2% |
| Gross revenue churn mensile | 2,8% | 5,4% |
| ARR medio cliente perso | 8.400 € | 19.700 € |

Se guardiamo i loghi, la situazione sembra stabile. Se guardiamo la revenue, il deterioramento è evidente.

Il problema non è “stiamo perdendo molti più clienti”. È:

> stiamo perdendo clienti mediamente più grandi.

La priorità operativa cambia immediatamente.

### Logo churn, revenue churn e retention della revenue

Nel SaaS è utile separare:

**Logo o customer churn** — quanti account escono.

**Gross revenue churn** — quanta revenue ricorrente viene persa per cancellazioni e contrazioni.

**Gross Revenue Retention (GRR)** — quanta revenue iniziale rimane senza considerare espansioni.

**Net Revenue Retention (NRR)** — quanta revenue iniziale rimane dopo churn e contraction, includendo anche expansion.

Una formulazione comune è:

`NRR = (revenue iniziale - churn - contraction + expansion) / revenue iniziale`

Una NRR superiore al 100% indica che, sulla base considerata, l'espansione dei clienti rimasti compensa più che completamente le perdite.

Ma l'aggregato può ancora ingannare.

CloudLedger ha NRR complessiva del 104%:

- SMB: 111%;
- mid-market: 102%;
- enterprise: 91%.

L'espansione degli account piccoli nasconde una perdita di valore nell'enterprise.

### Churn volontario e involontario

Un cliente può uscire perché non vuole più il prodotto. Ma un abbonamento può interrompersi anche perché il pagamento fallisce.

Stripe documenta esplicitamente il problema dell'**involuntary churn** e offre strumenti di revenue recovery e retry automatici per pagamenti ricorrenti falliti.[^stripe-recovery]

Le cause possono includere:

- carta scaduta;
- fondi insufficienti;
- rifiuto temporaneo dell'emittente;
- autenticazione richiesta e non completata;
- metodo di pagamento non più valido.

Questo cambia completamente il tipo di intervento.

Se il cliente vuole rimanere ma la carta è scaduta, una campagna “perché ci stai lasciando?” è la risposta sbagliata. Serve un processo di recovery del pagamento.

### Stato contrattuale e stato comportamentale

Un cliente può essere:

- contrattualmente attivo ma praticamente inattivo;
- molto attivo ma vicino a una scadenza non rinnovata;
- temporaneamente `past_due` per un pagamento fallito;
- cancellato ma ancora autorizzato a usare il prodotto fino alla fine del periodo pagato.

Per questo “churned” non dovrebbe essere una colonna booleana priva di definizione.

In un business subscription conviene spesso modellare separatamente:

1. **uso del prodotto**;
2. **stato della subscription**;
3. **stato del pagamento**;
4. **stato commerciale/contrattuale**.

### Churn osservato e churn a rischio

Un altro errore consiste nel mescolare un evento già avvenuto con una previsione.

- “Il cliente ha cancellato” è un evento osservato.
- “Il cliente non usa il prodotto da 30 giorni” è uno stato comportamentale.
- “Il cliente ha 72% di rischio di churn” è una previsione.

Sono tre informazioni diverse e richiedono azioni diverse.

### Il churn deve avere un denominatore coerente

Anche qui il denominatore conta.

Per un churn mensile su subscription, il denominatore può essere la base attiva all'inizio del periodo. In altri contesti può essere una popolazione eleggibile al rinnovo.

Un business annuale con rinnovi concentrati non dovrebbe interpretare allo stesso modo un churn mensile di un prodotto cancellabile in qualunque momento.

La metrica deve seguire il contratto e il ciclo del cliente.

### La domanda operativa

Prima di aprire un progetto di churn, conviene completare questa frase:

> Stiamo perdendo ______, per un valore di ______, soprattutto nella popolazione ______, nel momento ______, attraverso il meccanismo osservabile ______.

Le prime quattro parti possono spesso essere descritte con segmenti, coorti e lifecycle analysis.

L'ultima — **perché accade e quale intervento lo riduce** — richiederà spesso strumenti causali o sperimentali che incontreremo più avanti.

[^stripe-recovery]: Stripe Documentation, “Revenue recovery” e “Automate payment retries”, https://docs.stripe.com/billing/revenue-recovery ; https://docs.stripe.com/billing/revenue-recovery/smart-retries
