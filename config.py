from decouple import config

URL = 'mongodb+srv://alexrfarnes:{}@cluster0.huwjw09.mongodb.net/?retryWrites=true&w=majority'.format(
    config('MONGODB_PASSWORD', default="password")
)