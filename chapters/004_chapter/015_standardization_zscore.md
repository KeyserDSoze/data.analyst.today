## 4.14 Z-score: confrontare una posizione rispetto al proprio contesto

Un valore assoluto non ci dice quanto sia insolito rispetto alla popolazione da cui proviene.

`82` può essere alto, basso o perfettamente ordinario.

Lo **z-score** esprime la distanza di un'osservazione dalla media in unità di deviazione standard:

```text
z = (valore - media) / deviazione standard
```

Se `z = 0`, il valore coincide con la media.

Se `z = +2`, si trova due deviazioni standard sopra la media.

Se `z = -1,5`, si trova una deviazione standard e mezza sotto.

Il vantaggio è che la scala originale scompare e possiamo ragionare sulla **posizione relativa**.

### Caso simulato/composito — Il negozio più piccolo che risultò tra i migliori

**Northstar Retail** gestisce 84 negozi molto diversi per superficie e mercato.

Un ranking per fatturato mensile produce:

```text
Milano Centro: €1,84M
Aosta:         €0,21M
```

Chiamare Milano "migliore" e Aosta "peggiore" confonde dimensione e performance.

Il team confronta quindi il fatturato per metro quadrato **all'interno di gruppi di negozi comparabili**.

Grandi negozi urbani:

```text
media = €1.420/m²
SD    = €160/m²
Milano Centro = €1.650/m²
z ≈ +1,44
```

Piccoli negozi di provincia:

```text
media = €910/m²
SD    = €70/m²
Aosta = €1.075/m²
z ≈ +2,36
```

Aosta ha il fatturato assoluto più basso, ma rispetto al proprio peer group è molto più eccezionale.

### La popolazione di riferimento viene prima della formula

Possiamo calcolare uno z-score su qualsiasi insieme numerico.

Questo non rende automaticamente sensato l'insieme.

Se standardizziamo insieme:

- flagship cittadini;
- outlet;
- negozi aeroportuali;
- piccoli store turistici;

la media e la deviazione standard descrivono un miscuglio di processi differenti.

Il risultato sarà matematicamente valido e analiticamente debole.

La domanda corretta è:

> **rispetto a quale popolazione voglio definire questo valore come alto o basso?**

### Z-score elevato non significa automaticamente "probabilità quasi zero"

È comune associare soglie come `|z| > 2` o `|z| > 3` a osservazioni rare.

Questa interpretazione probabilistica richiede assunzioni sulla distribuzione, in particolare quando vogliamo usare le proprietà della distribuzione normale.

Nell'EDA non dobbiamo trasformare una soglia pratica in una legge universale.

Distribuzioni fortemente asimmetriche, multimodali o a code pesanti possono produrre molti z-score elevati senza che i valori siano errori.

### Standardizzazione e comparabilità non sono sinonimi

Lo z-score risolve una parte del problema di scala.

Non risolve:

- composizione diversa;
- causalità;
- differenze temporali;
- metriche definite in modo differente;
- peer group mal scelti.

Serve quindi come **strumento descrittivo**, non come certificato di equità del confronto.

### Quando è utile

Esempi:

- confrontare performance relative dentro peer group;
- evidenziare valori che meritano ispezione esplorativa;
- mettere variabili su una scala comune per alcune visualizzazioni o modelli;
- osservare quanto un valore corrente sia distante dal comportamento storico, se la baseline è appropriata.

### Quando preferire strumenti robusti

Se la distribuzione è molto asimmetrica o dominata da code lunghe, può essere più informativo usare:

- mediana;
- percentili;
- IQR;
- ranking percentili;
- trasformazioni motivate dal fenomeno.

> **Uno z-score dice quanto un valore è lontano dal centro della distribuzione di riferimento. La parte più importante della frase è “distribuzione di riferimento”.**