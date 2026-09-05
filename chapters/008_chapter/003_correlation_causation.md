## 8.2 Correlazione, previsione e causalità: tre domande diverse

Una relazione osservata può essere molto utile senza essere causale. Nel lavoro dell'analista convivono infatti tre obiettivi che usano spesso gli stessi dati ma chiedono cose differenti: descrivere quali variabili si muovono insieme, prevedere quali segnali anticipano un outcome e decidere che cosa cambierebbe se intervenissimo su una specifica esposizione. Il problema nasce quando una risposta valida per uno di questi obiettivi viene trasferita agli altri senza un nuovo argomento.

### Caso simulato/composito — Più chiamate al supporto, più churn

Una telco osserva:

| Clienti | Churn 60 giorni |
|---|---:|
| almeno 3 chiamate al supporto | 22% |
| meno di 3 chiamate | 6% |

Il numero di chiamate è un ottimo **segnale di rischio**. Potrebbe entrare in un modello predittivo e aiutare Customer Success a localizzare account fragili. Sarebbe però pericoloso trasformare la stessa evidenza in una policy del tipo “riduciamo le chiamate consentite, così ridurremo il churn”. Un meccanismo molto più plausibile è:

```text
problema di servizio -> più chiamate
problema di servizio -> churn
```

Il supporto potrebbe persino attenuare il churn rispetto a ciò che sarebbe avvenuto senza assistenza. La stessa variabile può quindi essere un forte predittore, una spiegazione causale debole e una pessima leva di intervento.

Quando `X` e `Y` sono associati, la freccia `X -> Y` è solo una delle storie possibili. Potremmo avere `Y -> X`, una causa comune `Z` che influenza entrambe, oppure un processo di selezione che crea l'associazione nel campione osservato. Più percorsi possono coesistere. Il coefficiente di correlazione misura la relazione nei dati; non contiene la direzione delle frecce.

La precedenza temporale aiuta, ma non risolve da sola il problema. Se il deterioramento del cliente inizia a gennaio, una chiamata di retention arriva a febbraio e il churn avviene a marzo, la chiamata precede l'outcome finale ma può essere stata provocata da un rischio già in corso. Il tempo esclude storie impossibili; non costruisce automaticamente il controfattuale.

### Dal pattern alla leva

Un retailer scopre che i clienti che utilizzano almeno quattro coupon l'anno hanno LTV superiore del **31%**. L'EDA ha trovato un pattern utile e un predictive model potrebbe sfruttare `coupon_usage`. Ma il dato è compatibile con storie molto diverse: i coupon potrebbero aumentare davvero frequenza e retention; i clienti loyalty potrebbero riceverne di più; chi compra spesso ha più occasioni di usarli; il marketing potrebbe inviare più offerte proprio agli utenti ad alto valore. Decidere di **inviare più coupon** richiede quindi una causal question separata.

Una prova mentale aiuta a riconoscere il salto logico. Trasformiamo “gli utenti con tre workflow hanno retention più alta” in “se inducissimo utenti comparabili a creare tre workflow, la loro retention aumenterebbe”. La seconda frase non è una parafrasi della prima: descrive un intervento e pretende un controfattuale.

Per mantenere calibrato il linguaggio useremo una **claim ladder**:

| Livello | Claim consentito |
|---|---|
| Descrittivo | `X` e `Y` sono associati. |
| Predittivo | `X` migliora la previsione di `Y` fuori campione. |
| Causale condizionato | Sotto queste assunzioni e con questo design, la stima è compatibile con un effetto causale di `X` su `Y`. |
| Decisionale | Per questa popolazione e questo trattamento, l'effetto stimato è abbastanza grande e preciso da giustificare questa azione. |

Non ogni analisi deve arrivare all'ultimo livello. Un'associazione può essere già preziosa per diagnosticare o prevedere; diventa pericolosa soltanto quando le chiediamo di rispondere a una domanda di intervento che il design non sostiene.

Il passaggio successivo è quindi capire **perché i gruppi che stiamo confrontando erano diversi prima del trattamento**. È il problema del confounding.
