def writeData(result, filename):
    try:
        file = open(f'./{filename}', 'a+')
    except:
        raise FileNotFoundError

    file.write('        {}            {}    {}           {}               {}                   {}                {}             {}           {}                  {}\n'.format(
        result[0][1],
        result[1][1],
        result[4][1],
        result[5][1],
        result[6][1],
        result[7][1],
        result[8][1],
        result[9][1],
        result[10][1],
        result[11][1])
    )
    file.close()