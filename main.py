class Automate:
    def __init__(self, state_automate, alphabet_automate, initial_state_automate, final_state_automate,
                 transitions_state_automate):
        # Initialisation de l'automate avec les paramètres donnés
        self.state = state_automate  # Liste des états de l'automate
        self.alphabet = alphabet_automate  # Liste des symboles de l'alphabet
        self.initial_state = initial_state_automate  # Liste des états initiaux
        self.final_state = final_state_automate  # Liste des états finaux
        self.transitions = transitions_state_automate  # Liste des transitions de l'automate

    def is_standard(self):
        # Vérifie si l'automate est standard (un seul état initial et pas de transition allant directement
        # vers l'état initial)

        # Vérifie s'il y a exactement un seul état initial
        if len(self.initial_state) != 1:
            return False  # Retourne False si ce n'est pas le cas

        # Parcourt toutes les transitions de l'automate
        for transition in self.transitions:
            current_state, symbol, next_state = transition
            # Pour chaque transition, extrait l'état actuel, le symbole et l'état suivant

            # Vérifie si une transition pointe directement vers l'état initial
            if next_state == self.initial_state[0]:
                return False  # Retourne False si une telle transition est trouvée

        # Si aucune condition n'a été violée, l'automate est considéré comme standard
        return True  # Retourne True si l'automate est standard

    def standardize(self):
        # Méthode pour standardiser l'automate si nécessaire

        # Vérifie si l'automate est déjà standard
        if self.is_standard():
            print("Automate already standardize")
            return self  # Si l'automate est déjà standard, retourne simplement l'instance actuelle

        # Ajoute un nouvel état initial "i" à l'ensemble des états de l'automate
        self.state.append("i")
        new_initial_state = ["i"]  # Définit le nouvel état initial comme une liste contenant "i"

        # Parcourt chaque état initial de l'automate d'origine
        for initial_state in self.initial_state:
            # Parcourt chaque transition de l'automate d'origine
            for transition in self.transitions:
                current_state, symbol, next_state = transition
                # Vérifie si la transition commence par l'état initial en cours d'itération
                if current_state == initial_state:
                    # Crée une nouvelle transition avec le nouvel état initial "i"
                    new_transition = "i" + symbol + next_state
                    # Ajoute cette nouvelle transition à la liste des transitions de l'automate
                    self.transitions.append(new_transition)

        # Convertit la liste des transitions en un ensemble pour éliminer les doublons éventuels
        self.transitions = set(self.transitions)

        # Crée une nouvelle instance d'Automate standardisé avec les paramètres mis à jour
        new_standardized_automate = Automate(self.state, self.alphabet, new_initial_state,
                                             self.final_state, self.transitions)

        # Retourne la nouvelle instance d'Automate standardisé
        return new_standardized_automate

    def is_determinist(self):
        # Vérifie si l'automate est déterministe

        # Vérifie s'il y a exactement un seul état initial
        if len(self.initial_state) != 1:
            return False  # Si ce n'est pas le cas, l'automate n'est pas déterministe

        seen_transitions = set()  # Initialise un ensemble pour stocker les transitions observées

        # Parcourt chaque transition de l'automate
        for transition in self.transitions:
            current_state, symbol, next_state = transition
            # Récupère l'état actuel, le symbole et l'état suivant de la transition

            # Vérifie si la même transition (même état actuel et même symbole) a déjà été vue
            if (current_state, symbol) in seen_transitions:
                return False  # Si une telle transition est déjà vue, l'automate n'est pas déterministe

            # Ajoute la transition (état actuel, symbole) à l'ensemble des transitions observées
            seen_transitions.add((current_state, symbol))

        # Si aucune transition ambiguë n'est trouvée, l'automate est déterministe
        return True  # Retourne True indiquant que l'automate est déterministe

    def successors_elem(self, state, letter):
        # Retourne les états suivants accessibles à partir d'un état donné avec un symbole donné

        successors = []  # Initialise une liste pour stocker les états suivants

        # Parcourt chaque transition de l'automate
        for transition in self.transitions:
            current_state, symbol, next_state = transition
            # Récupère l'état actuel, le symbole et l'état suivant de la transition

            # Vérifie si la transition correspond à l'état donné et au symbole donné
            if current_state == state and symbol == letter:
                # Si oui, ajoute l'état suivant à la liste des états suivants
                successors.append(next_state)

        return successors  # Retourne la liste des états suivants accessibles

    def determine(self):
        # Détermine l'automate si nécessaire
        # Attention la fonction n'est pas fonctionnelle nous n'avons pas réussi à l'implémenter entièrement

        # Vérifie si l'automate est déjà déterministe
        if self.is_determinist():
            print("Automate already determine.")
            return self  # Si l'automate est déjà déterministe, retourne simplement l'instance actuelle

        new_transitions = []  # Liste pour stocker les nouvelles transitions déterminisées
        new_states = []  # Liste pour stocker les nouveaux états déterminisés
        new_initial_state = tuple(self.initial_state)  # Convertit l'état initial en un tuple
        new_final_states = []  # Liste pour stocker les nouveaux états finaux déterminisés
        queue = [new_initial_state]  # File pour gérer les états à traiter
        visited = {new_initial_state}  # Ensemble pour suivre les états visités

        # Parcours de la file tant qu'il reste des états à traiter
        while queue:
            current_state = queue.pop(0)  # Récupère l'état actuel à traiter
            new_states.append(current_state)  # Ajoute l'état actuel à la liste des nouveaux états

            # Vérifie si l'état actuel contient au moins un état final de l'automate d'origine
            if any(state in self.final_state for state in current_state):
                new_final_states.append(current_state)  # Ajoute l'état actuel à la liste des nouveaux états finaux

            # Parcourt chaque symbole de l'alphabet de l'automate
            for letter in self.alphabet:
                next_state = set()  # Ensemble pour stocker les états suivants possibles

                # Parcourt chaque état de l'état actuel
                for state in current_state:
                    # Obtient les états suivants à partir de l'état actuel avec le symbole donné
                    next_state.update(self.successors_elem(state, letter))

                # Convertit l'ensemble des états suivants en tuple trié
                next_state_tuple = tuple(sorted(next_state))

                # Vérifie si le tuple des états suivants n'a pas déjà été visité
                if next_state_tuple not in visited:
                    visited.add(next_state_tuple)  # Marque le tuple comme visité
                    queue.append(next_state_tuple)  # Ajoute le tuple à la file pour traitement ultérieur

                # Ajoute la nouvelle transition à la liste des nouvelles transitions déterminisées
                new_transitions.append((current_state, letter, next_state_tuple))

        # Affiche que l'automate est déterminé
        print("Automate determine.")
        print(new_states)
        print(self.alphabet)
        print([new_initial_state])
        print(new_final_states)
        print(new_transitions)
        # Crée une nouvelle instance d'Automate déterminisé avec les paramètres mis à jour
        new_automate = Automate(new_states, self.alphabet, [new_initial_state], new_final_states, new_transitions)

        return new_automate  # Retourne la nouvelle instance d'Automate déterminisé

    def is_complete(self):
        # Vérifie si l'automate est complet

        all_pairs, existing_pairs = set(), set()  # Initialise deux ensembles vides

        # Génère tous les couples possibles (état, symbole) pour l'automate
        for state in self.state:
            for symbol in self.alphabet:
                all_pairs.add((state, symbol))

        # Parcourt chaque transition de l'automate
        for current_state, symbol, next_state in self.transitions:
            # Ajoute la transition (état actuel, symbole) à l'ensemble des transitions existantes
            existing_pairs.add((current_state, symbol))

        # Vérifie si tous les couples possibles sont définis par des transitions dans l'automate
        return all_pairs == existing_pairs

    def complete(self):
        # Complète l'automate s'il ne l'est pas déjà

        # Vérifie si l'automate est déjà complet
        if self.is_complete():
            print("Automate already complete.")
            return self  # Si l'automate est déjà complet, retourne simplement l'instance actuelle

        new_state = "P"  # Définit un nouvel état fictif pour les transitions manquantes
        self.state.append(new_state)  # Ajoute le nouvel état fictif à l'ensemble des états de l'automate

        existing_pairs = set()  # Initialise un ensemble pour stocker les transitions existantes

        # Parcourt chaque transition de l'automate
        for current_state, symbol, next_state in self.transitions:
            existing_pairs.add((current_state, symbol))  # Ajoute la transition à l'ensemble des transitions existantes

        # Parcourt tous les états et tous les symboles de l'alphabet
        for state in self.state:
            for symbol in self.alphabet:
                # Vérifie si le couple (état, symbole) n'existe pas dans les transitions existantes
                if (state, symbol) not in existing_pairs:
                    # Si le couple n'existe pas, crée une transition vers le nouvel état fictif
                    transition = state + symbol + new_state
                    self.transitions.append(
                        transition)  # Ajoute la nouvelle transition à la liste des transitions de l'automate

        print("Automate complete.")  # Affiche un message indiquant que l'automate a été complété

        # Crée et retourne une nouvelle instance d'Automate avec les transitions mises à jour
        return Automate(self.state, self.alphabet, self.initial_state, self.final_state, self.transitions)

    def complement(self):
        # Construit le complément de l'automate, s'il est déterministe et complet

        # Vérifie si l'automate n'est pas déterministe
        if not self.is_determinist():
            print("Automate is not deterministic.")
            return self  # Si l'automate n'est pas déterministe, affiche un message et retourne

        # Vérifie si l'automate n'est pas complet
        if not self.is_complete():
            print("Automate is not complete.")
            return self  # Si l'automate n'est pas complet, affiche un message et retourne

        new_final_state = []  # Liste pour stocker les nouveaux états finaux du complément

        # Parcourt chaque état de l'automate
        for state in self.state:
            # Vérifie si l'état n'est pas déjà un état final de l'automate d'origine
            if state not in self.final_state:
                new_final_state.append(state)  # Ajoute l'état à la liste des nouveaux états finaux du complément

        # Crée une nouvelle instance d'Automate représentant le complément
        new_automate = Automate(self.state, self.alphabet, self.initial_state, new_final_state, self.transitions)

        return new_automate  # Retourne l'automate complémentaire

    def read_automate(self):
        # Affiche les détails de l'automate créé

        # Affiche un message indiquant que l'automate a été créé
        print("Automate created")

        # Affiche les états de l'automate
        print("Automate State :", self.state)

        # Affiche l'alphabet de l'automate
        print("Alphabet :", self.alphabet)

        # Affiche les états initiaux de l'automate
        print("Initial(s) State(s) :", self.initial_state)

        # Affiche les états finaux de l'automate
        print("Final(s) State(s) :", self.final_state)

        # Appelle la méthode pour afficher la table de transitions de l'automate
        self.print_automate_transition_table()

    def recognize_word(self, word):
        # Vérifie si le mot donné est accepté par l'automate

        # Vérifie si l'automate n'est pas déterministe
        if not self.is_determinist():
            print("Automate is not deterministic.")
            return  # Si l'automate n'est pas déterministe, affiche un message et quitte la méthode

        # Parcourt chaque état initial de l'automate
        for initial_state in self.initial_state:
            current_state = initial_state
            valid_path = True  # Indicateur pour suivre le chemin valide dans l'automate

            # Parcourt chaque caractère du mot donné
            for char in word:
                # Vérifie si le caractère n'appartient pas à l'alphabet de l'automate
                if char not in self.alphabet:
                    print("Invalid character '" + char + "' in the input word '" + word + "'.")
                    valid_path = False
                    break  # Si le caractère est invalide, affiche un message et arrête le parcours

                next_state = None

                # Parcourt les transitions de l'automate
                for state, symbol, next_state_candidate in self.transitions:
                    # Vérifie si la transition correspond à l'état courant et au symbole actuel
                    if state == current_state and symbol == char:
                        next_state = next_state_candidate
                        break  # Trouve la transition correspondante et passe à l'état suivant

                # Vérifie si aucune transition n'a été trouvée pour l'état courant et le symbole actuel
                if next_state is None:
                    print("No transition available for state '" + current_state + "' and symbol '" + char + "'.")
                    valid_path = False
                    break  # Si aucune transition n'est disponible, affiche un message et arrête le parcours

                current_state = next_state  # Passe à l'état suivant

            # Vérifie si le chemin parcouru est valide et si l'état courant est un état final
            if valid_path and current_state in self.final_state:
                print("Word '" + word + "' is accepted.")
                return  # Si le mot est accepté, affiche un message et quitte la méthode

        # Si aucun chemin valide n'a été trouvé ou si aucun état final n'a été atteint
        print("Word '" + word + "' is not accepted.")  # Affiche un message indiquant que le mot n'est pas accepté

    def read_words_and_recognize(self):
        # Lit des mots depuis l'entrée utilisateur et vérifie s'ils sont acceptés par l'automate

        while True:
            # Demande à l'utilisateur de saisir un mot et le nettoie (supprime les espaces avant et après)
            word = input("Enter a word (type 'fin' to end): ").strip()

            # Vérifie si l'utilisateur a saisi "fin" pour terminer la saisie de mots
            if word.lower() == "fin":
                return  # Si l'utilisateur a saisi "fin", quitte la méthode

            # Appelle la méthode pour vérifier si le mot est accepté par l'automate
            self.recognize_word(word)

    def print_automate_transition_table(self):
        # Affiche la table de transitions de l'automate de manière structurée

        print("Transitions :")  # Affiche l'en-tête pour la table de transitions
        header = "I/F E"  # Initialise l'en-tête avec les colonnes
        # pour les états initiaux/finaux et les symboles de l'alphabet

        # Ajoute chaque symbole de l'alphabet à l'en-tête, centré dans une colonne de largeur 6
        for alphabet in sorted(self.alphabet):
            header += alphabet.center(6)

        print(header)  # Affiche l'en-tête complet de la table de transitions

        # Parcourt chaque état de l'automate, trié par ordre alphabétique
        for state in sorted(self.state):
            row = ""  # Initialise une nouvelle ligne pour l'état actuel

            # Ajoute 'I' à la ligne si l'état est initial, sinon ajoute un espace
            if state in self.initial_state:
                row += 'I '
            else:
                row += "  "

            # Ajoute 'F' à la ligne si l'état est final, sinon ajoute un espace
            if state in self.final_state:
                row += 'F '
            else:
                row += "  "

            row += str(state)  # Ajoute l'état actuel à la ligne

            # Parcourt chaque symbole de l'alphabet, trié par ordre alphabétique
            for symbol in sorted(self.alphabet):
                # Obtient les états suivants pour l'état actuel et le symbole actuel
                next_states = ",".join(self.successors_elem(state, symbol))

                # Ajoute les états suivants à la ligne, centrés dans une colonne de largeur 6
                row += next_states.center(6)

            print(row)  # Affiche la ligne complète de la table de transitions pour l'état actuel


