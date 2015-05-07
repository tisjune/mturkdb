from models import User
from mturkdb import lm

@lm.user_loader
def load_user(id):
	return User.query.get(id)