import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import simpledialog
import random
import os

# print('curpath : ' , os.curdir)
# print(os.listdir('cards'))
# pass
class Blackjackinterface:
    def __init__(self):
        # Create the main window
        self.window = tk.Tk()
        self.window.title("Blackjack Welcome Page")
        self.window.attributes('-fullscreen', 1)
        self.window.title("Black Jack")
        self.bg_image = tk.PhotoImage(file="fond_ecrant_avec_titre.png")

        # Create a label with the background image
        self.bg_label = tk.Label(self.window, image=self.bg_image, bg='black')
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        # bouton_tirer_carte= tk.Button(ecr, text="Carte!",)       
        self.quitter_boutton = tk.Button(self.window, text="quitter", bg="gray", fg="black",activebackground="black",activeforeground='gray',relief=tk.FLAT, command=self.quitter)
        self.start_button = tk.Button(self.window, text="Start Game", bg="gray", fg='black',activebackground="black",activeforeground='gray',relief=tk.FLAT, command=self.start_game)
        self.rules_button = tk.Button(self.window, text="Rules", bg='gray', fg='black',activebackground="black",activeforeground='gray',relief=tk.FLAT, command=self.show_rules)
        self.start_duo = tk.Button(self.window, text="mode dificile", bg='gray', fg='black',activebackground="black",activeforeground='gray',relief=tk.FLAT, command=self.start_difficil)
   
        #position des bouton 
        self.start_button.place(x=491,y=280)
        self.start_duo.place(x=982,y=280)
        self.rules_button.place(x=760,y=450)
        self.quitter_boutton.place(x=760,y=550)

    def quitter(self):
        #self.master.destroy() marche pas
        self.window.destroy()
    def start_game(self):
        self.window.destroy() 
    
    def start_difficil(self):
        self.window.destroy
       


    def show_rules(self):
        self.rules_window = tk.Toplevel(self.window)
        messagebox.showinfo("Règle du BlackJack", "Le Blackjack est un jeu de cartes où le joueur vise à obtenir un score aussi proche que possible de 21 sans le dépasser. Le jeu se joue avec un ou plusieurs jeux de 52 cartes. La valeur de chaque carte est la suivante :\n\n- 2 à 10 : valeur faciale\n- Valet, Dame, Roi : 10\n- As : 1 ou 11 (au choix du joueur)\n\nLe jeu commence avec le joueur et le croupier recevant chacun deux cartes. Les cartes du joueur sont distribuées face visible, tandis qu'une des cartes du croupier est distribuée face cachée. Le joueur a alors la possibilité de 'tirer' (prendre une autre carte) ou de 'rester' (garder son score actuel). Si le score du joueur dépasse 21, il 'explose' et perd la partie. Si le score du joueur est inférieur ou égal à 21, le croupier joue ensuite sa main. Le croupier doit tirer s'il a un score inférieur à 17, et rester s'il a un score de 17 ou plus. Si le croupier 'explose', le joueur gagne. Si le score du croupier est plus proche de 21 que celui du joueur, le joueur perd. Si le score du joueur est plus proche de 2")


class BlackjackApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Blackjack")
        self.master.attributes("-fullscreen",1)
        self.bg_game = tk.PhotoImage(file="fond_ecran_accueil_blackjackBlanc.png")
        self.bg_label = tk.Label(self.master, image=self.bg_game, bg='black')
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        # crée de deck des cartes
        self.deck_images = []
        self.load_card_images()

        self.deck = self.create_deck()

        self.player_hand = []
        self.dealer_hand = []

        self.create_widgets()

    def load_card_images(self):
        for filename in os.listdir('cards'):
            if (filename.endswith(".png")):
                image = tk.PhotoImage(file=os.path.join('cards', filename)).subsample(3, 3)
                self.deck_images.append(image)

    def create_deck(self):
        # deck = [('2', 2), ('3', 3), ('4', 4), ('5', 5), ('6', 6), ('7', 7), ('8', 8), ('9', 9), ('10', 10), ('Valet', 10),('Dame', 10), ('Roi', 10), ('As', 11)] * 4
        deck = [('2', 2, 1), ('3', 3, 1), ('4', 4, 1), ('5', 5, 1), ('6', 6, 1), ('7', 7, 1), ('8', 8, 1), ('9', 9, 1), ('10', 10, 1), ('Valet', 10, 1), ('Dame', 10, 1), ('Roi', 10, 1), ('As', 11, 1)]
        deck += [('2', 2, 2), ('3', 3, 2), ('4', 4, 2), ('5', 5, 2), ('6', 6, 2), ('7', 7, 2), ('8', 8, 2), ('9', 9, 2), ('10', 10, 2), ('Valet', 10, 2), ('Dame', 10, 2), ('Roi', 10, 2), ('As', 11, 2)]
        deck += [('2', 2, 3), ('3', 3, 3), ('4', 4, 3), ('5', 5, 3), ('6', 6, 3), ('7', 7, 3), ('8', 8, 3), ('9', 9, 3), ('10', 10, 3), ('Valet', 10, 3), ('Dame', 10, 3), ('Roi', 10, 3), ('As', 11, 3)]
        deck += [('2', 2, 4), ('3', 3, 4), ('4', 4, 4), ('5', 5, 4), ('6', 6, 4), ('7', 7, 4), ('8', 8, 4), ('9', 9, 4), ('10', 10, 4), ('Valet', 10, 4), ('Dame', 10, 4), ('Roi', 10, 4), ('As', 11, 4)]
        random.shuffle(deck)
        return deck

    def deal_card(self):
        return self.deck.pop()

    def deal_initial_cards(self):
        self.player_hand = [self.deal_card(), self.deal_card()]
        self.dealer_hand = [self.deal_card(), self.deal_card()]

    def calculate_hand_value(self, hand):
        value = sum(card[1] for card in hand)
        num_aces = sum(1 for card in hand if card[0] == 'As')
        while value > 21 and num_aces:
            value -= 10
            num_aces -= 1
        return value

    def hit(self):
        self.player_hand.append(self.deal_card())
        self.update_player_hand()
        player_score = self.calculate_hand_value(self.player_hand)
        self.player_score_label.config(text=f"Score du Joueur : {player_score}")
        if player_score > 21:
            self.outcome_label.config(text="Le joueur dépasse 21! La banque gagne.")
            self.stand()
        #on ne peut plus miser apres avoir tiré une carte
#        self.bet_button.config(state="disabled")

    def stand(self):
        player_score = self.calculate_hand_value(self.player_hand)
        dealer_score = self.calculate_hand_value(self.dealer_hand)
        while dealer_score < 17 and player_score <= 21:
            self.dealer_hand.append(self.deal_card())
            dealer_score = self.calculate_hand_value(self.dealer_hand)

        self.update_dealer_hand()
        self.dealer_score_label.config(text=f"Score de la Banque : {dealer_score}")
        #fin de partie le joueur ne peu plus piocher
        self.hit_button.config(state="disabled")     #nouveau
        self.stand_button.config(state="disabled")
        
        if dealer_score > 21 or (player_score > dealer_score and  21 >= player_score):
            self.outcome_label.config(text="Le joueur gagne!")
        elif dealer_score > player_score or player_score > 21:
            self.outcome_label.config(text="La banque gagne!")
        else:
            self.outcome_label.config(text="Égalité!")
        #fin de partie le joueur ne peu plus piocher 
        self.hit_button.config(state="disabled")      #nouveau
        self.stand_button.config(state="disabled")
        #on ne peut plus miser apres avoir tiré une carte        
#        self.bet_button.config(state="disabled")

    def replay(self): #nouveau
        self.master.destroy()
        root = tk.Tk()
        app = BlackjackApp(root)
        root.mainloop()
    
    def mise(self): ####################################
        self.mise = tk.Toplevel(self.master)
        simpledialog.askinteger('mise','Combien souhaite tu miser ?', minvalue=0, maxvalue=100,parent=self.master)
        entry=tk.Entry(self.master)
        resultat=int(entry.get())
        #on ne peut pas miser plusieur fois      
        self.bet_button.config(state="disabled")
        return resultat
    
