# Capitolo 4 - Statistica descrittiva ed Exploratory Data Analysis

> Prima di modellare, prevedere o spiegare, bisogna imparare a guardare davvero i dati.

La statistica descrittiva non è una collezione di formule. È un linguaggio per sintetizzare distribuzioni, confrontare gruppi, individuare anomalie e capire se ciò che osserviamo merita un approfondimento.

L'Exploratory Data Analysis, o EDA, è il momento in cui l'analista prova a capire che forma ha il fenomeno prima di costruire una spiegazione definitiva.

In questo capitolo useremo casi simulati ma realistici: e-commerce, logistica, customer support, SaaS e retail. L'obiettivo non è imparare a calcolare una media in astratto, ma capire quando una media aiuta e quando inganna.

## Caso di apertura: il tempo medio di consegna è migliorato

Una società di logistica comunica al management che il tempo medio di consegna è passato da 3,8 a 3,1 giorni in un trimestre.

La notizia sembra positiva.

Poi un'analista segmenta i dati per area geografica e scopre che:

- le consegne urbane sono passate da 2,1 a 1,8 giorni;
- le consegne rurali sono passate da 5,6 a 6,4 giorni;
- la quota di ordini urbani sul totale è cresciuta dal 58% al 74%.

La media complessiva è migliorata soprattutto perché è cambiato il mix degli ordini.

La domanda cambia immediatamente da:

**"Abbiamo migliorato la logistica?"**

a:

**"Abbiamo davvero migliorato il processo o stiamo semplicemente servendo una popolazione diversa?"**

Questa è la mentalità dell'EDA: non accettare il primo riassunto disponibile come se fosse la realtà intera.
