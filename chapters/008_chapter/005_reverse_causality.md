## 8.4 Causalità inversa: quando l'effetto sembra la causa

Una relazione può apparire plausibile anche quando la direzione causale è opposta a quella intuita inizialmente.

### Caso - Più sconti, più churn

Un'azienda SaaS osserva che i clienti che ricevono sconti di retention hanno un churn del 27%, contro il 9% dei clienti che non ricevono sconti.

La prima lettura potrebbe essere:

> "Gli sconti fanno aumentare il churn."

Ma gli sconti vengono concessi proprio ai clienti che hanno manifestato intenzione di cancellare, ridotto l'utilizzo o aperto ticket critici.

La direzione reale del processo è più simile a:

`rischio churn -> concessione sconto`

Non necessariamente:

`sconto -> churn`

Il trattamento è una risposta al rischio.

### Caso - Più medici, più mortalità ospedaliera

Supponiamo che un network sanitario osservi che gli ospedali con più specialisti per paziente hanno mortalità più alta.

Una conclusione ingenua sarebbe che una maggiore intensità clinica peggiori gli outcome.

Ma gli ospedali con casi più gravi ricevono più personale specializzato. La gravità del paziente influenza sia l'intensità delle cure sia la mortalità.

Nel business il meccanismo è diffusissimo:

- i clienti più problematici ricevono più assistenza;
- i negozi peggiori ricevono più visite del management;
- i lead più difficili ricevono più follow-up;
- gli SKU più instabili ricevono più interventi sul prezzo;
- i sistemi più fragili ricevono più manutenzione.

Se osserviamo solo intervento e outcome, l'intervento può sembrare associato a risultati peggiori proprio perché viene applicato dove il rischio era già maggiore.

### Il tempo aiuta a ragionare, ma non risolve tutto

Una causa deve precedere il proprio effetto. Ordinare correttamente gli eventi nel tempo è quindi essenziale.

Tuttavia la precedenza temporale non basta a dimostrare causalità.

Se un cliente riduce i login a gennaio, riceve uno sconto a febbraio e cancella a marzo, lo sconto precede il churn ma è stato generato da un deterioramento iniziato prima.

### Variabili laggate e finestre temporali

Per evitare errori grossolani conviene distinguere chiaramente:

- covariate pre-trattamento;
- momento del trattamento;
- outcome successivi;
- variabili che possono essere conseguenze del trattamento.

Nel caso SaaS potremmo definire:

- utilizzo nei 60 giorni precedenti;
- ticket aperti prima dell'offerta;
- sconto concesso nel giorno `t`;
- churn entro 90 giorni dopo `t`.

Questa struttura temporale non elimina da sola il confounding, ma impedisce di usare accidentalmente informazioni future per spiegare il passato.

> **Quando un'azienda interviene in risposta a un rischio, il rischio stesso può far sembrare inefficace o dannoso l'intervento.**
