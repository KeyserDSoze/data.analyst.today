## 4.11 Osservazioni influenti: quando un caso reale domina la storia

Nel Capitolo 3 abbiamo chiesto se un valore estremo rappresentasse un errore, un caso impossibile o un evento raro ma reale. Se il record ha superato quella verifica, nell'EDA nasce una domanda diversa: **quanto dipende il nostro pattern da quella singola osservazione o da quel piccolo gruppo di casi?**

Un valore può essere perfettamente valido e influenzare enormemente media, deviazione standard, retta di regressione o correlazione. Non abbiamo quindi motivo di cancellarlo, ma abbiamo motivo di capire se il linguaggio con cui descriviamo l'intera popolazione dipenda quasi completamente da lui.

Consideriamo una società SaaS con `ACV medio = €21.600` e `ACV mediano = €12.900`. Nel periodo entra un contratto enterprise da **€186.000**, verificato e reale: un gruppo internazionale consolida 14 società in un unico accordo. Non esiste alcuna giustificazione per rimuoverlo dai KPI economici.

L'analista esegue però una sensitivity analysis descrittiva:

```text
ACV medio con contratto enterprise: €21.600
ACV medio senza quel contratto:     €18.900
ACV mediano:                        €12.900
```

La differenza rende la storia più precisa. Il valore economico medio del portafoglio è realmente aumentato grazie a un nuovo tipo di contratto, mentre l'esperienza del cliente centrale è cambiata molto meno. Il punto estremo non “falsa” la media; ci dice che **la crescita della media è concentrata in una parte particolare della distribuzione**.

## Sensitivity analysis significa misurare la dipendenza della conclusione

Una pratica utile è ripetere la statistica principale in versioni plausibili: dataset completo, mediana invece della media, analisi per segmento e, quando serve, risultato senza il punto o il gruppo più influente. Non facciamo questo per scegliere la versione che produce la headline preferita, ma per capire quanto la conclusione sia robusta.

Se una correlazione passa da `0,74` a `0,18` quando separiamo un singolo punto reale dal resto, dobbiamo conservare entrambe le informazioni. Quel punto può essere economicamente importantissimo, ma la frase “esiste una forte relazione generale” non è più una buona descrizione dell'intera popolazione.

Outlier e punto influente, inoltre, non sono sinonimi. Un'osservazione può essere estrema in una variabile e modificare poco la relazione che stiamo studiando; un altro punto può avere un valore `X` molto lontano dal resto e determinare quasi interamente una retta pur non sembrando eccezionale in `Y`. Il quartetto di Anscombe rende questo rischio visibile.

Per questo box plot, regole IQR e z-score — che vedremo più avanti — non devono essere letti come istruzioni di cancellazione. Segnalano una posizione relativa nella distribuzione; non stabiliscono se il record sia corretto, se appartenga a un nuovo segmento o se abbia valore economico.

Una comunicazione rigorosa può quindi suonare così:

> L'AOV medio è €128, ma è fortemente influenzato da una piccola quota di ordini B2B ad alto valore. La mediana è €64 e, in una sensitivity analysis che separa il top 1%, la media del resto scende a €91. Gli ordini estremi sono validi e rimangono inclusi nei KPI economici.

La frase non nasconde né il totale né la fragilità del riepilogo. Mostra che il pattern cambia a seconda della parte di business che stiamo cercando di descrivere.

Questa disciplina prepara il caso successivo. Quando una correlazione molto alta spinge verso una riallocazione importante di budget, la prima responsabilità dell'EDA è chiedere **quanto quella correlazione sopravviva quando guardiamo punti, tempo, composizione e metrica economica completa**.

> **Un valore reale non va cancellato perché rende la statistica scomoda. Ma una statistica dominata da pochi casi non va raccontata come se descrivesse uniformemente tutta la popolazione.**
