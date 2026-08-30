## 6.2 Coorti: seguire gruppi comparabili nel tempo

Una coorte e' un gruppo di utenti o clienti che condivide un punto di partenza o una caratteristica rilevante. In molti casi, la coorte e' definita dal momento della prima acquisizione: mese di registrazione, prima transazione, attivazione o inizio abbonamento.

Il vantaggio principale e' che permette di separare il comportamento di gruppi entrati nel sistema in momenti diversi.

Immaginiamo FlowDesk, un SaaS B2B per la gestione dei processi operativi. Il management osserva che la retention a sei mesi e' passata dall'82% al 79% nell'ultimo anno. Tre punti percentuali sembrano un deterioramento moderato.

L'analista costruisce una tabella per coorte mensile di acquisizione:

| Coorte | M1 | M3 | M6 |
| --- | ---: | ---: | ---: |
| Gennaio | 94% | 88% | 84% |
| Febbraio | 93% | 87% | 83% |
| Marzo | 92% | 86% | 82% |
| Aprile | 91% | 84% | 79% |
| Maggio | 89% | 81% | 75% |
| Giugno | 88% | 79% | 72% |

Il deterioramento non e' uniforme. Le coorti piu' recenti stanno performando molto peggio.

Questo cambia completamente la diagnosi. La retention aggregata al 79% e' ancora sostenuta dai clienti storici, ma le nuove coorti mostrano un problema strutturale.

L'analista torna alla timeline operativa. A fine marzo l'azienda aveva modificato l'onboarding per ridurre il tempo medio di implementazione. Il nuovo processo aveva eliminato una sessione iniziale con un customer success manager per i clienti sotto i 20 utenti.

Segmentando le coorti per dimensione account, emerge il pattern:

- account con oltre 50 utenti: retention M6 quasi invariata;
- account tra 20 e 50 utenti: lieve peggioramento;
- account sotto 20 utenti: retention M6 scesa dall'81% al 66%.

Non basta per dire che il nuovo onboarding ha causato il calo, ma e' una spiegazione forte da investigare.

Le coorti rendono visibili proprio questi pattern che un dato aggregato puo' nascondere. La documentazione di Microsoft Databricks mostra la retention per coorte come confronto tra clienti che iniziano in periodi diversi e misura quanti restano attivi nei periodi successivi.[^1]

### Coorti di acquisizione e coorti comportamentali

Non tutte le coorti devono essere temporali.

Possiamo creare una coorte di utenti che:

- hanno completato l'onboarding entro tre giorni;
- hanno invitato almeno un collega nella prima settimana;
- hanno effettuato almeno cinque ordini nel primo mese;
- hanno attivato una funzione specifica;
- sono entrati attraverso una determinata campagna.

Queste sono coorti comportamentali.

In FlowDesk, l'analista scopre che gli account che creano almeno tre workflow nei primi sette giorni hanno retention M6 dell'88%, contro il 63% degli account che ne creano uno solo.

Questa associazione non prova causalita'. Potrebbe semplicemente indicare che i clienti piu' motivati utilizzano di piu' il prodotto e restano piu' a lungo.

Ma genera un'ipotesi operativa molto piu' utile della frase "dobbiamo migliorare la retention":

> Il raggiungimento di tre workflow entro la prima settimana potrebbe essere un indicatore di activation da testare e, forse, un comportamento da incentivare.

[^1]: Microsoft Learn, "Tipi di visualizzazione del dashboard di intelligenza artificiale/BI - Azure Databricks", https://learn.microsoft.com/it-it/azure/databricks/dashboards/manage/visualizations/types
