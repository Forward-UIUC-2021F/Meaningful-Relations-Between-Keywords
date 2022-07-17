import sys
sys.path.append('..')

from website_db_connect import db

import FindRelationship
from main import PAPERS_FILE, PAPERS_LEMMA_FILE

import json


if __name__ == '__main__':
    cur = db.cursor()

    keyword = "data mining"
    q_keyword = "b-tree"
    res = FindRelationship.FindRelationshipModifiedJson(keyword, q_keyword, PAPERS_FILE, PAPERS_LEMMA_FILE)

    print(json.dumps(res, indent=4))
