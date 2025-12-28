import re
NEGATIONS = ["not", "don't", "dont", "never", "no", "hardly", "rarely"]

SIGNALS = {
    "low_energy": {
        "keywords": ["tired", "sleepy", "exhausted", "drained", "fatigued"],
        "delta": {"mental_energy": -20, "focus_capacity": -10}
    },
    "high_stress": {
        "keywords": ["anxious", "overwhelmed", "pressure", "stressed", "panic"],
        "delta": {"stress_level": 25, "emotional_load": 15}
    },
    "resistance": {
    "keywords": [
        "don't feel like",
        "dont feel like",
        "can't start",
        "cannot start",
        "avoiding",
        "procrastinating"
    ],
    "delta": {"resistance_level": 30, "focus_capacity": -10},
    "force": True
},
    "motivation": {
        "keywords": ["ready", "focused", "motivated", "confident"],
        "delta": {"focus_capacity": 20, "mental_energy": 10}
    },
    "calm": {
        "keywords": ["calm", "okay", "fine", "relaxed", "peaceful"],
        "delta": {"stress_level": -10, "emotional_load": -10}
    }
}

def analyze_text(text):
    text = text.lower()
    text = text.replace("’", "'")  # normalize smart quotes

    applied_deltas = {}
    matched_signals = []

    for signal, config in SIGNALS.items():
        for kw in config["keywords"]:
            force_apply = config.get("force", False)
            if kw in text:
                #  NEGATION CHECK
                if is_negated(text, kw):
                    continue

                matched_signals.append(signal)
                for k, v in config["delta"].items():
                    applied_deltas[k] = applied_deltas.get(k, 0) + v
                break

    return applied_deltas, matched_signals

    
def is_negated(text, keyword, window=10):
    idx = text.find(keyword)
    if idx == -1:
        return False

    context = text[max(0, idx - window):idx]
    return any(neg in context.split() for neg in NEGATIONS)
