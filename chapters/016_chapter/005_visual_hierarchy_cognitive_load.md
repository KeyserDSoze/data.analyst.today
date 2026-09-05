## 16.4 Gerarchia visiva e cognitive load: progettare l'attenzione

Quando tutto sembra importante, niente lo è davvero. Una pagina può contenere numeri corretti e fallire perché trasferisce al lettore troppo lavoro: capire dove guardare, ricordare una legenda lontana, confrontare scale, distinguere headline e dettaglio, capire se una nota è un caveat decision-critical o semplice documentazione.

Il cognitive load non è quindi soltanto un problema estetico. È **rischio di interpretazione**.

### Salienza visiva = priorità implicita

Posizione, dimensione, contrasto, spazio bianco, peso tipografico, colore e annotazioni compongono un vero **salience budget**. Se usiamo massima enfasi su dieci elementi, non abbiamo dieci priorità: abbiamo perso la gerarchia.

Per questo conviene allineare la gerarchia grafica a quella semantica del Decision Record:

| Livello | Ruolo |
|---|---|
| **P1 — decision-critical** | recommendation, guardrail violato, soglia superata, caveat che può cambiare scelta |
| **P2 — supporting evidence** | prove che sostengono o discriminano le alternative |
| **P3 — context / verification** | dettaglio utile per comprensione, audit o drill-down |

Questa classificazione non obbliga a un layout fisso. Impone però una regola: **ciò che può cambiare decisione non può ricevere meno salienza di ciò che la sostiene**.

### Caso simulato/composito — Quattro KPI, sedici colori

Una fintech monitora default rate, loss given default, approval rate e fraud loss. La dashboard usa sedici colori per prodotti, stati, regioni e alert. Durante la review il management dedica diversi minuti a un segmento rosso che sembra critico; il rosso, però, indica soltanto una categoria prodotto.

Il redesign separa i linguaggi visivi. Le categorie restano neutre; l'enfasi è riservata agli scostamenti decisionali; gli alert usano testo e simboli oltre al colore; le linee sono etichettate direttamente. I dati non cambiano, ma cambia la probabilità che il lettore assegni correttamente priorità.

## Ridurre il lavoro di memoria

Una pagina efficace non chiede al lettore di ricordare quale colore era il target, quale linea rappresentava l'anno corrente o quale unità usava il grafico precedente. Etichette dirette, unità vicine al numero, filtri decision-critical visibili, annotazioni nel punto a cui si riferiscono e encoding coerenti tra pagine riducono il carico di memoria e rendono più difficile una lettura accidentale.

Lo spazio bianco svolge lo stesso compito. Non è “vuoto”: separa gruppi semantici, distingue evidence e recommendation, segnala un cambio di livello di dettaglio. Riempire ogni centimetro aumenta la quantità di informazione presente e può ridurre quella effettivamente utilizzabile.

## Precision budget

Anche i decimali competono per attenzione. `31,847362%` può sembrare rigoroso, ma se nessuna decisione cambia sotto 0,1 punti percentuali e il dato stesso ha incertezza maggiore, sei decimali comunicano una precisione che il processo non può usare.

Chiamiamo **precision budget** la quantità di dettaglio numerico che il metodo può difendere e la decisione può realmente utilizzare. Mostrare meno cifre non significa essere meno precisi: significa evitare che precisione tipografica venga scambiata per certezza epistemica.

## Il caveat non è una footnote se attraversa la decision boundary

Supponiamo che il beneficio centrale di un progetto sia **€1,2M**, con range plausibile **€0,4M–€1,9M**, contro un costo di **€1,0M**. Il range attraversa il break-even. Se la recommendation è P1, anche questa uncertainty è P1. Metterla in piccolo in fondo alla slide altererebbe la struttura della decisione costruita nel Capitolo 15.

È qui che gerarchia visiva e decision quality diventano la stessa cosa.

## Testare la gerarchia

Un controllo semplice è mostrare la pagina a una persona non coinvolta. Dopo pochi secondi chiediamo che cosa sembra più importante; dopo dieci secondi chiediamo quale problema o decisione pensa che la pagina stia evidenziando. Se le risposte non coincidono con l'intento, la gerarchia è sbagliata anche se ogni elemento isolato è corretto.

## Accessibilità come disciplina della ridondanza

W3C WCAG 2.2 richiede che il colore non sia l'unico mezzo per comunicare informazione.[^wcag-color] Questo obbligo migliora anche la comunicazione generale: label, simboli, ordine e struttura rendono il significato più robusto su proiettori, screenshot, stampa e display differenti.

> **La gerarchia visiva è una decisione su dove spendere l'attenzione del lettore. Va allocata con la stessa disciplina con cui allochiamo evidenza, tempo e budget analitico.**

[^wcag-color]: W3C, *WCAG 2.2 — Understanding 1.4.1 Use of Color*, https://www.w3.org/WAI/WCAG22/Understanding/use-of-color.html
