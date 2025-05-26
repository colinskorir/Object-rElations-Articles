from lib.db.seed import seed_database

def main():
    seed_database()
    import code
    code.interact(local=locals())

if __name__ == "__main__":
    main()