#    def cagnotte(self): ###############################nouveau
#        cagnotte=100
#        cagnotte-= self.mise()
#        if self.outcome_label.config(text="Le joueur gagne!"):
#            cagnotte+= self.mise() * 2
#        elif self.outcome_label.config(text="La banque gagne!"):
#            None
#        else:
#            cagnotte+=self.mise()
#        return cagnotte



    def create_widgets(self):
        style = ttk.Style()
        style.configure('TButton', font=('Arial', 12), padding=5)
        style.configure('TLabel', font=('Arial', 12), padding=5)

        self.dealer_frame = tk.Frame(self.master, background="grey")
        self.dealer_frame.pack(side=tk.TOP, pady=10, ipady=10)

        self.dealer_score_label = ttk.Label(self.dealer_frame, text="", background='gray', foreground='white')
        self.dealer_score_label.pack()

        self.player_frame = tk.Frame(self.master, background="grey")
        self.player_frame.pack(side=tk.TOP, pady=10, ipady=10)

        self.player_score_label = ttk.Label(self.player_frame, text="", background='gray', foreground='white')
        self.player_score_label.pack()
        self.player_cagnotte_label = ttk.Label(self.player_frame, text="", background='gray')
        self.player_cagnotte_label.pack()

        self.player_card_labels = []
        self.update_player_hand()

        

        self.dealer_card_labels = []
        self.update_dealer_hand(hidden=True)

        self.button_frame = tk.Frame(self.master, background="grey")
        self.button_frame.pack(side=tk.TOP, pady=10, ipady=10)

        self.hit_button = ttk.Button(self.button_frame, text="Piocher",style= 'succes.TButton', command=self.hit)
        self.hit_button.grid(row=0, column=0, padx=10)

        self.stand_button = ttk.Button(self.button_frame, text="Rester",  command=self.stand)
        self.stand_button.grid(row=0,column=2, padx=10)

        self.quit_button = ttk.Button(self.button_frame, text="Quitter",  command=self.master.destroy)    #nouveau
        self.quit_button.grid(row=3, column=1, padx=10)

        self.replay_button = ttk.Button(self.button_frame, text="rejouer",  command= self.replay)    ###################nouveau
        self.replay_button.grid(row=2, column=1, padx=0, pady=10)

        self.bet_button = ttk.Button(self.button_frame, text="miser",  command= self.mise)    #####################nouveau
        self.bet_button.grid(row=1, column=1, padx=0, pady=10)

        self.outcome_label = ttk.Label(self.master, text="", background='gray', foreground='white') # a quoi y sert
        self.outcome_label.pack()

        self.deal_initial_cards()

        player_score = self.calculate_hand_value(self.player_hand)
#        cagnotte_player = self.cagnotte(self.mise) ############################nouveau
        dealer_score = self.dealer_hand[0][1]  # Montrer seulement la première carte du croupier
        self.player_score_label.config(text=f"Score du Joueur : {player_score}")
#        self.player_cagnotte_label.config(text=f"vous avez: {cagnotte_player}€")###################################
        self.dealer_score_label.config(text="Score de la Banque : ?")

    def update_player_hand(self):
        for label in self.player_card_labels:
            label.destroy()
        self.player_card_labels.clear()
        print(self.player_hand)
        for card in self.player_hand:
            if (len(card[0]) <= 2 and card[0] != 'As'):
                image_index = (card[1] - 2)*4 + (card[2]-1)
            elif card[0] == 'Valet':
                 image_index = 9*4 + (card[2]-1)
            elif card[0]=='Dame':
                 image_index = 10*4 + (card[2]-1)
            elif card[0]=='Roi':
                 image_index = 11*4 + (card[2]-1)
            else:
                 image_index = 12*4 + (card[2]-1)
            print(image_index)
            card_image = self.deck_images[image_index]
            label = tk.Label(self.player_frame, image=card_image)
            label.image = card_image
            label.pack(side=tk.LEFT)
            self.player_card_labels.append(label)

    def update_dealer_hand(self, hidden=False):
        for label in self.dealer_card_labels:
            label.destroy()
        self.dealer_card_labels.clear()

        if hidden:
            image_index = 52
            card_image = self.deck_images[image_index]
            label = tk.Label(self.dealer_frame, image=card_image)
            label.image = card_image
            label.pack(side=tk.LEFT)
            self.dealer_card_labels.append(label)
            card_image = self.deck_images[image_index]
            label = tk.Label(self.dealer_frame, image=card_image)
            label.image = card_image
            label.pack(side=tk.RIGHT)
            self.dealer_card_labels.append(label)
        else:
            for card in self.dealer_hand:
                if (len(card[0]) <= 2 and card[0] != 'As'):
                    image_index = (card[1] - 2)*4 + (card[2]-1)
                elif card[0] == 'Valet':
                    image_index = 9*4 + (card[2]-1)
                elif card[0] == 'Dame':
                    image_index = 10*4 + (card[2]-1)
                elif card[0] == 'Roi':
                    image_index = 11*4 + (card[2]-1)
                else:
                    image_index = 12*4 + (card[2]-1)
                card_image = self.deck_images[image_index]
                label = tk.Label(self.dealer_frame, image=card_image)
                label.image = card_image
                label.pack(side=tk.LEFT)
                self.dealer_card_labels.append(label)

    def deal_initial_cards(self):
        self.deck = self.create_deck()  # Mélanger le jeu de cartes
        self.player_hand = [self.deal_card(), self.deal_card()]
        self.dealer_hand = [self.deal_card(), self.deal_card()]
        self.update_player_hand()
        self.update_dealer_hand(hidden=True)

    def sauvegarde_score(): #nouveau
        fichier_score=open("score.txt","a",encording="utf8")


