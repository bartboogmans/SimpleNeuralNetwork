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


# Another usecase: Estimating a surface
Lets say we estimate the surface:

given:

$$ r = \sqrt{x^2 + y^2} $$

then 

$$ z = \begin{cases} 
      \frac{\cos(r) + 1}{2} & \text{if } r < \pi \\
      0 & \text{otherwise}
   \end{cases} $$

Which is basically cylindrically symmetric a cosine-ish function near the origin and flat outside the radius $r>\pi$

cleancosinepic![cleanCosCone1](https://github.com/bartboogmans/SimpleNeuralNetwork/assets/5917472/fed39ca4-59cd-4ac9-8168-142fb63f264c)

First attempt gave:
![wrongsurfaceNotrainingset](https://github.com/bartboogmans/SimpleNeuralNetwork/assets/5917472/1b32cea1-564a-41fe-8d9e-9da86f3ea046)
Which was not really that nice. 

Although comparing with the training gave quite a good score in terms of error... Lets compare with the training set:

![withTrainingSetFaulty](https://github.com/bartboogmans/SimpleNeuralNetwork/assets/5917472/6fb09076-4b8c-44dd-8af5-45778afa2441)

This suggested that the training set was actually wrong! Looking back I found that i used $\frac{\cos(x) + 1}{2}$ instead of $\frac{\cos(r) + 1}{2}$

Correcting the training set gives:

![good2](https://github.com/bartboogmans/SimpleNeuralNetwork/assets/5917472/3807bf10-3bde-4ca0-b2ad-c7b4bbca50e8)

![good1](https://github.com/bartboogmans/SimpleNeuralNetwork/assets/5917472/759361d4-ef20-45d4-82e9-f98969ab1259)





