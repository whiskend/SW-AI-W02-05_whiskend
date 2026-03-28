if equation[start] == "+" or equation[start] == "-":
        for end in range(start+1, len(equation)):
            if equation[start] == "+" or equation[start] == "-" or end == len(equation)-1:
                equation[start+1:end+1] = str(int(equation[start+1:end+1]))