# Owners : Maache Jawad, Delmas Matthias
"""❌"""
############################################################################################################

import tkinter
from tkinter import *
from tkinter import ttk, messagebox

##################################### VARIABLES #####################################

A1 = (
{1, 2, 3}, {'a', 'b'}, {(1, 'a'): {2}, (1, 'b'): {1}, (2, 'a'): {2}, (2, 'b'): {3}, (3, 'a'): {3}, (3, 'b'): {3}}, {1},
{3})
A2 = ({1, 2, 3, 4, 5}, {'a', 'b'},
      {(1, 'a'): {3}, (2, 'a'): {2}, (2, 'b'): {1}, (3, 'a'): {4}, (3, 'b'): {5}, (4, 'a'): {3}, (5, 'a'): {5}}, {1},
      {3})
listeAutomates = {"A1": A1, "A2": A2}

ACTUAL_PROGRESS = []
ACTUAL_WORD = ""
ACTUAL_RESULT = False


##################################### FONCTIONS #####################################


def lireMot(aut, m):
    """
    Fonction qui permet de lire un mot avec un automate

    @param aut:
    @param m:
    @return: bool, list
    """
    Q, sig, T, Qzero, A = aut
    i = 0
    n = len(m)
    progress = [Qzero]

    while i < n and Qzero != 0:
        if (Qzero, m[i]) in T:
            Qzero = T[(Qzero, m[i])]
            i += 1
        else:
            Qzero = 0

        progress.append(Qzero)

    return Qzero in A, progress


def obtenirAutomate():
    """
    Fonction qui permet d'obtenir l'automate sélectionné dans la liste
    @return:
    """
    return listeAutomates[listAutomates.get(ACTIVE)]


def testerMot():
    """
    Fonction qui permet de tester un mot avec un automate
    @return:
    """
    global ACTUAL_PROGRESS
    global ACTUAL_WORD
    global ACTUAL_RESULT
    # On récupère l'automate sélectionné
    automate = obtenirAutomate()

    # On récupère le mot à tester
    motATester = mot.get()

    # On teste le mot
    resultat, progress = lireMot(automate, motATester)

    # On affiche le résultat
    if resultat:
        resLabel.config(text="Le mot est accepté", fg="green")
    else:
        resLabel.config(text="Le mot n'est pas accepté", fg="red")

    # On affiche la progression
    ACTUAL_PROGRESS = progress
    ACTUAL_WORD = motATester
    ACTUAL_RESULT = resultat
    boutonChaine.grid(row=5, column=2, sticky=S, padx=5, pady=5, columnspan=3)
    boutonRuban.grid(row=6, column=2, sticky=N, padx=5, pady=5, columnspan=3)


