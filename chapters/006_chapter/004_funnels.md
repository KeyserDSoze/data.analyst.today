## 6.3 Funnel: localizzare dove si interrompe il percorso

Se la coorte ci aiuta a capire **quando** nasce una differenza, il funnel ci aiuta a capire **dove** si manifesta lungo una sequenza di eventi.

Un funnel rappresenta un percorso definito dall'analista: visita → prodotto → carrello → checkout → pagamento, oppure signup → setup → prima azione di valore → utilizzo ricorrente.

Google Analytics descrive la funnel exploration come un modo per visualizzare i passaggi che gli utenti compiono per completare un'attività e individuare i punti in cui il percorso riesce o si interrompe.[^ga-funnel]

La parola importante è **definito**. Il funnel non esiste naturalmente nel database. È una rappresentazione del processo che decidiamo di misurare.

### Caso simulato/composito: QuickCart e il problema attribuito al marketing

**QuickCart** è un marketplace alimentare. Il conversion rate finale scende dal 6,2% al 5,1% in due mesi, mentre il traffico cresce.

La prima ipotesi del management è che le nuove campagne stiano portando visitatori meno qualificati.

L'analista ricostruisce il percorso:

| Step | Mese 1 | Mese 2 |
| --- | ---: | ---: |
| Sessioni | 1.000.000 | 1.080.000 |
| Visualizza almeno un prodotto | 71% | 70% |
| Aggiunge al carrello | 31% | 30% |
| Inizia checkout | 18% | 18% |
| Completa pagamento | 6,2% | 5,1% |

I primi passaggi sono quasi invariati. La perdita si concentra nell'ultimo tratto.

Guardando il completion rate tra checkout iniziato e pagamento completato per metodo:

| Metodo | Mese 1 | Mese 2 |
| --- | ---: | ---: |
| Carta | 72% | 71% |
| PayPal | 76% | 75% |
| Wallet mobile | 74% | 52% |

Il problema non appare più come “traffico peggiore”. È localizzato nel wallet mobile.

La successiva indagine tecnica identifica un errore di ritorno all'app dopo un nuovo flusso di autenticazione su alcune versioni Android.

Il funnel non ha dimostrato da solo la causa. Ha evitato che il team cercasse la causa nel punto sbagliato del sistema.

### Conversione globale e conversione locale

Ogni step ha due letture diverse.

Se su 1.000 sessioni:

- 300 utenti iniziano il checkout;
- 210 completano il pagamento;

la conversione complessiva sessione → acquisto è 21%, mentre la conversione locale checkout → pagamento è 70%.

Entrambe sono corrette. Rispondono a domande diverse.

Questo è essenziale perché un peggioramento finale può essere prodotto da:

- una piccola perdita distribuita su molti step;
- un singolo collo di bottiglia;
- un cambiamento di mix tra percorsi differenti.

Una buona analisi mostra quindi sia il denominatore iniziale sia il denominatore locale.

### Funnel aperto, chiuso e ordine degli eventi

La documentazione di Google Analytics distingue tra funnel **chiusi**, nei quali l'utente deve entrare dal primo step, e funnel **aperti**, nei quali può entrare da passaggi successivi. Permette inoltre di richiedere che uno step segua direttamente o indirettamente il precedente e di imporre una finestra temporale.[^ga-funnel]

Queste non sono opzioni cosmetiche.

Un funnel “signup → prova feature → acquisto” produce risultati diversi se:

- l'acquisto deve avvenire entro sette giorni oppure in qualunque momento;
- gli utenti possono saltare uno step;
- un utente può completare lo stesso percorso più volte;
- il percorso viene misurato per sessione, utente o account.

### Il problema dell'identità

Molti funnel digitali attraversano dispositivi e sessioni.

Un utente può:

1. scoprire il prodotto da mobile;
2. registrarsi da laptop;
3. ricevere una email;
4. completare l'acquisto da tablet.

Se l'identità non viene ricostruita correttamente, il percorso può sembrare composto da tre persone diverse.

Questo collega il funnel direttamente al Capitolo 3: prima di interpretare il drop-off dobbiamo sapere se gli eventi appartengono davvero alla stessa unità analitica.

### Il funnel può essere troppo semplice

Non tutti i processi sono lineari.

Un SaaS enterprise può avere percorsi con trial, demo, procurement, security review e setup paralleli. Un marketplace può consentire acquisti senza carrello. Un prodotto collaborativo può creare valore attraverso azioni di più utenti dello stesso account.

Forzare tutto in una sequenza unica può cancellare proprio i comportamenti che contano.

In questi casi è utile affiancare al funnel:

- path analysis;
- segmentazione dei percorsi;
- time-to-event;
- coorti per tipo di journey.

### La domanda operativa

Un funnel ben costruito deve permettere di completare questa frase:

> Il risultato finale peggiora soprattutto perché la popolazione ______ perde utenti tra ______ e ______, nella finestra ______.

Se non riusciamo a farlo, probabilmente abbiamo ancora soltanto una visualizzazione del funnel, non una diagnosi.

[^ga-funnel]: Google Analytics Help, “Funnel exploration”, https://support.google.com/analytics/answer/9327974
