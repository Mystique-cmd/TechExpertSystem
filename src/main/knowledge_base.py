from rule import Rule


class KnowledgeBase:
    def __init__(self):
        self.facts = set()
        self.rules = []

    def add_fact(self, fact):
        """Adds a fact to the knowledge base."""
        self.facts.add(fact)

    def add_rule(self, rule):
        """Adds a rule to the knowledge base."""
        self.rules.append(rule)

    def get_facts(self):
        """Returns all facts in the knowledge base."""
        return self.facts

    def get_rules(self):
        """Returns all rules in the knowledge base."""
        return self.rules
