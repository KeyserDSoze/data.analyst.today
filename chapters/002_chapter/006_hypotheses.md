## 2.5 Ipotesi: trasformare curiosità in piste verificabili

Una buona analisi esplorativa non significa guardare tutto indiscriminatamente.

Le ipotesi aiutano a trasformare un problema ampio in **spiegazioni candidate che competono tra loro**.

Supponiamo che la conversione e-commerce sia diminuita. Possibili ipotesi sono:

- il traffico è aumentato ma con intento più basso;
- una modifica al checkout ha aumentato l'abbandono;
- il mix di dispositivi si è spostato verso mobile;
- prodotti ad alta conversione sono meno disponibili;
- una campagna ha portato utenti meno qualificati;
- prezzi o condizioni di spedizione sono cambiati;
- il tracking è cambiato e parte del calo è artificiale.

Queste frasi non sono conclusioni. Sono un **portafoglio iniziale di spiegazioni da mettere alla prova**.

### Separare livello descrittivo e spiegazione

È utile distinguere:

**Osservazione**

> “Il calo è concentrato sul mobile.”

**Ipotesi diagnostica**

> “Il calo mobile deriva soprattutto da un aumento dell'abbandono nel passaggio di pagamento.”

**Ipotesi causale**

> “La nuova interfaccia di pagamento ha provocato parte del calo mobile.”

Ogni passaggio aggiunge una pretesa più forte.

Il brief può contenere ipotesi causali, ma deve evitare di trattarle come già dimostrate. I Capitoli 8 e 9 discuteranno quale evidenza serve per sostenere realmente affermazioni controfattuali.

### Hypothesis tree

Un albero di ipotesi aiuta a scomporre un outcome in componenti e spiegazioni.

**Il fatturato è diminuito**

- Sono diminuiti gli ordini?
  - meno traffico?
  - minore conversione?
  - minore frequenza di acquisto?
- È diminuito il valore medio dell'ordine?
  - prezzi più bassi?
  - mix prodotti diverso?
  - sconti maggiori?
- Sono aumentati resi o cancellazioni?
- È cambiata la contabilizzazione della metrica?

L'albero non deve essere perfettamente completo. Deve rendere visibile la struttura della diagnosi e impedirci di saltare subito alla storia che preferiamo.

Il principio MECE — *Mutually Exclusive, Collectively Exhaustive* — può essere utile come aspirazione: ridurre sovrapposizioni e verificare che non manchi un intero ramo importante. Nel mondo reale le cause possono interagire e le categorie non saranno sempre perfettamente indipendenti.

### Una buona ipotesi anticipa anche come potrebbe fallire

Per ogni ipotesi importante chiediamo:

- quale osservazione la renderebbe più credibile?
- quale osservazione la indebolirebbe?
- quale spiegazione alternativa produrrebbe lo stesso pattern?
- quale dato serve per distinguerle?

Questo passaggio è più utile di una semplice lista di “possibili cause”.

### Il registro delle ipotesi

Nel brief possiamo usare una tabella semplice:

| Ipotesi | Evidenza attesa se vera | Evidenza che la indebolisce | Dato necessario | Costo verifica | Priorità |
|---|---|---|---|---:|---:|
| Checkout mobile | drop dopo step pagamento sugli esposti | stesso calo sui non esposti | eventi funnel + release | basso | alta |
| Mix canali | calo concentrato nei nuovi canali | conversione cala dentro ogni canale | attribution + sessioni | medio | media |
| Stock-out | categorie colpite spiegano il delta | disponibilità stabile | inventory + catalogo | basso | alta |

Il valore della tabella non è assegnare punteggi scientifici alla plausibilità. È rendere esplicito **che cosa andremo a cercare e perché**.

### Prioritizzare prima di esplorare tutto

Un'ipotesi merita maggiore attenzione quando combina:

- impatto potenziale elevato;
- plausibilità coerente con il dominio;
- dati disponibili;
- basso costo di falsificazione;
- rilevanza per una decisione concreta.

Un controllo da dieci minuti che può eliminare un intero ramo dell'albero vale spesso più di un modello sofisticato applicato a una spiegazione marginale.

### Il ruolo dell'AI

L'AI può essere molto utile per ampliare lo spazio iniziale delle ipotesi e cercare controargomenti. Il Capitolo 0 ha già fissato la regola: generazione non significa evidenza.

Nel brief il contributo utile dell'AI è quindi produrre **candidate da sottoporre a un registro di verifica**, non una classifica da accettare come verità.

> **Non chiederti soltanto che cosa vedi nei dati. Chiediti quali spiegazioni competono e quale osservazione permetterebbe di distinguerle.**
