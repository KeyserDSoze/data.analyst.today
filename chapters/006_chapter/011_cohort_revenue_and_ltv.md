## 6.10 Cohort value e LTV: seguire il valore, non solo la presenza

Retention e churn descrivono persistenza e perdita, ma due coorti con la stessa retention possono produrre economics molto diversi. Per questo il lifecycle deve essere letto anche come **accumulazione di valore nel tempo**.

Prima di costruire un modello sofisticato di LTV, spesso è più utile osservare quanto revenue, margine o contribution profit le coorti abbiano realmente prodotto a D30, D90, D180 e oltre. Solo dopo ha senso separare ciò che è già osservato da ciò che stiamo prevedendo.

### ModaLab: il canale più costoso all'inizio crea più valore dopo

**ModaLab**, e-commerce fashion, confronta paid social e referral:

| Canale | CAC medio | Primo ordine medio |
| --- | ---: | ---: |
| Paid social | 41 € | 72 € |
| Referral | 23 € | 69 € |

Guardando soltanto CAC e primo ordine, referral sembra nettamente migliore. Le coorti raccontano però una traiettoria differente:

| Canale | Revenue D30 | Revenue D90 | Revenue D180 |
| --- | ---: | ---: | ---: |
| Paid social | 78 € | 146 € | 238 € |
| Referral | 73 € | 112 € | 151 € |

Paid social costa di più all'acquisizione ma genera più acquisti nei mesi successivi. Anche passando dalla revenue al margine lordo cumulato, a 180 giorni restano **91 €** per paid social contro **63 €** per referral.

La domanda quindi non è più “quale canale ha il CAC più basso?”, ma **quanto capitale siamo disposti a investire oggi per una coorte che restituisce più margine nel tempo?**

### Valore osservato e LTV previsto appartengono a due livelli di evidenza diversi

L'**observed cohort value** è ciò che la coorte ha realmente prodotto fino a un certo orizzonte. Il **predicted LTV** è invece una stima di ciò che dovrebbe produrre oltre la parte già osservata. Il primo è descrittivo; il secondo incorpora un modello e assunzioni sul futuro.

Confonderli fa sembrare un forecast un fatto già avvenuto. Per questo un numero di LTV dovrebbe dichiarare quanto del lifecycle sia osservato e quanto previsto.

Anche la misura economica deve essere esplicita. Una coorte può generare 300 € di revenue e contemporaneamente avere resi elevati, fulfilment costoso, incentivi, fee di pagamento, supporto intenso o sconti aggressivi. In ModaLab due coorti possono produrre entrambe 220 € di revenue a 180 giorni e avere economics molto differenti se una ha return rate **9%** e margine lordo **48%**, mentre l'altra ha return rate **24%**, margine **36%** e forte uso di coupon.

“LTV 220 €” senza specificare se parliamo di revenue, gross margin o contribution margin nasconde proprio ciò che dovrebbe guidare la decisione.

### La maturità deve essere allineata anche quando parliamo di denaro

Una coorte acquisita un mese fa ha avuto un mese per generare valore; una di un anno fa ne ha avuti dodici. Confrontare `lifetime_revenue` fino a oggi senza allineare l'età ripete lo stesso errore visto nella retention. D30 va confrontato con D30, M3 con M3, M12 con M12.

Quando le coorti recenti non sono mature, il valore futuro può essere previsto usando pattern di coorti più vecchie, modelli di retention/survival, frequenza di acquisto, margine atteso o scenari. Ma la qualità del forecast dipende dalla stabilità del processo. Cambi di pricing, prodotto, mix di acquisizione o retention possono rendere il passato poco trasferibile alle nuove coorti.

### Il payback può essere più decisionale del “valore a vita”

In molti business la domanda operativa è quando recuperiamo il CAC. Se una coorte con CAC di 80 € produce contribution margin cumulato di **22 € a D30**, **51 € a D90** e **86 € a D180**, il payback avviene fra tre e sei mesi.

Una seconda coorte potrebbe avere un LTV finale maggiore ma impiegare diciotto mesi a recuperare il costo di acquisizione. Per un'azienda con vincoli di cassa, le due strategie non sono equivalenti.

Anche rapporti eleganti come `LTV/CAC` richiedono quindi definizioni compatibili: LTV su revenue o margine, CAC completo o solo media spend, valore osservato o previsto, orizzonte, media o marginalità e soprattutto stessa coorte. Il rapporto non può correggere incoerenze fra numeratore e denominatore.

Una Lifecycle Diagnostic Map deve così tenere insieme tre piani: **presenza**, perché il cliente rimane o torna; **comportamento**, perché continua a ottenere o creare valore; **economics**, perché quella relazione produce un certo valore nel tempo.

Prima di presentare un LTV dovremmo poter completare:

> **Stiamo stimando ______ per la coorte ______, su un orizzonte di ______, usando ______ come misura economica; la parte fino a ______ è osservata, la parte successiva è prevista.**

Questa distinzione prepara l'ultimo passaggio del capitolo: anche sapere chi è economicamente a rischio non significa ancora sapere chi possiamo realmente influenzare.