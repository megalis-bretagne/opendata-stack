# *****************************
# Environment specific settings
# *****************************
from celery.schedules import crontab
# DO NOT use "DEBUG = True" in production environments
DEBUG = False

# API SIREN V3
API_SIREN_KEY = 'xxxxxxxxxxxxxxxxx'
API_SIREN_SECRET = 'xxxxxxxxxxxxxxxxxxxx'


SECRET_KEY = "F2EfXdzWCuoSxlLPQdbX6Sx8rLg7cbJGyCDkoApAgajPbfvTgQ"
#je sais pas quoi mettre car champ obligatoire et keycloak est en mode bearer only donc pas besoin de redirection
OIDC_REDIRECT_URI = 'http://localhost:5000'

# SQLAlchemy settings
#BASE DE DONNEE
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://datauser:datapassword@x.x.x.x:3306/data_extraction?charset=utf8'
SQLALCHEMY_TRACK_MODIFICATIONS = False    # Avoids a SQLAlchemy Warning

#URL marque blanche (outil gironde numérique)
URL_PUBLICATION='https://data-preprod.megalis.bretagne.bzh/private/publications/'
DIR_PUBLICATION='/private/publications/'
DIR_ROOT_PUBLICATION='/public'

#URL marque blanche (outil gironde numérique)
URL_MARQUE_BLANCHE='https://data-preprod.megalis.bretagne.bzh/OpenData/'
DIR_MARQUE_BLANCHE='/public/OpenData/'

#info de connexion au serveur BDD ( pour creation des flux ged SFTP dans pastell)
DEPOT_HOSTNAME='x.x.x.x'
DEPOT_USERNAME="megalis"
DEPOT_PASSWORD="passwordOpendaData"
#récupérer la valeur depuis l'ihm pastell dans un connecteur crée unitairement
DEPOT_FINGERPRINT='AAFCBCBFBSSCCE954253702F4EDAF326DA04BCA2'

#Pastell
API_PASTELL_URL='https://pastell-preprod.megalis.bretagne.bzh'
API_PASTELL_VERSION='/api/v2'
API_PASTELL_USER='admin'
API_PASTELL_PASSWORD='xxxxxxxxxx'

#apche solr
USER_SOLR='solr'
PASSWORD_SOLR='xxxxxxx'
URL_SOLR='https://solr-preprod.megalis.bretagne.bzh/solr/'
INDEX_DELIB_SOLR='publication_core'

#watcher
WORKDIR = '/tmp/workdir/'
DIRECTORY_TO_WATCH='/private/watcher/in'
DIRECTORY_TO_WATCH_ARCHIVE='/private/watcher/archives'
DIRECTORY_TO_PUBLICATION='/private/publications'

#UDATA - https://www.data.gouv.fr/fr/
API_UDATA='https://www.data.gouv.fr/api/1'
API_KEY_UDATA = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
# orga megalis
ORG_MEGALIS_UDATA = '534fff8ba3a7292c64a77ed3'
# https://www.data.gouv.fr/fr/datasets/donnees-essentielles-du-profil-acheteur-megalis-bretagne/
DATASET_MARCHE_UDATA = '5f4f4f8910f4b55843deae51'
# https://www.data.gouv.fr/fr/datasets/deliberations-des-collectivites-adherentes-de-megalis-bretagne/
DATASET_DELIB_UDATA = '60645c94e2bfd21cdc16c0be'
# https://www.data.gouv.fr/fr/datasets/budgets-des-collectivites-adherentes-de-megalis-bretagne/
DATASET_BUDGET_UDATA = '60645b816cccca6dab67f532'

#Salle des marches Atexo
URL_JETON_SDM = 'https://xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
URL_API_DECP='https://marches.megalis.bretagne.bzh/app.php/api/v1/donnees-essentielles/contrat/format-pivot'

#CRON
CELERY_CRON = {
}
