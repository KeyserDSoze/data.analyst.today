## 2.4 Metriche e KPI: misurare ciò che conta davvero

Una metrica è una quantificazione. Un KPI è una metrica collegata esplicitamente a un obiettivo e usata per valutare performance o avanzamento rispetto a un target.

Questa distinzione è importante perché un'organizzazione può avere centinaia di metriche, ma solo poche dovrebbero guidare decisioni strategiche.

Microsoft descrive un KPI come una misura che valuta il valore corrente di una metrica rispetto a un target definito. In pratica, un KPI ha almeno tre elementi:

- una misura corrente;
- un obiettivo o target;
- una logica con cui interpretare distanza e stato.

### Una metrica senza contesto può ingannare

Supponiamo che il fatturato sia aumentato del 10%.

È positivo?

Non necessariamente.

Se nello stesso periodo:

- i prezzi sono aumentati del 15%;
- il margine è diminuito;
- il numero di clienti attivi è crollato;
- il costo di acquisizione è raddoppiato;
- il budget prevedeva +25%;

quel +10% assume un significato completamente diverso.

### Definire la metrica prima di calcolarla

Per ogni metrica importante, scrivi una **metric contract** minima:

- nome;
- definizione business;
- formula;
- unità;
- granularità;
- popolazione inclusa;
- esclusioni;
- finestra temporale;
- fonte dati;
- owner;
- frequenza di aggiornamento;
- target o baseline, se presenti.

Esempio:

**Conversion Rate**

> Percentuale di sessioni e-commerce che generano almeno un ordine confermato entro la stessa sessione, escludendo traffico interno, bot e ordini di test.

Formula:

`sessioni con ordine confermato / sessioni valide`

Già questa definizione genera domande: una sessione può contenere più ordini? L'ordine deve essere pagato? Come riconosciamo i bot? Quale timezone utilizziamo?

La qualità dell'analisi dipende dalla risposta a queste domande più di quanto dipenda dal colore del grafico.

### Leading e lagging indicators

Un'altra distinzione utile è tra indicatori **lagging** e **leading**.

I lagging indicator descrivono risultati già avvenuti:

- fatturato;
- churn;
- margine;
- reclami chiusi;
- ordini consegnati.

I leading indicator cercano invece di anticipare risultati futuri:

- richieste demo;
- utilizzo del prodotto;
- tempo al primo valore;
- stockout previsti;
- qualità dei lead;
- engagement precoce.

Un buon sistema di misurazione tende a combinare entrambi. I lagging indicator dicono dove siamo arrivati; i leading indicator possono suggerire dove stiamo andando.

### KPI non significa "numero importante"

Un KPI dovrebbe essere collegato a una responsabilità e a una decisione.

Se una metrica cambia e nessuno sa cosa fare in risposta, forse è una metrica informativa, non un vero KPI operativo.

### Guardrail metrics

Ottimizzare una sola metrica può produrre effetti indesiderati.

Esempio: aumentare il tasso di conversione con sconti aggressivi può ridurre il margine. Ridurre il tempo medio di gestione dei ticket può peggiorare la soddisfazione dei clienti.

Per questo, accanto alla metrica obiettivo, conviene definire **guardrail metrics** che non devono deteriorarsi oltre una certa soglia.

Esempio:

- obiettivo: aumentare conversion rate;
- guardrail: margine per ordine;
- guardrail: tasso di reso;
- guardrail: customer satisfaction.

### Domande da fare prima di accettare un KPI

1. Quale obiettivo rappresenta?
2. Chi può influenzarlo?
3. Qual è il target?
4. Qual è la baseline?
5. Con quale frequenza cambia in modo significativo?
6. Può essere manipolato senza ottenere il vero risultato desiderato?
7. Quali metriche di guardia servono?
8. Quale decisione cambia quando supera una soglia?

## Riferimenti

- Microsoft Learn, *Create key performance indicator (KPI) visualizations*: https://learn.microsoft.com/en-us/power-bi/visuals/power-bi-visualization-kpi
- Microsoft Learn, *Key Performance Indicators in tabular models*: https://learn.microsoft.com/en-us/analysis-services/tabular-models/kpis-ssas-tabular