def creerAutomate():
    """
    Fonction qui permet de créer un automate
    @return:
    """
    # On ouvre une nouvelle fenêtre
    fenetre = Toplevel(root)
    fenetre.title("Création d'un automate")
    fenetre.geometry("700x500")

    # On crée un grid pour la fenêtre
    fenetre.grid_columnconfigure(0, weight=1)
    fenetre.grid_columnconfigure(1, weight=1)
    fenetre.grid_columnconfigure(2, weight=1)
    fenetre.grid_columnconfigure(3, weight=1)
    for i in range(13):
        fenetre.grid_rowconfigure(i, weight=1)

    v = tkinter.StringVar()
    v.set(None)

    Canvas(fenetre, width=800, height=600, bg="lightblue").grid(row=0, column=0, rowspan=13, columnspan=4, sticky=NSEW)

    Label(fenetre, text="Nom de l'automate", font=("Helvetica", 13, "bold"), bg="lightblue").grid(row=0,
                                                                                                  column=0,
                                                                                                  sticky=S,
                                                                                                  padx=5,
                                                                                                  pady=5,
                                                                                                  columnspan=4)
    nomAutomate = Entry(fenetre, width=50, justify="center")
    nomAutomate.grid(row=1, column=0, sticky=N, padx=5, pady=5, columnspan=4)

    # On insère les éléments dans la fenêtre
    Label(fenetre, text="Nombre d'états", font=("Helvetica", 13, "bold"), bg="lightblue").grid(row=2, column=0,
                                                                                               sticky=S,
                                                                                               pady=5, columnspan=4)
    nbEtats = Entry(fenetre, width=10, justify="center")
    nbEtats.grid(row=3, column=0, pady=5, sticky=N, columnspan=4)

    Label(fenetre, text="Alphabet (séparer les éléments par des virgules)", font=("Helvetica", 13, "bold"),
          bg="lightblue").grid(row=4,
                               column=0,
                               sticky=S,
                               pady=5, columnspan=4)
    alphabet = Entry(fenetre, width=50, justify="center")
    alphabet.grid(row=5, column=0, pady=5, sticky=N, columnspan=4)

    Label(fenetre, text="Etats acceptants (séparer les éléments par des virgules)", font=("Helvetica", 13, "bold"),
          bg="lightblue").grid(row=6, column=0, sticky=S, pady=5, columnspan=4)
    etatsAcceptants = Entry(fenetre, width=50, justify="center")
    etatsAcceptants.grid(row=7, column=0, pady=5, sticky=N, columnspan=4)

    Label(fenetre, text="Automate Complet / Incomplet", font=("Helvetica", 13, "bold"), bg="lightblue").grid(row=8,
                                                                                                             column=0,
                                                                                                             sticky=S,
                                                                                                             padx=5,
                                                                                                             pady=5,
                                                                                                             columnspan=4)
    r3 = Radiobutton(fenetre, text="Automate complet", variable=v, value="Complet", bg="lightblue")
    r3.grid(row=9, column=1, sticky=N, padx=5, pady=5)
    r4 = Radiobutton(fenetre, text="Automate incomplet", variable=v, value="Incomplet", bg="lightblue")
    r4.grid(row=9, column=2, sticky=N, padx=5, pady=5)

    Label(fenetre, text=" ", bg="lightblue").grid(row=10, column=0, sticky=NSEW, columnspan=4)

    Button(fenetre, text="Créer AFD",
           command=lambda: creerTableauDeter(nbEtats.get(), alphabet.get(), etatsAcceptants.get(), v.get(),
                                             nomAutomate.get()),
           bg="lightseagreen").grid(row=11, column=0, sticky=NSEW, padx=5, pady=5, columnspan=2)
    Button(fenetre, text="Créer AFN",
           command=lambda: creerTableauNonDeter(nbEtats.get(), alphabet.get(), etatsAcceptants.get(), v.get(),
                                                nomAutomate.get()),
           bg="lightseagreen").grid(row=11, column=2, sticky=NSEW, padx=5, pady=5, columnspan=2)


def creerTableauDeter(nbEtats, alphabet, etatsAcceptants, v, nomAutomate):
    """
    Fonction qui permet de créer un tableau pour un automate déterministe
    @param nbEtats:
    @param alphabet:
    @param etatsAcceptants:
    @param v:
    @param nomAutomate:
    @return:
    """
    if nbEtats and int(nbEtats) < 1:
        messagebox.showerror("Erreur", "Le nombre d'états doit être supérieur à 0")
        return

    if not nbEtats or not alphabet or not etatsAcceptants or not v or not nomAutomate:
        messagebox.showerror("Erreur", "Un ou plusieurs champs sont vides")
        return

    Q = set(range(1, int(nbEtats) + 1))
    sig = sorted(alphabet.split(","))
    T = {}
    A = set([int(i) for i in etatsAcceptants.split(",")])
    d = {}

    if any(x not in Q for x in A):
        messagebox.showerror("Erreur", "Un ou plusieurs états acceptants ne sont pas dans l'ensemble des états")
        return

    n = len(Q)
    m = len(sig)

    # On ouvre une nouvelle fenêtre
    fenetre = Toplevel(root)
    fenetre.title("Création d'un automate")
    fenetre.geometry("1200x900")

    for i in range(n + 4):
        fenetre.grid_rowconfigure(i, weight=1)
    for j in range(m + 3):
        fenetre.grid_columnconfigure(j, weight=1)

    canvas = Canvas(fenetre, width=1200, height=900, bg="lightblue")
    canvas.grid(row=0, column=0, rowspan=n + 5, columnspan=m + 3, sticky=NSEW)

    # On insère les éléments dans la fenêtre
    Label(fenetre, text="Table de transition", font=("Helvetica", 20, ["bold", "underline"]), bg="lightblue").grid(
        row=0, column=0,
        sticky=N, padx=5,
        pady=10,
        columnspan=m + 3)

    Label(fenetre, text="État initial", font=("Helvetica", 15, "bold"), bg="lightblue").grid(row=0, column=0,
                                                                                             sticky=S, padx=5,
                                                                                             pady=5, columnspan=m + 3)

    statesList = ttk.Combobox(fenetre, values=[str(i) for i in Q], state="readonly")
    statesList.grid(row=1, column=0, sticky=N, padx=5, pady=5, columnspan=m + 3)

    for i in range(1, n + 2):
        for j in range(1, m + 2):
            if i == 1:
                if j == 1:
                    Label(fenetre, text="Q \ Σ", borderwidth=1, relief="solid",
                          font=("Helvetica", 16, "bold")).grid(row=i + 1, column=j, sticky=NSEW)
                else:
                    Label(fenetre, text=sig[j - 2], borderwidth=1, relief="solid", font=("Helvetica", 16, "bold")).grid(
                        row=i + 1, column=j, sticky=NSEW)
            else:
                if j == 1:
                    if list(Q)[i - 2] in A:
                        Label(fenetre, text=list(Q)[i - 2], borderwidth=1, relief="solid",
                              font=("Helvetica", 16, "bold"),
                              bg="darkolivegreen1").grid(row=i + 1, column=j, sticky=NSEW)
                    else:
                        Label(fenetre, text=list(Q)[i - 2], borderwidth=1, relief="solid",
                              font=("Helvetica", 16, "bold")).grid(row=i + 1, column=j, sticky=NSEW)

                else:
                    d["{0},{1}".format(list(Q)[i - 2], sig[j - 2])] = ttk.Combobox(fenetre, values=[str(i) for i in Q],
                                                                                   state="readonly",
                                                                                   justify="center",
                                                                                   font=("Helvetica", 16))
                    d["{0},{1}".format(list(Q)[i - 2], sig[j - 2])].grid(row=i + 1, column=j, sticky=NSEW)
                    if v == "Complet":
                        d["{0},{1}".format(list(Q)[i - 2], sig[j - 2])].set(1)

    Label(fenetre, text=" ", bg="lightblue").grid(row=n + 3, column=0, sticky=NSEW, padx=5, pady=5, columnspan=m + 3)

    Button(fenetre, text="Valider", command=lambda: validerTableauDeter(Q, sig, T, statesList.get(), A, d, nomAutomate),
           bg="lightseagreen", font=("Helvetica", 16, "bold")).grid(row=n + 4, column=0, sticky=NSEW, padx=5, pady=5,
                                                                    columnspan=m + 3)


