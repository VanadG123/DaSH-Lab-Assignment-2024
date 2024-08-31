# HELIX RESEARCH PAPER

This is my understanding and summary of what I understood from the Helix research paper.

The problem arrises with  most of today’s LLM serving systems targeting homogeneous GPU clusters, where all GPUs are of the same type and have identical memory capacity whereas modern cloud platforms
increasingly consist of a mix of GPU types. There have been prior attempts to resolve this problem however, most of them are designed for long-running training workloads and cannot adapt to LLM serving 
scenarios with realtime inference requests, for example in the case of a chatbots which demand rapid responses. This creates an opportunity for helix, but to understand that it is esssential
to understand how LLM are deployed:

## Breaking Down Large Language Models for GPUs

When we use large language models (LLMs), they are so big that they can't fit on a single computer's graphics card (GPU). A GPU is a powerful piece of hardware that helps the computer handle complex tasks, like running these models.
Because LLMs are too big for one GPU, we need to split them up and spread the work across multiple GPUs.

There are two main techniques to do this:
1) Tensor Model Parallelism: This is like taking a big math problem and dividing it into smaller chunks. Each chunk is then handled by a different GPU. Think of it like a group of people working together
   on a large puzzle—each person focuses on their own section of the puzzle.
2) Pipeline Model Parallelism: This is a bit like an assembly line in a factory. The model is broken into different stages, and each stage is handled by a different GPU. The data flows from one GPU to the
   next, similar to how a product moves along the assembly line, with each stage adding something new.

Model Placement: This is the process of deciding which part of the model should go on which GPU. It's like planning who does which task in a team so that the work gets done efficiently.

## How does Helix leverage Heterogeneous Clusters of GPUs 

So, Helix is able to leverage the difference in many factors such as networking between neighbouring GPUs, processing power, and memory when deciding how to split and place the model across the GPUs. 
This means it can assign more demanding parts of the model to stronger GPUs and less demanding parts to weaker GPUs, optimizing the use of available resources. It is also able to redistribute resources based on real-time performance. It is the only Existing heterogeneity-aware serving system which takes into account both GPU and network heterogeneit. The model uses 
MILP (Mixed Integer Linear Programming) to optimise and find the best way to distribute the large language model (LLM) tasks across GPUs. In this, it takes into account all the constraints
and iterates through all the possible iterations to find the best possible way.

## PER-REQUEST PIPELINE 

Existing systems generally employ a group of fixed pipelines and assign requests to these pipelines in a rather fixed manner. Using fixed pipelines is not flexible enough to accommodate
the heterogeneous compute and network conditions and often causes under-utilization. Instead, Helix introduces per-request pipelines, where each request is assigned its own pipeline and since the number of possible pipelines is huge, it has sufficient flexibilty to be able to find that out. An example to understand this:
Let’s say you have a cluster of GPUs, where:

GPU A is very fast at processing certain types of tasks but is slightly slower to communicate with others due to network conditions.
GPU B is slower but has a better network connection.
GPU C is balanced but currently very busy with other tasks.
Traditional systems might assign a request to a fixed pipeline that always involves GPU A, then B, then C. But if GPU C is busy or if GPU A’s network connection is currently slow, this fixed pipeline might not be the best choice. The request might get delayed, and other GPUs might be under-utilized.

Helix, on the other hand, will look at the current status and might decide that for this particular request, it’s better to skip GPU C and use GPUs A and B more efficiently. Or it might find an alternative path that involves different GPUs entirely. It considers every possible combination, effectively creating a unique pipeline for each request.

This allows helix to reduce delays and process requests more quickly, leading to more efficiency and outperforming its competitors. 

## INNER WORKING OF HELIX 

### Graph Representation of the Cluster:
Helix represents the entire cluster of GPUs and their connections as a graph. In this graph:

Nodes represent GPUs.
Edges represent the network connections between them.

When a request comes in, Helix identifies all possible paths from the starting point (where the request enters) to the end point (where the result is returned). Each of these paths represents a potential pipeline. The number of possible pipelines is huge, as it's equal to the number of different paths you can take from start to finish in the graph.

Helix evaluates these paths and selects the best one for each individual request, ensuring that it uses the GPUs and network connections as efficiently as possible.




