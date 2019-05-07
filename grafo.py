class Grafo:
    """
    Classe que representa um grafo. Aqui representaremos grafos como no exemplo:
    { ’A’ : {’B’:[10, 100]},
      ’B’ : {’C’:[25, 15], ’D’:[30, 11]},
      ’C’ : {’C’:[10, 20], ’B’:[25, 110]},
      ’D’ : {’C’:[12, 12]}
    }

    ...

    Attributes
    ----------
    estrutura : dict 
        Estrutura do grafo em forma de dicionário. 
        
        dict é do tipo   str: dict2
        dict2 é do tipo  str: [number, number]

        Onde o primeiro elemento do array é tempo e o segundo custo.


    Methods
    -------
    AcrescentaVertice(v)
        Acrescenta um novo vértice v.
    
    RemoveVertice(v)
        Remove o vértice v (Obs: não deve remover se houverem arcos conectados ao vértice).
    
    AcrescentaArco(v1, v2, w)
        Acrescenta um novo arco entre os vértices v1 e v2 com peso dado por w=[t, c].

    RemoveArco(v1, v2)
        Remove o arco entre v1 e v2.

    caminho, tempo <- AchaCaminhoMenorTempo(v1, v2)
        Acha o caminho de menor tempo total entre v1 e v2, Path é uma lista que contêm a sequencia dos vértices a serem visitados.

    caminho, tempo <- AchaCaminhoMenorCusto(v1, v2)
        Acha o caminho de menor custo total entre v1 e v2, Path é uma lista que contêm a sequencia dos vértices a serem visitados.
    
    ImprimeGrafo()
        Imprime na tela uma representação alfanumérica do seu grafo.
    """
    indiceTempo = 0
    indiceCusto = 1

    def __init__(self):
        """
        Parameters
        ----------
        """

        self.estrutura = {}

    def  AcrescentaVertice(self, v):
        """Acrescenta um novo vértice v.

        Parameters
        ----------
        v : str
            O vértice a ser adicionado.

        Raises
        ------
        Error
            Se o vértice já existir.
        """
        assert v not in self.estrutura, "vértice %s já existe" %v
        self.estrutura[v] = {}
        
    
    def RemoveVertice(self, v):
        """Remove o vértice v.

        Parameters
        ----------
        v : str
            O vértice a ser removido.

        Raises
        ------
        Error
            Se o vértice tiver arcos conectados a ele.
        """
        assert self.estrutura[v] == {}, "arcos conectados ao vértice %s" %v
        self.estrutura.pop(v)
    
    def AcrescentaArco(self, v1, v2, w):
        """Acrescenta um novo arco entre os vértices v1 e v2 com peso dado por w=[t, c].

        Parameters
        ----------
        v1 : str
            O vértice origem do arco.
        v2 : str
            O vértice destino do arco.
        w : [number, number]
            Os pesos do arco.

        Raises
        ------
        Error
            Se os vértices não existem ou se o arco já existir.
        """
        assert v1 in self.estrutura, "vértice %s não existe" %v1
        assert v2 in self.estrutura, "vértice %s não existe" %v2
        assert v2 not in self.estrutura[v1], "arco %s-%s já existe" %(v1, v2)
        self.estrutura[v1][v2] = w        

    def RemoveArco(self, v1, v2):
        """Remove o arco entre v1 e v2.

        Parameters
        ----------
        v1 : str
            O vértice origem do arco.
        v2 : str
            O vértice destino do arco.

        Raises
        ------
        Error
            Se os vértices não existem.
        """
        assert v1 in self.estrutura, "vértice %s não existe" %v1
        assert v2 in self.estrutura, "vértice %s não existe" %v2
        self.estrutura[v1].pop(v2)

    def AchaCaminhoMenorTempo(self, v1, v2):
        """Acha o caminho de menor tempo total entre v1 e v2.

        Parameters
        ----------
        v1 : str
            O vértice origem.
        v2 : str
            O vértice destino.

        Returns
        ----------
        caminho : [str]
            Lista que contêm a sequencia dos vértices a serem visitados.
        tempo : number
            O tempo total de v1 a v2.
        """
        origemR = v1 + "R"
        origemT = v1 + "T"
        destinoR = v2 + "R"
        destinoT = v2 + "T"
        
        testes = []
        if origemT in self.estrutura:
            testes.append([origemT, destinoR])
            if destinoT in self.estrutura:
                testes.append([origemT, destinoT])
                testes.append([origemR, destinoT])
        caminhoMinimo, tempoMinimo = self.dijkstra(origemR, destinoR, Grafo.indiceTempo)

        for origem, destino in testes:
            caminho, tempo = self.dijkstra(origem, destino, Grafo.indiceTempo)  
            if tempo < tempoMinimo:
                tempoMinimo = tempo
                caminhoMinimo = caminho

        return caminhoMinimo, tempoMinimo
        
    def AchaCaminhoMenorCusto(self, v1, v2):
        """Acha o caminho de menor custo total entre v1 e v2.
        
        Parameters
        ----------
        v1 : str
            O vértice origem.
        v2 : str
            O vértice destino.

        Returns
        ----------
        caminho : [str]
            Lista que contêm a sequencia dos vértices a serem visitados.
        custo : number
            O custo total de v1 a v2.
        """
        origemR = v1 + "R"
        origemT = v1 + "T"
        destinoR = v2 + "R"
        destinoT = v2 + "T"
        
        testes = []
        if origemT in self.estrutura:
            testes.append([origemT, destinoR])
            if destinoT in self.estrutura:
                testes.append([origemT, destinoT])
                testes.append([origemR, destinoT])
        caminhoMinimo, custoMinimo = self.dijkstra(origemR, destinoR, Grafo.indiceCusto)

        for origem, destino in testes:
            caminho, custo = self.dijkstra(origem, destino, Grafo.indiceCusto)  
            if custo < custoMinimo:
                custoMinimo = custo
                caminhoMinimo = caminho

        return caminhoMinimo, custoMinimo
    
    def ImprimeGrafo(self):
        """Imprime na tela uma representação alfanumérica do seu grafo.
        """
        for vertice in self.estrutura.keys():
            print(vertice + " -> ", end='')
            for destino, custos in self.estrutura[vertice].items():
                print(destino + ":" + str(custos), end=' ')
            print("")
    
    def vizinho(self, v1, v2):
        """Verifica se v1 e v2 são vértices vizinhos.
        Isto é, se é possível ir de v1 para v2 diretamente.

        Parameters
        ----------
        v1 : str
            O vértice origem.
        v2 : str
            O vértice destino.

        Returns
        ----------
        vizinho : boolean
            Se os vértices são vizinhos ou não.
        """
        return v2 in self.estrutura[v1]
    
    def dijkstra(self, v1, v2, indice):
        """Algoritmo de menor custo de Dijkstra.

        Parameters
        ----------
        v1 : str
            O vértice origem.
        v2 : str
            O vértice destino.
        indice : int
            O índice que indica se é minimização de tempo ou custo.
            Ver constantes definidas no começo da classe.

        Returns
        ----------
        caminho : [str]
            Lista que contêm a sequencia dos vértices a serem visitados.
        custo : number
            O custo total de v1 a v2.
        """
        assert v1 in self.estrutura, "vértice %s não existe" %v1
        assert v2 in self.estrutura, "vértice %s não existe" %v2

        if v1 == v2: 
            return [v1], 0
        S = {v1}
        #inicialize o dict dist com o peso dos arcos conectados ao vértice v1
        #anterior é um dict que guarda o vértice anterior no caminho de menor custo até v1
        #hack feio: dist de v1 será inf ao invés de 0. Isso facilita as contas?
        dist = {}
        anterior = {}
        for vertice in self.estrutura:
            if vertice != v1 and vertice in self.estrutura[v1]:
                dist[vertice] = self.estrutura[v1][vertice][indice]
                anterior[vertice] = v1
            else:
                dist[vertice] = float("inf")
        minimo = v1
        
        while len(S) != len(self.estrutura):
            #escolha um vértice M, que não esteja em S para o qual Dist[M] é minimo
            for vertice in self.estrutura.keys() - S:
                if dist[vertice] <= dist[minimo]:
                    minimo = vertice
            S.add(minimo)
            for vertice in self.estrutura.keys() - S: 
                if self.vizinho(minimo, vertice) and dist[vertice] > dist[minimo] + self.estrutura[minimo][vertice][indice]:
                    dist[vertice] = dist[minimo] + self.estrutura[minimo][vertice][indice]
                    anterior[vertice] = minimo
            minimo = v1

        path = []
        if dist[v2] != float("inf"):
            path.append(v2)
            vertice = anterior[v2]
            while vertice != v1:
                path.insert(0, vertice)
                vertice = anterior[vertice]
            path.insert(0, vertice)

        #print(dist)
        #print(anterior)
        #print(path)
        return path, dist[v2]