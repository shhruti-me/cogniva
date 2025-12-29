**Cogniva**: Mood-Aware Study & Music Recommender (Offline)

An offline, explainable cognitive-state–based system that adapts study strategies, break activities, and music vibes based on how a user feels — without using machine learning, external APIs, or cloud services.

This project prioritizes mental well-being, transparency, and ethical design over black-box prediction accuracy.

**Problem Statement**
Most productivity tools assume users are always cognitively ready to work. In reality, mental energy, stress, resistance, and focus fluctuate over time.
This project addresses the question:
How can a system responsibly recommend study behavior while respecting human cognitive limits, emotional state, and recovery needs — without relying on opaque ML models?

**Core Idea**
Instead of predicting “mood” or sentiment, the system models a multi-dimensional cognitive state and adapts recommendations over time using:

  Rule-based NLP (offline)
  Temporal decay
  Gradual recovery
  Safety overrides
  Explainable reasoning
  Reinforcement-style feedback (no ML)

**System Architecture**

User Input (Text)
        ↓
Text Analyzer (rule-based NLP + negation handling)
        ↓
Cognitive State Engine
  - Energy
  - Stress
  - Focus
  - Emotional Load
  - Resistance
  - Time Decay
        ↓
Decision Engine (priority rules + safety overrides)
        ↓
Explainability Layer (human-readable reasoning)
        ↓
Feedback Loop (adaptive thresholds)


All computation is local and deterministic.

**Key Features**

  **Cognitive State Modeling**    
        Persistent state across sessions
        Multiple dimensions (not just sentiment)
        Gradual recovery instead of instant resets
        Time-based decay using wall-clock time
  **Rule-Based NLP (Offline)**  
        Keyword-based signal detection
        Negation handling ("not stressed", "don't feel tired")
        Semantic exceptions (e.g., "don't feel like" → resistance)
        Conservative, safety-first interpretation
  **Decision Intelligence**
        Burnout and resistance prioritized over productivity
        Extreme-stress safety override
        Study styles adapt to cognitive readiness
        Music recommendations are vibes, not copyrighted tracks
  **Explainable AI (XAI)**
        Every recommendation includes a clear explanation:
        Which signals were detected
        What cognitive state influenced the decision
        Why a specific study mode was chosen
  **Adaptive Feedback (No ML)**
        User feedback (“Did this help?”)
        Thresholds adjust gradually
        Fully offline reinforcement logic

**Why This Project Avoids Machine Learning?**
  ML introduces opacity and bias
  Requires datasets and tuning
  Reduces user trust in mental-health-adjacent systems
  Hard to justify decisions
  For this domain, predictability and explainability are more important than marginal accuracy gains.

**Why Not Sentiment Analysis?**
Sentiment analysis collapses emotional state into a single score.
This system requires:
  Energy ≠ Emotion
  Stress ≠ Focus
  Motivation ≠ Readiness

A user can be positive but exhausted or negative but highly focused.
Sentiment analysis cannot model this.

<img width="692" height="364" alt="image" src="https://github.com/user-attachments/assets/f5adf0ef-b8fd-4181-8416-41d38432d53b" />



**How to Run**
python main.py

Then type how you feel, e.g.: I feel exhausted and overwhelmed

The system will respond with:
  Study style
  Break activity
  Music vibe
  Explanation
  Feedback prompt

**Example Output**

Detected signals: ['high_stress', 'resistance']

Recommendations:
Study style: No-pressure activity (very light review or rest)
Break activity: Grounding break (breathing, walk, hydration)
Music vibe: Very soft ambient / silence

Explanation:
Because you expressed high stress and strong resistance,
the system prioritizes recovery over productivity.

**Known Limitations**
  No sarcasm detection
  No long-range semantic reasoning
  Rule-based NLP has bounded understanding
  These limitations are explicitly acknowledged and intentional.

**Learning Outcomes**  
Human-centered system design
  Ethical AI principles
  Explainable decision systems
  State modeling without ML
  Real-world edge-case handling

**Disclaimer**
  This project is not a medical or mental health diagnostic tool.
  It is intended as a personal productivity and self-reflection aid only.

**Final Note**
This project demonstrates that responsible, transparent systems can be built without machine learning — and that sometimes, less automation leads to more trust.
