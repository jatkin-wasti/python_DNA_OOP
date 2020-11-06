class DnaParse:
    def __init__(self, max_length, dna_sequence):
        self.max_length = max_length
        self.dna_sequence = dna_sequence
        self.a_num = 0
        self.c_num = 0
        self.g_num = 0
        self.t_num = 0

    def length_check(self):
        if len(self.dna_sequence) > self.max_length:
            return f"This sequence is too long to parse. Please provide a sequence shorter than {self.max_length} " \
                   f"characters long."
        else:
            return "We can parse this sequence!"

    def loop_through(self):
        if self.length_check() == "We can parse this sequence!":
            for _ in self.dna_sequence:
                if _.upper() == "A":
                    self.a_num += 1
                elif _.upper() == "C":
                    self.c_num += 1
                elif _.upper() == "G":
                    self.g_num += 1
                elif _.upper() == "T":
                    self.t_num += 1
            print(self.display_output())
        else:
            print(self.length_check())


    def display_output(self):
        return f"Here is a report of how often each letter appears in the provided string:\n" \
               f"A: {self.a_num}, " \
               f"C: {self.c_num}, " \
               f"G: {self.g_num}, " \
               f"T: {self.t_num}"


dna_test = DnaParse(1000, "ACTTTGCGCCGAGACAGATATATACACAGAAAGAACACATATAAATTATTCGGCGCTCTACTAGCGGCTA")
dna_test.loop_through()

