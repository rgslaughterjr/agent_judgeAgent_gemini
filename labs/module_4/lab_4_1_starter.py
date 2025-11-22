import dspy
from dspy.teleprompt import BootstrapFewShot

# Configure LM
# dspy.settings.configure(lm=dspy.OpenAI(model='gpt-4o'))

# --- Step 1: Define Signature ---
class SecurityJudge(dspy.Signature):
    """
    TODO: Define input (finding) and output (risk_level)
    """
    # finding = dspy.InputField()
    # risk_level = dspy.OutputField()
    pass

# --- Step 2: Define Module ---
class CoTJudge(dspy.Module):
    def __init__(self):
        super().__init__()
        # self.prog = dspy.ChainOfThought(SecurityJudge)
    
    def forward(self, finding):
        # return self.prog(finding=finding)
        pass

def run_lab_4_1():
    print("### Lab 4.1: DSPy Optimization ###")
    
    # Training Examples
    trainset = [
        # dspy.Example(finding="Open S3 bucket", risk_level="High").with_inputs("finding"),
        # ...
    ]
    
    # Compile
    # teleprompter = BootstrapFewShot(metric=dspy.evaluate.answer_exact_match)
    # compiled_judge = teleprompter.compile(CoTJudge(), trainset=trainset)
    
    # Test
    # pred = compiled_judge(finding="Hardcoded password in main.py")
    # print(f"Prediction: {pred.risk_level}")

if __name__ == "__main__":
    run_lab_4_1()
