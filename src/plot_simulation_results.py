import matplotlib.pyplot as plt

def parse_simulation_results(filename):
    passes = []
    errors = []
    
    with open(filename, 'r') as file:
        for line in file:
            if line.startswith("Pass"):
                pass_num = int(line.split(':')[0][4:])
            elif line.startswith("Net recent average error"):
                error = float(line.split(': ')[1])
                passes.append(pass_num)
                errors.append(error)
    return passes, errors

def plot_errors(passes, errors):
    plt.figure(figsize=(10, 6))
    plt.plot(passes, errors, marker='')
    plt.title('Net Recent Average Error Over Passes of z=XOR(x,y) training data')
    plt.xlabel('Pass Number')
    plt.ylabel('Net Recent Average Error')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    filename = 'results.txt'  # Replace with your actual file name
    passes, errors = parse_simulation_results(filename)
    plot_errors(passes, errors)
