# SimpleNeuralNetwork
This is a C++ implement of simple neural network. It's based on video [Neural Net in C++ Tutorial](https://vimeo.com/19569529) by David Miller.
# Test in Ubuntu
1 Gernerate training data to slove XOR problem
```
    g++ ./makeTrainingSamples.cpp -o makeTrainingSamples
    ./makeTrainingSamples > out.txt
```
2 Test neural netwrok
```
    g++ ./neural-net.cpp -o neural-net
    ./neural-net
```
And you will get the result!



# Display results
Let the neural net output its results to a file instead:
```
    ./neural-net > results.txt
```

Use python to plot iteration number vs recent average error:
``` 
    python3 plot_simulation_results.py
```

![Figure_1](https://github.com/bartboogmans/SimpleNeuralNetwork/assets/5917472/dcb5eb31-ac09-4ebc-8213-6934ab3b3e02)
