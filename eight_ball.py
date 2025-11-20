import random
import time
#Variables
slow_typing = True
#>Lists
question_list = []
soft_shake = ['Answer unclear... Try again later.', 'Maybe.', 'Probably...', 'Probably not...', "I don't think that's a yes or no...", 'It might be a yes...', 'I mean, I guess not...']
hard_shake = ['No, no, no!', 'Yes, yeah, sure, whatever.', 'Hey! Don\'t shake so hard!', 'Try asking somebody who knows!', 'Does that look like a yes or no question to you?', '', '']
normal_shake = ['Yes.', 'Maybe.', 'No.', 'Possibly.', 'Only ask yes or no questions.', 'I am... unsure.', 'No... most likely...']
bite = ['Ow! Why would you bite an 8 ball??', 'What is wrong with you?! Enjoy the toxic liquids!', 'Getting your macroplastics, I see.', 'cayden... it\'s you...']
#>>Probabilities
bite_probabilities = [0.60, 0.20, 0.20, 0.001]

def typer(text, delay=0.05):
    if slow_typing == True:
        for char in text:
            print(char, end = '', flush = True)
            time.sleep(delay)
        print()
    else:
        text = text.split(" ")
        for word in text:
            print(word, end=' ', flush = True)
            time.sleep(delay)
        print()
class Ball():
    def soft_shake():
        global soft_shake, soft_probabilities
        soft_probabilities = [0.142, 0.142, 0.142, 0.142, 0.142, 0.142, 0.142]
        if 'should' in question_list:
            soft_probabilities[2] += 0.25
        if 'will' in question_list:
            soft_probabilities[3] += 0.50
        if '?' in question_list:
            soft_probabilities[1] += 0.30
        if '?' not in question_list:
            soft_probabilities[0] += 0.40
        if "why" == question_list[0] or "what" == question_list[0] or "how" == question_list[0] or "who" == question_list[0]:
            soft_probabilities[4] += 100000
        selected_item = random.choices(soft_shake, weights=soft_probabilities, k=1)[0]
        if 'bet' == question_list or 'gamble' in question_list or 'gambling' in question_list:
            selected_item = 'Yeah... I guess...'
        typer("...", delay = 0.5)
        typer(selected_item)
    def normal_shake():
        global normal_shake, normal_probabilities
        normal_probabilities = [0.142, 0.142, 0.142, 0.142, 0.142, 0.142, 0.142]
        if 'should' in question_list:
            normal_probabilities[2] += 0.25
        if 'will' in question_list:
            normal_probabilities[3] += 0.50
        if '?' in question_list:
            normal_probabilities[1] += 0.30
        if '?' not in question_list:
            normal_probabilities[0] -= 0.05
        if "why" == question_list[0] or "what" == question_list[0] or "how" == question_list[0] or "who" == question_list[0]:
            normal_probabilities[4] += 100000
        selected_item = random.choices(normal_shake, weights=normal_probabilities, k=1)[0]
        if 'bet' in question_list or 'gamble' in question_list or 'gambling' in question_list:
            selected_item = 'Yes.'
        typer("...", delay = 0.5)
        typer(selected_item)
    def hard_shake():
        global hard_shake, hard_probabilities
        hard_probabilities = [0.142, 0.142, 0.142, 0.142, 0.142, 0.142, 0.142]
        if 'should' in question_list:
            hard_probabilities[0] += 0.25
        if 'will' in question_list:
            hard_probabilities[1] += 0.50
        if '?' in question_list:
            hard_probabilities[2] -= 0.03
        if '?' not in question_list:
            hard_probabilities[2] -= 0.05
        if "why" == question_list[0] or "what" == question_list[0] or "how" == question_list[0] or "who" == question_list[0]:
            hard_probabilities[4] += 100000
        selected_item = random.choices(hard_shake, weights=hard_probabilities, k=1)[0]
        if 'bet' in question_list or 'gamble' in question_list or 'gambling' in question_list:
            selected_item = 'Yes, and I hope you lose!.'
        typer("...", delay = 0.5)
        typer(selected_item)
    def bite():
        global bite_shake, bite_probabilities
        bite_probabilities[1] += 0.10
        bite_probabilities[2] += 0.10
        bite_probabilities[3] += 0.001
        selected_item = random.choices(bite, weights=bite_probabilities, k=1)[0]
        typer(selected_item)
while True:
    typer("What is your question?")
    question = input()
    question = question.lower()
    question_list = question.split(" ")
    shake_type = random.randint(1, 3)
    if 'bite' == question_list[0]:
        Ball.bite()
    else:
        try:
            typer('Shaking the eight ball')
            typer('...', delay = 0.5)
            if shake_type == 1:
                typer("That was weak, I know you can do better!")
                Ball.soft_shake()
            elif shake_type == 2:
                typer("Alright, that was pretty good! Good job!")
                Ball.normal_shake()
            elif shake_type == 3:
                typer("Wow, that was aggresive... Are you alright?")
                Ball.hard_shake()
            else:
                print('literally how.') 
        except Exception as e:
            typer(f"An error occured: {e}")
