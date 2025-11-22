# Lab 4.1: DSPy Optimization

## Goal

Learn how to use **DSPy** to *program* your prompts instead of hand-tuning them. We will build a "Judge" module and optimize it using a small dataset of examples.

## Concepts

### 1. Signatures

Instead of a prompt string, you define a function signature:
`InputField -> OutputField`

```python
class AssessRisk(dspy.Signature):
    """Assess the risk level of a finding."""
    finding = dspy.InputField()
    risk_level = dspy.OutputField(desc="High, Medium, or Low")
```

### 2. Modules

A `dspy.Module` uses signatures to process data. `dspy.ChainOfThought` is a common module that adds "Let's think step by step" logic automatically.

### 3. Teleprompters (Optimizers)

The magic of DSPy. The `BootstrapFewShot` optimizer takes your module and a training set, and *compiles* a new prompt that includes the best few-shot examples to maximize performance.

## Instructions

1. **Open `lab_4_1_starter.py`**.
2. **Step 1**: Define the `SecurityJudge` signature.
3. **Step 2**: Create a small training set (3-4 examples of Finding -> Risk Level).
4. **Step 3**: Use `BootstrapFewShot` to compile the module.
5. **Step 4**: Compare the "Zero-Shot" output vs. the "Compiled" output.

## Resources

* [DSPy Documentation](https://dspy-docs.vercel.app/)