class Blackjackinterface:
    def __init__(self):
        # Create the main window
        self.window = tk.Tk()
        self.window.title("Blackjack Welcome Page")
        self.window.attributes('-fullscreen', 1)
        self.window.title("Black Jack")
        self.bg_image = tk.PhotoImage(file="fond_ecrant_avec_titre.png")

        # Create a label with the background image
        self.bg_label = tk.Label(self.window, image=self.bg_image, bg='black')
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        # bouton_tirer_carte= tk.Button(ecr, text="Carte!",)       
        self.quitter_boutton = tk.Button(self.window, text="quitter", bg="gray", fg="black",activebackground="black",activeforeground='gray',relief=tk.FLAT, command=self.quitter)
        self.start_button = tk.Button(self.window, text="Start Game", bg="gray", fg='black',activebackground="black",activeforeground='gray',relief=tk.FLAT, command=self.start_game)
        self.rules_button = tk.Button(self.window, text="Rules", bg='gray', fg='black',activebackground="black",activeforeground='gray',relief=tk.FLAT, command=self.show_rules)
        self.start_duo = tk.Button(self.window, text="mode dificile", bg='gray', fg='black',activebackground="black",activeforeground='gray',relief=tk.FLAT,)
   
        #position des bouton 
        self.start_button.place(x=491,y=280)
        self.start_duo.place(x=982,y=280)
        self.rules_button.place(x=760,y=450)
        self.quitter_boutton.place(x=760,y=550)

    def quitter(self):
        #self.master.destroy() marche pas
        self.window.destroy()
    def start_game(self):
       
        self.window.destroy() 


    def show_rules(self):
        self.rules_window = tk.Toplevel(self.window)
        messagebox.showinfo("Règle du BlackJack", "Le Blackjack est un jeu de cartes où le joueur vise à obtenir un score aussi proche que possible de 21 sans le dépasser. Le jeu se joue avec un ou plusieurs jeux de 52 cartes. La valeur de chaque carte est la suivante :\n\n- 2 à 10 : valeur faciale\n- Valet, Dame, Roi : 10\n- As : 1 ou 11 (au choix du joueur)\n\nLe jeu commence avec le joueur et le croupier recevant chacun deux cartes. Les cartes du joueur sont distribuées face visible, tandis qu'une des cartes du croupier est distribuée face cachée. Le joueur a alors la possibilité de 'tirer' (prendre une autre carte) ou de 'rester' (garder son score actuel). Si le score du joueur dépasse 21, il 'explose' et perd la partie. Si le score du joueur est inférieur ou égal à 21, le croupier joue ensuite sa main. Le croupier doit tirer s'il a un score inférieur à 17, et rester s'il a un score de 17 ou plus. Si le croupier 'explose', le joueur gagne. Si le score du croupier est plus proche de 21 que celui du joueur, le joueur perd. Si le score du joueur est plus proche de 2")


