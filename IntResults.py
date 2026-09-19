class InterventionDecision(str, Enum):
    PASS = "pass"
    MODIFY = "modify"
    CLARIFY = "clarify"
    CONSTRAIN = "constrain"
    REFUSE = "refuse"
    HUMAN_REVIEW = "human_review"
