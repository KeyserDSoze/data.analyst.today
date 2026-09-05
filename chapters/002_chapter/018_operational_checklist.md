## 2.17 Pre-flight: il brief è pronto per l'esecuzione?

Dopo avere costruito il brief in prosa e discusso le dipendenze fra decisione, metriche, ipotesi, scope e dati, qui la forma cambia intenzionalmente. Questa sezione **deve** essere scansionabile: è un controllo operativo da usare prima di aprire il tool, non un altro pezzo di teoria.

La domanda del pre-flight è semplice: il brief contiene abbastanza informazioni da permettere a stakeholder, analyst e data owner di iniziare il lavoro senza interpretazioni materialmente incompatibili?

### Decisione

- Il problema di business è espresso senza confonderlo con il deliverable?
- La decisione è identificata?
- Esiste un decision owner?
- Le alternative disponibili sono note almeno a grandi linee?
- Deadline o frequenza della decisione sono chiare?
- Conosciamo il costo principale dell'errore?

### Domanda

- Esiste una domanda analitica primaria?
- Il tipo di domanda è dichiarato?
- È chiaro quale livello di pretesa potrà sostenere l'analisi?
- Le domande secondarie sono realmente subordinate alla primaria?

### Metriche

- L'outcome primaria è definita?
- Popolazione, numeratore e denominatore sono espliciti quando servono?
- Driver e guardrail hanno un ruolo chiaro?
- Target o soglie decisionali sono documentati se esistono?
- Metric owner o definizione autorevole sono identificati?

### Scope

- Popolazione ed esclusioni sono chiare?
- Unità di analisi e grain richiesto sono coerenti?
- Campo temporale e finestra di osservazione sono definiti?
- Abbiamo considerato maturazione e data latency?
- È esplicito ciò che resta fuori scope?

### Confronto e segmentazione

- La baseline risponde alla domanda corretta?
- I periodi o gruppi sono comparabili?
- Le segmentazioni prioritarie hanno una motivazione decisionale o teorica?
- Distingueremo tagli pre-specificati da esplorazioni emerse dopo?

### Ipotesi

- Le spiegazioni principali sono esplicite?
- Per ciascuna sappiamo quale evidenza la rafforzerebbe o indebolirebbe?
- Esiste almeno una spiegazione alternativa alla narrativa iniziale dello stakeholder?
- Abbiamo incluso possibili problemi di misurazione tra le ipotesi quando plausibili?

### Dati

- I dati required sono distinti da useful e proxy?
- Sappiamo quali fonti esistono davvero?
- Grain, storico, freshness e owner sono noti per le fonti critiche?
- I gap sono documentati con una strategia di mitigazione?

### Piano e sufficienza

- Il metodo iniziale è il più semplice capace di rispondere alla domanda?
- Conosciamo i controlli minimi da eseguire prima di concludere?
- Esiste una stop rule?
- Abbiamo previsto che l'esito possa essere inconcludente?
- È chiaro quale informazione aggiuntiva avrebbe più valore se il primo ciclo non bastasse?

### Output

- Il formato deriva dalla decisione e non dalla richiesta iniziale?
- Il criterio di successo descrive utilità decisionale e non solo consegna tecnica?
- Se il brief cambia durante il lavoro, sappiamo chi deve essere riallineato?

### E se useremo l'AI?

Non serve una checklist parallela. Le regole di supervisione sono già state fissate nel Capitolo 0 e i workflow tecnici arriveranno nel Capitolo 14. Nel brief l'AI deve operare **dentro lo stesso contratto**: stessa metrica, stesso scope, stesse fonti, stessa pretesa massima e stessi limiti.

Una query generata automaticamente non può estendere da sola la popolazione. Un agente non può sostituire la metrica primaria con una definizione più comoda. Se l'esplorazione produce una ragione valida per cambiare il piano, non cambia soltanto il prompt: **cambia il brief**, e le persone rilevanti vengono riallineate.

Il pre-flight non certifica che conosciamo già la risposta. Certifica qualcosa di più utile prima dell'esecuzione: sappiamo che cosa significherà cercarla bene e quali condizioni dovranno essere rispettate prima di credere al risultato.
