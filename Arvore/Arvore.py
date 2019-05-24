class Arvore:
    valor = 0
    dir = None
    esq = None

    def new(self, v):
        temp = Arvore()
        temp.valor = v
        return temp

    def inserir(self, v):
        if v > self.valor:
            if self.dir is None:
                self.dir = self.new(v)
                pass
            else:
                self.dir.inserir(v)
                pass
            pass
        else:
            if self.esq is None:
                self.esq = self.new(v)
                pass
            else:
                self.esq.inserir(v)
                pass
            pass
        pass

    def imprimir(self):
        if self is not None:
            print(self.valor)
            Arvore.imprimir(self.esq)
            Arvore.imprimir(self.dir)
            pass
        pass


    pass


