"""algorithm for scoring compatibility between two individual profiles. It can be used 2 times separately of the info for emotions of pictures and of interests of picture.

- Input: two dictionaries such that we have each pair { tag: number of pics with tags }
- output: A number between 0 and 100 rounded to nearest integer.

We will change the dictionaries such that we divide by the total number of pics (or whether we decide to not use all of the pictures, i.e. need a set number of 100 (maybe picked by some interval as to not cluster summer pictures of whatever)). Will need to decide what pictures to remove and not, possibly such that if the percentage 'p' of a tag is greater than (1/#oftags) then we leave the tag out."""

class algorithm():

    def __init__(self):
        pass

    def json2dic(self, json):
        """method to extract a dictionary with the (key:value) pair such that for a json file, we either form a new pair if the tag is not in the dictionary, or if it is in, we just ++1 the count of the tag (the value of the tag) if p > (1/#tagsinpicture)"""

        D = json['meta']['results'][0]['result']['tag']

        #tags
        tags = D['classes']
        probs = D['probs']

        dic = {}

        for i in range(len(tags)):
            dic[tags[i]] = probs[i]

        return dic

    def normalise_dic(self, dic):
        """method for making the values in the dictionary into probabilities rather than counters so that people with different number of pictures may be fairly compared."""
        sum = 0
        for key in dic:
            sum += dic[key]
        for key in dic:
            dic[key] = float(dic[key])/float(sum)

        return dic

    def get_union_keys(self, dic1, dic2):
        """getting the intersection of keys of dictionary1 and dictionary2, give back as a list"""
        keys1 = set(dic1.keys())
        keys2 = set(dic2.keys())
        union = keys1 | keys2
        return list(union)

    def get_score(self, dic1, dic2):
        """we get the score by calculating the average (or weighted average) of the distance of the probabilities in the intersection of tags in each new normalised intersection dictionary for each individual.!"""
        sum = 0
        l = len(dic1)
        k = 0.5 # the factor which penalises outliers
        for key in dic1:
            sum += abs(float(dic1[key]) - float(dic2[key]))**(k)

        score = int(100.0*(1-float(sum)/float(l)))

        return score

    def get_score_raw(self, dic1, dic2):
        A = self.normalise_dic(dic1)
        B = self.normalise_dic(dic2)

        keys = self.get_union_keys(A, B)

        for key in keys:
            if key not in A:
                A[key] = 0
            if key not in B:
                B[key] = 0

        return self.get_score(A, B)


    test = {'meta': {'tag': {'config': 'cf0267260d65c1312cac67ab2474dbdc',
    'model': 'default',
    'status_code': 'OK',
    'timestamp': 1414364476.483851}},
    'results': [{'docid': 15512461224882631443L,
    'local_id': '',
    'result': {'tag': {'classes': ['train',
      'subway',
      'railroad',
      'railway',
      'station',
      'rail',
      'transportation',
      'urban',
      'underground',
      'night',
      'traffic',
      'commuter',
      'bridge',
      'city',
      'road',
      'national park',
      'public',
      'platform',
      'street',
      'blur'],
      'probs': [0.1910400390625,
      0.10223388671875,
      0.09765625,
      0.093994140625,
      0.06884765625,
      0.0295257568359375,
      0.0292816162109375,
      0.0219879150390625,
      0.0218353271484375,
      0.0210418701171875,
      0.016265869140625,
      0.0162506103515625,
      0.013763427734375,
      0.01277923583984375,
      0.012603759765625,
      0.0120697021484375,
      0.01134490966796875,
      0.010833740234375,
      0.0102691650390625,
      0.00933837890625]}},
     'status_code': 'OK',
     'status_msg': 'OK'}],
   'status_code': 'OK',
   'status_msg': 'All data in request have completed sucessfully. '}
