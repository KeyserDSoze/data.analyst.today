## 6.3 Funnel: dove perdiamo le persone

Un funnel descrive una sequenza di passaggi attraverso cui un utente deve transitare per arrivare a un risultato.

Nel commercio elettronico potrebbe essere:

1. visita;
2. visualizzazione prodotto;
3. aggiunta al carrello;
4. checkout iniziato;
5. pagamento completato.

In un SaaS potrebbe essere:

1. registrazione;
2. onboarding iniziato;
3. onboarding completato;
4. prima azione di valore;
5. utilizzo ricorrente;
6. rinnovo.

L'errore piu' comune e' guardare solo il tasso finale.

Immaginiamo QuickCart, un marketplace alimentare. Il conversion rate finale passa dal 6,2% al 5,1% in due mesi. Il team marketing pensa a un problema di qualita' del traffico.

L'analista ricostruisce il funnel:

| Step | Mese 1 | Mese 2 |
| --- | ---: | ---: |
| Sessioni | 1.000.000 | 1.080.000 |
| Visualizza prodotto | 71% | 70% |
| Aggiunge al carrello | 31% | 30% |
| Inizia checkout | 18% | 18% |
| Completa pagamento | 6,2% | 5,1% |

I primi passaggi sono quasi invariati. Il problema e' tra checkout e pagamento.

Segmentando per metodo di pagamento:

| Metodo | Completion M1 | Completion M2 |
| --- | ---: | ---: |
| Carta | 72% | 71% |
| PayPal | 76% | 75% |
| Wallet mobile | 74% | 52% |

Il deterioramento e' quasi tutto concentrato sul wallet mobile.

Tre settimane prima, il provider di pagamento aveva introdotto un nuovo flusso di autenticazione. Il team tecnico scopre che su alcuni dispositivi Android la schermata di conferma non torna correttamente all'app.

Il marketing non era il problema.

### Il denominatore cambia a ogni step

In un funnel ogni conversione locale usa come base lo step precedente. Questo permette di distinguere dove avviene davvero la perdita.

Se 100.000 utenti arrivano al checkout e 70.000 completano il pagamento, la conversione checkout-to-purchase e' 70%. Non va confusa con la conversione session-to-purchase.

Questo sembra ovvio, ma nei dashboard reali si mescolano spesso percentuali con denominatori diversi.

### Funnel rigido e funnel flessibile

Un altro punto importante riguarda l'ordine degli eventi.

Un funnel puo' richiedere che gli step avvengano in sequenza stretta oppure accettare percorsi piu' flessibili. Un utente puo' visitare piu' prodotti, tornare dopo due giorni, aggiungere al carrello da un altro dispositivo e infine comprare.

La definizione del funnel e' quindi una scelta analitica, non una proprieta' naturale del dataset.

Prima di calcolarlo bisogna definire:

- identita' dell'utente;
- ordine richiesto degli eventi;
- finestra temporale;
- ripetizioni ammesse;
- sessione o utente come denominatore;
- evento che rappresenta davvero la conversione.

Il funnel diventa utile quando ci permette di passare da "convertiamo meno" a "perdiamo utenti precisamente qui".
