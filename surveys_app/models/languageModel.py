from surveys_app.config.mysqlconnection import connectToMySQL

class Language:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM languages;"
        results = connectToMySQL('dojo_survey_schema').query_db(query)

        languages = []

        for language in results:
            languages.append(cls(language))

        return languages