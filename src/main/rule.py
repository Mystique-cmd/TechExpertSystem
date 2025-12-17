class Rule:
    def __init__(self, rule_id, priority, conditions, conclusion):
        """
        Initializes a rule.

        Args:
            rule_id (str): The ID of the rule.
            priority (int): The priority of the rule, used for conflict resolution.
            conditions (list): A list of conditions (facts) that must be true for the rule to fire.
            conclusion (str): The fact that is concluded if the conditions are met.
        """
        self.rule_id = rule_id
        self.priority = priority
        self.conditions = conditions
        self.conclusion = conclusion

    def __repr__(self):
        return f"{self.rule_id}: IF {' AND '.join(self.conditions)} THEN {self.conclusion}"
