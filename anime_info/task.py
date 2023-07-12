from celery import shared_task

@shared_task
def tarea_larga():
    for i in range(10):
        print(f"anime {i}")
        time.sleep(1)
    print("Termine")

