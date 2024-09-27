如果连Prompt都不用写了，那么人力释放之后，我们又可以去充电（摸鱼）了。

自动化调优Prompt，听起来就很诱人，能否实现呢，效果又能达到什么程度呢？Let‘s see。

# Literature Review
伟大的研究来自于积累，而积累来自于分享（白嫖）。先看看是否有人已经做了这个课题，已经是否有成熟的工具。

## [自动优化Prompt：Automatic Prompt Engineering的3种方法](https://www.wehelpwin.com/article/4677)
APE(automatic prompt engineer)： Prompt Candidates Generation-> Prompt Selection-> Resample Prompt；
![workflow](/data/imgs/APE.png)
- Generate Prompts有两种模式：
  - Forward mode。常规生成模式，提供一些任务examples，让LLM在最后生成prompt。示例如下。
![alt text](/data/imgs/forward_mode.png)
  - Reverse mode。即insert模式，将待生成的prompt放到examples前面，让LLM用填空的方式写prompt。示例如下。
![alt text](/data/imgs/reverse_mode.png)
  
- Prompt Selection
在训练集上打分，并保留高分prompt, 打分方式有两种：

  - Execution accuracy。在训练集上执行prompt后，得到的任务metric（如Accuracy、F1等）
  - Log probability。不使用任务metric，而是评估生成desired answer的概率

实验表明，Execution accuracy的效果更好。

另外，这一步如果在全量训练集上评估，则开销非常大，因此作者提出一种multi-stage策略。大致思想是先在少量subset上评估，然后过滤掉比较差的，循环这一过程直到候选集足够小，此时再在全量训练集上进行评价、挑选。

- Resample Prompt
在高分prompt附近进行采样，模拟Monte-Carlo Search过程

这一步核心是尝试性地resample，生成语义相似的prompt，看看能否取得更好的效果。这一过程是可迭代的。

resample的工作仍然交由LLM，其prompt如下。
![alt text](/data/imgs/ape-resample.png)


## [Automatic Prompt Optimization With "Gradient Descent" and Beam Search](https://arxiv.org/abs/2305.03495)

![alt text](/data/imgs/api-flow.png)

这里是先有一个初始的prompt，然后给定一些error samples(init prompt)无法预测正确的，然后再让LLM给出当前prompt预测错误的原因，这一原因即文本形式的“gradient”。

生成gradient的prompt如下。