from tasks.task import Task,upgrade_task,purchase_task
from tasks.list.task_purchase import purchase_condition, purchase_reward
from tasks.list.task_upgrade import upgrade_condition, upgrade_reward

class Character:
    def __init__(self):
        self.upgradeCount = 0

    def upgrade(self):
        self.upgradeCount += 1

class Shop:
    def __init__(self):
        self.purchase_records = []

    def purchase(self, item):
        self.purchase_records.append(item)

def main_game_loop():
    character = Character()
    shop = Shop()

    # 主角升級行為，假設升級3次
    for _ in range(3):
        character.upgrade()

    # 商店購買行為，假設購買5次商品
    for _ in range(5):
        shop.purchase("商品")

    # 檢查是否完成任務
    if not upgrade_task.is_completed and upgrade_task.check_condition(character):
        upgrade_task.complete_task()

    if not purchase_task.is_completed and purchase_task.check_condition(shop):
        purchase_task.complete_task()

if __name__ == "__main__":
    from tasks.task import Task,upgrade_task,purchase_task
    from tasks.list.task_purchase import purchase_condition, purchase_reward
    from tasks.list.task_upgrade import upgrade_condition, upgrade_reward

    main_game_loop()
