class Task:
    def __init__(
        self,
        title,
        date=None,
        priority="normal",
        category="inne",
        energy_required="medium"
    ):
        self.title = title
        self.date = date
        self.priority = priority
        self.category = category
        self.energy_required = energy_required
        self.completed = False