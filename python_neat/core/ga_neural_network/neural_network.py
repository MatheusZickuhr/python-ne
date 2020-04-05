class NeuralNetwork:

    def __init__(self, create_model=True, output_size=None, input_shape=None):
        self.input_shape = input_shape
        self.output_size = output_size
        self.fitness = 0
        self.dense_layers = list()
        self.model = self.create_model() if create_model else None
        self.was_evaluated = False

    def create_model(self):
        raise NotImplementedError()

    def get_output(self, obs):
        raise NotImplementedError()

    def crossover(self, other):
        raise NotImplementedError()

    def mutate(self):
        raise NotImplementedError()

    def __str__(self):
        return f'fitness = {self.fitness}'