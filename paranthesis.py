
openingBrackets = ['(','[','{']
closingBrackets = [')',']','}']
stack = []
def checkParenthesis(inputString):
    for s in inputString:
        if s in openingBrackets:
            stack.append(s)

        elif s in closingBrackets:
            if s is ')':
                if (stack[len(stack)-1] is '('):
                    stack.pop()

                else:
                    break

            elif s is ']':
                if (stack[len(stack)-1] is '['):
                    stack.pop()

                else:
                    break


            elif s is '}':
                if (stack[len(stack)-1] is '}'):
                    stack.pop()

                else:
                    break

    if len(stack)==0:
            print('Valid Input')

    else:
        print('Invalid Input')

            



paranthesis = input('Enter input string')

checkParenthesis(paranthesis)