def read_automate_from_file(name_text):
    # Fonction pour lire les données d'un automate à partir d'un fichier et créer une instance de la classe Automate

    transitions_state_automate = []  # Liste pour stocker les transitions de l'automate

    # Ouvre le fichier spécifié en mode lecture
    with open(name_text, 'r') as file:
        lines = file.readlines()  # Lit toutes les lignes du fichier
        num_symbols = int(lines[0].strip())  # Nombre de symboles dans l'alphabet
        num_states = int(lines[1].strip())  # Nombre d'états dans l'automate
        num_initial_states = int(lines[2].strip().split()[0])  # Nombre d'états initiaux
        initial_states = lines[2].strip().split()[1:num_initial_states + 1]  # Liste des états initiaux
        num_final_states = int(lines[3].strip().split()[0])  # Nombre d'états finaux
        final_states = lines[3].strip().split()[1:num_final_states + 1]  # Liste des états finaux
        num_transitions = int(lines[4].strip())  # Nombre de transitions
        # Parcourt les lignes correspondant aux transitions
        for line in lines[5:5 + num_transitions]:
            transition = line.strip()  # Supprime les espaces autour de la ligne
            transitions_state_automate.append(transition)  # Ajoute la transition à la liste

    # Crée l'alphabet de l'automate à partir du nombre de symboles
    alphabet_automate = [chr(ord('a') + i) for i in range(num_symbols)]

    # Crée la liste des états de l'automate à partir du nombre d'états
    state_automate = [str(i) for i in range(num_states)]

    # Crée une nouvelle instance de la classe Automate avec les données lues
    new_automate = Automate(state_automate, alphabet_automate, initial_states, final_states,
                            transitions_state_automate)

    return new_automate  # Retourne l'instance de l'automate créée à partir du fichier


