## 7.3 Stazionarietà e decomposizione: separare struttura e rumore

Molti modelli di serie temporali diventano più semplici quando il comportamento della serie è relativamente stabile nel tempo. Una nozione centrale è quella di **stazionarietà**.

In termini pratici, una serie stazionaria non mostra cambiamenti sistematici persistenti nella media, nella varianza o nella struttura di autocorrelazione. Il NIST sottolinea che trend, variazioni di scala e stagionalità violano questa idea e che trasformazioni o differenziazione possono aiutare a rendere la serie più stabile.

### Caso: il numero di ordini che cresce ma la volatilità cresce ancora di più

Un marketplace passa da circa 20.000 ordini giornalieri a oltre 80.000 in quattro anni. Nel frattempo anche la variabilità giornaliera aumenta:

| Anno | Ordini medi/giorno | Deviazione standard |
|---|---:|---:|
| 2023 | 21.400 | 2.100 |
| 2024 | 31.800 | 3.900 |
| 2025 | 49.600 | 6.700 |
| 2026 | 78.300 | 12.900 |

Un modello che assume una scala costante nel tempo fatica. Gli errori più recenti diventano molto più grandi in valore assoluto rispetto a quelli storici.

L'analista prova a modellare la crescita relativa invece dei livelli assoluti, oppure applica una trasformazione logaritmica. La serie trasformata mostra una varianza più stabile.

Questo non è un trucco matematico fine a sé stesso. È un modo per rendere più coerente la relazione tra errore e scala del fenomeno.

### Differenziazione

Un'altra operazione comune è la differenza:

```text
variazione_t = valore_t - valore_(t-1)
```

Se una serie cresce lentamente ma in modo persistente, la differenza può eliminare parte del trend e rendere più chiara la dinamica locale.

Esempio:

| Mese | Clienti attivi | Differenza mensile |
|---|---:|---:|
| Gen | 102.000 | - |
| Feb | 105.500 | +3.500 |
| Mar | 109.100 | +3.600 |
| Apr | 112.400 | +3.300 |

La serie dei livelli cresce; la serie delle differenze è relativamente stabile attorno a circa +3.500 clienti al mese.

### Decomporre una serie

Una rappresentazione utile è:

```text
serie = trend + stagionalità + residuo
```

oppure, in casi in cui l'ampiezza stagionale cresce con il livello:

```text
serie = trend × stagionalità × residuo
```

La decomposizione aiuta a rispondere a domande diverse:

- il business sta crescendo strutturalmente?
- esiste una stagionalità ripetibile?
- il movimento recente è spiegabile da trend e calendario?
- il residuo contiene qualcosa di davvero eccezionale?

### Caso: le cancellazioni hotel a Pasqua

Una piattaforma di prenotazioni osserva un aumento del 17% nelle cancellazioni in aprile e apre un incidente operativo.

Dopo la decomposizione si vede che aprile registra un aumento simile quasi ogni anno, ma la data esatta si sposta con Pasqua e i ponti festivi. La componente anomala, una volta considerato il calendario, è solo +2.4%.

La decisione cambia: non si tratta di un guasto del sistema di pagamento, ma di un comportamento stagionale noto che va incorporato nella pianificazione.

> **Decomporre non significa spiegare causalmente. Significa separare pattern sistematici da ciò che resta da investigare.**

## Fonti

- NIST, *Stationarity*: https://www.itl.nist.gov/div898/handbook/pmc/section4/pmc442.htm
- NIST, *Common Approaches to Univariate Time Series*: https://www.itl.nist.gov/div898/handbook/pmc/section4/pmc444.htm
