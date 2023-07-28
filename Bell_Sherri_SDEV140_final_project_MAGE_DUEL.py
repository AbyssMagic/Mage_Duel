import tkinter as tk
import random
#A Mage Duel a simple tkinter based game where two wizards duel for the fate of the Valley of the Moonrise
class GUIDesign:
    #class for managing the GUI design how the end user interacts 
    def __init__(self, root):
        self.root = root
        self.current_canvas = None
        self.create_canvas_1()
    #Create the first screen called canvas_1 challenging Rubeius to a duel    
    def create_canvas_1(self):
        self.current_canvas = tk.Canvas(self.root, width=600, height=400, bg="purple")
        self.current_canvas.pack(fill="both", expand=True)

        self.current_canvas.create_text(300, 150, text="Stelius has challenged you to a duel!! Do you accept his challenge?",
                                        font=("Helvetica", 15), fill="white", anchor="center")

        button1 = tk.Button(self.root, text="Accept", command=self.create_canvas_2)
        button1.place(relx=0.5, rely=0.8, anchor="center")
    #create the second screen called canvas_2 Duel has been accepted and now they cast spells 
    def create_canvas_2(self):
        self.current_canvas.destroy()
        self.current_canvas = tk.Canvas(self.root, width=600, height=400, bg="green")
        self.current_canvas.pack(fill="both", expand=True)

        self.current_canvas.create_text(300, 150, text="Who will win, who will be defeated?",
                                        font=("Helvetica", 20), fill="white", anchor="center")

        button1 = tk.Button(self.root, text="roll to cast spell", command=self.create_canvas_3)
        button1.place(relx=0.5, rely=0.8, anchor="center")
    #create the third screen called canvas_3 and will print the outcome of the duel 
    def create_canvas_3(self):
        self.current_canvas.destroy()
        self.current_canvas = tk.Canvas(self.root, width=600, height=400, bg="blue")
        self.current_canvas.pack(fill="both", expand=True)

        self.current_canvas.create_text(300, 100, text="The Duel winner is:",
                                        font=("Helvetica", 30), fill="white", anchor="center")

        # Generate random numbers for Reubius and Stelius
        reubius_number = random.randint(1, 20)
        stelius_number = random.randint(1, 20)

        # Determine the winner
        if reubius_number > stelius_number:
            winner = "Reubius"
        elif reubius_number < stelius_number:
            winner = "Stelius"
        else:
            winner = "It's a tie!"

        # Display the winner of the Duel
        self.current_canvas.create_text(300, 200, text=f"Reubius: {reubius_number}", font=("Helvetica", 20), fill="white", anchor="center")
        self.current_canvas.create_text(300, 250, text=f"Stelius: {stelius_number}", font=("Helvetica", 20), fill="white", anchor="center")
        self.current_canvas.create_text(300, 350, text=winner, font=("Helvetica", 50), fill="white", anchor="center")
#function to end the program and close tkinter with the escape button 
def end_program():
    root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Button Escape")

    game = GUIDesign(root)

    escape_button = tk.Button(root, text="Escape", command=end_program)
    escape_button.pack()

    root.mainloop()
