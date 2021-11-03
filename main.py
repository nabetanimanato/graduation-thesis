import numpy as np
import random

# 問題の設定
PROCESS_MIN = 1 # 加工時間の最小
PROCESS_MAX = 10 # 加工時間の最大
JOB = 20 # ジョブの個数
WORKER = 3 # 作業員の人数
PATTERN = 3 # 部品タイプの数
MACHINE = 6
MACHINE_SELECTION = {1:[1,2],2:[3,4],3:[5,6]} # タイプから担当機械を選択する辞書を作成

class SimpleGA:
    def __init__(self):
        self.N = 100 # 個体数
        self.ITERATION = 100 # 世代数
        self._initialize()

    def _initialize(self):
        self.pool = [Chromosome() for i in range(self.N)]

    def _mutateAll(self): # 突然変異
        pass

    def _Selction(): # 選択
        pass

    def evolve(self):
        for i in range(self.ITERATION):
            self._Selction()
            self._mutateAll()
            pass

class Chromosome:
    def __init__(self):
        self.array_process_time = np.random.randint(PROCESS_MIN,PROCESS_MAX,(JOB,1)) # ジョブごとの作業時間の生成
        self.array_worker = np.random.randint(1,WORKER+1,(JOB,1)) # ジョブごとの担当作業者の決定
        self.machine_pattern = np.random.randint(1,PATTERN+1,(JOB,1)) # 部品タイプの決定
        # 部品タイプから担当できる機械を選択
        self.selected_machine = []
        for i in range(JOB):
            self.machine_dict = self.machine_pattern[i]
            self.machine_list = MACHINE_SELECTION[self.machine_dict[0]]
            self.sample = random.randint(min(self.machine_list),max(self.machine_list))
            self.selected_machine.append(self.sample)
        self.array_selected_machine = np.array(self.selected_machine).reshape(JOB,1)
        self.gene = np.concatenate([self.array_process_time,self.array_worker,self.array_selected_machine],axis = 1)
        # ,self.array_order
        # self.MUTATION_RATE = 0.05 # 突然変異率

    def mutate(self):
        pass

    def getVal(self): # 遺伝子型から表現型への発現
        # net_work_timeの関数を作成
        pass
    def net_work_time(self,process_time,worker): # 正味作業時間の計算（段取り時間×作業者の技能度）
        # 辞書型で、作業者と機械の技能係数を設定する?
        pass

    def getFitness(self): # 適応度評価
        pass