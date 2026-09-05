## 6.3 Funnel: localizzare dove si interrompe il percorso

Se segmenti e coorti ci dicono **chi** sta divergendo e **da quando**, il funnel aggiunge la terza coordinata: **dove** il percorso verso il valore si interrompe.

Un funnel non esiste naturalmente nel database. È una rappresentazione costruita dall'analista: visita → prodotto → carrello → checkout → pagamento, oppure signup → setup → prima azione di valore → utilizzo ricorrente. Google Analytics descrive la funnel exploration come uno strumento per visualizzare i passaggi con cui gli utenti completano un'attività e vedere in quali punti il percorso riesce o si interrompe.[^ga-funnel]

La parte importante è proprio questa natura progettata. Cambiare eventi, ordine, finestra temporale o unità di analisi significa cambiare il processo che stiamo misurando.

### QuickCart: il problema attribuito al marketing viveva nell'ultimo passaggio

**QuickCart**, marketplace alimentare, vede il conversion rate finale scendere dal **6,2% al 5,1%** in due mesi mentre il traffico cresce. Il management sospetta che le nuove campagne stiano portando visitatori meno qualificati.

Il funnel racconta una storia diversa:

| Step | Mese 1 | Mese 2 |
| --- | ---: | ---: |
| Sessioni | 1.000.000 | 1.080.000 |
| Visualizza almeno un prodotto | 71% | 70% |
| Aggiunge al carrello | 31% | 30% |
| Inizia checkout | 18% | 18% |
| Completa pagamento | 6,2% | 5,1% |

I passaggi iniziali sono quasi invariati. La perdita si concentra tra checkout e pagamento. Quando l'analista apre quel tratto per metodo di pagamento, il collo di bottiglia diventa ancora più preciso:

| Metodo | Mese 1 | Mese 2 |
| --- | ---: | ---: |
| Carta | 72% | 71% |
| PayPal | 76% | 75% |
| Wallet mobile | 74% | 52% |

La successiva indagine tecnica trova un errore di ritorno all'app dopo un nuovo flusso di autenticazione su alcune versioni Android. Il funnel non ha dimostrato da solo la causa, ma ha evitato che il team cercasse il problema nel marketing quando la rottura era molto più avanti nel percorso.

### Ogni passaggio porta con sé un denominatore

Su 1.000 sessioni, se 300 utenti iniziano il checkout e 210 completano il pagamento, la conversione complessiva sessione → acquisto è **21%**, mentre quella locale checkout → pagamento è **70%**. Le due percentuali sono entrambe corrette, ma descrivono fenomeni diversi.

Questa distinzione aiuta a separare un piccolo deterioramento distribuito su molti step da un collo di bottiglia concentrato. Per questo un funnel utile deve conservare sia la base iniziale sia il denominatore locale dei passaggi che stiamo interpretando.

Anche le regole di ingresso cambiano il significato. Google Analytics distingue funnel **aperti**, nei quali un utente può entrare da qualsiasi passaggio, e funnel **chiusi**, nei quali deve entrare dal primo; richiede inoltre che gli step rispettino la sequenza definita e consente di impostare vincoli temporali.[^ga-funnel] Sono scelte analitiche, non cosmetiche. Un percorso signup → feature → acquisto cambia se l'acquisto deve avvenire entro sette giorni, se un passaggio può essere saltato o se misuriamo per sessione, utente o account.

Il problema diventa ancora più serio quando l'identità attraversa dispositivi e sessioni. Un utente può scoprire il prodotto da mobile, registrarsi da laptop e acquistare da tablet. Se l'identità non viene ricostruita correttamente, il funnel trasforma un percorso unico in tre persone diverse. È il motivo per cui il lavoro del Capitolo 3 su grain e identity rimane una precondizione dell'analisi lifecycle.

### Non ogni percorso è un imbuto

Un SaaS enterprise può attraversare trial, demo, procurement, security review e setup in parallelo. Un marketplace può consentire acquisti senza carrello. Un prodotto collaborativo può produrre valore attraverso azioni distribuite fra più utenti dello stesso account. Forzare questi sistemi in una sequenza lineare rischia di rendere ordinato il grafico e sbagliato il modello del processo.

In questi casi il funnel può essere affiancato da path analysis, coorti per journey, segmentazione dei percorsi o time-to-event. Il criterio resta lo stesso: la rappresentazione deve aiutare a localizzare il punto in cui la traiettoria cambia, non costringere il comportamento dentro una forma comoda.

Una buona diagnosi di funnel deve permettere di completare questa frase:

> **Il risultato finale peggiora soprattutto perché la popolazione ______ perde utenti tra ______ e ______, nella finestra ______.**

A quel punto sappiamo dove guardare. La domanda successiva diventa più profonda: **quale passaggio rappresenta davvero il primo valore del prodotto, e quanti utenti riescono a raggiungerlo?**

[^ga-funnel]: Google Analytics Help, *Funnel exploration*: https://support.google.com/analytics/answer/9327974
