## 9.16 Rollout e rollback: un esperimento vinto non significa rollout al 100%

Un errore frequente è trattare il risultato positivo di un A/B test come un interruttore binario:

- test vinto;
- rollout al 100%;
- progetto chiuso.

Nel mondo reale, il rollout è una seconda fase di rischio.

Un esperimento può essere valido su una popolazione limitata e produrre problemi quando viene esteso a mercati, device, utenti o volumi non rappresentati sufficientemente nel test.

### Caso simulato — PayWave

PayWave testa un nuovo flusso di autenticazione per i pagamenti online.

Nel test su 20% del traffico:

- completion rate: +1,8%;
- fraud rate: stabile;
- latency: +40 ms;
- chargeback: nessun movimento rilevante.

Il risultato è positivo.

Il team decide però di non passare direttamente al 100%.

Piano di rollout:

1. 20% → 35%;
2. 35% → 60%;
3. 60% → 85%;
4. 85% → 100%.

A ogni fase vengono controllati:

- error rate;
- latency P95/P99;
- fraud;
- chargeback;
- conversione;
- distribuzione geografica;
- failure per circuito di pagamento.

Al 60% emerge un aumento del failure rate solo su un circuito minoritario usato soprattutto in due mercati dell'Europa centrale.

Il problema non era visibile nel test iniziale perché quel segmento aveva poco volume.

Il rollout viene riportato al 35%, la compatibilità viene corretta e il test riparte.

### Rollout non è experimentation, ma continua a essere measurement

Il rollout progressivo serve a gestire tre rischi:

- **scale risk**: il sistema si comporta diversamente a volumi maggiori;
- **coverage risk**: alcuni segmenti erano poco rappresentati nel test;
- **operational risk**: dipendenze infrastrutturali emergono solo su scala.

### Rollback criteria

Prima del rollout dovrebbero essere definiti criteri espliciti di rollback.

Esempio:

- crash rate > +5%;
- payment failure > +0,3 pp;
- latency P99 > +150 ms;
- fraud loss > soglia monetaria;
- guardrail business oltre il limite prestabilito.

Se questi criteri vengono decisi dopo aver visto i dati, il processo diventa negoziabile. Se sono definiti prima, diventano governance.

### Caso pubblico documentato — Microsoft

Microsoft descrive l'A/B testing come strumento anche per il rollout controllato di modifiche infrastrutturali. Nei casi documentati dalla Experimentation Platform, il team usa iterazioni successive e guardrail di prodotto per intercettare regressioni che test tecnici locali non avrebbero necessariamente evidenziato.

Questo è un punto importante: il rollout progressivo non è un segno di scarsa fiducia nell'esperimento. È una forma di gestione razionale del rischio residuo.

### Fonte pubblica

Microsoft Research, *A/B Testing Infrastructure Changes at Microsoft ExP*:
https://www.microsoft.com/en-us/research/articles/a-b-testing-infrastructure-changes-at-microsoft-exp/
