## 3.8 Outlier e valori impossibili: il dato estremo non è sempre un errore

Gli outlier sono valori che si discostano fortemente dal comportamento tipico del dataset.

Possono rappresentare:

- un errore di inserimento;
- un problema di unità di misura;
- un bug di sistema;
- un evento raro ma reale;
- un cliente eccezionale;
- una frode;
- un cambiamento strutturale del processo.

Eliminarli automaticamente è una delle scorciatoie più pericolose dell'analisi.

### Caso studio simulato — Il cliente da 487.000 euro

**Asteria Components**, distributore B2B di componenti industriali, analizza il valore medio degli ordini per cliente.

La media mensile è di circa 2.340 euro. Un record mostra invece un ordine da **487.000 euro**.

Il primo istinto del team è considerarlo un errore.

Un boxplot lo identifica immediatamente come valore estremo. Un algoritmo automatico di cleaning propone di rimuoverlo.

L'analista decide invece di verificare.

Scopre che il cliente è un produttore ferroviario che ha effettuato un ordine annuale concentrato in un'unica commessa. Il valore è reale.

Se quel record fosse stato cancellato, sarebbero stati distorti:

- fatturato del mese;
- concentrazione clienti;
- distribuzione del valore degli ordini;
- stima del rischio commerciale;
- previsioni di cassa.

Lo stesso dataset contiene però anche un ordine da **9.999.999 euro**.

Quello è effettivamente un errore: un valore placeholder usato da un sistema legacy durante un'importazione fallita.

Due outlier.

Uno reale.

Uno falso.

Lo strumento statistico non può conoscere da solo la differenza.

### Valori impossibili

Un valore impossibile è spesso più facile da identificare di un outlier.

Esempi:

- età = -4;
- quantità ordinata = -17 senza che il record rappresenti un reso;
- data di consegna precedente alla data di ordine;
- percentuale = 143% quando il dominio ammette solo valori tra 0 e 100;
- temperatura corporea = 240 °C;
- durata sessione = 19 anni.

Questi controlli vengono chiamati spesso **domain checks** o **business rule checks**.

### Il contesto decide

Un ordine da 100.000 euro può essere assurdo in un e-commerce di accessori per smartphone e perfettamente normale in un'azienda B2B.

Per questo un controllo del tipo:

```python
orders = orders[orders["amount"] < 100000]
```

è metodologicamente debole se la soglia non deriva da una regola di business o da un'analisi esplicita.

### Una procedura pratica

Quando incontri un valore estremo:

1. verifica il tipo e l'unità di misura;
2. controlla la fonte originale;
3. confronta il record con campi correlati;
4. verifica se esistono eventi analoghi;
5. chiedi a un domain expert se il valore è plausibile;
6. documenta la decisione;
7. se lo escludi, conserva una traccia della regola applicata.

L'obiettivo non è rendere il dataset più bello.

È renderlo più fedele al fenomeno reale.