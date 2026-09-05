## 9.16 Rollout e rollback: il test riduce l'incertezza, non elimina il rischio

Un esperimento positivo non chiude il problema. Cambia la domanda.

Durante il test chiedevamo se il trattamento produce un effetto utile rispetto al controllo. Durante il rollout chiediamo se quell'effetto e i guardrail restano accettabili quando aumentano **copertura, volume, eterogeneità e dipendenze operative**.

Il 20% non è sempre un piccolo 100%. A scala possono emergere limiti di database, code, API o payment provider; mercati e device rari possono finalmente avere abbastanza volume da mostrare failure; supply, inventory e network effects possono cambiare equilibrio; supporto, fraud review o warehouse possono assorbire un pilot e non il traffico completo.

Per questo un test valido produce una **ship candidate**, non una garanzia.

### Caso simulato/composito — PayWave

PayWave testa un nuovo flusso di autenticazione per pagamenti online. Sul 20% del traffico ottiene:

- payment completion: +1,8%;
- fraud loss: stabile;
- latency P95: +40 ms;
- chargeback: nessun movimento materialmente rilevante;
- Experiment Health Gate: **VALIDO**.

Il risultato supera anche la soglia economica del contract. Il rollout pianificato è:

| Fase | Exposure | Obiettivo principale |
|---|---:|---|
| 1 | 20% → 35% | confermare stabilità tecnica |
| 2 | 35% → 60% | ampliare coverage di mercati/provider |
| 3 | 60% → 85% | verificare scale risk e code operative |
| 4 | 85% → 100% | confermare guardrail a regime |

Al 60% il failure rate cresce di 0,6 punti percentuali su un circuito minoritario usato soprattutto in due mercati dell'Europa centrale. Il test iniziale non era necessariamente invalido: quel sottogruppo aveva poco volume e il problema raro non era emerso con chiarezza.

Il team fa rollback parziale al 35%, corregge l'integrazione e riprende il ramp solo dopo una nuova verifica. Il rollback non è il fallimento del metodo; è la **funzione di sicurezza prevista dal metodo**.

### Le soglie devono esistere prima dell'incidente

Un rollout governato collega ogni segnale a un'azione. Le metriche possono includere crash/error rate, payment failure, latency P95/P99, fraud/chargeback loss, support load, cancellation/refund, inventory o delivery failure.

Esempi:

- payment failure: rollback se delta > +0,30 pp per almeno due finestre;
- latency P99: rollback se delta > +150 ms;
- fraud loss: stop immediato sopra una soglia monetaria prestabilita;
- checkout error rate: rollback immediato se supera +5% relativo.

Il dettaglio non è il valore numerico universale — non esiste — ma il fatto che la soglia sia **predefinita, osservabile, con un owner e un'azione associata**.

### Non esiste soltanto rollback globale

L'architettura può permettere global rollback, partial rollback per mercato/provider/device, freeze dell'espansione o kill switch immediato. Queste opzioni dovrebbero essere progettate quando si costruisce la feature flag, non inventate durante l'incidente.

Se un trattamento rischioso non può essere disabilitato in tempi compatibili con il danno potenziale, questa limitazione appartiene già all'Experiment Contract.

### L'effetto può cambiare a regime

Durante il ramp conviene ricontrollare anche primary e guardrail business, pur sapendo che il rollout progressivo non è sempre un nuovo esperimento randomizzato puro. Un effetto può attenuarsi, amplificarsi, saturare o generare nuovi effetti indiretti quando quasi tutti sono trattati.

Nei marketplace e nei sistemi condivisi questo è particolarmente importante: il rollout è il momento in cui ci avviciniamo all'equilibrio che il buyer-level test non poteva rappresentare completamente.

Microsoft ExP ha documentato l'uso di experimentation e feature flag anche su cambi infrastrutturali, con regressioni che hanno portato a stop, investigazione, correzione e nuovo test prima del rollout completo.[^ms-infra]

### Stati decisionali più utili di win/loss

Un run può chiudersi come:

- **NO-SHIP**;
- **INCONCLUSIVE — serve altra evidenza**;
- **REDESIGN AND RETEST**;
- **SHIP CANDIDATE — rollout progressivo**;
- **SHIP WITH CONSTRAINTS — solo nello scope supportato dall'evidenza**.

Solo dopo ramp-up e osservazione prevista possiamo parlare di **SHIP COMPLETED**.

> **Il test decide se vale la pena aumentare l'esposizione. Il rollout verifica se il sistema continua a meritare quella decisione mentre l'esposizione aumenta.**

[^ms-infra]: Microsoft Research, *A/B Testing Infrastructure Changes at Microsoft ExP*: https://www.microsoft.com/en-us/research/articles/a-b-testing-infrastructure-changes-at-microsoft-exp/
