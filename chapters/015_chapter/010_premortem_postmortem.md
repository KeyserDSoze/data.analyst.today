## 15.9 Pre-mortem e post-mortem: imparare prima e dopo la decisione
Le organizzazioni spesso analizzano gli errori solo dopo che qualcosa è andato storto.

Ma una parte del valore analitico consiste nel cercare i failure mode **prima** di impegnarsi.

## Il pre-mortem

Immaginiamo di aver preso una decisione e che, sei mesi dopo, abbia fallito.

La domanda è:

> “Quali sono le ragioni più plausibili per cui è successo?”

Questo esercizio forza il team a cercare vulnerabilità che l'entusiasmo iniziale tende a nascondere.

## Caso realistico: rollout di un nuovo pricing

Una SaaS decide di aumentare il prezzo del piano Pro del 15%.

Il business case è positivo.

Prima del rollout, il team fa un pre-mortem.

Possibili failure mode:

- churn enterprise superiore alle attese;
- aumento dei ticket di supporto;
- sales discounting che annulla il prezzo di listino;
- competitors che usano l'aumento in campagne comparative;
- metrica ARR in crescita ma NRR in deterioramento;
- effetti diversi tra clienti nuovi ed esistenti.

Da questo pre-mortem nascono controlli concreti:

- rollout a coorti;
- guardrail su churn e NRR;
- tracking degli sconti commerciali;
- monitoraggio competitor;
- stop condition se il downside supera una soglia.

Il pre-mortem non serve a bloccare la decisione.

Serve a renderla più governabile.

## Il post-mortem

Dopo l'azione, il team dovrebbe confrontare:

- cosa ci aspettavamo;
- cosa è successo;
- quali assunzioni erano sbagliate;
- quali segnali avevamo ignorato;
- quali controlli hanno funzionato;
- cosa cambieremo nel processo successivo.

## Evitare il blame game

Un buon post-mortem non chiede soltanto:

> “Chi ha sbagliato?”

Chiede:

> **“Quale parte del sistema decisionale ha permesso che questo errore fosse plausibile?”**

Se un dashboard aveva dati stale, il problema non è solo chi non li ha controllati.

Potrebbe esserci:

- ownership ambigua;
- assenza di freshness alert;
- metriche non certificate;
- processo di review troppo debole;
- decision threshold incoerente col rischio.

## Closing the loop

La qualità di un'organizzazione analitica cresce quando chiude il ciclo:

**ipotesi → decisione → azione → risultato → confronto con attese → apprendimento**

Senza questa parte finale, ogni progetto ricomincia da zero.

**Un post-mortem ben fatto trasforma un errore passato in una riduzione di rischio futuro.**
