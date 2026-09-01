## 6.1 Segmentazione: dividere la popolazione solo quando cambia la decisione

Nel Capitolo 4 abbiamo usato la segmentazione come strumento esplorativo: rompere una media aggregata per scoprire struttura nascosta.

Nel lifecycle analysis la segmentazione ha un compito più specifico:

> **identificare gruppi che entrano, si attivano, restano, espandono o abbandonano in modo abbastanza diverso da richiedere una strategia diversa.**

Il punto non è creare più filtri.

È creare **unità decisionali**.

### Caso simulato/composito — “Il mobile converte peggio” non è ancora una diagnosi

L'e-commerce immaginario **Northstar Home** vede il conversion rate scendere dal 3,9% al 3,5%.

Per device:

| Device | Q1 | Q2 |
|---|---:|---:|
| Desktop | 5,8% | 5,9% |
| Mobile | 3,1% | 2,5% |
| Tablet | 3,4% | 3,3% |

Il deterioramento è mobile.

Sul mobile, per canale:

| Canale | Q1 | Q2 |
|---|---:|---:|
| Organic | 3,4% | 3,3% |
| Email | 4,6% | 4,5% |
| Paid search | 2,9% | 2,8% |
| Paid social | 2,7% | 1,6% |

Il problema è soprattutto `mobile + paid social`.

Segmentando ulteriormente per paese, il gap è concentrato in Italia e Spagna, dove è stata introdotta una nuova landing page.

La conclusione diventa:

> **“Il calo aggregato è concentrato nel traffico paid social mobile di Italia e Spagna dopo il cambio di landing.”**

Non abbiamo dimostrato che la landing **causi** il calo. Abbiamo però delimitato il punto del lifecycle in cui l'indagine deve continuare.

### Una segmentazione utile deve cambiare qualcosa

Un segmento è analiticamente utile se modifica almeno una di queste decisioni:

- **diagnosi:** dove crediamo si trovi il problema;
- **priorità:** quale gruppo genera più rischio o valore;
- **intervento:** quale azione è plausibile;
- **misurazione:** quale KPI o frequenza naturale è appropriata;
- **owner:** quale team può agire sul meccanismo.

Se dividere `country = IT / ES / FR / DE` non cambia nessuna di queste cose, la segmentazione può essere descrittiva ma non decisionale.

### Cinque famiglie di segmenti nel lifecycle

#### 1. Segmenti di acquisizione

- canale;
- campagna;
- referral source;
- sales motion;
- prezzo o offerta iniziale.

Servono a chiedere:

> *stiamo acquisendo lo stesso tipo di cliente?*

#### 2. Segmenti di profilo

- mercato;
- dimensione account;
- use case;
- piano;
- categoria prodotto.

Servono quando gruppi strutturalmente diversi hanno bisogni o frequenze differenti.

#### 3. Segmenti comportamentali

- feature adottate;
- frequenza d'uso;
- numero di collaboratori invitati;
- attività nei primi giorni;
- breadth/depth di utilizzo.

Sono spesso potenti perché descrivono ciò che il cliente **fa**, non soltanto ciò che è.

Ma richiedono cautela: un comportamento associato a retention elevata non è automaticamente una leva causale.

#### 4. Segmenti di lifecycle stage

- nuovo;
- onboarding;
- activated;
- retained;
- at-risk;
- dormant;
- reactivated.

Sono particolarmente utili per definire journey, comunicazioni e metriche coerenti con la fase.

#### 5. Segmenti economici

- ARR/GMV;
- margine;
- cost-to-serve;
- espansione;
- LTV.

Servono a distinguere frequenza e impatto economico.

Un churn del 10% su clienti da 20 € al mese non ha lo stesso significato economico del 10% su account enterprise.

### Caso reale documentato — Canal+ e i “power users”

In un case study pubblicato da **Amplitude**, Canal+ viene descritto mentre confronta la retention di gruppi con pattern di utilizzo differenti. Secondo il case study, gli utenti che guardavano sia contenuti live sia on-demand mostravano retention più alta rispetto a chi utilizzava soltanto una delle due modalità; il team usò questa informazione per orientare cambiamenti di prodotto.[^canal-amplitude]

È importante leggere correttamente il claim.

Il case study documenta una **associazione comportamentale utile al product team**. Non dimostra da solo che indurre un utente a consumare entrambi i formati provochi causalmente maggiore retention.

Questa distinzione è esattamente ciò che deve fare un buon analyst:

> **segmentare per trovare comportamenti interessanti, poi scegliere il metodo necessario per capire se sono anche leve.**

### Segmenti troppo piccoli: il problema che arriva dopo la heatmap

Se incrociamo:

- 8 paesi;
- 4 device;
- 6 canali;
- 5 piani;
- 3 fasce di tenure;

abbiamo già `8 × 4 × 6 × 5 × 3 = 2.880` combinazioni potenziali.

Molte avranno poche osservazioni.

Il Capitolo 5 ci impone quindi due discipline:

1. mostrare il denominatore;
2. distinguere segmentazione **pre-specificata** da pattern scoperti esplorativamente.

Un uplift del 40% su 17 utenti può essere una pista. Non è automaticamente una priorità aziendale.

### Segmenti definiti con il futuro: leakage analitico

Supponiamo di voler capire quali clienti, nei primi 30 giorni, hanno lifecycle migliore.

Creiamo un segmento chiamato:

> “clienti che hanno effettuato almeno 10 ordini nei primi 12 mesi”.

Poi scopriamo che questo segmento ha retention annuale altissima.

La scoperta è quasi tautologica: abbiamo usato comportamento futuro per definire il gruppo.

Se vogliamo una segmentazione utilizzabile **al giorno 30**, dobbiamo costruirla con informazione disponibile entro il giorno 30.

Questa regola anticipa il concetto di leakage del Capitolo 10.

### La scheda di un segmento utile

Prima di aggiungerlo a una dashboard lifecycle, compila:

```text
Segmento:
Regola di appartenenza:
Momento in cui l'appartenenza è conoscibile:
Dimensione / denominatore:
Differenza osservata nel lifecycle:
Decisione che cambia:
Owner dell'eventuale intervento:
Ipotesi o meccanismo plausibile:
Confermativo o esplorativo?
```

Se non sappiamo dire quale decisione cambia, probabilmente abbiamo creato un filtro, non ancora un segmento strategico.

> **La segmentazione è utile quando trasforma “gli utenti sono diversi” in “questi gruppi richiedono diagnosi o azioni diverse”.**

[^canal-amplitude]: Amplitude, *How Canal+ used Product Intelligence to increase conversion by 3x*: https://amplitude.com/case-studies/canal
