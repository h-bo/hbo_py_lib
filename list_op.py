def list_add(l1, l2):
    if len(l1) != len(l2):
        print "error: list not same len"
    else:
        for i in range(len(l1)):
            l1[i] += l2[i]