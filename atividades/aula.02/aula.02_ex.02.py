import pymongo

if __name__ == '__main__':
    client = pymongo.MongoClient('localhost')
    db = client.nosqlclass

#==============================================================================
# Listar as 10 palavras com maior valor no campo total
#==============================================================================

#    cursor = db.vocabulary.find().sort("total", -1).limit(10)

#    for document in cursor:
#        print('_id: ', document['_id'], 'total: ', document['total'])

#==============================================================================
# Encontrar todas as palavras que são usuários do twitter, hashtags, urls
# e adicionar um campo informando o tipo de palavra
#==============================================================================

#    cursor = db.vocabulary.find()

#    for document in cursor:
#        if (str(document['_id'])[0:1] == '@'):
#            db.vocabulary.update({ '_id' : document['_id'] }, { '$set' : { 'word' : 'twitter' } })
#        else:
#            if (str(document['_id'])[0:1] == '#'):
#                db.vocabulary.update({ '_id' : document['_id'] }, { '$set' : { 'word' : 'hashtag' } })
#            else:
#                if (str(document['_id'])[0:4] == 'http'):
#                    db.vocabulary.update({ '_id' : document['_id'] }, { '$set' : { 'word' : 'url' } })
#                else:
#                    db.vocabulary.update({ '_id' : document['_id'] }, { '$set' : { 'word' : 'generic' } })
 
#    cursor = db.vocabulary.find({'word' : 'generic'}).sort("total", -1).limit(10)

#    for document in cursor:
#        print(document)

#==============================================================================
# Conte o total de cada um dos tipos criados
#==============================================================================

    print('twitters..: ', db.vocabulary.find({'word' : 'twitter'}).count())
    print('hashtags..: ', db.vocabulary.find({'word' : 'hashtag'}).count())
    print('urls......: ', db.vocabulary.find({'word' : 'url'}).count())
    print('generics..: ', db.vocabulary.find({'word' : 'generic'}).count())
    print('total.....: ', db.vocabulary.find().count())
