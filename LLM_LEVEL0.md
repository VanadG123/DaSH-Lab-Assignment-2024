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

## A GOOD EXAMPLE TO UNDERSTAND SELF-ATTENTION MECHANISM

 Consider the sentence: “The cat sat on the mat.”

 	1.	Query Vector (Q): The Query vector represents the current word or token that the model is focusing on. For example, if the model is currently processing the word “cat,” the Query vector will encode what the model wants to know about “cat” in relation to the other words in the sentence.
	2.	Key Vector (K): The Key vector is generated for every word in the sentence. It acts like a descriptor that other tokens use to determine how relevant this word is to their current focus. For example, if the current word is “cat,” it will compare its Query vector with the Key vectors of other words (like “The” and “sat”) to figure out how much attention to give to each word.
	3.	Value Vector (V): The Value vector is the actual information or “content” associated with each word. Once the attention mechanism has determined which words are important (based on the Query-Key comparison), the Value vectors of those words are combined to form the final output.

	Step 1: Generate Query, Key, and Value Vectors
	For the word “cat”:
	The model generates a Query vector (Q) for “cat.”
	It also generates Key (K) and Value (V) vectors for every word in the sentence, including “The,” “sat,” “on,” “the,” and “mat.”
	Step 2: Compare Query with Keys
	The model compares the Query vector for “cat” with the Key vectors of every other word in the sentence. This comparison is usually done by taking the dot product between the Query and each Key.
	For example:
	Query(“cat”) ⋅ Key(“The”)
	Query(“cat”) ⋅ Key(“sat”)
	Query(“cat”) ⋅ Key(“on”)
	Query(“cat”) ⋅ Key(“the”)
	Query(“cat”) ⋅ Key(“mat”)
	These comparisons result in attention scores, which indicate how much attention “cat” should pay to each word in the sentence.
	Step 3: Apply Attention to Value Vectors
	The attention scores from Step 2 are used to weigh the Value vectors of each word. The Value vector contains the actual content or information that will be passed on to the next layer.
	If the attention score between “cat” and “sat” is high, the Value vector for “sat” will have a greater influence on the final output.
	Step 4: Combine the Value Vectors
	The model takes the weighted sum of the Value vectors based on the attention scores. This combined vector becomes the new representation of the word “cat,” enriched with information from the surrounding words.

Breaking Down the Differences:

	•	Key Vector (K): Think of this as a description of what each word is about. It’s used to determine how relevant a word is to the current word being processed (e.g., “cat”).
	•	Example: If “sat” has a Key vector that is very similar to the Query vector for “cat,” the model will conclude that “sat” is important for understanding “cat.”
	•	Value Vector (V): This is the actual information that gets passed along. Once the model decides that “sat” is important for understanding “cat,” it will use the Value vector of “sat” to modify the representation of “cat.”
	•	Example: If the Value vector of “sat” contains information about the action, that information will be incorporated into the final representation of “cat.”

Final Recap:

	•	Key (K): Used to measure relevance. It helps the model decide which other words to pay attention to.
	•	Value (V): Contains the information that will be passed along. Once relevance is determined, the Value vector is used to update the word representation.

## KV CACHE

When you're interacting with a large language model (LLM), the model doesn't just think about the current word or sentence— it remembers everything that's been said before in the conversation. This memory is essential because the model uses it to understand context and generate appropriate responses. In technical terms, this memory is stored in KV Cache, So, as the conversation gets longer, the amount of information the model needs to store keeps growing, and this requires more and more memory. There have been some different approaches used to tackle this challenges of high memory demand and resource management in large language models (LLMs). A few of them being: 

### Orca’s Iteration-Level Scheduling
When LLMs process multiple requests at once, they often group these requests into a "batch." In traditional systems, even if one request in the batch finishes early, the resources assigned to it (like GPU memory or processing power) can't be used for anything else until the entire batch is done. This leads to resource retention—resources are held up and wasted because they're waiting for the slower requests in the same batch to finish. Orca introduces a smarter way to handle this called iteration-level scheduling.

Dynamic Batch Updates: Instead of sticking to the same batch from start to finish, Orca checks the status of each request after every iteration. If a request completes its task (or finishes generating a response), Orca removes it from the batch. This way, the system isn’t holding onto resources that are no longer needed for that request.

Resource Reallocation: Once a request finishes, the resources (like memory and processing power) that were allocated to it are immediately freed up. Orca can then reallocate these resources to other tasks or requests that still need more processing.

### vLLM’s PagedAttention
In traditional systems, memory is often allocated in the form of large, contiguous memory blocks which is like a single large sheet of paper where all the memory is stored sequentialy,this leads to certain technical challenges such as Fragmentation where Fragmentation occurs when you have free space scattered throughout the memory that is too small to be useful. It is like having small gaps in your sheet of paper that you can’t use efficiently because they’re not big enough to fit the new data. This leads to inefficient use of memory. It also leads leads to Allocation Overhead where allocating large, contiguous blocks of memory can become increasingly difficult as memory usage grows. If your system’s memory is heavily fragmented, finding a large enough block to store new data becomes challenging, leading to potential delays and increased overhead in managing memory. 
vLLM's PagedAttention uses a different approach by breaking memory into smaller, fixed-size blocks called pages. By breaking memory into smaller, uniform pages and allocating these pages only when necessary, PagedAttention ensures that memory is used efficiently and effectively, reducing waste and improving the overall performance of the system. This approach is particularly valuable when dealing with the high and growing memory demands of long conversations or multiple simultaneous requests. 

### multi-query and groupquery attention
In traditional systems, every time the model thinks about a new word (token), it stores a lot of information (KV Cache). This can lead to huge memory demands as more words are added.
Multi-Query and Group-Query Attention are like smarter note-taking methods. Instead of writing down a ton of details for each word, they find ways to summarize or group information so that the notes (KV Cache) take up less space. This reduces the amount of memory needed without losing important details, making the whole process more efficient.
