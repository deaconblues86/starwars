import requests
import json
from constants import (
    base_url,
    char_endpoint,
    film_endpoint
    )


class BaseSwapi():
    '''
    Base Swapi object containing methods required to support
    required actions
    '''

    @staticmethod
    def get_request(url):
        '''
        Pulls data from requested url
        '''
        r = requests.get(url)
        if r.status_code != 200:
            raise Exception(f"Unable to retrieve data from: {r.url}")
        return r.json()

    @staticmethod
    def clean_refs(ret):
        '''
        Cleans out unwanted cross references
        '''
        return {k: ret[k] for k in ret if not isinstance(ret[k], list) and "https://" not in str(ret[k])}

    def unpack_deets(self):
        '''
        Set object attributes based on returned json
        '''
        for attr in self.details:
            setattr(self, attr, self.details[attr])

    def dump(self):
        '''
        Dumps raw json response
        '''
        return self.details

    def get_cross_ref(self, ref):
        '''
        Replaces requested ref url with actual values
        '''
        if ref not in self.refs:
            raise Exception(f"Invalid Ref: {ref}.  Valid refs are {', '.join(self.refs)}")

        ref_val = getattr(self, ref, None)
        if not ref_val:
            raise Exception(f"Missing Ref in object: {ref}")

        if isinstance(ref_val, list):
            new_val = []
            for ref_url in ref_val:
                ret = self.get_request(ref_url)
                new_val.append(self.clean_refs(ret))
            setattr(self, ref, new_val)
        else:
            r = requests.get(ref_url)
            ret = r.json()
            setattr(self, ref, self.clean_refs(ret))

    def get_all_cross_refs(self):
        '''
        Gets all cross references values for the Object in question
        '''
        for ref in self.refs:
            self.get_cross_ref(ref)


class Character(BaseSwapi):
    '''
    Character object containing character specific details
    - id: character id used in swapi
    '''
    url = base_url + char_endpoint
    refs = ["homeworld", "films", "species", "vehicles", "starships"]

    def __init__(self, char_id):
        self.id = char_id
        self.details = self.get_request(self.url + str(self.id))
        self.unpack_deets()

    def prep_for_db(self):
        '''
        cleans up films attr for db load
        '''
        self.films = '|'.join([f["title"] for f in self.films])
        self.height = str(self.height)


class Film(BaseSwapi):
    '''
    Film object containing methods required to support
    character related actions
    - id: film id used in swapi
    '''
    url = base_url + film_endpoint
    refs = ["characters", "planets", "starships", "vehicles", "species"]

    def __init__(self, film_id):
        self.id = film_id
        self.details = self.get_request(self.url + str(self.id))
        self.unpack_deets()

    def write_contents(self):
        '''
        Returns contents of Film.  This will include cross referenced items if requested
        '''
        contents = vars(self)
        contents = {k: v for k, v in contents.items() if k in self.details}
        return contents
