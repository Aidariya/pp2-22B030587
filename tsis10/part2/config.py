from configparser import ConfigParser


def config(filename=r'C:\Users\Aidariya1\Desktop\pp2-22B030587\tsis10\part2\database.ini', section='postgresql'):
    # create a parser
    #c:\Users\Aidariya1\Desktop\pp2-22B030587\tsis10\part2\database.ini
    parser = ConfigParser()
    # read config file
    parser.read(filename)

    # get section, default to postgresql
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception(f'Section {section} not found in the {filename} file')

    return db