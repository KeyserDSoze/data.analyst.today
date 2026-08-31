# 13.5 Cloud e scala: quando il laptop smette di essere il posto giusto

Il cloud non è automaticamente la risposta a ogni problema analitico. È utile quando permette di gestire scala, collaborazione, sicurezza, elasticità e integrazione meglio di un ambiente locale.

## 13.5.1 Il falso problema della scala

Molti team parlano di «big data» quando gestiscono dataset che entrano comodamente nella memoria di un laptop moderno.

Se un dataset ha 2 milioni di righe e l'analisi è occasionale, spostare tutto su un'architettura distribuita può aumentare complessità, latenza e costo senza creare valore.

La scala va misurata, non immaginata.

## 13.5.2 Quando il cloud diventa utile

Il cloud è particolarmente utile quando servono:

- grandi volumi;
- calcolo elastico;
- accesso condiviso;
- integrazione tra molte sorgenti;
- scheduling;
- sicurezza centralizzata;
- workload concorrenti;
- servizi gestiti;
- audit e governance;
- disaster recovery.

## 13.5.3 Caso realistico: l'analisi che funziona finché la fa una persona

Un retailer costruisce previsioni settimanali su 40 milioni di righe di vendite.

Sul laptop dell'analista senior il processo impiega 55 minuti e funziona.

Poi:

- tre analyst devono eseguirlo contemporaneamente;
- il dato cresce a 250 milioni di righe;
- il modello deve girare ogni notte;
- Finance vuole accesso allo stesso output;
- Security vieta copie locali del dataset clienti.

Il problema non è più solo computazionale. È operativo e organizzativo.

Qui il cloud diventa una scelta di sistema.

## 13.5.4 Costi: pagare per ciò che non capiamo

Nel cloud, una query o un job possono avere un costo marginale che in locale rimane invisibile.

Un analyst deve quindi imparare concetti come:

- dati scansionati;
- compute time;
- storage;
- egress;
- autoscaling;
- idle resources;
- caching;
- partition pruning.

La competenza analitica include anche capire quando una query scritta male consuma risorse sproporzionate.

## 13.5.5 Caso realistico: dashboard executive da 27.000 euro al mese

Una società costruisce un dashboard con 34 visualizzazioni, ognuna collegata direttamente a una tabella evento da miliardi di righe.

Ogni filtro genera nuove query. Centinaia di utenti aggiornano il dashboard durante la giornata.

Il costo cloud cresce fino a circa 27.000 euro al mese.

La soluzione non richiede un cloud più economico. Richiede un modello migliore:

- aggregazioni precomputate;
- partizionamento;
- caching;
- semantic model;
- riduzione delle query duplicate.

## 13.5.6 Locale e cloud sono complementari

Un workflow sano può essere:

1. SQL sul warehouse cloud per ridurre il dataset;
2. estrazione di un campione o tabella analitica;
3. EDA locale in Python;
4. trasformazione stabile riportata nella piattaforma centrale;
5. BI sul semantic layer.

L'obiettivo non è fare tutto nel cloud. È evitare movimenti inutili e mantenere la logica critica nel posto giusto.

> **Il cloud non risolve la complessità. La rende scalabile — nel bene e nel male.**
