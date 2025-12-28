from cognitive_state import CognitiveState
from text_analyzer import analyze_text
from decision_engine import decide
from explanation import explain
from feedback import load_feedback

state = CognitiveState()
state.load()
state.apply_time_decay()


user_input = input("How are you feeling right now?\n> ")

deltas, signals = analyze_text(user_input)

if deltas:
    state.apply_delta(**deltas)
else:
    state.natural_recovery()

state.save()

weights = load_feedback()
decision = decide(state, weights)

print("\nDetected signals:", signals)

print("\nCognitive state:")
for k, v in state.to_dict().items():
    print(f"- {k}: {v}")

print("\nRecommendations:")
print("Study style:", decision["study"])
print("Break activity:", decision["break"])
print("Music vibe:", decision["music"])
explanation = explain(state, decision, signals)

print("\nExplanation:")
print(explanation)