class Blackjackdifficile:
    def __init__(self, master):
        self.master = master
        self.master.title("Blackjack")
        self.master.attributes("-fullscreen",1)
        self.bg_game = tk.PhotoImage(file="fond_ecran_accueil_blackjackBlanc.png")
        self.bg_label = tk.Label(self.master, image=self.bg_game, bg='black')
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        # crée de deck des cartes
        self.deck_images = []
        self.load_card_images()

        self.deck = self.create_deck()

        self.player_hand = []
        self.dealer_hand = []

        self.create_widgets()

    def load_card_images(self):
        for filename in os.listdir('cards'):
            if (filename.endswith(".png")):
                image = tk.PhotoImage(file=os.path.join('cards', filename)).subsample(3, 3)
                self.deck_images.append(image)

    def create_deck(self):
        # deck = [('2', 2), ('3', 3), ('4', 4), ('5', 5), ('6', 6), ('7', 7), ('8', 8), ('9', 9), ('10', 10), ('Valet', 10),('Dame', 10), ('Roi', 10), ('As', 11)] * 4
        deck = [('2', 2, 1), ('3', 3, 1), ('4', 4, 1), ('5', 5, 1), ('6', 6, 1), ('7', 7, 1), ('8', 8, 1), ('9', 9, 1), ('10', 10, 1), ('Valet', 10, 1), ('Dame', 10, 1), ('Roi', 10, 1), ('As', 11, 1)]
        deck += [('2', 2, 2), ('3', 3, 2), ('4', 4, 2), ('5', 5, 2), ('6', 6, 2), ('7', 7, 2), ('8', 8, 2), ('9', 9, 2), ('10', 10, 2), ('Valet', 10, 2), ('Dame', 10, 2), ('Roi', 10, 2), ('As', 11, 2)]
        deck += [('2', 2, 3), ('3', 3, 3), ('4', 4, 3), ('5', 5, 3), ('6', 6, 3), ('7', 7, 3), ('8', 8, 3), ('9', 9, 3), ('10', 10, 3), ('Valet', 10, 3), ('Dame', 10, 3), ('Roi', 10, 3), ('As', 11, 3)]
        deck += [('2', 2, 4), ('3', 3, 4), ('4', 4, 4), ('5', 5, 4), ('6', 6, 4), ('7', 7, 4), ('8', 8, 4), ('9', 9, 4), ('10', 10, 4), ('Valet', 10, 4), ('Dame', 10, 4), ('Roi', 10, 4), ('As', 11, 4)]
        random.shuffle(deck)
        return deck

    def deal_card(self):
        return self.deck.pop()

    def deal_initial_cards(self):
        self.player_hand = [self.deal_card(), self.deal_card()]
        self.dealer_hand = [self.deal_card(), self.deal_card()]

    def calculate_hand_value(self, hand):
        value = sum(card[1] for card in hand)
        num_aces = sum(1 for card in hand if card[0] == 'As')
        while value > 21 and num_aces:
            value -= 10
            num_aces -= 1
        return value

    def hit(self):
        self.player_hand.append(self.deal_card())
        self.update_player_hand()
        player_score = self.calculate_hand_value(self.player_hand)
        self.player_score_label.config(text=f"Score du Joueur : {player_score}")
        if player_score > 21:
            self.outcome_label.config(text="Le joueur dépasse 21! La banque gagne.")
            self.stand()
        #on ne peut plus miser apres avoir tiré une carte
#        self.bet_button.config(state="disabled")

    def stand(self):
        player_score = self.calculate_hand_value(self.player_hand)
        dealer_score = self.calculate_hand_value(self.dealer_hand)
        while dealer_score < player_score and player_score <= 21:
            self.dealer_hand.append(self.deal_card())
            dealer_score = self.calculate_hand_value(self.dealer_hand)

        self.update_dealer_hand()
        self.dealer_score_label.config(text=f"Score de la Banque : {dealer_score}")
        #fin de partie le joueur ne peu plus piocher
        self.hit_button.config(state="disabled")     #nouveau
        self.stand_button.config(state="disabled")
        
        if dealer_score > 21 or (player_score > dealer_score and  21 >= player_score):
            self.outcome_label.config(text="Le joueur gagne!")
        elif dealer_score > player_score or player_score > 21:
            self.outcome_label.config(text="La banque gagne!")
        else:
            self.outcome_label.config(text="Égalité!")
        #fin de partie le joueur ne peu plus piocher 
        self.hit_button.config(state="disabled")      #nouveau
        self.stand_button.config(state="disabled")
        #on ne peut plus miser apres avoir tiré une carte        
