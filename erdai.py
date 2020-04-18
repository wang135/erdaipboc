# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 13:18:20 2020

@author: Administrator
"""

# 贷款最大逾期期数
# 逾期（透支）汇总信息
brief_yuqi = people['PCO']['PC02']['PC02D']['PC02DH']


def max_yuqi(brief_yuqi):
    list_max_yuqi = [0]
    for jj in brief_yuqi:
        PC02DS04 = float(jj['PC02DS04'])
        list_max_yuqi.append(PC02DS04)
    return list_max_yuqi


# 11,求近12个月贷款当前逾期总金额。6个月贷款当前逾期最大金额,贷款总逾期次数
def list_yuqi_12(list_current_overdue_amount, timedte):
    list_currentOverdueAmount_6 = [0]
    list_yuqu_12 = [0]
    list_rate_xinyongka = []
    loan_overdue_num = []
    for amount in list_current_overdue_amount:
        PD01AD01 = amount['PD01A']['PD01AD01']
        if PD01AD01 in ['贷记卡账户', '准贷记卡账户']:
            ## 总额度
            PD01AJ02 = flaot(amount['PD01A']['PD01AJ02'].replace(',', ''))
            # 使用余额
            try:
                PD01BJ01 = PD01AJ02 - flaot(amount['PD01B']['PD01BJ01'].replace(',', ''))
            except:
                PD01BJ01 = -99
            rate = PD01BJ01 / PD01AJ02
            list_rate_xinyongka.append(rate)
        ###这是逾期
        if "PD01C" in amount.keys():
            PD01C = amount['PD01C']
            PD01CD01 = PD01C['PD01CD01']
            loan_overdue_num.append(PD01CD01)
            if PD01CD01 == "逾期":
                if timedte <= 182:
                    PD01CJ06_6 = PD01C['PD01CJ06']
                    list_currentOverdueAmount_6.append(PD01CJ06_6)
                if timedte <= 365:
                    PD01CJ06_12 = PD01C['PD01CJ06']
                    list_yuqu_12.append(PD01CJ06_12)
        return list_currentOverdueAmount_6, list_yuqu_12


##3个月贷款笔数,
list_current_overdue_amount = people['PDA']['PD01']


def debat_three(list_current_overdue_amount, timedte):
    list_debate_3 = []
    for amount in list_current_overdue_amount:
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

##贷记卡使用额度
PC02HJ04 = people['PCO']['PC02']['PC02H']['PC02DH']['PC02HJ04']

# 贷款余额占总金额比率(PC02E 		非循环贷账户汇总信息段
#		PC02F 		循环额度下分账户汇总信息段
#		PC02G 		循环贷账户汇总信息段)
##1，非循环贷账户汇总信息段
PC02E = people['PCO']['PC02']['PC02E']
# 授信总额
PC02EJ01 = PC02E['PC02EJ01']
# 授信余额
PC02EJ02 = PC02E['PC02EJ02']
##2，循环额度下分账户汇总信息段
PC02F = people['PCO']['PC02']['PC02F']
# 授信总额
PC02FJ01 = PC02F['PC02FJ01']
# 授信余额
PC02FJ02 = PC02F['PC02FJ02']

## 3，循环贷账户汇总信息段
PC02G = people['PCO']['PC02']['PC02G']
# 授信总额
PC02GJ01 = PC02G['PC02GJ01']
# 授信余额
PC02GJ02 = PC02G['PC02GJ02']

####贷记卡最大逾期期数


PC05BS01
最近1个月内的查询机构数（贷款审批
PC05
查询记录概要信息单元
PC05BS02
最近1个月内的查询机构数（信用卡审批）
PC05
查询记录概要信息单元
PC05BS03
最近1个月内的查询次数（贷款审批）
PC05
查询记录概要信息单元
PC05BS04
最近1个月内的查询次数（信用卡审批）
PC05
查询记录概要信息单元
PC05BS05
最近1个月内的查询次数（本人查询）
PC05
查询记录概要信息单元
PC05BS06
最近2年内的查询次数（贷后管理）
PC05
查询记录概要信息单元
PC05BS07
最近2年内的查询次数（担保资格审查）
PC05
查询记录概要信息单元
PC05BS08
最近2年内的查询次数（特约商户实名审查）
##信用卡审批查询次数
chaxun = people['PQO']['PC05']['PC05B']


def chanxuns(chaxun):
    # 最近1个月内的查询机构数（信用卡审批）
    PC05BS02 = chaxun['PC05BS02']
    # 最近1个月内的查询次数(贷款)
    PC05BS03 = chanxun['PC05BS03']
    return PC05BS02, PC05BS03


##贷款总逾期次数
def