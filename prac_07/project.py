class Project:
    def __init__(self, name, start_date, priority, estimate, completion_percentage):
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.estimate = estimate
        self.completion_percentage = completion_percentage

    def __str__(self):
        return f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, priority {self.priority}, " \
               f"estimate: ${self.estimate:.2f}, completion: {self.completion_percentage}%"
