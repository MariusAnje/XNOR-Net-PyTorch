"""
xnor.0.weight (192, 3, 5, 5)
xnor.3.conv.weight (160, 192, 1, 1)
xnor.4.conv.weight (96, 160, 1, 1)
xnor.6.conv.weight (192, 96, 5, 5)
xnor.7.conv.weight (192, 192, 1, 1)
xnor.8.conv.weight (192, 192, 1, 1)
xnor.10.conv.weight (192, 192, 3, 3)
xnor.11.conv.weight (192, 192, 1, 1)
xnor.13.weight (10, 192, 1, 1)
"""

1. Why weights are more important than bias?
    weights are multiplications
    weights handle with inputs while bias are always the same for all data

one   [conv1, 1] [conv2, 0] [conv3, 0] [con4, 0] 
point [conv1, 984] [conv2, 2481] [conv3, 167] [conv4, ]
"""
xnor.0.weight (192, 3, 5, 5)
xnor.0.bias (192,)
xnor.1.running_mean (192,)
xnor.1.running_var (192,)
xnor.1.num_batches_tracked ()
xnor.3.bn.weight (192,)
xnor.3.bn.bias (192,)
xnor.3.bn.running_mean (192,)
xnor.3.bn.running_var (192,)
xnor.3.bn.num_batches_tracked ()
xnor.3.conv.weight (160, 192, 1, 1)
xnor.3.conv.bias (160,)
xnor.4.bn.weight (160,)
xnor.4.bn.bias (160,)
xnor.4.bn.running_mean (160,)
xnor.4.bn.running_var (160,)
xnor.4.bn.num_batches_tracked ()
xnor.4.conv.weight (96, 160, 1, 1)
xnor.4.conv.bias (96,)
xnor.6.bn.weight (96,)
xnor.6.bn.bias (96,)
xnor.6.bn.running_mean (96,)
xnor.6.bn.running_var (96,)
xnor.6.bn.num_batches_tracked ()
xnor.6.conv.weight (192, 96, 5, 5)
xnor.6.conv.bias (192,)
xnor.7.bn.weight (192,)
xnor.7.bn.bias (192,)
xnor.7.bn.running_mean (192,)
xnor.7.bn.running_var (192,)
xnor.7.bn.num_batches_tracked ()
xnor.7.conv.weight (192, 192, 1, 1)
xnor.7.conv.bias (192,)
xnor.8.bn.weight (192,)
xnor.8.bn.bias (192,)
xnor.8.bn.running_mean (192,)
xnor.8.bn.running_var (192,)
xnor.8.bn.num_batches_tracked ()
xnor.8.conv.weight (192, 192, 1, 1)
xnor.8.conv.bias (192,)
xnor.10.bn.weight (192,)
xnor.10.bn.bias (192,)
xnor.10.bn.running_mean (192,)
xnor.10.bn.running_var (192,)
xnor.10.bn.num_batches_tracked ()
xnor.10.conv.weight (192, 192, 3, 3)
xnor.10.conv.bias (192,)
xnor.11.bn.weight (192,)
xnor.11.bn.bias (192,)
xnor.11.bn.running_mean (192,)
xnor.11.bn.running_var (192,)
xnor.11.bn.num_batches_tracked ()
xnor.11.conv.weight (192, 192, 1, 1)
xnor.11.conv.bias (192,)
xnor.12.running_mean (192,)
xnor.12.running_var (192,)
xnor.12.num_batches_tracked ()
xnor.13.weight (10, 192, 1, 1)
xnor.13.bias (10,)
"""
