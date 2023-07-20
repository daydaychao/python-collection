class Task:
    def __init__(self, task_id, description, condition, reward):
        self.task_id = task_id
        self.description = description
        self.condition = condition
        self.reward = reward
        self.is_completed = False

    def check_condition(self, character):
        return self.condition(character)

    def complete_task(self):
        self.is_completed = True
        self.reward()


def upgrade_condition(character):
    return character.upgradeCount >= 3

def purchase_condition(shop):
    return len(shop.purchase_records) >= 5

def upgrade_reward():
    print("完成升級任務，獎勵金幣！")

def purchase_reward():
    print("完成購買任務，獎勵道具！")

upgrade_task = Task(task_id=1, description="升級主角3次", condition=upgrade_condition, reward=upgrade_reward)
purchase_task = Task(task_id=2, description="購買5次商品", condition=purchase_condition, reward=purchase_reward)
