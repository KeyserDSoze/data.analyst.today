## 2.3 Stakeholder: chi chiede non è sempre chi decide

Una richiesta analitica attraversa spesso più ruoli.

Chi invia il ticket può non essere chi utilizzerà il risultato. Chi utilizza il report può non avere autorità decisionale. Chi decide può avere vincoli che non sono stati comunicati all'analista.

Per questo è utile distinguere almeno quattro figure:

- **requester**: chi formula la richiesta;
- **domain expert**: chi conosce processo e significato dei dati;
- **decision owner**: chi prende la decisione;
- **end user**: chi utilizza concretamente il prodotto analitico.

A volte coincidono. Spesso no.

### Perché questa distinzione cambia l'analisi

Immaginiamo che Marketing chieda:

> "Costruiamo un report sul costo di acquisizione cliente."

Il requester è il marketing manager.

Ma Finance potrebbe stabilire quali costi debbano essere inclusi. Il CRM owner potrebbe conoscere i problemi di tracciamento. Il Chief Marketing Officer potrebbe essere la persona che decide il budget trimestrale. I campaign manager potrebbero essere gli utenti quotidiani del report.

Se parliamo soltanto con chi ha aperto la richiesta, possiamo costruire qualcosa di tecnicamente corretto ma organizzativamente sbagliato.

### Stakeholder interview

Una breve intervista iniziale dovrebbe chiarire:

1. **Quale problema stiamo cercando di risolvere?**
2. **Quale decisione verrà presa?**
3. **Chi la prenderà?**
4. **Quando deve essere presa?**
5. **Quali alternative sono realmente disponibili?**
6. **Quali metriche vengono già utilizzate?**
7. **Dove esistono disaccordi sulle definizioni?**
8. **Quali vincoli economici, normativi o operativi esistono?**
9. **Che cosa renderebbe l'analisi inutilizzabile?**
10. **Come capiremo, dopo la consegna, se il lavoro è stato utile?**

### Il dominio è parte del dato

Una colonna denominata `status = closed` sembra precisa. Ma cosa significa *closed* nel processo reale?

Un ticket chiuso può significare:

- problema risolto;
- richiesta duplicata;
- cliente non raggiungibile;
- pratica annullata;
- chiusura automatica dopo un certo numero di giorni.

Il domain expert può evitare settimane di analisi sbagliata spiegando in dieci minuti la semantica reale del processo.

### Non limitarsi a raccogliere requisiti

L'analista non è un cameriere dei requisiti.

Se lo stakeholder chiede venti grafici, il compito non è necessariamente costruire venti grafici. È capire che cosa sta cercando di sapere e proporre il modo più efficace per scoprirlo.

Questo richiede una relazione collaborativa: l'analista porta metodo quantitativo; lo stakeholder porta contesto, vincoli e conoscenza del dominio.

## Deliverable: stakeholder map

Per analisi importanti, annota almeno:

| Ruolo | Persona/Team | Cosa sa | Cosa decide | Cosa gli serve |
|---|---|---|---|---|
| Requester |  |  |  |  |
| Domain expert |  |  |  |  |
| Decision owner |  |  |  |  |
| End user |  |  |  |  |

Non è burocrazia: è un modo semplice per evitare di ottimizzare l'analisi per la persona sbagliata.