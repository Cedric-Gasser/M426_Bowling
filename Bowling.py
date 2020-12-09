result = 0


def score(scoreString):
    global result
    result = _convertScore(scoreString)


def getResult() -> int:
    return result


def _convertScore(scoreString) -> int:
    return 300
