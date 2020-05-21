from .args import configure, checking_requirements

def main():
    checking_requirements(configure())
    

if __name__ == '__main__':
    main()