def ask_and_print_automate_info():
    # Fonction pour demander à l'utilisateur de choisir un automate et afficher des informations sur celui-ci

    while True:  # Boucle infinie pour continuer à demander à l'utilisateur jusqu'à ce qu'il quitte
        try:
            print("Quel automate voulez-vous utiliser ? (0 pour quitter)")  # Demande à l'utilisateur de
            # choisir un automate
            number_file = int(input("> "))  # Lit le numéro de fichier saisi par l'utilisateur

            if number_file == 0:
                return  # Si l'utilisateur saisit 0, la fonction se termine

            if number_file < 10:
                number_file = str(0) + str(number_file)  # Formate le numéro de fichier
                # pour correspondre au format attendu
            file_name = "BDX4-" + str(number_file) + ".txt"  # Crée le nom de fichier à partir du numéro saisi
            new_automate = read_automate_from_file(file_name)  # Lit l'automate à partir du fichier spécifié
            new_automate.read_automate()  # Affiche les informations de l'automate lu

            # Vérifie si l'automate est déterministe et affiche le résultat correspondant
            if read_automate_from_file(file_name).is_determinist():
                print("This Automate is Determinist")
            else:
                print("This Automate is not Determinist")

            # Vérifie si l'automate est standard et affiche le résultat correspondant
            if read_automate_from_file(file_name).is_standard():
                print("This Automate is Standard")
            else:
                print("This Automate is not Standard")

            # Vérifie si l'automate est complet et affiche le résultat correspondant
            if read_automate_from_file(file_name).is_complete():
                print("This Automate is Complete")
            else:
                print("This Automate is not Complete")

            return new_automate  # Retourne l'instance de l'automate lu et affiché

        except FileNotFoundError:
            print("Le fichier n'existe pas")  # Gère l'erreur si le fichier spécifié n'existe pas
        except ValueError:
            print("Entrez un numéro valide")  # Gère l'erreur si l'utilisateur ne saisit pas un numéro valide


