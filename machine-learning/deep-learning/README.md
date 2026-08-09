# Deep Learning

Neural network fundamentals. Depth needed depends on the role — for AI lab roles
this is the on-ramp to [../../llm-post-training/](../../llm-post-training/).

## Checklist

**Fundamentals**
- [ ] Perceptron → MLP → universal approximation theorem (and why it's less useful than it sounds)
- [ ] Forward pass, loss, backward pass, parameter update
- [ ] **Backpropagation** — be able to derive it via the chain rule for a 2-layer net
- [ ] Computational graphs and automatic differentiation
- [ ] Weight initialization: Xavier/Glorot, He — and why zero init fails

**Activations**
- [ ] Sigmoid, tanh, and the vanishing gradient problem
- [ ] ReLU, dying ReLU, Leaky ReLU, ELU, GELU, SwiGLU
- [ ] Softmax and its numerical stability trick (subtract the max)

**Training**
- [ ] Optimizers: SGD, momentum, Nesterov, RMSprop, Adam, AdamW
- [ ] Adam vs AdamW — decoupled weight decay, and why it matters
- [ ] Learning rate schedules: step, cosine, warmup, one-cycle
- [ ] Batch size effects on generalization and on the learning rate you should use
- [ ] Gradient clipping; exploding gradients
- [ ] Batch norm vs layer norm vs RMS norm — and why transformers use layer/RMS norm
- [ ] Dropout, and why it behaves differently at train and inference time

**Architectures**
- [ ] **CNNs**: convolution, stride, padding, pooling, receptive field, parameter sharing
- [ ] Classic CNN lineage: ResNet (skip connections and why they fix depth), Inception, EfficientNet
- [ ] **RNNs**: sequence modeling, vanishing gradients through time, BPTT
- [ ] LSTM and GRU gating; what each gate does
- [ ] **Transformers**: self-attention, multi-head, positional encoding, encoder vs decoder
- [ ] Why attention replaced recurrence (parallelism, path length between tokens)
- [ ] Embeddings: word2vec, GloVe, contextual embeddings

**Practice**
- [ ] Transfer learning and fine-tuning; which layers to freeze
- [ ] Data augmentation by modality
- [ ] Regularization: weight decay, early stopping, label smoothing, mixup
- [ ] Debugging: overfit a single batch first — the single best sanity check
- [ ] Mixed precision; fp16 vs bf16
- [ ] Distributed training: data vs model parallelism

## The debugging ladder

When a network won't train, in order:

1. **Overfit one batch to ~zero loss.** If you can't, the bug is in the model,
   loss, or data pipeline — not the hyperparameters.
2. Check the data: labels aligned, normalization applied, no shuffling bug.
3. Check the loss: right function, right reduction, right shapes.
4. Check gradient flow: any layer with zero or NaN gradients.
5. *Then* tune the learning rate.

Reaching for the learning rate at step 1 is the most common wasted week in
applied deep learning, and interviewers ask this specifically to see if you know
the order.

## Questions to be ready for

- Derive backprop for a two-layer network.
- Why do ResNets let you train 100+ layers?
- Batch norm vs layer norm — why do transformers use layer norm?
- Your loss is NaN at step 50. Diagnose it.
- Why did attention replace recurrence?
- Adam vs SGD — when is plain SGD with momentum actually better?
- Your model overfits with 1000 examples. Five options, ordered by what you'd try first.

## Video courses

- [Stanford CS230 — Deep Learning](https://www.youtube.com/playlist?list=PLoROMvodv4rNRRGdS0rBbXOUGA0wjdh1X)
  (Autumn 2025) — architectures and training practice, including the debugging
  discipline above.
- [Stanford CS224N — NLP with Deep Learning](https://www.youtube.com/playlist?list=PLoROMvodv4rOaMFbaqxPDoLWjDaRAdP9D)
  (Spring 2024, Manning) — the path from word vectors through attention to
  transformers. Watch this before post-training: it explains *why* attention
  replaced recurrence instead of just asserting it, which is the version of the
  answer interviewers are listening for.

## Next

For transformer internals and everything downstream of pretraining, continue to
[../../llm-post-training/fundamentals/](../../llm-post-training/fundamentals/).

## Notes

_Add your own notes here._
