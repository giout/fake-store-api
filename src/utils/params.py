# verify if selecetd query parameters matches with the data type selected (query parameters are str by default)
def param_type(param, data_type):
    if not param:
        return False
    if isinstance(data_type(param), data_type):
        return True
    return False