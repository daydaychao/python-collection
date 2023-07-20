def purchase_condition(shop):
    return len(shop.purchase_records) >= 5

def purchase_reward():
    print("完成購買任務，獎勵道具！")