def validerTableauDeter(Q, sig, T, Qzero, A, d, nomAutomate):
    """
    Fonction qui permet de valider le tableau de transition pour un automate déterministe
    @param Q:
    @param sig:
    @param T:
    @param Qzero:
    @param A:
    @param d:
    @param nomAutomate:
    @return:
    """
    if not Qzero:
        messagebox.showerror("Erreur", "L'état initial n'a pas été sélectionné")
        return

    for key, value in d.items():
        if value.get():
            num, let = key.split(",")
            T[(int(num), let)] = {int(value.get())}

    automate = (Q, sig, T, {int(Qzero)}, A)

    listeAutomates[nomAutomate] = automate
    listAutomates.insert(END, nomAutomate)

    messagebox.showinfo("Succès", "L'automate a bien été créé")


def creerTableauNonDeter(nbEtats, alphabet, etatsAcceptants, v, nomAutomate):
    """
    Fonction qui permet de créer un tableau pour un automate non déterministe
    @param nbEtats:
    @param alphabet:
    @param etatsAcceptants:
    @param v:
    @param nomAutomate:
    @return:
    """
    if nbEtats and int(nbEtats) < 1:
        messagebox.showerror("Erreur", "Le nombre d'états doit être supérieur à 0")
        return

    if not nbEtats or not alphabet or not etatsAcceptants or not v or not nomAutomate:
        messagebox.showerror("Erreur", "Un ou plusieurs champs sont vides")
        return

    Q = set(range(1, int(nbEtats) + 1))
    sig = sorted(alphabet.split(","))
    T = {}
    A = set([int(i) for i in etatsAcceptants.split(",")])
    d = {}

    if any(x not in Q for x in A):
        messagebox.showerror("Erreur", "Un ou plusieurs états acceptants ne sont pas dans l'ensemble des états")
        return

    n = len(Q)
    m = len(sig)

    # On ouvre une nouvelle fenêtre
    fenetre = Toplevel(root)
    fenetre.title("Création d'un automate")
    fenetre.geometry("1200x900")

    for i in range(n + 4):
        fenetre.grid_rowconfigure(i, weight=1)
    for j in range(m + 3):
        fenetre.grid_columnconfigure(j, weight=1)

    canvas = Canvas(fenetre, width=1200, height=900, bg="lightblue")
    canvas.grid(row=0, column=0, rowspan=n + 5, columnspan=m + 3, sticky=NSEW)

    # On insère les éléments dans la fenêtre
    Label(fenetre, text="Table de transition", font=("Helvetica", 20, ["bold", "underline"]), bg="lightblue").grid(
        row=0, column=0,
        sticky=N, padx=5,
        pady=10,
        columnspan=m + 3)

    Label(fenetre, text="État initial", font=("Helvetica", 15, "bold"), bg="lightblue").grid(row=0, column=0,
                                                                                             sticky=S, padx=5,
                                                                                             pady=5, columnspan=m + 3)

    statesList = Listbox(fenetre, selectmode="multiple", exportselection=0, width=10, height=min(4, n),
                         font=("Helvetica", 14),
                         justify="center")
    statesList.grid(row=1, column=0, sticky=N, padx=5, pady=5, columnspan=m + 3)

    for i in Q:
        statesList.insert(END, i)

    for i in range(1, n + 2):
        for j in range(1, m + 2):
            if i == 1:
                if j == 1:
                    Label(fenetre, text="Q \ Σ", borderwidth=1, relief="solid",
                          font=("Helvetica", 16, "bold")).grid(row=i + 1, column=j, sticky=NSEW)
                else:
                    Label(fenetre, text=sig[j - 2], borderwidth=1, relief="solid", font=("Helvetica", 16, "bold")).grid(
                        row=i + 1, column=j, sticky=NSEW)
            else:
                if j == 1:
                    if list(Q)[i - 2] in A:
                        Label(fenetre, text=list(Q)[i - 2], borderwidth=1, relief="solid",
                              font=("Helvetica", 16, "bold"),
                              bg="darkolivegreen1").grid(row=i + 1, column=j, sticky=NSEW)
                    else:
                        Label(fenetre, text=list(Q)[i - 2], borderwidth=1, relief="solid",
                              font=("Helvetica", 16, "bold")).grid(row=i + 1, column=j, sticky=NSEW)

                else:
                    d["{0},{1}".format(list(Q)[i - 2], sig[j - 2])] = Entry(fenetre, width=10, justify="center",
                                                                            font=("Helvetica", 16), borderwidth=1,
                                                                            relief="solid")
                    d["{0},{1}".format(list(Q)[i - 2], sig[j - 2])].grid(row=i + 1, column=j, sticky=NSEW)

    Label(fenetre, text=" ", bg="lightblue").grid(row=n + 3, column=0, sticky=NSEW, padx=5, pady=5, columnspan=m + 3)

    Button(fenetre, text="Valider", command=lambda: validerTableauNonDeter(Q, sig, T, statesList, A, d, v, nomAutomate),
           bg="lightseagreen", font=("Helvetica", 16, "bold")).grid(row=n + 4, column=0, sticky=NSEW, padx=5, pady=5,
                                                                    columnspan=m + 3)


