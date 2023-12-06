class MyError(Exception):
    def __str__(self):
        return 'Натворил делов'

raise MyError()
