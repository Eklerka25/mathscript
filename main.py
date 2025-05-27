# btw i will change lexer and interpreter modes from strings to ints later

T_ASSIGN      = 0
T_EXPRESSION  = 1
T_KEYWORD     = 2
T_VAR         = 3

variables = {}

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
        return tokensMap

class Interpreter:
    def Interpret(self, tmap):
        interpreterMode = "default"

        tokenPlace = 0

        for y in tmap:
            if interpreterMode == "default":
                if tokenPlace == 0:
                    interpreterMode = "waitForAssign"

            elif interpreterMode == "waitForAssign":
                if tokenPlace == 1 and tmap[tokenPlace] == {'=': 0}:
                    interpreterMode = "variableAssignment"
                else:
                    print(f"SYNTAX ERROR : Expected assign symbol at {tokenPlace}!")

            elif interpreterMode == "variableAssignment":
                variables[list(tmap[0].keys())[0]] = eval(list(tmap[tokenPlace].keys())[0], {}, variables)

            tokenPlace += 1

        
lexerInstance = Lexer()
interpreterInstance = Interpreter()

data = "x = 10 + 20;"
interpreterInstance.Interpret(lexerInstance.Lex(data))
print(variables)
