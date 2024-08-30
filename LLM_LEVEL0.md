# LEVEL 0: SCHEDULER FOR LLM INTERFACING 

This is a summary of what I learnt from the article: https://jalammar.github.io/illustrated-gpt2/

The original transformer model is made up of an encoder and decoder – each is a stack of what we can call transformer blocks. 

Encoders:  Encoders process input data (like text, images, etc.) and convert it into a compact, fixed-size representation called an embedding or encoded representation. This captures the essential
information from the input in a way that the model can use for further processing. They do a context meaningful search and are by analyzing the tokens both to the right and to the left of the current
token. This is a key feature that differentiates Transformer-based models, like BERT, from traditional models. Some features include bi-directional contextual analysis, self-attention mechanism
and multi head attention.

Decoders: The decoder uses these encoded representations and, by attending to different parts of the input, generates the output sequence (e.g., the translated sentence). Some of its features 
include masked self attention, encoder-decoder layers (which allow the decoders to focus more on the relevants parts of encoder output), Feed-forward neural network, Linear layer and softmax.

A clear use is displayed in earlier language translation models and together, they form the backbone of many modern AI models, especially in natural language processing.

GPT-2 uses an only decoders model and is therefore, auto-regressive in nature, that is it generates one output token at a time by considering the previous token it has already generated. 

## WORKING OF GPT-2.0 

Step 1: Input Tokenization

The first step is to convert your input string into a format that the GPT-2 model can understand.

	•	Tokenization: The input string of 50 words is broken down into smaller units called tokens. Tokens can be words, subwords, or even single characters, depending on how the model was trained. For example, the sentence “The quick brown fox” might be tokenized into ["The", "quick", "brown", "fox"], but more commonly, it would be broken down further into subwords like ["The", "quick", "b", "rown", "fox"].
	•	Conversion to IDs: Each token is then converted into a corresponding numerical ID from the model’s vocabulary. This step translates your text into a sequence of numbers that the model can process.

Step 2: Embedding the Input

Once you have the token IDs, the next step is to embed them in a high-dimensional space.

	•	Embedding Layer: The token IDs are passed through an embedding layer, which converts each token ID into a dense vector of fixed size. For example, a token ID might be mapped to a 768-dimensional vector (this depends on the specific size of the GPT-2 model being used). These vectors capture semantic information about the words.

Step 3: Positional Encoding

Since the Transformer model (which GPT-2 is based on) doesn’t have a built-in understanding of the order of words, it needs to be explicitly told where each word is in the sequence.

	•	Positional Encoding: The model adds a positional encoding to each word’s embedding. This encoding is a vector that represents the position of the word in the sequence. By adding this positional information to the word embeddings, the model can distinguish between words based on their position in the input string.

Step 4: Passing Through the Transformer Layers

Now the model processes the input through multiple layers of the Transformer architecture. Each layer consists of two key components: self-attention and feed-forward networks. GPT-2 typically has 12, 24, or more layers, depending on the model size.

4.1 Self-Attention Mechanism

The self-attention mechanism allows the model to focus on different parts of the input sequence when making predictions. Here’s how it works:

	•	Query, Key, and Value Vectors: For each word in the input, the model generates three vectors—Query (Q), Key (K), and Value (V). These vectors are derived from the word embeddings.
	•	Attention Scores: The model calculates attention scores by taking the dot product of the Query vector of one word with the Key vectors of all other words in the sequence. This tells the model how much attention each word should give to every other word.
	•	Weighted Sum: The attention scores are used to compute a weighted sum of the Value vectors. This sum produces a new representation for each word that considers its context within the entire sequence.
	•	Masking: In GPT-2, which is auto-regressive, the model uses masking to ensure that predictions for the next word only depend on the words that have already been seen, not future words. The model masks out the attention scores for all positions beyond the current word, ensuring that it doesn’t “cheat” by looking ahead.

4.2 Feed-Forward Neural Network

After the self-attention step, the model passes the output through a feed-forward neural network (FFNN):

	•	Non-Linearity: The FFNN adds complexity to the model by applying a non-linear activation function, usually the Rectified Linear Unit (ReLU), to introduce non-linearities into the model’s processing. This helps the model capture more complex patterns in the data.
	•	Residual Connections: The model also uses residual connections, which means that the original input to the layer is added back to the output of the feed-forward network. This helps stabilize training and improves the flow of gradients during backpropagation.

Step 5: Generating the Next Word

Once the input has passed through all the layers of the Transformer, the model is ready to predict the next word.

	•	Output Layer: The final layer of the model outputs a vector for each position in the sequence. These vectors are then passed through a linear layer (fully connected layer) that maps them to the size of the vocabulary.
	•	Softmax Function: The output of the linear layer is a set of raw scores, known as logits, for each word in the vocabulary. The model applies the softmax function to these logits to convert them into probabilities. This gives the probability distribution over all possible next words in the vocabulary.
	•	Prediction: The word with the highest probability is selected as the next word in the sequence.

Step 6: Updating the Sequence

Once the next word is predicted:

	•	Appending the Word: The predicted word is added to the input sequence, making the sequence now 51 words long.
	•	Iterative Process: If you want to predict multiple words, the process repeats. The model takes the updated sequence (now with 51 words), processes it through all the layers again, and predicts the 52nd word, and so on.
