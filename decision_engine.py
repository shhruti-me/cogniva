def decide(state, weights):
    energy = state.mental_energy
    stress = state.stress_level
    focus = state.focus_capacity
    resistance = state.resistance_level
    # 0. Extreme stress override (safety-first)
    if state.stress_level > 80:
        return {
            "study": "No-pressure activity (very light review or rest)",
            "break": "Grounding break (breathing, walk, hydration)",
            "music": "Very soft ambient / silence",
            "mode": "recovery"
        }


    # 1. Burnout / overload (personalized threshold)
    if energy < (35 + weights.get("recovery_bias", 0)) and stress > 65:
        return {
            "study": "Passive revision (notes, summaries, videos)",
            "break": "10–15 min walk + water",
            "music": "Soft ambient / brown noise",
            "mode": "recovery"
        }

    # 2. High resistance (personalized)
    if resistance > (65 - weights.get("low_friction_bias", 0)):
        return {
            "study": "Micro-task (10–15 min, no pressure)",
            "break": "Gentle reset (breathing / stretching)",
            "music": "Warm instrumental / calm piano",
            "mode": "low-friction"
        }

    # 3. Deep focus (personalized)
    if (
        energy > (70 - weights.get("deep_focus_bias", 0))
        and focus > 65
        and stress < 50
    ):
        return {
            "study": "Deep work (50–10 Pomodoro)",
            "break": "Short stretch, no phone",
            "music": "Instrumental lo-fi / cinematic focus",
            "mode": "deep-focus"
        }

    # 4. Default balanced mode
    return {
        "study": "Structured study (25–5 Pomodoro)",
        "break": "Light movement",
        "music": "Low-volume instrumental",
        "mode": "balanced"
    }
