def div(x, y):
    try:
        c = x /y
        return c

    except Exception as e:
        print("błąd: " + str(e))

    except NameError:
        print('NE')

    except (RuntimeError, TypeError, NameError):
        pass

    else:
        print('dunnno')
