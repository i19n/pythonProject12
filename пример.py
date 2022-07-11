class MyManager(object):
    def __init__(self):
        self.resource=42

    def __enter__(self):
        print('Entered contex')
        return self.resource
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Left contex')
        if exc_type:
            print('(Exception occured: {})'.fromat(exc_type))

with MyManager() as resource:
    print('Some actions with resource:', resource)
    raise ValueError
