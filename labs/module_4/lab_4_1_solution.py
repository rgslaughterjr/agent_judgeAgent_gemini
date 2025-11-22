import dspy
from dspy.teleprompt import BootstrapFewShot

# Configure LM (Assuming env var OPENAI_API_KEY is set)
try:
    lm = dspy.OpenAI(model='gpt-4o', max_tokens=100)
    dspy.settings.configure(lm=lm)
except Exception as e:
    print(f"Warning: Could not configure DSPy OpenAI: {e}")

# --- Step 1: Define Signature ---
class SecurityJudge(dspy.Signature):
    """Assess the risk level of a security finding."""
    finding = dspy.InputField(desc="The security issue found in the code or infrastructure")
    risk_level = dspy.OutputField(desc="Risk rating: High, Medium, or Low")

# --- Step 2: Define Module ---
class CoTJudge(dspy.Module):
    def __init__(self):
        super().__init__()
        self.prog = dspy.ChainOfThought(SecurityJudge)
    
    def forward(self, finding):
        return self.prog(finding=finding)

def run_lab_4_1():
    print("### Lab 4.1: DSPy Optimization (Solution) ###")
    
    # Training Examples (Small dataset)
    trainset = [
        dspy.Example(finding="Publicly accessible S3 bucket containing customer data", risk_level="High").with_inputs("finding"),
        dspy.Example(finding="Missing docstring in utility function", risk_level="Low").with_inputs("finding"),
        dspy.Example(finding="Use of deprecated API version", risk_level="Medium").with_inputs("finding"),
        dspy.Example(finding="Hardcoded AWS credentials in git repository", risk_level="High").with_inputs("finding"),
    ]
    
    # --- Step 3: Compile ---
    print("Compiling prompt with BootstrapFewShot...")
    # Simple metric: exact match (for demo purposes)
    def validate_risk(example, pred, trace=None):
        return example.risk_level.lower() == pred.risk_level.lower()

    teleprompter = BootstrapFewShot(metric=validate_risk, max_bootstrapped_demos=2)
    
    # Note: In a real scenario, you'd compile this once and save it.
    # Here we compile on the fly.
    compiled_judge = teleprompter.compile(CoTJudge(), trainset=trainset)
    
    # --- Step 4: Test ---
    test_finding = "SQL Injection vulnerability in login form"
    print(f"\nTesting finding: '{test_finding}'")
    
    pred = compiled_judge(finding=test_finding)
    print(f"Predicted Risk: {pred.risk_level}")
    print(f"Rationale: {pred.rationale}")

    # Inspect the prompt
    # lm.inspect_history(n=1)

if __name__ == "__main__":
    run_lab_4_1()
