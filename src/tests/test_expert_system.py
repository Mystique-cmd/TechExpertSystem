import unittest
from src.main.knowledge_base import KnowledgeBase
from src.main.rule import Rule
from src.main.inference_engine import InferenceEngine

class TestExpertSystem(unittest.TestCase):

    def setUp(self):
        self.kb = KnowledgeBase()
        self.engine = InferenceEngine(self.kb)

    def test_add_fact(self):
        self.kb.add_fact("fact1")
        self.assertIn("fact1", self.kb.get_facts())

    def test_add_rule(self):
        rule = Rule(["cond1"], "conc1")
        self.kb.add_rule(rule)
        self.assertIn(rule, self.kb.get_rules())

    def test_forward_chain(self):
        self.kb.add_fact("A")
        self.kb.add_fact("B")
        self.kb.add_rule(Rule(["A", "B"], "C"))
        self.engine.forward_chain()
        self.assertIn("C", self.kb.get_facts())

    def test_backward_chain(self):
        self.kb.add_fact("A")
        self.kb.add_fact("B")
        self.kb.add_rule(Rule(["A", "B"], "C"))
        self.assertTrue(self.engine.backward_chain("C"))
        self.assertFalse(self.engine.backward_chain("D"))

    def test_conflict_resolution(self):
        rule1 = Rule(["A"], "B", priority=1)
        rule2 = Rule(["A"], "C", priority=2)
        applicable_rules = [rule1, rule2]
        resolved_rules = self.engine.resolve_conflicts(applicable_rules)
        self.assertEqual(resolved_rules, [rule2, rule1])

if __name__ == '__main__':
    unittest.main()
