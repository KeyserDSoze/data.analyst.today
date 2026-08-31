## 10.8 Calibration e soglie: una probabilità del 70% deve significare qualcosa

Un modello può ordinare bene i casi dal meno rischioso al più rischioso e allo stesso tempo produrre probabilità poco affidabili.

Questa distinzione è fondamentale.

Se assegniamo probabilità di churn intorno al 70% a cento clienti simili, ci aspettiamo che nel lungo periodo circa settanta di loro churnino. Se ne churnano solo quaranta, il modello è mal calibrato in quella regione.

### Ranking e calibration non sono la stessa cosa

Un modello può avere AUC alta ma probabilità distorte.

Esempio:

| Gruppo di score | Churn previsto medio | Churn osservato |
|---|---:|---:|
| 0,1–0,2 | 15% | 14% |
| 0,3–0,4 | 35% | 24% |
| 0,5–0,6 | 55% | 38% |
| 0,7–0,8 | 75% | 52% |

Il ranking può essere utile: i clienti con score più alto churnano di più.

Ma usare direttamente quelle probabilità per calcolare expected loss porterebbe a sovrastimare il rischio.

### Caso realistico: NovaCredit e il default risk

NovaCredit usa un classificatore per stimare il rischio di default a 12 mesi.

Il risk committee non usa soltanto il ranking. Calcola:

\[
Expected\ Loss = PD \times LGD \times EAD
\]

Dove:

- `PD` = probability of default;
- `LGD` = loss given default;
- `EAD` = exposure at default.

Se la PD è sistematicamente sovrastimata, il modello può portare a:

- pricing troppo alto;
- rifiuto di clienti profittevoli;
- allocazione eccessiva di capitale;
- stime di rischio poco credibili.

Il team scopre che il modello ha ROC-AUC 0,84, ma nella fascia stimata 20–30% il default osservato è solo 13%.

La discriminazione è discreta. La calibration no.

### Calibration curve

Un modo intuitivo per verificare la calibration è raggruppare le previsioni in intervalli e confrontare:

- probabilità prevista media;
- frequenza osservata dell'evento.

Un modello perfettamente calibrato si avvicina alla diagonale `predicted = observed`.

La documentazione scikit-learn dedica strumenti specifici alla calibration dei classificatori e distingue la qualità delle probabilità dalla sola capacità discriminativa.

Fonte: https://scikit-learn.org/stable/modules/calibration.html

### Brier score

Per target binari, una metrica utile è il Brier score:

\[
Brier = \frac{1}{n}\sum_{i=1}^{n}(p_i-y_i)^2
\]

Penalizza probabilità lontane dall'esito osservato.

Un valore più basso è migliore.

Ma anche qui non basta una metrica globale: la calibration può degradare in specifici segmenti.

### La soglia è una decisione, non una proprietà naturale del modello

Supponiamo che NovaCredit stabilisca:

- sotto 5%: approvazione automatica;
- 5–15%: revisione standard;
- 15–25%: analisi approfondita;
- sopra 25%: rifiuto salvo eccezioni.

Queste soglie non derivano magicamente dall'algoritmo.

Sono policy che dovrebbero incorporare:

- costo del capitale;
- margine del prodotto;
- appetite for risk;
- capacità di revisione;
- regolamentazione;
- qualità della calibration.

### Caso realistico: ServiceOne e la priorità dei ticket

ServiceOne costruisce un modello per prevedere quali ticket customer care finiranno in escalation.

Il team inizialmente usa soglia 0,5.

Risultato:

- solo 280 ticket al giorno vengono segnalati;
- il team specializzato può gestirne 900;
- molte escalation ad alto costo vengono perse.

Abbassando la soglia a 0,27:

- il volume sale a 860;
- recall aumenta fortemente;
- precision scende, ma rimane economicamente accettabile.

La soglia ottimale non è quella statisticamente più elegante. È quella coerente con capacità e costi.

### Segment calibration

Un modello globalmente calibrato può essere mal calibrato per:

- Paese;
- canale;
- fascia cliente;
- periodo;
- prodotto;
- device.

Se un risk score viene usato per decisioni importanti, l'analista deve chiedersi se la probabilità è affidabile **dove conta**.

### Un modello può degradare anche senza perdere subito AUC

Immagina che il tasso medio di churn raddoppi per un cambio di prezzo.

Il modello può continuare a ordinare correttamente i clienti — quindi mantenere AUC simile — ma sottostimare tutte le probabilità.

Questo rende calibration e monitoraggio nel tempo essenziali.

### Regola operativa

Prima di utilizzare probabilità predette in formule economiche o decisioni individuali, verifica:

1. discrimination;
2. calibration globale;
3. calibration per segmenti importanti;
4. stabilità nel tempo;
5. soglie coerenti con il costo degli errori;
6. capacità operativa generata dalle soglie.

Il classificatore non decide. Produce una stima. La soglia trasforma quella stima in una politica operativa.
