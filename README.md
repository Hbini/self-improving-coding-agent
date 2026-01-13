# Self-Improving Coding Agent

## Level: Intermediate | Complexity: High | Time: 6 weeks

### Project Overview

Build an autonomous coding agent that writes code, runs tests, and learns from failures through agentic loops. This agent implements a plan → execute → test → reflect cycle, achieving production-grade autonomous code generation and debugging.

### What This Project Proves

✅ **Agentic Loops** - Plan-execute-test-reflect cycle with state management  
✅ **Production Debugging** - Error analysis and hypothesis generation  
✅ **Self-Learning** - Store failures and avoid repeating mistakes  
✅ **Code Safety** - Sandboxing and permission gates  
✅ **Iterative Refinement** - Autonomous code improvement  

---

## Architecture & Key Components

### 1. Execution Loop

**Pattern**: Plan → Execute → Test → Reflect → Learn

```python
class ExecutionLoop:
    def __init__(self, max_iterations=5):
        self.max_iterations = max_iterations
        self.state = {}
        self.failures = []
    
    def run(self, goal: str) -> str:
        """Execute autonomously until goal achieved"""
        for iteration in range(self.max_iterations):
            # Plan: Generate approach
            plan = self.planner.generate_plan(goal, self.state)
            
            # Execute: Write code
            code = self.coder.generate_code(plan)
            
            # Test: Validate
            result, passed = self.executor.run_tests(code)
            
            # Reflect: Analyze
            if passed:
                return code
            
            # Learn: Store failure
            failure_pattern = self.analyzer.extract_pattern(result)
            self.failures.append(failure_pattern)
            
            # Update state for next iteration
            self.state["last_error"] = result
            self.state["attempts"] = iteration + 1
        
        return None  # Max iterations reached
```

### 2. Sandbox Environment

**Isolation Strategy**: Resource-limited execution

```python
class SandboxExecutor:
    def __init__(self, cpu_limit=2, memory_limit_mb=512, timeout_sec=10):
        self.cpu_limit = cpu_limit
        self.memory_limit_mb = memory_limit_mb
        self.timeout_sec = timeout_sec
    
    def execute_safely(self, code: str) -> Tuple[str, bool]:
        """Run code in isolated environment"""
        # Create isolated process with resource limits
        try:
            result = subprocess.run(
                ['python', '-c', code],
                capture_output=True,
                timeout=self.timeout_sec,
                cwd='/tmp/sandbox'  # Restricted directory
            )
            return result.stdout.decode(), result.returncode == 0
        except subprocess.TimeoutExpired:
            return "Timeout: Code exceeded time limit", False
        except Exception as e:
            return str(e), False
```

### 3. Memory Hierarchy

**Three-Level Memory System**:

```python
class MemoryHierarchy:
    def __init__(self):
        self.short_term = deque(maxlen=5)  # Current task (last 5 attempts)
        self.long_term = {}  # Problem patterns → solutions
        self.failure_memory = {}  # Error signatures → fixes
    
    def recall_similar_failures(self, error_signature: str) -> List[dict]:
        """Retrieve similar past failures"""
        return self.failure_memory.get(error_signature, [])
    
    def store_solution(self, problem_type: str, solution: str, success_rate: float):
        """Store proven solution"""
        self.long_term[problem_type] = {
            'solution': solution,
            'success_rate': success_rate,
            'last_used': time.time()
        }
```

### 4. Reflection Mechanism

**Error Analysis & Learning**:

```python
class ReflectionMechanism:
    def __init__(self):
        self.error_patterns = {}
    
    def reflect_on_failure(self, code: str, error: str) -> dict:
        """Analyze why code failed"""
        # Extract error pattern
        pattern = self._extract_error_pattern(error)
        
        # Find root cause
        root_cause = self._identify_root_cause(code, error)
        
        # Generate hypothesis for fix
        hypothesis = self._generate_hypothesis(code, root_cause)
        
        return {
            'pattern': pattern,
            'root_cause': root_cause,
            'hypothesis': hypothesis,
            'suggested_fix': self._suggest_fix(hypothesis)
        }
    
    def _extract_error_pattern(self, error: str) -> str:
        """Normalize error message into pattern"""
        # Convert "NameError: name 'x' is not defined" → "NameError:undefined_variable"
        return re.sub(r'[a-zA-Z0-9_]+', '[VAR]', error)[:50]
```

### 5. Learning from Mistakes

**Pattern-Based Learning**:

```python
class LearningSystem:
    def __init__(self):
        self.mistake_database = {}
    
    def learn_from_mistake(self, code: str, error: str, fix: str):
        """Store failure context for future reference"""
        pattern = self._get_error_pattern(error)
        
        if pattern not in self.mistake_database:
            self.mistake_database[pattern] = []
        
        self.mistake_database[pattern].append({
            'failed_code': code,
            'error': error,
            'fix': fix,
            'timestamp': time.time()
        })
    
    def avoid_similar_mistakes(self, code: str) -> List[str]:
        """Check code against known mistakes"""
        patterns = self._analyze_code_patterns(code)
        warnings = []
        
        for pattern in patterns:
            if pattern in self.mistake_database:
                similar_mistakes = self.mistake_database[pattern]
                warnings.append(f"Warning: Similar pattern caused {len(similar_mistakes)} failures")
        
        return warnings
```

---

## Tech Stack

- **Language**: Python 3.9+
- **Code Generation**: Anthropic Claude or Open-Source LLM
- **Testing**: pytest, unittest
- **Sandboxing**: Docker or subprocess with resource limits
- **Vector DB**: Pinecone or Weaviate (for failure similarity search)
- **Storage**: SQLite (local) or PostgreSQL (production)

---

## Implementation Phases

### Phase 1: Core Loop (Week 1)
- [ ] Implement basic plan-execute-test-reflect loop
- [ ] Setup code generation prompt
- [ ] Create basic test runner

### Phase 2: Safety (Week 2)
- [ ] Build sandbox execution environment
- [ ] Implement resource limits
- [ ] Add permission gates

### Phase 3: Learning (Week 3)
- [ ] Implement failure pattern extraction
- [ ] Create error database
- [ ] Build similarity search for past failures

### Phase 4: Optimization (Week 4-6)
- [ ] Fine-tune prompts based on failure patterns
- [ ] Implement reflection mechanism
- [ ] Add multi-agent coordination

---

## Success Metrics

- **Code Passing Rate**: > 90% (tests pass on first try)
- **Iterations to Success**: < 3 average
- **Execution Safety**: 100% (no crashes/security issues)
- **Learning Efficiency**: Solve similar problems 50% faster after first attempt

---

## Testing Strategy

```bash
# Unit tests
pytest tests/unit/ -v --cov=src/

# Integration tests
pytest tests/integration/ -v

# Safety tests
pytest tests/safety/ -v
```

---

## Resources

- [Anthropic Claude API](https://console.anthropic.com/)
- [OpenAI GPT-4 API](https://openai.com/api/)
- [LangChain Agents](https://python.langchain.com/docs/modules/agents/)
- [Docker Sandboxing](https://docs.docker.com/)
- [Pytest Documentation](https://pytest.org/)

---

## License

MIT - See LICENSE file
