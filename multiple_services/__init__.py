from util.report import app



# ejecuta flask del objeto __init__
def main():
    app.run(port=2323, debug=True)


if __name__ == '__main__':
    main()