def validerTableauNonDeter(Q, sig, T, Qzero, A, d, v, nomAutomate):
    """
    Fonction qui permet de valider le tableau de transition pour un automate non déterministe
    @param Q:
    @param sig:
    @param T:
    @param Qzero:
    @param A:
    @param d:
    @param v:
    @param nomAutomate:
    @return:
    """
    Qzero = set(i + 1 for i in Qzero.curselection())

    if not Qzero:
        messagebox.showerror("Erreur", "L'état initial n'a pas été sélectionné")
        return

    for key, value in d.items():
        valueSet = set()
        for i in value.get().split(","):
            if v == "Complet" and not i:
                messagebox.showerror("Erreur", "Un ou plusieurs champs sont vides")
                return
            if i and not 0 < int(i) <= len(Q):
                messagebox.showerror("Erreur", "Un ou plusieurs états ne sont pas dans l'ensemble des états")
                return
            if i:
                valueSet.add(int(i))

        if valueSet:
            num, let = key.split(",")
            T[(int(num), let)] = valueSet

    automate = (Q, sig, T, Qzero, A)

    listeAutomates[nomAutomate] = automate
    listAutomates.insert(END, nomAutomate)

    messagebox.showinfo("Succès", "L'automate a bien été créé")


def showChaine():
    """
    Fonction qui permet d'afficher la lecture en chaîne
    @return:
    """
    global ACTUAL_PROGRESS
    global ACTUAL_WORD
    global ACTUAL_RESULT

    # On crée une nouvelle fenêtre
    fenetre = Toplevel(root)
    fenetre.title("Lecture en chaîne")
    fenetre.geometry("1000x300")

    n = len(ACTUAL_PROGRESS)

    fenetre.grid_rowconfigure(0, weight=1)
    fenetre.grid_rowconfigure(1, weight=1)
    fenetre.grid_rowconfigure(2, weight=1)

    for i in range(n * 2 + 1):
        fenetre.grid_columnconfigure(i, weight=1)

    Canvas(fenetre, width=1000, height=300, bg="lightblue").grid(row=0, column=0, rowspan=3, columnspan=n * 2 + 1,
                                                                 sticky=NSEW)

    # On affiche la progression
    Label(fenetre, text="Lecture en chaîne", font=("Helvetica", 20, ["underline", "bold"]), bg="lightblue").grid(row=0,
                                                                                                                 column=0,
                                                                                                                 sticky=N,
                                                                                                                 padx=5,
                                                                                                                 pady=5,
                                                                                                                 columnspan=n * 2 + 1)

    Label(fenetre, text=str(ACTUAL_PROGRESS[0]), font=("Helvetica", 16, "bold"), bg="lightblue").grid(row=1, column=0,
                                                                                                      sticky=NSEW,
                                                                                                      padx=5, pady=5)
    for i in range(1, n):
        Label(fenetre, text="⇒", font=("Helvetica", 30, "bold"), bg="lightblue").grid(row=1, column=2 * i - 1, padx=5,
                                                                                      pady=5)
        Label(fenetre, text=str(ACTUAL_WORD[i - 1]), font=("Helvetica", 16, "bold"), bg="lightblue").grid(row=1,
                                                                                                          column=2 * i - 1,
                                                                                                          sticky=N,
                                                                                                          padx=5,
                                                                                                          pady=5)
        if ACTUAL_PROGRESS[i] == 0:
            Label(fenetre, text="Erreur", font=("Helvetica", 16, "bold"), bg="lightblue", fg="red").grid(row=1,
                                                                                                         column=2 * i,
                                                                                                         sticky=NSEW,
                                                                                                         padx=5, pady=5)
        else:
            Label(fenetre, text=str(ACTUAL_PROGRESS[i]), font=("Helvetica", 16, "bold"), bg="lightblue").grid(row=1,
                                                                                                              column=2 * i,
                                                                                                              sticky=NSEW,
                                                                                                              padx=5,
                                                                                                              pady=5)

    Label(fenetre, text="⇒", font=("Helvetica", 30, "bold"), bg="lightblue").grid(row=1, column=2 * n - 1, padx=5,
                                                                                  pady=5)
    Label(fenetre, text="Result", font=("Helvetica", 16, "bold"), bg="lightblue").grid(row=1, column=2 * n - 1,
                                                                                       sticky=S, padx=5, pady=5)

    if ACTUAL_RESULT:
        Label(fenetre, text="Accepté", font=("Helvetica", 16, "bold"), bg="lightblue", fg="green").grid(row=1,
                                                                                                        column=2 * n,
                                                                                                        sticky=NSEW,
                                                                                                        padx=5, pady=5)
    else:
        Label(fenetre, text="Refusé", font=("Helvetica", 16, "bold"), bg="lightblue", fg="red").grid(row=1,
                                                                                                     column=2 * n,
                                                                                                     sticky=NSEW,
                                                                                                     padx=5, pady=5)


