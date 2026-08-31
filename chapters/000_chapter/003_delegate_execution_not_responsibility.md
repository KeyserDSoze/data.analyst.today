## 0.2 Delegare l'esecuzione, non la responsabilità

L'AI rende possibile separare due cose che per molto tempo sono state quasi inseparabili:

- **fare materialmente il lavoro**;
- **rispondere professionalmente del lavoro**.

Questa separazione non è un dettaglio organizzativo. È una delle competenze centrali del lavoro AI-native.

Un analista può non scrivere personalmente una query e restare responsabile del numero che quella query produce. Può non addestrare a mano un modello e restare responsabile di come quel modello viene usato. Può non preparare la prima bozza di una presentazione e restare responsabile del messaggio consegnato al management.

La domanda non è quindi “chi ha premuto i tasti?”.

La domanda è:

> **chi è in grado di spiegare, difendere, fermare e correggere il processo?**

### Il falso dilemma

Quando si parla di AI emergono spesso due estremi.

Il primo è rifiutare la delega:

> “Se non scrivo io il codice, non mi fido.”

È una posizione che spreca una capacità utile. Se una parte dell'esecuzione può essere accelerata senza perdere controllo, non esiste un merito professionale nel farla più lentamente per principio.

Il secondo estremo è delegare anche il giudizio:

> “Se il modello l'ha detto, sarà giusto.”

Questo è più pericoloso, perché trasforma uno strumento di amplificazione in un sostituto della responsabilità.

La posizione professionale sta altrove:

> **delegare ciò che può essere delegato, mantenendo ownership su obiettivo, assunzioni, evidenze, controlli e decisione.**

### Caso simulato/composito: il report del lunedì

Un'azienda B2B automatizza il weekly business review.

Ogni lunedì un agente:

1. estrae i KPI;
2. confronta i risultati con forecast e anno precedente;
3. identifica anomalie;
4. genera possibili spiegazioni;
5. prepara una slide con raccomandazioni.

Per otto settimane il processo funziona bene.

Alla nona, il report mostra:

- pipeline coverage: +22%;
- expected bookings: +14%;
- raccomandazione: aumentare il target del trimestre.

Il VP Sales nota però un'incongruenza: il numero di opportunità aperte non è cresciuto.

L'indagine scopre che una modifica al CRM ha duplicato il valore di alcune opportunità multi-currency durante il consolidamento.

L'agente non aveva inventato un numero. Aveva letto correttamente un dato sbagliato e costruito sopra di esso una raccomandazione coerente.

È un tipo di errore molto più insidioso dell'allucinazione evidente: **input plausibile, elaborazione plausibile, conclusione plausibile, decisione sbagliata**.

Il fatto che il report fosse automatico non riduce la necessità di un owner. La aumenta.

### Ogni output importante deve avere un owner

L'owner non deve eseguire personalmente ogni passaggio. Deve sapere abbastanza da governarlo.

Per un processo analitico rilevante dovrebbe poter rispondere almeno a queste domande:

- da quali sistemi arriva il dato?
- quale definizione delle metriche viene usata?
- quali trasformazioni sono critiche?
- quali controlli devono passare?
- quali failure mode conosciamo?
- che cosa succede quando i controlli falliscono?
- chi può fermare o correggere il processo?

Un workflow senza owner è un processo nel quale l'errore può circolare senza che nessuno abbia l'obbligo di comprenderlo.

### “Show me the evidence”

Una conclusione importante non dovrebbe terminare con una frase. Dovrebbe essere accompagnata da un percorso verificabile.

Se un agente dice:

> “La Francia è il principale driver del calo.”

l'analista deve poter vedere la decomposizione del delta.

Se dice:

> “La campagna ha causato un aumento delle vendite.”

deve essere possibile ricostruire il disegno causale e capire quali alternative sono state escluse.

Se dice:

> “Il modello è migliorato.”

servono baseline, split, metriche e risultati fuori campione.

Le evidenze possono includere:

- query e trasformazioni;
- filtri e popolazioni;
- definizioni metriche;
- sorgenti;
- conteggi e reconciliation;
- test;
- grafici diagnostici;
- ipotesi alternative;
- limiti conosciuti.

Questo non significa mostrare tutto a tutti. Significa rendere il risultato **ispezionabile**.

### Un disclaimer non crea accountability

Scrivere sotto un report:

> “Output generato dall'AI. Verificare prima dell'uso.”

può essere utile per comunicare la natura dell'output, ma non sostituisce un processo di review se il report viene davvero usato per prendere decisioni.

L'accountability non si delega a una nota a piè di pagina.

### La regola di proporzionalità

Più un'azione è costosa, irreversibile, visibile esternamente o impattante su persone, denaro e compliance, più l'owner deve richiedere evidenze forti e approvazioni esplicite.

Nei task a basso rischio la review può essere leggera. Nei processi critici deve diventare parte del design.

> **La capacità dell'AI modifica chi esegue il lavoro. Non cancella la necessità di sapere chi ne risponde.**
