import random

game_scores = ["unos","dos","tres","cuatro","cinco","seises",
               "tres de un tipo","cuatro de un tipo","casa llena",
               "pequeño recto","grande recto","oportunidad","yahtzee"]

player_scores = {
    "jugador 1":{game_score: None for game_score in game_scores},
    "jugador 2":{game_score: None for game_score in game_scores}
}
#lanzar dados
def roll_dice (number_dices=5):
    return [random.randint(1,6) for _ in range(number_dices)]

#volver a tirar los dados

def reroll_dice(dice):
    while True:
        numbers_dices = input("Ingrese el número de los dados para tirar de nuevo (separado por espacios, valores del 1 al 5): ")
        try:
            numbers_dices = [int(i) - 1 for i in numbers_dices.split()] 
            if all(0 <= i < len(dice) for i in numbers_dices):
                break
            else:
                print("Índices inválidos, por favor ingrese valores entre 1 y 5.")
        except ValueError:
            print("Entrada inválida. Por favor ingrese números entre 1 y 5, separados por espacios.")
    
    for index in numbers_dices:
        dice[index] = random.randint(1, 6)
    return dice         

#calcular puntuaciones

def calculate_score(dice, score_game):
    if score_game == "unos":
        return dice.count(1) * 1
    elif score_game == "dos":
        return dice.count(2) * 2
    elif score_game == "tres":
        return dice.count(3) * 3
    elif score_game == "cuatro":
        return dice.count(4) * 4
    elif score_game == "cinco":
        return dice.count(5) * 5
    elif score_game == "seises":
        return dice.count(6) * 6
    elif score_game == "tres de un tipo":
        for i in set(dice):
            if dice.count(i) >= 3:
                return sum(dice)
    elif score_game == "cuatro de un tipo":
        for i in set(dice):
            if dice.count(i) >= 4:
                return sum(dice)
    
    #verifica si hay dos dados de un valor y tres de otro
    #esto significa casa llena y devuelve 25 puntos
    
    elif score_game == "casa llena":
        if len(set(dice)) == 2 and (dice.count(dice[0]) == 2 or dice.count(dice[0]) == 3):
            return 25
    elif score_game == "pequeño recto":
        if set([1, 2, 3, 4]).issubset(set(dice)) or set([2, 3, 4, 5]).issubset(set(dice)) or set([3, 4, 5, 6]).issubset(set(dice)):
            return 30
    elif score_game == "grande recto":
        if set([1, 2, 3, 4, 5]).issubset(set(dice)) or set([2, 3, 4, 5, 6]).issubset(set(dice)):
            return 40
        #verifica si todos los dados tienen el mismo valor
        #y devuelve 50 puntos
    elif score_game == "yahtzee":
        if len(set(dice)) == 1:
            return 50
    elif score_game == "oportunidad":
        return sum(dice)
    return 0 

#Manejar turnos de jugadores

for round_number in range(13):
    for player in ["jugador 1", "jugador 2"]:
         print("###################################")
         print(f"{player} turno {round_number + 1}")
         dice = roll_dice()
         print(f"Lanzamiento inicial: {dice}")
         
         for _ in range(3):
             reroll = input("Quiere lanzar de nuevo? (y/n): ")
             if reroll.lower() == 'y':
                dice = reroll_dice(dice)
                print(f"Nuevo resultado: {dice}")
             else:
                break
        
         print("Puntuaciones del juego disponibles:", [score for score in game_scores if player_scores[player][score] is None])
         choose_score = input("Elige una puntuación ")
         player_scores[player][choose_score] = calculate_score(dice, choose_score)
         print(f"{player} anotó {player_scores[player][choose_score]} puntos en {choose_score}")


total_scores = {player: sum(player_scores[player][score] for score in game_scores if player_scores[player][score] is not None) for player in player_scores}
winner = max(total_scores, key=total_scores.get)
print("Puntajes finales:", total_scores)
print(f"El ganador es: {winner}!")               