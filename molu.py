import sys

class MoluLang:
    class variable:
        diction = {}

        def __init__(self, name, value, tag):
            MoluLang.variable.diction[name] = self
            self.value = value
            self.tag = tag
        def valuize(code):
            if('몰' in code and '루' in code): return MoluLang.variable.diction[code].value, 'variable'
            elif('줘' in code): return 1 + code.count('더'), 'number'
            else: return str(code), 'string'

    def __init__(self):
        self.line = 0
        self.end = False

    def linecompile(self, code, NoPlusLine=False):
        if(NoPlusLine == False):self.line +=1
        code_sp = code.split(' ')
    
        if ('저기' in code): #조건문
            var1 = code_sp[0]
            var2 = code_sp[1]

            if('갸아아악 저기' in code):
                if(MoluLang.variable.valuize(var1)[0] != MoluLang.variable.valuize(var2)[0]):
                    self.linecompile(code[code.find('저기')+3:], True)
            else:
                if(MoluLang.variable.valuize(var1)[0] == MoluLang.variable.valuize(var2)[0]):
                    self.linecompile(code[code.find('저기')+3:], True)
        elif('츄릅' in code): #값 더하기
            if(code_sp[0] in MoluLang.variable.diction):
                MoluLang.variable.diction[code_sp[0]].value += MoluLang.variable.valuize(code_sp[2])[0]
        elif(code.startswith('몰') and '루' in code): #변수
            value = MoluLang.variable.valuize(code_sp[1])
            MoluLang.variable(code_sp[0], value[0], value[1])
        elif('뿅!' in code): #출력
            value = code[3:]
            print(MoluLang.variable.valuize(code[3:])[0])
        elif(code == '아!루'): #코드 종료
            sys.exit()
        elif(code.startswith('가자!')): #반복
            newline = MoluLang.variable.valuize(code_sp[1])
            if(newline[1] == 'number'): self.line = newline[0] - 1

    def compile(self, code):
        self.end = False
        codes = code.splitlines()

        while(self.end == False and self.line < len(codes)):
            self.linecompile(codes[self.line])

    def compilePath(self, path):
        self.compile(open(path, 'r', encoding='utf8').read())