## 6.10 Cohort revenue e LTV: non tutte le coorti valgono allo stesso modo

La retention comportamentale dice se gli utenti restano. Ma il business spesso deve sapere anche **quanto valore economico genera ogni coorte nel tempo**.

Una coorte può trattenere molti utenti e produrre poca revenue. Un'altra può avere meno utenti ma ticket medio, frequenza d'acquisto o margine molto più alti.

Per questo è utile costruire una vista di **cohort revenue**: per ogni coorte di acquisizione, misurare la revenue cumulata dopo 30, 60, 90, 180 giorni o qualunque orizzonte sia coerente con il business.

### Caso: ModaLab e il canale che sembrava troppo costoso

ModaLab è un e-commerce fashion. Il team performance confronta due canali:

- paid social;
- referral program.

A prima vista il referral sembra nettamente migliore:

| Canale | CAC medio | Primo ordine medio |
|---|---:|---:|
| Paid social | 41 € | 72 € |
| Referral | 23 € | 69 € |

Il CFO propone di ridurre paid social perché il rapporto tra primo ordine e CAC è peggiore.

L'analista costruisce invece le coorti e osserva la revenue cumulata per cliente.

| Canale | Revenue 30 gg | Revenue 90 gg | Revenue 180 gg |
|---|---:|---:|---:|
| Paid social | 78 € | 146 € | 238 € |
| Referral | 73 € | 112 € | 151 € |

I clienti paid social costano di più all'inizio, ma tendono a comprare categorie ad alta frequenza e tornano più spesso.

Quando il confronto viene fatto sul margine lordo cumulato, il quadro cambia ancora:

- paid social: 91 € di margine a 180 giorni;
- referral: 63 €.

La decisione non è più “paid social costa troppo”. Diventa “quanto siamo disposti a pagare oggi per una coorte che genera più valore nei prossimi sei mesi?”.

### Lifetime Value

Il **Customer Lifetime Value (LTV o CLV)** tenta di sintetizzare il valore economico atteso generato da un cliente durante la relazione con l'azienda.

Esistono molte formule. In un modello semplice:

\[
LTV \approx margine\ medio\ per\ periodo \times durata\ media\ della\ relazione
\]

Ma questa formula può essere troppo grezza quando retention, frequenza d'acquisto e margini cambiano nel tempo.

Un approccio più analitico è calcolare il valore cumulato osservato per coorte e, solo dopo aver compreso il pattern, valutare se stimare il valore futuro.

### Revenue LTV non significa profit LTV

Un errore comune è chiamare LTV la revenue cumulata senza sottrarre costi variabili, resi, incentivi o costi di servizio.

Per ModaLab, due coorti producono entrambe 220 € di revenue a 180 giorni, ma una ha:

- return rate del 9%;
- margine lordo del 48%;
- quasi nessun voucher.

L'altra ha:

- return rate del 24%;
- margine lordo del 36%;
- forte uso di coupon.

I due “LTV” non sono economicamente equivalenti.

### Cosa deve controllare l'analista

Prima di presentare un LTV, bisogna sapere:

- se è osservato o previsto;
- se è revenue, margine o contribution profit;
- qual è l'orizzonte temporale;
- come viene gestito il churn;
- se i costi di acquisizione sono inclusi;
- se le coorti sono mature abbastanza per essere confrontate.

Un LTV con una formula elegante e una definizione vaga è spesso meno utile di una semplice tabella di revenue cumulata per coorte, costruita bene.
