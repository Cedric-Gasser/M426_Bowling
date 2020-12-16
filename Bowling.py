import re

result = 0


def score(score_string):
    global result
    result = convertScore(score_string)


def getResult() -> int:
    return result


def convertScore(score_string) -> int:
    score_string = score_string.upper().replace("-", "0")
    score_per_round = []

    pointer = 0
    for i in range(10):
        if score_string[pointer] == "X":  #When there's a strike
            score_per_round.append(score_string[pointer] + score_string[pointer + 1] + score_string[pointer + 2])
            pointer += 1

        elif score_string[pointer + 1] == "/":   #When there's a spare
            score_per_round.append(score_string[pointer] + score_string[pointer + 1] + score_string[pointer + 2])
            pointer += 2

        else:    #When there are no special cases
            score_per_round.append(score_string[pointer] + score_string[pointer + 1])
            if int(score_string[pointer]) + int(score_string[pointer + 1]) > 9:
                raise Exception("More than 10 pins?!")
            pointer += 2

    print(score_per_round)

    res = 0
    for i in score_per_round:
        res += parseCode(i)

    return res


def parseCode(round_string) -> int:
    res = 0
    for i in range(len(round_string)):
        if round_string[i] == "X":
            res += 10
        elif round_string[i] == "/":
            res += 10
            res -= int(round_string[i - 1])
        else:
            res += int(round_string[i])
    return res


if __name__ == "__main__":
    score = input()
    print(convertScore(score))
