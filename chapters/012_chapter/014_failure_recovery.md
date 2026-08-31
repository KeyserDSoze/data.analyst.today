## 12.13 Failure e recovery: progettare il giorno in cui qualcosa andra' storto

Una pipeline affidabile non è quella che non fallisce mai. È quella che **fallisce in modo osservabile, recuperabile e senza corrompere il dato**.

### Caso realistico: Helix Pharma

Helix riceve dati di vendita da 42 mercati.

Ogni notte una pipeline:

1. acquisisce i file locali;
2. valida lo schema;
3. converte le valute;
4. aggiorna il warehouse;
5. ricalcola le metriche commerciali.

Alle 03:17 la pipeline si interrompe durante il caricamento del mercato brasiliano.

Il problema non è soltanto il fallimento.

Il problema è capire **cosa era già stato scritto**.

Se il sistema non distingue tra task completati, parziali e non eseguiti, una ripartenza può:

- duplicare dati;
- saltare record;
- lasciare versioni miste;
- pubblicare un dataset incompleto come se fosse valido.

### Atomicita' e checkpoint

Quando possibile, un passaggio dovrebbe essere atomico: o viene completato, oppure il risultato parziale non diventa visibile come prodotto valido.

Non sempre è possibile ottenere atomicita' perfetta. In alternativa servono checkpoint affidabili.

Esempio:

```text
market=BR
date=2026-08-30
last_successful_file=part-0187
```

In questo modo il sistema sa da dove riprendere.

### Retry con criterio

Non tutti gli errori meritano lo stesso retry.

Un timeout di rete può risolversi al secondo tentativo.

Uno schema incompatibile probabilmente no.

Ritentare automaticamente 20 volte una breaking change non rende la pipeline più robusta. Ritarda solo la diagnosi.

### Dead-letter e quarantena

Quando pochi record sono anomali, può essere utile separare:

- dati validi che possono proseguire;
- record problematici messi in quarantena.

Esempio:

```text
valid_orders -> curated.orders
invalid_orders -> quarantine.orders
```

Ma attenzione: la quarantena non deve trasformarsi in un buco nero ignorato.

Bisogna monitorare:

- quanti record entrano;
- perché;
- da quali sorgenti;
- da quanto tempo non vengono risolti.

### Recovery Point Objective e Recovery Time Objective

Anche nei sistemi dati sono utili due concetti operativi:

- **RPO**: quanta perdita di dati temporale possiamo tollerare;
- **RTO**: quanto tempo possiamo impiegare per ripristinare il servizio.

Un dashboard settimanale può tollerare un RTO di alcune ore.

Un sistema antifrode operativo probabilmente no.

### Il problema dei dati parziali

Una delle situazioni peggiori è quando il sistema non fallisce apertamente.

Supponiamo che arrivino 41 mercati su 42.

Il job termina con successo perché nessun errore tecnico si è verificato.

Il fatturato globale viene pubblicato comunque.

Tecnicamente la pipeline è verde.

Analiticamente il prodotto è incompleto.

Per questo servono controlli di **completeness attesa**, non solo controlli di esecuzione.

### Metodo operativo

Per ogni pipeline critica definire:

1. cosa succede se fallisce a meta';
2. come si identifica l'ultimo stato valido;
3. quali task sono idempotenti;
4. quali errori meritano retry;
5. quali dati vanno quarantinati;
6. quando bloccare il downstream;
7. chi riceve l'alert;
8. come eseguire il backfill;
9. come verificare che il recovery non abbia duplicato dati.

**Recovery non significa far ripartire un job. Significa tornare a uno stato del dato che possiamo di nuovo considerare affidabile.**
