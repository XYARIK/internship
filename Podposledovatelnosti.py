def min_subsequence_length(sequence):
    n = len(sequence)
    if n == 0:
        return "NONE"
    
    count = {}
    required_length = 26  