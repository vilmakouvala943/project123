import random

def get_random_python_code():
    """
    Generates a random Python code string
    :return: A random Python code string
    """
    python_keywords = ["if", "else", "while", "for", "in", "range"]
    python_functions = ["len", "sum", "max", "min", "sorted"]

    # Generate a random function name
    function_name = f"func_{random.randint(100, 999)}"

    # Generate a random list of arguments
    num_args = random.randint(1, 5)
    args = [f"arg{i}" for i in range(num_args)]

    # Generate a random body of the function
    body = ""
    for _ in range(random.randint(3, 8)):
        keyword = random.choice(python_keywords)
        if keyword == "if":
            body += f"{keyword} {random.choice(args)} > 0:\n" \
                    f"\tprint('{function_name}(', end='')\n" \
                    f"\tfor i in range({random.randint(1, 10)})" \
                    f":\n" \
                    f"\t\tprint('{random.choice(args)}, ', end='')'\n" \
                    f"\tprint(')')\n"
        elif keyword == "else":
            body += f"{keyword} print('{function_name}(', end='')\n" \
                    f"\tfor i in range({random.randint(1, 10)})" \
                    f":\n" \
                    f"\t\tprint('{random.choice(args)}, ', end='')'\n" \
                    f"\tprint(')')\n"
        elif keyword == "while":
            body += f"{keyword} {random.choice(args)} > 0:\n" \
                    f"\t{random.choice(python_functions)}({random.randint(1, 10)})" \
                    f"\n\tprint('{function_name}(', end='')\n" \
                    f"\tfor i in range({random.randint(1, 10)})" \
                    f":\n" \
                    f"\t\tprint('{random.choice(args)}, ', end='')'\n" \
                    f"\tprint(')')\n"
        elif keyword == "for":
            body += f"{keyword} i in range({random.randint(1, 10)}):\n" \
                    f"\tprint('{function_name}(', end='')\n" \
                    f"\tfor j in range({random.randint(1, 10)})" \
                    f":\n" \
                    f"\t\tprint('{random.choice(args)}, ', end='')'\n" \
                    f"\tprint(')')\n"
        elif keyword == "in":
            body += f"{keyword} {random.choice(args)} in range({random.randint(1, 10)}):\n" \
                    f"\tprint('{function_name}(', end='')\n" \
                    f"\tfor i in range({random.randint(1, 10)})" \
                    f":\n" \
                    f"\t\tprint('{random.choice(args)}, ', end='')'\n" \
                    f"\tprint(')')\n"
        elif keyword == "range":
            body += f"{keyword} {random.randint(1, 10)}:\n" \
                    f"\tprint('{function_name}(', end='')\n" \
                    f"\tfor i in range({random.randint(1, 10)})" \
                    f":\n" \
                    f"\t\tprint('{random.choice(args)}, ', end='')'\n" \
                    f"\tprint(')')\n"
        else:
            body += f"{keyword} {random.randint(1, 10)}:\n" \
                    f"\tprint('{function_name}(', end='')\n" \
                    f"\tfor i in range({random.randint(1, 10)})" \
                    f":\n" \
                    f"\t\tprint('{random.choice(args)}, ', end='')'\n" \
                    f"\tprint(')')\n"

    # Generate a random return statement
    return_statement = f"return {function_name}({', '.join(args)})"

    code = f"def {function_name}({', '.join(args)}):\n" \
           f"\t{body}\n" \
           f"\t{return_statement}"

    return code
