
import datetime
def shijiancha(times):
    #aa = '2017.01.10'
    data_kaishi = datetime.datetime.strptime(times,'%Y.%m.%d')
    print(data_kaishi)
    today = datetime.datetime.today()
    timedte = (today-data_kaishi).days
    print(timedte)
    return data_kaishi,timedte

class Twopeople:
    def __init__(self,people):
        self.people = people

    # def max_yuqi_qishu(self):
    #     brief_yuqi = self.people['PCO']['PC02']['PC02D']['PC02DH']
    # 贷款最大逾期期数
    # 逾期（透支）汇总信息
    def max_yuqi(self,brief_yuqi):
        list_max_yuqi = [0]
        for jj in brief_yuqi:
            PC02DS04 = float(jj['PC02DS04'])
            list_max_yuqi.append(PC02DS04)
        return list_max_yuqi




    ##6个月贷记卡最大额度使用率
    #for amount in list_current_overdue_amount:
        # list_rate = []
    def rates(self,amount):
        # rate = -999
        PD01AD01 = amount['PD01A']['PD01AD01']
        # PD01BD01 = amount['PD01B']['PD01BD01']
        if PD01AD01 in[ '贷记卡账户',"准贷记卡账户"]:
            ## 总额度
            rate = -999
            PD01AJ02 = float(amount['PD01A']['PD01AJ02'].replace(',', ''))
            ##以使用额度
            used_money= 0
            # PD01BD01的键存在说明账号不是正常账号
            if 'PD01BD01' in amount['PD01B'].keys():
                rate = -99
            else:
                # 如果PD01BJ01键存在说明最新的表现信息段有
                if "PD01BJ01" in amount['PD01B'].keys():
                    ###余额
                    PD01BJ01 = float(amount['PD01B']['PD01BJ01'].replace(',', ''))
                    PD01BJ01_used = PD01AJ02 - PD01BJ01
                    rate = PD01BJ01_used / PD01AJ02
                    used_money = PD01BJ01_used
                    print('rrrr', rate)
                else:
                    PD01CD01 = amount['PD01C']['PD01CD01']
                    if PD01CD01 == "正常":
                        ###余额
                        PD01CJ01 = float(amount['PD01C']['PD01CJ01'].replace(',', ''))
                        PD01CJ01_used = PD01AJ02 - PD01CJ01
                        rate = PD01CJ01_used / PD01AJ02
                        used_money = PD01CJ01_used
                        print('eeeeeeee', rate)
                    else:
                        print('www')

            print(rate)
            return used_money, rate
        else:
            rate = 0
            used_money = 0
            return used_money,rate
    # 11,求近12个月贷款当前逾期总金额。6个月贷款当前逾期最大金额,贷款总逾期次数,6个月贷记卡最大额度使用率
    def list_yuqi_12(self,amount, timedte):
        list_currentOverdueAmount_6 = [0]
        list_yuqu_12 = [0]
        list_rate_xinyongka = []
        loan_overdue_num = []
        #for amount in list_current_overdue_amount:
        PD01AD01 = amount['PD01A']['PD01AD01']
        PD01AR01 = amount['PD01A']['PD01AR01']

        ###这是逾期
        if "PD01C" in amount.keys():
            PD01C = amount['PD01C']
            ##逾期的次数
            PD01CD01 = PD01C['PD01CD01']
            #loan_overdue_num.append(PD01CD01)
            if PD01CD01 == "逾期":
                if timedte <= 182:
                    ##当前逾期总额
                    PD01CJ06_6 = PD01C['PD01CJ06']
                    #list_currentOverdueAmount_6.append(PD01CJ06_6)
                if timedte <= 365:
                    PD01CJ06_12 = PD01C['PD01CJ06']
                    #list_yuqu_12.append(PD01CJ06_12)
            return PD01CD01,PD01CJ06_6, PD01CJ06_12

    list_current_overdue_amount = people['PDA']['PD01']

    ##3个月贷款笔数,
    def debat_three(self,amount, timedte):
        list_debate_3 = []
        # for amount in list_current_overdue_amount:
        PD01AD01 = amount['PD01A']['PD01AD01']
        if PD01AD01 in ['非循环贷账户', '循环额度下分账户', '循环贷账户']:
            if timedte < 90:
                PD01A = amount['PD01A']
                PD01CD01 = PD01A['PD01AI01']
                list_debate_3.append(PD01CD01)
        return list_debate_3

    # 6个月平均使用额度的总和
    card_6month_average_amount_debat = float(people['PCO']['PC02']['PC02H']['PC02HJ05'].replace(',', ''))
    #
    card_6month_average_amount_zhundaijika = float(people['PCO']['PC02']['PC02I']['PC02IJ05'].replace(',', ''))

    ##信用卡审批查询次数
    chaxun = people['PQO']['PC05']['PC05B']

    def chanxuns(self,chaxun):
        # 最近1个月内的查询机构数（信用卡审批）
        PC05BS02 = chaxun['PC05BS02']
        # 最近1个月内的查询次数(贷款)
        PC05BS03 = chaxun['PC05BS03']
        return PC05BS02, PC05BS03

    ###逾期期数
    def yuqi_shi(self,amount):

        if 'PD01C' in amount.keys():
            # list_max_yuqi = []

            yuqi = ['PD01CJ06', 'PD01CJ07', 'PD01CJ08', 'PD01CJ09', 'PD01CJ10']
            # list_dicts = list(list_current_overdue_amount[15]['PD01C'].keys())
            list_dicts = list(amount['PD01C'].keys())
            mingzhongyuqi = [x for x in list_dicts if x in yuqi]
            if len(mingzhongyuqi) > 0:
                max_yuqishijian = mingzhongyuqi[-1]
            else:
                max_yuqishijian = 0
            return max_yuqishijian
        else:
            max_yuqishijian = 0
            return max_yuqishijian

    ###贷款当前的具体数据
    def now_yuqi(self,amount,timedate):
        list_status= []
        if "PD01E" in amount.keys():
            PD01EH = amount['PD01E']['PD01EH']
            for ii in PD01EH:
                D01ED01 = ii["D01ED01"]
                list_status.append(D01ED01)

