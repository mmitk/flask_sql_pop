import json
from flask import request, Flask
############### have to use get_db()
from flaskr.db import get_db
#from . import db

class Populate:
    #add parameter app, for extension use
    def __init__(self, app=None,file_path=None):
        self.app =app
        if app is not None:
            self.init_app(app)
        else:
            self.db=None
    
        self.file = file_path
        self.db = get_db()
        self.data = None
        self.error = None
        

    #add parameter app, for extension use
    def init_app(self,  file_path = None,data_base=None, app=None):
        app.config.setdefault('SQLITE3_DATABASE', ':memory:')
        app.teardown_appcontext(self.teardown)
        db.init_app(app)
        #use get_db() here
        if self.db is None:
            self.db=get_db()
        elif self.file is None:
            self.file = file_path
        self.data=None
        return

    #extracts data from given file path(JSON format)
    def extract(self):
        file_path = self.file
        #db = get_db()
        if file_path is not None:
            with open(file_path, 'r') as f:
                #saves extracted data to self.data for later use
                self.data = json.load(f)
                f.close()
        else:
            self.error="No file path given to populate object"  
        return 


    #populates database
    def popul(self):  
        db = self.db
        #if no data is saved in self.pop, then extract is called with given file path
        if self.data is None:
            if self.file is not None:
                #extract is called with given file path
                self.extract()
                data = self.data
            else:
                #if file path is None and pop_data are none, there is an error
                self.error = "No data or file path for data extraction given"
        
        #if pop_data is not None, file path is ignored (likely None) and data is set to pop_data
        else:
            data = self.data
        
        self.extract()
        data =  self.data
        i = 0
        #if self.error is not None:
        for key in data:
            try:
                word = str(key)
                definition = str(data[key])
            except:
                self.error="something went wrong"
                continue
            db.execute(
                        'INSERT INTO dictionary (word, definition) VALUES (?, ?)',
                        (word, definition)
                    )
            db.commit()
          
            #if db.execute(
             #   'SELECT id FROM dictionary WHERE word = ?', (word,)
             #   ).fetchone() is not None:
             #      error = 'word {} is already registered in dictionary.'.format(word)
            #else:
             #   try:
              #      word = str(key)
            #        definition = str(data[key])
             #   except:
            #        self.error="something went wrong"
            #        continue
             #   else:
               #     db.execute(
              #          'INSERT INTO dictionary (word, definition) VALUES (?, ?)',
               #         (word, definition)
              #      )
               #     db.commit()
            i+=1

        ##############################
        #FOR TESTING
        
        
        #flash(error)
        return i