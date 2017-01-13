# -*- coding: utf-8 -*-

from imio.urban.dataimport.mapping import table

VALUES_MAPS = {

'type_map': table({
'header'  : ['portal_type',         'foldercategory', 'abreviation'],
'B'       : ['BuildLicence',        'uap',            'BL'],
'L'       : ['ParcelOutLicence',    '',               'PL'],
'D'       : ['Declaration',         '',               'DU'],
}),


'eventtype_id_map': table({
'header'             : ['decision_event'],
'BuildLicence'       : ['delivrance-du-permis-octroi-ou-refus'],
'ParcelOutLicence'   : ['delivrance-du-permis-octroi-ou-refus'],
'Declaration'        : ['deliberation-college'],
'UrbanCertificateOne': ['octroi-cu1'],
'UrbanCertificateTwo': ['octroi-cu2'],
'MiscDemand'         : ['deliberation-college'],
'EnvClassOne'        : ['decision'],
'EnvClassTwo'        : ['decision'],
'EnvClassThree'      : ['acceptation-de-la-demande'],
}),

'documents_map': {
    'BuildLicence': 'URBA',
    'UniqueLicence': 'PERMIS-UNIQUE',
    'ParcelOutLicence': 'LOTISSEMENT',
    'Declaration': 'REGISTRE-PU',
    'UrbanCertificateOne': 'CU/1',
    'UrbanCertificateTwo': 'CU/2',
    'MiscDemand': 'AUTRE DOSSIER',
    'EnvClassOne': 'ENVIRONNEMENT',
    'EnvClassTwo': 'ENVIRONNEMENT',
    'EnvClassThree': 'ENVIRONNEMENT',
},

'titre_map': {
    'monsieur': 'mister',
    'messieurs': 'misters',
    'madame': 'madam',
    'mesdames': 'ladies',
    'mademoiselle': 'miss',
    'monsieur et madame': 'madam_and_mister',
},

'externaldecisions_map': {
    'F': 'favorable',
    'FC': 'favorable-conditionnel',
    'D': 'defavorable',
    'RF': 'favorable-defaut',
},
}
