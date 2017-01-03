def singeton(cls,*args, **kwargs):
    instance = {}
    def _singeleton():
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]
    return _singeleton()