from optparse import OptionParser


def run(app):

    parser = OptionParser(usage='usage: %prog [options] ')

    parser.add_option("-H",  "--host",
        default="127.0.0.1",
        type="str",
        dest="host"
    )

    parser.add_option("-D",  "--debug",
        default=True,
        dest="debug"
    )

    parser.add_option("-P",  "--port",
        type="int",
        default=9000,
        dest="port"
    )

    parser.add_option('-E', '--env',
        type='choice',
        action='store',
        dest='environment',
        choices=['PRO', 'QA', 'DEV',],
        default='DEV',
        help='Environment to run on',
    )
    (options, args) = parser.parse_args()
    print(options)

    # app.run(
    #     debug=options.debug,
    #     host=options.host,
    #     port=int(options.port)
    # )
