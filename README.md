# Smaller but Better: Self-Paced Knowledge Distillation for Lightweight yet Effective LCMs

This is the repository of our SODA framework.

## Dataset

We present partial data used in the three phases of SODA framework, as follows:

- Stage I: the correct and faulty knowledge for fine-tuning the student model is shown in [pairwise data](https://github.com/yujiachen99/SodaCoder/blob/main/datas/pairwise_data.json).
- Stage II: the scoring data for training the scoring model is shown in [scoring data](https://github.com/yujiachen99/SodaCoder/blob/main/datas/scoring_data.json).
- Stage III: the newly-generated seed knowledge is shown in [new data](https://github.com/yujiachen99/SodaCoder/blob/main/datas/new_data.json).

## Model

We use the [LLaMA-Factory library](https://github.com/hiyouga/LLaMA-Factory) for the training and inference process. 

## Code

We present the source code of the static tool which supports executing generated solutions with six programming languages (i.e., Python, Java, Javascript, C, C++ and Go) in [toolExecution](https://github.com/yujiachen99/SodaCoder/tree/main/toolExecution).

####  *We release partial data currently. We will release all code, data, and large code models after acceptance.*

