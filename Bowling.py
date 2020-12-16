result = 0


def score(score_string):
    global result
    result = convertScore(score_string)


def getResult() -> int:
    return result


def convertScore(score_string) -> int:
    score_string = score_string.upper()
    score_per_round = []

    pointer = 0
    for i in range(10):
        if score_string[pointer] == "X":
            score_per_round.append(score_string[pointer] + score_string[pointer + 1] + score_string[pointer + 2])
            pointer += 1

        elif 10 > int(score_string[pointer]) > 0 and score_string[pointer + 1] == "/":
            score_per_round.append(score_string[pointer] + score_string[pointer + 1] + score_string[pointer + 2])
            pointer += 2

        else:
            score_per_round.append(score_string[pointer] + score_string[pointer + 1])
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
        elif round_string[i] == "-":
            round_string[i] = "0"
        else:
            res += int(round_string[i])
    return res


if __name__ == "__main__":
    score = input()
    print(convertScore(score))
