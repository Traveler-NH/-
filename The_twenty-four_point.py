def get_dict(_list):
    return {'0':'(', '1':_list[0], '2':_list[1], '3':_list[2], '4':_list[3], '5':'+', '6':'-', '7':'*', '8':'/', '9':')'}

dictionary = get_dict([input('请输入第一张牌的点数：'), input('请输入第二张牌的点数：'), input('请输入第三张牌的点数：'), input('请输入第四张牌的点数：')])
print('计算中，请稍等······')

def calculate_num(num):
    num = str(num)
    length = len(num)
    formula=''
    count = 0
    for count in list(range(0, length)):
        try:
            formula = formula + dictionary[num[count]]
        except KeyError:
            pass
    try:
        try:
            try:
                return eval(formula), formula
            except ZeroDivisionError:
                pass
        except OverflowError:
            pass
    except SyntaxError:
        pass

def filter_formula(formula_num):
    formula_num = str(formula_num).replace('0', '')
    formula_num = str(formula_num).replace('9', '')
    if len(formula_num) == 7:
        if formula_num[1] in '5678':
            if formula_num[3] in '5678':
                if formula_num[5] in '5678':
                    formula_num = formula_num.replace('5', '')
                    formula_num = formula_num.replace('6', '')
                    formula_num = formula_num.replace('7', '')
                    formula_num = formula_num.replace('8', '')
                    if len(formula_num) == 4:
                        formula_num = formula_num.replace('1', '', 1)
                        formula_num = formula_num.replace('2', '', 1)
                        formula_num = formula_num.replace('3', '', 1)
                        formula_num = formula_num.replace('4', '', 1)
                        if len(formula_num) == 0:
                            return True
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False

number = 1515150
while True:
    number = number + 1
    if number == 484848410:
        print('此组合无解')
        input('按下回车键退出程序')
        exit()
    try:
        if filter_formula(number) == True:
            if calculate_num(number)[0] == 24:
                print('算式：', calculate_num(number)[1])
                input('按下回车键退出程序')
                exit()
    except TypeError:
        pass
