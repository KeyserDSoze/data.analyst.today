## 10.10 Regularizzazione: pagare meno fit per comprare stabilità

Quando un modello ha abbastanza libertà da inseguire il rumore, possiamo introdurre una preferenza esplicita per soluzioni più stabili. La regularizzazione accetta volontariamente un po' meno fit sul training set in cambio di una generalizzazione migliore.

Nei modelli lineari le due famiglie classiche sono L2/Ridge, che riduce coefficienti grandi, e L1/Lasso, che può portarne alcuni a zero. Per un Data Analyst, però, la domanda utile non è memorizzare la forma della penalizzazione. È capire **quale instabilità stiamo cercando di ridurre e se il guadagno sopravvive alla validation corretta**.

### Caso simulato/composito — BrightTel

BrightTel costruisce una regressione logistica di churn con 180 feature. Una combinazione rara di device, offerta e canale identifica 73 clienti e riceve un coefficiente enorme sul training; nei periodi successivi il pattern quasi scompare.

| Modello | AUC train | AUC validation |
|---|---:|---:|
| penalizzazione debole | 0,88 | 0,74 |
| L2 più forte | 0,83 | 0,77 |
| L1 | 0,81 | 0,76 |

Il modello L2 “perde” cinque punti sul training e guadagna tre punti dove conta. La penalizzazione ha ridotto il valore attribuito a pattern fragili.

### Coefficienti piccoli non significano variabili irrilevanti per il business

Con feature correlate — per esempio spesa 30 giorni, spesa 28 giorni, ordini, AOV e revenue — più colonne contengono informazione sovrapposta. L1 può lasciare una feature e azzerarne altre. Questo non dimostra che le feature eliminate siano causalmente inutili; indica soltanto che il modello può costruire una previsione simile senza usarle tutte contemporaneamente.

Con forte correlazione, la selezione stessa può cambiare tra campioni. Per questo l'interpretabilità deve guardare stabilità tra fold e periodi, non soltanto la soluzione finale.

### La forza della penalizzazione appartiene alla validation

Troppo poca regolarizzazione lascia coefficienti instabili e alta variance; troppa comprime anche pattern reali e produce underfitting. La quantità adeguata va scelta con una validation coerente con il deployment, non sul training fit.

Nei modelli interpretabili è utile osservare come i coefficienti cambiano tra fold, periodi, campioni e versioni. Un coefficiente che cambia spesso segno può segnalare multicollinearità, poco supporto, processo instabile o feature engineering fragile. La regularizzazione può attenuare il sintomo, ma non sostituisce la diagnosi.

### Che cosa regularizzare non può correggere

Una penalizzazione non ripara leakage, label sbagliate, training-serving skew, selection bias, concept drift o calibration difettosa. Un modello regolarizzato su dati sbagliati è soltanto un modello più disciplinato che impara il problema sbagliato.

La regularizzazione va quindi posizionata nella catena corretta:

```text
prediction task corretta
→ feature as-of valide
→ validation credibile
→ complessità osservata
→ regularization/tuning
→ nuova verifica fuori campione
```

> **Regularizzare significa imporre un prezzo alla complessità statistica. La complessità semantica del problema — cosa stiamo prevedendo, con quali dati e per quale decisione — deve essere risolta prima.**