## 4.11 Osservazioni influenti: quanto dipende il pattern da pochi casi?

Nel Capitolo 3 abbiamo affrontato gli outlier dal punto di vista della **data readiness**: un valore estremo è un errore, un caso impossibile oppure un evento raro ma reale?

Qui la domanda è diversa.

Supponiamo che il dato sia valido.

Vogliamo sapere:

> **quanto le nostre statistiche e relazioni dipendono da poche osservazioni estreme?**

Un valore può essere perfettamente reale e avere comunque un'influenza enorme sulla media, sulla deviazione standard o sulla correlazione.

### Caso simulato/composito — Il contratto enterprise che cambia la media

Una società SaaS ha questi dati annuali:

```text
ACV medio:   €21.600
ACV mediano: €12.900
```

Nel periodo compare un nuovo contratto da **€186.000**.

Il contratto è stato verificato ed è reale: un gruppo internazionale consolida 14 società in un unico accordo.

Non c'è nessun motivo di cancellarlo.

Ma l'analista vuole capire che ruolo svolge nella statistica:

```text
ACV medio con contratto enterprise:    €21.600
ACV medio senza quel contratto:        €18.900
mediana:                               €12.900
```

La differenza è informazione.

Il valore medio del business è realmente aumentato grazie al nuovo tipo di contratto, ma la distribuzione del cliente "tipico" è cambiata molto meno.

### Sensitivity analysis descrittiva

Una pratica utile è calcolare la statistica principale in più versioni plausibili:

- dataset completo;
- senza il punto più influente;
- mediana invece della media;
- statistiche per segmento;
- eventualmente una media troncata, quando ha una giustificazione.

Non per scegliere la versione che ci piace.

Per capire **quanto è robusta la storia**.

Se la correlazione passa da `0,74` a `0,18` togliendo un singolo punto reale, dobbiamo dirlo. Quel punto può essere essenziale per il business, ma la frase "esiste una forte relazione generale" diventa difficile da difendere.

### Outlier e punto influente non sono sinonimi

Un'osservazione può essere estrema in una singola variabile e avere poca influenza sulla relazione che studiamo.

Al contrario, un punto non particolarmente estremo in Y può avere un valore X molto distante dal resto e determinare quasi completamente una retta di regressione o una correlazione.

Il quartetto di Anscombe mostra precisamente questo tipo di rischio.

Per l'EDA la domanda non è soltanto:

> quanto è lontano questo valore?

ma:

> **che cosa succede alla conclusione se questo valore non domina più il riepilogo?**

### Box plot e z-score non sono ordini di cancellazione

Nelle sezioni successive vedremo strumenti che possono segnalare osservazioni lontane dalla massa centrale.

Una soglia IQR o uno z-score elevato descrivono una posizione relativa nella distribuzione.

Non stabiliscono:

- se il record sia corretto;
- se debba essere escluso;
- se rappresenti un nuovo segmento;
- se sia economicamente irrilevante.

Queste decisioni richiedono il contesto già costruito nella Data Readiness Review.

### Comunicare la sensibilità

Una frase rigorosa può essere:

> L'AOV medio è €128, ma è fortemente influenzato da una piccola quota di ordini B2B ad alto valore. La mediana è €64 e, escludendo il top 1% per una sensitivity analysis, la media scende a €91. Gli ordini estremi sono validi e restano inclusi nei KPI economici.

Qui non nascondiamo né il totale né la distribuzione.

### Regola operativa

Quando un insight dipende da osservazioni estreme:

1. verifica che siano già state validate dal punto di vista del dato;
2. misura quanto influenzano il risultato;
3. osserva statistiche robuste o segmentate;
4. non rimuoverle senza una regola sostantiva;
5. comunica la sensibilità quando cambia l'interpretazione.

> **Un valore reale non deve essere cancellato perché rende la statistica scomoda. Ma una statistica fragile non deve essere presentata come se descrivesse uniformemente tutta la popolazione.**