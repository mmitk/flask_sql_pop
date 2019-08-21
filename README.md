# flask_sql_pop
This is an incomplete personal use extension I have been working on for one of my flask app projects. It works with the "app factory" design, and is intended to populate a specific SQL table (empty) upon app initialization. The table it is currently populating is called dictionary, and has two columns: word, definition.  The extension uses an existing JSON file type object to extract the data with which to populate the table. It seems to have more success with a JSON list than a JSON object, and behaves problematically once more than 50 or so items are being populated. 
The module takes a class based approach in order to support the application factory pattern. 
Another prerequisite is a db.py (or similar code) that has a get_db() function which returns a database connection, as this module does not establish its own connection.
When an instance of the Populate class is created it must be created within app context:
with app.app_context():
        file_path='somefile.json'
        p = Populate.Populate(app,file_path)
All functions from module must be used within this block.
