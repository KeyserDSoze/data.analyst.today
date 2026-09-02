## 18.9 Adoption: un prodotto analitico non ha successo perché esiste

Una dashboard può essere tecnicamente eccellente e non entrare mai in una decisione.

Un semantic layer può essere usato da centinaia di persone e continuare a produrre discussioni sulla definizione di `revenue`.

Un modello può generare score ogni ora e non modificare nessuna azione operativa.

Per questo **utilizzo, adozione e valore non sono sinonimi**.

Microsoft, nella Fabric Adoption Roadmap, distingue esplicitamente il semplice uso dall'uso efficace: numero di utenti e statistiche di utilizzo sono segnali utili, ma non dimostrano da soli che l'analytics sia stato adottato con successo.

Fonte pubblica: https://learn.microsoft.com/en-us/power-bi/guidance/fabric-adoption-roadmap

## L'adoption ladder

Per un prodotto analitico ricorrente possiamo pensare a sei livelli.

### 1. Availability

Il prodotto esiste ed è accessibile.

Non significa ancora che qualcuno sappia che esiste.

### 2. Discoverability

Il consumer riesce a trovarlo e capisce per quale problema è autorevole.

Un catalogo con cinquemila asset e nessuna indicazione di certification non crea vera discoverability.

### 3. Usage

Il prodotto viene effettivamente consultato o interrogato.

Questa è la parte più semplice da misurare:

- utenti attivi;
- query;
- sessioni;
- report view;
- API call;
- frequenza di utilizzo.

Ma resta soltanto un livello intermedio.

### 4. Effective use

Gli utenti usano l'asset nel modo previsto.

Per esempio:

- scelgono la metrica certificata invece di una copia locale;
- interpretano correttamente denominatore e caveat;
- usano il drill-down appropriato;
- non esportano il numero per ricostruirlo manualmente in un altro file.

### 5. Decision embedding

Il prodotto è diventato parte di un workflow reale.

Esempi:

- il weekly pricing meeting usa il Decision Communication Pack prodotto dal sistema;
- il planner consulta il forecast prima del cut-off operativo;
- il Customer Success team utilizza la lista prioritaria durante la pianificazione settimanale;
- Finance chiude il mese usando la stessa metrica certificata del board pack.

### 6. Outcome

Possiamo osservare un miglioramento nel processo o nel risultato supportato.

Non sempre sarà causalmente attribuibile al prodotto, ma dobbiamo almeno cercare segnali come:

- minore tempo necessario per decidere;
- meno riconciliazioni manuali;
- meno decisioni prese su dati non ready;
- minore frequenza di metriche duplicate;
- migliore forecast-driven planning;
- riduzione del cost-to-serve;
- migliore qualità o reversibilità delle decisioni.

La ladder è quindi:

**availability → discoverability → usage → effective use → decision embedding → outcome**.

Saltare direttamente da `usage` a `success` è uno degli errori più comuni nei programmi analytics.

## Caso simulato/composito: 1.200 utenti, ma il problema resta

Un'azienda lancia un portale self-service.

Dopo sei mesi:

- 1.200 utenti registrati;
- 18.000 sessioni mensili;
- 320 dashboard create;
- 74% dei manager dichiara di aver usato il portale almeno una volta nell'ultimo mese.

Il progetto viene dichiarato un successo.

Ma il monthly business review continua a iniziare con:

> “Quale revenue stiamo usando?”

Un audit trova:

- 23 definizioni attive di `active_customer`;
- 11 varianti di `net_revenue`;
- 41% delle dashboard executive basate su dataset non certificati;
- quasi quattro ore medie di riconciliazione prima del meeting mensile.

L'accesso è aumentato.

Il significato condiviso no.

Il prodotto ha migliorato availability e usage, ma non effective use né decision embedding.

## Adoption failure non significa automaticamente user failure

Se un prodotto non viene usato bene, non basta concludere:

> “Gli utenti non sono data-driven.”

Il problema può essere nel prodotto.

Possibili failure mode:

- scarsa discoverability;
- naming incomprensibile;
- troppe alternative quasi equivalenti;
- freshness insufficiente;
- workflow separato dal processo operativo;
- mancanza di fiducia dopo incidenti precedenti;
- assenza di supporto;
- interfaccia troppo tecnica;
- nessuna indicazione di owner;
- nessuna distinzione tra experimental e certified.

L'adoption è quindi una responsabilità condivisa tra prodotto e consumer.

## Misurare tre tipi di adozione

La Fabric Adoption Roadmap di Microsoft distingue tre prospettive che sono utili anche oltre un prodotto specifico:

- **organizational adoption** — quanto governance, supporto e pratiche organizzative rendono possibile l'uso corretto dell'analytics;
- **user adoption** — quanto le persone utilizzano effettivamente ed efficacemente gli strumenti;
- **solution adoption** — quale valore e impatto produce una specifica soluzione analitica.

Fonte pubblica: https://learn.microsoft.com/en-us/power-bi/guidance/fabric-adoption-roadmap-maturity-levels

Questa distinzione evita di comprimere tutto in una metrica come `monthly active users`.

## Una scorecard di adozione

Per un prodotto critico possiamo osservare almeno cinque famiglie.

| Dimensione | Esempi |
|---|---|
| Reach | consumer target raggiunti, discoverability, access success |
| Usage | utenti attivi, frequenza, query/report view |
| Effective use | quota su metriche certificate, errori di interpretazione, support request ripetitive |
| Workflow | percentuale di decisioni/processi che usa il prodotto, tempo domanda → risposta |
| Outcome | tempo decisionale, riconciliazioni evitate, errori ridotti, valore economico/operativo |

Non tutte richiedono una metrica perfetta.

Serve però evitare che il solo utilizzo diventi la definizione implicita di successo.

## L'adoption può anche diminuire correttamente

Una crescita continua dell'utilizzo non è sempre desiderabile.

Se due dashboard duplicate vengono sostituite da un unico prodotto certificato, il numero totale di dashboard e query può diminuire mentre il sistema migliora.

Se un alert diventa più preciso, il numero di notifiche può scendere.

Se un prodotto viene incorporato direttamente nel workflow operativo, gli utenti possono non aprire più una dashboard separata.

Quindi:

> **la metrica di adozione deve riflettere il comportamento desiderato, non una vanity metric di attività.**

## Retirement è parte dell'adoption

Un asset che nessuno usa più non dovrebbe restare indefinitamente `certified`.

L'Analytics Operating Contract deve prevedere anche un **retirement trigger**.

Possibili segnali:

- nessun decision process dipende più dal prodotto;
- utilizzo sotto soglia per più periodi;
- esiste un sostituto certificato;
- cost-to-serve superiore al valore residuo;
- definizione o processo business non più valido.

Prima del retirement bisogna verificare lineage e consumer reali.

Dopo il retirement, discovery e documentazione devono indicare chiaramente il successore.

## La domanda finale

La domanda più utile non è:

> “Quante persone usano questa dashboard?”

È:

> **“Quale decisione viene presa meglio, più velocemente o con meno ambiguità perché questo prodotto esiste?”**

Se non riusciamo a nominare quella decisione, abbiamo ancora un problema di product design.

> **Un prodotto analitico realizza valore quando entra nel flusso di una decisione e riduce un rischio reale, non quando accumula visualizzazioni.**
