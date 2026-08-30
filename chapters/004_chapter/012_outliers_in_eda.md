## 4.11 Outlier nell'EDA: errore, eccezione o informazione preziosa?

Un outlier è un'osservazione che si discosta fortemente dal comportamento prevalente. Ma questa definizione statistica non dice ancora cosa farne.

Un valore estremo può essere un errore di inserimento, un problema di pipeline, un evento raro ma reale, una nuova tipologia di cliente o il primo segnale di un cambiamento importante.

### Caso: il cliente da 186.000 euro

Un'azienda B2B vende software in abbonamento. Il contratto annuale medio vale 18.400 euro, la mediana 12.900. Nel dataset compare un nuovo contratto da 186.000 euro.

Un'analisi automatica lo segnala come outlier. Un analista inesperto potrebbe rimuoverlo per "pulire" la distribuzione.

Il contratto è invece corretto: è il primo enterprise agreement siglato con un gruppo internazionale che consolida 14 società controllate in un unico accordo.

Quell'outlier non sporca il dato. Racconta un cambiamento nel modello commerciale.

### Caso opposto: 31 ore di sessione

In un'app mobile, la durata media delle sessioni cresce improvvisamente. Alcune sessioni durano 20, 26, 31 ore.

Il product team interpreta inizialmente il dato come forte crescita dell'engagement. L'analista verifica la strumentazione e scopre che una nuova versione dell'app non invia correttamente l'evento di chiusura quando passa in background.

Qui l'outlier è un errore di misurazione.

### Un metodo prima di cancellare

Davanti a un valore estremo conviene chiedere:

1. è tecnicamente possibile?
2. è coerente con altre fonti?
3. deriva da una nuova categoria o da un processo noto?
4. influenza in modo sproporzionato la media o un modello?
5. la decisione cambia includendolo o escludendolo?

L'ultima domanda è spesso trascurata. Una buona analisi può mostrare entrambe le versioni.

Per esempio:

- ricavo medio cliente: 21.600 euro;
- ricavo medio escludendo il contratto enterprise: 18.900 euro;
- mediana: 12.900 euro.

In questo modo il lettore vede sia il dato complessivo sia la sensibilità della statistica al valore estremo.

**Un outlier non è un ordine di cancellazione. È una richiesta di indagine.**