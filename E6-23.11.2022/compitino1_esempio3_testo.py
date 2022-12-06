"""
   Primo Compitino di Elementi di Informatica e Programmazione - Canale 2

   Copiare questo file in CognomeMatricola.py usando il proprio cognome
   e il proprio numero di matricola. Se il cognome contiene spazi o apostrofo,
   ignorarli; se contiene lettere accentate, usare la corrispondente lettera
   non accentata. SOLO IL COGNOME, senza il nome.
   
   MODIFICARE SOLTANTO IL FILE CognomeMatricola.py !!!!!!!!
   Quello sara' il file valutato per l'esame.

   TEMPO A DISPOSIZIONE = 1 ora e 20 minuti (80 minuti)
   
   Il progetto consiste nello sviluppo di alcune funzioni cooperanti tra loro,
   ma la struttura della cooperazione (cioe' dell'interazione tra le funzioni)
   e' gia' delineata nella funzione main().
   
   Le funzioni si occupano di risolvere problemi riguardanti sequenze di DNA,
   descritte mediante stringhe contenenti soltanto le lettere A, C, G, T,
   i simboli standard per identificare le quattro basi nucleotidi
   (adenina, citosina, guanina e timina)
   
   Ciascuna funzione e' descritta nel commento che la precede, che a volte
   contiene anche delle prescrizioni o dei divieti da seguire durante la
   scrittura del codice: valgono soltanto per la funzione a cui si riferisce il commento.
   
   Alcune sezioni di codice sono gia' presenti e non possono essere modificate!
   Le sezioni mancanti e da scrivere sono identificate dal commento
   # SCRIVERE QUI 
   
   Si consiglia di progettare le funzioni nello stesso ordine in cui
   sono elencate nel programma (sono approssimativamente di difficolta' crescente),
   anche se non e' strettamente necessario.
   NON SI POSSONO DEFINIRE ALTRE FUNZIONI.
   Tutto cio' che serve per progettare una delle funzioni e' scritto PRIMA della
   funzione stessa: non serve leggere piu' avanti.
   
   ATTENZIONE: nel codice gia' presente NON sono stati utilizzati caratteri di tabulazione
   per l'indentazione, sono tutti spazi singoli.
   
   Gli enunciati "pass" presenti nel codice servono a fare in modo che non ci 
   siano errori di sintassi prima che il vostro codice venga scritto nelle funzioni.
   Quando completate una funzione potete eliminare il "pass" eventualmente presente
   (ma potete anche lasciarlo, non crea problemi).
   Si tratta di una "istruzione nulla", quando viene eseguita non fa NIENTE ma
   serve dove sarebbe necessaria una istruzione ma non si sa ancora cosa scrivere...
 
   SI TRATTA DI SCRIVERE COMPLESSIVAMENTE CIRCA 35 RIGHE DI CODICE.
   
"""
def main() :
   """
      Alcuni collaudi... NON MODIFICARE
      
      Ovviamente finche' non saranno state realizzate tutte le funzioni richieste
      verra' visualizzato il messaggio "Collaudo non riuscito".
      
      Per collaudare il programma quando e' realizzato soltanto parzialmente
      basta commentare qui sotto le righe che invocano funzioni non ancora realizzate.
      PRIMA DELLA CONSEGNA "scommentate" eventuali righe che avete commentato.
      
      NON CANCELLATE RIGHE PER NESSUN MOTIVO.
      
      NON e' NECESSARIO ANALIZZARE IL CODICE DI QUESTA FUNZIONE.
   """
   str1 = "ACGT"
   str2 = "ACGTACGT"
   str3 = "AGCTTACG"
   list1 = ("ATTT", "TACG", "GGGG", "TTTT", "ATAT")
   list2 = list1 + ("AA",)
   list3 = list1 + (str1,)
   if (True
       and distance(str1, str2) == -1
       and distance(str2, str3) == 6
       and distance(str2, str2) == 0
       and minDistance(str1, list2) == ""
       and minDistance(str1, list3) == str1
       and minDistance(str1, list1) == "ATTT"
       and len(minGlobDist(())) == 0
       and len(minGlobDist(list2)) == 0
       and (sorted(minGlobDist(list1)) == ["ATTT", "TTTT"] or sorted(minGlobDist(list1)) == ["ATAT", "ATTT"])
      ) :
      print("Collaudo riuscito (ma non significa che non ci siano errori...)")
   else :
      print("Collaudo non riuscito")
   """
   Qui sotto si possono inserire altri collaudi, ma poi devono essere eliminati (o commentati).
   """
   # EVENTUALMENTE SCRIVERE QUI
   
   
