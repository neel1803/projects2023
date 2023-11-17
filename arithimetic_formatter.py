def arithmetic_arranger(problems, solver = False):
    # Final Variables
    
    top_number = ""
    bottom_number = ""
    lines = ""
    solution_number =  ""
    resolutions = ""
    
    # First Check after the FOR loop
    
    if len(problems) > 5:
        return "Error: Too many problems."

    #Core FOR Loop
    
    for problem in problems:
        first_number = ""
        operator = ""
        second_number = ""
        first_number = problem.split()[0]
        operator = problem.split()[1]
        second_number = problem.split()[2]
        
        # Checking if the operators are valid
        
        if first_number.isdigit() and second_number.isdigit():
          if len(first_number) > 4 or len(second_number) > 4:
            return "Error: Numbers cannot be more than four digits."

        else:
          return "Error: Numbers must only contain digits."

        solution = ""

        if operator == "+":
          solution = str(int(first_number) + int(second_number))
        elif operator == "-":
          solution = str(int(first_number) - int(second_number))
        else:
          return "Erorr: Operator must be '+' or '-'."
  
    #Distance comprobation

        distance =  max(len(first_number), len(second_number)) + 2

    #Items Padding

        if problem != problems[-1]:
            top_number = top_number + str(first_number.rjust(distance)) + "    "
            bottom_number = bottom_number + operator + str(second_number.rjust(distance - 1)) + "    "
            lines = lines + "-" * (distance) + "    "
            solution_number = solution_number + solution.rjust(distance) + "    "
        else:
          top_number = top_number + str(first_number.rjust(distance))
          bottom_number = bottom_number + operator + str(second_number.rjust(distance - 1))
          lines = lines + "-" * (distance)
          solution_number = solution_number + solution.rjust(distance)


    #Solver comprobation


    if solver:
      resolutions = top_number + "\n" + bottom_number + "\n" + lines + "\n" + solution_number
    else:
      resolutions = top_number + "\n" + bottom_number + "\n" + lines
    return resolutions
