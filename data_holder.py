class DataHolder:
    def __init__(self):
        self.bpm_data = []
        self.blink_data = []


    def add_new_bpm_input(self, input_data):
        self.bpm_data.append(input_data)

    def add_new_blink_input(self, input_data):
        self.bpm_data.append(input_data)