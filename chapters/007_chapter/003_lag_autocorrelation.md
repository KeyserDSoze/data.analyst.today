## 7.2 Lag e autocorrelazione: il passato lascia una traccia

Nelle serie temporali, le osservazioni vicine possono essere correlate. Questo significa che il valore di oggi può contenere informazione sul valore di domani.

Un **lag** è semplicemente uno spostamento temporale. Se osserviamo le vendite giornaliere \(y_t\), allora:

- \(y_{t-1}\) è il valore di ieri;
- \(y_{t-7}\) è il valore di una settimana fa;
- \(y_{t-12}\), in una serie mensile, è il valore dello stesso mese dell'anno precedente.

L'**autocorrelazione** misura quanto una serie è correlata con una versione ritardata di sé stessa. Il NIST la indica come strumento sia per rilevare non-randomness sia per identificare struttura utile alla modellazione.

### Caso: il contact center che sembrava imprevedibile

Un contact center riceve ogni giorno un numero di chiamate molto variabile:

| Giorno | Chiamate |
|---|---:|
| Lun | 8.420 |
| Mar | 7.910 |
| Mer | 7.760 |
| Gio | 7.580 |
| Ven | 7.210 |
| Sab | 4.100 |
| Dom | 3.320 |
| Lun successivo | 8.510 |

Guardando solo la deviazione standard giornaliera, il volume sembra estremamente instabile.

Ma il pattern settimanale è forte. La correlazione tra oggi e ieri è moderata; quella tra oggi e sette giorni fa è molto più alta.

La conseguenza operativa è importante. Per pianificare il personale del prossimo lunedì, la domenica precedente è un riferimento debole; il lunedì precedente è molto più informativo.

### Perché il lag giusto dipende dal processo

In un'app di mobilità urbana possono essere rilevanti lag di 24 ore e 168 ore. In un business mensile possono essere rilevanti lag 1 e 12. Per un impianto industriale con misure ogni minuto, possono essere rilevanti pochi minuti.

Non esiste un lag universalmente corretto. Il lag deve avere senso rispetto alla frequenza di raccolta e al meccanismo del business.

### Autocorrelazione non significa causalità

Se le vendite di oggi sono fortemente correlate a quelle di ieri, non significa che le vendite di ieri “causino” quelle di oggi. Entrambe possono riflettere domanda stabile, calendario, campagne, disponibilità di stock o altri processi persistenti.

L'autocorrelazione è soprattutto una proprietà utile per capire struttura e prevedibilità.

### Il pericolo delle osservazioni non indipendenti

Molte tecniche statistiche standard assumono osservazioni indipendenti. Se ignoriamo l'autocorrelazione, possiamo sottostimare l'incertezza e trattare come più informativa una serie che in realtà contiene molta ripetizione.

Avere 10.000 misure al minuto non equivale necessariamente ad avere 10.000 osservazioni indipendenti.

> **Nelle serie temporali, più righe non significano automaticamente più informazione indipendente.**

## Fonti

- NIST, *Autocorrelation*: https://itl.nist.gov/div898/handbook/eda/section3/eda35c.htm
