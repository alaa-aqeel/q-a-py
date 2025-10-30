from src.app import main 
print("Welcome to Q&A CLI!")
try :
    main()
except KeyboardInterrupt:
    print("Goodbye!")
