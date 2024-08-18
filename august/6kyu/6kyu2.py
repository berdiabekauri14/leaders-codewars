def reverse_alternate(st, *args):
    if st == "":
        return ""
    
    for i in args:
        st[i::-1]
    
    return st