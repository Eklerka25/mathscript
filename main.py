# btw i will change lexer modes from strings to ints later

T_ASSIGN      = 0
T_EXPRESSION  = 1
T_KEYWORD     = 2
T_VAR         = 3

variables = {}

context = {"a": 5, "b": 3}
result = eval("2 + 2", {}, context)

class Lexer:
    def Lex(self, data):
        print("InputData:", data)
        print("InputDataSize:", len(data))

        tokensMap = {}
        tokenPlace = 0
        currentExpression = ""

        lexerMode = "default"

        for x in data.replace(" ", ""):
            if x == ";":
                if lexerMode == "waitForExpression":
                    tokensMap[tokenPlace] = {currentExpression : T_EXPRESSION}
                break
            else:
                if tokenPlace == 0:
                    if x.isalpha() and x.isascii():
                        tokensMap[tokenPlace] = {x : T_VAR}
                        lexerMode = "waitForAssign"
                    elif x == ">":
                        tokensMap[tokenPlace] = {x : T_KEYWORD}
                        lexerMode = "waitForVariableReference"

                elif lexerMode == "waitForAssign":
                    if x == "=":
                        tokensMap[tokenPlace] = {x : T_ASSIGN}
                        lexerMode = "waitForExpression"
                    else:
                        print(f"SYNTAX ERROR : Expected assign symbol at {tokenPlace}!")
                        break

                elif lexerMode == "waitForExpression":
                    currentExpression += x
                    tokenPlace -= 1

            tokenPlace += 1

        print("OutputMap:", tokensMap)
        
lexerInstance = Lexer()

data = "x = 10 + 20;"
lexerInstance.Lex(data)
