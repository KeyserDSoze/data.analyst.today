## 14.14 Checklist operativa: usare l'AI senza perdere il controllo
Prima di consegnare un'analisi assistita dall'AI, l'analista dovrebbe riuscire a rispondere a queste domande.

## Problema

- Qual è la decisione che dobbiamo supportare?
- La domanda è descrittiva, predittiva o causale?
- L'AI ha ricevuto abbastanza contesto business per interpretare correttamente la richiesta?

## Dati

- Quali fonti sono state usate?
- Sono certificate?
- Sono fresche, complete e coerenti con la finestra temporale?
- Sono stati esposti dati non necessari o sensibili?
- Gli accessi dell'agente rispettano il minimo privilegio?

## Semantica

- La metrica usata è quella ufficiale?
- Il grain è corretto?
- Date, filtri, denominatori e join sono stati verificati?
- Esistono definizioni alternative plausibili?

## Output generati

- Ho letto davvero la query o il codice?
- Ho verificato almeno un campione manualmente?
- Ho fatto sanity check sugli ordini di grandezza?
- Il risultato è coerente con metriche di controllo indipendenti?
- L'AI ha usato parole causali senza un design causale adeguato?

## Modelli e forecasting

- Esiste una baseline semplice?
- Lo split rispetta la temporalità?
- Ho escluso leakage?
- Le metriche riflettono il costo decisionale?
- L'errore è stato analizzato per segmento?
- La performance verrà monitorata dopo il deployment?

## Agentic workflow

- Chi è l'owner?
- Quali azioni può eseguire autonomamente?
- Quali richiedono approvazione umana?
- Qual è il criterio di stop?
- Come viene gestito un conflitto tra agenti?
- Esiste rollback?
- Possiamo ricostruire cosa è successo?

## Evaluation

- Esiste un eval set realistico?
- Include edge case rari ma costosi?
- Abbiamo controlli deterministici dove possibile?
- Gli LLM judge sono periodicamente auditati da persone competenti?
- Misuriamo la severità degli errori, non solo la percentuale di risposte corrette?

## Comunicazione

- Ho distinto fatti, inferenze e ipotesi?
- Ho dichiarato l'incertezza?
- Posso spiegare come siamo arrivati alla conclusione senza rifugiarmi in “l'ha detto l'AI”?
- Sarei in grado di difendere il risultato davanti a qualcuno che conosce il dominio meglio di me?

## La domanda finale

Prima di premere “send”, chiediamoci:

> **Se questa conclusione fosse sbagliata, saprei spiegare dove potrebbe essersi rotto il processo?**

Se la risposta è no, non siamo ancora al timone.

**L'AI può essere parte della catena di produzione dell'evidenza. La responsabilità della catena resta nostra.**
