import string
def calculate(expression,val_type):
    # Принимает на вход список из строк с числами и операторами,
    # целое число, которое определяет тип чисел
    # производит вычисления согласно всем правилам математических операций
    # Возвращает ответ результатов вычисления в строковом типе
    if len(expression)==1:return expression
    else:
        up_bakets_positions=[index for index,item in enumerate(expression) if item=="("]
        down_brackets_positions=[index for index,item in enumerate(expression) if item==")"]
        
        if len(up_bakets_positions)!=len(down_brackets_positions):
            return 'Некорректное выражение, количество открывающих скобок и закрывающих не совпадает'
        if len(up_bakets_positions)>0:
            return calculate(expression[0:up_bakets_positions[0]]+calculate(expression[up_bakets_positions[0]+1:down_brackets_positions[-1]],val_type)+expression[down_brackets_positions[-1]+1:],val_type)
        else:
            while len(expression)>1:
                result=[' ']
                exp_ind=1
                try:
                    mult_ind=expression.index('*')
                    exp_ind=mult_ind
                except:
                    mult_ind=-1
                try:
                    dev_ind=expression.index('/')
                    if dev_ind<mult_ind:exp_ind=dev_ind
                except:
                    dev_ind=-1
                expression[exp_ind]=operate(complex(expression[exp_ind-1]),complex(expression[exp_ind+1]),expression[exp_ind])
                expression=expression[0:exp_ind-1]+expression[exp_ind:exp_ind+1:]+expression[exp_ind+2::]
                result[0]= expression[0]
            if val_type=='2': result[0] = str(float((str(result[0])[1:].split('+'))[0]))
        return result

def operate(digit1: complex,digit2:complex, oper:str):
        if oper=='+':
            return digit1+digit2
        if oper=='-':
            return digit1-digit2
        if oper=='*':
            return digit1*digit2
        if oper=='/':
            return digit1/digit2