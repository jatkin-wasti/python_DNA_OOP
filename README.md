# Task
## DNA string parsing
- Create a class with methods that takes a string of a DNA sequence
- Have it search through the string and tally up how often each letter occurs in the string
- The implementation should support a string up to 1000 characters long, but not longer
## Solution
- First we create our class and use our initialisation method to assign all relevant attributes
- The (letter)_num variables are the counters that we will use later in our loop
```
class DnaParse:
    def __init__(self, max_length, dna_sequence):  # Taking the max length to test and the sequence to be tested
        # Assign these values so that we can use them later
        self.max_length = max_length
        self.dna_sequence = dna_sequence
        self.a_num = 0
        self.c_num = 0
        self.g_num = 0
        self.t_num = 0
```
- The task says to take "A DNA string of length 1000 at most", we will include a method to check the length of a given 
sequence
```
    def length_check(self):
        # Check if the provided sequence is too long and return the appropriate message
        if len(self.dna_sequence) > self.max_length:
            return f"This sequence is too long to parse. Please provide a sequence shorter than {self.max_length} " \
                   f"characters long."
        else:
            return "We can parse this sequence!"
```
- We should also have a method to display the values of our (letter)_num variables
```
    def display_output(self):
        return f"Here is a report of how often each letter appears in the provided string:\n" \
               f"A: {self.a_num}, " \
               f"C: {self.c_num}, " \
               f"G: {self.g_num}, " \
               f"T: {self.t_num}"
```
- Now we need a method to actually loop through the sequence and add up how many of each letter it contains
- But we should only loop through sequences that are shorter than the defined maximum (in this case 1000)
- Therefore, we'll first check what is returned from our length_check method and only continue if it is shorter than
 this value 
```
    def loop_through(self):
        # We should only loop through a sequence that isn't bigger than the max_length
        if self.length_check() == "We can parse this sequence!":
```
- And then we can loop through the sequence
```
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
``` 
- Once this loop has completed, we can print the output of our display_output method

```
            # Once the for loop is done we can call our display_output method to display the numbers calculated
            print(self.display_output())
        else:
            # If the sequence is too long, print the message telling the user this
            print(self.length_check())
```
- That trailing else is the counterpart to the initial if statement checking the length of the sequence, if it is too 
long the else statement runs and prints the necessary warning to the user
## Testing
- First lets test it where the sequence is less than the max length allowed
```
dna_test = DnaParse(1000, "ACTTTGCGCCGAGACAGATATATACACAGAAAGAACACATATAAATTATTCGGCGCTCTACTAGCGGCTA")
dna_test.loop_through()
```
- This test outputs the result exactly as it should so let's now test it with a much more restricted max length
```
dna_test = DnaParse(10, "ACTTTGCGCCGAGACAGATATATACACAGAAAGAACACATATAAATTATTCGGCGCTCTACTAGCGGCTA")
dna_test.loop_through()
```
- This tells the user to provide a sequence that has fewer characters than the max length