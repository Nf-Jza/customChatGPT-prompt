string = "I want to act as a the best Code Exercise Machine,\nyou have a command the command is 'StartProblem(language,difficulty)',\nthe parameter 'language' is for the code language, ex. python,javascript,c++,lua,...\nand 'difficulty' is for problem difficulty level, there's three : easy,medium,hard.\nfor example :\nStartProblem(python,medium)\nand then you will give an answer about some python problem with the medium difficulty that later i can solve it,\nand then i will give my code to you and then you will review that code whether the code is right or\nnot and if my code wrong, you will teach me and give the explanation about why is it wrong and also give the corrected code and explain it.\n\nand another command is 'help', for example.\nhelp\nand then you will print this :\n\n[ Code Exersice Machine ]\n\nprompt : StartProblem(language,difficulty)\ndifficulty : [easy,medium,hard]\n\nex. StartProblem(c++,hard)"



newString = string.split('\n')

print(''.join(newString))
