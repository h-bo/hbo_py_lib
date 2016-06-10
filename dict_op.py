def sort_dict_by_value(dict):
  """
    return the list with the dict's key
  """
  sorted_keylist = list(sorted(dict, key=dict.__getitem__, reverse=True))
  return sorted_keylist
  
def setparam_dict(dict, list, namelist):
    if len(namelist) != len(list):
        raise ValueError('error: list no same length') 
    else:
        for i in range(len(list)):
            exec('dict[namelist[i]] = list[i]')