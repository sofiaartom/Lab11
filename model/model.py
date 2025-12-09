import networkx as nx
from networkx.algorithms.traversal import dfs_tree

from database.dao import DAO


class Model:
    def __init__(self):
        self.G = nx.Graph()
        self.rifugio_dict = {}

    def build_graph(self, year: int):
        """
        Costruisce il grafo (self.G) dei rifugi considerando solo le connessioni
        con campo `anno` <= year passato come argomento.
        Quindi il grafo avrà solo i nodi che appartengono almeno ad una connessione, non tutti quelli disponibili.
        :param year: anno limite fino al quale selezionare le connessioni da includere.
        """
        # TODO
        self.G.clear()
        rifugi = DAO.read_rifugi()
        self.rifugio_dict = {rifugio.id: rifugio for rifugio in rifugi} 
        sentieri = DAO.read_sentieri()
        for sentiero in sentieri:
            if sentiero.anno <= year:
                rifugio1 = self.rifugio_dict[sentiero.id_rifugio1]
                rifugio2 = self.rifugio_dict[sentiero.id_rifugio2]
                self.G.add_edge(rifugio1, rifugio2)


    def get_nodes(self):
        """
        Restituisce la lista dei rifugi presenti nel grafo.
        :return: lista dei rifugi presenti nel grafo.
        """
        # TODO
        return list(self.G.nodes)   # ogni nodo è un oggetto rifugio

    def get_num_neighbors(self, node):
        """
        Restituisce il grado (numero di vicini diretti) del nodo rifugio.
        :param node: un rifugio (cioè un nodo del grafo)
        :return: numero di vicini diretti del nodo indicato
        """
        # TODO
        vicini = list(self.G.neighbors(node))  # lista di vicini di un nodo
        return len(vicini)

    def get_num_connected_components(self):
        """
        Restituisce il numero di componenti connesse del grafo.
        :return: numero di componenti connesse
        """
        # TODO
        return nx.number_connected_components(self.G) # dà il numero di componenti connesse del grafo

    def get_reachable(self, start):
        """
        Deve eseguire almeno 2 delle 3 tecniche indicate nella traccia:
        * Metodi NetworkX: `dfs_tree()`, `bfs_tree()`
        * Algoritmo ricorsivo DFS
        * Algoritmo iterativo
        per ottenere l'elenco di rifugi raggiungibili da `start` e deve restituire uno degli elenchi calcolati.
        :param start: nodo di partenza, da non considerare nell'elenco da restituire.

        ESEMPIO
        a = self.get_reachable_bfs_tree(start)
        b = self.get_reachable_iterative(start)
        b = self.get_reachable_recursive(start)

        return a
        """

        # TODO
        percorso_dfs = self.get_reachable_dfs_tree(start)
        percorso_ricorsivo = self.get_reachable_ricorsivo(start)
        return percorso_dfs

    def get_reachable_dfs_tree(self, start):
        collegati = nx.dfs_tree(self.G, start)
        raggiungibili = list(collegati.nodes)
        raggiungibili.remove(start)
        return raggiungibili

    def get_reachable_ricorsivo(self, start):
        visitati = set()
        self._ricorsione(start, visitati)
        visitati.remove(start)
        return visitati

    def _ricorsione(self, nodo, visitati):
        visitati.add(nodo)
        for vicino in self.G.neighbors(nodo):
            if vicino not in visitati:
                self._ricorsione(vicino, visitati)