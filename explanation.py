def explain(state, decision, signals):
    reasons = []

    if "high_stress" in signals:
        reasons.append("you expressed feeling overwhelmed, which increases cognitive load")

    if "low_energy" in signals:
        reasons.append("low energy reduces sustained attention")

    if "calm" in signals:
        reasons.append("a calm state helps gradual recovery")

    energy = state.mental_energy
    stress = state.stress_level
    focus = state.focus_capacity
    resistance = state.resistance_level

    if stress > 65:
        reasons.append("stress levels are still high")
    elif stress < 40:
        reasons.append("stress has reduced to a manageable level")

    if resistance > 60:
        reasons.append("high resistance suggests avoiding pressure")

    explanation = "Because " + " and ".join(reasons) + ",\n"
    explanation += f"the system recommends {decision['study'].lower()}."

    return explanation
