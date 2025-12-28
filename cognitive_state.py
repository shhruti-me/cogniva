import json
import os
import time

STATE_FILE = "data/user_state.json"


class CognitiveState:
    def __init__(self):
        # Core cognitive dimensions
        self.mental_energy = 60
        self.emotional_load = 40
        self.stress_level = 40
        self.focus_capacity = 60
        self.resistance_level = 30

        # Timestamp for time decay
        self.last_updated = time.time()

    # -------------------------
    # Utility
    # -------------------------
    def clamp(self):
        for attr in vars(self):
            val = getattr(self, attr)
            if isinstance(val, (int, float)):
                setattr(self, attr, max(0, min(100, val)))

    # -------------------------
    # Apply deltas from text analysis
    # -------------------------
    def apply_delta(self, **changes):
        for key, delta in changes.items():
            if hasattr(self, key):
                setattr(self, key, getattr(self, key) + delta)
        self.clamp()
        self.last_updated = time.time()

    # -------------------------
    # Natural recovery (when no strong signals)
    # -------------------------
    def natural_recovery(self):
        self.stress_level -= 5
        self.emotional_load -= 4
        self.resistance_level -= 3
        self.mental_energy += 4
        self.focus_capacity += 3
        self.clamp()
        self.last_updated = time.time()

    # -------------------------
    # Time decay (hours-based)
    # -------------------------
    def apply_time_decay(self):
        now = time.time()
        elapsed_hours = (now - self.last_updated) / 3600

        if elapsed_hours <= 0:
            return

        # Decay / recovery rates per hour
        self.stress_level -= 6 * elapsed_hours
        self.emotional_load -= 5 * elapsed_hours
        self.resistance_level -= 4 * elapsed_hours

        self.mental_energy += 4 * elapsed_hours
        self.focus_capacity += 3 * elapsed_hours

        self.clamp()
        self.last_updated = now

    # -------------------------
    # Persistence
    # -------------------------
    def to_dict(self):
        return vars(self)

    def load(self):
        if not os.path.exists(STATE_FILE):
            return

        try:
            with open(STATE_FILE, "r") as f:
                data = json.load(f)
                for k, v in data.items():
                    if hasattr(self, k):
                        setattr(self, k, v)
        except json.JSONDecodeError:
            # Corrupted or empty file → ignore safely
            pass

    def save(self):
        os.makedirs("data", exist_ok=True)
        with open(STATE_FILE, "w") as f:
            json.dump(self.to_dict(), f, indent=2)
