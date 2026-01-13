agent.py"""Self-Improving Coding Agent implementation."""
import re
from typing import Dict, List, Tuple, Optional
from datetime import datetime


class CodeAnalyzer:
    """Analyze and improve code."""
    
    def __init__(self):
        self.metrics = {"complexity": 0, "efficiency": 0, "readability": 0}
        self.issues = []
    
    def analyze(self, code: str) -> Dict:
        """Analyze code for improvements."""
        lines = code.split('\n')
        self.metrics["complexity"] = len([l for l in lines if 'if' in l or 'for' in l])
        self.metrics["readability"] = len([l for l in lines if l.strip() and not l.strip().startswith('#')])
        return {"metrics": self.metrics, "issues": self.issues}
    
    def suggest_improvements(self, code: str) -> List[str]:
        """Generate improvement suggestions."""
        suggestions = []
        if 'import *' in code:
            suggestions.append("Replace 'import *' with specific imports")
        if '  ' in code:
            suggestions.append("Use consistent indentation")
        if 'TODO' in code or 'FIXME' in code:
            suggestions.append("Address TODO/FIXME comments")
        return suggestions


class CodeOptimizer:
    """Optimize code for better performance."""
    
    @staticmethod
    def optimize_loops(code: str) -> str:
        """Optimize loop structures."""
        # Simple optimization example
        code = re.sub(r'for\s+(\w+)\s+in\s+range\(len\((\w+)\)\)', r'for \1 in \2', code)
        return code
    
    @staticmethod
    def optimize_imports(code: str) -> str:
        """Optimize import statements."""
        lines = code.split('\n')
        imports = []
        other_lines = []
        
        for line in lines:
            if line.startswith('import ') or line.startswith('from '):
                imports.append(line)
            else:
                other_lines.append(line)
        
        imports.sort()
        return '\n'.join(imports + other_lines)


class AgentLearner:
    """Learn from code patterns and improve."""
    
    def __init__(self):
        self.learned_patterns = {}
        self.improvement_history = []
    
    def extract_patterns(self, code: str) -> Dict[str, int]:
        """Extract patterns from code."""
        patterns = {}
        for word in code.split():
            patterns[word] = patterns.get(word, 0) + 1
        return {k: v for k, v in patterns.items() if v > 1}
    
    def log_improvement(self, before: str, after: str, improvement_type: str):
        """Log code improvements."""
        self.improvement_history.append({
            "timestamp": datetime.now().isoformat(),
            "type": improvement_type,
            "before_lines": len(before.split('\n')),
            "after_lines": len(after.split('\n'))
        })
    
    def get_learning_stats(self) -> Dict:
        """Get learning statistics."""
        return {
            "total_improvements": len(self.improvement_history),
            "pattern_count": len(self.learned_patterns),
            "avg_reduction": self._calculate_avg_reduction()
        }
    
    def _calculate_avg_reduction(self) -> float:
        """Calculate average code reduction."""
        if not self.improvement_history:
            return 0.0
        reductions = [h["before_lines"] - h["after_lines"] for h in self.improvement_history]
        return sum(reductions) / len(reductions)


class CodingAgent:
    """Main coding agent for self-improvement."""
    
    def __init__(self):
        self.analyzer = CodeAnalyzer()
        self.optimizer = CodeOptimizer()
        self.learner = AgentLearner()
    
    def improve_code(self, code: str) -> Dict:
        """Improve code through analysis and optimization."""
        original_code = code
        
        # Analyze
        analysis = self.analyzer.analyze(code)
        
        # Suggest improvements
        suggestions = self.analyzer.suggest_improvements(code)
        
        # Optimize
        code = self.optimizer.optimize_loops(code)
        code = self.optimizer.optimize_imports(code)
        
        # Learn
        patterns = self.learner.extract_patterns(code)
        self.learner.log_improvement(original_code, code, "full_improvement")
        
        return {
            "improved_code": code,
            "analysis": analysis,
            "suggestions": suggestions,"""Main entry point for Coding Agent."""
from agent import CodingAgent

def main():
    agent = CodingAgent()
    test_code = '''
def calc(x,y):
    if x>0:
        return x+y
    else:
        return x-y
'''
    result = agent.improve_code(test_code)
    print("Analysis:", result["analysis"])
    print("Suggestions:", result["suggestions"])
    print("Improved Code:", result["improved_code"])
    print("Stats:", agent.get_performance_report())

if __name__ == "__main__":
    main()

            "patterns": patterns,
            "learning_stats": self.learner.get_learning_stats()
        }
    
    def get_performance_report(self) -> Dict:
        """Get agent performance report."""
        return {
            "name": "Self-Improving Coding Agent",
            "version": "0.1.0",
            "capabilities": ["analyze", "optimize", "learn"],
            "learning_stats": self.learner.get_learning_stats()
        }