#        self.bet_button.config(state="disabled")

    def replay(self): #nouveau
        self.master.destroy()
        root = tk.Tk()
        app = BlackjackApp(root)
        root.mainloop()
    
    def mise(self): ####################################
        self.mise = tk.Toplevel(self.master)
        simpledialog.askinteger('mise','Combien souhaite tu miser ?', minvalue=0, maxvalue=100,parent=self.master)
        entry=tk.Entry(self.master)
        resultat=int(entry.get())
        #on ne peut pas miser plusieur fois      
        self.bet_button.config(state="disabled")
        return resultat
    
#    def cagnotte(self): ###############################nouveau
#        cagnotte=100
#        cagnotte-= self.mise()
#        if self.outcome_label.config(text="Le joueur gagne!"):
#            cagnotte+= self.mise() * 2
#        elif self.outcome_label.config(text="La banque gagne!"):
#            None
#        else:
#            cagnotte+=self.mise()
#        return cagnotte



    def create_widgets(self):
        style = ttk.Style()
        style.configure('TButton', font=('Arial', 12), padding=5)
        style.configure('TLabel', font=('Arial', 12), padding=5)

        self.dealer_frame = tk.Frame(self.master, background="grey")
        self.dealer_frame.pack(side=tk.TOP, pady=10, ipady=10)

        self.dealer_score_label = ttk.Label(self.dealer_frame, text="", background='gray', foreground='white')
        self.dealer_score_label.pack()

        self.player_frame = tk.Frame(self.master, background="grey")
        self.player_frame.pack(side=tk.TOP, pady=10, ipady=10)

        self.player_score_label = ttk.Label(self.player_frame, text="", background='gray', foreground='white')
        self.player_score_label.pack()
        self.player_cagnotte_label = ttk.Label(self.player_frame, text="", background='gray')
        self.player_cagnotte_label.pack()

        self.player_card_labels = []
        self.update_player_hand()

        

        self.dealer_card_labels = []
        self.update_dealer_hand(hidden=True)

        self.button_frame = tk.Frame(self.master, background="grey")
        self.button_frame.pack(side=tk.TOP, pady=10, ipady=10)

        self.hit_button = ttk.Button(self.button_frame, text="Piocher",style= 'succes.TButton', command=self.hit)
        self.hit_button.grid(row=0, column=0, padx=10)

        self.stand_button = ttk.Button(self.button_frame, text="Rester",  command=self.stand)
        self.stand_button.grid(row=0,column=2, padx=10)

        self.quit_button = ttk.Button(self.button_frame, text="Quitter",  command=self.master.destroy)    #nouveau
        self.quit_button.grid(row=3, column=1, padx=10)

        self.replay_button = ttk.Button(self.button_frame, text="rejouer",  command= self.replay)    ###################nouveau
        self.replay_button.grid(row=2, column=1, padx=0, pady=10)

        self.bet_button = ttk.Button(self.button_frame, text="miser",  command= self.mise)    #####################nouveau
        self.bet_button.grid(row=1, column=1, padx=0, pady=10)

        self.outcome_label = ttk.Label(self.master, text="", background='gray', foreground='white') # a quoi y sert
        self.outcome_label.pack()

        self.deal_initial_cards()

        player_score = self.calculate_hand_value(self.player_hand)
#        cagnotte_player = self.cagnotte(self.mise) ############################nouveau
        dealer_score = self.dealer_hand[0][1]  # Montrer seulement la première carte du croupier
        self.player_score_label.config(text=f"Score du Joueur : {player_score}")
