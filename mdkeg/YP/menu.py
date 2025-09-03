import tkinter as tk
root = None
class QuizApp:
    def __init__(self, window):
        self.window = window
        self.window.title("Что приготовить?")
        self.window["bg"] = "BlanchedAlmond"
        self.window.resizable(False, False)
        self.questions = [
            ("Что вы предпочитаете больше?", ["Соленое", "Острое",
                                              "Сладкое", "Горькое", "Кислое"]),
            ("Сколько вы готовы потратить на готовку?", ["до 30 минут",
                                                         "30-60 минут",
                                                         "от 1 часа и более"]),
            ("Вы уже готовили раньше? Как долго?", ["Нет, я новичок",
                                                    "Да, я уже давно готовлю",
                                                    "Когда-то готовил(а), но простые блюда"]),
        ]
        self.questionsindex = 0
        self.answers = []
        self.label = tk.Label(window, text=self.questions[self.questionsindex][0], bg="BlanchedAlmond",
                              font=("Bahnschrift SemiBold Condensed", 28), fg="grey17")
        self.label.pack(pady=20)
        self.buttons = []
        self.create_buttons()

    def create_buttons(self):
        for button in self.buttons:
            button.pack_forget()
        self.buttons = []
        for answer in self.questions[self.questionsindex][1]:
            button = tk.Button(self.window, text=answer,
                               command=lambda ans=answer: self.click_answer(ans),
                               bg="dark salmon", fg="grey17",
                               font=("Bahnschrift SemiBold Condensed", 24))
            button.pack(pady=5)
            self.buttons.append(button)

    def click_answer(self, answer):
        self.answers.append(answer)
        self.questionsindex += 1
        if self.questionsindex < len(self.questions):
            self.update_question()
        else:
            self.show_results()

    def update_question(self):
        self.label.config(text=self.questions[self.questionsindex][0])
        self.create_buttons()

    def show_results(self):
        self.label.pack_forget()
        for button in self.buttons:
            button.pack_forget()
        main_frame = tk.Frame(self.window, bg="BlanchedAlmond")
        main_frame.pack(fill=tk.BOTH, expand=True)
        text_frame = tk.Frame(main_frame, bg="PeachPuff", padx=20, pady=20)
        text_frame.pack(pady=20, fill=tk.X, padx=40)
        header_label = tk.Label(text_frame, text="Ваши результаты:",
                                font=("Bahnschrift SemiBold Condensed", 20),
                                bg="PeachPuff", fg="grey17")
        header_label.pack(anchor=tk.W)
        recipe_text = tk.Label(text_frame, text=self.get_recipe(),
                               font=("Bahnschrift SemiBold Condensed", 20),
                               bg="PeachPuff", fg="grey17", justify=tk.LEFT, anchor=tk.W)
        recipe_text.pack(fill=tk.X)
        button_frame = tk.Frame(main_frame, bg="BlanchedAlmond")
        button_frame.pack(side=tk.BOTTOM, pady=40)
        restart_button = tk.Button(button_frame, text="Ещё раз пройти опрос", command=self.restart,
                                   bg="dark salmon",
                                   fg="grey17",
                                   font=("Bahnschrift SemiBold Condensed", 20))
        restart_button.pack(side=tk.LEFT, padx=20)
        exit_button = tk.Button(button_frame, text="Выйти", command=exit_app,
                                bg="dark salmon", fg="grey17",
                                font=("Bahnschrift SemiBold Condensed", 20))
        exit_button.pack(side=tk.LEFT, padx=20)
        self.window.update_idletasks()

    def get_recipe(self):
        with open('recipes.txt', 'r', encoding='utf-8') as file:
            recipes = file.readlines()
        key = ','.join(self.answers)
        for recipe in recipes:
            parts = recipe.strip().split(':')
            if len(parts) == 2:
                tags, recipe_text = parts
                if tags == key:
                    steps = recipe_text.split('. ')
                    formatted_recipe = '\n'.join(steps)
                    return formatted_recipe
        return "Извините, подходящий рецепт не найден."

    def restart(self):
        self.answers = []
        self.questionsindex = 0
        for widget in self.window.winfo_children():
            widget.destroy()
        QuizApp(self.window)


def instructions():
    root.withdraw()
    instruction_win = tk.Toplevel()
    instruction_win.title("Инструкция")
    instruction_win.geometry("1500x900")
    instruction_win.configure(bg="BlanchedAlmond")
    instruction_win.resizable(False, False)
    title = tk.Label(instruction_win, text="Инструкция",
                     font=("Bahnschrift SemiBold Condensed", 40),
                     bg="BlanchedAlmond", fg="grey17")
    title.pack(pady=50)
    instruction_text = (
        "Вам предстоит пройти опрос из нескольких вопросов, в результате которого вам выдаст"
        " несколько вариантов блюд и их рецепты. "
        "Нажимайте на кнопки с подходящим для вас вариантом ответа. "
        "Если вас не устраивает результат, опрос всегда можно пройти заново, "
        "нажав на кнопку «Ещё раз»."
    )
    text_label = tk.Label(instruction_win, text=instruction_text,
                          font=("Bahnschrift SemiBold Condensed", 26),
                          bg="BlanchedAlmond", fg="grey17", wraplength=1300, justify="left")
    text_label.pack(pady=40)

    def return_to_menu():
        instruction_win.destroy()
        root.deiconify()
    ok_button = tk.Button(instruction_win, text="Ок", command=return_to_menu, bg="dark salmon", fg="grey17",
                          font=("Bahnschrift SemiBold Condensed", 26), width=10)
    ok_button.pack(pady=40)

def exit_app():
    root.quit()
    root.destroy()

def start():
    for widget in root.winfo_children():
        widget.destroy()
    QuizApp(root)

def launch_main_menu():
    global root
    root = tk.Tk()
    root["bg"] = "BlanchedAlmond"
    root.title("Что приготовить?")
    root.geometry("1500x900")
    root.resizable(False, False)
    title_label = tk.Label(root, text="Что приготовить?", bg="BlanchedAlmond", fg="grey17",
                           font=("Bahnschrift SemiBold Condensed", 50))
    title_label.pack(pady=80)
    button_frame = tk.Frame(root, bg="BlanchedAlmond")
    button_frame.pack(side=tk.BOTTOM, pady=100)
    b1 = tk.Button(button_frame, text="Инструкция", command=instructions, bg="dark salmon", fg="grey17",
                   font=("Bahnschrift SemiBold Condensed", 30), width=20, height=2)
    b1.pack(side=tk.LEFT, padx=40)
    b2 = tk.Button(button_frame, text="Начать опрос", command=start, bg="dark salmon", fg="grey17",
                   font=("Bahnschrift SemiBold Condensed", 30), width=20, height=2)
    b2.pack(side=tk.LEFT, padx=40)
    b3 = tk.Button(button_frame, text="Выйти", command=exit_app, bg="dark salmon", fg="grey17",
                   font=("Bahnschrift SemiBold Condensed", 30), width=20, height=2)
    b3.pack(side=tk.LEFT, padx=40)
    root.mainloop()
launch_main_menu()
