## 2.5 Ipotesi: analizzare senza vagare

Una buona analisi esplorativa non significa guardare tutto indiscriminatamente. Significa esplorare con curiosità, ma anche con struttura.

Le ipotesi aiutano a trasformare un problema ampio in piste verificabili.

Supponiamo che la conversione e-commerce sia diminuita.

Possibili ipotesi:

- il traffico è aumentato ma è di qualità inferiore;
- una modifica al checkout ha aumentato l'abbandono;
- il mix di dispositivi si è spostato verso mobile;
- alcuni prodotti ad alta conversione sono meno disponibili;
- i prezzi sono cresciuti rispetto ai competitor;
- una campagna ha portato utenti con intento più basso;
- il tracking è cambiato e il calo è almeno in parte artificiale.

Queste ipotesi non sono conclusioni. Sono **spiegazioni candidate**.

### Ipotesi descrittive, diagnostiche e causali

Possiamo distinguere almeno tre livelli.

**Ipotesi descrittiva**

> Il calo si concentra sul traffico mobile.

**Ipotesi diagnostica**

> Il calo mobile coincide con un aumento dell'abbandono nel passaggio pagamento.

**Ipotesi causale**

> La nuova interfaccia di pagamento ha causato parte del calo di conversione mobile.

Ogni livello richiede evidenza più forte del precedente. Il fatto che due eventi coincidano temporalmente non dimostra causalità.

### Hypothesis tree

Un modo pratico per strutturare il problema è costruire un albero di ipotesi.

Esempio semplificato:

**Il fatturato è diminuito**

- Sono diminuiti gli ordini?
  - meno traffico?
  - minore conversione?
  - minore frequenza di acquisto?
- È diminuito il valore medio dell'ordine?
  - prezzi più bassi?
  - mix prodotti diverso?
  - maggiori sconti?
- Sono aumentati resi/cancellazioni?
- È cambiata la contabilizzazione del fatturato?

Questa decomposizione collega una metrica finale ai suoi driver possibili.

### MECE come aspirazione, non religione

Nel problem solving viene spesso usato il principio MECE: categorie *Mutually Exclusive, Collectively Exhaustive*, cioè non sovrapposte e complessivamente complete.

Nella realtà dei dati non sempre riusciremo a costruire categorie perfettamente MECE. Tuttavia il principio è utile perché costringe a chiedersi:

- sto contando due volte lo stesso fenomeno?
- sto dimenticando una categoria importante?
- le mie spiegazioni si sovrappongono?

### Cosa rende buona un'ipotesi analitica

Una buona ipotesi è:

- specifica;
- falsificabile almeno in linea di principio;
- collegata a dati osservabili;
- rilevante per la decisione;
- distinta da una semplice descrizione;
- formulata prima di conoscere troppo bene il risultato, quando possibile.

### L'AI come generatore di ipotesi

L'AI è molto utile per ampliare rapidamente lo spazio delle spiegazioni candidate.

Possiamo fornirle:

- descrizione del business;
- schema dati;
- metriche;
- anomalie osservate;
- vincoli noti;

e chiedere di proporre possibili driver, controlli e segmentazioni.

Ma una lista plausibile non è evidenza. L'AI può suggerire ipotesi che suonano convincenti ma sono incompatibili con il processo reale.

Il ruolo dell'analista è quindi:

**generare -> prioritizzare -> verificare -> scartare o approfondire**.

### Prioritizzare le ipotesi

Non tutte meritano lo stesso tempo. Una semplice matrice può aiutare:

| Ipotesi | Impatto potenziale | Plausibilità | Dati disponibili | Costo di verifica | Priorità |
|---|---:|---:|---:|---:|---:|
| H1 | Alto | Alta | Buoni | Basso | Alta |
| H2 | Alto | Media | Parziali | Medio | Media |
| H3 | Basso | Alta | Buoni | Basso | Bassa |

Lo scopo non è attribuire numeri perfetti. È evitare di spendere tre giorni su una spiegazione irrilevante quando un controllo semplice potrebbe eliminare metà dello spazio delle ipotesi.

## Principio operativo

**Non chiederti soltanto "che cosa vedo nei dati?". Chiediti "quali spiegazioni competono tra loro, e quale evidenza le renderebbe più o meno credibili?"**