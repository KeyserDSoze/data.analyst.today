# 0.8 Manifesto dell'analista AI-native

Il resto di questo libro insegnerà statistica, SQL, modeling, causalità, forecasting, architettura, strumenti, comunicazione e AI-assisted analytics.

Ma prima di tutto questo serve un patto professionale.

L'AI può cambiare il modo in cui lavoriamo.

Non deve cambiare il fatto che qualcuno deve capire cosa sta succedendo.

## 1. Comando io l'obiettivo

Non chiedo all'AI semplicemente di “analizzare i dati”.

Definisco:

- la decisione;
- la domanda;
- il perimetro;
- la popolazione;
- il livello di evidenza richiesto.

## 2. Delego l'esecuzione, non la responsabilità

Posso delegare:

- codice;
- query;
- ricerca;
- sintesi;
- grafici;
- documentazione;
- test;
- esplorazione.

Non delego la responsabilità di capire ciò che consegno.

## 3. Chiedo evidenza, non soltanto risposte

Una conclusione importante deve essere accompagnata da elementi verificabili:

- dati;
- fonti;
- query;
- definizioni;
- test;
- assunzioni;
- alternative;
- limiti.

## 4. Un output plausibile non è un output corretto

Gli errori più pericolosi non sono sempre assurdi.

Sono quelli che sembrano ragionevoli.

Per questo verifico soprattutto:

- grain;
- join;
- metriche;
- temporalità;
- denominatori;
- popolazioni;
- leakage;
- causalità.

## 5. Progetto controlli, non micromanagement

Non rifaccio manualmente ogni lavoro dell'AI.

Costruisco:

- test deterministici;
- reconciliation;
- controlli statistici;
- review semantiche;
- sampling;
- red-team;
- audit;
- escalation.

## 6. Non tutti gli agenti hanno la stessa autorità

Un agente che genera una bozza e un agente che può spostare denaro non sono la stessa cosa.

L'autonomia cresce soltanto insieme a:

- affidabilità dimostrata;
- osservabilità;
- reversibilità;
- controlli;
- accountability.

## 7. Un buon agente sa anche fermarsi

Non considero “non lo so” un fallimento quando l'evidenza non basta.

Definisco stop conditions.

Definisco escalation.

Mantengo la possibilità di interrompere il sistema.

## 8. Non confondo velocità con produttività

Produrre cento analisi non vale più che produrne dieci se le prime non meritano fiducia.

La metrica reale è:

> **output utile e affidabile per unità di tempo.**

## 9. Proteggo le competenze che mi permettono di governare

Non devo memorizzare ogni funzione.

Ma devo comprendere abbastanza bene i fondamentali da poter riconoscere quando qualcosa non torna.

Mantengo capacità in:

- analytical thinking;
- business understanding;
- data semantics;
- statistica;
- causalità;
- validazione;
- lettura di codice e query;
- comunicazione dell'incertezza.

## 10. Se l'AI e io siamo d'accordo, cerco comunque come potremmo sbagliarci

La conferma non è verifica.

Cerco:

- spiegazioni alternative;
- segmenti contrari;
- controlli indipendenti;
- failure mode;
- dati che potrebbero falsificare la mia ipotesi.

## 11. Più una decisione conta, più alzo la soglia

Un grafico interno e una decisione che incide su persone, soldi o sistemi critici richiedono livelli diversi di evidenza.

La verifica deve essere proporzionata al rischio.

## 12. Mantengo un owner umano

Ogni processo importante deve avere qualcuno che possa rispondere:

- cosa è successo?
- perché?
- quali dati sono stati usati?
- quali controlli sono passati?
- cosa può andare storto?
- come fermiamo o correggiamo il sistema?

Microsoft, nelle sue linee guida più recenti sugli agenti, insiste proprio su accountability, named owner, human oversight, audit logging e governance proporzionata al rischio. Il NIST AI RMF per Generative AI colloca gestione, misurazione e valutazione del rischio lungo l'intero ciclo di vita dei sistemi AI.

Fonti:
- https://learn.microsoft.com/en-us/agents/center-of-excellence/responsible-ai
- https://learn.microsoft.com/en-us/azure/security/fundamentals/shared-responsibility-ai-agent
- https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence

## La frase da ricordare

Possiamo riassumere tutto il capitolo in una regola.

> **Puoi delegare all'AI l'esecuzione. Puoi delegare l'esplorazione. Puoi delegare la prima bozza. Puoi delegare persino parte della verifica. Non puoi delegare la responsabilità di capire ciò che stai consegnando.**

Essere al timone non significa fare tutto.

Significa sapere dove stiamo andando, cosa sta facendo il sistema, quali segnali osservare, quando correggere la rotta e quando fermarsi.

Questo è il modo in cui useremo l'AI nel resto del libro.

Non come oracolo.

Non come alibi.

Come moltiplicatore di capacità sotto responsabilità umana.

> **Il nuovo standard professionale non è “l'ho fatto io”. È “posso difenderlo”.**