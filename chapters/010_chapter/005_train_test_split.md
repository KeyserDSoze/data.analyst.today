## 10.5 Validation: simulare il deployment, non dividere il dataset

Un modello predittivo viene giudicato su ciò che non ha ancora visto. Per questo il problema della validation non è scegliere `80/20`, ma costruire una simulazione credibile del futuro in cui lo useremo.

Training, validation e test hanno ruoli diversi. Il training stima parametri e pattern; la validation supporta scelte di feature, modello, iperparametri e talvolta soglie; il test finale dovrebbe restare il più possibile isolato dal processo di sviluppo. Questa separazione serve a conservare almeno una misura di generalizzazione che non sia stata ottimizzata indirettamente dal team.

La domanda che viene prima dello split è:

> **a che cosa deve generalizzare il modello?**

Potremmo voler prevedere nuovi eventi degli stessi clienti, clienti mai visti, nuovi negozi, nuove città, periodi futuri oppure una combinazione di questi casi. La risposta determina lo split corretto.

### Caso simulato/composito — FinSure

FinSure costruisce un modello di default con dati 2021–2025. Uno split casuale produce ottime metriche, ma nel 2026 la performance scende nettamente. Nel 2025 erano cambiati criteri di acquisizione, pricing, underwriting, mix settoriale e canali commerciali.

Lo split casuale aveva distribuito righe degli stessi regimi nei due lati. Rispondeva quindi a:

> “Quanto funzioniamo su altri esempi mescolati dello stesso archivio?”

La domanda di produzione era:

> “Quanto funzioniamo sul prossimo periodo operativo?”

Un test più onesto può usare train 2021–2024, validation gennaio–giugno 2025 e test luglio–dicembre 2025. La metrica può peggiorare; la qualità della misura migliora.

Google raccomanda esplicitamente, per modelli destinati al futuro, di misurare performance su dati raccolti **dopo** quelli di training perché questa configurazione assomiglia maggiormente alla produzione.

Riferimento: https://developers.google.com/machine-learning/guides/rules-of-ml/

### Il grain della validation deve seguire il grain della generalizzazione

Consideriamo un churn model con uno snapshot mensile per cliente. Se gennaio–maggio dello stesso account sono nel training e giugno finisce nel test, il modello riconosce un soggetto che ha già visto.

Questo può essere corretto se in produzione prevederemo mesi futuri di clienti noti. È poco informativo se vogliamo sapere quanto generalizziamo a un cliente nuovo. In quel caso dobbiamo lasciare interi account da una sola parte dello split.

Lo stesso problema ricorre con pazienti, device, negozi, aziende, prodotti e qualsiasi entità ripetuta. La validation non deve fingere indipendenza quando il deployment non la avrà.

### Caso simulato/composito — MoveNow

MoveNow costruisce un ETA model su 12 milioni di consegne. Ottiene:

- split casuale tra consegne in città note: **MAE 5,8 minuti**;
- holdout su città non viste: **MAE 11,4 minuti**.

Non esiste un unico numero “vero”. I due test rispondono a due domande: nuove consegne in contesti noti oppure generalizzazione a una città nuova. Se il prodotto promette entrambi gli use case, deve riportare entrambi gli scope.

### Anche la validation viene contaminata dal processo di ricerca

Se proviamo centinaia di combinazioni di feature sullo stesso validation set, le decisioni del team iniziano ad adattarsi anche a quel campione. Per questo, nei progetti con molte iterazioni, un test finale untouched o un periodo out-of-time successivo può avere molto valore.

Il test non è “sacro” per rituale statistico. Serve a misurare quanto il processo di model search abbia imparato anche il set usato per scegliere.

### Split e frontiera informativa sono due controlli diversi

Uno split corretto non salva feature costruite con il futuro. La validation ha due dimensioni complementari:

- **quali osservazioni** il modello può usare;
- **quali informazioni** dentro ogni osservazione erano disponibili al prediction time.

La prima viene governata dal validation design. La seconda sarà il tema della sezione sul leakage.

Nella Predictive Decision Card non scriveremo soltanto “5-fold” o “80/20”, ma una frase come:

> **“Valutiamo il modello su account non usati nel training e su un periodo successivo, perché in produzione dovrà generalizzare sia a clienti nuovi sia a mesi futuri.”**

> **Il miglior split non è quello che usa meglio il dataset. È quello che riproduce meglio il modo in cui il modello potrà fallire dopo il deployment.**