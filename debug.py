from main import *

if __name__ == '__main__':
    context = ('ssl/local.crt', 'ssl/local.key')
    app.run(port=443, ssl_context=context, debug=True)
