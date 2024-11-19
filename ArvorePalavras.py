import os 
os.system('cls')

dici = [
    'Porta',
    'Portão',
    'Arroz',
    'Prata',
    'Árvore',
    'Argola',
    'Bola',
    'Bala',
    'Batata',
    'Casa',
    'Casamento',
    'Barco',
    'Bar',
]

tam = 0

for p in dici:
    tam += len(p)

class No:
    def __init__(self, ch):
        self.ch = ch
        self.fim = False #marcador de final da palavra
        
        self.filhos = []
        
    def add(self, palavra):
        if len(palavra) >= 1:
            ch = palavra[0].lower()
            
            #busca se o ch existe
            for f in self.filhos:
                if f.ch == ch:
                    f.add(palavra[1:])
                    return 
            
            #Não existe ch
            no = No(ch)
            self.filhos.append(no)
            no.add(palavra[1:])
        else:
            #Marcando a ultima letra da palavra como o fim da palavra
            self.fim = True
            
    def preordem(self):
        print(self.ch, end =", ")
        
        for f in self.filhos:
            f.preordem()
        
    def busca(self, palavra):
        ch = palavra[0].lower()
        for f in self.filhos:
            if f.ch == ch:
                if len(palavra) == 1:
                    return f.fim
                else:
                    return f.busca(palavra[1:])
                          
        return False
        
raiz = No('')

for p in dici:
    raiz.add(p)

raiz.preordem()
print("\n",raiz.busca('bar'))
