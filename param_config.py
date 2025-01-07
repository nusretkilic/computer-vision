class ParamConfig:
    def __init__(self):
        self._mode = None
        self._path = None
        self._gpu = None

    @property
    def mode(self):
        return self._mode

    @mode.setter
    def mode(self, value):
        self._mode = value

    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, value):
        self._path = value

    @property
    def gpu(self):
        return self._gpu

    @gpu.setter
    def gpu(self, value):
        self._gpu = value
