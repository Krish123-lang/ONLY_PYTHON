# Kwargs are treated as dictionary, so we can access it value using key, value pairs

def hello(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))


hello(first='krishna', mid='is', third='a', fourth='robot')
