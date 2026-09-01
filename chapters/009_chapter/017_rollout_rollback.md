## 9.16 Rollout e rollback: il test riduce l'incertezza, non elimina il rischio

Un risultato sperimentale positivo non chiude il problema. Cambia il tipo di problema.

Durante l'esperimento chiedevamo:

> **il trattamento produce un effetto utile rispetto al controllo?**

Durante il rollout chiediamo invece:

> **l'effetto e i guardrail restano accettabili quando aumentano copertura, volume, eterogeneità e dipendenze operative?**

Sono domande diverse.

Un test può essere perfettamente valido e un rollout può comunque fallire.

### Perché il 20% non è sempre un piccolo 100%

Aumentare l'esposizione può cambiare il sistema stesso.

Possiamo incontrare almeno quattro rischi.

**Scale risk**  
Database, API, code, modelli e sistemi di pagamento possono comportarsi diversamente sotto carico elevato.

**Coverage risk**  
Nel test alcuni paesi, device, payment provider o customer segment possono avere troppo poco volume per mostrare problemi rari.

**Equilibrium/interference risk**  
In marketplace, sistemi di ranking o reti collaborative, l'effetto può cambiare quando quasi tutti ricevono il trattamento perché cambiano congestione, offerta e comportamento degli altri attori.

**Operational risk**  
Processi di supporto, fraud review, warehouse o Customer Success possono assorbire un pilot ma non il traffico completo.

Il rollout progressivo serve a osservare questi rischi prima che diventino irreversibili o costosi.

### Caso simulato/composito — PayWave

PayWave testa un nuovo flusso di autenticazione per pagamenti online.

Nel test sul 20% del traffico:

- payment completion: +1,8%;
- fraud loss: stabile;
- latency P95: +40 ms;
- chargeback: nessun movimento materialmente rilevante;
- Experiment Health Gate: **VALIDO**.

Il risultato supera anche la soglia economica definita nell'Experiment Contract.

La decisione è quindi **SHIP CANDIDATE**, non "100% immediato".

Il rollout previsto è:

| Fase | Exposure | Obiettivo principale |
|---|---:|---|
| 1 | 20% → 35% | confermare stabilità tecnica |
| 2 | 35% → 60% | ampliare coverage di mercati/provider |
| 3 | 60% → 85% | verificare scale risk e code operative |
| 4 | 85% → 100% | confermare guardrail a regime |

Al 60% il failure rate cresce di 0,6 punti percentuali su un circuito di pagamento minoritario usato soprattutto in due mercati dell'Europa centrale.

Il test iniziale non era necessariamente sbagliato: quel sottogruppo aveva volume insufficiente perché un problema raro emergesse con chiarezza.

Il team esegue un rollback parziale al 35%, corregge l'integrazione e riprende il ramp-up solo dopo un nuovo controllo.

### Rollback non significa fallimento analitico

Se il piano prevedeva criteri di rollback e il sistema li applica correttamente, il processo ha funzionato.

Un buon sistema di experimentation non promette che ogni ship candidate sarà perfetto a scala. Promette che:

- il rischio residuo è esplicito;
- viene aumentata l'esposizione in modo controllato;
- i segnali critici vengono osservati;
- esiste una strada rapida per tornare indietro.

Questo è molto diverso dal rollout "speriamo vada bene".

### Rollback criteria: devono essere scritti prima

Le soglie dipendono dal prodotto, ma possono riguardare:

- crash/error rate;
- payment failure;
- latency P95/P99;
- fraud o chargeback loss;
- customer support load;
- cancellation/refund;
- inventory o delivery failures;
- guardrail economiche;
- incident severity.

Esempio:

- payment failure: rollback se delta > +0,30 pp per almeno due finestre di monitoraggio;
- latency P99: rollback se delta > +150 ms;
- fraud loss: stop immediato sopra una soglia monetaria prestabilita;
- checkout error rate: rollback immediato se supera +5% relativo.

Il dettaglio importante non è la soglia specifica. È che la soglia sia **predefinita, osservabile e associata a un'azione**.

### Global rollback e partial rollback

Non tutti gli incidenti richiedono lo stesso intervento.

Possiamo distinguere:

- **global rollback**: il trattamento viene disabilitato ovunque;
- **partial rollback**: si torna indietro solo su un mercato, provider, device o segmento;
- **freeze**: si blocca l'espansione mantenendo l'attuale percentuale;
- **kill switch**: disabilitazione immediata per incidenti critici.

Queste opzioni dovrebbero essere compatibili con l'architettura del prodotto. Se tecnicamente non possiamo fare rollback in tempi compatibili con il rischio, quella limitazione fa parte del design sperimentale.

### Effetto a test e effetto a regime

Un'altra domanda importante è se l'effetto stimato nel test sia trasferibile al rollout completo.

Un trattamento può avere:

- effetto stabile;
- effetto attenuato a scala;
- effetto amplificato;
- nuovi effetti indiretti;
- saturazione.

Per questo durante il ramp-up non basta monitorare solo error rate e latency. Conviene ricontrollare anche primary metric e guardrail business, sapendo però che il rollout non è più necessariamente un esperimento randomizzato puro.

### Caso reale documentato — Microsoft ExP

Microsoft ha documentato l'uso dell'experimentation anche per modifiche infrastrutturali e backend. In casi reali, regressioni osservate durante i test hanno portato a stop, investigazione, correzione e nuova sperimentazione prima di procedere. La lezione è utile anche fuori dall'infrastruttura: **la decisione di ship deve essere reversibile quando resta rischio operativo materiale**.

### Il passaggio di stato

Una terminologia semplice aiuta a evitare il falso binario "win/loss".

Un esperimento può chiudersi come:

- **NO-SHIP**;
- **INCONCLUSIVE — serve altra evidenza**;
- **REDESIGN AND RETEST**;
- **SHIP CANDIDATE — rollout progressivo**;
- **SHIP WITH CONSTRAINTS — solo per popolazioni/mercati supportati dall'evidenza**.

Solo dopo il ramp-up e il periodo di osservazione previsto possiamo parlare di **SHIP COMPLETED**.

> **Il test decide se vale la pena aumentare l'esposizione. Il rollout verifica se il sistema continua a meritare quella decisione quando l'esposizione aumenta.**

### Fonte pubblica

- Microsoft Experimentation Platform, *A/B Testing Infrastructure Changes at Microsoft ExP*: https://www.microsoft.com/en-us/research/articles/a-b-testing-infrastructure-changes-at-microsoft-exp/
