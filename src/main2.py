"""Módulo principal.
Lê os argumentos diretamente da linha de comando.
"""
import argparse
import grafo

def parse_args():
    parser = argparse.ArgumentParser(description='Lê arquivo de configuração de grafo e calcula caminhos de custo mínimo.')
    parser.add_argument('arquivo', type=str, help='nome do arquivo do grafo')
    parser.add_argument('origem', type=str, help='vértice de origem')
    parser.add_argument('destino', type=str, help='vértice de destino')
    return parser.parse_args()

def main(args):
    """Função principal da aplicação.
    """
    config = args.arquivo
    c = grafo.Grafo()

    #adiciona os vértices
    for linha in open(config):
        c.AcrescentaVertice(linha.split(' ')[0].upper())

    #adiciona os arcos
    for linha in open(config):
        linha = linha.strip()
        arcos = linha.split(' ')
        origem = arcos.pop(0)
        for arco in arcos:
            arco = arco.split(':')
            destino = arco[0]
            custos = eval(arco[1])
            c.AcrescentaArco(origem.upper(), destino.upper(), custos)

    #c.ImprimeGrafo()
    v1 = args.origem
    v2 = args.destino
    
    f = open("caminhos.txt", "a")
    caminho, tempo = c.AchaCaminhoMenorTempo(v1, v2)
    print("Caminho de menor tempo (%.1f) de %s até %s é:" %(tempo, v1, v2), caminho)
    f.write("Caminho de menor tempo (%.1f) de %s até %s é: " %(tempo, v1, v2) + str(caminho) + '\n')

    caminho, custo = c.AchaCaminhoMenorCusto(v1, v2)
    print("Caminho de menor custo (%d) de %s até %s é:" %(custo, v1, v2), caminho)
    f.write("Caminho de menor custo (%d) de %s até %s é: " %(custo, v1, v2) + str(caminho) + '\n\n')

    f.close()

def ArquivoExiste(fn):
    try:
      open(fn, "r")
      return 1
    except IOError:
      print("Erro: Arquivo \"%s\" não encontrado." %fn)
      return 0

def testeInicial():
    c = grafo.Grafo()
    c.AcrescentaVertice("1")
    c.AcrescentaVertice("2")
    c.AcrescentaVertice("3")
    c.AcrescentaVertice("4")
    c.AcrescentaVertice("5")
    c.AcrescentaVertice("6")
    c.AcrescentaArco("1", "2", 30)
    c.AcrescentaArco("1", "4", 50)
    c.AcrescentaArco("1", "5", 40)
    c.AcrescentaArco("1", "6", 100)
    c.AcrescentaArco("2", "3", 40)
    c.AcrescentaArco("3", "5", 10)
    c.AcrescentaArco("3", "6", 30)
    c.AcrescentaArco("4", "3", 10)
    c.AcrescentaArco("5", "4", 20)
    c.AcrescentaArco("5", "6", 70)
    c.dijkstra("1", "6", 0)

if __name__ == '__main__':
    main(parse_args())
