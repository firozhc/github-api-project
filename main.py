from repository import Repository


def main():

	username =  "emperorscourge@gmail.com"

	password = "Apple_123"

	repo = Repository(username, password)


	repo.create_repository("miscellaneous-python-programs")

	repo.list_repositories()

	#repo.delete_repository("animated-broccoli")




if __name__=="__main__":
	main()