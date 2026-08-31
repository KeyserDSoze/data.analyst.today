## 16.10 Dashboard anti-pattern: quando più informazione produce meno comprensione
Una dashboard può essere tecnicamente completa e cognitivamente inutilizzabile.

Il problema nasce spesso quando proviamo a soddisfare ogni stakeholder nello stesso schermo.

## Anti-pattern 1 — Il cockpit pieno di strumenti

Una pagina contiene:

- 24 KPI;
- 12 filtri;
- 8 grafici;
- 6 card;
- 3 mappe;
- una tabella da 40 colonne.

Ogni elemento ha una ragione individuale per esistere.

Il risultato complessivo però non ha una gerarchia.

Il lettore non sa dove guardare.

## Anti-pattern 2 — KPI senza baseline

Revenue: €12,4M.

Conversion: 3,8%.

Churn: 2,7%.

Senza confronto con target, periodo precedente o benchmark, questi valori hanno poco significato decisionale.

Una dashboard dovrebbe aiutare a distinguere:

- normale;
- anomalo;
- migliorato;
- peggiorato;
- fuori soglia.

## Anti-pattern 3 — Filtri che cambiano il significato

Un filtro di data applicato a `order_date` in una pagina e a `delivery_date` in un'altra può produrre dashboard coerenti visivamente ma semanticamente incompatibili.

La governance delle metriche precede la visualizzazione.

## Anti-pattern 4 — Interattività come sostituto del design

Drill-down, tooltip, bookmark e slicer sono utili, ma non dovrebbero costringere l'utente a esplorare dieci livelli per capire se esiste un problema.

L'interattività deve permettere di approfondire una storia già leggibile, non nasconderla.

## Anti-pattern 5 — Semafori ovunque

Rosso, giallo e verde sembrano intuitivi.

Ma se ogni KPI ha soglie arbitrarie, il colore produce una falsa sensazione di precisione.

Inoltre una dashboard che dipende solo dal colore crea problemi di accessibilità.

La Government Analysis Function raccomanda di ridurre clutter e decorazioni non necessarie e di progettare grafici accessibili, non dipendenti da elementi puramente estetici.

Fonte: https://analysisfunction.civilservice.gov.uk/policy-store/charts-a-checklist/

## Caso realistico: il dashboard che nessuno riusciva a usare

Una società industriale investe mesi in una dashboard di operations.

La home page contiene 62 visualizzazioni distribuite in più tab.

Gli utenti dichiarano di volere “tutti i dati disponibili”.

Dopo il rilascio, però, durante il weekly review i manager continuano a chiedere screenshot preparati manualmente dagli analyst.

L'analisi del comportamento mostra che quasi tutti usano soltanto:

- backlog;
- throughput;
- on-time delivery;
- defect rate;
- tre segmentazioni principali.

Il redesign parte non dalle visualizzazioni, ma dalle decisioni settimanali.

La home diventa:

1. stato complessivo;
2. deviazioni principali;
3. contributori al delta;
4. aree che richiedono azione;
5. link al dettaglio operativo.

Il numero di visualizzazioni diminuisce, ma l'utilità aumenta.

## Una domanda da fare prima di aggiungere un elemento

> “Quale decisione migliora questa visualizzazione?”

Se non riusciamo a rispondere, probabilmente stiamo aggiungendo informazione invece di aggiungere valore.

**Una dashboard non è un archivio di grafici. È un'interfaccia tra dati e decisioni.**
