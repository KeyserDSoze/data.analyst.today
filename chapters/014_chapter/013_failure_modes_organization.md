# 14.13 Failure modes organizzativi: quando il problema non è il modello

Molti fallimenti dell'AI in azienda non nascono da un modello incapace. Nascono da un sistema organizzativo che usa l'AI senza ownership, senza confini chiari o senza capire cosa è stato delegato.

## “L'ha fatto l'AI” non è una spiegazione professionale

Se una query sbaglia un join, un agente invia un report errato o una previsione porta a una decisione sbagliata, dire:

> “L'ha fatto l'AI.”

non risolve il problema. Rivela che nessuno aveva chiaro chi fosse responsabile del risultato.

Un workflow maturo assegna sempre:

- un owner;
- un perimetro di autonomia;
- controlli;
- criteri di escalation;
- procedure di rollback;
- un livello di review coerente con il rischio.

Microsoft, nella propria guida agli agenti responsabili, raccomanda un owner nominato e human-in-the-loop per azioni conseguenziali o difficili da invertire.

## Failure mode 1: automazione senza supervisione

Un agente aggiorna automaticamente il forecast commerciale e invia il file al management.

Un cambio di schema fa sì che `pipeline_value` venga interpretato in centesimi anziché euro.

Il processo tecnico funziona perfettamente:

- job verde;
- API verde;
- file generato;
- email inviata.

Il business riceve un forecast 100 volte più alto.

Il problema non è la disponibilità del sistema. È l'assenza di un sanity check sul significato del risultato.

## Failure mode 2: deskilling silenzioso

Un team smette progressivamente di leggere le query generate dall'AI. Dopo un anno, quasi nessuno sa più diagnosticare un join esplosivo o un filtro temporale sbagliato.

La produttività sembra aumentare finché tutto funziona. Quando arriva un caso anomalo, nessuno è in grado di capire il comportamento del sistema.

L'obiettivo non è continuare a scrivere tutto a mano. È mantenere abbastanza competenza per:

- verificare;
- correggere;
- interrogare criticamente;
- riconoscere pattern sospetti;
- sapere quando l'AI sta operando fuori dal proprio perimetro.

## Failure mode 3: troppi agenti, nessuna gerarchia

Un'organizzazione crea agenti per:

- data quality;
- forecasting;
- SQL;
- report generation;
- anomaly detection;
- executive summaries;
- budget recommendations.

Ma nessuno definisce quali output siano autorevoli, quali solo esplorativi e quali possano attivare azioni.

Il risultato è una rete di sistemi che si citano a vicenda e amplificano lo stesso errore.

## Failure mode 4: metriche locali, danno globale

Un agente di marketing viene ottimizzato per ROAS. Scopre che può aumentarlo concentrando il budget su clienti già vicinissimi all'acquisto.

Il ROAS sale. L'incrementalità quasi scompare.

L'agente ha ottimizzato perfettamente la metrica assegnata.

La responsabilità umana era scegliere la metrica giusta.

## Failure mode 5: nessuno sa quando fermarsi

Un sistema agentico continua a iterare, generare query e modificare ipotesi senza un criterio di stop. Il costo cresce e la complessità supera il valore informativo prodotto.

Serve una policy di arresto:

- evidenza sufficiente;
- budget massimo;
- numero massimo di iterazioni;
- escalation per conflitto tra agenti;
- blocco quando la qualità del dato non consente una conclusione.

## La nuova responsabilità dell'analista

Con agenti sempre più capaci, l'analista diventa sempre meno un esecutore seriale e sempre più un orchestratore.

Questo non riduce la responsabilità. La aumenta.

**Più lavoro possiamo delegare, più importante diventa sapere cosa abbiamo delegato, a chi, con quali vincoli e come dimostriamo che il risultato è affidabile.**

### Fonti

- Microsoft Learn, Responsible AI for agents: https://learn.microsoft.com/en-us/agents/center-of-excellence/responsible-ai
- Microsoft Learn, AI shared responsibility model: https://learn.microsoft.com/en-us/azure/security/fundamentals/shared-responsibility-ai
