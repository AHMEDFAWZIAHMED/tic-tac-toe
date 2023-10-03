from tkinter import *
import time
import random

class play(Label):

    turn = 1
    board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    template1 = []
    template2 = []
    template_list = [0, 1, 2, 3, 4, 5, 6, 7, 8]

    def __init__(self):
        Label.__init__(self)
        self.ex = PhotoImage(file='png\\player1.png')
        self.winer_ex = PhotoImage(file='png\\player12.png')
        self.circle = PhotoImage(file='png\\player2.png')
        self.winer_circle = PhotoImage(file='png\\player22.png')
        self.user_choice = PhotoImage(file='png\\empty3.png')

        self.player1 = lambda:Label(image=self.ex)
        self.player1_win = lambda:Label(image=self.winer_ex)
        self.player2 = lambda:Label(image=self.circle)
        self.player2_win = lambda:Label(image=self.winer_circle)

        self.user_player()

    
    def user_player(self):

        def user_click0():
            if self.turn == 1:
                self.player1().place(x=22, y=22)
                self.board[0] = 1
                self.template1.append(0)
                self.turn = 2

                if len(self.template2) == 2:
                    del self.template2[0]

                for i, number in enumerate(self.template_list):
                    if [number] == self.template2:
                        del self.template_list[i]

                self.result()
        
        def user_click1():
            if self.turn == 1:
                self.player1().place(x=230, y=22)
                self.board[1] = 1
                self.template1.append(1)
                self.turn = 2

                if len(self.template2) == 2:
                    del self.template2[0]

                for i, number in enumerate(self.template_list):
                    if [number] == self.template2:
                        del self.template_list[i]

                self.result()

        def user_click2():
            if self.turn == 1:
                self.player1().place(x=438, y=22)
                self.board[2] = 1
                self.template1.append(2)
                self.turn = 2

                if len(self.template2) == 2:
                    del self.template2[0]

                for i, number in enumerate(self.template_list):
                    if [number] == self.template2:
                        del self.template_list[i]

                self.result()

        def user_click3():
            if self.turn == 1:
                self.player1().place(x=22, y=230)
                self.board[3] = 1
                self.template1.append(3)
                self.turn = 2

                if len(self.template2) == 2:
                    del self.template2[0]

                for i, number in enumerate(self.template_list):
                    if [number] == self.template2:
                        del self.template_list[i]

                self.result()

        def user_click4():
            if self.turn == 1:
                self.player1().place(x=230, y=230)
                self.board[4] = 1
                self.template1.append(4)
                self.turn = 2

                if len(self.template2) == 2:
                    del self.template2[0]

                for i, number in enumerate(self.template_list):
                    if [number] == self.template2:
                        del self.template_list[i]

                self.result()

        def user_click5():
            if self.turn == 1:
                self.player1().place(x=438, y=230)
                self.board[5] = 1
                self.template1.append(5)
                self.turn = 2

                if len(self.template2) == 2:
                    del self.template2[0]

                for i, number in enumerate(self.template_list):
                    if [number] == self.template2:
                        del self.template_list[i]

                self.result()

        def user_click6():
            if self.turn == 1:
                self.player1().place(x=22, y=438)
                self.board[6] = 1
                self.template1.append(6)
                self.turn = 2

                if len(self.template2) == 2:
                    del self.template2[0]

                for i, number in enumerate(self.template_list):
                    if [number] == self.template2:
                        del self.template_list[i]

                self.result()

        def user_click7():
            if self.turn == 1:
                self.player1().place(x=230, y=438)
                self.board[7] = 1
                self.template1.append(7)
                self.turn = 2

                if len(self.template2) == 2:
                    del self.template2[0]

                for i, number in enumerate(self.template_list):
                    if [number] == self.template2:
                        del self.template_list[i]

                self.result()

        def user_click8():
            if self.turn == 1:
                self.player1().place(x=438, y=438)
                self.board[8] = 1
                self.template1.append(8)
                self.turn = 2

                if len(self.template2) == 2:
                    del self.template2[0]

                for i, number in enumerate(self.template_list):
                    if [number] == self.template2:
                        del self.template_list[i]

                self.result()

        choice_button1 = Button(image=self.user_choice, command=user_click0, borderwidth=0)
        choice_button1.place(x=22, y=22)

        choice_button2 = Button(image=self.user_choice, command=user_click1, borderwidth=0)
        choice_button2.place(x=230, y=22)

        choice_button3 = Button(image=self.user_choice, command=user_click2, borderwidth=0)
        choice_button3.place(x=438, y=22)

        choice_button4 = Button(image=self.user_choice, command=user_click3, borderwidth=0)
        choice_button4.place(x=22, y=230)

        choice_button5 = Button(image=self.user_choice, command=user_click4, borderwidth=0)
        choice_button5.place(x=230, y=230)

        choice_button6 = Button(image=self.user_choice, command=user_click5, borderwidth=0)
        choice_button6.place(x=438, y=230)

        choice_button7 = Button(image=self.user_choice, command=user_click6, borderwidth=0)
        choice_button7.place(x=22, y=438)

        choice_button8 = Button(image=self.user_choice, command=user_click7, borderwidth=0)
        choice_button8.place(x=230, y=438)

        choice_button9 = Button(image=self.user_choice, command=user_click8, borderwidth=0)
        choice_button9.place(x=438, y=438)

    
    def computer_player(self):

        if self.turn == 2:

            if len(self.template_list) > 0:
                computer_choice = random.choice(self.template_list)
                if computer_choice == 0:
                    self.player2().place(x=22, y=22)
                    self.template2.append(0)
                    self.board[0] = 2
                    self.turn = 1
                if computer_choice == 1:
                    self.player2().place(x=230, y=22)
                    self.template2.append(1)
                    self.board[1] = 2
                    self.turn = 1
                if computer_choice == 2:
                    self.player2().place(x=438, y=22)
                    self.template2.append(2)
                    self.board[2] = 2
                    self.turn = 1
                if computer_choice == 3:
                    self.player2().place(x=22, y=230)
                    self.template2.append(3)
                    self.board[3] = 2
                    self.turn = 1
                if computer_choice == 4:
                    self.player2().place(x=230, y=230)
                    self.template2.append(4)
                    self.board[4] = 2
                    self.turn = 1
                if computer_choice == 5:
                    self.player2().place(x=438, y=230)
                    self.template2.append(5)
                    self.board[5] = 2
                    self.turn = 1
                if computer_choice == 6:
                    self.player2().place(x=22, y=438)
                    self.template2.append(6)
                    self.board[6] = 2
                    self.turn = 1
                if computer_choice == 7:
                    self.player2().place(x=230, y=438)
                    self.template2.append(7)
                    self.board[7] = 2
                    self.turn = 1
                if computer_choice == 8:
                    self.player2().place(x=438, y=438)
                    self.template2.append(8)
                    self.board[8] = 2
                    self.turn = 1

                self.result()


    def result(self):

        if self.turn == 1:
            if self.board[0:3] == [2, 2, 2]:
                self.player2_win().place(x=22, y=22)
                self.player2_win().place(x=230, y=22)
                self.player2_win().place(x=438, y=22)
                self.turn = 0
                self.after(7000, self.restart)
            if self.board[3:6] == [2, 2, 2]:
                self.player2_win().place(x=22, y=230)
                self.player2_win().place(x=230, y=230)
                self.player2_win().place(x=438, y=230)
                self.turn = 0
                self.after(7000, self.restart)
            if self.board[6:9] == [2, 2, 2]:
                self.player2_win().place(x=22, y=438)
                self.player2_win().place(x=230, y=438)
                self.player2_win().place(x=438, y=438)
                self.turn = 0
                self.after(7000, self.restart)
            if self.board[0::3] == [2, 2, 2]:
                self.player2_win().place(x=22, y=22)
                self.player2_win().place(x=22, y=230)
                self.player2_win().place(x=22, y=438)
                self.turn = 0
                self.after(7000, self.restart)
            if self.board[1::3] == [2, 2, 2]:
                self.player2_win().place(x=230, y=22)
                self.player2_win().place(x=230, y=230)
                self.player2_win().place(x=230, y=438)
                self.turn = 0
                self.after(7000, self.restart)
            if self.board[2::3] == [2, 2, 2]:
                self.player2_win().place(x=438, y=22)
                self.player2_win().place(x=438, y=230)
                self.player2_win().place(x=438, y=438)
                self.turn = 0
                self.after(7000, self.restart)
            if self.board[0::4] == [2, 2, 2]:
                self.player2_win().place(x=22, y=22)
                self.player2_win().place(x=230, y=230)
                self.player2_win().place(x=438, y=438)
                self.turn = 0
                self.after(7000, self.restart)
            if self.board[2:7:2] == [2, 2, 2]:
                self.player2_win().place(x=438, y=22)
                self.player2_win().place(x=230, y=230)
                self.player2_win().place(x=22, y=438)
                self.turn = 0
                self.after(7000, self.restart)
            elif len(self.template_list) == 0:
                self.after(7000, self.restart)

        if self.turn == 2:

            if len(self.template1) == 2:
                del self.template1[0]
            
            for i, number in enumerate(self.template_list):
                if [number] == self.template1:
                    del self.template_list[i]
                    
            if self.board[0:3] == [1, 1, 1]:
                self.player1_win().place(x=22, y=22)
                self.player1_win().place(x=230, y=22)
                self.player1_win().place(x=438, y=22)
                self.turn = 0
                self.after(7000, self.restart)
            if self.board[3:6] == [1, 1, 1]:
                self.player1_win().place(x=22, y=230)
                self.player1_win().place(x=230, y=230)
                self.player1_win().place(x=438, y=230)
                self.turn = 0
                self.after(7000, self.restart)
            if self.board[6:9] == [1, 1, 1]:
                self.player1_win().place(x=22, y=438)
                self.player1_win().place(x=230, y=438)
                self.player1_win().place(x=438, y=438)
                self.turn = 0
                self.after(7000, self.restart)
            if self.board[0::3] == [1, 1, 1]:
                self.player1_win().place(x=22, y=22)
                self.player1_win().place(x=22, y=230)
                self.player1_win().place(x=22, y=438)
                self.turn = 0
                self.after(7000, self.restart)
            if self.board[1::3] == [1, 1, 1]:
                self.player1_win().place(x=230, y=22)
                self.player1_win().place(x=230, y=230)
                self.player1_win().place(x=230, y=438)
                self.turn = 0
                self.after(7000, self.restart)
            if self.board[2::3] == [1, 1, 1]:
                self.player1_win().place(x=438, y=22)
                self.player1_win().place(x=438, y=230)
                self.player1_win().place(x=438, y=438)
                self.turn = 0
                self.after(7000, self.restart)
            if self.board[0::4] == [1, 1, 1]:
                self.player1_win().place(x=22, y=22)
                self.player1_win().place(x=230, y=230)
                self.player1_win().place(x=438, y=438)
                self.turn = 0
                self.after(7000, self.restart)
            if self.board[2:7:2] == [1, 1, 1]:
                self.player1_win().place(x=438, y=22)
                self.player1_win().place(x=230, y=230)
                self.player1_win().place(x=22, y=438)
                self.turn = 0
                self.after(7000, self.restart)
            elif len(self.template_list) == 0:
                self.after(7000, self.restart)

            self.after(500, self.computer_player)


    def restart(self):

        self.turn = 1
        self.board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.template1 = []
        self.template2 = []
        self.template_list = [0, 1, 2, 3, 4, 5, 6, 7, 8]

        self.user_player()


class board_frame(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.template_label = PhotoImage(file='png\\tic-tac-toe3.png')
        self.board_label = Label(image=self.template_label)
        self.board_label.place(x=0, y=0)


class game(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title('Tic-Tac-Toe')
        self.geometry("618x618")
        self.resizable(0, 0)
        
        self.boardFrame = board_frame()
        self.playing = play()
        

if __name__ == "__main__":
    root = game()
    root.mainloop()
