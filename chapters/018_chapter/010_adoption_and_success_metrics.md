## 18.9 Adoption: un prodotto analitico non crea valore perché esiste

Una dashboard può essere tecnicamente eccellente e non entrare mai in una decisione. Un semantic layer può essere interrogato da centinaia di persone e continuare a produrre discussioni su che cosa significhi `revenue`. Un modello può generare score ogni ora e non modificare nessuna azione operativa.

Per questo **availability, usage, adoption e value non sono sinonimi**. Il cost-to-serve della sezione precedente acquista significato soltanto quando sappiamo quale parte del servizio viene realmente incorporata nei processi decisionali.

Microsoft, nella Fabric Adoption Roadmap, distingue organizzazione, utenti e singole soluzioni e sottolinea che statistiche di utilizzo sono segnali utili ma non dimostrano, da sole, un uso efficace dell'analytics.

Fonti:
- https://learn.microsoft.com/en-us/power-bi/guidance/fabric-adoption-roadmap
- https://learn.microsoft.com/en-us/power-bi/guidance/fabric-adoption-roadmap-maturity-levels

## Dall'accesso all'outcome: l'adoption ladder

La progressione utile non è “pubblicato → usato”. È:

**availability → discoverability → usage → effective use → decision embedding → outcome**.

**Availability** significa soltanto che il prodotto esiste ed è accessibile. **Discoverability** aggiunge la capacità del consumer di trovarlo e capire per quale problema sia autorevole. **Usage** misura sessioni, query, report view o API call. È facile da osservare, ma dice ancora poco sulla correttezza dell'uso.

Con **effective use** chiediamo se il consumer usa la metrica certificata invece della copia locale, interpreta correttamente denominatore e caveat e non deve esportare il numero per ricostruirlo manualmente altrove. **Decision embedding** è il salto successivo: il prodotto entra davvero nel weekly pricing meeting, nel capacity plan, nel workflow Customer Success o nel closing Finance. Solo a quel punto possiamo cercare **outcome** come minore tempo per decidere, meno reconciliation, meno decisioni prese su dati non ready, migliore planning o riduzione del cost-to-serve.

Non sempre l'outcome sarà causalmente attribuibile al prodotto. La disciplina sta nel non fermarsi alla vanity metric più semplice.

## 1.200 utenti e lo stesso meeting che comincia con “quale revenue?”

Un'azienda lancia un portale self-service. Dopo sei mesi conta 1.200 utenti registrati, 18.000 sessioni mensili, 320 dashboard e il 74% dei manager che dichiara di averlo usato almeno una volta nel mese. Il programma viene definito un successo.

Il monthly business review, però, continua a iniziare con “quale revenue stiamo usando?”. Un audit trova 23 definizioni di `active_customer`, 11 varianti di `net_revenue`, il 41% delle dashboard executive su dataset non certificati e quasi quattro ore medie di reconciliation prima del meeting.

L'accesso è aumentato. Il significato condiviso no. Il sistema ha migliorato availability e usage, non effective use né decision embedding.

Questo caso mostra perché un adoption failure non è automaticamente un user failure. Se un prodotto viene usato male, il problema può essere scarsa discoverability, troppe alternative quasi equivalenti, naming incomprensibile, freshness insufficiente, workflow separato dal processo reale, mancanza di fiducia dopo incidenti, nessun owner visibile o nessuna distinzione tra `experimental` e `certified`.

Dire “gli utenti non sono data-driven” è spesso il modo più rapido per evitare una product diagnosis.

## Tre prospettive diverse sull'adozione

La Fabric Adoption Roadmap distingue **organizational adoption**, cioè governance, supporto e pratiche che rendono possibile l'uso corretto; **user adoption**, cioè uso effettivo ed efficace da parte delle persone; e **solution adoption**, cioè valore prodotto dalla specifica soluzione.

Fonte: https://learn.microsoft.com/en-us/power-bi/guidance/fabric-adoption-roadmap-maturity-levels

Per un prodotto critico questa distinzione può diventare una scorecard:

| Dimensione | Evidenza utile |
|---|---|
| Reach | consumer target raggiunti, discoverability, access success |
| Usage | utenti attivi, frequenza, query/report view |
| Effective use | quota su metriche certificate, misunderstanding, support request ripetitive |
| Workflow | processi decisionali che usano il prodotto, tempo domanda→risposta |
| Outcome | reconciliation evitate, errori/rischi ridotti, decision time, valore operativo/economico |

La scorecard non richiede una metrica perfetta per ogni cella. Richiede però di non comprimere tutta l'adozione in `monthly active users`.

## A volte una buona adozione fa diminuire le metriche di attività

Se due dashboard duplicate vengono ritirate a favore di un prodotto certificato, il numero di asset e query può scendere mentre il sistema migliora. Se un alert diventa più preciso, le notifiche diminuiscono. Se un feed entra direttamente nel workflow operativo, gli utenti possono aprire meno dashboard.

Quindi una metrica di adoption deve riflettere il comportamento desiderato, non l'attività massima. Anche qui il Decision Record aiuta: se sappiamo quale processo vogliamo migliorare, possiamo scegliere una misura coerente con quel processo.

## Retirement è una forma di successo

Un asset che nessun decision process usa più non dovrebbe restare `CERTIFIED` indefinitamente. L'Operating Contract deve prevedere retirement trigger: nessun consumer decisionale, usage sotto soglia per più periodi, successore certificato, cost-to-serve superiore al valore residuo, semantica non più valida.

Prima di spegnerlo vanno verificati lineage e consumer reali; dopo il retirement, catalogo e documentazione devono indicare chiaramente il successore. Il portfolio scala anche attraverso ciò che smette di mantenere.

Questo chiude il legame con cost management: una dashboard costosa e poco usata non è automaticamente da eliminare se sostiene un processo trimestrale critico; una dashboard economica e molto usata non è automaticamente di valore se perpetua definizioni incoerenti. **Adoption e economics devono essere letti attraverso la decisione.**

La domanda finale non è quindi “quante persone usano questa dashboard?”, ma:

> **Quale decisione viene presa meglio, più velocemente o con meno ambiguità perché questo prodotto esiste?**

Se non sappiamo nominarla, abbiamo ancora un problema di product design.

> **Un prodotto analitico realizza valore quando entra nel flusso di una decisione e riduce un rischio reale, non quando accumula visualizzazioni.**

Questo vale anche per il prodotto più nuovo del portfolio: un agente AI. La differenza è che, oltre a produrre informazione, può disporre di tool e autorità. Per questo il suo operating model deve governare non soltanto qualità dell'output, ma autonomia, revoca e blast radius.