## 2.3 Stakeholder: chi chiede non è sempre chi decide

Una richiesta analitica attraversa spesso più ruoli.

Chi apre il ticket può non essere chi userà il risultato. Chi usa il report può non avere autorità decisionale. Chi decide può dipendere da definizioni possedute da un altro team. Chi conosce il processo reale può non essere stato coinvolto affatto.

Per questo, nelle analisi importanti, conviene distinguere almeno cinque figure:

- **requester** — formula la richiesta;
- **decision owner** — può agire sul risultato;
- **domain expert** — conosce processo, eccezioni e significato operativo;
- **data/metric owner** — conosce fonte, trasformazioni o definizione ufficiale;
- **end user** — utilizza concretamente l'output.

A volte coincidono. Spesso no.

### Caso simulato/composito: un CAC, quattro interpretazioni

Marketing chiede:

> “Costruiamo un report sul Customer Acquisition Cost.”

Il marketing manager è il requester. Il CMO userà il numero per allocare budget. Finance stabilisce quali costi devono entrare nel calcolo. Il CRM owner conosce i limiti dell'attribuzione. I campaign manager sono gli utenti quotidiani del report.

Se l'analista parla soltanto con chi ha aperto la richiesta, può costruire un CAC tecnicamente consistente con i dati marketing ma incompatibile con la definizione usata da Finance per il budget.

Il problema non è una formula sbagliata.

È **ownership semantica non mappata**.

### Il disaccordo è informazione

Se due stakeholder danno definizioni diverse di “cliente acquisito”, “revenue” o “lead qualificato”, non bisogna nascondere il conflitto scegliendo una versione in silenzio.

Il disaccordo rivela un requisito del progetto:

- serve una definizione condivisa?
- servono due metriche diverse per due decisioni diverse?
- chi ha autorità sulla definizione?
- la divergenza deve essere documentata come limite?

Una stakeholder interview non serve soltanto a raccogliere requisiti. Serve anche a trovare **incompatibilità prima che entrino nel codice**.

### Domande iniziali

Una breve intervista dovrebbe chiarire almeno:

1. Quale problema stiamo cercando di risolvere?
2. Quale decisione verrà presa e da chi?
3. Quando deve essere presa?
4. Quali alternative sono realmente disponibili?
5. Quali metriche vengono già usate?
6. Dove esistono disaccordi sulle definizioni?
7. Chi conosce le eccezioni operative?
8. Chi possiede le fonti o le metriche critiche?
9. Quali vincoli economici, normativi o operativi esistono?
10. Che cosa renderebbe l'analisi inutilizzabile?

### Il dominio è parte del dato

Una colonna `status = closed` sembra precisa. Nel processo reale, però, *closed* può significare:

- problema risolto;
- richiesta duplicata;
- cliente non raggiungibile;
- pratica annullata;
- chiusura automatica dopo un certo numero di giorni.

Il domain expert può evitare giorni di analisi sbagliata spiegando in dieci minuti il significato operativo di uno stato.

Questo è un motivo per cui il contesto di business non è un'aggiunta “soft” all'analisi. È parte del modello dei dati.

### L'analista non è un raccoglitore passivo di requisiti

Se lo stakeholder chiede venti grafici, il compito non è automaticamente costruire venti grafici.

L'analista deve capire che cosa lo stakeholder sta cercando di sapere, quali decisioni ha davanti e quale prodotto analitico sarebbe sufficiente.

La relazione è collaborativa:

- il business porta contesto, vincoli e possibilità d'azione;
- i domain e data owner portano significato e conoscenza delle fonti;
- l'analista porta struttura, metodo e disciplina dell'evidenza.

### Campo del brief: stakeholder map

| Ruolo | Persona/Team | Conoscenza/ownership | Decisione o uso | Coinvolgimento necessario |
|---|---|---|---|---|
| Requester |  |  |  |  |
| Decision owner |  |  |  |  |
| Domain expert |  |  |  |  |
| Data/metric owner |  |  |  |  |
| End user |  |  |  |  |

> **Mappare gli stakeholder significa capire dove vive il contesto necessario perché una domanda analitica abbia lo stesso significato per tutti.**