def showRuban():
    """
    Fonction qui permet d'afficher la lecture en ruban
    @return:
    """
    global ACTUAL_PROGRESS
    global ACTUAL_WORD
    global ACTUAL_RESULT

    n = len(ACTUAL_PROGRESS)
    state = 1

    # On crée une nouvelle fenêtre
    fenetre = Toplevel(root)
    fenetre.title("Lecture en ruban")
    fenetre.geometry(str(n * 75 + 175) + "x450")

    canvas = Canvas(fenetre, width=n * 75 + 175, height=450, bg="lightblue")
    canvas.pack()

    def drawRuban(state):
        canvas.delete("all")
        canvas.create_text((n * 75 + 175) / 2, 50, text="Lecture Ruban", font=("Helvetica", 20, ["underline", "bold"]))
        buttonBack = Button(fenetre, text="⏪", command=lambda: drawRuban(state - 1), bg="lightseagreen",
                            font=("Helvetica", 20, "bold"), width=5)
        buttonBack.pack()
        # Place the button to the center left of the canvas
        buttonBack.place(x=(n * 75 + 175) / 2 - 120, y=370)
        buttonForward = Button(fenetre, text="⏩", command=lambda: drawRuban(state + 1), bg="lightseagreen",
                               font=("Helvetica", 20, "bold"), width=5)
        buttonForward.pack()
        buttonForward.place(x=(n * 75 + 175) / 2 + 30, y=370)
        if state == 1:
            buttonBack.config(state=DISABLED)
        else:
            buttonBack.config(state=NORMAL)
        if state == n:
            buttonForward.config(state=DISABLED)
        else:
            buttonForward.config(state=NORMAL)

        canvas.create_polygon(125, 225, 100, 250, 150, 250, fill="lightgray", outline="black")
        canvas.create_rectangle(100, 250, 150, 300, fill="lightgray", outline="black")
        canvas.create_text(125, 275, text=ACTUAL_PROGRESS[0], font=("Helvetica", 16, "bold"))

        for i in range(1, state):
            if ACTUAL_PROGRESS[i] == 0:
                canvas.create_polygon(50 + 75 * (i + 1), 225, 75 * (i + 1) + 25, 250, 75 * (i + 1) + 75, 250,
                                      fill="indianred1", outline="black")
                canvas.create_rectangle(75 * (i + 1) + 25, 250, 75 * (i + 1) + 75, 300, fill="indianred1",
                                        outline="black")
            elif i + 1 == n:
                if ACTUAL_RESULT:
                    canvas.create_polygon(50 + 75 * (i + 1), 225, 75 * (i + 1) + 25, 250, 75 * (i + 1) + 75, 250,
                                          fill="darkolivegreen1", outline="black")
                    canvas.create_rectangle(75 * (i + 1) + 25, 250, 75 * (i + 1) + 75, 300, fill="darkolivegreen1",
                                            outline="black")
                else:
                    canvas.create_polygon(50 + 75 * (i + 1), 225, 75 * (i + 1) + 25, 250, 75 * (i + 1) + 75, 250,
                                          fill="indianred1", outline="black")
                    canvas.create_rectangle(75 * (i + 1) + 25, 250, 75 * (i + 1) + 75, 300, fill="indianred1",
                                            outline="black")
            else:
                canvas.create_polygon(50 + 75 * (i + 1), 225, 75 * (i + 1) + 25, 250, 75 * (i + 1) + 75, 250,
                                      fill="lightgray", outline="black")
                canvas.create_rectangle(75 * (i + 1) + 25, 250, 75 * (i + 1) + 75, 300, fill="lightgray",
                                        outline="black")
            canvas.create_text(75 * (i + 1) + 50, 275, text=ACTUAL_PROGRESS[i], font=("Helvetica", 16, "bold"))
            canvas.create_rectangle(50 + 75 * i, 150, 75 * i + 125, 225, fill="lightgray", outline="black")
            canvas.create_text(75 * i + 87.5, 187.5, text=ACTUAL_WORD[i - 1], font=("Helvetica", 16, "bold"))

    drawRuban(state)


