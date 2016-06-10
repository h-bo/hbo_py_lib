def setparam_class(object, param, namelist, list):
    if len(namelist) != len(list):
        print 'error: list no same length' 
    for i in range(len(list)):
        exec('object.param[namelist[i]] = list[i]')