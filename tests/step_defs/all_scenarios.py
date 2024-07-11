import glob
import os

from resources.utilities import *
from pytest_bdd import scenarios


feature_files = glob.glob(os.path.join(os.path.dirname(__file__), '../features/*.feature'))
for feature_file in feature_files:
    scenarios(feature_file)
