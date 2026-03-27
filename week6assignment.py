def log_action(func):
    def wrapper(*args, **kwargs):
        print(f"[ACTION] {func.__name__} executed")
        result = func(*args, **kwargs)
        return result
    return wrapper
class Employee:
    _total_employees = 0
    def __init__(self, name, emp_code):
        self.name = name
        self.emp_code = emp_code
        self._tasks = {}
        Employee._total_employees += 1
    @log_action
    def assign_task(self, task_name, score):
        task_name = task_name.upper()
        self._tasks[task_name] = int(score)
        return f"{self.name} assigned {task_name} with score {score}"
    def avg_score(self):
        if not self._tasks:
            return 0.0
        avg = sum(self._tasks.values()) / len(self._tasks)
        return float(round(avg, 1))
    def top_task(self):
        if not self._tasks:
            return "No tasks"
        return max(self._tasks, key=self._tasks.get)
    @classmethod
    def from_record(cls, data):
        name, code = data.split('-')
        return cls(name, code)
    @staticmethod
    def is_valid_code(emp_code):
        return isinstance(emp_code, str) and len(emp_code) == 7 and emp_code.isdigit()
    @classmethod
    def total_employees(cls):
        return cls._total_employees
    
e1 = Employee("Sardor", "3301001")
e1.assign_task("report", 90)
e1.assign_task("analysis", 76)
e1.assign_task("design", 84)

e2 = Employee.from_record("Kamola-3301002")
e2.assign_task("Testing", 88)
e2.assign_task("review", 95)

print(f"{e1.name}: Avg = {e1.avg_score()}, Top = {e1.top_task()}")
print(f"{e2.name}: Avg = {e2.avg_score()}, Top = {e2.top_task()}")

print(f"Valid code '3301001': {Employee.is_valid_code('3301001')}")
print(f"Valid code '33B': {Employee.is_valid_code('33B')}")
print(f"Total employees: {Employee.total_employees()}")
