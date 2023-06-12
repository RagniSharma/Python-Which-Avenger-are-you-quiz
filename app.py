from flask import Flask, render_template, request

app = Flask(__name__)


questions = [
    "Which superpower would you choose?",
    "What is your preferred weapon?",
    "Which word describes you best?",
    "How do you handle challenges?",
    "What is your favorite color?",
    "What is your ideal team size?",
    "What is your favorite hobby?",
    "How do you make decisions?",
    "What is your preferred mode of transportation?",
    "How do you handle responsibility?"
]

options = [
    ["Super strength", "Flight", "Telepathy", "Invisibility"],
    ["Sword", "Shield", "Bow and arrows", "Guns"],
    ["Brave", "Intelligent", "Determined", "Mysterious"],
    ["Face them head-on", "Analyze and strategize", "Seek help from others", "Adapt and improvise"],
    ["Red", "Blue", "Green", "Yellow"],
    ["Alone", "Small group", "Large team", "No preference"],
    ["Sports", "Reading", "Gaming", "Outdoor activities"],
    ["Trust your instincts", "Analyze pros and cons", "Seek advice from others", "Go with the flow"],
    ["Sports car", "Motorcycle", "Jet", "Public transportation"],
    ["Take charge", "Delegate tasks", "Work as a team", "Depends on the situation"]
]

score=0

@app.route('/')
def home():
   return render_template('index.html')


@app.route('/quiz/', methods=['GET', 'POST'])
def quiz():
    if request.method == 'POST':
        answers = []
        for i in range(len(questions)):
            answer = request.form.get(f'answer-{i}')
            if answer is None or not answer.isdigit() or not (1 <= int(answer) <= 4):
                return render_template('q.html', questions=questions, options=options, error=True)
            answers.append(int(answer))

        score = sum(answers)

        avengers_characters = {
            "Iron Man": range(12,14),
            "Captain America": range(23,25),
            "Black Widow": range(10,12),
            "Thor": range(14,16),
            "Hulk": range(18, 20),
            "Black Panther": range(16,18),
            "Spider-Man": range(22, 24),
            "Doctor Strange": range(30,32),
            "Captain Marvel": range(28,30),
            "Scarlet Witch": range(24,26),
            "Hawkeye": range(26, 28),
            "Nick Fury": range(40,42),
            "Ant-Man": range(20, 22),
            "Wasp": range(32,34),
            "Vision": range(34, 36),
            "Falcon": range(38, 40),
            "War Machine": range(36, 38),
        }

        avenger = None
        for character, score_range in avengers_characters.items():
            if score in score_range:
                avenger = character
                break

        return render_template('r.html', avenger=avenger,score=score)
    
        

    return render_template('q.html', questions=questions, options=options, error=False)
    

if __name__ == '__main__':
    app.run(debug=True)
