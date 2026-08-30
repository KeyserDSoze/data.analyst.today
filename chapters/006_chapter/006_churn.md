## 6.5 Churn: chi se ne va e cosa stiamo davvero misurando

Il churn e' spesso presentato come l'opposto della retention. In molti contesti e' una buona approssimazione, ma nella pratica bisogna essere piu' precisi.

Per un servizio in abbonamento, il customer churn puo' essere definito come:

\[
Customer\ Churn = \frac{Clienti\ persi\ nel\ periodo}{Clienti\ attivi\ a\ inizio\ periodo}
\]

Ma questa formula non dice nulla sul valore economico dei clienti persi.

### Caso: churn stabile, business in peggioramento

CloudLedger vende software contabile a PMI e aziende mid-market. Nel trimestre il customer churn resta stabile al 3,2% mensile. Il management conclude che la retention e' sotto controllo.

L'analista calcola anche il revenue churn.

Scopre che i clienti persi nel trimestre sono meno numerosi, ma mediamente molto piu' grandi.

| Metrica | Trimestre precedente | Trimestre attuale |
| --- | ---: | ---: |
| Customer churn mensile | 3,1% | 3,2% |
| Gross revenue churn mensile | 2,8% | 5,4% |
| ARR medio cliente perso | 8.400 € | 19.700 € |

Il numero di clienti che lascia e' quasi invariato. Il valore perso e' quasi raddoppiato.

La diagnosi cambia completamente: non c'e' un problema generalizzato di churn, ma un problema concentrato sui clienti di valore maggiore.

### Logo churn, revenue churn e net revenue retention

Nel SaaS e nei modelli subscription, guardare solo il numero di clienti puo' essere insufficiente.

Un'azienda puo' perdere alcuni clienti ma espandere gli account esistenti tramite upgrade, nuovi utenti o moduli aggiuntivi. Per questo spesso si misura anche la Net Revenue Retention:

\[
NRR = \frac{Ricavi\ iniziali - churn - contraction + expansion}{Ricavi\ iniziali}
\]

Una NRR sopra il 100% significa che l'espansione dei clienti rimasti piu' che compensa churn e riduzioni.

Ma anche questo indicatore va segmentato.

CloudLedger ha una NRR complessiva del 104%. Sembra eccellente. Segmentando:

- SMB: 111%;
- mid-market: 102%;
- enterprise: 91%.

L'aggregato nasconde un problema serio sull'enterprise.

### Churn volontario e involontario

Non tutto il churn deriva da una decisione consapevole del cliente.

In un servizio consumer, una quota di abbonamenti puo' terminare per carta scaduta, pagamento rifiutato o errore di fatturazione. Questo e' churn involontario.

Se il 18% delle cancellazioni deriva da pagamenti falliti, un progetto di retention basato solo su campagne email ai clienti insoddisfatti parte dalla diagnosi sbagliata.

### Churn come evento o come stato

Un'altra distinzione importante riguarda il momento in cui il cliente e' considerato perso.

Un account che non usa il prodotto da 45 giorni e' gia' churned? Oppure lo diventa solo alla cancellazione contrattuale? Un cliente e-commerce che non acquista da sei mesi e' perso o semplicemente inattivo?

Non esiste una risposta universale.

La definizione deve essere coerente con:

- ciclo di acquisto;
- modello contrattuale;
- comportamento naturale del cliente;
- decisione che vogliamo prendere.

Il churn e' utile quando rappresenta un evento economicamente e operativamente interpretabile, non quando e' solo una percentuale presente in un dashboard.
