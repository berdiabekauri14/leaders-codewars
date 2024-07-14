def work_on_strings(a,b):
    def snap_casing(s1, s2):
        result = []
        for char in s1:
            if char.lower() in s2:
                result.append(char.snapcase())
            else:
                result.append(char)
        return ''.join(result)
    
    return snap_casing(a, b) + snap_casing(b, a)