def AfficherTable():
    """
    Fonction qui permet d'afficher la table de transition
    @return:
    """
    automate = obtenirAutomate()
    Q, sig, T, Qzero, A = automate
    Q, sig = sorted(list(Q)), sorted(list(sig))
    n = len(Q)
    m = len(sig)
    print(Qzero)
    print(T)
    # On crée une nouvelle fenêtre
    fenetre = Toplevel(root)
    fenetre.title("Table de transition")
    fenetre.geometry("800x600")

    for i in range(n + 3):
        fenetre.grid_rowconfigure(i, weight=1)
    for j in range(m + 3):
        fenetre.grid_columnconfigure(j, weight=1)

    canvas = Canvas(fenetre, width=800, height=600, bg="lightblue")
    canvas.grid(row=0, column=0, rowspan=n + 3, columnspan=m + 3, sticky=NSEW)

    # On affiche la table de transition
    Label(fenetre, text="Table de transition", font=("Helvetica", 20, ["bold", "underline"]), bg="lightblue").grid(
        row=0, column=0,
        sticky=NSEW, padx=5,
        pady=5,
        columnspan=m + 3)

    for i in range(1, n + 2):
        for j in range(1, m + 2):
            if i == 1:
                if j == 1:
                    Label(fenetre, text="Q \ Σ", borderwidth=1, relief="solid",
                          font=("Helvetica", 16, "bold")).grid(row=i, column=j, sticky=NSEW)
                else:
                    Label(fenetre, text=sig[j - 2], borderwidth=1, relief="solid", font=("Helvetica", 16, "bold")).grid(
                        row=i, column=j, sticky=NSEW)
            else:
                if j == 1:
                    if Q[i - 2] in A:
                        Label(fenetre, text=Q[i - 2], borderwidth=1, relief="solid", font=("Helvetica", 16, "bold"),
                              bg="darkolivegreen1").grid(row=i, column=j, sticky=NSEW)
                    else:
                        Label(fenetre, text=Q[i - 2], borderwidth=1, relief="solid",
                              font=("Helvetica", 16, "bold")).grid(row=i, column=j, sticky=NSEW)

                    if Q[i - 2] in Qzero:
                        Label(fenetre, text="⇒", font=("Helvetica", 30, "bold"), bg="lightblue", fg="cyan4").grid(row=i,
                                                                                                                  column=0,
                                                                                                                  sticky=E)
                else:
                    if (Q[i - 2], sig[j - 2]) in T:
                        Label(fenetre, text=T[(Q[i - 2], sig[j - 2])], borderwidth=1, relief="solid",
                              font=("Helvetica", 16)).grid(row=i, column=j, sticky=NSEW)
                    else:
                        Label(fenetre, text="", borderwidth=1, relief="solid", font=("Helvetica", 16, "bold")).grid(
                            row=i, column=j, sticky=NSEW)


