## 2.16 Quando la conclusione corretta è “non sappiamo ancora abbastanza”

Una stop rule deve prevedere un esito che molte culture aziendali tollerano male: **i dati disponibili non hanno guadagnato il diritto di sostenere una conclusione più forte**.

Questo risultato non implica automaticamente che l'analisi sia fallita. Può essere precisamente ciò che il brief doveva scoprire. Un campione piccolo, un tracking non comparabile, una variabile decisiva non osservata o due spiegazioni che producono lo stesso pattern possono rendere impossibile scegliere una storia senza inventare certezza.

L'errore professionale non consiste nell'incontrare questo limite. Consiste nel nasconderlo dietro una narrazione più netta di quanto l'evidenza permetta.

## “Non abbiamo evidenza” non significa sempre “non esiste”

Tre situazioni vengono confuse frequentemente.

Nel primo caso **non abbiamo trovato evidenza convincente di un effetto**. Il risultato può dipendere da un effetto realmente piccolo, ma anche da dati troppo rumorosi o insufficienti.

Nel secondo caso disponiamo di dati abbastanza informativi da dire che **un effetto materialmente rilevante è improbabile**. Questa è una conclusione più forte: non stiamo soltanto fallendo nel rilevare qualcosa, stiamo escludendo una parte importante degli effetti che avrebbero contato per la decisione.

Nel terzo caso l'incertezza è così ampia che i dati restano compatibili sia con un effetto trascurabile sia con uno materialmente importante. Qui la risposta corretta è che **non distinguiamo ancora tra le due possibilità**.

Trasformare il primo o il terzo caso in “non c'è effetto” non semplifica il messaggio; cambia il significato statistico e decisionale della conclusione.

## Un esito inconcludente deve comunque ridurre l'incertezza

Una buona consegna non si limita a dire “non è emerso niente”. Deve spiegare che cosa è stato verificato, quali pattern sono compatibili con i dati, quale affermazione non possiamo sostenere e perché. Deve poi collegare quel limite alla decisione: possiamo scegliere comunque l'opzione più reversibile? Conviene raccogliere più campione? Serve migliorare la misurazione? Un esperimento avrebbe più valore di un'altra analisi osservazionale?

Consideriamo due onboarding flow. Nei dati disponibili il flow B mostra retention a 30 giorni superiore di circa **3 punti percentuali**, ma il campione è piccolo e l'intervallo compatibile con i dati include sia un effetto trascurabile sia un effetto materialmente utile.

Una conclusione professionale potrebbe essere:

> “Nei dati disponibili il flow B mostra retention a 30 giorni superiore di circa 3 punti percentuali, ma il campione è piccolo e l'incertezza include sia un effetto trascurabile sia un effetto materialmente utile. Non raccomandiamo un rollout globale sulla base di questa evidenza. Il prossimo passo con maggiore valore è estendere l'esperimento fino al campione pianificato mantenendo invariata la metrica primaria.”

Questa frase non nasconde l'incertezza, ma non rinuncia a guidare il passo successivo.

## Il prossimo passo compete sul Value of Information

Quando il primo ciclo non conclude, la domanda non dovrebbe essere automaticamente “come possiamo analizzare ancora?”. La domanda corretta è:

> **“Quale nuova informazione ha la probabilità più alta di cambiare la decisione?”**

Forse serve più campione. Forse serve un campo di exposure che oggi non viene tracciato. Forse serve un esperimento. Forse nessuna informazione aggiuntiva vale il costo perché tutte le alternative plausibili portano comunque alla stessa scelta.

Anche “non agire per ora” è una decisione, purché sia coerente con il costo dell'errore e con il valore dell'attesa. L'assenza di una conclusione causale non rende impossibile ogni azione; può spingerci verso un intervento più piccolo, reversibile e osservabile.

Per analisi ad alto rischio può essere utile pre-accettare nel brief più di un esito legittimo:

```text
A. Evidenza sufficiente per raccomandare un'azione.
B. Evidenza sufficiente per escludere alcune azioni ma non scegliere tra le restanti.
C. Evidenza insufficiente: specificare il prossimo dato/test con maggiore Value of Information.
```

Questa struttura è particolarmente utile quando parte della sintesi viene prodotta con sistemi generativi, che tendono naturalmente a chiudere la storia in una risposta completa. La completezza linguistica non deve avere più valore della completezza dell'evidenza.

> **Un'analisi professionale non promette sempre una risposta netta. Promette che il livello di certezza dichiarato sarà quello che i dati hanno realmente guadagnato.**