# fine main


## Calcola la "distanza" tra due stringhe.
#
#  La distanza tra due stringhe (aventi la stessa lunghezza) e' uguale al numero di coppie di
#  caratteri in posizioni corrispondenti tra le due stringhe che contengono caratteri tra loro
#  diversi (la funzione, quindi, restituisce zero se e solo se le due stringhe sono identiche).
#
#  Es. distance("ACGTTGA", "AGCTTTA") restituisce 3 (per differenze nelle posizioni 1, 2 e 5).
#
#  Se le due stringhe non hanno la stessa lunghezza, la funzione restituisce -1.
#
#  @param s1 una delle due stringhe
#  @param s2 una delle due stringhe
#  @return la "distanza" tra s1 e s2 (-1 se hanno lunghezze diverse)
#
def distance(s1, s2) :
   pass 
   # SCRIVERE QUI  
   
#
# fine distance() 
#

## Data una stringa S e una tupla di stringhe L, trova in L la stringa che ha distanza minima da S.
#
#  Data una stringa S e una tupla di stringhe L, tutte di lunghezza uguale a len(S),
#  trova in L la stringa che ha distanza minima da S e la restituisce.
#
#  Nel caso in cui in L siano presenti piu' stringhe aventi la stessa distanza da S
#  e questa sia la distanza minima, restituisce la stringa avente indice minore in L,
#  tra quelle individuate.
#
#  Se S e' la stringa vuota oppure L e' una tupla vuota, restituisce la stringa vuota,
#  cosi' come in qualsiasi altra situazione di parametri non validi (da individuare).
#
#  Per calcolare la distanza tra una coppia di stringhe si invoca la funzione distance.
#  Se in L sono presenti m stringhe, la funzione distance non puo' essere invocata piu' di m volte.
#
#  @param s la stringa S
#  @param t la tupla di stringhe L
#  @return la stringa in L avente distanza minima da S;
#          in caso di pareggi, vince la stringa di indice minimo in L;
#          in caso di errore, restituisce la stringa vuota
#
def minDistance(s, t) :
   pass 
   # SCRIVERE QUI   
   
#
# fine minDistance()
#

## Data una tupla di stringhe L, trova in L la coppia di stringhe che hanno distanza minima.
#
#  Data una tupla di stringhe L, aventi tutte le stessa lunghezza, trova in L la coppia di stringhe
#  aventi distanza reciproca minima tra tutte le coppie presenti.
#  Nel caso in cui in L siano presenti piu' coppie di stringhe aventi la stessa distanza e questa
#  sia la distanza minima, restituisce una coppia qualsiasi tra quelle individuate.
#  La due stringhe da restituire devono costituire una tupla di 2 elementi.
#
#  Se L e' una tupla vuota, restituisce una tupla vuota, cosi' come in qualsiasi
#  altra situazione di parametri non validi (da individuare).
#
#  Si possono invocare le funzioni distance e/o minDistance.
#  ATTENZIONE: se si invoca minDistance(s, lst) e s appartiene a lst, si ottiene sempre come
#              risultato s, che e' a distanza minima (uguale a zero) da se stessa...
#
#  @param t la tupla di stringhe L
#  @return una tupla contenente le due stringhe di L aventi distanza reciproca minima tra
#          tutte le coppie di stringhe presenti in L;
#          in caso di pareggi, restituisce una qualsiasi delle coppie di stringhe individuate;
#          in caso di errore, restituisce la tupla vuota
#
def minGlobDist(t) :
   pass 
   # SCRIVERE QUI  
   
#
# fine minGlobDist()
#

main()
