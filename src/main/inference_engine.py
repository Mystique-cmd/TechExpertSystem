from knowledge_base import KnowledgeBase
from rule import Rule

class InferenceEngine:
    def __init__(self, knowledge_base):
        self.kb = knowledge_base

    def forward_chain(self):
        """
        Applies forward chaining to deduce all possible facts.
        """
        new_facts_added = True
        while new_facts_added:
            new_facts_added = False
            for rule in self.kb.get_rules():
                if self.rule_is_applicable(rule) and rule.conclusion not in self.kb.get_facts():
                    self.kb.add_fact(rule.conclusion)
                    new_facts_added = True
        return self.kb.get_facts()

    def backward_chain(self, goal):
        """
        Applies backward chaining to determine if a goal can be proven.
        """
        if goal in self.kb.get_facts():
            return True

        for rule in self.kb.get_rules():
            if rule.conclusion == goal:
                if all(self.backward_chain(condition) for condition in rule.conditions):
                    return True
        return False

    def rule_is_applicable(self, rule):
        """
        Checks if a rule is applicable given the current facts.
        """
        return all(condition in self.kb.get_facts() for condition in rule.conditions)

    def resolve_conflicts(self, applicable_rules):
        """
        Resolves conflicts between rules using a priority-based strategy.
        """
        return sorted(applicable_rules, key=lambda r: r.priority, reverse=True)
