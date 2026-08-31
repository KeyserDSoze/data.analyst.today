## 13.3 Python, R e notebook: quando l'analisi diventa programmabile
Python e R diventano particolarmente utili quando l'analisi richiede più flessibilità di quella offerta da SQL o da un foglio di calcolo.

Il vantaggio principale non è semplicemente «poter scrivere codice». È poter descrivere un processo analitico complesso in modo ripetibile, estendibile e verificabile.

## 13.3.1 Quando il codice aggiunge davvero valore

Python o R sono una scelta naturale quando servono:

- statistica avanzata;
- machine learning;
- simulazioni;
- ottimizzazione;
- elaborazioni iterative;
- analisi di testo o immagini;
- automazione personalizzata;
- grafici diagnostici;
- integrazione con API;
- pipeline analitiche non facilmente esprimibili in SQL.

## 13.3.2 Caso realistico: 600 segmentazioni possibili

Un marketplace vuole capire quali combinazioni di categoria, paese, canale e tenure mostrano il maggiore deterioramento della retention.

Le combinazioni possibili sono centinaia.

Costruire manualmente pivot e grafici sarebbe lento e fragile. In Python o R possiamo generare sistematicamente:

- cohort table;
- intervalli di confidenza;
- ranking dei cambiamenti;
- grafici;
- controlli di numerosità;
- export di una sintesi finale.

Qui il codice non è un vezzo tecnico. Riduce il lavoro ripetitivo e rende l'analisi più completa.

## 13.3.3 Il notebook come laboratorio

Un notebook combina:

- codice;
- testo;
- formule;
- output;
- visualizzazioni.

Questo lo rende molto efficace per EDA, ricerca, prototipazione e comunicazione tecnica.

Ma un notebook può diventare fragile se:

- le celle vengono eseguite fuori ordine;
- lo stato in memoria non è chiaro;
- i dati cambiano senza versionamento;
- dipendenze e ambiente non sono documentati;
- il notebook diventa una pipeline produttiva nascosta.

## 13.3.4 Caso realistico: il notebook che funziona solo sul laptop di Marco

Un modello di forecasting viene presentato al management con ottimi risultati.

Due settimane dopo un altro analyst prova a riprodurlo e ottiene errori.

Scopre che:

- il notebook dipende da un CSV locale non versionato;
- una libreria è stata aggiornata;
- alcune celle devono essere eseguite in un ordine specifico;
- due variabili sono rimaste in memoria da una sessione precedente.

Il problema non è Python. È la mancanza di disciplina operativa.

## 13.3.5 Dal notebook al processo

Quando un'analisi diventa ricorrente, conviene separare:

1. configurazione;
2. acquisizione dati;
3. trasformazioni;
4. funzioni analitiche;
5. test;
6. output.

Il notebook può restare come interfaccia esplorativa, mentre la logica stabile passa in moduli o pipeline versionate.

## 13.3.6 Python o R?

Non esiste una risposta universale.

Python è molto diffuso perché integra analytics, automazione, API, ML e software engineering in un ecosistema unico.

R rimane particolarmente forte in statistica, ricerca, visualizzazione e numerosi workflow accademici e scientifici.

Per un Data Analyst la scelta può dipendere da:

- stack aziendale;
- competenze del team;
- librerie necessarie;
- facilità di deployment;
- standard interni.

Il principio resta invariato: **non scegliere un linguaggio per identità professionale; sceglilo per il problema e per l'ambiente in cui il lavoro deve vivere.**

## 13.3.7 Il costo nascosto della flessibilità

Più uno strumento è flessibile, più aumenta la responsabilità dell'analista.

In un foglio, molte scelte sono già imposte dall'interfaccia. Nel codice possiamo fare quasi tutto, incluso costruire pipeline difficili da comprendere, testare o mantenere.

Per questo il codice richiede disciplina:

- naming chiaro;
- versionamento;
- test;
- gestione delle dipendenze;
- logging;
- documentazione;
- controlli sui dati.

> **La programmabilità aumenta ciò che possiamo fare. Aumenta anche il numero di modi in cui possiamo sbagliare.**

### Fonti

- pandas documentation: https://pandas.pydata.org/docs/
- Project Jupyter: https://jupyter.org/
