def cat_builder(n, c, t):
    cat_dict = {}
    cat_dict["name"] = n
    cat_dict["color"] = c
    cat_dict["toys"] = t

    return cat_dict


print(cat_builder("nova", "black", ["cat","cat","cat"]))