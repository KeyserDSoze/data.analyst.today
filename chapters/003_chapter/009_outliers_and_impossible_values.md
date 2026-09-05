## 3.8 Outlier e valori impossibili: raro non significa sbagliato

Un valore estremo può essere un errore, ma può anche essere il record più importante del dataset. La distanza dalla media non basta a distinguerli, perché l'anomalia statistica e l'errore di misura sono concetti diversi.

Conviene pensare a tre categorie. Un valore **impossibile** viola una regola del fenomeno o del sistema. Un valore **implausibile** è possibile ma abbastanza anomalo da richiedere verifica. Un valore **raro ma reale** descrive invece un evento eccezionale che non deve essere cancellato soltanto perché disturba una distribuzione.

Questa distinzione porta immediatamente il problema fuori dalla sola statistica e dentro il dominio.

### Caso simulato/composito — Il cliente da 487.000 euro

Asteria Components, distributore B2B di componenti industriali, ha ordini mensili con mediana di poche migliaia di euro. Un record da **487.000 euro** viene segnalato da un boxplot e una routine automatica propone di rimuoverlo.

L'analista verifica il caso e scopre che appartiene a un produttore ferroviario che ha concentrato un ordine annuale in una singola commessa. Il valore è eccezionale ma reale. Eliminarlo ridurrebbe artificialmente fatturato, concentrazione del portafoglio, esposizione di cassa e rischio commerciale.

Nello stesso dataset compare un ordine da **9.999.999 euro**. L'indagine porta a una storia diversa: è un placeholder generato da un'importazione legacy fallita.

Due valori estremi. Uno descrive il business; l'altro descrive un errore del sistema che lo misura.

## Le regole del dominio vengono prima delle soglie statistiche

Alcuni problemi possono essere identificati senza conoscere la distribuzione storica. Età negativa, `delivery_date < order_date` quando il processo non lo consente, percentuali oltre il dominio ammesso, una valuta non supportata o una quantità negativa in una tabella che non registra resi sono violazioni di regole esplicite.

Più difficile è il caso dell'implausibile. Un ordine da 100.000 euro può essere assurdo per un piccolo e-commerce e normale per un distributore industriale. Una sessione di quattordici ore può essere un bug oppure una pagina lasciata aperta; ottocento ordini in un giorno possono indicare un bot, un reseller o un'importazione batch.

Per questo un filtro come:

```python
orders = orders[orders["amount"] < 100000]
```

è metodologicamente fragile se `100000` non deriva da una regola di dominio, da un processo documentato o da una decisione esplicita sull'analisi.

## L'outlier è una pista sul processo

Un valore estremo può segnalare un cliente strategico, una frode, un cambio di unità, un backfill, una nuova modalità operativa o una transazione che prima arrivava frammentata e ora arriva aggregata. Trattarlo come rumore prima di investigarlo significa perdere proprio l'informazione che può spiegare un cambiamento nel sistema.

La procedura, quindi, deve seguire la storia del record: verificare tipo e unità, risalire alla sorgente più vicina all'evento reale, osservare timestamp e campi correlati, cercare casi analoghi e confrontare il valore con limiti di business conosciuti. Quando la plausibilità resta incerta, il domain expert diventa parte del controllo.

Se decidiamo di escludere un record, la regola deve essere riproducibile e l'effetto dell'esclusione va quantificato. Se una conclusione cambia radicalmente perché rimuoviamo tre osservazioni, quella sensibilità non è un dettaglio da nascondere: è parte dell'evidenza.

> **L'obiettivo non è normalizzare il mondo finché assomiglia alla distribuzione attesa. È capire quali valori descrivono il mondo e quali descrivono un errore del sistema che lo misura.**
