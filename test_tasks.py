from src.services.task_storage import save_tasks, load_tasks


tasks = [
    {
        "title": "Umyć auto",
        "priority": "normal"
    }
]


save_tasks(tasks)

print(load_tasks())