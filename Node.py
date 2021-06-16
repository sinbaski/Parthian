import numpy as np

class Node:
    def __init__(self):
        self.name = None;
        self.location = (np.nan, np.nan);
        self.capacity = np.inf;
        self.costPerUnit = 0;
        self.type = "warehouse";

class Lorry:
    def __init__(self):
        self.id = None;
        self.location = (np.nan, np.nan);

class Container:
    def __init__(self, containerId, location, loaded, destination):
        self.id = containerId;
        self.location = location;
        self.loaded = (loaded != 0);
        self.destination = destination;
        
class TrafficNetwork:
    def __init__(self):
        self.nodeIndex = {};
        # A matrix describing the traffic network
        # self.edges = np.array((len(self.nodeIndex), len(self.nodeIndex)));
        self.edges = np.array([
            [np.inf, 1, 1],
            [1, np.inf, 1],
            [1, 1, np.inf]
            ]);
        