def complet():
    """
    Fonction qui permet de compléter un automate
    @return:
    """
    automate = obtenirAutomate()
    Q, sig, T, Qzero, A = automate

    if len(T) < len(Q) * len(sig):
        Q.add(len(Q) + 1)

    for n in Q:
        for l in sig:
            if not (n, l) in T:
                T[(n, l)] = {len(Q)}

    automate = (Q, sig, T, Qzero, A)
    listeAutomates[listAutomates.get(ACTIVE)] = automate

    # On remplace l'automate dans la liste
    listAutomates.delete(0, END)
    for key in listeAutomates:
        listAutomates.insert(END, key)

    messagebox.showinfo("Succès", "L'automate a bien été complété")


def accessible(aut):
    """
    Fonction qui permet de trouver les états accessibles
    @param aut:
    @return:
    """
    Q, sig, T, Qzero, A = aut

    visited = Qzero.copy()
    queue = list(Qzero)

    while queue:
        x = queue.pop(0)

        for l in sig:
            if (x, l) in T:
                target = T[(x, l)]
                for state in target:
                    if not state in visited:
                        visited.add(state)
                        queue.append(state)

    return visited


def coAccessible(aut):
    """
    Fonction qui permet de trouver les états co-accessibles
    @param aut:
    @return:
    """
    Q, sig, T, Qzero, A = aut

    invT = {}
    for k in T:
        n, l = k
        for state in T[k]:
            if not (state, l) in invT:
                invT[(state, l)] = {n}
            else:
                invT[(state, l)].add(n)

    visited = A.copy()
    queue = list(A)

    while queue:
        x = queue.pop(0)

        for l in sig:
            if (x, l) in invT:
                target = invT[(x, l)]
                for val in target:
                    if val not in visited:
                        visited.add(val)
                        queue.append(val)

    return visited


def emonder():
    """
    Fonction qui permet d'émonder un automate
    @param aut:
    @return:
    """
    aut = obtenirAutomate()
    Q, sig, T, Qzero, A = aut

    acc = accessible(aut)
    coAcc = coAccessible(aut)

    newQ = {i for i in acc if i in coAcc}

    switch = {list(newQ)[i]: i + 1 for i in range(len(newQ))}

    newA = {switch[i] for i in A}
    newT = {}
    for k in T:
        n, l = k
        for state in T[k]:
            if state in newQ:
                if (switch[n], l) in newT:
                    newT[(switch[n], l)].add(switch[state])
                else:
                    newT[(switch[n], l)] = {switch[state]}
    newQ = set(range(1, len(newQ) + 1))

    newQzero = {switch[i] for i in Qzero}

    automate = (newQ, sig, newT, newQzero, newA)
    listeAutomates[listAutomates.get(ACTIVE)] = automate
    print(newT)
    # On remplace l'automate dans la liste
    listAutomates.delete(0, END)
    for key in listeAutomates:
        listAutomates.insert(END, key)

    messagebox.showinfo("Succès", "L'automate a bien été émondé")


##################################### INTERFACE #####################################

# On crée la fenêtre principale
root = Tk()
root.title("Automates")
root.geometry("1000x600")
# On crée un grid pour la fenêtre
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)
root.grid_columnconfigure(3, weight=1)
root.grid_columnconfigure(4, weight=1)
root.grid_columnconfigure(5, weight=1)
root.grid_columnconfigure(6, weight=1)
root.grid_columnconfigure(7, weight=1)
root.grid_columnconfigure(8, weight=1)
root.grid_columnconfigure(9, weight=1)
root.grid_columnconfigure(10, weight=1)
root.grid_columnconfigure(11, weight=1)
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=1)
root.grid_rowconfigure(4, weight=1)

# Canvas pour séparer la fenêtre en deux parties : partie gauche pour les options, partie droite pour les résultats


###### PARTIE GAUCHE ######
Canvas(root, width=500, height=500, bg="lightblue").grid(row=0, column=0, rowspan=12, columnspan=2, sticky=NSEW)

