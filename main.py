import networkx as nx

from spikyballsampler import SpikyBallSampler

graph = nx.watts_strogatz_graph(1000, 10, 0)

sampler = SpikyBallSampler()

new_graph = sampler.sample(graph)