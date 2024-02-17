def writeData(result, filename):
    try:
        file = open(f'./{filename}', 'a+')
    except:
        raise FileNotFoundError
    
    if result[0][1] == '001':
        file.write('        {}            {}    {}           {}               {}                   {}\n'.format(
        0.01,
        result[1][1],
        result[4][1],
        result[5][1],
        result[6][1],
        result[7][1],
        )
    )
    else:
        file.write('        {}            {}    {}           {}               {}                   {}\n'.format(
            result[0][1],
            result[1][1],
            result[4][1],
            result[5][1],
            result[6][1],
            result[7][1],
            )
        )
    file.close()