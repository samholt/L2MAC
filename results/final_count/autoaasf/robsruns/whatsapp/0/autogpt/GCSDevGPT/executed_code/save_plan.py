def create_plan():
    return 'Detailed Plan for GCS'

plan = create_plan()
with open('plan.txt', 'w') as f:
    f.write(plan)