## 8.7 Randomizzazione e natural experiment: quando l'assegnazione rende credibile il confronto

La domanda centrale di un design causale è:

> **Perché il gruppo non trattato rappresenta ciò che sarebbe successo ai trattati senza intervento?**

La randomizzazione offre una risposta particolarmente forte: l'assegnazione viene generata da un meccanismo noto che, in media, non dipende dalle caratteristiche preesistenti delle unità.

### Caso simulato/composito — Nuovo onboarding B2B

Una piattaforma assegna casualmente nuovi account a:

- onboarding standard;
- onboarding guidato.

Dopo sei settimane:

| Gruppo | Account | Activation D14 | Retention D60 |
|---|---:|---:|---:|
| Standard | 4.812 | 42,6% | 31,8% |
| Guidato | 4.776 | 47,9% | 35,1% |

La differenza osservata non diventa causale perché esiste una colonna `variant`.

Diventa interpretabile causalmente perché **l'assegnazione era randomizzata prima dell'outcome**, a condizione che il design e l'analisi rispettino quell'assegnazione.

Il Capitolo 9 affronterà in dettaglio gli errori operativi degli A/B test. Qui ci interessa il principio:

> la randomizzazione costruisce il controfattuale attraverso il meccanismo di assegnazione.

### Randomizzazione dell'unità giusta

Se la promozione è applicata a un intero punto vendita, l'unità di randomizzazione può essere il negozio, non la transazione.

Se 40 store vengono randomizzati, non abbiamo automaticamente centinaia di migliaia di unità indipendenti solo perché esistono molte ricevute.

Il livello di assignment influenza:

- l'estimand;
- la dipendenza tra osservazioni;
- l'incertezza;
- gli spillover possibili.

### Intent-to-treat e trattamento ricevuto

In un esperimento alcune unità assegnate al trattamento possono non riceverlo davvero.

È importante distinguere:

- **assignment:** ciò che la randomizzazione ha deciso;
- **exposure:** ciò che è realmente successo.

Confrontare i gruppi secondo l'assegnazione conserva il vantaggio della randomizzazione e stima spesso un effetto **intent-to-treat**.

Confrontare soltanto chi ha effettivamente aderito può reintrodurre selezione, perché compliance e motivazione possono essere correlate all'outcome.

### Quando non possiamo randomizzare

Molte esposizioni sono determinate da:

- norme;
- soglie amministrative;
- rollout geografici;
- vincoli di capacità;
- timing esterno;
- shock naturali o istituzionali.

A volte questi processi creano variazione che può essere sfruttata causalmente.

Ma “è successo fuori dal nostro controllo” non basta per chiamarlo natural experiment.

Dobbiamo capire **come l'evento assegna l'esposizione** e perché quell'assegnazione può essere considerata plausibilmente indipendente dalle cause dell'outcome, almeno nel confronto rilevante.

## Caso reale documentato — Natural experiments e Premio Nobel 2021

Il comitato del Premio Sveriges Riksbank 2021 ha riconosciuto David Card per contributi empirici all'economia del lavoro e Joshua Angrist e Guido Imbens per contributi metodologici all'analisi causale. La motivazione sottolinea come i **natural experiments** abbiano permesso di rispondere a domande per cui una randomizzazione deliberata sarebbe impossibile o inappropriata.[^nobel]

Tra gli esempi discussi nei materiali del Nobel compare il confronto sul salario minimo tra aree sottoposte a cambiamenti di policy differenti: la variazione istituzionale crea una situazione simile, per alcuni aspetti, a un esperimento.[^nobel-lessons]

La lezione metodologica è più generale del caso economico:

> **cercare eventi o regole che producano esposizione per ragioni esterne al normale processo di selezione può rendere disponibili confronti causali che i dati osservazionali standard non offrono.**

### Natural experiment non significa assumption-free

Un evento esterno può comunque essere confuso con:

- altre policy simultanee;
- differenze territoriali;
- anticipazione dell'intervento;
- migrazione tra gruppi;
- shock specifici;
- cambi di measurement.

Quindi il lavoro non termina dicendo “è un esperimento naturale”.

Inizia documentando:

```text
Qual è la fonte di variazione?
Chi viene esposto e perché?
Chi rappresenta il confronto?
Quali altre cose cambiano nello stesso momento?
Quanto è locale l'effetto identificato?
```

### Il ponte verso i prossimi metodi

Difference-in-Differences, RDD e IV possono essere letti come modi diversi di sfruttare strutture nel processo di assegnazione:

- **DiD:** un gruppo cambia esposizione mentre un altro rappresenta la dinamica controfattuale;
- **RDD:** il trattamento cambia bruscamente a una soglia;
- **IV:** una fonte esterna modifica la probabilità di trattamento.

Matching segue una logica diversa: tenta di costruire comparabilità sulle covariate osservate quando il processo di assegnazione non offre una quasi-randomizzazione forte.

> **Il nome del metodo viene dopo. Prima dobbiamo capire quale caratteristica del processo di assegnazione rende possibile il confronto.**

[^nobel]: Nobel Prize, *The Prize in Economic Sciences 2021 — Press release*: https://www.nobelprize.org/prizes/economic-sciences/2021/press-release/
[^nobel-lessons]: Nobel Prize, *Nobel Prize Lessons 2021 — Natural experiments*: https://www.nobelprize.org/uploads/2021/10/Speakersmanuscript_All_Nobelprizes_2021_Nobelprizelessons.pdf
