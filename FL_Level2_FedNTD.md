# FedNTD Paper

## FedAVG

Each device (called a client) trains its own version of the model using the data it has. After training, each client sends its model (not the data) back to a central server. The server
then combines these models by averaging them together. The average is weighted against the data on which it was trained, meaning that if a client has more data, its model
has a bigger influence on the final result.

## Data Heterogeneity

In an ideal world, the data on each device would look very similar (i.i.d., which means "independently and identically distributed"). This would make the averaging process simple and effective.
But in reality, the data on each client is often very different because people use their devices in unique ways. This difference in data is known as data heterogeneity.
Since each client’s data is different, the models they train can be very different too. When the server averages these models, the final combined model might not work as well as
expected because it doesn’t properly represent the overall, global data. This also leads to poor performance and may need to multiple rounds of communication between server and client to learn
properly which can lead to heavy costs if we are dealing with a high number of devices. 

### Catastrophic Forgetting 

This is a problem often encountered in Continual Learning in which the model is trained on multiple tasks in a sequential way, one after the other. Upon learning a new task, it updates its parameter
and since the data of each task can be really different it may lead to the model forgetting how to perform an older task by learning how to do the new one. This is a problem as in an ideal 
state, we want our model to remember how to do every task well. 

Something similar is experienced in Federated Learning Based Systems,  As the global model is updated round after round with data from different devices, the underlying data distributions might change significantly.
This change can cause the global model to forget important information from previous rounds, just like in continual learning. Researchers even observed that after a few rounds of updating 
the model started predicting wrongly for a class of data which it was earlier predicting well. This happens because the model forgets important information as it learns from new data
from different devices. 

## Knowledge Distillation 

It's a technique to make a simpler model (called the Student Model) learn from a more complicated model (called the Teacher Model). The student model's learning is guided by two main factors:
#### Cross-Entropy Loss (LCE): This is a standard way of measuring how well the model is predicting the right class.
#### Kullback-Leibler Divergence Loss (LKL): This measures how well the student model’s softened probabilities match the teacher’s.

The student model doesn't merely try to mimic the Teacher Model's answers, rather it tries to copy the soft probabilities of the teacher, which we get through a technique called temperatrue scaling. 

### Temperature Scaling 

Imagine you have a teacher model trained on the MNIST dataset, which contains images of handwritten digits (0-9).

Teacher’s Prediction (Without Scaling):
Digit 3: 0.98
Digit 8: 0.01
Digit 5: 0.01
The teacher is very confident that the digit is "3".

Teacher’s Prediction (With Temperature Scaling, τ = 2):
Digit 3: 0.60
Digit 8: 0.25
Digit 5: 0.15
With temperature scaling, the predictions are less confident. Now, when the student model learns, it pays more attention to the similarities between "3", "8", and "5", which helps it understand that these digits can look somewhat similar and improve its ability to classify them correctly. Thus, By softening the probabilities, the student model learns from a broader range of possibilities, which can improve its performance on new, unseen data.


