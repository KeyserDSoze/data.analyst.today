## 6.6 Caso studio: il churn che sembrava colpa del prezzo

Asteria CRM è un SaaS B2B europeo con circa 18.000 account paganti. Nel primo semestre aumenta il listino del piano Professional del 12%. Due mesi dopo, il churn mensile passa dal 2,7% al 3,6%.

La conclusione arriva rapidamente: l'aumento di prezzo sta facendo scappare i clienti.

L'analista non parte dalla correlazione temporale. Costruisce prima la segmentazione.

### Primo taglio: piano

| Piano | Churn prima | Churn dopo |
| --- | ---: | ---: |
| Starter | 3,8% | 5,4% |
| Professional | 2,5% | 2,8% |
| Enterprise | 1,1% | 1,2% |

Il piano Professional, quello interessato dall'aumento di prezzo, peggiora pochissimo. Il vero deterioramento è sullo Starter.

### Secondo taglio: coorte di acquisizione

L'analista crea coorti mensili e misura la retention a 90 giorni.

| Coorte | Retention D90 |
| --- | ---: |
| Gennaio | 79% |
| Febbraio | 78% |
| Marzo | 77% |
| Aprile | 69% |
| Maggio | 66% |
| Giugno | 65% |

Il problema inizia nelle coorti di aprile.

A marzo l'azienda aveva lanciato una campagna self-service dedicata alle microimprese. Il volume di trial era aumentato del 48%, soprattutto sul piano Starter.

### Terzo taglio: canale

| Canale | Retention D90 |
| --- | ---: |
| Organic | 80% |
| Partner | 84% |
| Paid search | 76% |
| Paid social nuova campagna | 51% |

Il churn sembra ormai molto meno legato al prezzo.

### Funnel di activation

L'analista costruisce poi il funnel delle prime due settimane:

1. trial avviato;
2. importazione contatti;
3. prima pipeline creata;
4. primo task assegnato;
5. almeno tre utenti invitati.

I clienti della nuova campagna paid social arrivano numerosi al trial, ma solo il 22% completa l'importazione dei contatti, contro il 47% degli altri canali.

La campagna prometteva "CRM operativo in cinque minuti" e portava utenti con aspettative molto diverse dal prodotto reale.

### Il risultato

Il prezzo era una spiegazione intuitiva perché l'aumento era visibile e temporalmente vicino al peggioramento. Ma la combinazione di segmentazione, coorti e funnel raccontava un'altra storia:

> Il deterioramento del churn è spiegato soprattutto dalle nuove coorti Starter acquisite tramite una campagna paid social con bassa activation iniziale. L'aumento di prezzo del Professional non appare, nei dati disponibili, il driver principale.

La decisione cambia.

Invece di annullare immediatamente l'aumento di prezzo, l'azienda:

- modifica targeting e messaggio della campagna;
- introduce un onboarding guidato per gli Starter;
- monitora activation entro 14 giorni;
- avvia un test controllato sul supporto onboarding;
- continua a osservare separatamente il churn del Professional.

Tre mesi dopo, la retention D90 delle nuove coorti Starter sale dal 65% al 73%.

Questo non dimostra da solo che ogni intervento sia causalmente responsabile del recupero. Ma mostra il valore dell'analisi corretta: la prima ipotesi poteva essere plausibile e comunque sbagliata.

### Il metodo dietro il caso

Il percorso è replicabile:

**KPI aggregato -> segmento -> coorte -> funnel -> ipotesi -> intervento -> nuova misurazione**

Quando retention e churn cambiano, questo schema è spesso più utile di qualsiasi dashboard piena di KPI non segmentati.
