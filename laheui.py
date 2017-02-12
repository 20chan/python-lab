class AheuiFunc:
    def __init__(self, code):
        self.code = code

    def eval(self, input):
        '''
        요기는~~~~ 아희 코드를 실행하는~~~~
        이걸 보시는 사람은 구현해서 풀리퀘를 날려줘요~~~~~~~~~
        '''
        return 1

    def __call__(self, *args):
        return self.eval(args)

# print 1+1
plus = AheuiFunc('방방다망희')
print(plus(1, 1))

# print ord(input)
ah_ord = AheuiFunc('밯망희')
print(ah_ord(input()))
