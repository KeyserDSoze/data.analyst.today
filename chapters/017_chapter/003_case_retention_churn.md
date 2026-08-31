# 17.2 Caso end-to-end: retention e churn senza confondere rischio e causa

Una piattaforma SaaS B2B, **NorthPeak**, vede il logo churn salire dal 2,8% al 4,1% trimestrale.

Il Chief Customer Officer chiede:

> “Quali clienti dobbiamo salvare subito?”

La domanda sembra predittiva. In realtà contiene almeno tre problemi diversi:

1. chi rischia di churnare?
2. perché rischia di churnare?
3. su chi un intervento può davvero cambiare l'esito?

## 1. Definire churn e popolazione

Il team chiarisce:

- unità: account, non utenti;
- churn: contratto non rinnovato alla data di renewal;
- finestra di previsione: 90 giorni;
- esclusioni: trial, account acquisiti da meno di 60 giorni, contratti già in dismissione.

Senza questa definizione, il modello sarebbe stato addestrato su popolazioni semanticamente diverse.

## 2. Cohort analysis prima del machine learning

Le coorti mostrano che il peggioramento è concentrato nei clienti acquisiti negli ultimi 12 mesi tramite un nuovo partner channel.

Il churn dei clienti direct-sales è quasi stabile.

Questo riduce immediatamente lo spazio delle ipotesi.

## 3. Funnel di adozione

Nel partner channel emergono:

- activation entro 14 giorni: 71% → 54%;
- uso della feature core nel primo mese: -19%;
- ticket di onboarding: +32%;
- tempo al primo valore: +4,6 giorni.

Il finding più utile non è quindi ancora “questi clienti hanno churn risk alto”.

È:

> “Il peggioramento nasce molto prima del rinnovo.”

## 4. Il modello predittivo

Viene costruito un modello con AUC 0,84 e buona calibration.

Le feature principali includono:

- diminuzione utilizzo;
- mancata attivazione feature core;
- numero di ticket;
- distanza dal renewal;
- NPS;
- seat utilization.

Ma il team evita un errore frequente: interpretare feature importance come causalità.

Il fatto che molti ticket predicano churn non significa che ridurre artificialmente i ticket riduca churn.

## 5. Risk score ≠ treatment opportunity

I 500 account con rischio più alto vengono analizzati economicamente.

Alcuni sono quasi certamente persi perché:

- azienda chiusa;
- merger;
- budget azzerato;
- migrazione strategica già decisa.

Spendere retention budget su questi clienti avrebbe basso valore atteso.

Il team costruisce quindi una matrice:

| | Alta persuadibilità | Bassa persuadibilità |
|---|---|---|
| Alto rischio | priorità | evitare spreco |
| Basso rischio | test selettivo | nessuna azione |

## 6. Intervento e causalità

Storicamente, i Customer Success Manager chiamavano soprattutto clienti molto a rischio. Nei dati osservazionali, chi riceveva una chiamata churnava di più.

Una lettura ingenua avrebbe concluso:

> “Le chiamate fanno aumentare il churn.”

È selection bias: le chiamate venivano assegnate proprio ai clienti peggiori.

Il team decide quindi di randomizzare un nuovo intervento di onboarding intensivo su un sottoinsieme di nuovi account partner-channel.

## 7. Decisione

La strategia cambia da:

> “Chiamiamo i 500 clienti con score più alto.”

a:

- correggere onboarding partner-channel;
- intervenire prima, entro i primi 30 giorni;
- usare il risk model per priorità operativa;
- usare esperimenti per stimare l'effetto incrementale degli interventi;
- escludere account non persuadibili o economicamente non convenienti.

## 8. Misurazione

Metriche:

- 30-day activation;
- time-to-first-value;
- feature adoption;
- renewal rate;
- incremental retention uplift;
- costo per renewal salvato;
- NRR per coorte.

Microsoft documenta oggi scenari di transactional churn prediction in cui il processo comprende ingestione, unificazione, attività transazionali, previsione e segmentazione dei clienti ad alto rischio. È un buon esempio di workflow predittivo, ma il passaggio successivo — decidere quale intervento causi davvero una riduzione del churn — richiede un disegno analitico aggiuntivo.

Fonte pubblica documentata: https://learn.microsoft.com/en-us/dynamics365/customer-insights/data/sample-guide-predict-transactional-churn

> **Predire chi perderemo non equivale a sapere chi possiamo salvare.**
