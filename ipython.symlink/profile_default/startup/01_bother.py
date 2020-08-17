from dotenv import load_dotenv
import sys
load_dotenv('/Users/pete/coding/bother-brain/.env')
sys.path.append('/Users/pete/coding/bother-brain/src')
from botherbrain.data_manager import DataManager

dm = DataManager('ipython')

