## 7.4 Anomalie: prima di cercare una causa, verifica che l'evento esista davvero

Un'anomalia è un'osservazione o un pattern che si discosta da ciò che ci aspetteremmo dato il comportamento storico della serie.

Questa definizione sembra semplice, ma contiene una parola pericolosa: **aspettarsi**.

Per decidere se qualcosa è anomalo dobbiamo prima costruire una baseline ragionevole. Un picco di ordini il 24 novembre può sembrare enorme rispetto alla media di ottobre, ma essere perfettamente normale durante Black Friday. Un calo del traffico alle tre del mattino è normale. Lo stesso calo alle undici del mattino può essere un incidente.

### Tipi di anomalie utili per un Data Analyst

Possiamo distinguere almeno quattro situazioni:

1. **point anomaly**: un singolo punto è insolito;
2. **contextual anomaly**: il valore è anomalo solo in quel contesto temporale;
3. **collective anomaly**: nessun punto è estremo da solo, ma una sequenza intera è insolita;
4. **structural break**: cambia il comportamento del processo, non solo un singolo punto.

### Caso: il -42% che non era un problema commerciale

Un marketplace europeo monitora il GMV ogni quindici minuti. Alle 14:30 il sistema di alert segnala:

```text
GMV atteso 14:00-14:15: 318.000 €
GMV osservato: 184.000 €
scostamento: -42.1%
```

Marketing sospende immediatamente una campagna per paura che il checkout sia rotto.

L'analista controlla il funnel:

- sessioni: normali;
- add-to-cart: normali;
- checkout iniziati: normali;
- payment success: apparentemente -39%;
- errori del payment gateway: normali.

Poi controlla il timestamp di ingestion. Il 38% degli eventi `payment_success` ha un ritardo superiore a venti minuti a causa di un problema nella pipeline streaming.

Alle 15:05, una volta arrivati gli eventi in ritardo, il GMV reale della finestra risulta 309.000 €, cioè circa -2.8% rispetto all'atteso.

L'anomalia era nel **sistema di osservazione**, non nel business.

### Data anomaly vs business anomaly

Questa distinzione dovrebbe diventare automatica.

Quando un numero si muove in modo inatteso, le prime ipotesi non dovrebbero essere solo commerciali:

- il comportamento degli utenti è cambiato;
- il mix clienti è cambiato;
- una campagna è partita;
- un competitor ha cambiato prezzo;

ma anche:

- manca una partizione;
- sono arrivati eventi in ritardo;
- è cambiato uno schema;
- un timestamp è passato da UTC a ora locale;
- una join ha perso righe;
- un job è stato eseguito due volte;
- è cambiata la definizione della metrica.

### Soglie statiche: semplici ma spesso fragili

Un alert del tipo:

```text
se revenue < 1.000.000 € allora alert
```

può essere utile, ma ignora trend e stagionalità.

Una soglia dinamica può essere più sensata:

```text
alert se valore osservato è molto lontano dal valore atteso dato
trend + stagionalità + variabilità storica
```

Ma anche un sistema dinamico può generare falsi positivi se non conosce promozioni, festività, migrazioni o cambi strutturali.

### Caso: il miglior giorno dell'anno classificato come incidente

Una piattaforma food delivery implementa un detector automatico che segnala deviazioni superiori a quattro deviazioni standard dalla media recente.

La sera della finale di Champions League gli ordini aumentano del 63%. Il detector apre un incidente severity 1 perché il volume è “impossibile”.

Tecnicamente l'algoritmo ha ragione: rispetto alla distribuzione recente il valore è estremo. Operativamente ha torto: il fenomeno è spiegabile e desiderabile.

Il problema non è nel calcolo, ma nella baseline incompleta.

### Un workflow pratico per investigare un'anomalia

Quando ricevi un alert:

1. verifica freshness e completezza;
2. confronta metriche upstream e downstream;
3. controlla se esistono eventi di calendario;
4. segmenta per paese, piattaforma, prodotto, canale;
5. verifica se il cambiamento è un punto singolo o persiste;
6. confronta con periodi stagionalmente simili;
7. misura l'impatto economico;
8. solo dopo formula ipotesi causali.

> **Un'anomalia statistica è un invito a investigare, non una spiegazione.**
