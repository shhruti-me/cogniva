import json
import os

FEEDBACK_FILE = "data/feedback.json"

DEFAULT_WEIGHTS = {
    "recovery_bias": 0,
    "low_friction_bias": 0,
    "deep_focus_bias": 0
}

def load_feedback():
    if not os.path.exists(FEEDBACK_FILE):
        return DEFAULT_WEIGHTS.copy()

    try:
        with open(FEEDBACK_FILE, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return DEFAULT_WEIGHTS.copy()

def save_feedback(weights):
    os.makedirs("data", exist_ok=True)
    with open(FEEDBACK_FILE, "w") as f:
        json.dump(weights, f, indent=2)

def update_feedback(weights, mode, rating):
    # rating: 1=Yes, 2=Somewhat, 3=No
    delta = {1: 2, 2: 0, 3: -2}[rating]

    if mode == "recovery":
        weights["recovery_bias"] += delta
    elif mode == "low-friction":
        weights["low_friction_bias"] += delta
    elif mode == "deep-focus":
        weights["deep_focus_bias"] += delta

    return weights
