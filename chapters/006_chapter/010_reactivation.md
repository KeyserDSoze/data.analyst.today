## 6.9 Reactivation: quando un utente torna non significa che il problema sia risolto

Retention e churn vengono spesso trattati come stati definitivi: attivo oppure perso. Nella realtà molti prodotti hanno comportamenti intermittenti. Un utente può sparire per settimane, tornare, utilizzare intensamente il prodotto per pochi giorni e poi sparire di nuovo.

Per questo è utile distinguere almeno tre stati:

- attivo;
- inattivo o churnato secondo una soglia operativa;
- riattivato.

La **reactivation rate** misura la quota di utenti precedentemente inattivi che tornano a soddisfare la definizione di attività.

### Caso: FitNow e la campagna che “recupera” il 18% degli utenti

FitNow è un'app fitness in abbonamento. L'azienda considera churnato un utente che non apre l'app e non completa alcun workout per 30 giorni.

A marzo il CRM team lancia una campagna aggressiva verso 180.000 utenti inattivi: email, push notification e un mese premium gratuito.

Dopo due settimane la dashboard mostra un dato apparentemente ottimo:

- 32.400 utenti tornano nell'app;
- reactivation rate = 18%.

La campagna viene presentata come successo.

L'analista decide però di estendere la finestra di osservazione. Divide gli utenti riattivati in base alla profondità del ritorno:

| Comportamento dopo la riattivazione | Quota dei riattivati | Attivi anche dopo 60 giorni |
|---|---:|---:|
| una sola apertura | 37% | 4% |
| almeno un workout | 34% | 21% |
| almeno 3 workout in 14 giorni | 21% | 49% |
| nuovo piano settimanale completato | 8% | 68% |

Il 18% iniziale era tecnicamente corretto, ma mescolava ritorni quasi irrilevanti con veri recuperi di comportamento.

La domanda diventa quindi:

> cosa intendiamo davvero per utente riattivato?

### Reactivation non è acquisition

Un utente che torna porta con sé una storia. Ha già sperimentato il prodotto, ha avuto un motivo per allontanarsi e potrebbe avere aspettative diverse da un nuovo utente.

Per questo non conviene analizzare i riattivati come se fossero nuovi signup. È utile costruire coorti specifiche e misurare:

- tempo trascorso dall'ultima attività;
- motivo di churn, quando noto;
- canale che ha generato il ritorno;
- evento di reactivation;
- retention dopo il ritorno;
- revenue incrementale;
- costo dell'incentivo.

### Il costo nascosto della reactivation

Nel caso FitNow, il mese premium gratuito costa in media 5,40 € per utente riattivato. Se consideriamo tutti i 32.400 ritorni, il costo sembra accettabile.

Ma solo 9.396 utenti restano attivi dopo 60 giorni. Il costo per riattivazione duratura è quindi molto più alto.

Questo esempio mostra perché **un tasso di ritorno senza una finestra di persistenza può trasformare un evento momentaneo in un successo fittizio**.

### Una definizione operativa migliore

FitNow sostituisce infine la vecchia metrica con:

> utente riattivato = utente inattivo da almeno 30 giorni che completa almeno due workout in 14 giorni e rimane attivo nella finestra successiva di 30 giorni.

La percentuale scende dal 18% al 6,3%.

La metrica è meno spettacolare. Ma descrive meglio il fenomeno che interessa davvero al business.
