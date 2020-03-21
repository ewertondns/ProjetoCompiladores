import sys

class BagOfWord():

    def __init__(self, textos):

        self.textos = textos

    def contador(self):

        qtd_textos = len(self.textos)
        bag = {}
        palavras = []
        count_textos = 0

        print("\n")
        print(self.textos)
        for texto in self.textos:
            texto = texto.split(" ")

            for palavra in texto:
                if palavra not in palavras:
                    bag[palavra] = {}

                    bag[palavra]["contagem"] = [0] * qtd_textos
                    bag[palavra]["contagem"][count_textos] = 1

                    palavras.append(palavra)
                else:

                    bag[palavra]["contagem"][count_textos] += 1

            count_textos += 1

        for palavra in palavras:

            total_palavras = len(palavras)
            qtd_palavra = sum(bag[palavra]["contagem"])

            bag[palavra]["frequencia"] = ((qtd_palavra)/total_palavras) * 100
            bag[palavra]["frequencia"] = str("{:.2f}".format(bag[palavra]["frequencia"])) + "%"

        print("\n\n\nPalavras:\n", palavras)
        print("\n\n\nBag of Words:\n", bag)
