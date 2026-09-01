## 3.8 Outlier e valori impossibili: raro non significa sbagliato

Un valore estremo può essere un errore. Ma può anche essere il record più importante del dataset.

Prima di eliminarlo conviene distinguere almeno tre categorie:

- **impossibile**: viola una regola del fenomeno o del sistema;
- **implausibile**: è possibile, ma abbastanza anomalo da richiedere verifica;
- **raro ma reale**: rappresenta un evento eccezionale che non deve essere cancellato solo perché disturba la distribuzione.

Questa distinzione sposta il problema dalla statistica alla comprensione del dominio.

### Caso simulato/composito — Il cliente da 487.000 euro

**Asteria Components**, distributore B2B di componenti industriali, analizza il valore degli ordini.

La mediana mensile è di poche migliaia di euro. Un record mostra invece un ordine da **487.000 euro**.

Un boxplot lo segnala immediatamente come outlier. Una routine automatica di cleaning propone di rimuoverlo.

L'analista verifica il record prima di accettare la proposta.

Scopre che appartiene a un produttore ferroviario che ha concentrato un ordine annuale in una sola commessa. Il valore è eccezionale, ma reale.

Eliminarlo avrebbe distorto:

- fatturato mensile;
- concentrazione del portafoglio clienti;
- distribuzione del valore degli ordini;
- previsione di cassa;
- valutazione del rischio commerciale.

Nello stesso dataset compare anche un ordine da **9.999.999 euro**.

Questa volta l'indagine porta a una spiegazione diversa: è un valore placeholder proveniente da un'importazione legacy fallita.

Due valori estremi.

Uno è informazione.

L'altro è errore.

La distanza dalla media non basta a distinguerli.

### Valori impossibili: le regole del dominio sono più forti della distribuzione

Alcuni problemi possono essere identificati senza conoscere la distribuzione storica.

Esempi:

- età = `-4`;
- `delivery_date < order_date` quando il processo non consente correzioni retroattive di quel tipo;
- percentuale = `143%` quando il dominio ammette solo 0–100;
- quantità negativa in una tabella che non registra resi;
- data futura per un evento già concluso;
- valuta non supportata dal sistema.

Questi sono controlli di dominio o di business rule.

### Implausibile non significa impossibile

Un ordine da 100.000 euro può essere assurdo in un negozio di cover per smartphone e normale in una società industriale.

Una sessione web di 14 ore può essere un bug di tracking, ma anche una pagina lasciata aperta.

Un cliente con 800 ordini in un giorno può essere un bot, un reseller o un'importazione batch.

Per questo soglie arbitrarie come:

```python
orders = orders[orders["amount"] < 100000]
```

sono metodologicamente deboli se non sappiamo da dove proviene `100000`.

### Gli outlier possono rivelare il processo

Un valore estremo può segnalare:

- un cliente strategico;
- una frode;
- una nuova modalità operativa;
- un errore di unità;
- un cambio di sistema;
- un backfill;
- una transazione aggregata che prima arrivava separata.

Quindi l'outlier non è soltanto qualcosa da "gestire". È una pista investigativa.

### Procedura pratica

Quando incontri un valore estremo:

1. controlla tipo, unità e formato;
2. verifica il record nella sorgente più vicina all'evento reale;
3. osserva campi correlati e timestamp;
4. cerca altri casi analoghi;
5. confronta il valore con limiti di business noti;
6. coinvolgi un domain expert quando la plausibilità non è evidente;
7. documenta la decisione presa;
8. se escludi il record, conserva una regola riproducibile e quantifica l'effetto dell'esclusione.

### Una domanda utile

Prima e dopo aver trattato gli outlier, confronta il risultato principale.

Se una conclusione cambia radicalmente perché abbiamo escluso tre osservazioni, quella sensibilità è essa stessa informazione da comunicare.

> **L'obiettivo non è normalizzare il mondo finché assomiglia alla nostra distribuzione attesa. È capire quali valori descrivono il mondo e quali descrivono un errore del sistema che lo misura.**