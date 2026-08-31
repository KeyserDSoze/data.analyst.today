# 13.4 BI e semantic layer: quando il risultato deve diventare condiviso

Una buona analisi può vivere in un notebook. Una buona metrica aziendale, invece, spesso deve vivere in un sistema condiviso.

Gli strumenti di Business Intelligence entrano in gioco quando il problema non è più soltanto analizzare, ma distribuire una lettura coerente del business a molte persone.

## 13.4.1 Dashboard non significa automaticamente BI matura

È facile costruire un dashboard. È molto più difficile costruire un sistema di metriche affidabile.

Un ambiente BI maturo richiede:

- definizioni condivise;
- modello semantico;
- relazioni coerenti;
- permessi;
- refresh controllati;
- metriche certificate;
- lineage;
- ownership.

Il grafico è la parte visibile. La semantica è l'infrastruttura invisibile.

## 13.4.2 Caso realistico: cinque dashboard, cinque conversion rate

Un'azienda SaaS ha cinque dashboard create da team diversi.

Il conversion rate varia tra 7,4% e 11,8%.

Le differenze derivano da definizioni diverse:

- lead creati;
- lead qualificati;
- opportunity create;
- trial started;
- account con almeno un utente attivo.

Nessun grafico è tecnicamente rotto. È il linguaggio del business a non essere condiviso.

La soluzione non è costruire un sesto dashboard. Serve un semantic layer.

## 13.4.3 Il semantic layer come contratto analitico

Il semantic layer traduce strutture tecniche in concetti utilizzabili dal business.

Può definire:

- Revenue Netta;
- Cliente Attivo;
- Churn;
- Gross Margin;
- Conversion Rate;
- Retention D30;
- ARR;
- NRR.

Queste definizioni diventano riusabili e riducono la duplicazione della logica.

## 13.4.4 Self-service non significa «ognuno calcola quello che vuole»

Il vero self-service analytics separa due livelli:

**governed core**

- dati certificati;
- dimensioni condivise;
- metriche ufficiali;
- controlli di accesso;

**exploration layer**

- filtri;
- segmentazioni;
- drill-down;
- analisi ad hoc;
- prototipi.

Il self-service funziona quando gli utenti possono esplorare senza dover reinventare la semantica.

## 13.4.5 Quando usare la BI

La BI è appropriata quando:

- il consumo è ricorrente;
- molte persone usano gli stessi KPI;
- serve monitoraggio continuo;
- devono esistere permessi e governance;
- il risultato deve essere aggiornato automaticamente;
- il consumo è soprattutto visuale e interattivo.

È meno adatta come ambiente principale quando l'analisi è ancora fortemente esplorativa, statistica o sperimentale.

## 13.4.6 Caso realistico: il dashboard usato per una domanda che cambia ogni giorno

Un team Strategy chiede un dashboard per investigare un calo improvviso della redditività.

Ogni giorno emergono nuove ipotesi:

- mix prodotto;
- sconti;
- freight;
- resi;
- FX;
- nuovi clienti;
- marketplace fees.

Costruire subito un dashboard formalizzato rallenta l'indagine. È più efficiente esplorare prima con SQL/notebook e costruire il dashboard solo quando le metriche e i percorsi diagnostici si stabilizzano.

> **La BI è eccellente per industrializzare una domanda stabile. È meno adatta per scoprire quale sia la domanda giusta.**
