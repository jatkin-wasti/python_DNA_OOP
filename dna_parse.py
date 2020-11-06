class DnaParse:
    def __init__(self, max, dna_sequence):
        self.max = max
        self.dna_sequence = dna_sequence
        self.a_num = 0
        self.c_num = 0
        self.g_num = 0
        self.t_num = 0

    def length_check(self):
        if len(self.dna_sequence) > self.max:
            return f"This sequence is too long to parse. Please provide a sequence shorter than {self.max} " \
                   f"characters long."
        else:
            return "We can parse this sequence!"

    def loop_through(self):
        for _ in self.dna_sequence:
            if _.upper() == "A":
                self.a_num += 1
            elif _.upper() == "C":
                self.c_num += 1
            elif _.upper() == "G":
                self.g_num += 1
            elif _.upper() == "T":
                self.t_num += 1

