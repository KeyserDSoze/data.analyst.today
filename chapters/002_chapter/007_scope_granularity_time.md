## 2.6 Scope: a chi, a che cosa e a quale tempo si applicherà la conclusione

Una domanda può sembrare precisa e produrre comunque risposte incompatibili se persone diverse immaginano popolazioni, unità di analisi o finestre temporali differenti. Per questo lo scope non è un dettaglio che si risolve nella `WHERE` della query: definisce **a quale porzione del mondo potremo applicare la conclusione**.

Il Capitolo 3 entrerà nel grain tecnico di tabelle, chiavi, eventi e snapshot. Nel brief ci serve la specifica analitica che viene prima: che cosa entra nell'indagine, che cosa resta fuori e quale osservazione rappresenta ogni riga del ragionamento.

## Popolazione e unità di analisi

Scrivere “clienti” o “ordini” è raramente sufficiente. Una popolazione utile contiene condizioni di eleggibilità ed esclusioni intenzionali. “Clienti con contratto attivo all'inizio del mese”, “nuovi clienti acquisiti tra gennaio e giugno” oppure “ordini completati e non integralmente rimborsati” definiscono mondi diversi e impediscono che stati incompatibili vengano aggregati come se fossero equivalenti.

Una volta definita la popolazione, dobbiamo scegliere l'unità a cui attribuiamo il fenomeno. La stessa azienda può essere analizzata a livello di evento, sessione, ordine, cliente, account, prodotto, negozio o coorte. Questa non è una preferenza tecnica. Se chiediamo quale percentuale di clienti riacquista, il cliente è l'unità naturale; se cerchiamo dove fallisce un pagamento, dobbiamo osservare tentativi o eventi. Se una policy è assegnata per negozio, trattare ogni transazione come osservazione indipendente può farci sovrastimare quanta informazione possediamo.

Prima della query dovremmo quindi riuscire a completare senza ambiguità:

> **“Una osservazione nella mia analisi rappresenta…”**

## Il tempo è parte del fenomeno

Anche una finestra apparentemente semplice come “ultimo trimestre” è ambigua finché non scegliamo quale evento assegna un'osservazione al periodo. Un ordine può avere `created_at`, `paid_at`, `shipped_at`, `delivered_at` e `returned_at`; ciascuna data descrive una fase diversa del processo. La data corretta dipende dalla domanda, non dalla comodità della colonna già disponibile.

Il tempo introduce inoltre il problema della **maturazione**. Se misuriamo retention o repeat purchase a 90 giorni, i clienti acquisiti dieci giorni fa non hanno ancora avuto la stessa opportunità di manifestare l'outcome. Includerli nel denominatore non significa avere dati più freschi: significa mescolare osservazioni mature e immature e attribuire alle seconde un esito che non è ancora conoscibile.

Per la stessa ragione il brief deve annotare la latenza con cui una sorgente diventa completa. Una metrica calcolata oggi su eventi che si consolidano dopo tre giorni può apparire in calo ogni volta che guardiamo l'ultima finestra disponibile.

## Stock e flow non sono intercambiabili

Lo scope deve anche chiarire se stiamo descrivendo uno **stock**, cioè uno stato in un istante, oppure un **flow**, cioè eventi accumulati durante un intervallo. “Clienti attivi a fine mese” è uno stock; “nuovi clienti acquisiti nel mese” è un flow. “Pipeline aperta al 31 marzo” e “opportunità create nel trimestre” possono entrambe essere metriche commerciali valide, ma non misurano lo stesso oggetto temporale.

Questa distinzione evita KPI confusi e aiuta a capire quali confronti siano legittimi.

## Lo scope protegge anche dal progetto che si espande

Una volta iniziata l'analisi, nuove domande emergeranno inevitabilmente. Partiamo dal churn enterprise europeo e qualcuno propone di includere SMB, pricing globale, support e tre anni di storico. Le nuove piste possono essere utili, ma non sono gratuite: modificano costo, tempo, dati richiesti e forse perfino la decisione supportata.

La disciplina consiste nel trattarle come un **cambio di brief**, non come dettagli che entrano silenziosamente nel lavoro. Questo permette di distinguere una scoperta che richiede reframing dallo scope creep che consuma capacità senza una scelta esplicita.

Il campo operativo rimane strutturato perché deve poter essere riutilizzato:

```text
Popolazione eleggibile:
Esclusioni:
Unità di analisi:
Grain richiesto per i dati:
Campo temporale principale:
Timezone:
Finestra di analisi:
Periodo di maturazione:
Data latency / data complete as of:
Fuori scope:
```

> **Definire lo scope significa stabilire in anticipo chi ha davvero avuto l'opportunità di entrare nel numeratore, nel denominatore e nella conclusione.**
