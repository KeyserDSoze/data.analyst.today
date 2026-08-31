# 16.7 Annotazioni e contesto: aiutare il lettore a vedere ciò che conta

Un grafico non dovrebbe costringere chi lo legge a ricostruire mentalmente il contesto.

Se una linea cambia direzione perché è stato lanciato un nuovo pricing, se un picco coincide con una campagna, se un calo deriva da un cambio di definizione o se una serie contiene un'interruzione metodologica, quel contesto deve essere visibile.

Le annotazioni servono proprio a questo: collegare il dato al fenomeno.

## Il titolo non deve essere neutro per forza

Un titolo come:

> Revenue mensile 2025-2026

è corretto, ma spesso poco utile.

Un titolo come:

> La revenue è tornata sopra il trend pre-calo dopo il rilascio di giugno

aiuta il lettore a capire immediatamente la tesi del grafico.

Questo non significa manipolare.

Significa rendere esplicito ciò che il grafico mostra, purché il titolo sia sostenuto dall'evidenza.

L'Office for National Statistics raccomanda di progettare titolo, scala, testo e annotazioni in funzione del messaggio principale e del confronto che aiuta a interpretarlo.

Fonte: https://service-manual.ons.gov.uk/data-visualisation/guidance/principles

## Caso realistico: la linea che sembrava raccontare una crisi

Una piattaforma SaaS mostra il numero di utenti attivi giornalieri.

A metà aprile la serie scende improvvisamente del 16%.

Il grafico finisce in un executive report con il titolo:

> Engagement in forte calo

Il problema è che il 14 aprile è cambiata la definizione di `active_user`: prima bastava aprire l'app; dopo il cambio serviva completare almeno un'azione significativa.

Il dato non è necessariamente sbagliato.

È la comparabilità temporale a essere cambiata.

Una semplice annotazione verticale:

> 14 aprile — nuova definizione di active user

cambia completamente la lettura.

## Annotare eventi, non spiegazioni speculative

È corretto annotare:

- una release;
- una campagna;
- un cambio di prezzo;
- una modifica di tracking;
- un'interruzione del servizio;
- una variazione normativa;
- una migrazione di sistema.

È più pericoloso annotare:

> “Il calo è causato dalla nuova release”

se abbiamo solo una coincidenza temporale.

Meglio:

> “Nuova release distribuita al 65% degli utenti”

L'annotazione deve distinguere fatti osservati e interpretazioni.

## Contesto di confronto

Una variazione del 12% può sembrare enorme o irrilevante a seconda del confronto.

Serve chiedere:

- rispetto a cosa?
- su quale periodo?
- rispetto a quale baseline?
- il fenomeno è stagionale?
- esiste un target?
- esiste un benchmark?

Un buon grafico spesso contiene almeno uno di questi riferimenti.

## La regola pratica

Prima di pubblicare un grafico chiediamoci:

> “Quale informazione non è nei punti o nelle barre, ma è necessaria per interpretarli correttamente?”

Quella informazione è candidata a diventare titolo, sottotitolo, nota o annotazione.

**Il contesto non è decorazione. È parte del dato interpretato.**
