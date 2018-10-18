from django.db import models

import json
import requests
import random

class Taco(models.Model):
    shell = models.CharField(max_length=200)
    base_layer = models.CharField(max_length=2000)
    mixin = models.CharField(max_length=2000)
    condiment = models.CharField(max_length=2000)
    seasoning = models.CharField(max_length=2000)

    api_link = r'https://tacos-ocecwkpxeq.now.sh'
    api_links = {
        'shell':r'/shells',
        'base_layer':r'/baseLayers',
        'mixin':r'/mixins',
        'condiment':r'/condiments',
        'seasoning':r'/seasonings'
    }

    @classmethod
    def get_options(cls):
        options = {}
        for i in Taco.api_links:
            link = Taco.api_link + Taco.api_links[i]
            aux = json.loads(requests.get(link).text)
            aux = [(x['name'], x['name']) for x in aux]
            options[i] = aux
        return options

    @classmethod
    def create(cls, shell, base_layer, mixin, condiment, seasoning):
        shell = shell
        base_layer = json.dumps(base_layer)
        mixin = json.dumps(mixin)
        condiment = json.dumps(condiment)
        seasoning = json.dumps(seasoning)
        return Taco(shell=shell, base_layer=base_layer, mixin=mixin,
                    condiment=condiment, seasoning=seasoning)

    @classmethod
    def create_random(cls):
        options = Taco.get_options()
        shell = random.choice(options['shell'])[1]
        base_layer = [random.choice(options['base_layer'])[1]]
        mixin = [random.choice(options['mixin'])[1]]
        condiment = [random.choice(options['condiment'])[1]]
        seasoning = [random.choice(options['seasoning'])[1]]
        return Taco.create(shell, base_layer, mixin, condiment, seasoning)

    def __str__(self):
        base_layer = ', '.join(json.loads(self.base_layer))
        mixin = ', '.join(json.loads(self.mixin))
        condiment = ', '.join(json.loads(self.condiment))
        seasoning = ', '.join(json.loads(self.seasoning))
        result = 'A taco made using {} as a shell, {} for its base layer, ' \
                 '{} mixins, {} condiments and {} seasonings'\
                .format(self.shell, base_layer, mixin, condiment, seasoning)
        return  result