#        self.player_cagnotte_label.config(text=f"vous avez: {cagnotte_player}€")###################################
        self.dealer_score_label.config(text="Score de la Banque : ?")

    def update_player_hand(self):
        for label in self.player_card_labels:
            label.destroy()
        self.player_card_labels.clear()
        print(self.player_hand)
        for card in self.player_hand:
            if (len(card[0]) <= 2 and card[0] != 'As'):
                image_index = (card[1] - 2)*4 + (card[2]-1)
            elif card[0] == 'Valet':
                 image_index = 9*4 + (card[2]-1)
            elif card[0]=='Dame':
                 image_index = 10*4 + (card[2]-1)
            elif card[0]=='Roi':
                 image_index = 11*4 + (card[2]-1)
            else:
                 image_index = 12*4 + (card[2]-1)
            print(image_index)
            card_image = self.deck_images[image_index]
            label = tk.Label(self.player_frame, image=card_image)
            label.image = card_image
            label.pack(side=tk.LEFT)
            self.player_card_labels.append(label)

    def update_dealer_hand(self, hidden=False):
        for label in self.dealer_card_labels:
            label.destroy()
        self.dealer_card_labels.clear()

        if hidden:
            image_index = 52
            card_image = self.deck_images[image_index]
            label = tk.Label(self.dealer_frame, image=card_image)
            label.image = card_image
            label.pack(anchor='center')
            self.dealer_card_labels.append(label)
        else:
            for card in self.dealer_hand:
                if (len(card[0]) <= 2 and card[0] != 'As'):
                    image_index = (card[1] - 2)*4 + (card[2]-1)
                elif card[0] == 'Valet':
                    image_index = 9*4 + (card[2]-1)
                elif card[0] == 'Dame':
                    image_index = 10*4 + (card[2]-1)
                elif card[0] == 'Roi':
                    image_index = 11*4 + (card[2]-1)
                else:
                    image_index = 12*4 + (card[2]-1)
                card_image = self.deck_images[image_index]
                label = tk.Label(self.dealer_frame, image=card_image)
                label.image = card_image
                label.pack(side=tk.LEFT)
                self.dealer_card_labels.append(label)

    def deal_initial_cards(self):
        self.deck = self.create_deck()  # Mélanger le jeu de cartes
        self.player_hand = [self.deal_card(), self.deal_card()]
        self.dealer_hand = [self.deal_card(), self.deal_card()]
        self.update_player_hand()
        self.update_dealer_hand(hidden=True)

    def sauvegarde_score(): #nouveau
        fichier_score=open("score.txt","a",encording="utf8")

# Create the BlackjackApp object
app = Blackjackinterface()

# Start the Tkinter event loop

app.window.mainloop()
root = tk.Tk()
app = BlackjackApp(root)
root.mainloop()


# Create the BlackjackApp object
app2 = Blackjackinterface()

# Start the Tkinter event loop
app2.window.mainloop()
root2 = tk.Tk()
app2 = Blackjackdifficile(root2)
root2.mainloop()

class RulesInterface:
    def __init__(self, master):
        self.master = master

        self.label = ttk.Label(self.master, text="Blackjack Rules", font=("Arial", 24))
        self.label.pack(pady=20)

        self.rules_text = ttk.Label(self.master, text="Le Blackjack est un jeu de cartes où le joueur vise à obtenir un score aussi proche que possible de 21 sans le dépasser. Le jeu se joue avec un ou plusieurs jeux de 52 cartes. La valeur de chaque carte est la suivante :\n\n- 2 à 10 : valeur faciale\n- Valet, Dame, Roi : 10\n- As : 1 ou 11 (au choix du joueur)\n\nLe jeu commence avec le joueur et le croupier recevant chacun deux cartes. Les cartes du joueur sont distribuées face visible, tandis qu'une des cartes du croupier est distribuée face cachée. Le joueur a alors la possibilité de 'tirer' (prendre une autre carte) ou de 'rester' (garder son score actuel). Si le score du joueur dépasse 21, il 'explose' et perd la partie. Si le score du joueur est inférieur ou égal à 21, le croupier joue ensuite sa main, en suivant un ensemble de règles. Le croupier doit tirer s'il a un score inférieur à 17, et rester s'il a un score de 17 ou plus. Si le croupier 'explose', le joueur gagne. Si le score du croupier est plus proche de 21 que celui du joueur, le joueur perd. Si le score du joueur est plus proche de 2", wraplength=350)
        self.rules_text.pack(pady=20)

        self.back_button = ttk.Button(self.master, text="Back", command=self.back)
        self.back_button.pack(pady=20)

    def back(self):
        self.master.destroy()