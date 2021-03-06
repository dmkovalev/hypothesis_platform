from utils import check_completeness
from utils import is_structure
from utils import save_default_names
from utils import set_default_names
from CreateGraph import Hypothesis_encoding
from HypothesisConnection import construct_lattice

class VirtualExperiment(self, specification):

    def __init__(self, workflow, hypotheses, models, ontology):
        self.workflow = workflow  # No. of vertices
        self.hypothesis = hypotheses  # default dictionary to store graph
        self.models = models
        self.ontology = ontology
        self.lattice = construct_lattice(hypotheses, workflow)

    def __getattr__(self, item):
        return self.graph[item]

    def __repr__(self):
        return str(self.graph)

    def load(db, type, id):
        db.connect()
        try:
            print(f'Loading from: {cls.root / storage / filename}') if cls.debug else None
            with open(cls.root / storage / filename, 'rb') as f:
                return pickle.load(f)

            if type == 'hypothesis':
                artefact = db._load_hypothesis(id)
            elif type == 'model':
                artefact = db._load_model(id)
            elif type == 'ontology':
                artefact = db._load_ontology(id)
            elif type == 'workflow':
                artefact = db._load_workflow(id)
            elif type == 'lattice':
                artefact = db._load_lattice(id)

            return artefact
        except FileNotFoundError:
            print('Объект отсутствует в базе данных.')

    def add(self, type, artefact):
        if type == 'hypothesis':
            self.hypothesis.append(artefact)
        elif type == 'model':
            self.model.append(artefact)
        elif type == 'ontology':
            self.ontology.append(artefact)
        elif type == 'workflow':
            self.workflow = artefact
        elif type == 'lattice':
            self.lattice.append(artefact)

    def modify(self, type, artefact):

        if type == 'hypothesis':
            artefacts = []

            for i in range(1, len(H_list)):
                H1 = H_list[i][0]
                H2 = H_list[i][1]
                print("Check pair: ", (H1, H2))

                connected_h, is_connected = concat_H(data.copy(), H1, H2)
                if is_connected:
                    artefacts.append((H1, H2))

        elif type == 'model':
            artefacts = []

            for i in range(1, len(artefact)):
                M1 = artefact[i][0]
                M2 = artefact[i][1]
                print("Check pair: ", (M1, M2))

                connected_h, is_connected = concat_H(data.copy(), M1, M2)
                if is_connected:
                    artefacts.append((M1, M2))

        return artefacts

class Hypothesis(self, specification):
    def __init__(self, vertices):
        self.V = vertices  # No. of vertices
        self.graph = defaultdict(list)  # default dictionary to store graph
        self.real_V_names = []

    def __getattr__(self, item):
        return self.graph[item]

    def __repr__(self):
        return str(self.graph)


class Model(self, specification):
    def __init__(self, model):
        spec = _parse_specification(model, specification)
        self.model = model  # No. of vertices
        self.spec = defaultdict(spec)  # default dictionary to store graph

    def __getattr__(self, item):
        return self.graph[item]

    def __repr__(self):
        return str(self.graph)


class Ontology(self, specification):
    def __init__(self, ontology):
        spec = _parse_specification(ontology, specification)
        self.model = ontology  # No. of vertices
        self.spec = defaultdict(spec)  # default dictionary to store graph

    def __getattr__(self, item):
        return self.ontology[item]

    def __repr__(self):
        return str(self.ontology)


class Workflow(self, specification):
    self.G = Graph(connection_matrix.shape[1])
    self.G.real_V_names = connection_matrix.columns.values
    connection_matrix.columns = ["H" + str(k) for k in range(G.V)]
    connection_matrix.index = ["H" + str(k) for k in range(G.V)]

    for col in self.connection_matrix.columns:
        self.connected = self.connection_matrix.index[connection_matrix[col] == 1]
        sself.tart = int(col.split("H")[1])
        for k in range(len(self.connected)):
            self.G.addEdge(start, int(connected[k].split("H")[1]))







