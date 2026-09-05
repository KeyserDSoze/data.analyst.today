## 12.11 SLI, SLO e SLA del dato: definire che cosa significa essere affidabile

“Il dashboard viene aggiornato ogni mattina” non è una garanzia misurabile. Dopo aver descritto readiness e publish boundary, dobbiamo tradurre l'affidabilità in proprietà osservabili dal punto di vista del consumer.

Il vocabolario SRE è utile: uno **SLI** è ciò che misuriamo, uno **SLO** è il target che vogliamo rispettare, uno **SLA** è un impegno formale verso il consumer. Google SRE insiste su due principi importanti: gli indicatori devono partire da ciò che interessa agli utenti, non da ciò che è facile misurare; e un obiettivo del 100% è spesso tanto costoso quanto indesiderabile.

Fonte: https://sre.google/sre-book/service-level-objectives/

### Partire dalla user journey

Per un prodotto dati una user journey può essere:

> **Alle 08:00 il finance analyst apre il report e deve poter decidere usando dati completi fino alla chiusura di ieri.**

Da questa frase derivano indicatori più utili di “pipeline verde”.

### Caso simulato/composito — Solaria Energy e il report disponibile ma incompleto

Solaria raccoglie letture da contatori intelligenti. Il requisito informale è “report pronto entro le 08:00”. Alle 07:55 il dashboard è interrogabile, ma solo il **93%** dei meter attesi ha contribuito alla giornata.

Il serving è disponibile; il prodotto dati non è sufficientemente completo.

Per questo distinguiamo almeno quattro proprietà. **Freshness** misura quanto recente è il dato rispetto al periodo atteso. **Completeness** misura quanto input previsto è arrivato ed è stato accettato. **Availability** misura se il consumer può realmente leggere il prodotto. **Correctness/reconciliation**, quando esiste una reference autorevole, misura se il risultato resta entro una tolleranza concordata.

Un esempio di SLO può essere:

```text
99% dei giorni:
dati fino alle 23:59 di T-1 pubblicati entro le 07:30

completezza:
>= 99,2% dei meter attesi entro le 08:00
```

Freshness e completeness non sono intercambiabili: possiamo avere un timestamp recentissimo su dati parziali oppure un dato più vecchio ma quasi completo.

### Recovery e error budget

Quando lo SLO viene violato interessa anche quanto tempo serve per tornare a uno stato affidabile. Time to detect, acknowledge, restore e complete reconciliation/backfill misurano fasi diverse. Il job che riparte non coincide con il dato recuperato.

L'**error budget** rende inoltre esplicita la quota di mancato rispetto tollerata. Un SLO del 99% non significa che l'altro 1% sia irrilevante: significa che abbiamo dichiarato un margine e possiamo reagire quando viene consumato troppo rapidamente.

### SLO differenti per decisioni differenti

Lo stesso dominio può servire Operations con freshness sotto dieci minuti e dati provisional, e Finance con T+1, completezza quasi totale e reconciliation obbligatoria. Non è incoerenza: sono user journey diverse.

Il consumer deve poter vedere anche lo stato del dato, per esempio:

```text
READY
DEGRADED
STALE
INCOMPLETE
FAILED
```

con timestamp e caveat. Lo stato non dovrebbe derivare soltanto dall'ultimo refresh BI, ma dalle garanzie dell'intero percorso.

Nella Data Flow Architecture Map annotiamo:

```text
consumer journey:
SLI:
SLO target:
measurement point:
compliance window:
error budget / allowed misses:
alert threshold:
degraded behavior:
recovery owner:
```

> **Un dataset non è “affidabile” in astratto. È affidabile per un consumer, entro una finestra, con un livello dichiarato di completezza e con un comportamento noto quando quella promessa non viene rispettata.**
