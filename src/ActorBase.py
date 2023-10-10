class ActorBase:
    def __init__(self):
        # 基础血量（白字）、当前血量(最大值）、当前血量（剩余值）
        self.HP_base = 0.
        self.HP_max = 0.
        self.HP = 0.

        # 基础攻击力（白字）、当前攻击力
        self.ATK_base = 0.
        self.ATK = 0.

        # 基础防御力（白字）、当前防御力
        self.DEF_base = 0.
        self.DEF = 0.

        # 基础速度（白字）、当前速度
        self.SPD_base = 0.
        self.SPD = 0.

        # 攻击属性(0-无，1-物理，2-火，3-冰，4-雷，5-风，6-量子，7-虚数）
        self.property = 0

        # 基础属性增伤(白字），属性增伤（包括全属性增伤），小数，非百分比
        self.damage_increase_base = [0, 0, 0, 0, 0, 0, 0, 0]
        self.damage_increase = [0, 0, 0, 0, 0, 0, 0, 0]

        # 基础属性抗性(白字），属性抗性
        self.damage_resistance_base = [0, 0, 0, 0, 0, 0, 0, 0]
        self.damage_resistance = [0, 0, 0, 0, 0, 0, 0, 0]

        # 减伤，易伤
        self.damage_reduction = 0
        self.damage_vulnerability = 0
