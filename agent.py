
class PersonalAIAgent:
    def __init__(self):
        self.name = "Personal AI Agent"

    def create_plan(self, task):
        return [
            f"Понять задачу: {task}",
            "Разбить задачу на этапы",
            "Определить необходимые инструменты",
            "Выполнить действия",
            "Проверить результат",
            "Подготовить отчёт"
        ]

    def run(self, task):
        plan = self.create_plan(task)

        return {
            "task": task,
            "status": "План подготовлен",
            "steps": plan
        }
