# coding=utf-8


def orderretrun(cases, new, old):
    print('入参序号--->', new, type(new), old, type(old))
    temp_new = cases[new].serial_num
    # temp_old = cases[old].serial_num
    for i in range(len(cases)):
        case = cases[i]
        try:
            if new < old:
                if new <= i < old:
                    case.serial_num = int(case.serial_num) + 1
                    case.save()
                if i == old:
                    case.serial_num = str(temp_new)
                    case.save()
            else:
                if old < i <= new:
                    case.serial_num = int(case.serial_num) - 1
                    case.save()
                if i == old:
                    case.serial_num = temp_new
                    case.save()
        except Exception as e:
            print('序号处理错误：', e)

if __name__=='main':
    cases=''
    new=0
    old=11
    order_return = orderretrun(cases, new, old)