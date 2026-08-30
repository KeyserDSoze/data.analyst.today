## 3.9 Tipi di dato e domini: una colonna non è solo un contenitore

Una colonna ha almeno tre livelli di significato:

1. **tipo tecnico** — integer, decimal, string, date, boolean;
2. **dominio ammesso** — quali valori sono validi;
3. **significato di business** — cosa rappresenta davvero quel campo.

Confondere questi tre livelli produce errori sottili.

### Caso studio simulato — Il CAP che perse gli zeri

Una società di logistica, **Mercurio Express**, importa ogni notte un file CSV con gli indirizzi dei clienti.

Il campo `postal_code` viene interpretato automaticamente come numero intero.

Per alcune aree, i codici che iniziano con zero vengono trasformati. Un valore come `00144` diventa `144`.

Il dato continua a essere formalmente valido come numero.

Ma semanticamente è sbagliato.

Il CAP non è una quantità sulla quale abbia senso fare somme o medie. È un identificatore testuale.

La correzione è semplice:

```python
customers["postal_code"] = customers["postal_code"].astype("string").str.zfill(5)
```

Ma il punto non è la riga di codice.

Il punto è capire che **la rappresentazione tecnica deve seguire il significato del dato**.

### Tipi frequenti e rischi tipici

**Numeri interi e decimali**

Possono rappresentare quantità, importi, identificatori o codici. Un `customer_id` composto solo da cifre non è per questo una misura numerica.

**Stringhe**

Possono contenere categorie, descrizioni, codici, identificatori, JSON o dati sporchi mascherati da testo.

**Date e timestamp**

Richiedono attenzione a timezone, calendario, formato, precisione e significato dell'evento temporale.

**Boolean**

Un campo `is_active` può sembrare semplice, ma bisogna sapere chi lo aggiorna, quando e secondo quale regola.

**Categorie**

Valori come `Italy`, `Italia`, `IT`, `ita` e `ITALY` possono rappresentare la stessa categoria oppure no, a seconda del sistema.

### Il dominio

Il dominio definisce l'insieme dei valori plausibili.

Per esempio:

- `discount_pct`: 0–100;
- `quantity`: intero positivo, salvo resi;
- `country_code`: elenco ISO previsto dal sistema;
- `order_status`: `created`, `paid`, `shipped`, `cancelled`, `refunded`;
- `currency`: valuta ammessa;
- `birth_date`: non futura.

Queste regole possono essere trasformate in test automatici.

```python
assert orders["discount_pct"].between(0, 100).all()
assert orders["order_status"].isin(ALLOWED_STATUSES).all()
```

### Il tipo giusto riduce ambiguità

Un buon analista non guarda soltanto `dtype`.

Chiede:

- che cosa rappresenta questa colonna?
- quali valori sono ammessi?
- quali valori sono impossibili?
- `NULL` ha un significato specifico?
- l'unità di misura è esplicita?
- il formato può cambiare tra sistemi?

La qualità dell'analisi comincia spesso da dettagli apparentemente banali come questi.