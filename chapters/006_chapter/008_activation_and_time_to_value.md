## 6.7 Activation e time-to-value: il primo momento in cui il prodotto mantiene la promessa

Registrarsi non significa aver trovato valore. Completare un onboarding non significa aver capito il prodotto. Aprire l'app tre volte non significa essersi attivati.

L'**activation** è il momento in cui un utente compie una o più azioni che indicano che ha sperimentato il valore centrale del prodotto. È una definizione analitica, non una proprietà universale.

Per un software di project management potrebbe essere la creazione del primo progetto condiviso con almeno due colleghi. Per un marketplace potrebbe essere il primo acquisto completato. Per una piattaforma di investimento potrebbe essere il primo versamento seguito da un investimento effettivo. Per un prodotto B2B complesso potrebbe essere una sequenza di eventi distribuita su più giorni.

Il punto è semplice: **l'evento di activation deve rappresentare valore, non attività**.

### Caso: CloudDesk e l'onboarding che sembrava migliorato

CloudDesk vende un software SaaS per piccoli studi professionali. Nel Q1 il team Product ridisegna l'onboarding per renderlo più breve. Il risultato iniziale è entusiasmante:

- completamento onboarding: dal 61% al 79%;
- tempo medio di onboarding: da 18 a 9 minuti;
- drop-off nella schermata di configurazione: -42%.

Il team dichiara il progetto un successo.

Tre mesi dopo, però, la retention a 90 giorni delle nuove coorti è scesa dal 72% al 64%.

L'analista rivede la definizione di activation. Fino a quel momento l'azienda considerava attivo chi completava tutte le schermate iniziali. Ma la feature che più correla con la retention a 90 giorni è un'altra: **creare almeno tre workflow reali e invitare almeno un collega entro sette giorni**.

Quando l'analista segmenta per questo evento, emerge che:

| Coorte | Completa onboarding | Raggiunge activation reale entro 7 giorni | Retention 90 giorni |
|---|---:|---:|---:|
| prima del redesign | 61% | 44% | 72% |
| dopo il redesign | 79% | 36% | 64% |

Il nuovo onboarding era più facile da completare, ma portava meno utenti al valore vero.

### Time-to-value

Una volta definita l'activation, diventa importante misurare il **time-to-value (TTV)**: quanto tempo passa tra l'ingresso dell'utente e il primo risultato significativo.

Possiamo definire, per esempio:

\[
TTV_i = t_{value,i} - t_{signup,i}
\]

Non è necessario che il valore sia istantaneo. In alcuni prodotti un TTV di 20 minuti è ottimo; in altri un TTV di tre settimane è normale. Ciò che conta è confrontarlo con il ciclo naturale del prodotto e con le coorti migliori.

Nel caso CloudDesk, gli utenti che raggiungono il valore entro 48 ore hanno una retention a 90 giorni del 81%. Quelli che lo raggiungono tra il giorno 3 e il giorno 7 hanno una retention del 68%. Oltre il giorno 7, la retention scende al 41%.

Questa relazione non dimostra automaticamente causalità: gli utenti più motivati potrebbero sia attivarsi prima sia restare più a lungo. Ma è un segnale operativo molto forte e genera ipotesi testabili.

Amplitude, nelle proprie analisi sul time-to-value, suggerisce di misurare non solo il tempo al primo valore, ma anche il tasso di raggiungimento del value moment, il tempo al secondo momento di valore e la retention per velocità di activation.[^amplitude-ttv]

### Da metrica a decisione

La domanda non è quindi “quante persone completano l'onboarding?”, ma:

> Quale esperienza precoce distingue gli utenti che trovano valore da quelli che abbandonano, e quanto rapidamente riusciamo a portarli lì?

È una domanda molto più difficile. Ed è anche molto più utile.

[^amplitude-ttv]: Amplitude, *Time to Value: The Key to Driving User Retention*, 2025, https://amplitude.com/blog/time-to-value-drives-user-retention
