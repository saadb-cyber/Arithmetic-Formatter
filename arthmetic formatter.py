MAX_NUM_OF_PROBLEMS = 5
MAX_OPERAND_LEN = 4

first_operands = list()
operators = list()
second_operands = list()
results = list()


def arithmetic_arranger(problems, show_results = True):
  process_input(problems)

  return build_output(show_results)


def process_input(problems):
  assert len(problems) <= MAX_NUM_OF_PROBLEMS, "ERROR: Too many problems"

  for problem in problems:
    parts = problem.split()

    assert len(parts) == 3, "ERROR: problems must have 2 operands and 1 operator"

    t1 = parts[0]
    op = parts[1]
    t2 = parts[2]

    assert t1.isnumeric() and t2.isnumeric(), "ERROR: operands must only contain digits"
    assert len(t1) <= MAX_OPERAND_LEN and len(t2) <= MAX_OPERAND_LEN, "ERROR: operands must not have more than " + MAX_OPERAND_LEN + " digits"
    assert op == "+" or op == "-", "ERROR: operator must be '+' or '-'"

    first_operands.append(t1)
    operators.append(op)
    second_operands.append(t2)
    result = ""
    if op == "+":
      result = str(int(t1) + int(t2))
    else: # we checked for + or - above
      result = str(int(t1) - int(t2))
    results.append(result)


def build_output(show_results):
  spacer = " " * 3
  line1 = ""
  line2 = ""
  dashes = ""
  line3 = ""

  for index in range(len(first_operands)):
    t1 = first_operands[index]
    op = operators[index]
    t2 = second_operands[index]
    result = results[index]
    width = max(len(t1), len(t2))

    line1 += spacer + " " + " " + t1.rjust(width)
    line2 += spacer + op + " " + t2.rjust(width)
    dashes += spacer + "-" * (width + 2)
    line3 += spacer + " " * (2 - len(result) + width) + result

  output = line1 + "\n" + line2 + "\n"
  if show_results:
    output += dashes + "\n" + line3 + "\n"
  return output


