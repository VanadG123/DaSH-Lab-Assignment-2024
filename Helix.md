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
This means it can assign more demanding parts of the model to stronger GPUs and less demanding parts to weaker GPUs, optimizing the use of available resources. It is also able to redistribute
resources 
