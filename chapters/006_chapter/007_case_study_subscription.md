## 6.6 Dall'aggregato al punto di rottura: combinare segmento, coorte e funnel

Segmentazione, coorti e funnel diventano davvero utili quando vengono usati insieme.

La segmentazione localizza **chi** contribuisce al cambiamento. La coorte mostra **quando** il problema è comparso. Il funnel individua **dove** il comportamento si interrompe.

Questa sezione non è ancora il caso end-to-end del capitolo. È un esercizio di diagnosi: partire da una spiegazione intuitiva e restringere progressivamente lo spazio delle ipotesi.

### Caso simulato/composito: Asteria CRM e il churn attribuito al prezzo

**Asteria CRM** è un SaaS B2B europeo con circa 18.000 account paganti. Nel primo semestre aumenta il listino del piano Professional del 12%.

Due mesi dopo, il churn mensile complessivo passa dal 2,7% al 3,6%.

La storia è pronta:

> abbiamo alzato i prezzi e i clienti stanno scappando.

È plausibile. Ma plausibile non significa ancora supportato dai dati.

### 1. Segmento — chi sta peggiorando?

L'analista separa i piani:

| Piano | Churn prima | Churn dopo |
| --- | ---: | ---: |
| Starter | 3,8% | 5,4% |
| Professional | 2,5% | 2,8% |
| Enterprise | 1,1% | 1,2% |

Il piano interessato dall'aumento di prezzo peggiora di poco. Il deterioramento maggiore è sullo Starter.

La prima ipotesi perde forza.

Non è ancora esclusa: effetti indiretti di pricing o cambi di mix potrebbero esistere. Ma non è più la spiegazione dominante.

### 2. Coorte — quando nasce il problema?

L'analista misura la retention D90 delle nuove coorti Starter:

| Coorte | Retention D90 |
| --- | ---: |
| Gennaio | 79% |
| Febbraio | 78% |
| Marzo | 77% |
| Aprile | 69% |
| Maggio | 66% |
| Giugno | 65% |

La rottura comincia ad aprile.

La timeline del business mostra che a fine marzo Asteria aveva lanciato una nuova campagna self-service per microimprese, aumentando fortemente i trial Starter.

### 3. Canale — quale popolazione porta il cambiamento?

| Canale | Retention D90 |
| --- | ---: |
| Organic | 80% |
| Partner | 84% |
| Paid search | 76% |
| Nuova campagna paid social | 51% |

A questo punto il churn aggregato può essere descritto come un problema molto più specifico:

> le nuove coorti Starter provenienti dalla campagna paid social hanno retention molto più bassa.

### 4. Funnel — dove si interrompe il percorso?

Il team costruisce il funnel dei primi quattordici giorni:

1. trial avviato;
2. importazione contatti;
3. prima pipeline creata;
4. primo task assegnato;
5. almeno tre utenti invitati.

Gli utenti della nuova campagna arrivano numerosi al trial, ma solo il 22% completa l'importazione dei contatti, contro il 47% degli altri canali.

Le registrazioni crescono. Il passaggio verso l'uso reale no.

### 5. Timeline e ipotesi

Il messaggio pubblicitario prometteva “CRM operativo in cinque minuti”. Il prodotto richiedeva invece migrazione dati, configurazione della pipeline e collaborazione del team.

L'ipotesi aggiornata diventa:

> la nuova campagna sta acquisendo una popolazione con aspettative e livello di intent diversi; molti trial non raggiungono il primo valore operativo e le coorti risultano meno persistenti.

Questa formulazione è più forte della spiegazione iniziale, ma resta ancora una diagnosi osservazionale.

Non abbiamo dimostrato che cambiare il messaggio della campagna o l'onboarding aumenterà la retention.

### La decisione che cambia

Asteria non annulla immediatamente l'aumento di prezzo del Professional.

Decide invece di:

- separare il monitoraggio dello Starter dal Professional;
- ridefinire targeting e promessa della campagna;
- misurare il passaggio trial → importazione → primo workflow;
- creare una metrica di activation entro quattordici giorni;
- progettare una verifica controllata degli interventi di onboarding.

Il valore dell'analisi non è aver “trovato la causa”.

È aver trasformato:

> il churn sale, probabilmente per il prezzo

in:

> il deterioramento è concentrato nelle nuove coorti Starter acquisite da un nuovo canale e si manifesta prima del raggiungimento del valore iniziale.

Questa seconda frase delimita molto meglio ciò che sappiamo, ciò che sospettiamo e ciò che dobbiamo testare.

### Il pattern operativo

Il percorso può essere riutilizzato:

**KPI aggregato → segmento → coorte → funnel → timeline → ipotesi → prossimo metodo**

Il passo successivo è capire che cosa intendiamo per **primo valore**. È il tema dell'activation.
