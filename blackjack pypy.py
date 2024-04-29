import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import random
import os

class BlackjackApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Blackjack")
        self.master.geometry("800x600")

        self.deck_images = []
        self.load_card_images()

        self.deck = self.create_deck()
        self.player_hand = []
        self.dealer_hand = []

        self.create_widgets()

    def load_card_images(self):
        for filename in os.listdir("cards"):
            image = tk.PhotoImage(file=os.path.join("cards", filename))
            self.deck_images.append(image)

    def create_deck(self):
        deck = [('2', 2), ('3', 3), ('4', 4), ('5', 5), ('6', 6), ('7', 7), ('8', 8), ('9', 9), ('10', 10), ('Valet', 10),
                ('Dame', 10), ('Roi', 10), ('As', 11)] * 4
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
        self.play_sound("draw_card.wav")
        self.player_hand.append(self.deal_card())
        self.update_player_hand()
        player_score = self.calculate_hand_value(self.player_hand)
        self.player_score_label.config(text=f"Score du Joueur : {player_score}")
        if player_score > 21:
            self.outcome_label.config(text="Le joueur dépasse 21! La banque gagne.")
            self.stand()

    def stand(self):
        player_score = self.calculate_hand_value(self.player_hand)
        dealer_score = self.calculate_hand_value(self.dealer_hand)
        while dealer_score < 17:
            self.dealer_hand.append(self.deal_card())
            dealer_score = self.calculate_hand_value(self.dealer_hand)

        self.update_dealer_hand()
        self.dealer_score_label.config(text=f"Score de la Banque : {dealer_score}")

        if dealer_score > 21 or player_score > dealer_score:
            self.outcome_label.config(text="Le joueur gagne!")
        elif dealer_score > player_score:
            self.outcome_label.config(text="La banque gagne!")
        else:
            self.outcome_label.config(text="Égalité!")

    def create_widgets(self):
        style = ttk.Style()
        style.configure('TButton', font=('Arial', 12), padding=5)
        style.configure('TLabel', font=('Arial', 12), padding=5)

        self.player_frame = tk.Frame(self.master)
        self.player_frame.pack(side=tk.TOP, pady=10)

        self.player_score_label = ttk.Label(self.player_frame, text="")
        self.player_score_label.pack()

        self.player_card_labels = []
        self.update_player_hand()

        self.dealer_frame = tk.Frame(self.master)
        self.dealer_frame.pack(side=tk.TOP, pady=10)

        self.dealer_score_label = ttk.Label(self.dealer_frame, text="")
        self.dealer_score_label.pack()

        self.dealer_card_labels = []
        self.update_dealer_hand(hidden=True)

        self.button_frame = tk.Frame(self.master)
        self.button_frame.pack(side=tk.TOP, pady=10)

        self.hit_button = ttk.Button(self.button_frame, text="Piocher", command=self.hit)
        self.hit_button.pack(side=tk.LEFT, padx=10)

        self.stand_button = ttk.Button(self.button_frame, text="Rester", command=self.stand)
        self.stand_button.pack(side=tk.LEFT, padx=10)

        self.outcome_label = ttk.Label(self.master, text="")
        self.outcome_label.pack()

        self.deal_initial_cards()

        player_score = self.calculate_hand_value(self.player_hand)
        dealer_score = self.dealer_hand[0][1]  # Montrer seulement la première carte du croupier
        self.player_score_label.config(text=f"Score du Joueur : {player_score}")
        self.dealer_score_label.config(text="Score de la Banque : ?")

    def update_player_hand(self):
        for label in self.player_card_labels:
            label.destroy()
        self.player_card_labels.clear()

        for card in self.player_hand:
            image_index = (card[1] - 2) + (card[0] == 'As') * 13
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
        else:
            for card in self.dealer_hand:
                image_index = (card[1] - 2) + (card[0] == 'As') * 13
                card_image = self.deck_images[image_index]
                label = tk.Label(self.dealer_frame, image=card_image)
                label.image = card_image
                label.pack(side=tk.LEFT)
                self.dealer_card_labels.append(label)

    def play_sound(self, filename):
        try:
            if os.name == 'nt':
                import winsound
                winsound.PlaySound(filename, winsound.SND_FILENAME)
            else:
                import subprocess
                subprocess.Popen(["afplay", filename])
        except Exception as e:
            print(f"Erreur lors de la lecture du fichier audio : {e}")

    def deal_initial_cards(self):
        self.play_sound("shuffle_cards.wav")
        self.deck = self.create_deck()  # Mélanger le jeu de cartes
        self.player_hand = [self.deal_card(), self.deal_card()]
        self.dealer_hand = [self.deal_card(), self.deal_card()]
        self.update_player_hand()
        self.update_dealer_hand(hidden=True)

root = tk.Tk()
app = BlackjackApp(root)
root.mainloop()