# On crée un bouton pour créer un automate
boutonCreer = Button(root, text="Créer un automate", bg="lightseagreen", command=creerAutomate,
                     font=("Helvetica", 14, "bold"))
boutonCreer.grid(row=0, column=0, sticky=NSEW, padx=5, pady=5, columnspan=2)

# Label vide pour créer un espace entre les éléments (plus esthétique)
Label(root, text=" ", bg="lightblue").grid(row=1, column=0, sticky=NSEW, padx=5, pady=5, columnspan=2)

# On crée la liste des automates
labelAutomates = Label(root, text="Liste des automates", bg="lightblue", font=("Helvetica", 14, ["bold", "underline"]),
                       justify="center")
labelAutomates.grid(row=2, column=0, sticky=S, padx=5, pady=5, columnspan=2)
listAutomates = Listbox(root, justify="center", font=("Helvetica", 12), selectmode=SINGLE, height=8)
listAutomates.grid(row=3, column=0, rowspan=2, sticky=NSEW, padx=5, pady=5, columnspan=2)

# On crée un bouton pour compléter l'automate
boutonCompleter = Button(root, text="Compléter l'automate", bg="lightseagreen", font=("Helvetica", 12, "bold"),
                         command=complet)
boutonCompleter.grid(row=5, column=0, sticky=NSEW, padx=5, pady=5)

# On crée un bouton pour émonder l'automate
boutonEmonder = Button(root, text="Émonder l'automate", bg="lightseagreen", font=("Helvetica", 12, "bold"),
                       command=emonder)
boutonEmonder.grid(row=5, column=1, sticky=NSEW, padx=5, pady=5)

# On crée un bouton pour afficher la table de transition de l'automate sélectionné
boutonTable = Button(root, text="Afficher la table de transition", bg="lightseagreen", font=("Helvetica", 12, "bold"),
                     command=AfficherTable)
boutonTable.grid(row=6, column=0, sticky=NS, padx=5, pady=5, columnspan=2)

# Label vide pour créer un espace entre les éléments (plus esthétique)
Label(root, text=" ", bg="lightblue").grid(row=7, column=0, sticky=NSEW, padx=5, pady=5, columnspan=2)

# On crée une zone de texte pour taper le mot à tester
labelMot = Label(root, text="Mot à tester", bg="lightblue", font=("Helvetica", 14, ["bold", "underline"]))
labelMot.grid(row=8, column=0, sticky=S, padx=5, pady=5, columnspan=2)
mot = Entry(root)
mot.grid(row=9, column=0, sticky=NSEW, padx=5, pady=5, columnspan=2)

# Label vide pour créer un espace entre les éléments (plus esthétique)
Label(root, text=" ", bg="lightblue").grid(row=10, column=0, sticky=NSEW, padx=5, pady=5, columnspan=2)

# On crée un bouton pour tester le mot
boutonTester = Button(root, text="Tester", command=testerMot, bg="lightseagreen", font=("Helvetica", 12, "bold"))
boutonTester.grid(row=11, column=0, sticky=NSEW, padx=5, pady=5, columnspan=2)

####### PARTIE DROITE #######
Canvas(root, width=500, height=500, bg="lightgray").grid(row=0, column=2, rowspan=12, columnspan=3, sticky=NSEW)

# On crée une zone de texte pour afficher le résultat
labelResultat = Label(root, text="Résultat de la lecture", font=("Helvetica", 20, ["bold", "underline"]),
                      bg="lightgray")
labelResultat.grid(row=1, column=2, padx=5, pady=5, columnspan=3)
resLabel = Label(root, bg="lightgray", text=" ", font=("Helvetica", 16, "bold"))
resLabel.grid(row=2, column=2, sticky=N, padx=5, pady=5, columnspan=3)

# Label vide pour créer un espace entre les éléments (plus esthétique)
Label(root, text=" ", bg="lightgray").grid(row=3, column=2, padx=5, pady=5, columnspan=3, rowspan=2)

# On crée une zone de texte pour afficher la lecture en chaine et en ruban
boutonChaine = Button(root, text="Voir la lecture en chaîne", width=20, command=showChaine, bg="darkgoldenrod2",
                      font=("Helvetica", 12, "bold"))
boutonRuban = Button(root, text="Voir la lecture en ruban", width=20, command=showRuban, bg="darkgoldenrod2",
                     font=("Helvetica", 12, "bold"))

##################################### MAIN #####################################

if __name__ == '__main__':
    # On ajoute les automates à la liste
    for automate in listeAutomates:
        listAutomates.insert(END, automate)

    # On lance la fenêtre principale
    root.mainloop()
