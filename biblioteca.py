import csv

def carica_da_file(file_path):
    # funzione che legge il file e lo inserisce in un lista di dizionari, utilizzando try except per gestire eventuali errori nel file
    biblioteca = []
    try:
        with open(file_path,'r', newline="", encoding="utf-8") as file_biblioteca:

            reader = csv.reader(file_biblioteca, delimiter=',')

            for row in reader:
                try:
                    record = {
                        'Titolo': row[0],
                        'Autore': row[1],
                        'Pubblicazione': int(row[2]),
                        'Pagine': int(row[3]),
                        'Sezione': int(row[4]),
                    }
                    biblioteca.append(record)
                except IndexError:
                    print(f"Attenzione errore sugli indici,riga incompleta") # gestione errore sugli indici
                except ValueError:
                    print(f"Attenzione: riga contiene valori non validi")# gestione errore sui valori
    except FileNotFoundError: # nel caso il file non esiste
        print(f"Errore: il file {file_path} non esiste.")
    except Exception as e:# altro errore non previsto
        print(f"Errore imprevisto")

    return biblioteca




def aggiungi_libro(biblioteca, titolo, autore, anno, pagine, sezione, file_path):#funzione che aggiunge un libro nella biblioteca


    for dizionario in biblioteca:
        if dizionario['Titolo'] == titolo:
            return None # se il libro inserito esiste già
        else:
            nuova_riga =[titolo, autore, anno, pagine, sezione] # campi inseriti dall' utente
            with open(file_path, mode="a", newline="", encoding="utf-8") as file_biblioteca: #apertura del file
                writer= csv.writer(file_biblioteca,delimiter=',')# impostazione del file in scrittura
                writer.writerow(nuova_riga) # scrive in coda la nuova riga
                return True # ritorna true se il libro è stato inserito






def cerca_libro(biblioteca, titolo):# funzione che cerca un libro scelto dall'utente

    #Ciclo che scorre i dizionari nella lista
    for dizionario in biblioteca:
        if dizionario['Titolo'].lower() == titolo.lower(): # verifica che il dizionario alla voce titolo sia il titolo richiesto dall' utente


            return dizionario



# funzione che ordina per sezione
def elenco_libri_sezione_per_titolo(biblioteca, sezione):

    lista_da_ordinare = [] # lista dove inserisco inizialmente tutti i libri della sezione richiesta dall'utente
    # ciclo che scorre i libri all'interno della lista e verifica che la sezione sia quella richiesta
    for dizionario in biblioteca:
        if dizionario['Sezione'] == sezione:
            lista_da_ordinare.append(dizionario)
    lista_da_ordinare.sort(key=lambda x: x['Pubblicazione']) # comando che ordina la lista di libri della sezione indicata per data di pubblicazione
    return lista_da_ordinare




def main():

    file_path = "biblioteca.csv"

    biblioteca = carica_da_file(file_path)


    while True:
        print("\n--- MENU BIBLIOTECA ---")
        print("1. Carica biblioteca da file")
        print("2. Aggiungi un nuovo libro")
        print("3. Cerca un libro per titolo")
        print("4. Ordina titoli di una sezione")
        print("5. Esci")

        scelta = input("Scegli un'opzione >> ").strip()

        if scelta == "1":
            print(biblioteca) # stampa la bibiblioteca nella sua struttura dati

        elif scelta == "2": # chiama la funzione aggiungi libro

            if not biblioteca:
                print("Prima carica la biblioteca da file.")
                continue

            titolo = input("Titolo del libro: ").strip() # chiede all' utente di inserire titolo
            autore = input("Autore: ").strip() # ///// autore
            try: # se nelle voci seguenti i valori non sono numeri da errore
                anno = int(input("Anno di pubblicazione: ").strip())
                pagine = int(input("Numero di pagine: ").strip())
                sezione = int(input("Sezione: ").strip())
            except ValueError:
                print("Errore: inserire valori numerici validi per anno, pagine e sezione.")
                continue

            libro = aggiungi_libro(biblioteca, titolo, autore, anno, pagine, sezione, file_path)
            if libro == True:
                print(f"Libro aggiunto con successo!")
            else:
                print("Non è stato possibile aggiungere il libro.")

        elif scelta == "3":
            if not biblioteca:
                print("La biblioteca è vuota.")
                continue

            titolo = input("Inserisci il titolo del libro da cercare: ").strip().lower()
            risultato = cerca_libro(biblioteca, titolo)
            if risultato:
                print(f"Libro trovato: {risultato}")
            else:
                print("Libro non trovato.")

        elif scelta == "4":# richiama la funzione che ordina la sezione
            if not biblioteca:
                print("La biblioteca è vuota.")
                continue

            try:
                sezione = int(input("Inserisci numero della sezione da ordinare: ").strip())# chiede la funzione da riondinare
            except ValueError:
                print("Errore: inserire un valore numerico valido.")
                continue

            titoli = elenco_libri_sezione_per_titolo(biblioteca, sezione)
            if titoli is not None:
                print(f'\nSezione {sezione} ordinata:')
                print("\n".join([f"- {titolo}" for titolo in titoli]))

        elif scelta == "5":
            print("Uscita dal programma...")
            break
        else:
            print("Opzione non valida. Riprova.")


if __name__ == "__main__":
    main()

