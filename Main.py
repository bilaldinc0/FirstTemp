import sys
import re
import operator

args = sys.argv


def main():
    f = open(args[1], 'r')
    lines = f.readlines()
    f.close()

    type1w = 0;
    type2w = 0;
    outputs = []
    warnings = {}

    j = 0
    k = 0
    for i in lines:
        j = j + 1
        if 'warning:' in i:
            outputs.append(i)
            type1w = type1w + 1
            searchobj = re.search(r'\[.*\]', i, re.M | re.I)

            if searchobj:
                if searchobj.group() in warnings:
                    warnings[searchobj.group()] = warnings[searchobj.group()] + 1;
                else:
                    warnings[searchobj.group()] = 1
            else:
                print(str(j) + ' line with warning but not [...] in line ')
                k = k + 1

        # if 'WARNING' in i:
        #     outputs.append(i)
        #     type2w = type2w + 1
        #     searchobj = re.search(r'WARNING\(.*\)', i, re.M | re.I)
        #
        #     if searchobj:
        #         if searchobj.group() in warnings:
        #             warnings[searchobj.group()] = warnings[searchobj.group()] + 1;
        #         else:
        #             warnings[searchobj.group()] = 1
        #     else:
        #         print(str(j) + ' line with warning but not (...) in line ')
        #         k = k + 1

    print('number of above list ' + str(k))
    f = open("Lines_with_warning_2.txt", 'w')
    for i in outputs:
        f.write(i)
    f.close()


    sorted_x = sorted(warnings.items(), key = operator.itemgetter(1), reverse = True) #i dont know how it works
    f = open("Warnings_types_2.txt", 'w')
    for i in sorted_x:
        f.write('occurrence : ' + str(i[1]) + '    type : ' + i[0] + '\n')
    f.close()

    # f = open("pout2.txt", 'w')
    # for i in warnings:
    #     f.write('occurrence : ' + str(warnings[i]) + '\ttype : ' + i + '\n')
    # f.close()

    print("t1:" + str(type1w) + "\nt2:" + str(type2w))
    print("DONE!")



main()
