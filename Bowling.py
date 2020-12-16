result = 0

def score(scoreString):
    global result
    result = _convertScore(scoreString)


def getResult() -> int:
    return result


def _convertScore(scoreString) -> int:
    scoreString = scoreString.upper();
    scorePerRound = []

    pointer = 0
    for i in range(10):
        round = scoreString[pointer]
        if round == "X":
            scorePerRound.append(scoreString[pointer] + scoreString[pointer+1] + scoreString[pointer+2])
            pointer += 1

        elif int(round) < 10 and int(round) > 0 and scoreString[pointer + 1] == "/":
            scorePerRound.append(scoreString[pointer] + scoreString[pointer+1] + scoreString[pointer+2])
            pointer += 2

        else:
            scorePerRound.append(scoreString[pointer] + scoreString[pointer + 1])
            pointer += 2

    print(scorePerRound)

    res = 0
    for i in scorePerRound:
        res += parseCode(i)

    return res

def parseCode(roundString) -> int:
    res = 0
    for i in range(len(roundString)):
        if roundString[i] == "X":
            res += 10
        elif roundString[i] == "/":
            res += 10
            res -= int(roundString[i-1])
        elif roundString[i] == "-":
            roundString[i] = "0"
            pass
        else:
            res += int(roundString[i])
    return res


if __name__ == "__main__":
    score = input()
    print(_convertScore(score))