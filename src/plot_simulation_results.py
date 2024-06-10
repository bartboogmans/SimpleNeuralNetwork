import matplotlib.pyplot as plt
import numpy as np

def parse_simulation_results(filename):
    passes = []
    errors = []
    topology = None
    x_data = []
    y_data = []
    z_data = []
    
    with open(filename, 'r') as file:
        data_section = False
        for line in file:
            if data_section==False:
                if line.startswith("Pass"):
                    pass_num = int(line.split(':')[0][4:])
                elif line.startswith("Net recent average error"):
                    error = float(line.split(': ')[1])
                    passes.append(pass_num)
                    errors.append(error)
                elif line.startswith("Topology"):
                    topology = line.split(': ')[1].strip()
                    data_section = True                    
            else:
                x, y, z = map(float, line.split(','))
                x_data.append(x)
                y_data.append(y)
                z_data.append(z)    


    
    print("topology:", topology)
    return passes, errors, topology, x_data, y_data, z_data

def plot_errors(passes, errors, topology):
    plt.figure(figsize=(10, 6))
    plt.plot(passes, errors, marker='')
    title = 'Net Recent Average Error Over Passes of z=XOR(x,y) training data'
    if topology:
        title += f' (Topology: {topology})'
    plt.title(title)
    plt.xlabel('Pass Number')
    plt.ylabel('Net Recent Average Error')
    plt.grid(True)
    plt.show()

def plot_surface(x_data, y_data, z_data, x_train, y_train, z_train):
    fig = plt.figure(figsize=(10, 6))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_trisurf(x_data, y_data, z_data, cmap='viridis', alpha=0.7)
    ax.scatter(x_train, y_train, z_train, color='r', marker='o')
    ax.view_init(elev=50, azim=118)  # Set the elevation and azimuth
    ax.set_title('Surface Plot of x, y, z Data with Training Points')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.show()

def parse_training_data(filename):
    x_train = []
    y_train = []
    z_train = []
    
    with open(filename, 'r') as file:
        lines = file.readlines()
        for line in lines:
            if line.startswith("in:"):
                x, y = map(float, line.split(': ')[1].split())
                x_train.append(x)
                y_train.append(y)
            elif line.startswith("out:"):
                z = float(line.split(': ')[1])
                z_train.append(z)
    
    return x_train, y_train, z_train


if __name__ == "__main__":
    filename = 'results.txt'  # Replace with your actual file name
    training_filename = 'trainingData.txt'  # Replace with your actual file name
    passes, errors, topology, x_data, y_data, z_data = parse_simulation_results(filename)
    # print numpasses, len(x_data), len(y_data), len(z_data)
    print("passes: ",len(passes)," len(x_data):", len(x_data), "len(y_data):", len(y_data), "len(z_data):", len(z_data))
    x_train, y_train, z_train = parse_training_data(training_filename)
    plot_errors(passes, errors, topology)

    # thin out the training data up to a length of 1000
    x_train = x_train[:1000]
    y_train = y_train[:1000]
    z_train = z_train[:1000]

    plot_surface(x_data, y_data, z_data, x_train, y_train, z_train)

    # also plot surface without training data
    plot_surface(x_data, y_data, z_data, [], [], [])

    # Generate 3d data for the reference surface z = cos(r-1)/2 if r<pi else zero, r=sqrt(x^2+y^2)
    # Define the grid
    axislims = 6.0
    numgrid = 40
    x = np.linspace(-axislims, axislims, numgrid)
    y = np.linspace(-axislims, axislims, numgrid)
    x, y = np.meshgrid(x, y)

    # Calculate r
    r = np.sqrt(x**2 + y**2)

    # Calculate z based on the condition
    z = np.where(r < np.pi, (np.cos(r)+1) / 2, 0)

    # Plotting
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(x, y, z, cmap='viridis')

    # Set labels
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    # Show plot
    plt.show()