def menu():
    automate = ask_and_print_automate_info()  # Demande à l'utilisateur de choisir un automate et le récupère

    while True:  # Boucle infinie pour continuer à permettre à l'utilisateur d'effectuer des actions
        print("Quelle action voulez-vous réaliser ? (stop pour quitter)")
        action_name = str(input("> "))  # Lit l'action souhaitée par l'utilisateur

        # Vérifie si l'utilisateur souhaite quitter
        if action_name.lower() == "stop":
            return  # Termine la fonction si l'utilisateur entre "stop"

        # Effectue différentes actions en fonction de l'action choisie par l'utilisateur
        if action_name.lower() == "determiniser":
            automate = automate.determine()  # Détermine l'automate
        elif action_name.lower() == "standardiser":
            automate = automate.standardize()  # Standardise l'automate
        elif action_name.lower() == "completer":
            automate = automate.complete()  # Complète l'automate
        elif action_name.lower() == "reconnait":
            print("Quel mot ?")
            word = str(input("> "))  # Demande à l'utilisateur de saisir un mot
            automate.recognize_word(word)  # Reconnaît le mot dans l'automate
        elif action_name.lower() == "complement":
            automate = automate.complement()  # Calcule le complément de l'automate

        automate.print_automate_transition_table()  # Affiche la table de transitions de l'automate après chaque action


menu()
