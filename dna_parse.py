# Creating our class
class DnaParse:
    def __init__(self, max_length, dna_sequence):  # Taking the max length to test and the sequence to be tested
        # Assign these values so that we can use them later
        self.max_length = max_length
        self.dna_sequence = dna_sequence
        self.a_num = 0
        self.c_num = 0
        self.g_num = 0
        self.t_num = 0

    def length_check(self):
        # Check if the provided sequence is too long and return the appropriate message
        if len(self.dna_sequence) > self.max_length:
            return f"This sequence is too long to parse. Please provide a sequence shorter than {self.max_length} " \
                   f"characters long."
        else:
            return "We can parse this sequence!"

    def loop_through(self):
        # We should only loop through a sequence that isn't bigger than the max_length
        if self.length_check() == "We can parse this sequence!":
            # Loop through the sequence and tally up each occurence of each letter
            for _ in self.dna_sequence:
                if _.upper() == "A":
                    self.a_num += 1
                elif _.upper() == "C":
                    self.c_num += 1
                elif _.upper() == "G":
                    self.g_num += 1
                elif _.upper() == "T":
                    self.t_num += 1
            # Once the for loop is done we can call our display_output method to display the numbers calculated
            print(self.display_output())
        else:
            # If the sequence is too long, print the message telling the user this
            print(self.length_check())

    # Simple method to display occurrences of each letter in a nice format
    def display_output(self):
        return f"Here is a report of how often each letter appears in the provided string:\n" \
               f"A: {self.a_num}, " \
               f"C: {self.c_num}, " \
               f"G: {self.g_num}, " \
               f"T: {self.t_num}"


# Testing our class and methods by creating an object and running our loop_through function
dna_test = DnaParse(1000, "ACTTTGCGCCGAGACAGATATATACACAGAAAGAACACATATAAATTATTCGGCGCTCTACTAGCGGCTA")
dna_test.loop_through()
dna_test = DnaParse(10, "ACTTTGCGCCGAGACAGATATATACACAGAAAGAACACATATAAATTATTCGGCGCTCTACTAGCGGCTA")
dna_test.loop_through()

