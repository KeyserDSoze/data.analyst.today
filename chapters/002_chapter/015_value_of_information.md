## 2.14 Value of Information: quanto vale sapere qualcosa in più?

La prioritizzazione decide quale domanda merita capacità analitica. Il **Value of Information** aiuta a decidere quanto approfondirla prima di agire.

L'idea è economica prima ancora che statistica: un'informazione aggiuntiva ha valore quando ha una possibilità realistica di cambiare una decisione o di ridurre un rischio che conta. Questo criterio protegge da due errori opposti. Possiamo fermarci troppo presto e prendere una decisione costosa sulla base di evidenza fragile; oppure possiamo continuare a perfezionare l'analisi quando la scelta non cambierebbe comunque.

### Caso simulato/composito: due giorni prima di spendere €2 milioni

Un'azienda sta per investire **€2 milioni** in una nuova campagna di acquisizione. Il business case presume che il segmento target abbia economics simili ai clienti acquisiti l'anno precedente. Prima del lancio, il team dedica due giorni a un controllo mirato e scopre che il churn del nuovo segmento è molto più alto e che il payback atteso supera ampiamente l'orizzonte accettato dal business.

L'analisi non deve essere perfetta per avere enorme valore. Se quei due giorni cambiano la decisione di spendere €2 milioni o impongono un test più piccolo, il valore dell'informazione può essere ordini di grandezza superiore al suo costo.

Consideriamo ora il caso opposto. Un forecast passa dal 93% al 94% di accuratezza dopo tre settimane di tuning, ma staffing, stock e budget rimangono identici in tutto il range di previsioni plausibili. Il modello è migliorato; la decisione no. In quel contesto l'informazione marginale può valere molto meno delle tre settimane impiegate per ottenerla.

## Informazione sufficiente, non informazione perfetta

Nel lavoro reale raramente possiamo eliminare tutta l'incertezza. Cerchiamo un livello di evidenza sufficiente rispetto al costo dell'errore e al costo di aspettare.

Una prima decomposizione può cambiare completamente il piano; la ventesima segmentazione aggiunge magari dettaglio senza modificare nulla. Questo rendimento decrescente è ciò che collega Value of Information e stop rule: ogni nuovo approfondimento dovrebbe giustificare il proprio costo mostrando quale incertezza importante potrebbe ancora ridurre.

La reversibilità della decisione cambia il calcolo. Se un piccolo test può essere annullato rapidamente e il costo di aspettare è alto, può essere razionale agire con evidenza incompleta ma guardrail forti. Se la scelta è difficilmente reversibile e può produrre un danno molto grande, spendere più tempo per ridurre l'incertezza può avere valore elevato.

Perciò prima di aggiungere un'altra settimana di analisi conviene ragionare su cinque elementi in relazione fra loro: quanto costa sbagliare, quanto costa aspettare, quanto sono diverse le conseguenze delle alternative, quanto è reversibile la scelta e quanto è probabile che l'informazione aggiuntiva cambi effettivamente la decisione.

## Il prossimo dato deve competere con il suo costo

Per progetti importanti il brief può contenere un piccolo promemoria operativo:

```text
Quale incertezza, se ridotta, potrebbe cambiare la decisione?
Quale informazione aggiuntiva avrebbe più valore?
Quanto costa ottenerla?
Quanto costa aspettarla?
```

Queste domande diventano particolarmente utili quando il primo ciclo è inconcludente. Non dobbiamo automaticamente “analizzare ancora”; dobbiamo scegliere quale nuovo dato, esperimento o fonte abbia la probabilità più alta di cambiare ciò che faremo.

L'AI modifica il costo di alcune informazioni. Se segmentazioni, sensitivity analysis e controlli preliminari diventano più economici, può essere razionale eseguirne di più. Ma il criterio non cambia: una verifica facile da generare non è automaticamente utile.

> **Il valore dell'informazione non dipende da quanto è interessante produrla. Dipende da quanto può cambiare una decisione abbastanza importante da giustificare tempo, costo e attesa.**
