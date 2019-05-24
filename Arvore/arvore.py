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

    def tostring(self):
        if self is not None:
            esq = str(Arvore.tostring(self.esq))
            dir = str(Arvore.tostring(self.dir))
            return str(self.valor)+ " \n" + esq + dir
            pass
        else:
            return ""
        pass



    pass


arv = Arvore.new(Arvore, 10)
arv.inserir(9)
arv.inserir(11)
arv.inserir(13)
arv.inserir(12)
arv.inserir(13)
arv.inserir(12)
print(arv.tostring())
